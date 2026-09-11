# Global fixed-order Leray--Oseen propagator for the angular mean

**Status:** PROVED FOR THE RECONSTRUCTED SLOW-BASE LINEARIZATION AT FIXED SOBOLEV ORDER; NO ARTIFICIAL SPATIAL BOUNDARY.

This note combines `whole_space_leray_fixed_order_bound.md`, the principal swirl cancellation, and the source slow-base coefficient bounds to close the remaining global linear mean estimate. The evolution is forward only in normalized physical time. Pressure is eliminated by the exact whole-space Leray projector.

The theorem is deliberately restricted to the angular-mean linearization. The designated nonzero packet response is not inserted into the Oseen coefficients; its dependence on the mean is already handled by `nonzero_mean_sensitivity.md` and returns through the source-small covariance block.

## 1. Equation and coefficient split

Let `m` be the reconstructed physical angular-mean correction, divergence free in `R^3`. Write the slow reconstructed base as

\[
U_0=U_{\rm fix}+U_{\rm sm,\ell}.
\tag{GO1}
\]

On the reserved mean patch:

- the non-small swirl profile is fixed once the relay design is frozen;
- its derivative-bearing action on the mean reduces to zeroth order by `principal_swirl_mean_cancellation.md`;
- the radial/axial slow-base pieces and all chart/cutoff perturbations satisfy, at every fixed derivative order used here,

\[
\boxed{
\|U_{\rm sm,\ell}\|_{W^{m_0+1,\infty}}
\le C_{M,m_0}S_*^C\varepsilon^{\delta_0}
=o(1)
}
\tag{GO2}
\]

for some source-positive `delta_0>0` after the finite source bookkeeping is frozen.

The fixed part satisfies

\[
\boxed{
\|U_{\rm fix}\|_{W^{m_0+1,\infty}}
\le C_{M,m_0}.
}
\tag{GO3}
\]

Choose one integer `m_0>=6`.

The global projected linear equation is

\[
\boxed{
\partial_s m
=\mathbb P_{\rm ws}
\left[
\varepsilon\Delta m
-(U_0\cdot\nabla)m
-(m\cdot\nabla)U_0
+\mathcal C_0m
\right]
+F,
\qquad \nabla\cdot m=0.
}
\tag{GO4}
\]

Here `C_0` collects the already reduced cylindrical/coordinate zeroth-order terms. In a physical Cartesian reconstruction these are smooth bounded coefficient matrices supported on the relay region, because the active annulus stays a fixed positive distance from the symmetry axis.

## 2. L2 estimate

Since the whole-space Leray projector is orthogonal in `L^2` and `m` is divergence free,

\[
\langle\mathbb P_{\rm ws}G,m\rangle=\langle G,m\rangle.
\tag{GO5}
\]

Also

\[
\langle\Delta m,m\rangle=-\|\nabla m\|_2^2.
\tag{GO6}
\]

The slow base is divergence free after physical reconstruction, so

\[
\langle(U_0\cdot\nabla)m,m\rangle=0
\tag{GO7}
\]

without any artificial boundary flux. The stretching and zeroth-order terms satisfy

\[
\left|
\langle(m\cdot\nabla)U_0,m\rangle
\right|
+
|\langle\mathcal C_0m,m\rangle|
\le C_{M}\|m\|_2^2.
\tag{GO8}
\]

Hence

\[
\boxed{
\frac12\frac d{ds}\|m\|_2^2
+\varepsilon\|\nabla m\|_2^2
\le C_M\|m\|_2^2+\|F\|_2\|m\|_2.
}
\tag{GO9}
\]

## 3. Fixed derivative order

Because `P_ws` commutes with Cartesian derivatives, apply `partial^alpha`, `|alpha|<=m_0`, to (GO4). The principal transport term decomposes as

\[
\partial^\alpha[(U_0\cdot\nabla)m]
=(U_0\cdot\nabla)\partial^\alpha m
+[\partial^\alpha,U_0\cdot\nabla]m.
\tag{GO10}
\]

The first term is skew in `L^2`. By the standard Moser commutator estimate,

\[
\boxed{
\|[\partial^\alpha,U_0\cdot\nabla]m\|_2
\le C_{m_0}
\|U_0\|_{W^{m_0+1,\infty}}
\|m\|_{H^{m_0}}.
}
\tag{GO11}
\]

Similarly,

\[
\|(m\cdot\nabla)U_0\|_{H^{m_0}}
\le C_{m_0}
\|U_0\|_{W^{m_0+1,\infty}}
\|m\|_{H^{m_0}}.
\tag{GO12}
\]

Using (GO2)-(GO3), all non-small coefficients contribute only a fixed `C_{M,m_0}` and all source-varying pieces contribute `o(1)`. Therefore, for sufficiently large dyadic level,

\[
\boxed{
\frac d{ds}\|m\|_{H^{m_0}}^2
+c\varepsilon\|m\|_{H^{m_0+1}}^2
\le
C_{M,m_0}\|m\|_{H^{m_0}}^2
+C\|F\|_{H^{m_0}}^2.
}
\tag{GO13}
\]

No term depending positively on spatial frequency, auxiliary harmonic index, or radial phase parameter appears.

## 4. Uniform global propagator

On the fixed normalized temporal relay interval `I=[s_-,s_+]`, Gronwall yields

\[
\boxed{
\|\mathcal V_{\rm ws}(s,s_0)f\|_{H^{m_0}}
\le
K_{M,I,m_0}\|f\|_{H^{m_0}},
\qquad s_0\le s\in I,
}
\tag{GO14}
\]

where

\[
\boxed{K_{M,I,m_0}<\infty}
\]

is independent of the dyadic level.

The Duhamel estimate is

\[
\boxed{
\left\|
\int_{s_0}^s\mathcal V_{\rm ws}(s,\tau)F(\tau)d\tau
\right\|_{H^{m_0}}
\le
K_{M,I,m_0}|I|
\|F\|_{L^\infty(I;H^{m_0})}.
}
\tag{GO15}
\]

## 5. Why the previous boundary problem disappears

No annular wall is introduced in (GO4). Consequently there is no harmonic boundary-replacement field and no radial pressure Cauchy propagation.

The nonlocal pressure is already exactly included through `P_ws`. The pressure tail may extend outside the relay core, but its global Sobolev norm is controlled by the source through the order-zero projector estimate.

Thus the local mean contraction may be performed directly in a global fixed-order Sobolev space. Spatial localization of the *velocity correction* is no longer required at this step.

## 6. Composition with the nonlinear source

Let

\[
\mathcal F_{\rm nl,\ell}(m)
:=
\mathbb P_{\rm ws}
F_{\rm nl}(m,z(m)).
\tag{GO16}
\]

The current branch gives the aggregate difference estimate

\[
\boxed{
\|\mathcal F_{\rm nl,\ell}(m)-\mathcal F_{\rm nl,\ell}(\widetilde m)\|_{H^{m_0}}
\le
\eta_{\rm nl,\ell}
\|m-\widetilde m\|_{H^{m_0}},
}
\tag{GO17}
\]

with

\[
\boxed{
\eta_{\rm nl,\ell}
\le C_MS_*^C
\left[
\varepsilon^{9/50-2\kappa_s}
+\varepsilon^{1/2-\kappa_s}
+\varepsilon^{1-2\kappa_s}
+\rho_\ell
\right]
\to0.
}
\tag{GO18}
\]

Combining (GO15) and (GO17), the nonlinear Duhamel map has Lipschitz constant

\[
\boxed{
q_\ell
\le
K_{M,I,m_0}|I|\eta_{\rm nl,\ell}
\to0.
}
\tag{GO19}
\]

Therefore for sufficiently large `ell`,

\[
\boxed{q_\ell<1/2.}
\tag{GO20}
\]

## 7. Remaining fixed-point obligation

The contraction constant is now closed. The only remaining local mean step is the ball invariance estimate for the inhomogeneous defect:

\[
\boxed{
\|\mathcal T_\ell(0)\|_{H^{m_0}}
\le r_\ell/2,
\qquad
r_\ell\to0.
}
\tag{GO21}
\]

The branch already records the nonzero supported defect scale

\[
\rho_\ell
\lesssim
S_*^C\varepsilon^{1/5}+S_*^Ce^{-c_MS_*}.
\]

What remains is to collect every *mean* inhomogeneous source term after global projection into one explicit bound of the same type.

Once (GO21) is proved, Banach gives a unique exact global angular mean on the local temporal relay interval.

## 8. Conclusion

The linear whole-space mean propagator obstruction is closed:

\[
\boxed{
\|\mathcal V_{\rm ws}(s,s_0)\|_{H^{m_0}\to H^{m_0}}
\le K_{M,I,m_0}
}
\]

dyadically uniformly.

The next attack is no longer pressure or derivative loss. It is purely quantitative bookkeeping of the mean inhomogeneous defect needed for the self-map estimate.