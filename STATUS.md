# STATUS

**Project:** SOL-UNFORCED-NS  
**Working version:** v0.8 preferred model candidate  
**Date:** 2026-09-10  
**Branch:** `research/local-beta-relay-v0.2`

## Corrected carrier law

The bootstrap/v0.3 comparison

\[
\Omega_\ell\asymp Q_\ell^{-(1+h)/2},
\qquad
\Omega_{\ell+1}/\Omega_\ell=2^{(1+h)/2}
\]

was retracted when interpreted as a physical frequency jump between overlapping dyadic charts at a fixed physical point. The corrected intrinsic leading carrier scale is

\[
\boxed{\Omega_{\rm phys}(q)\asymp q^{-(1+h)/2}.}
\]

See `proofs/chart_invariant_carrier_scale.md`.

## v0.4–v0.7 historical progression

- **v0.4:** valid same-scale difference relay, but `(1,-2)` is a genuinely growing feedback mode and exact compact support creates a compatibility problem.
- **v0.5:** integral-beta choice `2-1=1` kills the inviscid growth term of `(1,-2)` exactly, but the first regenerated unit-beta descendant is action-supercritical.
- **v0.6:** moving the parent to `x_1=3/4` creates an in-window action filter for the radial feedback ladder, including a proved finite-`u_*` deficit for `(2,-3)`.
- **v0.7:** rational half-step tuning closes the off-window principal lattice at one moderate tuned value `u_*≈49.36`, but leaves a possible source cone-threshold issue.

## v0.8 preferred large-u half-step family

The current preferred **model-level** architecture is the asymptotic half-step family in

`proofs/integral_beta_v08_large_u_halfstep_family.md`.

For an integer `M`, set

\[
\boxed{
\beta_1=2,
\qquad
\beta_2=1,
\qquad
u_M=M^2,
\qquad
\delta_M=\frac1{2M}.
}
\]

Choose a relay root `x_M` and define

\[
y_M=(1+\delta_M)x_M,
\qquad
x_{c,M}=(1-\delta_M)x_M.
\]

Then

\[
2x_M-y_M=x_{c,M},
\]

so the desired difference harmonic is exactly unit-beta.

The theorem proves that for every sufficiently large integer `M` there exists an exact finite-`u_*` resonance

\[
\boxed{u_*=M^2}
\]

with

\[
x_M\to2^{-2/3},
\qquad
y_M\to2^{-2/3},
\qquad
x_{c,M}\to2^{-2/3}.
\]

Thus the admissible design values satisfy

\[
\boxed{u_*\to\infty.}
\]

This removes the v0.7 concern that the tuned root might lie below an unknown profile-dependent cone threshold: choose one sufficiently large `M` after that threshold is known, then freeze it for the dyadic cascade.

## Complete principal lattice action filter

For a lattice mode `(a,b)`, define

\[
T=2a+b,
\qquad
N=(2M+1)T-2a.
\]

Then its reduced radial coefficient is exactly

\[
\boxed{r_{a,b}=\frac{x_M}{2M}N.}
\]

The theorem proves the half-step arithmetic gap and, more importantly, a **uniform principal action deficit**: there exist `M_0` and `delta_*>0` such that for every `M>=M_0` and every non-designated principal-growing lattice mode,

\[
\boxed{
S_M(a,b)
-
\mathcal E_{|T|,M^2}(\xi_M(a,b))
\le-\delta_*.
}
\]

The only action-resonant nonzero modes are the deliberately retained catalyst and desired child (plus conjugates). Modes with `T=0` are purely viscous at principal level. Every other growing harmonic is action-subcritical.

For one fixed sufficiently large `M`, since

\[
L_s\asymp S_*,
\]

the post-amplification suppression is

\[
\boxed{
\exp(-\delta_*\lambda_0L_s/M^2)=e^{-c_M S_*}.
}
\]

Hence the complete two-generator harmonic lattice is filtered at the principal envelope level, including the previously problematic off-window modes.

This is now the strongest model theorem in the branch.

## Other established layers

**DERIVED:** chart-invariant physical carrier scaling at fixed physical point.

**DERIVED WORKING PROPOSITION:** beta rescaling preserves principal inviscid eigendirections while viscous damping scales quadratically in carrier magnitude; exact beta turning/envelope formulas are in `proofs/beta_phase_stability.md`.

**PROVED GEOMETRIC LEMMA:** translated auxiliary-torus rectangles realize distinct local pulse coordinates in a prescribed common overlap collar while preserving exact separation outside relay supernodes.

**PROVED PRINCIPAL ALGEBRA:** desired difference-harmonic source has a robust nonzero growing-child projection after correcting the source slope to `s=u_*x`.

**PROVED HARMONIC-LATTICE LEMMA:** high lattice modes are increasingly viscously stable and only finitely many low modes can require separate treatment at fixed design parameters.

**PROVED ABSTRACT CONTROL LEMMA:** if a residual low compatibility condition survives later source-level audit, two separated complex relay collars give full rank for one complex child-output condition plus one complex endpoint moment.

## Immediate frontier

The model-level carrier/envelope/lattice architecture is now substantially cleaner. The next decisive theorem is:

### Source-localized action preservation

Prove that replacing reference waves by the actual localized curl-generated source packets changes the action bookkeeping only through algebraic/polynomial prefactors:

\[
S_*^C\varepsilon^\rho,
\]

or already-flat factors, but **does not create an exponential gain of order `e^{+cS_*}`** capable of erasing the v0.8 action deficit.

The audit must include:

1. curl-generated remainder classes from Lemma 7.7;
2. slow and bounded-`v` collar cutoffs;
3. phase transport defects and `O(S_*^{-1})` frame/Leray errors;
4. common-torus coordinate changes;
5. stable/unstable one-sided inverses and exact compact-support compatibility;
6. nonlinear products of already-subcritical correction modes.

Only after this theorem is proved should the branch attempt a full exact zero-force local fixed point.

## Not proved

- Full Controlled-Overlap Local Difference-Relay Lemma for actual localized curl-generated packets.
- Source-localized preservation of the v0.8 global action deficit.
- Exact zero-force solution of all non-designated residuals.
- Physical-scale inheritance from the generated child at `q_j` to a valid parent at a later smaller `q_{j+1}`.
- A finite or infinite autonomous Navier–Stokes relay chain.
- Exact global closure `R(u,p) == 0`.
- Finite-time blowup for unforced 3D Navier–Stokes.

## Publication threshold

**Not reached yet, but the model-level publication threshold is close.**

The v0.8 theorem is now a coherent nontrivial result: arbitrarily large admissible `u_*`, exact finite-`u_*` resonance, half-step small-divisor protection, and a complete principal lattice action filter. I would still wait before a standalone preprint because its significance for the actual Navier–Stokes packet construction depends on the next source-localized action-preservation theorem. If that theorem closes, the local relay architecture should be assembled immediately into a technical preprint even before physical-scale inheritance is solved.
