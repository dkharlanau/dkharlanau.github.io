(() => {
  const form = document.getElementById('ams-cost-inputs');
  const results = document.getElementById('ams-cost-results');
  if (!form || !results) return;

  const money = new Intl.NumberFormat('en-US', {style: 'currency', currency: 'USD'});
  const whole = new Intl.NumberFormat('en-US');
  // The inputs allow hundredths of a minute, a dollar, and a percent.
  // Keep fractional cents exact until display or the break-even ceiling.
  const unitsPerCent = 60n * 100n * 10000n;
  const formatCost = (cost, requestCount = 1n) => {
    const divisor = unitsPerCent * requestCount;
    const cents = (cost + divisor / 2n) / divisor;
    const fraction = (cents % 100n).toString().padStart(2, '0');
    return money.formatToParts(cents / 100n)
      .map(part => part.type === 'fraction' ? fraction : part.value)
      .join('');
  };
  const set = (key, value) => {
    results.querySelector('[data-cost-result="' + key + '"]').textContent = value;
  };

  form.addEventListener('submit', event => {
    event.preventDefault();
    if (!form.reportValidity()) return;

    const read = name => form.elements.namedItem(name).valueAsNumber;
    const hundredths = name => BigInt(Math.round(read(name) * 100));
    const years = BigInt(form.elements.namedItem('years').value);
    const requestCount = BigInt(read('volume')) * years;
    const hourly = hundredths('hourly');
    const fixed = (hundredths('setup') + years * hundredths('annual')) * unitsPerCent;
    const manualUnit = hundredths('manualMinutes') * hourly * 10000n;
    const exceptionUnit = hundredths('exceptionRate') * hundredths('exceptionMinutes') * hourly;
    const variableUnit = hundredths('usageUnit') * unitsPerCent + exceptionUnit;
    const manualTotal = requestCount * manualUnit;
    const automatedTotal = fixed + requestCount * variableUnit;
    const delta = manualTotal - automatedTotal;
    const absoluteDifference = delta < 0n ? -delta : delta;
    const marginPerAnnualRequest = years * (manualUnit - variableUnit);

    set('period', years === 1n ? '1 year' : years + ' years');
    set('manual', formatCost(manualTotal) + ' total · ' + formatCost(manualUnit) + ' per request');
    set('automated', formatCost(automatedTotal) + ' total · ' + formatCost(automatedTotal, requestCount) + ' per request');
    if (delta === 0n) {
      set('difference', 'Equal cost');
    } else {
      const direction = delta < 0n ? ' higher with automation' : ' lower with automation';
      const amount = absoluteDifference * 2n < unitsPerCent ? 'Less than $0.01' : formatCost(absoluteDifference);
      set('difference', amount + direction);
    }
    if (marginPerAnnualRequest > 0n) {
      const threshold = (fixed + marginPerAnnualRequest - 1n) / marginPerAnnualRequest;
      set('breakEven', threshold > 1n ? whole.format(threshold) + ' requests per year' : '1 request per year');
    } else if (marginPerAnnualRequest === 0n && fixed === 0n) {
      set('breakEven', 'Equal cost at every volume');
    } else {
      set('breakEven', 'No break-even at these per-request costs');
    }
  });

  form.hidden = false;
})();
