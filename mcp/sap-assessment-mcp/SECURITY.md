# Security boundary

This package is read-only and local-first. It reads public files from a local checkout and writes only JSON-RPC responses to stdout.

It must not receive SAP credentials, client data, private assessment notes, production identifiers, or landscape-specific evidence. It does not connect to SAP, call remote URLs, execute assessment actions, or change local scoring history.

Treat all case content as public training material. Validate release-sensitive SAP product facts against primary sources before using them as factual authority.
