# Finite-u persistence of the corrected beta-difference relay

**Status:** PROVED MODEL THEOREM for the exact finite-\(u_*\) beta-envelope model. It does not yet include the full localized curl-generated PDE packet system or exact zero-force residual closure.

## 1. Exact envelope

For \(\beta>0\), let

\[
a_\beta=\beta^{-2/3},
\qquad
x_{\beta,u}=\sqrt{a_\beta^2+\frac{a_\beta^2-1}{u^2}},
\]

whenever the square root is real. For the v0.4 values \(\beta\in\{25/16,9/16,1\}\), this is real for every \(u\ge2\).

Define

\[
\begin{aligned}
\mathcal E_{\beta,u}(x)
={}&\operatorname{arsinh}(ux)-\operatorname{arsinh}(ux_{\beta,u})\\
&-\frac{\beta^2}{(1+u^2)^{3/2}}
\left[u(x-x_{\beta,u})+\frac{u^3}{3}(x^3-x_{\beta,u}^3)\right].
\end{aligned}
\tag{P1}
\]

Its reduced limit is

\[
I_\beta(x)=\log x+\frac23\log\beta-\frac{\beta^2x^3}{3}+\frac13.
\tag{P2}
\]

On the compact design set

\[
\beta\in\left\{\frac{25}{16},\frac9{16},1\right\},
\qquad
x\in\left[\frac12,\frac32\right],
\]

the same expansion used in `proofs/beta_phase_stability.md` gives the explicit conservative bound

\[
\boxed{
|\mathcal E_{\beta,u}(x)-I_\beta(x)|\le\frac6{u^2}
}
\tag{P3}
\]

for all \(u\ge20\). The proof uses \(|1-a_\beta^{-2}|<1\), which remains true for both \(\beta_1=25/16\) and \(\beta_2=9/16\).

## 2. Corrected relay data

Set

\[
\beta_1=\frac{25}{16},
\qquad
\beta_2=\frac9{16},
\qquad
x_1=\frac{29}{32},
\]

and

\[
x_c(y)=\beta_1x_1-\beta_2y.
\]

Define

\[
G_u(y)
=\mathcal E_{\beta_1,u}(x_1)
+\mathcal E_{\beta_2,u}(y)
-\mathcal E_{1,u}(x_c(y)).
\tag{P4}
\]

Then

\[
|G_u(y)-G(y)|\le\frac{18}{u^2}.
\tag{P5}
\]

## 3. Existence for all \(u\ge20\)

Use the wider rational bracket

\[
y_-=\frac{11}{10},
\qquad
y_+=\frac{13}{10}.
\]

The exact-rational reduced certificate gives

\[
G(11/10)<-0.10644,
\]

\[
G(13/10)>0.05949.
\]

For \(u\ge20\),

\[
18/u^2\le0.045.
\]

Hence

\[
G_u(11/10)<0,
\qquad
G_u(13/10)>0.
\]

So a finite-\(u\) root exists in \((1.1,1.3)\).

## 4. Exact uniqueness

Let

\[
H_{\beta,u}(x)=\partial_x\mathcal E_{\beta,u}(x)
=\frac{u}{\sqrt{1+u^2x^2}}
-\beta^2u\frac{1+u^2x^2}{(1+u^2)^{3/2}}.
\tag{P6}
\]

It changes sign at the exact turning point \(x_{\beta,u}\).

For \(u\ge20\), throughout \(y\in[1.1,1.3]\),

\[
y<x_{\beta_2,u},
\]

so

\[
H_{\beta_2,u}(y)>0.
\]

Also

\[
0.684<x_c(y)<0.798<1=x_{1,u},
\]

hence

\[
H_{1,u}(x_c(y))>0.
\]

Differentiating (P4),

\[
\boxed{
G_u'(y)=H_{\beta_2,u}(y)+\beta_2H_{1,u}(x_c(y))>0.
}
\tag{P7}
\]

Thus the finite-\(u\) root is unique.

## 5. Orientation

For the first parent, \(x_1=29/32\) lies strictly above the exact \(\beta_1\)-turning point for \(u\ge20\), so

\[
H_{\beta_1,u}(x_1)<0.
\]

The catalyst root lies below its turning point and the child coordinate lies below one, hence

\[
H_{\beta_2,u}(y_u)>0,
\qquad
H_{1,u}(x_c(y_u))>0.
\]

Therefore the exact finite-\(u_*\) envelope model preserves

\[
\boxed{
\text{decaying parent}
+\text{ growing catalyst}
\xrightarrow{\text{difference}}
\text{ growing child}
}
\]

for every \(u_*\ge20\).

## 6. Scope

This theorem supersedes the previous finite-\(u\) theorem tied to the obsolete `17/12` chart-frequency interpretation. The remaining PDE obligations are phase admissibility under the source rounding conventions, localized curl interaction estimates, exact sum-sideband correction, and physical-scale inheritance to smaller \(q\).
