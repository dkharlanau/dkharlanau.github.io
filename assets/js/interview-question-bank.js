---
---
(() => {
  'use strict';

  const BANK = {{ site.data.career.question_bank | jsonify }};
  const ROADMAP_SKILLS = {{ site.data.career.roadmap.skills | jsonify }};
  const TRACKS = {
    sales: 'Sales',
    logistics: 'Procurement & Logistics',
    integration: 'Integration & Architecture',
    ai: 'AI & Data',
    delivery: 'Delivery & Operations',
    leadership: 'Lead Judgment'
  };

  const skillById = Object.fromEntries(ROADMAP_SKILLS.map(skill => [skill.id, skill]));
  const questions = [];

  BANK.skills.forEach(group => {
    const skill = skillById[group.skill_id];
    if (!skill) return;
    group.questions.forEach(item => {
      const type = BANK.types[item.type] || {};
      questions.push({
        id: `${group.skill_id}-${item.type}`,
        skill_id: group.skill_id,
        skill_title: skill.title,
        track: skill.track,
        tier: skill.tier,
        type: item.type,
        level: type.label || item.type,
        q: item.prompt,
        follow_up: item.follow_up || type.pressure || '',
        evidence: item.evidence || type.evidence || '',
        sources: skill.sources || []
      });
    });
  });

  window.InterviewQuestionBank = {
    version: BANK.version,
    updated_at: BANK.updated_at,
    types: BANK.types,
    tracks: TRACKS,
    skills: skillById,
    questions
  };

  const IR = window.InterviewReadiness;
  if (!IR) return;

  Object.keys(IR.TRACKS).forEach(key => delete IR.TRACKS[key]);
  Object.assign(IR.TRACKS, TRACKS);
  IR.QUESTION_TYPES = BANK.types;
  IR.SKILLS = skillById;
  IR.QUESTIONS = questions;

  function shuffled(values) {
    return [...values].sort(() => Math.random() - 0.5);
  }

  IR.shuffledQuestions = function shuffledQuestions(count = 12) {
    const trackIds = Object.keys(TRACKS);
    const typeIds = Object.keys(BANK.types);
    const selected = [];
    const used = new Set();

    trackIds.forEach((track, trackIndex) => {
      const preferredTypes = [
        typeIds[trackIndex % typeIds.length],
        typeIds[(trackIndex + 2) % typeIds.length]
      ];
      preferredTypes.forEach(type => {
        const candidates = shuffled(questions.filter(item => item.track === track && item.type === type && !used.has(item.id)));
        if (!candidates.length) return;
        selected.push(candidates[0]);
        used.add(candidates[0].id);
      });
    });

    if (selected.length < count) {
      shuffled(questions.filter(item => !used.has(item.id))).some(item => {
        selected.push(item);
        used.add(item.id);
        return selected.length >= count;
      });
    }

    return shuffled(selected).slice(0, count);
  };
})();
