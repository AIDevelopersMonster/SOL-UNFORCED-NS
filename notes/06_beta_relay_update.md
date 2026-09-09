# Note 06 — β-relay update after source audit

## Summary

A direct source audit of the OpenAI forced Navier–Stokes construction supports the following working picture.

1. The projected inviscid pulse operator is scale-invariant under a fixed carrier-magnitude rescaling \(n_\Phi\mapsto\beta n_\Phi\) at principal level.
2. Viscous damping scales as \(\beta^2\).
3. The growth/decay turning point shifts from \(|s|=u_*\) to
   \[
   y_\beta=\sqrt{(1+u_*^2)\beta^{-4/3}-1}.
   \]
4. Therefore a β-packet should be recentered at its own turning point rather than forced to share the original midpoint.

See `proofs/beta_phase_stability.md`.

## New obstruction

The earlier relay witness used a child with reduced coordinate near \(x_c\approx0.53\). The source cutoff in the published pulse construction is narrower than the raw pulse interval, so that witness is not automatically admissible without modifying the support/cutoff architecture.

A numerical scan also indicates that requiring *all* parents and child simultaneously inside a conservative common active window can eliminate the simple opposite-sign witness family. This suggests that asynchronous β-centering is not optional; it may be structurally necessary.

## Revised target

The local relay problem is now split into two lemmas:

### A. β-Pulse Stability Lemma

Show that for β in a fixed compact interval, the OpenAI pulse construction persists with:

- the same principal growing/decaying frame;
- β²-scaled damping;
- a β-dependent turning point and Gaussian envelope;
- the same coefficient-class losses up to uniform constants.

### B. Asynchronous Controlled-Overlap Relay Lemma

Construct two β-packets centered at different pulse coordinates whose supports overlap in a short relay collar and whose sum-frequency component lands in the growing branch of a child packet.

The key issue is no longer just algebraic phase closure. We must synchronize:

- physical support,
- β-dependent envelope centers,
- phase normals,
- growing/decaying signs,
- and the next-band frequency ratio.

## Current status

This is still pre-publication research. No exact local relay lemma is proved yet.
