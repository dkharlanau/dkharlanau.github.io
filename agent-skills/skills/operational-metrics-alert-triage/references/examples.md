# Examples

All examples are synthetic.

## Example 1: queue depth alert
Queue depth crosses a threshold, but message age stays low and throughput is increasing after a planned traffic burst.

Result: signal valid but business impact low. Do not escalate as a major incident. Tune alert to include age and sustained-duration context rather than queue depth alone.

## Example 2: green API, failed business flow
API success rate is 99.9%, but order confirmations stop because accepted requests accumulate in an asynchronous queue.

The service metric is green while business completion is red. Add confirmation-lag or age-of-unconfirmed-order metric and correlate it with queue health.

## Example 3: duplicate cascade
One database issue triggers service latency, API error, worker retry, queue backlog, and business-delay alerts.

Five alerts describe one failure. Correlate them around the shared dependency and route one incident to the team that owns the first failing boundary.

## Example 4: false-positive cleanup
A batch job normally finishes between 02:00 and 02:20. An alert fires whenever it is not complete at 02:05.

Incident review shows repeated false positives. Tune the threshold using expected completion distribution and add a stronger signal for genuine overrun rather than simply suppressing the alert.
