(() => {
  'use strict';

  const STORAGE_KEY = 'sapInterviewReadinessV1';
  const PRACTICE_KEY = 'sapInterviewPracticeV1';
  const STORY_KEY = 'sapInterviewStoryBankV1';

  const STATUSES = [
    { id: 'not-reviewed', label: 'Not reviewed', score: 0 },
    { id: 'refreshed', label: 'Refreshed', score: 1 },
    { id: 'explain', label: 'Can explain', score: 2 },
    { id: 'defend', label: 'Can defend', score: 3 }
  ];

  const TRACKS = {
    sales: 'Sales',
    logistics: 'Procurement & Logistics',
    integration: 'Integration & Architecture',
    ai: 'AI & Data',
    leadership: 'Lead Judgment'
  };

  const TOPICS = [
    {id:'sales-o2c',track:'sales',title:'Order-to-Cash',href:'/labs/enterprise-context/sales-processes/',why:'Explain the full business flow before discussing one transaction.'},
    {id:'sales-order',track:'sales',title:'Sales Order',href:'/labs/enterprise-context/sales-order/',why:'Connect document logic, partners, dates, quantities, and follow-on documents.'},
    {id:'sales-pricing',track:'sales',title:'Pricing',href:'/labs/enterprise-context/pricing/',why:'Explain condition technique, ownership, and failure evidence without turning the answer into a configuration dump.'},
    {id:'sales-atp',track:'sales',title:'ATP and availability',href:'/labs/enterprise-context/atp/',why:'Separate stock, availability, confirmation, and business promise.'},
    {id:'sales-shipping',track:'sales',title:'Shipping and delivery',href:'/labs/enterprise-context/shipping/',why:'Trace order readiness into delivery, picking, goods issue, and exceptions.'},
    {id:'sales-billing',track:'sales',title:'Billing',href:'/labs/enterprise-context/billing/',why:'Explain billing relevance, document flow, blocks, and accounting hand-off.'},
    {id:'sales-credit',track:'sales',title:'Credit Management',href:'/labs/enterprise-context/credit/',why:'Show how business risk, checks, blocks, release, and order execution meet.'},
    {id:'sales-tax',track:'sales',title:'Tax',href:'/labs/enterprise-context/tax/',why:'Keep the answer at decision and dependency level unless configuration detail is requested.'},
    {id:'sales-diagnostics',track:'sales',title:'Sales diagnostics',href:'/labs/enterprise-context/sales-diagnostics/',why:'Move from symptom to document flow, data, configuration, enhancement, and interface evidence.'},
    {id:'sales-special',track:'sales',title:'Special sales cases',href:'/labs/enterprise-context/condition-contract-management/',why:'Be ready to discuss exceptions without losing the main process model.'},

    {id:'procurement-p2p',track:'logistics',title:'Procure-to-Pay',href:'/labs/enterprise-context/procurement/',why:'Explain demand, sourcing, purchasing, receipt, invoice, and ownership across the flow.'},
    {id:'logistics-inventory',track:'logistics',title:'Inventory Management',href:'/labs/enterprise-context/inventory-management/',why:'Separate physical stock, book stock, movement logic, reservations, and availability.'},
    {id:'logistics-material',track:'logistics',title:'Material behaviour',href:'/labs/enterprise-context/material-behavior/',why:'Connect master data choices to process behaviour instead of listing fields.'},
    {id:'logistics-ewm',track:'logistics',title:'EWM boundaries',href:'/labs/enterprise-context/ewm/',why:'Explain what belongs in warehouse execution and what remains outside it.'},
    {id:'logistics-tm',track:'logistics',title:'Transportation Management',href:'/labs/enterprise-context/transportation-management/',why:'Connect transport planning and execution to sales, delivery, warehouse, and cost decisions.'},
    {id:'logistics-production',track:'logistics',title:'Production touchpoints',href:'/labs/enterprise-context/production/',why:'Know enough to trace demand, supply, availability, staging, and logistics dependencies.'},
    {id:'logistics-quality',track:'logistics',title:'Quality Management touchpoints',href:'/labs/enterprise-context/quality-management/',why:'Explain how quality decisions can block or redirect logistics execution.'},
    {id:'logistics-master-data',track:'logistics',title:'Master Data',href:'/labs/enterprise-context/master-data/',why:'Treat master data as process control, not administrative background.'},
    {id:'logistics-mdg',track:'logistics',title:'MDG and governance',href:'/labs/enterprise-context/mdg/',why:'Explain ownership, approval, replication, and downstream business effect.'},
    {id:'logistics-finance',track:'logistics',title:'Finance and logistics boundary',href:'/labs/enterprise-context/finance-logistics/',why:'Show where logistics decisions create accounting consequences and where ownership changes.'},

    {id:'integration-patterns',track:'integration',title:'Integration patterns',href:'/labs/enterprise-context/integrations/',why:'Choose API, IDoc, event, file, or synchronous call from business and operational needs.'},
    {id:'integration-operations',track:'integration',title:'Integration operations',href:'/labs/enterprise-context/integration-operations/',why:'Talk about monitoring, retry, ownership, idempotency, and recovery, not only message transport.'},
    {id:'integration-failure',track:'integration',title:'Integration failure analysis',href:'/labs/templates/',why:'Structure diagnosis across source, contract, middleware, target, data, and recovery path.'},
    {id:'integration-development',track:'integration',title:'Development boundary',href:'/labs/enterprise-context/development/',why:'Know when a problem is process, configuration, enhancement, custom code, or external integration.'},
    {id:'integration-analytics',track:'integration',title:'Analytics and observability',href:'/labs/enterprise-context/end-to-end-analytics/',why:'Connect operational evidence to business outcome and decision quality.'},
    {id:'integration-deployment',track:'integration',title:'Deployment model choices',href:'/labs/enterprise-context/deployment-models/',why:'Explain constraints and trade-offs across public cloud, private cloud, and on-premise landscapes.'},
    {id:'integration-cleancore',track:'integration',title:'Clean core and side-by-side',href:'/frameworks/',why:'Defend the boundary between core stability and change outside the core.'},
    {id:'integration-ownership',track:'integration',title:'Cross-system ownership',href:'/labs/enterprise-context/logistics-capabilities/',why:'Assign responsibility for business outcome, data, contract, processing, and recovery.'},
    {id:'integration-architecture',track:'integration',title:'Architecture trade-offs',href:'/labs/assessment/core-boundaries/',why:'Explain why a design is appropriate, what it costs, and what you would challenge.'},
    {id:'integration-board',track:'integration',title:'Board-level architecture answer',href:'/labs/assessment/board/',why:'Translate technical design into business risk, delivery sequence, and decision options.'},

    {id:'ai-readiness',track:'ai',title:'AI readiness',href:'/labs/ai-ready/',why:'Start with process, data, controls, evaluation, and operating boundary before model choice.'},
    {id:'ai-business',track:'ai',title:'Business AI use cases',href:'/labs/business-ai/',why:'Connect a business job to an AI pattern, control, outcome, and evidence.'},
    {id:'ai-data-quality',track:'ai',title:'Data quality for AI',href:'/labs/enterprise-context/data-governance/',why:'Explain why retrieval quality and automation safety depend on governed source data.'},
    {id:'ai-retrieval',track:'ai',title:'Retrieval and context',href:'/labs/ai-ready/',why:'Separate source quality, chunking, retrieval, grounding, permissions, and answer generation.'},
    {id:'ai-agents',track:'ai',title:'Agents and tools',href:'/labs/ai-ready/',why:'Know when an agent needs tools, state, approvals, boundaries, and a recovery path.'},
    {id:'ai-evals',track:'ai',title:'Evaluation',href:'/labs/ai-ready/',why:'Define what good means before arguing about model quality.'},
    {id:'ai-security',track:'ai',title:'AI security and access',href:'/labs/ai-ready/',why:'Cover identity, permissions, data exposure, prompt injection, logging, and human control.'},
    {id:'ai-production',track:'ai',title:'AI in production',href:'/labs/ai-ready/',why:'Discuss ownership, latency, cost, monitoring, fallback, versioning, and change control.'},
    {id:'ai-mcp',track:'ai',title:'MCP and tool access',href:'/machine/',why:'Explain the value and the boundary of structured tool access without treating MCP as magic plumbing.'},
    {id:'ai-value',track:'ai',title:'AI business value',href:'/labs/business-ai/',why:'Tie the solution to measurable work reduction, decision quality, risk, or cycle time.'},

    {id:'lead-answer',track:'leadership',title:'Lead-level answer structure',href:'/labs/assessment/start-here/',why:'Keep answers anchored in business goal, owner, flow, decision, boundary, evidence, and trade-off.'},
    {id:'lead-challenge',track:'leadership',title:'Challenge a requirement',href:'/labs/assessment/core-boundaries/',why:'Show where you would disagree, what evidence you need, and what safer option you would offer.'},
    {id:'lead-stakeholders',track:'leadership',title:'Stakeholder conflict',href:'/labs/assessment/board/',why:'Handle competing business, architecture, delivery, and operational priorities without hiding the trade-off.'},
    {id:'lead-failure',track:'leadership',title:'Failure and recovery',href:'/labs/templates/',why:'Explain diagnosis, containment, ownership, communication, recovery, and prevention.'},
    {id:'lead-evidence',track:'leadership',title:'Evidence coverage',href:'/labs/assessment/evidence-coverage/',why:'Back claims with a project, decision, failure, result, or public artefact.'},
    {id:'lead-story',track:'leadership',title:'Project story quality',href:'/labs/interview-readiness/stories/',why:'Turn experience into a short story with role, decision, trade-off, result, and lesson.'},
    {id:'lead-mock',track:'leadership',title:'Pressure practice',href:'/labs/assessment/mock/',why:'Test whether the answer stays structured when topics switch and follow-up pressure increases.'},
    {id:'lead-feedback',track:'leadership',title:'Feedback calibration',href:'/labs/assessment/feedback/',why:'Use observed feedback to change practice instead of polishing the same comfortable answers.'},
    {id:'lead-readiness',track:'leadership',title:'Promotion and role readiness',href:'/labs/assessment/promotion-readiness/',why:'Separate topic knowledge from evidence that you can lead decisions across boundaries.'},
    {id:'lead-human',track:'leadership',title:'Human review',href:'/labs/assessment/human-review/',why:'Keep final judgment with a human reviewer when the evidence is incomplete or context-specific.'}
  ];

  const QUESTIONS = [
    {track:'sales',level:'Explain',q:'Walk me through Order-to-Cash from customer demand to accounting impact. Where do ownership boundaries change?'},
    {track:'sales',level:'Trace',q:'A sales order has a confirmed quantity, but delivery cannot proceed. What do you check and in what order?'},
    {track:'sales',level:'Diagnose',q:'Pricing is correct for most customers but wrong for one sales area. How would you separate master data, condition records, access logic, and custom code?'},
    {track:'sales',level:'Design',q:'A business wants every sales channel to calculate availability independently. What would you challenge before agreeing?'},
    {track:'sales',level:'Challenge',q:'The business asks to solve a recurring delivery block with a background job. What questions do you ask before accepting the workaround?'},
    {track:'sales',level:'Explain',q:'How do you explain the difference between stock, ATP, confirmed quantity, and delivery readiness to a business manager?'},
    {track:'sales',level:'Diagnose',q:'Billing is blocked after a successful goods issue. Which document, data, and configuration dependencies do you inspect first?'},
    {track:'sales',level:'Design',q:'How would you design ownership for a sales process that crosses CRM, SAP, warehouse, tax, and finance systems?'},

    {track:'logistics',level:'Explain',q:'Walk me through Procure-to-Pay and name the points where data quality can stop the process.'},
    {track:'logistics',level:'Trace',q:'Physical stock exists, but the business cannot use it for an order. How do you structure the investigation?'},
    {track:'logistics',level:'Diagnose',q:'A goods movement posts differently for one material group. How do you separate material master, movement logic, configuration, and enhancement effects?'},
    {track:'logistics',level:'Design',q:'When does EWM add useful control, and when does it add unnecessary complexity?'},
    {track:'logistics',level:'Challenge',q:'A programme wants one global material template with no local exceptions. What would you test before supporting that decision?'},
    {track:'logistics',level:'Explain',q:'How do production, inventory, warehouse, and sales availability influence each other without becoming one giant ownership model?'},
    {track:'logistics',level:'Diagnose',q:'A supplier delivery is received but downstream processing is blocked by quality status. Who owns the next decision?'},
    {track:'logistics',level:'Design',q:'How would you set governance for master data changes that affect purchasing, warehouse execution, sales, and finance?'},

    {track:'integration',level:'Explain',q:'How do you choose between API, IDoc, event, file, and synchronous call for an enterprise integration?'},
    {track:'integration',level:'Trace',q:'An outbound message left SAP but the business outcome did not happen. Describe your evidence path from source to target.'},
    {track:'integration',level:'Diagnose',q:'Messages are duplicated after retries. Which contract and runtime behaviours do you investigate?'},
    {track:'integration',level:'Design',q:'Design a recoverable integration for a business process where the target system can be unavailable for several hours.'},
    {track:'integration',level:'Challenge',q:'A team wants point-to-point interfaces because they are faster to deliver. What trade-offs do you put on the table?'},
    {track:'integration',level:'Explain',q:'What does clean core mean in an integration-heavy landscape, beyond the slogan?'},
    {track:'integration',level:'Design',q:'How would you split monitoring responsibility between SAP application, middleware, external system, and business operations?'},
    {track:'integration',level:'Challenge',q:'An architecture board wants one integration technology for every use case. How do you respond?'},

    {track:'ai',level:'Explain',q:'What makes an SAP process ready for AI assistance, and what makes it a bad candidate?'},
    {track:'ai',level:'Trace',q:'An AI support assistant gives a confident but wrong answer. What layers do you inspect before blaming the model?'},
    {track:'ai',level:'Diagnose',q:'Retrieval quality fell after a documentation update. How do you separate source, indexing, chunking, permissions, retrieval, and generation issues?'},
    {track:'ai',level:'Design',q:'Design an AI-assisted incident triage flow where a wrong action could affect production.'},
    {track:'ai',level:'Challenge',q:'A sponsor wants an autonomous agent because the manual process is slow. What evidence do you require before removing human approval?'},
    {track:'ai',level:'Explain',q:'What problem does MCP solve, and what problems does it not solve?'},
    {track:'ai',level:'Design',q:'How would you evaluate an AI assistant for SAP operations before production release?'},
    {track:'ai',level:'Challenge',q:'The business measures AI success by number of generated answers. What outcome measures would you propose instead?'},

    {track:'leadership',level:'Lead',q:'Tell me about a time you challenged a requested solution because the real problem was elsewhere.'},
    {track:'leadership',level:'Lead',q:'Describe a production issue where several teams owned different parts of the failure. How did you drive the decision?'},
    {track:'leadership',level:'Lead',q:'A programme is late. Business wants scope, architecture wants quality, delivery wants speed. How do you frame the decision?'},
    {track:'leadership',level:'Lead',q:'Which technical decision have you made that created an operational cost later? What did you learn?'},
    {track:'leadership',level:'Lead',q:'How do you know when you have enough evidence to make a decision and when you should keep investigating?'},
    {track:'leadership',level:'Lead',q:'Give an example where your first diagnosis was wrong. What changed your view?'},
    {track:'leadership',level:'Lead',q:'How do you explain a complex SAP problem to a manager who does not need the technical detail?'},
    {track:'leadership',level:'Lead',q:'What is one area where you would still ask for a specialist rather than lead the decision alone?' }
  ];

  function readJson(key, fallback) {
    try {
      const parsed = JSON.parse(localStorage.getItem(key));
      return parsed == null ? fallback : parsed;
    } catch (_) { return fallback; }
  }

  function writeJson(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); return true; }
    catch (_) { return false; }
  }

  function getState() {
    const raw = readJson(STORAGE_KEY, {});
    return raw && typeof raw === 'object' && !Array.isArray(raw) ? raw : {};
  }

  function getStatus(topicId) {
    const state = getState();
    const status = state[topicId];
    return STATUSES.some(item => item.id === status) ? status : STATUSES[0].id;
  }

  function setStatus(topicId, statusId) {
    if (!TOPICS.some(topic => topic.id === topicId) || !STATUSES.some(status => status.id === statusId)) return false;
    const state = getState();
    state[topicId] = statusId;
    writeJson(STORAGE_KEY, state);
    window.dispatchEvent(new CustomEvent('interview-readiness-change', { detail: { topicId, statusId } }));
    return true;
  }

  function cycleStatus(topicId) {
    const current = getStatus(topicId);
    const index = STATUSES.findIndex(item => item.id === current);
    const next = STATUSES[(index + 1) % STATUSES.length];
    setStatus(topicId, next.id);
    return next;
  }

  function statusObject(topicId) {
    return STATUSES.find(item => item.id === getStatus(topicId)) || STATUSES[0];
  }

  function readinessFor(items) {
    if (!items.length) return 0;
    const total = items.reduce((sum, topic) => sum + statusObject(topic.id).score, 0);
    return Math.round((total / (items.length * 3)) * 100);
  }

  function summary() {
    const tracks = {};
    Object.keys(TRACKS).forEach(track => {
      const items = TOPICS.filter(topic => topic.track === track);
      tracks[track] = { label: TRACKS[track], readiness: readinessFor(items), count: items.length };
    });
    const orderedWeak = TOPICS.slice().sort((a,b) => {
      const delta = statusObject(a.id).score - statusObject(b.id).score;
      if (delta !== 0) return delta;
      return a.title.localeCompare(b.title);
    });
    const statuses = Object.fromEntries(STATUSES.map(status => [status.id, TOPICS.filter(topic => getStatus(topic.id) === status.id).length]));
    return { overall: readinessFor(TOPICS), tracks, weak: orderedWeak, statuses };
  }

  function dailyPlan(limit = 4) {
    const picked = [];
    const usedTracks = new Set();
    const sorted = TOPICS.slice().sort((a,b) => statusObject(a.id).score - statusObject(b.id).score || a.title.localeCompare(b.title));
    for (const topic of sorted) {
      if (!usedTracks.has(topic.track)) {
        picked.push(topic);
        usedTracks.add(topic.track);
      }
      if (picked.length >= limit) break;
    }
    for (const topic of sorted) {
      if (picked.length >= limit) break;
      if (!picked.some(item => item.id === topic.id)) picked.push(topic);
    }
    return picked.map((topic,index) => ({...topic, minutes:[20,15,10,15][index] || 15, status:statusObject(topic.id)}));
  }

  function resetReadiness() {
    localStorage.removeItem(STORAGE_KEY);
    window.dispatchEvent(new CustomEvent('interview-readiness-change'));
  }

  function practiceHistory() {
    const rows = readJson(PRACTICE_KEY, []);
    return Array.isArray(rows) ? rows : [];
  }

  function savePracticeAttempt(attempt) {
    const rows = practiceHistory();
    rows.unshift(attempt);
    writeJson(PRACTICE_KEY, rows.slice(0, 100));
  }

  function storyBank() {
    const rows = readJson(STORY_KEY, []);
    return Array.isArray(rows) ? rows : [];
  }

  function saveStories(rows) { return writeJson(STORY_KEY, rows); }

  function shuffledQuestions(count = 10) {
    const byTrack = {};
    Object.keys(TRACKS).forEach(track => { byTrack[track] = QUESTIONS.filter(item => item.track === track); });
    const targets = {sales:2,logistics:2,integration:2,ai:2,leadership:2};
    const selected = [];
    Object.entries(targets).forEach(([track,qty]) => {
      const pool = byTrack[track].slice().sort(() => Math.random() - .5);
      selected.push(...pool.slice(0,qty));
    });
    return selected.sort(() => Math.random() - .5).slice(0,count);
  }

  window.InterviewReadiness = {
    STORAGE_KEY,PRACTICE_KEY,STORY_KEY,STATUSES,TRACKS,TOPICS,QUESTIONS,
    getState,getStatus,setStatus,cycleStatus,statusObject,readinessFor,summary,dailyPlan,resetReadiness,
    practiceHistory,savePracticeAttempt,storyBank,saveStories,shuffledQuestions
  };
})();
