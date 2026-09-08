# Consolidation record

This repository replaces ten transaction-direction repositories that were
verified as generated scaffolds with no independent deployment configuration,
tests, or domain implementation. Eight had one initial scaffold commit; two
were empty.

The non-empty source commits are retained as merge parents in this repository:

- `continuum-credit-transfer-outbound` — `e948cc6be49e`
- `continuum-payment-ack-outbound` — `3d12eb9987f6`
- `continuum-payment-return-inbound` — `ac1923e11560`
- `continuum-payment-return-outbound` — `2ca45a8d6e7f`
- `continuum-request-for-payment-inbound` — `08fb0ae8036d`
- `continuum-request-for-payment-outbound` — `8e673a527186`
- `continuum-return-of-funds-inbound` — `237550c909ba`
- `continuum-return-of-funds-outbound` — `d0bd0df9c2bc`

`continuum-credit-transfer-inbound` and `continuum-payment-ack-inbound` had no
Git commits to retain. All ten route identities remain explicit and tested in
`supported_routes()`.
