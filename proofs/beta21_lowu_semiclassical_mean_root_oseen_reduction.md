# Source-normalized semiclassical whole-space mean-root Oseen reduction

**Status:** PROVED UNIFORM ROOT-COEFFICIENT REDUCTION / EXACT SOURCE EQUATION AND COUPLED CONTRACTION STILL OPEN.  This revision incorporates the sharpened direct-curl estimate from `beta21_lowu_designated_mean_root_cauchy_curl_realization.md`.  The principal designated root coefficient is uniformly bounded and every positive-order semiclassical derivative is `O(S^{-a})+o(1)` after division by its natural `h=sqrt(epsilon)` amplitude.  Therefore the root does not create an `exp(poly(S))` Oseen constant.

All statements are made in the isotropically normalized whole-space chart

\[
y=(x-x_0)/\sqrt Q,
\]

not in raw physical coordinates.  The whole-space Leray projector survives this dilation exactly because its Fourier symbol is homogeneous of degree zero.

No exact unforced reset cell or global cascade is claimed here.

## 1. Semiclassical whole-space norm

Let

\[
h:=\sqrt\varepsilon,
\qquad
D_h:=h\nabla_y=h\sqrt Q\,\nabla_x.
\]

For `1<p<infty` and fixed integer `m`, define

\[
\boxed{
\|f\|_{W^{m,p}_{h}}
:=\sum_{|\alpha|\le m}
\|D_h^\alpha f\|_{L^p_y(\mathbb R^3)}.
}
\tag{SO1}
\]

For the auxiliary mean lattice use

\[
\boxed{
\|a\|_{\mathfrak M^p_{\sigma,m,h}}
:=
\sum_{k\in\mathbb Z^2}
 e^{\sigma|k|_1}
 \|M_{\ell,k}a_k\|_{W^{m,p}_{h}}.
}
\tag{SO2}
\]

The source carrier identity is

\[
\boxed{h kB_s\asymp1.}
\tag{SO3}
\]

## 2. Whole-space Leray under the source dilation

If `S_Q` is the pullback by `x=x_0+sqrt(Q)y` together with the scalar velocity normalization, then

\[
\boxed{S_Q\mathbb P_x=\mathbb P_yS_Q.}
\tag{SO4}
\]

Indeed the Leray symbol

\[
P(\xi)=I-\xi\otimes\xi/|\xi|^2
\]

is homogeneous of degree zero.  For every `1<p<infty`, `P_y` is bounded on `L^p` and commutes with `D_h`.  Hence

\[
\boxed{
\|\mathbb P_{coeff,\ell}a\|_{
\mathfrak M^p_{\sigma,m,h}}
\le C_p
\|a\|_{
\mathfrak M^p_{\sigma,m,h}}
}
\tag{SO5}
\]

uniformly in `Q,h,S` and the auxiliary index.

## 3. Semiclassical product price

For `p>3` and sufficiently large fixed `m`, the normalized-coordinate Sobolev embedding gives

\[
\boxed{
\|f\|_\infty
\le C_{m,p}h^{-3/p}\|f\|_{W^{m,p}_h}
}
\tag{SO6}
\]

and

\[
\boxed{
\|fg\|_{W^{m,p}_h}
\le C_{m,p}h^{-3/p}
\|f\|_{W^{m,p}_h}
\|g\|_{W^{m,p}_h}.
}
\tag{SO7}
\]

The same estimate holds after summation in the analytic coefficient lattice because phase indices add and the exponential weight is submultiplicative.

## 4. Sharp designated-root coefficient bound

The exact Cauchy/curl construction gives

\[
\widetilde M_{des}=hV_M
\]

with

\[
\boxed{\|V_M\|_\infty\le C}
\tag{SO8}
\]

and, for every fixed `a>=1`,

\[
\boxed{
\|D_h^aV_M\|_\infty
\le
C_a\left[S^{-a}+h\operatorname{poly}(S)\right].
}
\tag{SO9}
\]

Since `h` decreases exponentially in the source level while `S` grows polynomially,

\[
\boxed{
\sup_{a\le m+1}\|D_h^aV_M\|_\infty
\le C_m
}
\tag{SO10}
\]

uniformly for sufficiently large levels, and every positive-order non-principal contribution tends to zero.

The root lattice shift is the fixed character

\[
M=(1,-2),
\qquad |M|_1=3,
\]

so multiplication by the root costs only the fixed analytic factor

\[
\boxed{e^{3\sigma_0}}
\tag{SO11}
\]

with `sigma_0=0.005`.

## 5. Uniform root transport operator

The root part of the normalized mean linearization is

\[
\mathcal L_Mm
=-\mathbb P_y\left[
(\widetilde M_{des}\cdot\nabla_y)m
+(m\cdot\nabla_y)\widetilde M_{des}
\right].
\]

Since `nabla_y=h^{-1}D_h`,

\[
(\widetilde M_{des}\cdot\nabla_y)m
=(V_M\cdot D_h)m.
\]

Thus the transport coefficient is exactly the uniformly bounded `V_M`; no `h^{-1}` remains.

The stretching term satisfies, at principal level,

\[
\nabla_y\widetilde M_{des}
=O(S^{-1}),
\]

while its localized/frame correction is `o(1)` by (SO9).  Standard fixed-order commutator estimates therefore give

\[
\boxed{
\|\mathcal L_Mm\|_{W^{m-1,p}_h}
\le C_m\|m\|_{W^{m,p}_h}
}
\tag{SO12}
\]

with `C_m` independent of `S` and the dyadic level.

This closes the specific Gronwall concern that remained in the previous revision.

## 6. Root-augmented whole-space Oseen generator

Let

\[
U_{bg}=U_{base}+\widetilde M_{des}.
\]

The slow-base part is handled by the same whole-space forward Oseen structure as in `global_fixed_order_leray_oseen_propagator.md`, now after isotropic source rescaling.  Add `L_M` from Section 5 to the full linear generator.

The functional-analytic target is

\[
\boxed{
\|\mathcal V_M(s,s_0)f\|_{
\mathfrak M^p_{\sigma_0,m,h}}
\le K_{p,m,I}
\|f\|_{
\mathfrak M^p_{\sigma_0,m,h}}
}
\tag{SO13}
\]

on one bounded normalized collar, with `K_{p,m,I}` independent of `S` and the level.

After (SO12), no coefficient in the root part grows with `S`; proving (SO13) now requires only writing the exact source-rescaled mean operator and carrying the usual forward `W^{m,p}` parabolic/transport estimate through the cylindrical/zeroth-order terms.  There is no remaining root-frequency obstruction.

## 7. Residual mean quadratic exponent

The residual mean correction has source size

\[
\|m_{corr}\|
\sim\varepsilon^{1-\kappa_s}
=h^{2-2\kappa_s}
\]

up to fixed polynomial powers of `S`.

One convective derivative costs `h^{-1}` and the `W_h^{m,p}` algebra costs `h^{-3/p}`.  Therefore

\[
\boxed{
\|(m_{corr}\cdot\nabla_y)m_{corr}\|
\lesssim
S^A h^{3-4\kappa_s-3/p}.
}
\tag{SO14}
\]

Choose

\[
\boxed{p=6.}
\tag{SO15}
\]

Then

\[
\boxed{
3-4\kappa_s-3/p
=2.5-4\kappa_s
=2.49996>0.
}
\tag{SO16}
\]

Thus the residual mean self-interaction remains strongly perturbative in the new whole-space norm.

## 8. Orbit covariance and beta-zero residual mean modes

Conjugate beta-one/beta-two orbit pairs lie in the source mean class

\[
W_{1/2}\times W_{1/2}	o M_{1-\kappa_s}.
\]

The `O(S)` orbit cardinality and fixed derivatives contribute only fixed powers of `S`.  Generated `rM`, `r\ne\pm1`, have the much stronger action/analytic margins proved in `beta21_lowu_mean_orbit_harmonic_split_and_covariance_audit.md`.

The exact covariance estimate still to be pinned in the new norm has the form

\[
\boxed{
\|F_{cov}^{orb}\|_{
\mathfrak M^6_{\sigma_0,m,h}}
\le
S^A\varepsilon^{\eta_{cov}}
+S^Ae^{-cS}
}
\tag{SO17}
\]

for some explicit `eta_cov>0`.  The available source exponent `1-kappa_s` leaves ample room for the single derivative/algebra losses in the local Duhamel map.

## 9. Coupling to the nonzero orbit

The order-one root interactions

\[
M+C_j\to C_{j+1},
\qquad
M+Q_n\to Q_{n+1}
\]

are part of the designated nonzero shift generator and are not estimated as perturbative terms.

A residual mean perturbation couples to the nonzero orbit through the old mean-to-wave map.  Its return through covariance must be estimated in the common graph norm.  The extra growing-orbit mode count is polynomial in `S`; the analytic lattice losses are already budgeted by `sigma_0=0.005`.

## 10. Remaining exact obligations

The mean-root frequency/jet problem is now closed at the reduction level.  The remaining tasks are:

1. write the exact source-rescaled whole-space mean equation in `W^{m,6}_{h,y}` and prove the forward propagator bound (SO13);
2. translate the source covariance and mean-to-wave-to-mean estimates into this norm, producing explicit positive epsilon exponents;
3. couple the resulting mean contraction to the corrected nonzero orbit/complement propagator;
4. apply the already proved principal `C^1` transversality to obtain an exact finite-`S` local cell.

## 11. Consequence

For the designated beta-zero root,

\[
\boxed{
\widetilde M_{des}/h=O(1),
\qquad
D_h^a(\widetilde M_{des}/h)=O(S^{-a})+o(1)\quad(a\ge1).
}
\]

Therefore its inclusion in the forward mean generator costs a **uniform** coefficient constant, not `exp(poly(S))`.  The next attack is no longer root localization; it is the exact source-rescaled Oseen/covariance estimate and the common coupled fixed point.
