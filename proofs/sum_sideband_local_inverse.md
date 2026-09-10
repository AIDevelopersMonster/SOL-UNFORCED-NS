# Local stable inverse for the unwanted v0.4 sum sideband

**Status:** PROVED MODEL / COEFFICIENT-LEVEL LEMMA. The scalar stable inverse and the quantitative damping gap are rigorous for the exact finite-`u_*` beta-envelope model. Embedding this inverse into the full localized Navier–Stokes packet/correction system remains open.

## 1. Sum-sideband geometry

For the corrected difference relay,

\[
\beta_1=\frac{25}{16},\qquad
\beta_2=\frac9{16},\qquad
\beta_+=\beta_1+\beta_2=\frac{17}{8},
\]

and

\[
x_1=\frac{29}{32}.
\]

For a catalyst coordinate

\[
y\in\left[\frac{11}{10},\frac75\right],
\]

the unwanted sum harmonic has normalized local coordinate

\[
\boxed{
x_+(y)
=\frac{\beta_1x_1+\beta_2y}{\beta_+}.
}
\tag{S1}
\]

At the endpoints,

\[
x_+\left(\frac{11}{10}\right)=\frac{5209}{5440},
\qquad
x_+\left(\frac75\right)=\frac{5641}{5440}.
\]

Hence throughout the full finite-`u_*` resonance bracket,

\[
\boxed{
\frac{5209}{5440}
\le x_+(y)\le
\frac{5641}{5440}.
}
\tag{S2}
\]

In particular the sum branch stays uniformly near `x=1`, while its beta is greater than two.

## 2. Exact finite-`u` net-rate derivative

Recall

\[
H_{\beta,u}(x)
=\frac{u}{\sqrt{1+u^2x^2}}
-\beta^2u\frac{1+u^2x^2}{(1+u^2)^{3/2}}.
\tag{S3}
\]

For every `u>=20`,

\[
\frac{u^3}{(1+u^2)^{3/2}}
=(1+u^{-2})^{-3/2}
>\frac{99}{100}.
\tag{S4}
\]

Also

\[
\frac{u}{\sqrt{1+u^2x^2}}<\frac1x.
\]

Using (S2),

\[
H_{\beta_+,u}(x_+)
<
\frac{5440}{5209}
-
\left(\frac{17}{8}\right)^2
\left(\frac{5209}{5440}\right)^2
\frac{99}{100}.
\]

The right-hand side is the exact rational number

\[
-\frac{10427436688571}{3413770240000}
<-3.
\]

Therefore

\[
\boxed{
H_{17/8,u}(x_+(y))<-3
}
\tag{S5}
\]

uniformly for

\[
u\ge20,
\qquad
\frac{11}{10}\le y\le\frac75.
\]

This is substantially stronger than merely saying that the sum branch lies to the decaying side of its turning point.

## 3. Conversion to the pulse-time rate

For a beta envelope,

\[
\log P_\beta(v)
=\frac{\lambda_0L_s}{u_*}\mathcal E_{\beta,u_*}(x(v)),
\qquad
x(v)=\frac12+\frac{v}{L_s}.
\]

Thus

\[
\frac{d}{dv}\log P_\beta(v)
=\frac{\lambda_0}{u_*}H_{\beta,u_*}(x(v)).
\]

For the sum sideband, (S5) gives the uniform local decay rate

\[
\boxed{
\frac{d}{dv}\log P_+(v)
\le-\gamma_0,
\qquad
\gamma_0:=\frac{3\lambda_0}{u_*}>0.
}
\tag{S6}
\]

throughout any bounded relay collar whose local coordinates stay inside the bracket in (S2).

## 4. Scalar stable inverse

Consider the scalar forced equation for the stable sum-sideband coordinate

\[
z'(v)=a_+(v)z(v)+f_+(v),
\qquad
z(v_-)=0,
\]

with

\[
a_+(v)\le-\gamma_0.
\]

Variation of constants gives

\[
z(v)=\int_{v_-}^{v}
\exp\left(\int_w^v a_+(s)\,ds\right)f_+(w)\,dw.
\]

Since

\[
\exp\left(\int_w^v a_+(s)\,ds\right)
\le e^{-\gamma_0(v-w)},
\]

we obtain the scale-uniform estimate

\[
\boxed{
\|z\|_{L^\infty([v_-,v_+])}
\le\gamma_0^{-1}
\|f_+\|_{L^\infty([v_-,v_+])}.
}
\tag{S7}
\]

The same bound holds in coefficient seminorms after differentiating a fixed number of slow variables, up to the already permitted polynomial factors in `S_*`, provided the coefficient matrix and source satisfy the source-type derivative bounds.

## 5. Stability under frame errors

The actual moving-frame equation carries `O(S_*^{-1})` perturbations. For sufficiently large dyadic level, choose `ell_0` so that

\[
\|E_+(v)\|\le\frac{\gamma_0}{2}
\qquad(\ell\ge\ell_0).
\]

Then the perturbed stable propagator still decays at rate at least `gamma_0/2`, and

\[
\boxed{
\|z\|_\infty
\le\frac{2}{\gamma_0}\|f_+\|_\infty.
}
\tag{S8}
\]

Thus the unwanted principal sum harmonic possesses a uniformly bounded local forward inverse.

## 6. What this proves for the relay program

The v0.4 sum sideband is not merely numerically damped. In the exact finite-`u_*` envelope model it has a quantitative damping gap, and the corresponding local coefficient equation can be solved forward with no loss of a negative power of `epsilon`.

Symbolically,

\[
\boxed{
S_+
\xrightarrow{\text{stable local inverse}}
W_+^{\rm corr},
\qquad
\|W_+^{\rm corr}\|\lesssim\|S_+\|.
}
\tag{S9}
\]

## 7. What this does **not** prove

This lemma does **not** yet establish exact zero-force closure. In the full PDE system the correction `W_+^{corr}` itself creates:

- interactions with the two parents;
- interactions with the child;
- self-interactions;
- curl/localization/cutoff residuals;
- pressure/Leray corrections.

A complete unforced construction must solve the entire coupled correction map, not only its first stable sideband equation.

The next target is therefore a **local nonlinear correction contraction** on the relay collar: show that after extracting the desired child source, all remaining terms are mapped by stable/improved inverses into a ball with contraction constant `<1` at sufficiently large level.
