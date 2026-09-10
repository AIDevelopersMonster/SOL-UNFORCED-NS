# STATUS

**Project:** SOL-UNFORCED-NS  
**Working version:** v0.6 preferred candidate  
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

## v0.4 established but superseded as preferred design

The v0.4 difference design

\[
\beta_1=25/16,\qquad \beta_2=9/16,\qquad \beta_1-\beta_2=1
\]

remains a valid model benchmark: its reduced and finite-`u_*` envelope resonance, desired projection, and first unwanted sum-sideband stable inverse were proved. However, its `(1,-2)` feedback mode is genuinely growing and requires a finite-dimensional compatibility solve. The two-collar theorem proves rank for one complex compatibility moment plus one complex child-output condition, but this is no longer the preferred architecture.

## v0.5 integral-beta improvement

The choice

\[
\beta_1=2,\qquad \beta_2=1
\]

eliminates the inviscid growth term of the first child-minus-catalyst feedback mode `(1,-2)` exactly because

\[
T_{1,-2}=2-2=0.
\]

The original v0.5 point `x_1=4/5` nevertheless leaves the next regenerated growing mode `(2,-3)` action-supercritical. Therefore v0.5 is now retained as an intermediate design step, not the preferred candidate.

## v0.6 preferred integral-beta design

The current preferred model parameters are

\[
\boxed{
\beta_1=2,
\qquad
\beta_2=1,
\qquad
x_1=\frac34.
}
\]

The desired difference harmonic remains unit-beta:

\[
2-1=1.
\]

The certified reduced resonance is

\[
\boxed{
0.7854<y_0<0.7855,
}
\]

with

\[
y_0\approx0.7854873695884608,
\qquad
x_{c,0}=\frac32-y_0\approx0.7145126304115392.
\]

The exact finite-`u_*` envelope resonance is now proved for every

\[
\boxed{u_*\ge20,}
\]

with a unique root

\[
\boxed{19/25<y_{u_*}<4/5.}
\]

Representative values are

\[
y_{20}\approx0.786166291392389,
\quad
y_{50}\approx0.785595530752873,
\quad
y_{100}\approx0.785514393236699.
\]

The orientation is

\[
\boxed{
\text{decaying beta-2 parent}
+\text{ growing beta-1 catalyst}
\to
\text{ growing beta-1 child}.
}
\]

## First feedback filter

For v0.6 the first feedback mode

\[
r_0=(1,-2)
\]

has zero tangential coefficient and is purely viscous at principal level.

The next regenerated unit-beta mode is

\[
m_2=(2,-3),
\]

which is locally growing. However, `proofs/integral_beta_v06_finite_u_action_filter.md` proves the exact finite-`u_*` action deficit

\[
\boxed{
\Delta_{2,u_*}< -\frac1{200}
}
\]

for every `u_*>=20`.

Thus even after maximal homogeneous amplification from its generation point to its natural unit-beta peak, the mode retains a factor

\[
\boxed{
\exp\!\left(-\frac{\lambda_0L_s}{200u_*}\right)
=e^{-cS_*}.
}
\]

The same theorem proves an in-window filter for the whole unit-beta radial-feedback ladder

\[
m_a=(a,1-2a),\qquad a\ge2:
\]

apart from the deliberately resonant desired child `m_1`, every such mode that is generated inside the standard unit-beta growing window is exponentially action-subcritical.

This is currently the strongest local structural result in the branch.

## Other proved/derived layers

**DERIVED:** chart-invariant physical carrier scaling at fixed physical point.

**DERIVED WORKING PROPOSITION:** beta rescaling preserves principal inviscid eigendirections while viscous damping scales quadratically in carrier magnitude; exact beta turning/envelope formulas are in `proofs/beta_phase_stability.md`.

**PROVED GEOMETRIC LEMMA:** translated auxiliary-torus rectangles realize distinct local pulse coordinates in one common overlap collar while retaining exact separation outside designated relay supernodes.

**PROVED PRINCIPAL ALGEBRA:** desired difference-harmonic growing projection is nonzero, with source-normalized lower bounds after correcting `s=u_*x`.

**PROVED HARMONIC-LATTICE LEMMA:** the two-generator phase lattice has a uniform carrier lower bound; high lattice modes become increasingly viscously stable, so only finitely many low modes can require individual analysis for fixed `u_*`.

**PROVED ABSTRACT CONTROL LEMMA:** two separated complex relay collars give full rank for one complex child-output condition plus one complex endpoint-compatibility moment. This remains available if a future low mode cannot be removed by arithmetic/action design.

## Not proved

- Full Controlled-Overlap Local Difference-Relay Lemma for the actual localized curl-generated packet system.
- Source-level proof that the v0.6 action gaps survive every cutoff/curl/transport/Leray correction with unchanged exponential action.
- Complete classification and disposal of low **off-window** lattice modes.
- Exact solution of all non-designated residuals with zero external force.
- Physical-scale inheritance from a generated child at `q_j` to a valid parent at a later smaller `q_{j+1}`.
- A finite or infinite autonomous Navier–Stokes relay chain.
- Exact global closure `R(u,p) == 0`.
- Finite-time blowup for unforced 3D Navier–Stokes.

## Publication threshold

**Not reached, but substantially closer.**

The v0.6 action-filter theorem is a genuine theorem-level local advance, but the branch should not yet be promoted to a technical preprint until the localized packet calculus and off-window low modes are closed. If those two steps succeed, the local autonomous relay module itself becomes a serious publication candidate even before physical-scale inheritance is solved.
