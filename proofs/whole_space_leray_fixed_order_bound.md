# Whole-space Leray projector at fixed Sobolev order

**Status:** PROVED FUNCTIONAL-ANALYTIC BLOCK FOR THE GLOBAL MEAN FORMULATION.

This note implements the corrected frontier from `harmonic_boundary_replacement_obstruction.md`: rather than compare an artificial annular Hodge projector with the global pressure by a perturbative harmonic corrector, incorporate the whole-space Leray projector directly into the mean evolution.

The key point is standard but decisive for the relay architecture. At one fixed Sobolev order, the whole-space Leray projector is an order-zero Fourier multiplier. Therefore it preserves every epsilon/smallness factor carried by its input and introduces no new dyadic, spatial-frequency, or derivative loss.

## 1. Global physical-space projector

On `R^3`, define

\[
\boxed{
\mathbb P_{\rm ws}
:=I-\nabla\Delta^{-1}\operatorname{div}.
}
\tag{WL1}
\]

Its Fourier symbol is

\[
\boxed{
P(\xi)=I-\frac{\xi\otimes\xi}{|\xi|^2},
\qquad \xi\ne0,
}
\tag{WL2}
\]

and set `P(0)=I` on the zero mode for definiteness.

For every `xi`, `P(xi)` is an orthogonal projection onto `xi^perp`, hence

\[
\boxed{\|P(\xi)\|_{\mathbb C^3\to\mathbb C^3}\le1.}
\tag{WL3}
\]

## 2. Exact H^m boundedness

For every real `m`,

\[
\begin{aligned}
\|\mathbb P_{\rm ws}F\|_{H^m}^2
&=\int_{\mathbb R^3}
(1+|\xi|^2)^m
|P(\xi)\widehat F(\xi)|^2\,d\xi\\
&\le
\int_{\mathbb R^3}
(1+|\xi|^2)^m
|\widehat F(\xi)|^2\,d\xi.
\end{aligned}
\]

Therefore

\[
\boxed{
\|\mathbb P_{\rm ws}F\|_{H^m}
\le
\|F\|_{H^m}.
}
\tag{WL4}
\]

The constant is exactly one and is independent of every relay parameter.

The same estimate holds componentwise for finite products with the auxiliary coefficient space used in the common-torus representation, provided the auxiliary variables are merely parameters for the physical-space Fourier transform.

## 3. Commutation with physical derivatives

Because `P(xi)` is a Fourier multiplier,

\[
\boxed{
[\mathbb P_{\rm ws},\partial^\alpha]=0
}
\tag{WL5}
\]

for every physical multi-index `alpha`. Thus no commutator appears when deriving fixed-order Sobolev energy estimates.

If the relay norm uses the exact source differential operators only after pullback to a physical chart, one first estimates in physical derivatives and then transfers through the fixed chart maps. The chart coefficients contribute only the already-recorded finite-order source polynomial factors.

## 4. Pressure recovery

For a forcing `F`, the removed pressure gradient is

\[
\boxed{
\nabla p=(I-\mathbb P_{\rm ws})F
=\nabla\Delta^{-1}\operatorname{div}F.
}
\tag{WL6}
\]

Since `I-P(xi)` is also an orthogonal projection symbol,

\[
\boxed{
\|\nabla p\|_{H^m}
\le
\|F\|_{H^m}.
}
\tag{WL7}
\]

Thus the nonlocal pressure tail may be spatially extended, but its global fixed-order Sobolev size is no larger than the source size.

This is exactly what is needed for the nonlinear contraction: the global pressure does not need an additional epsilon gain if the source entering it already has one.

## 5. Preservation of source-small factors

Suppose a nonlinear block satisfies

\[
\boxed{
\|F_\ell(m)-F_\ell(\widetilde m)\|_{H^{m_0}}
\le
\eta_\ell
\|m-\widetilde m\|_{H^{m_0}},
\qquad
\eta_\ell\to0.
}
\tag{WL8}
\]

Then by (WL4),

\[
\boxed{
\|\mathbb P_{\rm ws}[F_\ell(m)-F_\ell(\widetilde m)]\|_{H^{m_0}}
\le
\eta_\ell
\|m-\widetilde m\|_{H^{m_0}}.
}
\tag{WL9}
\]

Hence the projector preserves without degradation each current source-small factor:

\[
\varepsilon^{9/50-2\kappa_s},
\qquad
\varepsilon^{1/2-\kappa_s},
\qquad
\varepsilon^{1-2\kappa_s},
\qquad
\rho_\ell.
\tag{WL10}
\]

## 6. Global linear mean operator

The correct whole-space mean equation is therefore

\[
\boxed{
\partial_s m
=
\mathbb P_{\rm ws}
\left[
\varepsilon\Delta m
-(U_0\cdot\nabla)m
-(m\cdot\nabla)U_0
+\mathcal C_{\rm cyl}m
\right]
+
\mathbb P_{\rm ws}F_{\rm nl}(m,z(m))
+F_{\rm in}.
}
\tag{WL11}
\]

All `O(1)` pressure effects are contained in the first projected linear operator. All nonlinear pressure effects inherit the already-audited smallness of `F_nl`.

At the `L^2` level, orthogonality of `P_ws` gives

\[
\langle\mathbb P_{\rm ws}G,m\rangle
=
\langle G,m\rangle
\]

for divergence-free `m`, exactly as in the bounded-domain Hodge estimate.

At fixed derivative order, (WL5) eliminates projector commutators altogether.

Therefore the only remaining analytic issue for the global mean propagator is the ordinary variable-coefficient transport/stretching estimate of the physical base field `U_0`; the projector itself contributes no loss.

## 7. Relation to the common-torus gauge

The common-torus variables are a coefficient/packet representation of the physical relay, not extra physical dimensions. The global projector acts in physical space after reconstruction. Consequently the large radial phase parameter `M_r` is not a parameter of the symbol (WL2).

When estimates are transferred back to the packet representation, radial phase straightening from `cylindrical_common_torus_hodge_projector.md` remains useful for bounding the coefficient seminorms, but it is no longer needed to define pressure.

This avoids the conceptual error of applying a four- or five-dimensional Hodge projector to the auxiliary torus variables themselves.

## 8. Consequence

The boundary-replacement problem is removed from the **local contraction theorem**: one should never introduce the artificial radial wall in the first place.

The global Leray operator is bounded with norm one on `H^{m_0}`, so every already-small nonlinear mean block remains small after exact whole-space pressure elimination.

What remains before exact local whole-space mean closure is now:

1. prove the global fixed-order Leray--Oseen propagator estimate for the exact reconstructed base coefficients;
2. combine it with the already-proved nonzero map and nonlinear Lipschitz factors;
3. verify the fixed-point ball maps into itself, including the inhomogeneous defect size.

The nonlocal spatial tail of pressure remains relevant later for **physical-scale inheritance**, but it is no longer a local Banach-contraction obstruction.