# STATUS

**Project:** SOL-UNFORCED-NS  
**Working version:** v0.6 preferred / v0.7 global-filter candidate  
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

## v0.6 preferred design

The current broadly robust model candidate uses

\[
\beta_1=2,\qquad \beta_2=1,\qquad x_1=\frac34.
\]

Its exact finite-`u_*` resonance is proved for every `u_*>=20`, the first feedback mode `(1,-2)` is purely radial at principal level, and every in-window unit-beta feedback-ladder descendant beyond the desired child is action-subcritical.

## v0.7 rational half-step candidate

A sharper candidate was introduced to close the previously open off-window low-mode problem. It uses

\[
\boxed{
\beta_1=2,
\qquad
\beta_2=1,
\qquad
x_1=\frac{29}{40},
\qquad
y=\frac{1073}{1440},
\qquad
x_c=\frac{203}{288}.
}
\]

These coordinates satisfy the exact desired relation

\[
2x_1-y=x_c.
\]

The unit-beta feedback ladder has

\[
x_a=\frac{1073-58a}{1440},
\]

so zero lies exactly halfway between `a=18` and `a=19`; the near-zero off-window accident is replaced by a fixed arithmetic gap.

Define the exact finite-`u` resonance residual

\[
R(u)=\mathcal E_{2,u}(29/40)
+\mathcal E_{1,u}(1073/1440)
-\mathcal E_{1,u}(203/288).
\]

Outward interval arithmetic certifies

\[
R(20)<0<R(100),
\]

so at least one tuned

\[
\boxed{u_\dagger\in(20,100)}
\]

exists. Numerically,

\[
\boxed{u_\dagger\approx49.35646602870114.}
\]

At any such tuned root, the entire two-generator lattice can be parameterized by integers

\[
T=2a+b,
\qquad
N=37T-2a,
\]

with exact radial coefficient

\[
r=\frac{29}{1440}N.
\]

`proofs/integral_beta_v07_global_action_filter.md` proves at the principal exact-envelope/lattice level that every non-designated growing lattice mode is action-subcritical. In particular there is a uniform gap

\[
\boxed{
S_{a,b}
-
\mathcal E_{|T|,u_\dagger}
\left(\frac{29|N|}{1440|T|}\right)
< -0.15
}
\]

for every non-designated growing mode. Hence even the previously open off-window modes retain an `e^{-cS_*}` deficit after maximal homogeneous amplification.

This is stronger than the v0.6 in-window filter, but v0.7 is **not yet promoted to preferred design** for one important reason: the source construction only requires `u_*` to exceed a profile-dependent cone-margin threshold, and the repository has not yet proved that some tuned resonance can be placed above an arbitrarily large admissible threshold.

## Other proved/derived layers

- Chart-invariant physical carrier scaling at fixed physical point.
- Beta-dependent envelope/turning formulas.
- Translated auxiliary-torus overlap geometry.
- Exact difference-phase locking.
- Source-normalized nonzero growing projection.
- Harmonic-lattice separation and high-mode viscous stabilization.
- Stable inverse for the first unwanted sum sideband.
- Compact-support compatibility obstruction for generic unstable correction modes.
- Abstract two-collar rank theorem for one complex compatibility moment plus prescribed child output.

## Not proved

- Full Controlled-Overlap Local Difference-Relay Lemma for actual localized curl-generated packets.
- Source-level proof that action exponents are unchanged by every cutoff/curl/transport/Leray correction.
- Exact zero-force solution of all subcritical residual modes.
- A family of v0.7-type tuned resonances available for arbitrarily large admissible `u_*`.
- Physical-scale inheritance from `q_j` to a later smaller `q_{j+1}`.
- A finite or infinite autonomous Navier–Stokes relay chain.
- Exact global closure `R(u,p)==0`.
- Finite-time blowup for unforced 3D Navier–Stokes.

## Publication threshold

**Not reached, but the local model is now materially stronger.**

The v0.7 global principal action filter closes the off-window lattice problem at model level. The next decisive test is whether its rational half-step geometry can be embedded into the source admissible large-`u_*` regime and then survive the localized packet calculus. Success on those two points would make a technical preprint on the autonomous local relay mechanism plausible even before physical-scale inheritance is complete.
