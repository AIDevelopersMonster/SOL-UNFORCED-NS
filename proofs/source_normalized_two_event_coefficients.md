# Source-normalized designated coefficients for the v0.8 two-event cell

**Status:** PROVED SOURCE-NORMALIZED NONVANISHING / UNIFORM COEFFICIENT-FIELD THEOREM for the two designated quadratic events, after freezing one sufficiently large v0.8 design `M` and one fixed nonnegative overlap profile in each bounded interaction collar. The theorem includes the exact `epsilon,k,B_s` normalization, the leading Leray projection, envelope matching, source moving-frame error, and the curl remainder size. It proves a continuous uniformly nonzero coefficient field over any compact strict-cone slow set.

It does **not** claim that the coefficient converges to one universal number when the slow profile point drifts from cell to cell. That stronger statement is unnecessary and, without convergence of the slow profile point, is not justified by the source. The remaining exact-PDE obligation is the uniform `C^1` passage from this designated coefficient field to the complete two-collar zero-residual renewal map.

Primary source: OpenAI, *Finite Time Blowup for Navier--Stokes*, equations (7.2)--(7.13), Proposition 7.2, Lemma 7.4, Lemma 7.7, Proposition 9.1 and Lemma 9.2.

## 1. Frozen design and slow parameter set

Fix one sufficiently large integer `M` from `integral_beta_v08_large_u_halfstep_family.md` and put

\[
u:=u_*=M^2,
\qquad
\beta_P=2,
\qquad
\beta_C=1.
\tag{SC1}
\]

Let

\[
x_M,
\qquad
y_M=\left(1+\frac1{2M}\right)x_M,
\qquad
c_M=\left(1-\frac1{2M}\right)x_M
\tag{SC2}
\]

be the exact first-event resonance coordinates. Let `theta_M^ren` be the exact second-event resonance from `v08_beta2_feedback_renewal.md`.

Let `K_slow` be a compact subset of the strict source admissible slow annulus on which the relay is placed. The source strict cone and shear bounds give

\[
\boxed{
0<\lambda_-\le \lambda_0(p)\le\lambda_+<\infty,
\qquad p\in K_{\rm slow}.
}
\tag{SC3}
\]

All constants below may depend on the frozen `M`, the two fixed collar profiles, and `K_slow`, but not on the physical band level `ell`.

## 2. Exact cancellation of the apparent carrier-scale factor

At level `ell`, the source chooses

\[
k_\ell=\lceil\varepsilon_\ell^{-1/2}\rceil
\tag{SC4}
\]

and, from source (7.2),

\[
B_{s,\ell}(p)^2
=
\frac{\lambda_0(p)}
{\varepsilon_\ell k_\ell^2(1+u^2)^{3/2}}.
\tag{SC5}
\]

Therefore the coefficient that appears when one phase derivative hits a quadratic product of two `W_{1/2}` waves is not merely asymptotically bounded: its reference value is **exactly scale independent**,

\[
\boxed{
\rho(p)
:=\sqrt{\varepsilon_\ell}\,k_\ell B_{s,\ell}(p)
=
\frac{\sqrt{\lambda_0(p)}}{(1+u^2)^{3/4}}.
}
\tag{SC6}
\]

In particular,

\[
\boxed{
0<\rho_-\le\rho(p)\le\rho_+<\infty
}
\tag{SC7}
\]

uniformly on `K_slow`.

This is the key normalization identity. The two parent velocities each carry `sqrt(epsilon)`; the principal derivative contributes `k B_s`; after dividing the child equation by its natural `sqrt(epsilon)` wave scale, the remaining factor is exactly `rho(p)`.

## 3. First event: `2-1 -> 1`

At the first collar use the reference slopes

\[
s_P=ux_M,
\qquad
s_C=uy_M,
\qquad
s_D=uc_M.
\tag{SC8}
\]

Let `Gamma_1(M)` be the growing-frame coordinate of the Leray-projected principal difference interaction after removing the common factor `k B_s`. In the notation of `v08_designated_projection_nonvanishing.md`,

\[
\boxed{
\Gamma_1(M)=A_+^{(1)},
\qquad
\Gamma_1(M)<0,
\qquad
|\Gamma_1(M)|\ge\frac{3M}{16}.
}
\tag{SC9}
\]

Choose a fixed real overlap profile

\[
\omega_1\in C_c^\infty((-L_1,L_1)),
\qquad
\omega_1\ge0,
\qquad
\omega_1\not\equiv0,
\tag{SC10}
\]

inside the translated common collar. This is a construction parameter, not an external force.

Let `P_P,P_C,P_D` denote the exact reference beta envelopes. The exact finite-`M` resonance gives at the collar center

\[
\boxed{P_P(0)P_C(0)=P_D(0).}
\tag{SC11}
\]

For a bounded pulse offset `xi`, the normalized envelope ratio is

\[
R_{1,\ell}(p,\xi)
:=
\frac{P_P(v_1+\xi)P_C(v_1+\xi)}{P_D(v_1+\xi)}.
\tag{SC12}
\]

Because all three reduced pulse coordinates change by `xi/L_s`, Taylor expansion of the exact envelope primitive gives, uniformly for `|xi|<=L_1`,

\[
\boxed{
R_{1,\ell}(p,\xi)
=
\exp\!\big(\mu_1(p)\xi\big)
\left(1+O_M(L_s^{-1})\right),
}
\tag{SC13}
\]

where

\[
\mu_1(p)
=a_{2,p}(x_M)+a_{1,p}(y_M)-a_{1,p}(c_M)
\tag{SC14}
\]

and

\[
a_{\beta,p}(x)
:=\lambda_0(p)
\left[
\frac1{\sqrt{1+u^2x^2}}
-\beta^2\frac{1+u^2x^2}{(1+u^2)^{3/2}}
\right].
\tag{SC15}
\]

The reference child envelope removes the scalar growing-coordinate homogeneous rate. Source (7.10)--(7.11) leaves an `O(S_*^{-1})` moving-frame/damping error. Hence the renormalized growing Green kernel on a fixed collar is

\[
\boxed{G_{1,\ell}(p;\xi_+,\xi)=1+O_M(S_*^{-1})}
\tag{SC16}
\]

uniformly on the collar.

Up to the fixed Fourier convention factor `varsigma_1` with `|varsigma_1|=1`, the limiting normalized first-event coefficient is therefore

\[
\boxed{
\kappa_1^{0}(p)
=
\varsigma_1\rho(p)\Gamma_1(M)
\int_{-L_1}^{L_1}
\omega_1(\xi)e^{\mu_1(p)\xi}\,d\xi.
}
\tag{SC17}
\]

The integral is strictly positive. By (SC3), (SC7), (SC9) and compactness,

\[
\boxed{
0<c_{1,M}\le |\kappa_1^0(p)|\le C_{1,M}<\infty,
\qquad p\in K_{\rm slow}.
}
\tag{SC18}
\]

Thus the complete source normalization does **not** introduce a hidden vanishing factor into the first designated coefficient.

## 4. Second event: `1+1 -> 2`

At the renewal collar put

\[
s_C^{\rm ren}=u(y_M+\theta_M^{\rm ren}),
\quad
s_D^{\rm ren}=u(c_M+\theta_M^{\rm ren}),
\quad
s_P^{\rm ren}=u(x_M+\theta_M^{\rm ren}).
\tag{SC19}
\]

Let `Gamma_2(M)` be the beta-two growing-frame coordinate of the principal sum interaction after removing the common `k B_s` factor. `v08_beta2_feedback_renewal.md` proves

\[
\boxed{
\Gamma_2(M)>0,
\qquad
\Gamma_2(M)\ge c_{\rm ren,M}>0.
}
\tag{SC20}
\]

Choose another fixed nonnegative nonzero overlap profile

\[
\omega_2\in C_c^\infty((-L_2,L_2)).
\tag{SC21}
\]

The exact second-event envelope resonance gives

\[
\boxed{
P_C(0)P_D(0)=P_P^{\rm ren}(0).
}
\tag{SC22}
\]

The same bounded-offset calculation yields

\[
\frac{P_C(v_2+\xi)P_D(v_2+\xi)}{P_P^{\rm ren}(v_2+\xi)}
=
\exp(\mu_2(p)\xi)
\left(1+O_M(L_s^{-1})\right)
\tag{SC23}
\]

for a continuous bounded function `mu_2(p)` obtained from the three exact net rates at (SC19). The renormalized beta-two Green kernel is `1+O_M(S_*^{-1})` on the fixed collar.

Hence, with another fixed unimodular Fourier convention factor `varsigma_2`, the limiting normalized second-event coefficient is

\[
\boxed{
\kappa_2^{0}(p)
=
\varsigma_2\rho(p)\Gamma_2(M)
\int_{-L_2}^{L_2}
\omega_2(\xi)e^{\mu_2(p)\xi}\,d\xi.
}
\tag{SC24}
\]

Therefore

\[
\boxed{
0<c_{2,M}\le |\kappa_2^0(p)|\le C_{2,M}<\infty,
\qquad p\in K_{\rm slow}.
}
\tag{SC25}
\]

The fact that the beta-two output lies on the decaying side of its turning point does not change this conclusion: the `+` frame coordinate remains a valid coordinate; its net homogeneous rate is simply negative there, and the forward source inverse is bounded.

## 5. Actual phase, frame and curl corrections

The source phase normal satisfies, uniformly on every fixed collar,

\[
n_\Phi
=\beta B_s(s,K)+O(S_*^{-1}),
\qquad
n_\Phi'=O(S_*^{-1}),
\tag{SC26}
\]

and the moving-frame projected matrix differs from its reference diagonal form by `O(S_*^{-1})`. Thus the actual Leray-projected principal interaction coefficients differ from (SC17), (SC24) by `O_M(S_*^{-1})` after the natural `sqrt(epsilon)` normalization.

Taking physical curls produces an exactly divergence-free wave `t+r`. Source Lemma 7.7 gives, for a primary `W_{1/2}` coefficient,

\[
\boxed{r\in W_{1-\kappa_s}.}
\tag{SC27}
\]

Hence every quadratic term in which at least one principal factor `t` is replaced by a curl remainder gains

\[
\boxed{\varepsilon^{1/2-\kappa_s}}
\tag{SC28}
\]

relative to the designated principal source, up to the fixed polynomial `S_*` losses already allowed by the coefficient calculus.

The remaining phase-transport, amplitude-derivative and base-correction terms carry the positive source gains of Proposition 9.1. Therefore the localized designated coefficients before solving the global two-collar remainder satisfy

\[
\boxed{
\kappa_{i,\ell}^{\rm loc}(p)
=\kappa_i^0(p)+o_\ell(1),
\qquad i=1,2,
}
\tag{SC29}
\]

uniformly for `p in K_slow`, where one may take the error to be bounded schematically by a fixed polynomial in `S_*` times positive powers of `epsilon`, together with `O(S_*^{-1})`.

Consequently, after increasing the starting band,

\[
\boxed{
|\kappa_{i,\ell}^{\rm loc}(p)|\ge\frac12c_{i,M}>0,
\qquad i=1,2.
}
\tag{SC30}
\]

## 6. Why a universal limit is not needed

The slow representative `p_ell` along the trapped background spine is known to remain in a compact strict-cone set; it has not been proved to converge to one point. Therefore the correct source statement is the coefficient-field theorem

\[
\boxed{
\kappa_{i,\ell}^{\rm loc}(p_\ell)
=\kappa_i^0(p_\ell)+o(1),
\quad
0<c_{i,M}\le|\kappa_i^0(p)|\le C_{i,M}.
}
\tag{SC31}
\]

It would be unjustified to replace this by `kappa_{i,ell}->kappa_i^*` without an additional convergence theorem for `p_ell`.

This correction strengthens the useful conclusion: the designated coefficient never degenerates anywhere on the allowed compact slow set.

## 7. Consequence for the algebraic renewal state

Let

\[
a(p):=|\kappa_1^0(p)|,
\qquad
b(p):=|\kappa_2^0(p)|.
\]

The principal magnitude renewal map is

\[
(x,y)\mapsto
\left(a(p)b(p)xy^2,\ a(p)xy\right).
\tag{SC32}
\]

Its nonzero fixed magnitude is

\[
\boxed{
x_*(p)=a(p)^{-1},
\qquad
y_*(p)=[a(p)b(p)]^{-1/2}.}
\tag{SC33}
\]

By (SC18), (SC25), this fixed state stays in one compact positive rectangle uniformly over `K_slow`.

Moreover, for

\[
F_p(x,y)
=\left(a(p)b(p)xy^2-x,\ a(p)xy-y\right),
\]

a direct substitution into the Jacobian gives the exact identity

\[
\boxed{
\det D_{x,y}F_p(x_*(p),y_*(p))=-2.
}
\tag{SC34}
\]

Thus transversality is not merely nonzero; it is uniform and independent of the values of the two coefficient magnitudes.

## 8. What is now closed

The source-normalization question isolated in `physical_scale_inheritance_update_v0.4.md` is closed in the form actually needed by the construction:

\[
\boxed{
\text{both designated quadratic coefficients form a continuous uniformly nonzero field on the admissible slow compact set.}
}
\tag{SC35}
\]

The apparent dangerous factor `sqrt(epsilon) k B_s` is exactly scale independent by (SC6), envelope matching is exact at both event centers, and curl/frame corrections are lower order.

## 9. Remaining exact PDE step

What remains before one may call the two-event cell an exact autonomous renewal theorem is **not** coefficient nonvanishing. It is the uniform parameter-dependent fixed-point audit:

\[
\boxed{
\mathscr R_{\ell,p}
=\mathscr R_{0,p}+o_{C^1}(1)
}
\tag{SC36}
\]

on one fixed compact neighborhood of the section (SC33), uniformly for `p in K_slow`.

Once (SC36) is proved, the exact determinant `-2` in (SC34) gives a uniform implicit-function theorem for an exact nonzero two-collar renewal state at every sufficiently high level.

After that, the remaining genuinely global issue is to shadow these local renewal states through the physical cross-`q` transport along the trapped spine.