(() => {
  'use strict';

  const IR = window.InterviewReadiness;
  const dataNode = document.getElementById('career-roadmap-data');
  if (!IR || !dataNode) return;

  let DATA;
  try {
    DATA = JSON.parse(dataNode.textContent);
  } catch (error) {
    console.error('Career roadmap data could not be parsed.', error);
    return;
  }

  const tracks = DATA.tracks || {};
  const skills = Array.isArray(DATA.skills) ? DATA.skills : [];
  const tiers = DATA.tiers || {};
  const stages = Array.isArray(DATA.stages) ? DATA.stages : [];
  const trackGrid = document.getElementById('career-track-grid');
  const skillList = document.getElementById('career-skill-list');
  const tierFilters = document.getElementById('career-tier-filters');
  const health = document.getElementById('career-health');
  const activeLabel = document.getElementById('career-active-label');
  const reset = document.getElementById('career-reset');
  const initialHash = window.location.hash.replace(/^#/, '');
  let activeTrack = tracks[initialHash] ? initialHash : 'all';
  let activeTier = 'all';

  function status(skillId) {
    return IR.statusObject(skillId);
  }

  function scoreFor(skillSet) {
    if (!skillSet.length) return 0;
    const points = skillSet.reduce((sum, skill) => sum + status(skill.id).score, 0);
    return Math.round((points / (skillSet.length * 3)) * 100);
  }

  function sortedTracks() {
    return Object.entries(tracks).sort((a, b) => (a[1].order || 99) - (b[1].order || 99));
  }

  function selectTrack(trackId) {
    activeTrack = trackId;
    if (trackId === 'all') {
      history.replaceState(null, '', window.location.pathname + window.location.search);
    } else {
      history.replaceState(null, '', `#${trackId}`);
    }
    render();
  }

  function renderHealth() {
    if (!health) return;
    const defendCount = skills.filter(skill => status(skill.id).score === 3).length;
    const mappedLabs = new Set(
      skills.flatMap(skill => (skill.sources || []).filter(source => source.kind === 'lab').map(source => source.href))
    ).size;
    health.innerHTML = `
      <article><strong>${skills.length}</strong><span>Career skills</span></article>
      <article><strong>${sortedTracks().length}</strong><span>Interview tracks</span></article>
      <article><strong>${mappedLabs}</strong><span>Lab evidence routes</span></article>
      <article><strong>${defendCount}</strong><span>Skills at Can defend</span></article>`;
  }

  function renderTracks() {
    trackGrid.replaceChildren();
    const all = document.createElement('button');
    all.className = 'career-track-card';
    all.type = 'button';
    all.dataset.track = 'all';
    all.setAttribute('aria-pressed', activeTrack === 'all' ? 'true' : 'false');
    all.innerHTML = `<div class="career-track-card__top"><strong>All tracks</strong><span class="career-track-card__score">${scoreFor(skills)}%</span></div><div class="career-track-card__bar"><span style="width:${scoreFor(skills)}%"></span></div><small>${skills.length} skills across the full SAP Lead map.</small>`;
    all.addEventListener('click', () => selectTrack('all'));
    trackGrid.appendChild(all);

    sortedTracks().forEach(([trackId, track]) => {
      const trackSkills = skills.filter(skill => skill.track === trackId);
      const score = scoreFor(trackSkills);
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'career-track-card';
      button.dataset.track = trackId;
      button.id = `career-track-${trackId}`;
      button.setAttribute('aria-pressed', activeTrack === trackId ? 'true' : 'false');
      button.innerHTML = `<div class="career-track-card__top"><strong>${track.label}</strong><span class="career-track-card__score">${score}%</span></div><div class="career-track-card__bar"><span style="width:${score}%"></span></div><small>${track.statement}</small>`;
      button.addEventListener('click', () => selectTrack(trackId));
      trackGrid.appendChild(button);
    });
  }

  function renderTierFilters() {
    tierFilters.replaceChildren();
    const options = [['all', 'All skills'], ...Object.entries(tiers).map(([id, tier]) => [id, tier.label])];
    options.forEach(([id, label]) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.textContent = label;
      button.setAttribute('aria-pressed', activeTier === id ? 'true' : 'false');
      button.addEventListener('click', () => { activeTier = id; renderSkills(); });
      tierFilters.appendChild(button);
    });
  }

  function sourceLink(source) {
    const anchor = document.createElement('a');
    anchor.className = 'career-source';
    anchor.href = source.href;
    anchor.innerHTML = `<span>${source.kind}</span><strong>${source.label}</strong>`;
    return anchor;
  }

  function renderSkills() {
    skillList.replaceChildren();
    let filtered = skills.filter(skill => activeTrack === 'all' || skill.track === activeTrack);
    filtered = filtered.filter(skill => activeTier === 'all' || skill.tier === activeTier);
    if (activeLabel) {
      const trackText = activeTrack === 'all' ? 'All tracks' : tracks[activeTrack].label;
      const tierText = activeTier === 'all' ? 'all skill tiers' : tiers[activeTier].label;
      activeLabel.textContent = `${trackText} · ${tierText} · ${filtered.length} skills`;
    }
    if (!filtered.length) {
      const empty = document.createElement('div');
      empty.className = 'career-empty';
      empty.textContent = 'No skills match this filter.';
      skillList.appendChild(empty);
      return;
    }

    filtered.forEach(skill => {
      const state = status(skill.id);
      const track = tracks[skill.track] || {};
      const tier = tiers[skill.tier] || {};
      const card = document.createElement('article');
      card.className = 'career-skill';
      const head = document.createElement('div');
      head.className = 'career-skill__head';
      head.innerHTML = `<div><div class="career-skill__meta"><span class="career-chip">${track.short_label || track.label || skill.track}</span><span class="career-chip">${tier.label || skill.tier}</span></div><h3>${skill.title}</h3><p>${skill.why}</p></div>`;
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'ir-status';
      button.dataset.level = state.score;
      button.textContent = state.label;
      button.setAttribute('aria-label', `Change readiness for ${skill.title}`);
      button.addEventListener('click', () => { IR.cycleStatus(skill.id); render(); });
      head.appendChild(button);
      card.appendChild(head);

      const signal = document.createElement('p');
      signal.className = 'career-skill__signal';
      signal.innerHTML = `<strong>Interview signal:</strong> ${skill.interview_signal}`;
      card.appendChild(signal);

      const footer = document.createElement('div');
      footer.className = 'career-skill__footer';
      const sources = document.createElement('div');
      sources.className = 'career-source-list';
      (skill.sources || []).forEach(source => sources.appendChild(sourceLink(source)));
      const capabilities = document.createElement('div');
      capabilities.className = 'career-capabilities';
      (skill.capabilities || []).forEach(capability => {
        const stage = stages.find(item => item.id === capability);
        const item = document.createElement('span');
        item.textContent = stage ? stage.label : capability;
        capabilities.appendChild(item);
      });
      footer.appendChild(sources);
      footer.appendChild(capabilities);
      card.appendChild(footer);
      skillList.appendChild(card);
    });
  }

  function render() {
    renderHealth();
    renderTracks();
    renderTierFilters();
    renderSkills();
  }

  if (reset) {
    reset.addEventListener('click', () => {
      if (window.confirm('Reset all Interview Readiness topic states in this browser?')) IR.resetReadiness();
    });
  }
  window.addEventListener('hashchange', () => {
    const next = window.location.hash.replace(/^#/, '');
    if (tracks[next] && next !== activeTrack) {
      activeTrack = next;
      render();
    }
  });
  window.addEventListener('interview-readiness-change', render);
  render();
})();