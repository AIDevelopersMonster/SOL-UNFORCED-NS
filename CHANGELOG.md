# CHANGELOG

## v0.5 — 2026-09-11

Mean-block closure audit and radial reformulation.

- Decomposed the differentiated angular-mean map into temporal/transport, five-dimensional moment, wave-covariance, signed-stress, supported-remnant, and radial compactification blocks.
- Isolated positive small factors for every visible **non-radial** nonlinear block:
  \[
  \varepsilon^{1-2\kappa_s},\quad
  \varepsilon^{0.9-2\kappa_s},\quad
  \varepsilon^{1/2-\kappa_s},\quad
  \varepsilon^{0.17},\quad
  \rho_\ell.
  \]
- Corrected the previous Gevrey radial claim: compact radial remainders are stretched-exponentially small only **across a fixed Gevrey-radius gap**; unrestricted same-radius `o(1)` operator norm fails because of near-resonant torus modes.
- Added an exact one-sided radial characteristic inverse as the preferred input-output alternative to two-sided radial compact support.
- Marked `proofs/forward_relay_input_output_closure.md` superseded wherever it asserted complete local zero residual; the valid theorem remains exact nonzero-harmonic forward closure conditional on the angular mean.
- Updated `STATUS.md`: current local frontier is the coupled temporal-radial characteristic mean theorem, including a quantitative exponent-preserving `m -> z(m)` difference estimate and simultaneous radial pressure/stress forwardization.

## v0.4 — 2026-09-10

Major carrier-scaling correction and relay redesign.

- Retracted the claim that overlapping dyadic charts produce a physical carrier jump \(2^{(1+h)/2}\).
- Derived chart invariance of the leading physical carrier at fixed physical point and the intrinsic law \(\Omega_{\rm phys}\asymp q^{-(1+h)/2}\).
- Deprecated the physical interpretation of all `17/12` cross-band relay witnesses.
- Rebuilt the local relay around the **difference harmonic** with \(\beta_1=25/16\), \(\beta_2=9/16\), so \(\beta_1-\beta_2=1\).
- Identified the unwanted sum branch \(\beta_+=17/8\) as strongly viscously decaying.
- Added exact difference-phase locking, updated resonance certificates, finite-\(u_*\) persistence, and principal growing-projection analysis.
- Separated the local same-\(q\) relay problem from the new **physical-scale inheritance** problem \(q_j\to q_{j+1}\).

## v0.1 — 2026-09-09

Initial research bootstrap: Euler-viscosity barrier, backward-heat barrier, beta-relay geometry, controlled-overlap proof obligation, and reproducible parameter checks.
