# Phase-adapted whole-space Oseen propagator with the designated beta-zero root

**Status:** PROVED ROOT-AUGMENTED FORWARD LINEAR PROPAGATOR REDUCTION + PROVED RESIDUAL MEAN QUADRATIC SMALLNESS IN THE PARABOLIC GRAPH NORM / ORBIT-COVARIANCE AND FULL COUPLED MEAN-NONZERO C1 CLOSURE STILL OPEN.

This note closes the linear whole-space mean obstruction left by
`beta21_lowu_mean_orbit_harmonic_split_and_covariance_audit.md`.

The designated beta-zero root

\[
M=P-2C
\]

is an angular-mean coefficient of source size `M_{1/2}`.  In raw reconstructed physical coordinates it is highly oscillatory, so the old fixed ordinary-`H^m` theorem `global_fixed_order_leray_oseen_propagator.md` must not be reused by simply replacing `U_0` by `U_0+M_des`.

The correct norm is obtained by combining

1. the **exact source common-graph scaling**;
2. the parabolic scale
   \[
   \eta:=\sqrt\varepsilon;
   \]
3. the anisotropic source axial derivative `D_z=epsilon partial_Z`;
4. exact whole-space Leray conjugation;
5. the one-dimensional beta-zero lattice `rM`.

In that norm the root becomes a uniformly bounded first-order Oseen coefficient.  The remaining nonlinear residual mean correction retains a strictly positive small exponent.

No exact low-`u` reset cell, infinite cascade, or Navier--Stokes blowup theorem is claimed here.

## 1. Exact source-to-physical normalization

The source theorem

`PhysicalResidualBridge.commonGraph_physical_residual`

identifies the actual graph residual with the viscosity-one Cartesian Navier--Stokes residual.  The source theorem

`CommonBaseContext.operators_match_physical`

identifies the actual `graphOperators` coefficients with

\[
G_{n,k}
:=\operatorname{commonGraph}(Q_n,h,k)
\]

at every band and common-cover index.

Thus the graph equation is not a model equation with a modified physical viscosity.  The factor

\[
\varepsilon=Q_n^h
\]

is the exact coefficient produced by the physical graph pullback.

This is recorded in
`beta21_lowu_whole_space_basebounds_physical_bridge.md`.

## 2. Source spatial derivatives and the parabolic scale

Write

\[
\boxed{\eta:=\sqrt\varepsilon.}
\tag{PO1}
\]

On one common graph the mean spatial differential family has, schematically,

\[
D_r=\partial_R+\text{common-torus radial term},
\]

\[
D_z=\varepsilon\partial_Z,
\]

with the ordinary angular derivative suppressed on angularly invariant fields except for the fixed cylindrical frame connection.

The source viscosity is

\[
\varepsilon
\left(
D_r^2+R^{-1}D_r+D_z^2+\text{bounded cylindrical connection}
\right).
\tag{PO2}
\]

Consequently the parabolic differential scale is

\[
\boxed{
\mathscr D_r:=\eta D_r,
\qquad
\mathscr D_z:=\eta D_z.
}
\tag{PO3}
\]

In the common normalized Cartesian graph coordinates `y`, this corresponds to the additional linear dilation

\[
\boxed{
B_\eta
=\operatorname{diag}(\eta,\eta,\eta\varepsilon)
=\operatorname{diag}(\eta,\eta,\eta^3).
}
\tag{PO4}
\]

The two radial-plane entries are equal because the physical radial plane is isotropic before imposing axisymmetry.  The third entry reflects the source identity `D_z=epsilon partial_Z`.

If

\[
y=B_\eta\zeta,
\]

then, at principal Cartesian level,

\[
\varepsilon D_r^2\rightsquigarrow\partial_{\zeta_r}^2,
\qquad
\varepsilon D_z^2\rightsquigarrow\partial_{\zeta_z}^2.
\tag{PO5}
\]

The annular cylindrical connection terms remain zeroth/first order with bounded coefficients because the active core stays a fixed positive normalized distance from the axis.

## 3. Leray remains norm one after both anisotropic dilations

Let `A_Q` denote the exact linear spatial scaling associated with the common graph and let

\[
C_{Q,\eta}:=A_QB_\eta.
\]

Use the unitary dilation

\[
(\mathcal U_{Q,\eta}f)(\zeta)
:=|\det C_{Q,\eta}|^{1/2}
 f(x_0+C_{Q,\eta}\zeta).
\]

The whole-space Leray projector has physical symbol

\[
P(\xi)=I-\frac{\xi\otimes\xi}{|\xi|^2}.
\]

After conjugation by `U_{Q,eta}` its symbol is

\[
\boxed{
P_{Q,\eta}(\xi)
=I-\frac{C_{Q,\eta}^{-T}\xi\otimes C_{Q,\eta}^{-T}\xi}
{|C_{Q,\eta}^{-T}\xi|^2}.
}
\tag{PO6}
\]

For every nonzero `xi`, (PO6) is still the orthogonal projection onto

\[
(C_{Q,\eta}^{-T}\xi)^\perp.
\]

Hence

\[
\boxed{\|P_{Q,\eta}(\xi)\|_{op}\le1}
\tag{PO7}
\]

for every band, every `eta`, and every anisotropy ratio.

Because (PO6) is a constant-coefficient Fourier multiplier in `zeta`, it commutes with every `partial_zeta^alpha`.  Therefore

\[
\boxed{
\|\mathcal U_{Q,\eta}\mathbb P_{ws}\mathcal U_{Q,\eta}^{-1}f\|_{H^m_\zeta}
\le\|f\|_{H^m_\zeta}.
}
\tag{PO8}
\]

This strengthens `beta21_lowu_anisotropic_leray_graph_norm.md`: adding the parabolic dilation does not change the projection constant.

## 4. Phase-adapted beta-zero lattice

The entire angular-mean auxiliary lattice is one-dimensional.  Since

\[
\beta(a,b)=2a+b,
\]

we have

\[
\beta(a,b)=0
\Longleftrightarrow
(a,b)=r(1,-2)=rM,
\qquad r\in\mathbb Z.
\tag{PO9}
\]

Let

\[
\Theta_r=r\Theta_M.
\]

The linearity of reconstruction in the auxiliary character gives this identity exactly.

For a coefficient sequence `a=(a_r)`, define the parabolically normalized phase-adapted norm

\[
\boxed{
\|a\|_{\mathcal Y_{\sigma,m}}:=
\sum_{r\in\mathbb Z}
 e^{3\sigma|r|}
 \left\|
 \mathcal U_{Q,\eta}
 \bigl(e^{i\Theta_r}a_r\bigr)
 \right\|_{H^m_\zeta}.
}
\tag{PO10}
\]

The factor `3` is exact because

\[
|rM|_1=3|r|.
\]

By (PO8), whole-space Leray is bounded on (PO10) with norm at most one, mode by mode and after summation.

## 5. Parabolic carrier size of the designated root

The low-`u` boundary layer has

\[
\delta_S=\kappa_S/S,
\qquad
\kappa_S=\kappa_*+O(S^{-1}).
\]

The exact source-normalized carrier satisfies

\[
\eta\,kB_s=O(1).
\]

The beta-zero root phase is the radial mismatch between the beta-two parent and twice the beta-one catalyst.  Hence on a strict compact core

\[
\boxed{
|\nabla_\zeta\Theta_M|
\le \frac{C}{S}
}
\tag{PO11}
\]

for all sufficiently large levels.

The Cauchy/curl construction in
`beta21_lowu_designated_mean_root_cauchy_curl_realization.md`
gives

\[
M_{des}
=\eta\,\mathfrak m_M e^{i\Theta_M}
+\eta\,\overline{\mathfrak m_M}e^{-i\Theta_M}
+R_M,
\tag{PO12}
\]

with exact divergence-free physical reconstruction and

\[
\boxed{
\left\|\eta^{-1}M_{des}\right\|_{W^{m+1,\infty}_\zeta}
\le C_m
}
\tag{PO13}
\]

at every fixed order needed below.  More precisely, derivatives falling on the principal phase gain `S^{-1}`, while derivatives of the localized/curl remainder are `o(1)` after division by `eta`.

Thus the high raw physical carrier has disappeared from the coefficient constant in the correct parabolic graph scale.

## 6. Root transport is an order-one first-order coefficient

Every graph spatial derivative entering the mean transport may be written in the parabolic variables as

\[
D_j=\eta^{-1}\widetilde D_j,
\tag{PO14}
\]

where `tilde D_j` is a bounded smooth first-order operator in `zeta`; for the principal Cartesian part it is an ordinary `zeta` derivative.

Therefore

\[
(M_{des}\cdot D)m
=\left(\eta^{-1}M_{des}\right)\cdot\widetilde Dm.
\tag{PO15}
\]

By (PO13), the coefficient in (PO15) has a fixed `W^{m+1,infinity}` bound independent of the dyadic level.

The principal root has no radial polarization and its phase normal is radial.  Hence its principal self-advection is zero.  For the linearized stretching term one obtains the stronger coefficient estimate

\[
\boxed{
\|DM_{des}\|_{W^{m,\infty}_\zeta}
\le C_m\left(S^{-1}+o(1)\right).
}
\tag{PO16}
\]

No inverse power of `eta` remains.

## 7. The analytic lattice shift costs only a fixed constant

Multiplication by the positive root character sends

\[
rM\mapsto(r+1)M,
\]

and its conjugate sends

\[
rM\mapsto(r-1)M.
\]

The analytic weights satisfy

\[
e^{3\sigma|r\pm1|}
\le e^{3\sigma}e^{3\sigma|r|}.
\]

Therefore the two root shifts obey

\[
\boxed{
\|R_M^{\pm}a\|_{\mathcal Y_{\sigma,m}}
\le e^{3\sigma}\,C_m
\|a\|_{\mathcal Y_{\sigma,m+1}}.
}
\tag{PO17}
\]

At the fixed choice

\[
\sigma_0=0.005,
\]

the lattice price is

\[
\boxed{e^{3\sigma_0}=e^{0.015}.}
\tag{PO18}
\]

It is an absolute constant.  In particular there is no `e^{cS}` factor and no `O(S) x O(S)` inverse.

## 8. Uniform linear energy estimate

Let `L_base` denote the root-free whole-space mean generator already treated in `global_fixed_order_leray_oseen_propagator.md`, written after the exact graph and parabolic conjugations above.  The fixed slow base contributes bounded coefficients; the principal swirl cancellation remains zeroth order; all source-small slow-base perturbations are `o(1)`.

Let `L_M` be the two terms

\[
\mathcal L_Mm
=-\mathbb P_{ws}
\left[(M_{des}\cdot\nabla)m+(m\cdot\nabla)M_{des}\right]
\]

written in the normalized graph variables.

By (PO13)--(PO17), the first term is a uniformly bounded first-order coefficient operator and the second is bounded zeroth/first order with coefficient `O(S^{-1})+o(1)`.

For one fixed integer `m>=6`, ordinary differentiated parabolic energy in the `zeta` variables gives

\[
\begin{aligned}
\frac d{ds}\|m\|_{\mathcal Y_{\sigma_0,m}}^2
&+c_0\|\nabla_\zeta m\|_{\mathcal Y_{\sigma_0,m}}^2\\
&\le
C_{m,I}\|m\|_{\mathcal Y_{\sigma_0,m}}^2
+C_{m,I}\|F\|_{\mathcal Y_{\sigma_0,m}}^2,
\end{aligned}
\tag{PO19}
\]

where `c_0>0` and `C_{m,I}` are independent of `S` and the dyadic level for all sufficiently large levels.

The first-order root transport is absorbed by Young's inequality against the parabolic derivative term; no skew-adjointness assumption is needed.  The exact Leray projector contributes no loss by (PO8).

Thus the forward propagator satisfies

\[
\boxed{
\|\mathcal V_{M,S}(s,s_0)f\|_{\mathcal Y_{\sigma_0,m}}
\le K_{m,I}
\|f\|_{\mathcal Y_{\sigma_0,m}},
}
\tag{PO20}
\]

and

\[
\boxed{
\left\|
\int_{s_0}^{s}\mathcal V_{M,S}(s,\tau)F(\tau)d\tau
\right\|_{\mathcal Y_{\sigma_0,m}}
\le K_{m,I}|I|
\|F\|_{L^\infty_s\mathcal Y_{\sigma_0,m}}.
}
\tag{PO21}
\]

The constants are uniform in the size of the beta-zero Fourier truncation and, in the completed weighted lattice, in the full integer chain.

## 9. Why the large-`r` mean chain is not a new inverse problem

For `rM`, the viscous principal rate is already known to be

\[
\lambda_{rM}=-c_M(r/S)^2.
\tag{PO22}
\]

This gives additional high-`r` damping, but it is **not needed** for the basic propagator bound (PO20).  The weighted root shift is bounded by (PO17), while the parabolic energy handles the derivative.

The quadratic rate (PO22) is useful only for sharper tails and for fallback static inversion estimates.

## 10. Residual mean quadratic nonlinearity still has a positive exponent

The residual mean correction has the source scale

\[
m_{corr}=O(\varepsilon^{1-\kappa_s})
=O(\eta^{2-2\kappa_s}).
\tag{PO23}
\]

The parabolic spatial dilation has determinant

\[
\det B_\eta=\eta^2(\eta\varepsilon)=\eta^5.
\tag{PO24}
\]

Under unitary dilation the standard `H^m`, `m>3/2`, algebra estimate therefore introduces at worst the fixed factor

\[
\eta^{-5/2}.
\tag{PO25}
\]

A graph convective derivative contributes one further factor `eta^{-1}` through (PO14).  Hence the worst quadratic residual estimate is

\[
\boxed{
\|\mathcal B(m_{corr},m_{corr})\|
\lesssim
S^A
\eta^{-7/2}
\eta^{4-4\kappa_s}
=
S^A\eta^{1/2-4\kappa_s}.
}
\tag{PO26}
\]

The source uses

\[
\kappa_s=10^{-5},
\]

so

\[
\boxed{
\frac12-4\kappa_s=0.49996>0.
}
\tag{PO27}
\]

Therefore the residual mean self-interaction remains perturbative even after paying the full three-dimensional anisotropic parabolic Sobolev scaling cost.

This is deliberately conservative: axisymmetry and the actual support geometry can improve the exponent, but no improvement is required.

## 11. Orbit-generated mean forcing

The orbit-covariance audit gives

\[
\|F_{rM}^{gen}\|
\le
S^A\left(e^{-0.176S}+e^{-0.233S}\right)
+S^A\varepsilon^{1-\kappa_s}.
\tag{PO28}
\]

The analytic weight at `sigma_0=0.005` consumes only about `10^{-3}S` in the worst parent-difference direction, leaving a large fixed exponential gap.

The propagator estimate (PO21) therefore preserves every exponentially small `rM` forcing.  The genuine zero-character covariance term remains at the ordinary source scale `M_{1-kappa_s}`.

The remaining publication-level task is not the linear propagation of these terms; it is to write the actual `O(S)` orbit covariance sum in the norm (PO10) with its complete curl/frame coefficient bookkeeping.

## 12. Mean-to-wave interface

The same root is already inserted as a designated coefficient in the nonzero orbit generator.  A residual mean perturbation of order `M_mu` changes the designated wave orbit at order `W_mu`, while the return covariance with a designated `W_{1/2}` wave gains

\[
\varepsilon^{1/2-\kappa_s}.
\]

The root-augmented mean propagator (PO20) adds no adverse epsilon power to this round trip.  Thus the target growing-orbit feedback remains

\[
\boxed{
\|\delta\mathcal N_{w\to m}\|
\le
S^A\left[
\varepsilon^{1/2-\kappa_s}
+\rho_{S,\ell}
\right]
\|\delta m\|,
}
\tag{PO29}
\]

subject only to the already isolated exact source packet summation.

## 13. Parameter dependence

The macroscopic root amplitude `A_M`, boundary-layer spacing parameter `kappa`, and phase parameter `theta` vary in a fixed compact neighborhood of the principal reset point.

At every fixed parameter-differentiation order:

- the normalized root coefficient and its `zeta` jets remain uniformly bounded;
- differentiating the fixed character shift does not change the lattice displacement;
- the Leray symbol remains an orthogonal projection;
- all source coefficient changes cost at most fixed powers of `S`.

Therefore

\[
\boxed{
\|D_{(\kappa,\theta,A_M)}\mathcal V_{M,S}\|
\le S^{A_m}K_{m,I}
}
\tag{PO30}
\]

for a fixed finite exponent `A_m`.  This is compatible with the exponentially/sourced-small correction required by the final `C^1` implicit-function argument.

## 14. Closed and open parts

The following obstruction is now closed:

\[
\boxed{
\text{the designated oscillatory angular-mean root admits a dyadically uniform}
\atop
\text{whole-space forward Oseen propagator in the correct phase/parabolic norm.}
}
\tag{PO31}
\]

The closure uses:

1. exact source-to-physical graph matching;
2. exact viscosity-one physical residual scaling;
3. exact anisotropic whole-space Leray norm one;
4. parabolic dilation `B_eta`;
5. fixed root lattice shift `M=(1,-2)`;
6. uniform normalized root coefficient jets;
7. forward parabolic energy, not a static mean inverse.

Still open before an exact finite-`S` low-`u` reset theorem:

1. the actual curl/Leray off-orbit estimate `(DC14)--(DC15)` in the nonzero block;
2. the complete `O(S)` orbit covariance estimate in the norm (PO10);
3. the common coupled mean/nonzero contraction with all polynomial multiplicities displayed;
4. `C^1` transfer of that coupled correction to `(kappa,theta,A_M)`;
5. the final finite-dimensional implicit-function correction.

No global unforced Navier--Stokes claim follows from (PO31).
