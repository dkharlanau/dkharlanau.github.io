// Pure deterministic checks. Written reasoning is intentionally not scored.
export function parseQuantity(value) {
  const text = String(value ?? '').trim();
  if (!/^-?\d+(?:[.,]\d+)?$/.test(text)) return null;
  const number = Number(text.replace(',', '.'));
  return Number.isFinite(number) ? number : null;
}
export function sameReferences(actual, expected) {
  const values = [...new Set(actual || [])].sort();
  const required = [...new Set(expected)].sort();
  return values.length === required.length && values.every((value, index) => value === required[index]);
}
export function evaluateCase(caseData, answer) {
  const checks = [
    { id: 'quantity', title: 'Calculation', passed: parseQuantity(answer.quantity) === caseData.calculation.expected, explanation: caseData.calculation.explanation },
    { id: 'cause', title: 'Diagnosis', passed: answer.cause === caseData.cause.correct, explanation: caseData.cause.explanation },
    { id: 'citations', title: 'Evidence chain', passed: sameReferences(answer.citations, caseData.citations.expected), explanation: caseData.citations.explanation },
    { id: 'action', title: 'Next action', passed: answer.action === caseData.action.correct, explanation: caseData.action.explanation },
    { id: 'verification', title: 'Verification', passed: answer.verification === caseData.verification.correct, explanation: caseData.verification.explanation }
  ];
  return { checks, correct: checks.filter(check => check.passed).length, total: checks.length, complete: checks.every(check => check.passed) };
}
export function blankAnswer() {
  return { quantity: '', cause: '', citations: [], action: '', verification: '', reasoning: '', uncertainty: '' };
}
export function missingAnswers(answer) {
  const missing = [];
  if (parseQuantity(answer.quantity) === null) missing.push('Enter a number for the calculation.');
  if (!answer.cause) missing.push('Choose a diagnosis.');
  if (!answer.citations?.length) missing.push('Select at least one evidence reference.');
  if (!answer.action) missing.push('Choose a next action.');
  if (!answer.verification) missing.push('Choose a verification check.');
  return missing;
}
