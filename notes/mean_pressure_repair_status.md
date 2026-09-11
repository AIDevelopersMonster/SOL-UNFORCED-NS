# Mean pressure repair status

**Branch:** `research/mean-pressure-repair-v0.1`  
**Base:** `research/local-beta-relay-v0.2` at `6fc5e352dcb52fcc34ae836c971057092e644d8d`  
**Date:** 2026-09-11

## Result of the present attack

The quantitative nonzero sensitivity lemma is already present in the base branch:

\[
\|z(m)-z(\tilde m)\|_X\le C_{M,I}\|m-\tilde m\|_Y,
\]

and the small factor is correctly located on the covariance return leg:

\[
\|\delta\mathcal W_{\rm mean}\|_Y
\le C_MS_*^C\bigl(\varepsilon^{1/2-\kappa_s}+\rho_\ell\bigr)
\|m-\tilde m\|_Y.
\]

Thus the previously advertised first obligation `m -> z(m)` is substantially closed at the abstract/exponent level.

The attack on the next linear obligation found a new obstruction.

## New obstruction

`proofs/one_sided_pressure_cauchy_instability.md` proves that the proposed one-sided radial pressure propagation is not a bounded smooth/Gevrey propagator after pressure is coupled back to incompressibility and axial momentum.

Already in the auxiliary-Haar, zero-base linear subsystem,

\[
\partial_R p=D_z u,
\qquad
(\partial_R+R^{-1})u+D_zp=0,
\]

an axial Fourier mode with `a=epsilon |xi|` satisfies

\[
u''+R^{-1}u'-(a^2+R^{-2})u=0.
\]

The growing modified-Bessel branch gives

\[
|u(R_1)|\gtrsim
\exp\bigl(c\varepsilon|\xi|(R_1-R_0)\bigr)|u(R_0)|.
\]

Therefore the radial Cauchy map is not bounded in finite Sobolev spaces and not bounded even across fixed Gevrey-`s>1` radius gaps. This obstruction occurs at auxiliary torus mode zero, so it is independent of the earlier Diophantine radial compactification issue.

## Correction to the previous route

The scalar one-sided inverses in `radial_characteristic_forward_inverse.md` remain valid, and the algebraic identities in `one_sided_radial_mean_reorganization.md` remain valid. What fails is the inference that the coupled pressure/divergence system can be solved by propagating radial entrance data.

The estimate in `full_linear_mean_propagator_reduction.md`

\[
\|\mathcal M_\ell-I\|\lesssim\varepsilon^{\delta_M}
\]

cannot be interpreted as a same-space operator norm on arbitrary axial frequencies merely because each `D_z=epsilon partial_Z` receives a positive source exponent in finite-stage bookkeeping. At frequency `xi`, the apparent perturbation contains `epsilon^2 xi^2`, which is unbounded as `|xi| -> infinity`.

## Preferred repair

`proofs/elliptic_leray_mean_forward_reduction.md` replaces the failed radial Cauchy route by a time-forward, space-elliptic formulation:

\[
t_*m=\mathcal L_{\rm mean}m+F_{\rm nl}(m,z(m))+F_{\rm in},
\qquad \operatorname{div}_*m=0,
\]

with pressure eliminated by the spatial Leray projector. The principal high-frequency spatial symbol is dissipative,

\[
-\varepsilon |\zeta|_*^2,
\]

and the already-proved swirl cancellation makes the non-small base-swirl coupling zeroth order.

For frozen coefficients this gives the frequency-uniform energy estimate

\[
\frac12\frac d{ds}|\widehat m|^2
\le -c\varepsilon|\zeta|^2|\widehat m|^2+C_M|\widehat m|^2.
\]

The correct remaining local linear theorem is therefore a bounded Leray--Oseen/Stokes propagator on the exact cylindrical/common-torus collar.

## Remaining obligations

1. Prove boundedness of the exact cylindrical/common-torus Leray projector in the chosen characteristic Gevrey realization and specify boundary conditions.
2. Prove the variable-coefficient Leray--Oseen/Stokes propagator estimate uniformly in the dyadic level.
3. Pin the signed-stress Lipschitz exponent exactly instead of using the provisional `0.17` shorthand.
4. Reinsert the already-audited nonlinear factors and close the final time-forward mean contraction.

## Publication status

**No exact local zero-force theorem yet.**

The project nevertheless advanced: the `m -> z(m)` sensitivity is no longer the main unknown, the one-sided radial pressure route has been decisively falsified in the relevant function spaces, and the correct frontier is now a conventional-looking but source-specific space-elliptic/time-parabolic mean propagator problem rather than a radial Cauchy problem.
