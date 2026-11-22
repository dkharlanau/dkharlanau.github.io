---
layout: default
title: "Apache Kafka — Events, Topics, Consumer Groups and a Working Local Lab"
description: "Learn Kafka by running one broker, sending keyed logistics events, replaying them, and designing a reliable SAP integration boundary."
permalink: /labs/enterprise-context/integrations/kafka/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-22
last_reviewed: 2026-11-22
review_method: "Apache Kafka 4.4 official quickstart and SAP Cloud Integration adapter documentation; local execution and human review pending"
content_model: technical_guide
hide_global_cta: true
career_impact: mapped
career_skills:
  - integration-patterns
  - integration-recovery
  - integration-observability
tags: [apache-kafka, event-streaming, sap-integration, event-driven-architecture, logistics, docker]
structured_data:
  type: TechArticle
  primary_topic: sap-integration
semantic_links:
  - type: part_of
    title: "SAP Integration Architecture"
    url: "/labs/enterprise-context/integrations/"
  - type: related_topic
    title: "RabbitMQ Practical Guide"
    url: "/labs/enterprise-context/integrations/rabbitmq/"
  - type: related_topic
    title: "Kafka vs RabbitMQ Decision Guide"
    url: "/labs/enterprise-context/integrations/event-brokers/"
  - type: related_topic
    title: "Integration Operations and Recovery"
    url: "/labs/enterprise-context/integration-operations/"
source_links:
  - title: "Apache Kafka 4.4 quickstart"
    url: "https://kafka.apache.org/44/getting-started/quickstart/"
  - title: "Apache Kafka 4.4 Docker guide"
    url: "https://kafka.apache.org/44/getting-started/docker/"
  - title: "SAP Cloud Integration Kafka sender adapter"
    url: "https://help.sap.com/docs/integration-suite/isuite-integrations-and-apis/configure-kafka-sender-adapter"
  - title: "SAP Cloud Integration adapter overview"
    url: "https://help.sap.com/docs/cloud-integration/sap-cloud-integration/introduction"
---
<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">SAP Enterprise</a></li><li><a href="/labs/enterprise-context/integrations/">Integrations</a></li><li aria-current="page">Kafka</li></ol></nav>
<div class="research-canvas">
<header class="research-canvas__hero" data-reveal>
<div class="research-canvas__hero-copy">
<p class="research-canvas__eyebrow">SAP Enterprise / Integration / Hands-on</p>
<h1>Apache Kafka: follow one delivery event through the system</h1>
<p>Two applications need the same logistics event. One updates an external tracking view; another builds analytics. Neither should block the SAP transaction. Kafka stores the event so independent consumers can read it at their own pace.</p>
<a class="research-canvas__button" href="#first-run">Run the first event <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
</div>
<div class="research-canvas__signal" aria-label="What this lab teaches">
<p>One practical learning path</p>
<div class="research-canvas__signal-line"><span>01</span><strong>Model</strong><small>Topic, partition, offset</small></div>
<div class="research-canvas__signal-line"><span>02</span><strong>Run</strong><small>Docker and CLI</small></div>
<div class="research-canvas__signal-line"><span>03</span><strong>Prove</strong><small>Replay and groups</small></div>
<div class="research-canvas__signal-line"><span>04</span><strong>Design</strong><small>SAP boundaries and failure</small></div>
<em>Apache Kafka 4.4.0 sample; single-node training only.</em></div></header>
<section class="research-canvas__boundary" data-reveal><span class="material-symbols-outlined" aria-hidden="true">hub</span>
<p><strong>Remember:</strong> Kafka is an event log, not an SAP transaction engine. A producer appends records to a topic; a consumer reads records by position (offset). Reading does not normally delete an event immediately.</p>
<p><strong>Outcome:</strong> create a three-partition topic, publish keyed events, read them from two independent consumer groups, and explain a safe SAP-to-Kafka integration.</p></section>
<section class="research-canvas__inventory" id="mental-model" data-reveal><header><p class="research-canvas__eyebrow">01 / Build the mental model</p><h2>Six words that explain Kafka</h2><p>Think of a topic as a durable sequence of records, divided into partitions for scale. Consumers track how far they have read.</p></header>
<div class="ecg-decision-columns">
<div><h3>Producer</h3><p>The app or connector that publishes an event, such as <code>DeliveryStatusChanged</code>. It must decide what the event means and which key it uses.</p></div>
<div><h3>Topic</h3><p>A named stream, here <code>delivery-events</code>. Multiple subscribers can independently consume the same retained records.</p></div>
<div><h3>Partition</h3><p>One ordered log inside a topic. Ordering is guaranteed <strong>within a partition</strong>, not across the whole topic.</p></div>
<div><h3>Key</h3><p>We use <code>deliveryId</code>. With a stable partitioning scheme, events for the same delivery land in the same partition and preserve their relative order.</p></div>
<div><h3>Offset</h3><p>A record position in one partition. It is not the SAP document number; it tells a consumer where a record was stored.</p></div>
<div><h3>Consumer group</h3><p>Consumers in one group divide assigned partitions. A second group sees its own copy of the stream from its own offsets.</p></div></div>
<p><strong>Important nuance:</strong> Kafka retention controls how long records remain available. Committing an offset is not proof that the external business update was committed. Broker acknowledgements and a database transaction are separate boundaries.</p></section>
<section class="research-canvas__inventory" id="first-run" data-reveal><header><p class="research-canvas__eyebrow">02 / 10-minute local lab</p><h2>Start Kafka and create a topic</h2><p>Prerequisites: Docker Desktop on macOS, Windows, or Linux; terminal access; ports 9092 free. Docker is only for learning here.</p></header>
<p>Run these commands in Terminal. Apache's official image uses KRaft and does not need a separate ZooKeeper container.</p>
<pre><code class="language-bash">docker run -d --name kafka-lab -p 9092:9092 apache/kafka:4.4.0
docker logs kafka-lab --tail 25
docker exec kafka-lab /opt/kafka/bin/kafka-topics.sh --create \
  --topic delivery-events --partitions 3 --replication-factor 1 \
  --bootstrap-server localhost:9092
docker exec kafka-lab /opt/kafka/bin/kafka-topics.sh --describe \
  --topic delivery-events --bootstrap-server localhost:9092</code></pre>
<p><strong>What to check:</strong> the topic description should report <code>PartitionCount: 3</code> and <code>ReplicationFactor: 1</code>. That replication factor is intentionally unsafe for production.</p>
<h3>Publish two events for one delivery</h3>
<pre><code class="language-bash">printf '%s\n' \
  'D-45001|{"eventId":"evt-1001","deliveryId":"D-45001","status":"PICKED","version":1}' \
  'D-45001|{"eventId":"evt-1002","deliveryId":"D-45001","status":"SHIPPED","version":2}' \
  | docker exec -i kafka-lab /opt/kafka/bin/kafka-console-producer.sh \
    --bootstrap-server localhost:9092 --topic delivery-events \
    --property parse.key=true --property 'key.separator=|'</code></pre>
<p>Kafka uses <code>D-45001</code> as the record key. The JSON value is illustrative, not an SAP-delivered event schema. <code>eventId</code> identifies the message; <code>deliveryId</code> identifies the business object; <code>version</code> helps detect stale updates.</p>
<h3>Read with two independent consumer groups</h3>
<pre><code class="language-bash">docker exec kafka-lab /opt/kafka/bin/kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 --topic delivery-events \
  --group logistics-demo-v1 --from-beginning --max-messages 2 \
  --property print.key=true --property 'key.separator= | '

# Another consumer group reads the same retained events independently:
docker exec kafka-lab /opt/kafka/bin/kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 --topic delivery-events \
  --group analytics-demo-v1 --from-beginning --max-messages 2 \
  --property print.key=true --property 'key.separator= | '</code></pre>
<p><strong>Expected:</strong> each group reads both records. A new group may read from the beginning when <code>--from-beginning</code> is specified; an existing group with committed offsets will normally resume at its stored position. Change the group name for a clean replay.</p>
<p>When finished: <pre><code class="language-bash">docker rm -f kafka-lab</code></pre></p></section>
<section class="research-canvas__inventory" id="experiments" data-reveal><header><p class="research-canvas__eyebrow">03 / Test the failure model</p><h2>Three changes that teach more than a diagram</h2><p>Run these small experiments before using Kafka in an SAP solution design.</p></header>
<ol>
<li><strong>Scale consumers.</strong> Start two consumers with the same group ID while producing more events. With three partitions, assignment is split across active consumers; one partition is assigned to at most one consumer in a group at a time. Stop one consumer and observe reassignment.</li>
<li><strong>Replay.</strong> Start a brand-new group with <code>--from-beginning</code>. It can read retained records even if another group processed them earlier. A replay is not automatically safe: a receiver may create duplicate business transactions.</li>
<li><strong>Ordering challenge.</strong> Send messages for two delivery keys. Compare ordering per key with the interleaving across partitions. A larger partition count can change the key-to-partition mapping; plan changes deliberately.</li></ol>
<p><strong>Production rule:</strong> a consumer may receive a record more than once. Design idempotent processing using a stable event ID or an appropriate business key, commit progress only after the outcome is durably recorded, and reconcile the target state. Exactly-once features within Kafka do not automatically make an external SAP update exactly-once.</p></section>
<section class="research-canvas__inventory" id="sap-case" data-reveal><header><p class="research-canvas__eyebrow">04 / Apply to SAP</p><h2>A safe logistics example: delivery visibility</h2><p>This is a <strong>synthetic architecture case</strong>. The described event name and payload are examples, not SAP standard event names.</p></header>
<div class="research-route-list">
<a href="#sap-options"><span>1</span><strong>S/4HANA records the business change</strong><small>Check whether the relevant business event or released integration interface exists in the target S/4HANA edition and release.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
<a href="#sap-options"><span>2</span><strong>Integration layer transforms and publishes</strong><small>SAP Cloud Integration can use supported Kafka sender and receiver adapters; verify runtime availability, network, authentication, and feature support.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
<a href="#sap-options"><span>3</span><strong>Kafka retains the external event</strong><small>Use the stable delivery key, agreed schema, retention policy, topic ACLs, and client encryption.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
<a href="#sap-options"><span>4</span><strong>Tracking and analytics consume separately</strong><small>Each consumer group handles its own offsets, idempotency, error handling, monitoring, and reconciliation.</small><i class="material-symbols-outlined" aria-hidden="true">task_alt</i></a>
</div>
<h3 id="sap-options">Options you must distinguish</h3>
<ul><li><strong>SAP standard:</strong> use released business events, APIs, or integration content where available for the specific edition/release.</li><li><strong>Integration design:</strong> route a supported source message through SAP Integration Suite to Kafka. The Integration Suite adapters are not a guarantee that every SAP business object publishes a Kafka event automatically.</li><li><strong>Custom extension:</strong> when standard interfaces cannot satisfy the requirement, assess a clean-core-compliant event publisher, transactional outbox, or change-capture approach. Treat these as design decisions, not built-in S/4HANA behavior.</li></ul>
<p><strong>Do not</strong> use a tracking event to replicate SAP inventory or financial postings as if the external consumer owned those core transactions. Make the receiving system's responsibility explicit.</p></section>
<section class="research-canvas__inventory" id="operations" data-reveal><header><p class="research-canvas__eyebrow">05 / Design and support</p><h2>What breaks, where to look, and what to measure</h2><p>Separate the transport signal from the business result.</p></header>
<div class="table-scroll study-table"><table class="study-table__table"><thead><tr><th>Symptom</th><th>Investigate first</th><th>Business proof</th></tr></thead><tbody>
<tr><td>Events arrive late</td><td>Producer failures, broker health, consumer lag, slow target API, partition assignment</td><td>Age of the tracking update compared with its source timestamp</td></tr>
<tr><td>One delivery is out of order</td><td>Record key, partition, retry/concurrency, consumer state, source event version</td><td>Target reflects the latest valid version</td></tr>
<tr><td>Duplicate target updates</td><td>Offset commit timing, retries, rebalancing, idempotency ledger</td><td>Only one effective business action per event ID</td></tr>
<tr><td>Record missing from a replay</td><td>Topic retention, wrong group/offset, ACLs, topic name, producer publish result</td><td>Compare source outbox or change log to consumed event IDs</td></tr>
</tbody></table></div>
<p><strong>Architecture checklist:</strong> schema and schema version; key/ordering; retention and replay; partition sizing; acks and producer retries; group ownership; failure isolation; credentials/TLS; monitoring and alert thresholds; consumer lag; target reconciliation; privacy and data minimisation.</p>
<p><strong>Cost boundary:</strong> Docker on a laptop is a learning environment, not a production cluster. Real costs include brokers, storage, replication, networking, managed service fees, observability, and engineering operations.</p></section>
<section class="research-canvas__inventory" id="checkpoint" data-reveal><header><p class="research-canvas__eyebrow">06 / Prove you understand</p><h2>Explain it like a SAP Lead</h2><p>Do not memorise a definition. Answer with the ownership and failure boundary.</p></header>
<p><strong>Case:</strong> A logistics manager asks for two independent external systems to react to each delivery status change, with the option to rebuild analytics from past events. Why would you choose Kafka, and what conditions might change your decision?</p>
<p><strong>30-second answer:</strong> “Kafka fits when we need a retained event stream and independent consumers. I would first check which S/4HANA event or API is available, define the delivery key and contract, then design lag monitoring, replay, idempotency, and reconciliation. Kafka does not confirm that the downstream business update succeeded.”</p>
<p><strong>Practice:</strong> explain what changes when the business instead needs one document-processing worker with a dead-letter queue and no historical replay. Continue with the <a href="/labs/enterprise-context/integrations/rabbitmq/">RabbitMQ lab</a> or the <a href="/labs/enterprise-context/integrations/event-brokers/">decision comparison</a>.</p></section>
<section class="research-canvas__inventory" id="references" data-reveal><header><p class="research-canvas__eyebrow">Official references</p><h2>Documentation and release boundaries</h2><p>Commands are aligned with the official Apache Kafka 4.4 image and help pages, but were not executed inside this website.</p></header>
<ul><li><a href="https://kafka.apache.org/44/getting-started/quickstart/" target="_blank" rel="noopener">Apache Kafka 4.4 quickstart</a> — official local broker, producer and consumer commands.</li>
<li><a href="https://kafka.apache.org/44/getting-started/docker/" target="_blank" rel="noopener">Apache Kafka Docker guide</a> — image support and development setup.</li>
<li><a href="https://help.sap.com/docs/integration-suite/isuite-integrations-and-apis/configure-kafka-sender-adapter" target="_blank" rel="noopener">SAP Kafka sender adapter</a> — integration flow connectivity.</li>
<li><a href="https://help.sap.com/docs/cloud-integration/sap-cloud-integration/introduction" target="_blank" rel="noopener">SAP Cloud Integration adapter overview</a> — receiver and sender responsibilities.</li></ul>
<p>Reviewed against official documentation on 22 November 2026. SAP adapter capabilities and connectivity must be verified against your tenant and service plan. Human editorial and hands-on validation are pending.</p></section>
<div class="research-canvas__support" data-reveal><p><a href="/labs/enterprise-context/integrations/">Back to Integration Architecture</a> · <a href="/labs/enterprise-context/integrations/rabbitmq/">Next: RabbitMQ</a> · <a href="/labs/enterprise-context/integrations/event-brokers/">Compare choices</a></p></div>
</div>