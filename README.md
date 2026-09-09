# SOL-UNFORCED-NS

**Research bootstrap repository — v0.1, 2026-09-09**

Goal: investigate whether an **autonomous finite-time cascade** can coexist with viscosity in the 3D incompressible unforced Navier–Stokes equations

\[
\partial_t u + (u\cdot\nabla)u-\nu\Delta u+\nabla p=0,
\qquad
\nabla\cdot u=0,
\qquad
\nu>0.
\]

## Status

This repository **does not claim a solution** of the unforced 3D Navier–Stokes regularity problem.

The current work is a mechanism study inspired by, but distinct from, the 2026 OpenAI Euler and forced Navier–Stokes constructions and the Buckmaster–Alpöge / Córdoba–Martínez-Zoroa program.

Current target:

> **Controlled-Overlap Local β-Relay Lemma**  
> Can two deliberately overlapping localized viscous packets generate, through their quadratic interaction, the growing eigenmode of a child packet at the next scale while all unwanted branches remain perturbative or are suppressed by viscosity?

## Current working picture

Three barriers have been isolated:

1. **Direct Euler-to-NS transfer fails on the published Euler scale hierarchy.**  
   Viscous damping dominates the parent-shear amplification at those frequencies.

2. **Backward storage of future high-frequency seeds is incompatible with heat smoothing.**  
   A high-frequency child should be created late and forward in time, not hidden at the same frequency in \(u_0\).

3. **Standard same-band \(m=1\) OpenAI pulses do not frequency-match the next physical band.**  
   This motivates a one-parameter family of intermediate **β-relay waves**.

A candidate principal-level mechanism has been found:

\[
\text{decaying old packet}
+
\text{live catalyst}
\longrightarrow
\text{growing child},
\]

with the undesired difference branch lying in a strong viscous decay region.

See `STATUS.md` and `proofs/local_beta_relay_lemma.md`.

## Repository map

- `notes/` — chronological research notes and barriers.
- `proofs/` — statements, derivations, and proof obligations.
- `experiments/` — reproducible numerical checks of candidate parameters.
- `results/` — machine-readable candidate parameter sets.
- `references/` — primary sources.
- `docs/` — research and claims protocol.

## Immediate next step

Prove or kill the local relay at the level of the actual localized curl-generated packet class:

\[
\text{parents}
\to
\text{child }W^{1/2}
+
\text{remainder }W^{1-\delta}.
\]

Only after that should the project be considered to have a publication-grade local theorem.
