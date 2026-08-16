# Examples

## Daily file import recovery

The procedure starts only after a failed import alert. Preconditions include the original file, checksum, target batch state, and approval to reprocess. A retry step checks whether duplicate creation is possible. If idempotency is unknown, the procedure stops and escalates instead of retrying blindly.

## User access onboarding

The stable procedure defines required approvals, identity checks, role request, expected provisioning result, evidence, and validation. User-specific names and roles belong in the run record, not the procedure definition.

## Production deployment checklist

Each deployment step records expected result and evidence. Stop conditions appear before database migration and traffic switching. Rollback ownership and go/no-go authority are explicit. Post-deployment validation includes business transactions, not only infrastructure health.
