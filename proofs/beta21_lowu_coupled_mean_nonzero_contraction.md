# Coupled mean/nonzero contraction for the low-`u` boundary-layer cell

**Status:** PROVED ASYMPTOTIC PRODUCT-SPACE BANACH CONTRACTION AFTER THE ROOT/ORBIT SOURCE ESTIMATES / `C^1` PARAMETER DIFFERENTIATION AND FINAL FINITE-DIMENSIONAL IFT STILL OPEN.

The previous theorem layers close the two diagonal propagators and the source estimates needed to couple them:

- `beta21_lowu_phase_adapted_mean_root_oseen_propagator.md` gives the root-augmented mean propagator;
- `beta21_lowu_designated_orbit_complement_propagator_reduction.md` plus `beta21_lowu_off_orbit_weighted_convolution_reduction.md` and `beta21_lowu_uniform_source_bilinear_packet_bound.md` close the hybrid nonzero propagator and off-orbit leakage;
- `beta21_lowu_orbit_covariance_weighted_convolution.md` closes the growing-orbit mean covariance counting;
- `nonzero_mean_sensitivity.md` proves that the mean-to-wave leg is only `O(1)`, while the return wave-to-mean covariance leg gains `epsilon^(1/2-kappa_s)`.

The apparent problem is therefore a two-block Lipschitz matrix with one non-small off-diagonal entry.  This note proves that the full system is nevertheless a contraction in a level-dependent weighted product norm because the product of the two off-diagonal entries tends to zero.

No final exact reset cell, infinite cascade, or Navier--Stokes blowup theorem is claimed here.

## 1. Coupled correction variables

Write the exact field as

\[
U
=U_{base}+M_{des}+U_{orb,S}
+m+z,
\]

where

- `m` is the residual angular-mean correction in the phase-adapted mean space `Y_S`;
- `z` is the residual nonzero-angular correction in the hybrid complement space `Z_S`.

The designated mean root `M_des` and the beta-one/beta-two orbit `U_orb,S` are fixed principal-state coordinates, not Banach unknowns.

Let

\[
\mathcal T_S(m,z)
=
\bigl(
\mathcal T_{m,S}(m,z),
\mathcal T_{z,S}(m,z)
\bigr)
\tag{CP1}
\]

be one forward Duhamel iteration over the local relay collar, using the already constructed root-augmented mean propagator and hybrid nonzero propagator.

## 2. Diagonal Lipschitz constants

The mean nonlinear blocks give

\[
\boxed{
\|\delta\mathcal T_{m,S}\|_{Y_S}
\le
q_{m,S}\|\delta m\|_{Y_S}
+\text{wave-return term},
}
\tag{CP2}
\]

where

\[
\boxed{
q_{m,S}
\le
S^A
\left[
\varepsilon^{9/50-2\kappa_s}
+\varepsilon^{1-2\kappa_s}
+\rho_{S}
\right]
+S^Ae^{-cS}
\longrightarrow0.
}
\tag{CP3}
\]

The nonzero fixed-point theorem gives

\[
\boxed{
\|\delta\mathcal T_{z,S}\|_{Z_S}
\le
q_{z,S}\|\delta z\|_{Z_S}
+\text{mean-input term},
}
\tag{CP4}
\]

with

\[
\boxed{
q_{z,S}
\le
S^A\rho_{S}
+S^Ae^{-c_*S}
\longrightarrow0.
}
\tag{CP5}
\]

Here one may take conservatively

\[
\rho_S
\le
S^A\varepsilon^{1/5}
+S^Ae^{-c_*S}.
\tag{CP6}
\]

All fixed powers of `S` are harmless against the positive epsilon exponents in the source hierarchy.

## 3. Mean-to-wave leg

`nonzero_mean_sensitivity.md` gives the corrected estimate

\[
W_{1/2}\times M_\mu\to W_\mu.
\]

Thus the bare mean-to-wave derivative is bounded but not small.  After inserting the growing orbit and fixed-order polynomial losses, write

\[
\boxed{
\|\delta\mathcal T_{z,S}\|_{Z_S}
\le
q_{z,S}\|\delta z\|_{Z_S}
+c_S\|\delta m\|_{Y_S},
}
\tag{CP7}
\]

with

\[
\boxed{c_S\le C S^{A_c}.}
\tag{CP8}
\]

No claim is made that `c_S=o(1)`.

This is essential: assigning an artificial small factor to the mean-to-wave leg would be incorrect.

## 4. Wave-to-mean return leg

A nonzero perturbation returns to the mean through covariance with a designated `W_{1/2}` wave.  The source rule is

\[
W_{1/2}\times W_\mu
\to
M_{\mu+1/2-\kappa_s}.
\]

The weighted orbit covariance and uniform source bilinear estimates therefore give

\[
\boxed{
\|\delta\mathcal T_{m,S}\|_{Y_S}
\le
q_{m,S}\|\delta m\|_{Y_S}
+b_S\|\delta z\|_{Z_S},
}
\tag{CP9}
\]

where

\[
\boxed{
 b_S
\le
C S^{A_b}
\left[
\varepsilon^{1/2-\kappa_s}
+\rho_S
\right].
}
\tag{CP10}
\]

Hence

\[
\boxed{b_S\to0.}
\tag{CP11}
\]

More importantly,

\[
\boxed{
b_Sc_S\to0}
\tag{CP12}
\]

because `c_S` is only polynomial in `S` whereas `b_S` contains a strictly positive epsilon exponent.

## 5. Lipschitz matrix

For differences, (CP7) and (CP9) give the positive matrix bound

\[
\begin{pmatrix}
\|\delta m'\|\\
\|\delta z'\|
\end{pmatrix}
\le
\begin{pmatrix}
q_{m,S}&b_S\\
c_S&q_{z,S}
\end{pmatrix}
\begin{pmatrix}
\|\delta m\|\\
\|\delta z\|
\end{pmatrix}.
\tag{CP13}
\]

Denote this matrix by

\[
L_S=
\begin{pmatrix}
q_{m,S}&b_S\\
c_S&q_{z,S}
\end{pmatrix}.
\]

Its spectral radius is

\[
\rho(L_S)
=
\frac12
\left[
q_{m,S}+q_{z,S}
+
\sqrt{(q_{m,S}-q_{z,S})^2+4b_Sc_S}
\right].
\tag{CP14}
\]

By (CP3), (CP5), and (CP12),

\[
\boxed{\rho(L_S)\longrightarrow0.}
\tag{CP15}
\]

Thus the coupled system is asymptotically contractive even though one off-diagonal leg is only `O(1)` or polynomially bounded.

## 6. Explicit weighted product norm

The spectral-radius argument can be realized by an explicit Banach norm.

Assume first `b_S,c_S>0` and define

\[
\boxed{
\tau_S:=\sqrt{\frac{b_S}{c_S}}.
}
\tag{CP16}
\]

Use

\[
\boxed{
\|(m,z)\|_{*,S}
:=
\|m\|_{Y_S}
+\tau_S\|z\|_{Z_S}.
}
\tag{CP17}
\]

Then

\[
\begin{aligned}
\|\delta m'\|+
\tau_S\|\delta z'\|
&\le
(q_{m,S}+\tau_Sc_S)\|\delta m\|\\
&\quad+
(b_S+\tau_Sq_{z,S})\|\delta z\|.
\end{aligned}
\]

By the choice of `tau_S`,

\[
\tau_Sc_S=\sqrt{b_Sc_S},
\]

and

\[
\frac{b_S}{\tau_S}=\sqrt{b_Sc_S}.
\]

Therefore

\[
\boxed{
\|\mathcal T_S(U)-\mathcal T_S(V)\|_{*,S}
\le
q_{*,S}
\|U-V\|_{*,S},
}
\tag{CP18}
\]

with

\[
\boxed{
q_{*,S}
\le
\max(q_{m,S},q_{z,S})
+\sqrt{b_Sc_S}
\longrightarrow0.
}
\tag{CP19}
\]

If either off-diagonal coefficient vanishes, the same conclusion follows with any positive fixed weight on the decoupled component.

Thus for sufficiently large levels one may arrange

\[
\boxed{q_{*,S}<1/2.}
\tag{CP20}
\]

## 7. Inhomogeneous radii

The zero-input nonzero defect satisfies

\[
\boxed{
R_{z,S}
\le
S^A\varepsilon^{1/5}
+S^Ae^{-c_*S}.
}
\tag{CP21}
\]

The residual mean forcing consists of:

- old source mean defects;
- genuine zero-character orbit covariance of order `M_{1-kappa_s}`;
- exponentially small nonzero `rM` tails;
- lower-order localized root self-source.

Hence

\[
\boxed{
R_{m,S}
\le
S^A\varepsilon^{1-\kappa_s}
+S^Ae^{-cS}.
}
\tag{CP22}
\]

In the weighted product norm the zero-input size is

\[
R_{*,S}
:=R_{m,S}+\tau_SR_{z,S}.
\tag{CP23}
\]

Although `tau_S` may tend to zero or infinity polynomially/exponentially depending on the chosen coarse bounds, its asymptotic size is controlled by (CP10) and (CP8):

\[
\tau_S
\lesssim
S^A\varepsilon^{1/4-\kappa_s/2}
\]

up to harmless factors when the leading `epsilon^(1/2-kappa_s)` term dominates `b_S`.

Therefore

\[
\boxed{R_{*,S}\to0.}
\tag{CP24}
\]

In particular one can choose a product ball radius

\[
\boxed{r_{*,S}:=2R_{*,S}}
\tag{CP25}
\]

for all sufficiently large levels.

## 8. Ball invariance

For `U` in the ball

\[
\|U\|_{*,S}\le r_{*,S},
\]

use (CP18) with `V=0`:

\[
\|\mathcal T_S(U)\|_{*,S}
\le
R_{*,S}+q_{*,S}r_{*,S}.
\]

If `q_{*,S}<=1/2`, then

\[
R_{*,S}+q_{*,S}(2R_{*,S})
\le2R_{*,S}=r_{*,S}.
\]

Hence

\[
\boxed{
\mathcal T_S(B_{r_{*,S}})
\subset B_{r_{*,S}}.
}
\tag{CP26}
\]

## 9. Exact coupled correction

Banach's fixed-point theorem now gives a unique pair

\[
\boxed{
(m_S,z_S)
}
\tag{CP27}
\]

in the shrinking product ball such that

\[
\boxed{
\mathcal T_S(m_S,z_S)=(m_S,z_S).
}
\tag{CP28}
\]

Within the exact source/physical reconstruction already established, this means the residual mean and nonzero equations vanish simultaneously on the local relay collar for the frozen macroscopic principal parameters.

The correction obeys

\[
\boxed{
\|(m_S,z_S)\|_{*,S}
\le2R_{*,S}	o0.
}
\tag{CP29}
\]

This is a local coupled zero-residual correction theorem **at fixed principal parameter values**.  It is not yet the final reset theorem because the corrected outgoing finite-dimensional Poincare coordinates need not equal their exact reset targets until the macroscopic parameters are adjusted.

## 10. Why triangular solving is equivalent but less transparent

One could first solve the nonzero equation for `z=z(m)` and substitute into the mean equation.  That route gives the same return factor `b_Sc_S` and was used in several earlier theorem layers.

The product-space argument here is stronger conceptually: it shows directly that the full PDE correction map is contractive and that the `O(1)` mean-to-wave sensitivity is harmless because it is paired with a small return channel.

## 11. `C^1` frontier

The remaining local theorem is no longer existence of the coupled correction.  It is parameter dependence.

Let

\[
p=(\kappa,\theta,A_M).
\]

One must prove that the coupled map

\[
\mathcal T_S(p;m,z)
\]

is `C^1` in `p` and that

\[
\boxed{
\|D_p(m_S,z_S)\|_{*,S}
\le S^A R_{*,S}
=o(1)
}
\tag{CP30}
\]

in action-normalized outgoing coordinates.

The source audits already show that fixed parameter differentiation costs only polynomial powers of `S`; the contraction inverse

\[
(I-D_{(m,z)}\mathcal T_S)^{-1}
\]

has norm at most `2` once (CP20) holds.  Thus (CP30) is expected to follow from the same source estimates, but it is recorded as the next theorem rather than silently assumed.

## 12. Consequence

The **Banach/PDE existence part of the low-`u` local correction is now closed** under the source estimates proved in the preceding theorem layers:

\[
\boxed{
\text{frozen principal low-`u` cell}
\Longrightarrow
\text{unique exact coupled residual correction }(m_S,z_S).
}
\]

The remaining local obstacle is finite-dimensional and `C^1`:

1. prove parameter differentiability of the coupled correction;
2. show its normalized derivative is `o(1)`;
3. perturb the already transverse principal Poincare map;
4. apply the finite-dimensional implicit-function theorem to obtain the exact finite-`S` reset target.

No global infinite cascade follows until that reset theorem and the later inter-cell assembly are proved.
