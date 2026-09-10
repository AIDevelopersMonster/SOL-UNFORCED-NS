# STATUS

**Project:** SOL-UNFORCED-NS  
**Working version:** v0.8 forward relay architecture  
**Date:** 2026-09-10  
**Branch:** `research/local-beta-relay-v0.2`

## Corrected carrier law

The earlier apparent dyadic-chart frequency jump was retracted. The corrected intrinsic leading carrier scale is

\[
\boxed{\Omega_{\rm phys}(q)\asymp q^{-(1+h)/2}.}
\]

See `proofs/chart_invariant_carrier_scale.md`.

## v0.8 architecture

Freeze one sufficiently large integer `M` and set

\[
\beta_1=2,\qquad \beta_2=1,\qquad u_*=M^2,
\]

with the half-step relay family from `proofs/integral_beta_v08_large_u_halfstep_family.md`. Exact finite-`u_*` resonances exist along `u_*=M^2->infinity`; the desired difference harmonic is unit-beta; every non-designated principal-growing lattice mode is action-subcritical; and `T=0` modes are purely viscous.

The principal action deficit is

\[
\boxed{
S_M(a,b)-\mathcal E_{|T|,M^2}(\xi_M(a,b))\le-\delta_*
}
\]

for some fixed `delta_*>0` after `M` is frozen.

## Source-localized action preservation — CLOSED at finite stage

`proofs/source_localized_action_preservation.md` proves that the v0.8 action gap survives every fixed finite composition of the localized source operations audited from the OpenAI construction. No audited operation creates `exp(+cS_*)`; non-designated action-subcritical descendants retain

\[
\boxed{e^{-c_MS_*}.}
\]

## Stage-uniform infinite lattice — stable complement CLOSED

`proofs/finite_critical_block_uniform_stable_inverse.md` proves that for one frozen design the infinite stable complement has a uniform negative gap and quadratic high-mode smoothing:

\[
\boxed{
\|G_\nu f_\nu\|_{\rm pkt}
\le
\frac{C_M}{1+|\nu|^2}
\|f_\nu\|_{\rm pkt}.
}
\]

`proofs/analytic_quadratic_symbol_bound.md` proves that this smoothing controls the one-output-carrier loss of the localized Navier-Stokes bilinear symbol in the analytic lattice norm. Hence the infinite stable complement is contractive at the action-subcritical scale.

## Critical block count — new result

`proofs/v08_critical_block_cardinality.md` quantifies the finite critical set for the large-`u_*` family. Although finite for every frozen `M`, its scalar cardinality satisfies

\[
\boxed{|\mathcal C_M|=\Theta(M^5).}
\]

Representative center counts are already large at modest values:

\[
|\mathcal C_5|\approx7.9\times10^3,
\qquad
|\mathcal C_{10}|\approx2.66\times10^5,
\qquad
|\mathcal C_{20}|\approx8.88\times10^6.
\]

Therefore the previously proposed literal strategy of imposing a separate two-sided compact-support compatibility condition on every critical scalar mode is mathematically finite but architecturally poor. The abstract multicollar theorem remains correct, but it is no longer the preferred local closure mechanism.

## Preferred local closure — FORWARD INPUT-OUTPUT MAP

`proofs/forward_relay_input_output_closure.md` reformulates the relay as an exact forward initial-value problem on a bounded characteristic collar.

Instead of imposing

\[
Z(v_-)=Z(v_+)=0,
\]

we prescribe only the incoming correction

\[
Z(v_-)=Z_{\rm in}
\]

and solve the exact localized correction equation forward.

On the finite critical block, smoothness over the fixed bounded collar gives a finite propagator constant. On the infinite stable complement, the stronger uniform inverse and high-mode smoothing are available. Combining both yields a full forward Duhamel map on the analytic packet lattice space.

For incoming error

\[
\|Z_{\rm in}\|\lesssim\rho_\ell,
\qquad
\rho_\ell=C_MS_*^{C_M}e^{-c_MS_*},
\]

the Duhamel map is contractive for sufficiently large dyadic level. Therefore there is a unique exact local correction satisfying

\[
\boxed{R(U_{\rm des}+Z)=0}
\]

throughout the relay collar, with **zero external force**.

The outgoing correction is not forced to vanish. It exits as part of the state:

\[
\boxed{Z_{\rm out}=Z(v_+)},
\]

and remains action-subcritical:

\[
\boxed{
\|Z_{\rm out}\|
\le C_MS_*^{C_M}e^{-c_MS_*}.
}
\]

This changes the architecture fundamentally. A relay is treated as an input-output dynamical module rather than an isolated compactly supported bubble that erases its entire correction state at every stage.

## Current local conclusion

At the theorem-architecture level, the local module now has:

1. exact finite-`u_*` half-step resonance at arbitrarily large admissible `u_*`;
2. robust designated growing-child projection;
3. complete principal lattice action filter;
4. finite-stage source-localized preservation of that filter;
5. stage-uniform analytic control of the infinite stable lattice complement;
6. a forward Banach contraction giving exact zero residual inside the bounded relay collar while carrying a flat outgoing error state.

The earlier full critical-kernel determinant is no longer required for the preferred local formulation. It remains relevant only if one insists on exact two-sided temporal compact support of every local correction.

## Remaining source-specific local bookkeeping

Before packaging a publication-final **Controlled-Overlap Local Difference-Relay Theorem**, one consolidated source-class statement should still be written showing explicitly that the designated child extraction and the decomposition

\[
U=U_{\rm des}+Z
\]

are compatible with the exact divergence-free curl/Leray formulation on the same translated collar. This appears to be bookkeeping rather than a new spectral obstruction, but it must be written rather than assumed.

## New decisive frontier — physical-scale inheritance

The major mathematical problem is now global rather than local:

\[
\boxed{
(A_{c,\rm out},Z_{\rm out})\text{ at scale }q_j
\longrightarrow
\text{valid input state at a smaller physical scale }q_{j+1}<q_j.
}
\]

Need to prove simultaneously that:

- the designated child becomes a valid parent/catalyst component for the next relay after actual physical transport to smaller `q`;
- its intrinsic carrier follows the corrected physical law `Omega_phys(q)~q^{-(1+h)/2}`;
- the flat outgoing correction remains in the admissible incoming error class;
- repeated relay maps do not accumulate the flat errors to primary size.

This **Physical-Scale Inheritance Law** is now the decisive frontier for constructing an autonomous chain.

## Not proved

- Publication-final consolidated source-class statement for the exact local input-output relay.
- Physical-scale inheritance from a generated child at `q_j` to a valid parent/catalyst state at some `q_{j+1}<q_j`.
- Iterability of the relay map through infinitely many physical scales.
- A finite or infinite autonomous Navier-Stokes relay chain producing singularity.
- Exact global closure `R(u,p)==0` on the complete space-time construction.
- Finite-time blowup for unforced 3D Navier-Stokes.

## Publication threshold

**Local technical-preprint threshold is now essentially reached, subject to one consolidated source-class bookkeeping theorem.**

The local zero-force relay no longer depends on an enormous critical-kernel determinant once formulated as a forward input-output map. After the source-class compatibility statement is written and audited, the local relay architecture is sufficiently self-contained for a technical preprint. This would still be a local construction theorem, not a solution of the unforced Navier-Stokes blowup problem.
