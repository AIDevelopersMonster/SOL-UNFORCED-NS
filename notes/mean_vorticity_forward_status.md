# Mean vorticity / Hodge forward status

**Branch:** `research/mean-vorticity-forward-v0.1`  
**Base:** `research/mean-pressure-repair-v0.1`  
**Date:** 2026-09-11

## Closed in this branch

Two local linear obligations are now closed for a fixed annular spatial boundary realization.

First, `proofs/cylindrical_common_torus_hodge_projector.md` proves that the common-torus radial phase derivative

\[
D_r=\partial_R+a_\ell(R)v_r\cdot\partial_y
\]

is exactly conjugate to `partial_R` by an `R`-dependent torus translation. Consequently the cylindrical Hodge/Leray projector on an impermeable annulus is bounded uniformly in the dyadic level, the auxiliary torus frequency, and the radial phase parameter.

Second, `proofs/fixed_annulus_leray_oseen_propagator.md` proves the forward estimate for the projected mean equation at one fixed sufficiently high Sobolev order:

\[
\|\mathcal V_{\rm mean}(s,s_0)f\|_{H^{m_0}}
\le K_{M,I,m_0}\|f\|_{H^{m_0}},
\]

with `K_{M,I,m_0}` independent of the dyadic level and all spatial/auxiliary frequencies.

The proof uses:

- exact radial-phase straightening;
- orthogonality of the Hodge projector;
- viscous dissipation;
- divergence-free skew structure of base transport;
- exact principal swirl derivative cancellation;
- fixed-order Sobolev algebra estimates rather than an unnecessary infinite Gevrey hierarchy.

## Important correction of function-space strategy

The compact radial Gevrey iteration was needed only because the original source demanded two-sided compact radial correction. Once that mechanism is abandoned, the local exact mean fixed point may be formulated at one fixed high Sobolev order. This avoids the same-radius Gevrey obstruction and avoids paying infinitely many derivative-radius losses.

At this fixed order, the already-audited nonlinear return factors remain

\[
\eta_{\rm nl,\ell}
\lesssim C_MS_*^C
\left[
\varepsilon^{0.17}
+\varepsilon^{1/2-\kappa_s}
+\varepsilon^{1-2\kappa_s}
+\rho_\ell
\right]
\to0.
\]

Thus no bounded-domain linear obstruction remains.

## New obstruction/frontier

The bounded-annulus Hodge solve is not automatically the whole-space Navier--Stokes pressure solve.

The actual whole-space Leray projector is nonlocal. Even compactly supported local forcing generates a pressure gradient with spatial tails. Therefore a solution of the artificial annular Hodge problem cannot simply be extended to all of space and declared an exact whole-space relay.

The new sharp problem is the **boundary replacement theorem**:

\[
\boxed{
\text{bounded-annulus Hodge solve}
\longrightarrow
\text{whole-space pressure solve}
}
\]

without losing the small outgoing error class or the relay action filter.

Inside a smaller core collar one may write schematically

\[
\mathbb P_{\mathbb R^3}F
=\mathbb P_\Omega F+\nabla h_F,
\]

where the difference potential `h_F` is harmonic in the core. The next attack should estimate this harmonic boundary corrector from the buffer separation and determine whether it inherits `rho_ell` or another positive epsilon gain.

## Remaining publication obligations

1. Prove the harmonic boundary-corrector / whole-space Leray replacement estimate in the actual relay geometry.
2. Upgrade the signed-stress source size gain to an explicit Lipschitz difference estimate at the fixed Sobolev order and pin the exact exponent replacing the conservative decimal `0.17`.
3. Combine the whole-space pressure replacement with the exact nonzero forward map and close the final local Duhamel contraction.
4. Only after (1)--(3), audit physical-scale inheritance of the resulting nonlocal pressure/error tail.

## Publication status

**Not yet ready for a claim of exact local whole-space zero-force closure.**

However the mathematical narrative is now substantially stronger: two false/unsafe pressure routes have been isolated, the correct fixed-annulus Hodge/Stokes propagator is under control, and the remaining local obstruction has been reduced to a concrete nonlocal harmonic-boundary replacement problem.
