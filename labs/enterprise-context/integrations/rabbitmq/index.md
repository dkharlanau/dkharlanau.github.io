---
layout: default
title: "RabbitMQ — Exchanges, Queues, Acknowledgements and a Working Local Lab"
description: "Install RabbitMQ, route a synthetic logistics event to two queues, acknowledge work, test dead-letter handling, and make SAP integration decisions."
permalink: /labs/enterprise-context/integrations/rabbitmq/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-22
last_reviewed: 2026-11-22
review_method: "RabbitMQ 4.4 official guides, Pika tutorial and SAP Cloud Integration adapter documentation; local execution and human review pending"
content_model: technical_guide
hide_global_cta: true
career_impact: mapped
career_skills:
  - integration-patterns
  - integration-recovery
  - integration-observability
tags: [rabbitmq, amqp, messaging, dead-letter-queue, sap-integration, logistics, docker]
structured_data:
  type: TechArticle
  primary_topic: sap-integration
semantic_links:
  - type: part_of
    title: "SAP Integration Architecture"
    url: "/labs/enterprise-context/integrations/"
  - type: related_topic
    title: "Apache Kafka Practical Guide"
    url: "/labs/enterprise-context/integrations/kafka/"
  - type: related_topic
    title: "Kafka vs RabbitMQ Decision Guide"
    url: "/labs/enterprise-context/integrations/event-brokers/"
source_links:
  - title: "RabbitMQ 4.4 documentation"
    url: "https://www.rabbitmq.com/docs"
  - title: "RabbitMQ 4.4 installation"
    url: "https://www.rabbitmq.com/docs/download"
  - title: "RabbitMQ Python Pika tutorial"
    url: "https://www.rabbitmq.com/tutorials/tutorial-one-python"
  - title: "RabbitMQ acknowledgements and publisher confirms"
    url: "https://www.rabbitmq.com/docs/confirms"
  - title: "RabbitMQ AMQP 1.0 client documentation"
    url: "https://www.rabbitmq.com/client-libraries/amqp-client-libraries"
  - title: "SAP Integration Suite RabbitMQ adapter"
    url: "https://help.sap.com/docs/integration-suite/sap-integration-suite/rabbitmq-adapter"
  - title: "SAP Cloud Integration AMQP adapter"
    url: "https://help.sap.com/docs/cloud-integration/sap-cloud-integration/5cc1a71231cb4cbfbfedb0cdc63e1488.html"
---
<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">SAP Enterprise</a></li><li><a href="/labs/enterprise-context/integrations/">Integrations</a></li><li aria-current="page">RabbitMQ</li></ol></nav>
<div class="research-canvas">
<header class="research-canvas__hero" data-reveal>
<div class="research-canvas__hero-copy">
<p class="research-canvas__eyebrow">SAP Enterprise / Integration / Hands-on</p>
<h1>RabbitMQ: route the right message to the right worker</h1>
<p>A document-processing worker is busy, but the sender must not wait for it. RabbitMQ receives a message, routes it to a queue, and lets the worker acknowledge completion. A failed message can be moved to a dead-letter queue for investigation.</p>
<a class="research-canvas__button" href="#first-run">Start the local broker <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
</div>
<div class="research-canvas__signal" aria-label="What this lab teaches">
<p>Four things to master</p>
<div class="research-canvas__signal-line"><span>01</span><strong>Route</strong><small>Exchange and binding</small></div>
<div class="research-canvas__signal-line"><span>02</span><strong>Queue</strong><small>Buffer and consume</small></div>
<div class="research-canvas__signal-line"><span>03</span><strong>Confirm</strong><small>Publish and acknowledge</small></div>
<div class="research-canvas__signal-line"><span>04</span><strong>Recover</strong><small>Dead letter and retry</small></div>
<em>RabbitMQ 4.x; local examples use AMQP 0.9.1.</em></div></header>
<section class="research-canvas__boundary" data-reveal>
<span class="material-symbols-outlined" aria-hidden="true">hub</span>
<p><strong>Remember:</strong> an exchange routes a message; a queue holds it; a binding connects the two; a consumer handles the work and acknowledges it. The producer should not assume the target's business transaction succeeded because a publish was confirmed.</p>
<p><strong>Protocol decision:</strong> RabbitMQ 4.x recommends <strong>AMQP 1.0 for new applications</strong>. This first lab uses Python's well-documented <code>pika</code> client for AMQP 0.9.1 so you can see exchanges, routing, and acknowledgements directly. These protocols are not wire-compatible; assess client availability before a production design.</p></section>
<section class="research-canvas__inventory" id="mental-model" data-reveal><header><p class="research-canvas__eyebrow">01 / Understand the message path</p><h2>One exchange, two queues, two independent results</h2><p>We use a synthetic delivery notification, not a real SAP event or an instruction to post goods issue.</p></header>
<div class="ecg-decision-columns">
<div><h3>Exchange</h3><p><code>delivery.events</code> receives the published message. It decides the destination using the exchange type and queue bindings.</p></div>
<div><h3>Routing key</h3><p><code>delivery.pgi.posted</code> matches the topic binding <code>delivery.pgi.*</code>. The star matches one routing-key segment.</p></div>
<div><h3>Queue</h3><p><code>wms.pgi</code> and <code>tracking.pgi</code> each get their own copy because both queues are bound to the exchange.</p></div>
<div><h3>Competing workers</h3><p>If two workers consume <em>the same queue</em>, messages are distributed among them. They do not each get a separate copy.</p></div>
<div><h3>Consumer ack</h3><p>The worker acknowledges only after successful processing. If it dies before the ack, an unacknowledged delivery may be redelivered.</p></div>
<div><h3>Dead-letter queue</h3><p>A rejected message with <code>requeue=False</code> goes to the configured dead-letter exchange and queue, rather than looping forever.</p></div></div>
<p><strong>Useful distinction:</strong> Kafka consumers track log offsets. RabbitMQ queue consumers usually receive deliveries and settle them. RabbitMQ also has Streams, so this comparison refers to its conventional queue model.</p></section>
<section class="research-canvas__inventory" id="first-run" data-reveal><header><p class="research-canvas__eyebrow">02 / Local installation</p><h2>Start RabbitMQ with its management console</h2><p>Prerequisites: Docker Desktop, Python 3 and an isolated local workstation. Do not expose demo ports or guest credentials on a public network.</p></header>
<pre><code class="language-bash">docker run -d --name rabbit-lab \
  -p 127.0.0.1:5672:5672 -p 127.0.0.1:15672:15672 \
  rabbitmq:4-management
docker logs rabbit-lab --tail 25
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pika</code></pre>
<p>Open <a href="http://localhost:15672/" target="_blank" rel="noopener">http://localhost:15672/</a>. On a fresh local demo container, use <code>guest</code> / <code>guest</code>. The UI shows connections, exchanges, queues, bindings, ready messages, and unacknowledged deliveries. The messaging port is 5672; the UI port is 15672.</p>
<p>If you use PowerShell, activate the virtual environment with <code>.venv\Scripts\Activate.ps1</code>. If the broker is still booting, wait for the startup to complete in <code>docker logs</code> before running the publisher.</p></section>
<section class="research-canvas__inventory" id="publish" data-reveal><header><p class="research-canvas__eyebrow">03 / Declare and publish</p><h2>Create the topology by running Python</h2><p>The script declares one topic exchange, two durable queues and a separate dead-letter route. It publishes two example events with publisher confirms enabled.</p></header>
<pre><code class="language-python"># Save as publish.py (training example: AMQP 0.9.1 with Pika)
import json
import pika

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
ch = conn.channel()
ch.exchange_declare(exchange="delivery.events", exchange_type="topic", durable=True)
ch.exchange_declare(exchange="delivery.dead", exchange_type="direct", durable=True)

ch.queue_declare(
    queue="wms.pgi", durable=True,
    arguments={
        "x-dead-letter-exchange": "delivery.dead",
        "x-dead-letter-routing-key": "wms.failed",
    },
)
ch.queue_bind(queue="wms.pgi", exchange="delivery.events",
              routing_key="delivery.pgi.*")
ch.queue_declare(queue="tracking.pgi", durable=True)
ch.queue_bind(queue="tracking.pgi", exchange="delivery.events",
              routing_key="delivery.pgi.*")
ch.queue_declare(queue="wms.pgi.dlq", durable=True)
ch.queue_bind(queue="wms.pgi.dlq", exchange="delivery.dead",
              routing_key="wms.failed")

ch.confirm_delivery()
for event in [
    {"eventId": "evt-2001", "deliveryId": "D-45001",
     "eventType": "PGI_POSTED", "simulateFailure": False},
    {"eventId": "evt-2002", "deliveryId": "D-45002",
     "eventType": "PGI_POSTED", "simulateFailure": True},
]:
    ch.basic_publish(
        exchange="delivery.events", routing_key="delivery.pgi.posted",
        body=json.dumps(event).encode(),
        mandatory=True,
        properties=pika.BasicProperties(
            delivery_mode=2, content_type="application/json",
            message_id=event["eventId"]),
    )
    print("Published:", event["eventId"])
conn.close()</code></pre>
<p>Save the code as <code>publish.py</code>, then run:</p>
<pre><code class="language-bash">python publish.py</code></pre>
<p><strong>Expected in the UI:</strong> two ready messages in <code>wms.pgi</code> and two in <code>tracking.pgi</code>, before you start a consumer. They are separate queues, so processing one does not remove the copy from the other.</p>
<p><strong>Why the flags matter:</strong> durable exchanges/queues survive ordinary broker restarts; persistent delivery mode asks the broker to persist the messages; publisher confirms tell the producer the broker has taken responsibility. None of these replaces backups, replication, or an idempotent receiver. For complex production topology, manage policies and definitions outside ad-hoc publisher code.</p></section>
<section class="research-canvas__inventory" id="consume" data-reveal><header><p class="research-canvas__eyebrow">04 / Consume, acknowledge, fail</p><h2>Process one queue and test a dead letter</h2><p>The second event deliberately fails. It should leave the normal queue and appear in the dead-letter queue.</p></header>
<pre><code class="language-python"># Save as worker.py; stop with Ctrl+C
import json
import pika

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
ch = conn.channel()
ch.basic_qos(prefetch_count=1)

def handle(channel, method, properties, body):
    event = json.loads(body)
    print("Received:", event["eventId"])
    if event.get("simulateFailure"):
        print("Rejected; expect a copy in wms.pgi.dlq")
        channel.basic_reject(delivery_tag=method.delivery_tag, requeue=False)
        return
    # In real integration, commit an idempotent business update here first.
    print("Processed:", event["deliveryId"])
    channel.basic_ack(delivery_tag=method.delivery_tag)

ch.basic_consume(queue="wms.pgi", on_message_callback=handle,
                 auto_ack=False)
print("Waiting for events...")
try:
    ch.start_consuming()
except KeyboardInterrupt:
    ch.stop_consuming()
finally:
    conn.close()</code></pre>
<p>Save as <code>worker.py</code>, then run:</p>
<pre><code class="language-bash">python worker.py</code></pre>
<p><strong>Expected:</strong> <code>evt-2001</code> is acknowledged; <code>evt-2002</code> is rejected without requeue and routed to <code>wms.pgi.dlq</code>. Inspect the queues in the management UI. The independent <code>tracking.pgi</code> queue still holds its two messages until it has its own consumer.</p>
<p><strong>Test the opposite failure:</strong> stop the worker before acknowledging a message. A restarted consumer may receive it again. The right response is not to turn off acknowledgements; it is to make the downstream business action idempotent and commit before acknowledging.</p>
<p>Clean up after the exercise:</p>
<pre><code class="language-bash">docker rm -f rabbit-lab</code></pre>
<p>This container is ephemeral; removing it deletes the local test data unless a persistent volume was explicitly configured.</p></section>
<section class="research-canvas__inventory" id="production" data-reveal><header><p class="research-canvas__eyebrow">05 / Build a reliable interface</p><h2>What the first demo leaves out</h2><p>A successful local test proves routing, not production readiness.</p></header>
<div class="table-scroll study-table"><table class="study-table__table"><thead><tr><th>Decision</th><th>Recommended question</th><th>Failure if ignored</th></tr></thead><tbody>
<tr><td>Queue type</td><td>Do we need a classic queue or replicated quorum queue?</td><td>Wrong availability, latency, or operational expectations</td></tr>
<tr><td>Routing and bindings</td><td>What if no queue matches the routing key?</td><td>Unroutable messages (use mandatory publishing and confirms)</td></tr>
<tr><td>Acknowledgement</td><td>Do we ack after the receiver commits?</td><td>Lost work or duplicate side effects</td></tr>
<tr><td>Retries and poison messages</td><td>How are repeated failures delayed and finally quarantined?</td><td>Infinite redelivery loops and hidden loss</td></tr>
<tr><td>Operations</td><td>Who owns queue depth, age, consumer count, DLQ investigation?</td><td>Transport looks healthy while SLAs fail</td></tr>
<tr><td>Security</td><td>Which vhost, users, ACLs, TLS, and secret rotation?</td><td>Unauthorised access and exposed operational data</td></tr>
</tbody></table></div>
<p><strong>Quorum queue nuance:</strong> RabbitMQ 4.x has built-in delivery limits for quorum queues. Repeatedly failing messages can be discarded or dead-lettered depending on configuration. Configure and verify the DLX strategy rather than assuming a queue is automatically lossless. Prefer a policy for production dead-letter settings, and monitor the target DLQ.</p>
<p><strong>Production note:</strong> our Python scripts use classic queues and hard-coded local defaults. A production deployment needs explicit topology management, cluster/storage plan, credentials, certificate validation, reconnection, structured logs, metrics, and recovery playbooks.</p></section>
<section class="research-canvas__inventory" id="sap-case" data-reveal><header><p class="research-canvas__eyebrow">06 / SAP architecture</p><h2>Where RabbitMQ belongs in an SAP landscape</h2><p>Use a separate messaging layer when an independent service or partner worker should process a task asynchronously.</p></header>
<p><strong>Illustrative scenario:</strong> a released SAP interface provides a shipment-notification payload. An integration flow validates it and sends an external document-rendering request to RabbitMQ. The worker creates a PDF, stores the result, and records its status. The SAP business document remains owned by SAP.</p>
<ul><li><strong>SAP standard to check:</strong> availability of the released event/API/IDoc for the actual S/4HANA edition, release, and business object; do not invent a native RabbitMQ event source.</li>
<li><strong>SAP Integration Suite:</strong> SAP documents a RabbitMQ adapter for publishing/consuming, available through SAP Business Accelerator Hub with service-plan constraints. SAP Cloud Integration also has AMQP adapters. Verify the protocol, adapter version, connection and authentication options for the target tenant.</li>
<li><strong>End-to-end control:</strong> an iFlow status and a RabbitMQ acknowledgement do not prove that the PDF was created. Correlate <code>messageId</code>, SAP business reference, worker result, and final storage/status record.</li>
<li><strong>Do not:</strong> use a message handler to silently replace SAP standard posting logic or let an external worker invent its own inventory or FI state.</li></ul>
<p>The flow is: <strong>SAP business data → released interface → Integration Suite → RabbitMQ exchange → queue → worker → outcome/reconciliation</strong>. An SAP Event Mesh product is another architectural option and is not simply a different name for RabbitMQ.</p></section>
<section class="research-canvas__inventory" id="checkpoint" data-reveal><header><p class="research-canvas__eyebrow">07 / Architecture test</p><h2>Can you defend this choice?</h2><p>Answer the trade-off, not only the message flow.</p></header>
<p><strong>Case:</strong> A partner service needs to generate ASN documents one at a time, retry temporary failures, and send invalid payloads for manual review. Historical event replay is not a requirement. Would you choose RabbitMQ queues or Kafka?</p>
<p><strong>30-second answer:</strong> “I would start with a durable work queue and a dead-letter strategy. RabbitMQ suits asynchronous task distribution and clear acknowledgement control. I would define retries, idempotency, monitoring and ownership before selecting the adapter. Kafka becomes more attractive if many independent systems need a retained event history and replay.”</p>
<p><strong>Next challenge:</strong> a stakeholder says that the message has been acknowledged, but the external document is missing. What technical evidence distinguishes broker delivery from business completion? Compare both platforms in the <a href="/labs/enterprise-context/integrations/event-brokers/">decision guide</a>.</p></section>
<section class="research-canvas__inventory" id="references" data-reveal><header><p class="research-canvas__eyebrow">Documentation / boundaries</p><h2>Primary sources and version scope</h2><p>This learning guide uses the vendor documentation available on 22 November 2026. Local commands and code still require execution and human review.</p></header>
<ul><li><a href="https://www.rabbitmq.com/docs/download" target="_blank" rel="noopener">RabbitMQ installation and Docker</a> and <a href="https://www.rabbitmq.com/docs/management" target="_blank" rel="noopener">Management plugin</a>.</li>
<li><a href="https://www.rabbitmq.com/tutorials/tutorial-one-python" target="_blank" rel="noopener">Official AMQP 0.9.1 Python tutorial</a> and <a href="https://www.rabbitmq.com/docs/confirms" target="_blank" rel="noopener">acks and confirms</a>.</li>
<li><a href="https://www.rabbitmq.com/docs/quorum-queues" target="_blank" rel="noopener">Quorum queues and delivery limits</a>; <a href="https://www.rabbitmq.com/client-libraries/amqp-client-libraries" target="_blank" rel="noopener">AMQP 1.0 client libraries</a>.</li>
<li><a href="https://help.sap.com/docs/integration-suite/sap-integration-suite/rabbitmq-adapter" target="_blank" rel="noopener">SAP RabbitMQ adapter</a> and <a href="https://help.sap.com/docs/cloud-integration/sap-cloud-integration/5cc1a71231cb4cbfbfedb0cdc63e1488.html" target="_blank" rel="noopener">SAP AMQP adapter</a>.</li></ul>
<p>Human verification is pending. Validate release-specific adapter settings and tenant entitlements before any project use.</p></section>
<div class="research-canvas__support" data-reveal><p><a href="/labs/enterprise-context/integrations/">Back to Integration Architecture</a> · <a href="/labs/enterprise-context/integrations/kafka/">Kafka lab</a> · <a href="/labs/enterprise-context/integrations/event-brokers/">Choose the broker</a></p></div>
</div>