# STATUS

**Project:** SOL-UNFORCED-NS  
**Working version:** v0.8 preferred model candidate  
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

`proofs/source_localized_action_preservation.md` proves that the v0.8 action gap survives every fixed finite composition of the localized source operations audited from the OpenAI construction:

- designated products in the overlap supernode;
- common-torus pullback;
- normalized coefficient derivatives;
- curl generation and curl remainders;
- pulse inversion;
- supported linear residual operators;
- wave-wave transport with incompressibility gain;
- relay-compatible shifted cutoffs;
- every fixed finite physical derivative order.

No audited operation creates `exp(+c S_*)`; non-designated action-subcritical descendants retain

\[
\boxed{e^{-c_M S_*}.}
\]

## Stage-uniform infinite lattice — stable complement CLOSED

`proofs/finite_critical_block_uniform_stable_inverse.md` proves that for one frozen v0.8 design and one fixed correction interval there is a **finite** critical set

\[
\mathcal C_M\subset\mathbb Z^2
\]

containing every lattice mode that can be neutral or growing anywhere in the interval.

The infinite complement

\[
\mathcal S_M=(\mathbb Z^2\setminus\{0\})\setminus\mathcal C_M
\]

has a uniform negative gap

\[
\Gamma_\nu\le-\gamma_M<0
\]

and, for high indices, quadratic viscous damping. Hence the exact localized stable-complement inverse satisfies a stage-uniform modewise estimate

\[
\boxed{
\|G_\nu f_\nu\|_{\rm pkt}
\le
\frac{C_M}{1+|\nu|^2}
\|f_\nu\|_{\rm pkt}.
}
\]

This reduces all possible compact-support/Fredholm obstructions to a **finite-dimensional critical block**.

## Infinite quadratic convolution — CLOSED on the stable complement

`proofs/analytic_quadratic_symbol_bound.md` introduces the analytic lattice norm

\[
\|z\|_{\mathfrak A_\sigma}
=
\sum_{\nu\in\mathbb Z^2}
 e^{\sigma|\nu|}(1+|\nu|)
\|z_\nu\|_{\rm pkt}.
\]

Using the one-output-carrier structure left after exact incompressibility and the two-power high-mode smoothing of the stable inverse, the nonlinear stable-complement map obeys

\[
\boxed{
\|\mathcal G_S\mathcal B(z,w)\|_{\mathfrak A_\sigma}
\le
C_M
\|z\|_{\mathfrak A_\sigma}
\|w\|_{\mathfrak A_\sigma}.
}
\]

The associated Lipschitz estimate gives a contraction on a ball of radius

\[
\rho_\ell\asymp S_*^C e^{-c_M S_*}
\]

once the finite critical component has been chosen at the same action-subcritical size.

Thus the **infinite-dimensional stable complement is no longer the local obstruction**.

## Finite critical block — abstract control reduction CLOSED

`proofs/multicollar_finite_critical_transversality.md` proves the general finite control theorem.

If the `N` critical compact-support moment kernels

\[
K_1,\dots,K_N
\]

are linearly independent on the relay interval, then one can choose `N` distinct narrow collar centers so that the sampling matrix

\[
[K_i(\tau_j)]
\]

has nonzero determinant. If one also prescribes the desired complex child output, `N+1` complex collars suffice provided the augmented family

\[
K_0,K_1,\dots,K_N
\]

is linearly independent.

The rank persists for smooth narrow collars and under the `o(1)` localized packet perturbations. The implicit-function theorem then slaves the finite critical controls to the small stable correction.

This generalizes the previously proved one-moment two-collar theorem.

## Immediate frontier

The local zero-force problem has now been reduced to one concrete **source-specific finite-dimensional condition**:

\[
\boxed{
K_0,K_1,\dots,K_N
\text{ for the actual v0.8 finite critical set are linearly independent.}
}
\]

Everything else in the local architecture now has a theorem-level route:

1. complete principal lattice action filter — proved;
2. arbitrarily large admissible `u_*` — proved;
3. finite-stage localized action preservation — proved;
4. stage-uniform stable-complement inverse — proved;
5. analytic quadratic contraction on the infinite stable complement — proved;
6. abstract finite multi-collar control theorem — proved.

The next decisive task is therefore to **enumerate the actual finite critical set `C_M`, derive its moment kernels, and prove the augmented kernel family is linearly independent**. If that succeeds, the local Lyapunov-Schmidt system closes and one can assemble the full Controlled-Overlap Local Difference-Relay Theorem with zero external force.

## Not proved

- Linear independence/transversality of the actual full v0.8 finite critical kernel family.
- Exact local zero-force closure of the complete corrected packet system.
- Full Controlled-Overlap Local Difference-Relay Theorem.
- Physical-scale inheritance from a generated child at `q_j` to a valid parent at a later smaller `q_{j+1}`.
- A finite or infinite autonomous Navier-Stokes relay chain.
- Exact global closure `R(u,p)==0`.
- Finite-time blowup for unforced 3D Navier-Stokes.

## Publication threshold

**Not crossed yet, but now concentrated in one finite-dimensional local question.**

If the actual finite critical kernel family is proved independent and the local Lyapunov-Schmidt system closes, the local autonomous relay module crosses the publication threshold immediately, even before physical-scale inheritance is solved.
