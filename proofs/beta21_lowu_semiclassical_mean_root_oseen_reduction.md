# Source-normalized semiclassical whole-space mean-root Oseen reduction

**Status:** PROVED FUNCTIONAL-ANALYTIC REDUCTION IN THE ISOTROPIC SOURCE CHART / EXACT SOURCE-LEVEL OSEEN AND COUPLED FIXED POINT STILL OPEN.  This revision corrects the coordinate scaling of the previous version.  The relevant semiclassical derivative is

\[
\boxed{h\nabla_y=h\sqrt Q\,\nabla_x,}
\]

where `y=(x-x_0)/sqrt(Q)` is the source-normalized whole-space Cartesian coordinate.  It is not `h nabla_x` in raw physical coordinates.

The dilation maps `R^3` to `R^3`; no artificial boundary is introduced.  Because the Leray projector is a degree-zero whole-space Fourier multiplier, its `L^p` bounds are invariant under this isotropic dilation.  In the normalized chart the designated beta-zero root has amplitude `O(h)`, covector `O((hS)^{-1})`, and therefore uniformly admissible semiclassical jets.

The preferred concrete exponent remains `p=6`.  The remaining tasks are exact source insertion and the common mean/nonzero graph fixed point.  No exact unforced reset cell or global cascade is claimed.

## 1. Normalized whole-space chart and semiclassical scale

Let

\[
\boxed{h:=\sqrt\varepsilon}
\tag{SO1}
\]

and use the isotropic source chart

\[
\boxed{y=\frac{x-x_0}{\sqrt Q}.}
\tag{SO2}
\]

For the source-normalized velocity representative write schematically

\[
\widetilde u(y)=Q^A u_{phys}(x_0+\sqrt Q\,y).
\]

The carrier normalization gives

\[
\boxed{h kB_s\asymp1.}
\tag{SO3}
\]

Thus the natural semiclassical derivative is

\[
\boxed{D_h:=h\nabla_y=h\sqrt Q\,\nabla_x.}
\tag{SO4}
\]

For `1<p<infty` and integer `m>=0`, define

\[
\boxed{
\|f\|_{W^{m,p}_{h,y}}
:=
\sum_{|\alpha|\le m}
\|D_h^\alpha f\|_{L^p_y(\mathbb R^3)}.
}
\tag{SO5}
\]

In these normalized coordinates the source viscous operator has coefficient `epsilon=h^2`, so `D_h` is also the natural parabolic derivative scale.

## 2. Isotropic dilation and whole-space Leray

Let `S_Q` denote the pullback under `x=x_0+sqrt(Q)y` together with the scalar velocity normalization.  Translation and isotropic dilation preserve the direction of the Fourier covector.  The Leray symbol

\[
P(\xi)=I-\frac{\xi\otimes\xi}{|\xi|^2}
\]

is homogeneous of degree zero.  Therefore

\[
\boxed{
S_Q\mathbb P_x
=\mathbb P_yS_Q.
}
\tag{SO6}
\]

For every `1<p<infty`, `P_y` is bounded on `L^p` and commutes with the constant-coefficient derivatives `D_h`.  Hence

\[
\boxed{
\|\mathbb P_y f\|_{W^{m,p}_{h,y}}
\le C_p\|f\|_{W^{m,p}_{h,y}}
}
\tag{SO7}
\]

with a constant independent of `Q,h,S`.

For auxiliary mode `k`, conjugate by the exact source reconstruction modulation `M_{ell,k}` and define

\[
\boxed{
\|a\|_{\mathfrak M^p_{\sigma,m,h}}
:=
\sum_k e^{\sigma|k|_1}
\|M_{\ell,k}a_k\|_{W^{m,p}_{h,y}}.
}
\tag{SO8}
\]

Then the exact coefficient Leray operator satisfies

\[
\boxed{
\|\mathbb P_{coeff,\ell}a\|_{
\mathfrak M^p_{\sigma,m,h}}
\le C_p
\|a\|_{\mathfrak M^p_{\sigma,m,h}}.
}
\tag{SO9}
\]

## 3. Semiclassical embedding and algebra price

For `p>3` and sufficiently large fixed integer `m`, scaling in the normalized `y` variable gives

\[
\boxed{
\|f\|_{L^\infty_y}
\le C_{m,p}h^{-3/p}
\|f\|_{W^{m,p}_{h,y}}.
}
\tag{SO10}
\]

and

\[
\boxed{
\|fg\|_{W^{m,p}_{h,y}}
\le
C_{m,p}h^{-3/p}
\|f\|_{W^{m,p}_{h,y}}
\|g\|_{W^{m,p}_{h,y}}.
}
\tag{SO11}
\]

The exact phase-addition identity and

\[
e^{\sigma|k+j|_1}
\le e^{\sigma|k|_1}e^{\sigma|j|_1}
\]

give the same coefficient-lattice estimate.

This explicit `h^{-3/p}` is the only Sobolev-embedding loss introduced by the whole-space `L^p` algebra.  The `Q` dilation produces no additional operator loss because all norms are taken in the normalized whole-space `y` chart.

## 4. Correct root scale

The Cauchy/curl theorem `beta21_lowu_designated_mean_root_cauchy_curl_realization.md` gives in the same normalized chart

\[
\boxed{\|\widetilde M_{des}\|_\infty=O(h),}
\tag{SO12}
\]

and

\[
\boxed{
\frac{c_-}{S}
\le h|\Xi_M|
\le\frac{c_+}{S},
\qquad
\Xi_M=\nabla_y\widetilde\Theta_M.
}
\tag{SO13}
\]

Thus its pure-phase semiclassical jets satisfy

\[
\boxed{
\|D_h^a\widetilde M_{des}^{principal}\|_\infty
\le C_a hS^{-a}.
}
\tag{SO14}
\]

The exact curl/localization remainder has an additional `hS poly(S)=o(1)` relative factor at fixed source order.  The source-level target is therefore

\[
\boxed{
\|D_h^a\widetilde M_{des}\|_\infty
\le C_a h\,\operatorname{poly}(S)(1+S^{-a}),
}
\tag{SO15}
\]

with the leading coefficient uniformly `O(h)`.

## 5. Mean-root transport operator

The root contribution to the normalized projected mean linearization is

\[
\mathcal L_Mm
=-\mathbb P_y
\left[
(\widetilde M_{des}\cdot\nabla_y)m
+(m\cdot\nabla_y)\widetilde M_{des}
\right].
\]

Write

\[
\nabla_y=h^{-1}D_h.
\]

The transport coefficient is

\[
\widetilde M_{des}/h=O(1).
\]

At principal level, each `D_h` derivative falling on that coefficient gains `S^{-1}`.  Therefore the frozen principal root defines an `O(1)` first-order semiclassical operator.

The stretching coefficient satisfies

\[
\boxed{
\|\nabla_y\widetilde M_{des}^{principal}\|_\infty
=O(S^{-1}).
}
\tag{SO16}
\]

The exact source/curl remainder changes this by the already isolated lower source class.  Consequently the source-level target estimate is

\[
\boxed{
\|\mathcal L_Mm\|_{W^{m-1,p}_{h,y}}
\le C\operatorname{poly}(S)
\|m\|_{W^{m,p}_{h,y}},
}
\tag{SO17}
\]

with an **actual leading operator constant `O(1)`**.  The publication-level task is to replace the conservative polynomial in (SO17) by the exact source small factors for the localization/frame remainder, so that the full forward propagator constant is uniform rather than `exp(poly(S))`.

In auxiliary coefficient space the root shifts the lattice by

\[
M=(1,-2),\qquad |M|_1=3.
\]

Thus the analytic lattice penalty is only

\[
\boxed{e^{3\sigma_0}}
\tag{SO18}
\]

with `sigma_0=0.005`, independent of `S`.

## 6. Whole-space root-augmented Oseen target

Let

\[
U_{bg}=U_{base}+\widetilde M_{des}
\]

in normalized coordinates.  The old slow-base Oseen argument remains valid after isotropic rescaling because the whole-space geometry and Leray projector are unchanged up to conjugation.

Include the **principal** root transport in the linear generator.  If the lower-order source/curl remainder in (SO17) is shown to be `o(1)` in the same graph norm, the standard forward parabolic/transport argument yields

\[
\boxed{
\|\mathcal V_M(s,s_0)f\|_{
\mathfrak M^p_{\sigma_0,m,h}}
\le K_{p,m,I}
\|f\|_{
\mathfrak M^p_{\sigma_0,m,h}},
}
\tag{SO19}
\]

with `K_{p,m,I}` independent of `S` and the dyadic level.

Thus the only unresolved linear issue is no longer the large root frequency; it is the sharp source estimate for the localized/frame remainder of the exact Cauchy root.

## 7. Residual mean quadratic exponent

Let the residual mean correction have the old source size

\[
\|m_{corr}\|
\sim\varepsilon^{1-\kappa_s}
=h^{2-2\kappa_s}
\]

up to fixed powers of `S` in the normalized source norm.

One convective derivative contributes `h^{-1}`, and the semiclassical algebra contributes `h^{-3/p}`.  Therefore

\[
\boxed{
\|(m_{corr}\cdot\nabla_y)m_{corr}\|
\lesssim
S^A h^{3-4\kappa_s-3/p}.
}
\tag{SO20}
\]

For every `p>3` the exponent is positive.  Choose

\[
\boxed{p=6.}
\tag{SO21}
\]

Then

\[
\boxed{
3-4\kappa_s-3/p
=2.5-4\kappa_s
=2.49996>0.
}
\tag{SO22}
\]

Hence the residual mean self-interaction remains strongly perturbative.

## 8. Orbit covariance and generated beta-zero means

The designated beta-one/beta-two orbit waves remain source order `W_{1/2}`.  Genuine conjugate covariance lies in `M_{1-kappa_s}`.  The `O(S)` orbit multiplicity and fixed derivatives cost only fixed powers of `S`.

Generated nonzero `rM` auxiliary mean coefficients have the action/analytic gaps proved in `beta21_lowu_mean_orbit_harmonic_split_and_covariance_audit.md`; after `sigma_0=0.005` they retain gaps larger than `0.176S` and `0.233S` before polynomial factors.

The exact source-level covariance estimate required for the common graph norm is therefore of the form

\[
\boxed{
\|F_{cov}^{orb}\|_{
\mathfrak M^6_{\sigma_0,m,h}}
\le
S^A\varepsilon^{\eta_{cov}}
+S^Ae^{-cS}
}
\tag{SO23}
\]

for some explicit `eta_cov>0`.  Establishing the sharp value is a bookkeeping/interface step; the source exponent `1-kappa_s` leaves substantial room for the single semiclassical derivative/algebra loss.

## 9. Coupling to the designated nonzero orbit

The principal root interactions

\[
M+C_j\to C_{j+1},
\qquad
M+Q_n\to Q_{n+1}
\]

are already included exactly in the designated nonzero shift generator.  They are not estimated as small terms.

A residual mean perturbation couples to the nonzero orbit through the old mean-to-wave map and then returns through covariance.  The growing orbit adds polynomial mode-count factors and the explicit semiclassical `h` losses above, but no exponential lattice loss beyond the already budgeted `sigma_0` factors.

The final common contraction must record one explicit positive exponent for this loop.

## 10. Remaining exact obligations

The corrected norm leaves four concrete tasks:

1. sharpen the exact curl/frame remainder in (SO15)--(SO17) to an `O(1)+o(1)` coefficient bound in the normalized chart;
2. prove the forward root-augmented Oseen propagator (SO19) in the coefficient lattice;
3. translate the orbit covariance and mean-to-wave-to-mean source estimates into the normalized `W^{m,6}_{h,y}` graph norm with explicit positive epsilon exponents;
4. couple that mean solve to the corrected nonzero orbit/complement propagator and apply the already proved principal transversality.

No raw-physical estimate using `h nabla_x` should be used; the `sqrt(Q)` source dilation is essential.

## 11. Consequence

The high physical frequency of the beta-zero mean root is compatible with whole-space pressure and forward Oseen propagation once the **actual source normalization** is used:

\[
\boxed{D_h=h\sqrt Q\,\nabla_x=h\nabla_y.}
\]

The whole-space Leray projector survives the isotropic dilation exactly, and the root phase increment is only `O(S^{-1})` in this semiclassical derivative.  The remaining barrier is now a sharp source/curl remainder bound, not a carrier-frequency blowup.
