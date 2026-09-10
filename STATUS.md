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

The theorem proves the half-step arithmetic gap and a **uniform principal action deficit**: there exist `M_0` and `delta_*>0` such that for every `M>=M_0` and every non-designated principal-growing lattice mode,

\[
\boxed{
S_M(a,b)-\mathcal E_{|T|,M^2}(\xi_M(a,b))\le-\delta_*.
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

## Source-localized action preservation — finite stage CLOSED

A finite-stage transfer theorem is now proved in

`proofs/source_localized_action_preservation.md`.

Fix one sufficiently large v0.8 design `M`, freeze `u_*=M^2`, and work in a bounded relay collar `|v-v_0|<=L_0`. Because every translated pulse coordinate has derivative `1/L_s`, the local coordinates satisfy

\[
 x_1(v)=x_M+\theta(v),\qquad
 x_2(v)=y_M+\theta(v),\qquad
 x_c(v)=x_{c,M}+\theta(v),
\]

with

\[
|\theta(v)|=O(S_*^{-1}).
\]

For every nonzero-tangential lattice phase its effective reduced slope obeys the exact covariance

\[
\boxed{
\xi_{a,b}(v)=\xi_{a,b}(v_0)+\theta(v).
}
\]

Combining this with the v0.8 pointwise global action gap, negativity of the base actions, and a high-degree/finite-degree split yields a uniform collar estimate: every non-designated principal-growing genealogy retains a fixed fraction of the center action deficit throughout the relay collar.

The following source operations have now been audited against the OpenAI coefficient calculus:

- selected coefficient products inside the designated overlap supernode;
- common-torus pullback;
- normalized coefficient derivatives;
- curl generation and curl remainder;
- pulse amplitude inversion;
- supported linear residual operators;
- wave-wave transport using the incompressibility gain;
- relay-compatible shifted temporal cutoffs;
- conversion to every fixed finite physical derivative order.

For every fixed finite correction depth, these operations introduce only powers of `epsilon`, `Q`, `S_*`, and fixed coefficient constants. None introduces `exp(+cS_*)`. Therefore every non-designated action-subcritical genealogy retains

\[
\boxed{e^{-c_MS_*}}
\]

through the finite-stage localized curl-generated packet calculus.

This closes the previously stated source-localized action-preservation barrier **at finite stage**.

## Other established layers

**DERIVED:** chart-invariant physical carrier scaling at fixed physical point.

**PROVED GEOMETRIC LEMMA:** translated auxiliary-torus rectangles realize distinct local pulse coordinates in a prescribed common overlap collar while preserving exact separation outside relay supernodes.

**PROVED PRINCIPAL ALGEBRA:** desired difference-harmonic source has a robust nonzero growing-child projection after correcting the source slope to `s=u_*x`.

**PROVED HARMONIC-LATTICE LEMMA:** high lattice modes are increasingly viscously stable and only finitely many low modes require separate treatment for a fixed design.

**PROVED ABSTRACT CONTROL LEMMA:** if a finite compact-support compatibility condition survives, two separated complex relay collars give full rank for one complex child-output condition plus one complex endpoint moment.

**PROVED FINITE-STAGE SOURCE TRANSFER:** the v0.8 global action deficit survives every fixed finite composition of the localized source operators audited above.

## Immediate frontier

The remaining local obstruction is no longer the pointwise lattice, off-window modes, large-`u_*` tuning, or finite-stage localization.

The sharp target is now a **stage-uniform infinite-lattice zero-force closure**.

A natural analytic lattice norm is

\[
\|z\|_\sigma
=
\sum_{(a,b)\in\mathbb Z^2}
 e^{\sigma(|a|+|b|)}
\|z_{a,b}\|_{\rm packet},
\]

augmented by the v0.8 action weight. The exponential lattice weight is submultiplicative and therefore compatible with quadratic convolution.

Need to prove simultaneously:

1. quadratic lattice convolution is bounded in a packet norm carrying the action weight;
2. after removing a finite low block, the full linearized lattice symbol has stable/unstable right inverses with constants uniform in harmonic index;
3. the finite mean/endpoint compatibility block can be solved exactly;
4. the nonlinear correction map is contractive in the resulting weighted space, giving **zero external force**.

## Not proved

- Stage-uniform infinite-lattice right inverse and contraction.
- Exact compact-support solution of the full compatibility block.
- Exact local zero-force residual closure.
- Full Controlled-Overlap Local Difference-Relay Theorem for the infinite corrected packet system.
- Physical-scale inheritance from a generated child at `q_j` to a valid parent at a later smaller `q_{j+1}`.
- A finite or infinite autonomous Navier–Stokes relay chain.
- Exact global closure `R(u,p)==0`.
- Finite-time blowup for unforced 3D Navier–Stokes.

## Publication threshold

**Not yet crossed, but now very close at the local-theorem level.**

The complete principal two-generator lattice and the finite-stage source-localized action calculus are both under control. Publication should wait for the stage-uniform weighted lattice closure. If that closure succeeds, the exact local autonomous relay module itself merits immediate technical-preprint assembly even before physical-scale inheritance is solved. If it fails for a clean structural reason, that obstruction may itself be publishable.