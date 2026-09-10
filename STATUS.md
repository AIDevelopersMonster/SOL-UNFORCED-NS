# STATUS

**Project:** SOL-UNFORCED-NS  
**Working version:** v0.4  
**Date:** 2026-09-10  
**Branch:** `research/local-beta-relay-v0.2`

## Current correction

### RETRACTED

The bootstrap/v0.3 comparison

\[
\Omega_\ell\asymp Q_\ell^{-(1+h)/2},
\qquad
\Omega_{\ell+1}/\Omega_\ell=2^{(1+h)/2}
\]

when interpreted as a physical frequency jump between overlapping dyadic charts at a fixed physical point.

The omitted chart scaling of \(\lambda_0\) cancels the apparent \(Q\)-dependence. The corrected intrinsic leading carrier scale is

\[
\boxed{
\Omega_{\rm phys}(q)\asymp q^{-(1+h)/2}
}
\]

up to the profile factor recorded in `proofs/chart_invariant_carrier_scale.md`.

Therefore the old physical locking condition

\[
\beta_1+\beta_2=17/12
\]

and all witnesses whose physical interpretation depended on it are deprecated.

## Current v0.4 design

Use the desired **difference branch**

\[
\boxed{
\beta_1=\frac{25}{16},
\qquad
\beta_2=\frac9{16},
\qquad
\beta_1-\beta_2=1.
}
\]

Choose

\[
x_1=\frac{29}{32}.
\]

The corrected reduced envelope model has a unique transverse resonance

\[
1.226<y_0<1.227,
\qquad
x_{c,0}=\beta_1x_1-\beta_2y_0\approx0.7263647213.
\]

At the root,

\[
F_{\beta_1}(x_1)<0,
\qquad
F_{\beta_2}(y_0)>0,
\qquad
F_1(x_{c,0})>0.
\]

The unwanted sum branch has

\[
\beta_+=\beta_1+\beta_2=\frac{17}{8}
\]

and is strongly decaying at its induced local coordinate.

## Proved / derived layers

**DERIVED from source normalization:** chart-invariant carrier scaling at fixed physical point.

**DERIVED WORKING PROPOSITION:** beta-rescaling preserves the principal inviscid eigendirections while viscous damping scales as \(\beta^2\); exact beta turning point and envelope primitive are recorded in `proofs/beta_phase_stability.md`.

**PROVED GEOMETRIC LEMMA:** translated auxiliary-torus rectangles can realize distinct local pulse coordinates in one common overlap collar while preserving separation outside designated relay supernodes.

**PROVED REDUCED LEMMA:** the v0.4 same-scale difference relay has a unique transverse reduced resonance in the explicit rational interval \((613/500,1227/1000)\).

**PROVED MODEL THEOREM:** the v0.4 resonance persists in the exact finite-\(u_*\) envelope model for all \(u_*\ge20\).

**DERIVED PHASE-LOCKING LEMMA:** defining \(\Phi_c=\Phi_1-\Phi_2\) gives exact harmonic closure and automatically preserves angular periodicity because the rounded quantities \(kp_j\) are integers.

**PROVED PRINCIPAL ALGEBRA:** the desired difference interaction of the source growing polarizations has a strictly nonzero growing-child projection; a quantitative witness lower factor is recorded in `proofs/difference_branch_projection.md`.

**CONDITIONAL COEFFICIENT LEMMA:** during a bounded tail-seeding collar, parent-child feedback is exponentially smaller than the desired parent-parent seed, conditional on the full localized phase/PDE embedding.

## Not proved

- Full Controlled-Overlap Local beta-Relay Lemma for actual localized curl-generated packets.
- Exact solution of the unwanted sum sideband and all feedback/cutoff/curl residuals with **zero external force**.
- A transported physical-scale inheritance theorem taking a generated child at \(q_j\) into a valid parent at some later \(q_{j+1}<q_j\).
- A finite or infinite autonomous Navier–Stokes relay chain.
- Exact global closure \(R(u,p)\equiv0\).
- Finite-time blowup for unforced 3D Navier–Stokes.

## Publication threshold

**Not reached.**

The present results justify GitHub versioning and internal theorem files. A technical preprint becomes warranted when the **localized difference-branch relay module** is closed with a quantitative growing projection and an exact correction mechanism for the non-designated terms, or if an independently interesting obstruction theorem emerges first.
