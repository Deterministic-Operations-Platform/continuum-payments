# Continuum Payments

Coherent payment-message workflow primitives for the Continuum deterministic
operations platform.

The module represents five generic message families in both inbound and
outbound directions:

- credit transfer
- payment acknowledgement
- payment return
- request for payment
- return of funds

It does not contain rail-specific schemas, customer data, network connectivity,
or claims of payment-network certification. Those concerns belong in versioned
adapters owned by a real deployment.

## Install and test

```bash
python -m pip install .
python -m unittest discover -s tests -v
python -m compileall -q src tests
```

## Design

`PaymentEnvelope` binds a message identifier, family, direction, and immutable
payload view. `PaymentProcessor` produces a deterministic validation result and
evidence list. The ten former repository identities are represented by
`supported_routes()` rather than duplicated deployables.

See [CONSOLIDATION.md](CONSOLIDATION.md) for source-history attribution.
