# Anisotropic source-scaled whole-space Leray norm for the low-`u` mean problem

**Status:** PROVED FUNCTIONAL-ANALYTIC PROJECTOR THEOREM.  The spatial source normalization is anisotropic, but this produces **no loss at all** for the whole-space Leray projector when the norm is defined after the same linear dilation.  This removes the need to compare variable cylindrical graph derivatives directly with raw Cartesian derivatives.

The theorem is elementary Fourier analysis but decisive for the root-augmented mean architecture.  It also extends exactly to the phase-adapted coefficient norm by defining the coefficient projector through physical reconstruction, as in `phase_adapted_whole_space_leray_intertwining.md`.

No forward Oseen bound or exact reset cell is claimed in this note.

## 1. Spatial source dilation

At one band let

\[
Q>0,
\qquad
D=\frac12-h_{prof},
\]

and define the spatial scaling matrix

\[
\boxed{
A_Q
:=
\operatorname{diag}
\left(
Q^{1/2},
Q^{1/2},
Q^D
\right).
}
\tag{AL1}

The two transverse Cartesian directions use the physical radial/angular scale `sqrt(Q)`; the axial direction uses the exact source scale `Q^D` appearing in `PhysicalResidualBridge.commonGraph_map`.

Fix any spatial center `x_0`.  Define the pullback

\[
\boxed{
(T_Q f)(y):=f(x_0+A_Qy),
\qquad y\in\mathbb R^3.
}
\tag{AL2}

Translation has no effect on Fourier multiplier norms, so `x_0` will be suppressed below.

## 2. Conjugated Leray symbol

The whole-space Leray projector has Fourier symbol

\[
P(\xi)
=I-\frac{\xi\otimes\xi}{|\xi|^2}
\qquad(\xi\ne0),
\]

with `P(0)=I`.

Under the anisotropic dilation, Fourier covectors transform by

\[
\xi=A_Q^{-T}\eta.
\]

Therefore

\[
\boxed{
\mathbb P_Q
:=T_Q\mathbb P_{ws}T_Q^{-1}
}
\tag{AL3}
\]

is the multiplier with symbol

\[
\boxed{
P_Q(\eta)
=I-
\frac{A_Q^{-T}\eta\otimes A_Q^{-T}\eta}
{|A_Q^{-T}\eta|^2}.
}
\tag{AL4}

For every nonzero `eta`, this is the orthogonal projection onto

\[
(A_Q^{-T}\eta)^\perp.
\]

Hence

\[
\boxed{
\|P_Q(\eta)\|_{\mathbb C^3\to\mathbb C^3}
\le1
}
\tag{AL5}
\]

for all `Q`, despite the anisotropy ratio

\[
\frac{Q^D}{Q^{1/2}}=Q^{-h_{prof}}=\varepsilon^{-1}.
\]

Thus the large condition number of `A_Q` does **not** enter the Leray operator norm.

## 3. Exact normalized `H^m` contraction

For every real `m`, define the source-normalized whole-space norm

\[
\boxed{
\|f\|_{H^m_Q}
:=
\|T_Q f\|_{H^m(\mathbb R^3_y)}.
}
\tag{AL6}

Then by Plancherel and (AL5),

\[
\begin{aligned}
\|\mathbb P_{ws}f\|_{H^m_Q}^2
&=
\int
(1+|\eta|^2)^m
|P_Q(\eta)\widehat{T_Qf}(\eta)|^2\,d\eta\\
&\le
\int
(1+|\eta|^2)^m
|\widehat{T_Qf}(\eta)|^2\,d\eta.
\end{aligned}
\]

Therefore

\[
\boxed{
\|\mathbb P_{ws}f\|_{H^m_Q}
\le
\|f\|_{H^m_Q}.
}
\tag{AL7}
\]

The constant is exactly one and is uniform in `Q`, the dyadic level and the source anisotropy.

Since `P_Q` is a Fourier multiplier in `y`, it commutes with every constant normalized Cartesian derivative `partial_y^alpha`.

## 4. Pressure complement

The complementary symbol

\[
I-P_Q(\eta)
=
\frac{A_Q^{-T}\eta\otimes A_Q^{-T}\eta}
{|A_Q^{-T}\eta|^2}
\]

is also an orthogonal projection. Hence

\[
\boxed{
\|(I-\mathbb P_{ws})f\|_{H^m_Q}
\le
\|f\|_{H^m_Q}.
}
\tag{AL8}
\]

Thus whole-space pressure elimination preserves every source-small factor carried by a forcing in the normalized norm.

## 5. Phase-adapted coefficient norm

Let `k in Z^2` index a reconstructed mean coefficient and let

\[
\mathcal M_{\ell,k}
\]

be its exact physical phase modulation/reconstruction factor, as in `phase_adapted_whole_space_leray_intertwining.md`.

Define

\[
\boxed{
\|m\|_{\mathfrak M^{Q}_{\sigma,m}}
:=
\sum_{k\in\mathbb Z^2}
 e^{\sigma|k|_1}
\left\|
T_Q\mathcal M_{\ell,k}m_k
\right\|_{H^m_y}.
}
\tag{AL9}
\]

Define the coefficient Leray projector modewise by exact physical conjugation:

\[
\boxed{
\mathbb P_{coeff,\ell,k}^{Q}
:=
\mathcal M_{\ell,k}^{-1}
T_Q^{-1}
\mathbb P_Q
T_Q
\mathcal M_{\ell,k}.
}
\tag{AL10}
\]

Equivalently, reconstruct the mode physically, apply the whole-space Leray projector, and return to the coefficient representation.

By definition of the norm and (AL7),

\[
\begin{aligned}
\|\mathbb P_{coeff,\ell}^{Q}m\|_{\mathfrak M^{Q}_{\sigma,m}}
&=
\sum_k e^{\sigma|k|_1}
\|\mathbb P_Q(T_Q\mathcal M_{\ell,k}m_k)\|_{H^m_y}\\
&\le
\sum_k e^{\sigma|k|_1}
\|T_Q\mathcal M_{\ell,k}m_k\|_{H^m_y}.
\end{aligned}
\]

Hence

\[
\boxed{
\|\mathbb P_{coeff,\ell}^{Q}m\|_{
\mathfrak M^{Q}_{\sigma,m}}
\le
\|m\|_{
\mathfrak M^{Q}_{\sigma,m}}.
}
\tag{AL11}
\]

Again the constant is exactly one.

No assumption that the phase modulation itself is an `H^m` isometry is used: the modulation is included inside the definition of the norm on both sides.

## 6. Fixed beta-zero root shift

The designated root character is

\[
M=(1,-2),
\qquad |M|_1=3.
\]

Multiplication by the reconstructed root shifts coefficient index by `M`.  Therefore the analytic lattice weight changes by at most

\[
\boxed{e^{3\sigma}.}
\tag{AL12}
\]

At the chosen

\[
\boxed{\sigma_0=0.005,}
\]

this is a fixed harmless factor independent of `S` and the level.

The large physical radial frequency of the root does not enter the multiplier constant because its phase is part of the reconstructed field inside (AL9).

## 7. Relation to exact source graph scaling

`PhysicalResidualBridge.commonGraph_map` uses precisely the spatial scales

\[
Q^{-1/2}q_r,
\qquad
Q^{-D}q_z,
\]

corresponding to (AL1).  Its exact theorem `commonGraph_physical_residual` identifies the source graph residual with the physical viscosity-one Navier--Stokes residual.

Thus (AL6) is the natural whole-space Cartesian Sobolev norm associated with the same physical scaling already present in the source graph map.  No second or independent PDE rescaling has been introduced.

## 8. What remains

The projector problem itself is now closed in the normalized whole-space norm.  The remaining mean theorem is to show that:

1. source `BaseBounds(b^sharp)` imply uniform finite-order coefficient bounds for the root-augmented transport/stretching operator in `mathfrak M^Q_{sigma_0,m}`;
2. the orbit covariance forcing has the previously audited positive epsilon exponent in this norm;
3. the resulting forward Oseen propagator is uniformly bounded on one boundary-layer collar;
4. the residual mean contraction couples to the growing nonzero orbit without losing those exponents.

These are coefficient/transport estimates.  Whole-space pressure elimination itself introduces **no** anisotropic or lattice loss beyond the fixed shift weight already recorded.

## 9. Consequence

The whole-space Leray operator is compatible with the exact anisotropic source scaling at norm one:

\[
\boxed{
\|\mathbb P_{ws}\|_{H^m_Q\to H^m_Q}
\le1.
}

After exact phase-adapted reconstruction the same is true mode by mode in the analytic mean lattice.  Therefore pressure nonlocality is no longer a source of an `epsilon^{-1}` anisotropy loss for the low-`u` root-augmented cell.
