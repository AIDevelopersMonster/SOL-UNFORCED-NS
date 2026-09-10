# Note 06 — beta-relay update after carrier audit

## Stable part of the beta analysis

The source pulse equation continues to support the following working facts:

1. fixed rescaling \(n_\Phi\mapsto\beta n_\Phi\) leaves the principal inviscid projected operator unchanged;
2. leading viscous damping acquires \(\beta^2\);
3. the exact turning point is
   \[
   y_\beta=\sqrt{(1+u_*^2)\beta^{-4/3}-1};
   \]
4. the exact beta envelope and its large-\(u_*\) primitive remain valid.

See `proofs/beta_phase_stability.md`.

## What changed

The beta family is no longer used to match a fictitious neighboring-chart physical frequency ratio. The chart audit shows that the leading physical carrier at a fixed point is independent of dyadic chart \(Q\).

The v0.4 beta family is used instead to engineer an exact local harmonic relation:

\[
\boxed{\beta_1-\beta_2=1.}
\]

This makes the difference harmonic a standard unit-beta child while leaving the sum harmonic at high beta and strong viscous decay.

## Current design

\[
\beta_1=25/16,
\qquad
\beta_2=9/16,
\qquad
\beta_+=17/8.
\]

Translated auxiliary-torus geometry lets the parent, catalyst and child meet at different local pulse coordinates inside one physical overlap collar. The next tasks are exact phase admissibility, localized curl interaction, and exact correction of the damped sum branch.

The eventual frequency cascade, if it exists, must come from decreasing physical \(q\), not changing chart labels.
