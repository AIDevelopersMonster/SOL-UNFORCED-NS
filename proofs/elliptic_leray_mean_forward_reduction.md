# Time-forward, space-elliptic reduction of the angular mean block

**Status:** PARTIAL THEOREM / CORRECTED PREFERRED ROUTE.

The preceding note `one_sided_pressure_cauchy_instability.md` shows that pressure cannot be propagated as one-sided radial Cauchy data in the smooth or compactly supported Gevrey setting: the coupled incompressibility/pressure subsystem has exponential axial-frequency growth. This note replaces that failed route by a time-forward, space-elliptic formulation.

The goal is not yet to prove the final local zero-force theorem. It is to identify the correct linear operator to which the already-audited nonlinear small factors should be attached.

## 1. Spatial divergence-free formulation

Let the angular mean velocity correction be

\[
m=(\beta,v,\gamma)
\]

on one fixed bounded spatial collar `Omega` in `(R,Z,y)`, with the angular mean condition in the physical azimuthal variable already imposed. Let

\[
\operatorname{div}_* m
=(D_r+R^{-1})\beta+D_z\gamma.
\]

Work in the closed divergence-free subspace

\[
\boxed{
\mathcal H_\sigma
:=\{m:\operatorname{div}_*m=0\}
}
\tag{EL1}
\]

of the chosen characteristic analytic/Gevrey packet space, with spatial boundary conditions fixed so that the Helmholtz-Leray projection is bounded. The exact choice of boundary realization must be frozen once for the local theorem; the present note uses only its standard consequences.

Let

\[
\boxed{\mathbb P_*}
\]

denote the corresponding spatial Leray projector. Then

\[
\mathbb P_*\nabla_*p=0
\]

and the pressure may be reconstructed elliptically after the velocity is solved.

## 2. Forward mean equation after projection

Linearize the exact angular-mean Navier-Stokes equation at the frozen slow base `U_0=(b,V,G)` and the fixed designated wave background. Absorb all terms linear in the mean correction into

\[
\boxed{
\mathcal L_{\rm mean}m
:=
\mathbb P_*\Bigl[
\varepsilon\Delta_*m
-(U_0\cdot\nabla_*)m
-(m\cdot\nabla_*)U_0
+\mathcal C_{\rm cyl}m
\Bigr],
}
\tag{EL2}
\]

where `C_cyl` denotes the fixed cylindrical zeroth-order terms. The exact cancellation in `principal_swirl_mean_cancellation.md` shows that the visibly non-small swirl contribution is zeroth order after the divergence-free constraint is imposed.

Thus the mean correction satisfies

\[
\boxed{
 t_*m=\mathcal L_{\rm mean}m+F_{\rm nl}(m,z(m))+F_{\rm in},
\qquad m\in\mathcal H_\sigma.
}
\tag{EL3}
\]

Here:

- `F_in` contains the known supported mean defect and entrance data;
- `F_nl` contains quadratic mean terms, covariance feedback, signed-stress reconstruction errors, and the already-audited supported remainders;
- pressure is absent from the evolution equation.

## 3. Why the high axial-frequency Cauchy instability disappears

In the failed radial route, spatial pressure was determined from one radial face and then propagated through the axial momentum equation. That converted the elliptic divergence constraint into the modified-Bessel Cauchy system of `one_sided_pressure_cauchy_instability.md` and created growth

\[
\exp(c\varepsilon|\xi|\Delta R).
\]

In (EL3), no spatial coordinate is used as an evolution variable. The only evolution direction is the physical-time characteristic `t_*`. Spatial high frequencies remain inside the projected Stokes/Oseen operator.

The viscous principal symbol on the divergence-free subspace is

\[
\boxed{
-\varepsilon |\zeta|_*^2 I
}
\tag{EL4}
\]

modulo bounded first- and zeroth-order frozen coefficients. Hence high spatial frequencies are damped rather than exponentially amplified by a spatial Cauchy propagator.

This is the structural reason the Leray route is the correct repair.

## 4. Frozen-coefficient energy estimate

First freeze the smooth coefficients of `U_0` on one chart. For a Fourier mode `\zeta` in the straightened spatial variables, the projected linear system has the form

\[
\frac{d}{ds}\widehat m
=
\Bigl[-\varepsilon Q(\zeta)+iA(\zeta)+B\Bigr]\widehat m,
\tag{EL5}
\]

where:

- `Q(\zeta)>=c|\zeta|^2` on the divergence-free subspace;
- `A(\zeta)` is the real transport symbol and contributes no positive symmetric part;
- `B` is a bounded matrix depending only on the frozen relay design and collar.

Taking the Hermitian inner product gives

\[
\frac12\frac d{ds}|\widehat m|^2
\le
- c\varepsilon|\zeta|^2|\widehat m|^2
+C_M|\widehat m|^2.
\tag{EL6}
\]

Therefore

\[
\boxed{
|\widehat m(s)|
\le e^{C_M(s-s_0)}|\widehat m(s_0)|.
}
\tag{EL7}
\]

The crucial point is that the constant is independent of the spatial frequency and of the dyadic level once the relay design and normalized collar are frozen.

## 5. Variable coefficients and Gevrey commutators

Return to the fixed smooth coefficient family. Because all source cutoffs and frozen base profiles lie in one common compactly supported Gevrey-`s>1` class, multiplication by these coefficients and commutators with the characteristic derivatives are bounded after a preassigned finite radius margin.

For one final radius `lambda_* > 0`, standard Gevrey product estimates give

\[
\boxed{
\frac d{ds}\|m(s)\|_{Y_{s,\lambda_*}}
\le
C_{M,I}\|m(s)\|_{Y_{s,\lambda_*}}
+
\|F(s)\|_{Y_{s,\lambda_*}}
}
\tag{EL8}
\]

provided the Leray projector is bounded on the same spatial Gevrey realization.

Gronwall then yields the candidate propagator estimate

\[
\boxed{
\|\mathcal V_{\rm mean}(s,s_0)f\|_{Y_{s,\lambda_*}}
\le
K_{M,I}\|f\|_{Y_{s,\lambda_*}},
}
\tag{EL9}
\]

with `K_{M,I}` independent of dyadic level and spatial frequency.

The remaining analytic obligation in this note is therefore reduced to one standard but source-specific statement:

\[
\boxed{
\mathbb P_*:Y_{s,\lambda_*}\to Y_{s,\lambda_*}
\text{ is bounded uniformly on the frozen collar.}
}
\tag{EL10}
\]

For periodic tangential variables and a fixed smooth annular collar with standard elliptic boundary realization, this is an elliptic regularity statement, not a small-divisor problem.

## 6. Pressure recovery

Once `m` is known, recover the mean pressure from the divergence of the unprojected equation. Schematically,

\[
\boxed{
-\Delta_*p_m
=
\operatorname{div}_*\Bigl[
(U_0\cdot\nabla_*)m
+(m\cdot\nabla_*)U_0
+\mathcal Q(m,z)
\Bigr]
}
\tag{EL11}
\]

with the boundary normalization associated to the chosen Leray realization. Standard elliptic regularity gives

\[
\boxed{
\|\nabla_*p_m\|_{Y_{s,\lambda_*}}
\le C_{M,I}
\Bigl(
\|m\|_{Y_{s,\lambda_*}}+
\|\mathcal Q(m,z)\|_{Y_{s,\lambda_*}}
\Bigr).
}
\tag{EL12}
\]

Thus pressure reconstruction costs only a bounded spatial elliptic operator after the velocity evolution is closed.

## 7. Reinserting the nonlinear small factors

The branch already supplies:

\[
\|z(m)-z(\tilde m)\|_X
\le C_{M,I}\|m-\tilde m\|_Y,
\]

while the return covariance gains

\[
\varepsilon^{1/2-\kappa_s}.
\]

The signed-stress, transport/viscosity remainder, and supported residual blocks have positive factors recorded in the mean block audit. Therefore, once (EL9)-(EL10) are established in the exact source realization, the Duhamel map obeys

\[
\boxed{
\|\mathcal T_\ell(m)-\mathcal T_\ell(\tilde m)\|_Y
\le
K_{M,I}\eta_{\rm nl,\ell}
\|m-\tilde m\|_Y,
}
\tag{EL13}
\]

with

\[
\boxed{
\eta_{\rm nl,\ell}
\lesssim
C_MS_*^C\left[
\varepsilon^{0.17}
+\varepsilon^{1/2-\kappa_s}
+\varepsilon^{1-2\kappa_s}
+\rho_\ell
\right]
\to0.
}
\tag{EL14}
\]

Thus the numerical smallness required for contraction survives the elliptic repair.

## 8. What is proved and what remains

Proved structurally here:

1. the correct mean evolution is time-forward and spatially elliptic;
2. the radial Cauchy instability is absent after Leray projection because spatial high frequencies stay in the Stokes/Oseen operator;
3. the principal frozen-coefficient energy estimate is frequency-uniform;
4. pressure recovery is an elliptic post-processing step;
5. the existing nonlinear small factors are compatible with this architecture.

Still to prove in publication form:

1. boundedness of the exact cylindrical/common-torus Leray projector in the chosen characteristic Gevrey space on the actual local collar;
2. variable-coefficient commutator estimates with all source chart factors and boundary conditions written explicitly;
3. the resulting exact propagator estimate (EL9) for the source operator, including viscosity and frozen swirl;
4. the signed-stress difference estimate with its exact exponent rather than the provisional `0.17` shorthand.

## 9. New immediate frontier

The next local theorem target is now

\[
\boxed{
\textbf{uniform Leray--Oseen/Stokes mean propagator in the exact source Gevrey collar.}
}
\]

If that theorem closes, the branch already contains the small nonlinear factor needed for Banach contraction. No radial Cauchy propagation and no compact radial Neumann series should re-enter the local proof.
