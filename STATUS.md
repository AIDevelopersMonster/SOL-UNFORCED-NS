# STATUS

**Project:** SOL-UNFORCED-NS  
**Working version:** v0.4 with v0.5 candidate under audit  
**Date:** 2026-09-10  
**Branch:** `research/local-beta-relay-v0.2`

## Corrected carrier law

The bootstrap/v0.3 comparison

\[
\Omega_\ell\asymp Q_\ell^{-(1+h)/2},
\qquad
\Omega_{\ell+1}/\Omega_\ell=2^{(1+h)/2}
\]

was retracted when interpreted as a physical frequency jump between overlapping dyadic charts at a fixed physical point. The chart scaling of \(\lambda_0\) cancels the apparent \(Q\)-dependence. The corrected intrinsic leading carrier scale is

\[
\boxed{\Omega_{\rm phys}(q)\asymp q^{-(1+h)/2}.}
\]

See `proofs/chart_invariant_carrier_scale.md`.

## v0.4 established local design

The current fully audited model branch uses

\[
\beta_1=\frac{25}{16},
\qquad
\beta_2=\frac9{16},
\qquad
\beta_1-\beta_2=1,
\]

with desired difference child phase \(\Phi_c=\Phi_1-\Phi_2\).

The reduced and finite-\(u_*\) envelope resonance are proved; the desired principal growing projection is nonzero with a strong source-normalized lower bound; the unwanted sum sideband has a stable inverse.

However, the first child-minus-catalyst feedback mode `(1,-2)` is uniformly growing. Exact compact support of a correction then imposes endpoint compatibility moments. This invalidates the earlier stable-only contraction idea and leads to a Lyapunov-Schmidt / exponential-dichotomy correction problem.

The abstract two-collar theorem `proofs/two_collar_compatibility_rank.md` proves that one complex compatibility moment plus a prescribed complex child output can be solved with two independent complex relay-collar amplitudes whenever the feedback coupling has fixed nonzero sign.

## v0.5 integral-beta candidate

A cleaner candidate is now under audit:

\[
\boxed{
\beta_1=2,
\qquad
\beta_2=1,
\qquad
\beta_1-\beta_2=1,
\qquad
x_1=\frac45.
}
\]

Its corrected reduced envelope resonance is rigorously certified:

\[
\boxed{
\frac{89}{100}<y_0<\frac{8901}{10000},
}
\]

with

\[
y_0\approx0.8900876081470894,
\qquad
x_{c,0}=\frac85-y_0\approx0.7099123918529107.
\]

The orientation is

\[
F_2(4/5)<0,
\qquad
F_1(y_0)>0,
\qquad
F_1(x_{c,0})>0.
\]

The unwanted sum branch has \(\beta_+=3\) and is strongly decaying.

Most importantly, the first v0.4 dangerous feedback mode now has

\[
T_{1,-2}=\beta_1-2\beta_2=0,
\]

so its principal inviscid growing term vanishes exactly and only viscous damping remains. See `proofs/integral_beta_v05_reduced_resonance.md`.

This is a genuine architectural improvement, but v0.5 is **not yet promoted to the active design** until finite-\(u_*\) persistence, source-normalized polarization, and the low-generation harmonic table are completed.

## Other proved/derived layers

**DERIVED:** chart-invariant physical carrier scaling at fixed physical point.

**DERIVED WORKING PROPOSITION:** beta rescaling preserves the principal inviscid eigendirections while viscous damping scales quadratically in carrier magnitude; exact beta turning/envelope formulas are recorded in `proofs/beta_phase_stability.md`.

**PROVED GEOMETRIC LEMMA:** translated auxiliary-torus rectangles realize distinct local pulse coordinates in one common overlap collar while retaining exact separation outside designated relay supernodes.

**PROVED HARMONIC-LATTICE LEMMA:** the two-generator phase lattice has a uniform carrier lower bound, so high lattice modes become increasingly viscously stable and only finitely many low modes can require individual resonance analysis at fixed `u_*`.

**PROVED ABSTRACT CONTROL LEMMA:** two separated complex relay collars give full rank for one complex child-output condition plus one complex endpoint-compatibility moment.

## Not proved

- Full Controlled-Overlap Local Difference-Relay Lemma for actual localized curl-generated packets.
- Finite-\(u_*\) persistence and source-class embedding of the new v0.5 integral-beta candidate.
- Complete low-generation resonance/compatibility table for v0.5.
- Exact solution of all non-designated feedback/cutoff/curl residuals with zero external force.
- A transported physical-scale inheritance theorem taking a generated child at \(q_j\) into a valid parent at some later \(q_{j+1}<q_j\).
- A finite or infinite autonomous Navier–Stokes relay chain.
- Exact global closure \(R(u,p)\equiv0\).
- Finite-time blowup for unforced 3D Navier–Stokes.

## Publication threshold

**Not reached.**

The branch now contains several independent local lemmas and one genuine compatibility obstruction, but a technical preprint should wait until either the v0.5 local relay survives finite-\(u_*\) and localized-PDE audit, or the compatibility/obstruction line is developed into an independently complete theorem.
