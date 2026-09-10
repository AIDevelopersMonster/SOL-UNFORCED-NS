# Finite-\(u_*\) persistence of the reduced β-relay resonance

**Status:** PROVED MODEL THEOREM. This theorem upgrades the certified reduced resonance to the exact finite-\(u_*\) β-envelope model used in this branch. It does **not** yet include angular rounding, exact parent-sum phase locking, curl localization, or exact unforced residual closure.

## 1. Exact and reduced envelopes

For \(0<\beta\le1\), put

\[
a_\beta:=\beta^{-2/3},
\qquad
x_{\beta,u}:=
\sqrt{a_\beta^2+\frac{a_\beta^2-1}{u^2}}.
\]

The exact normalized β-envelope primitive is

\[
\begin{aligned}
\mathcal E_{\beta,u}(x)
={}&\operatorname{arsinh}(ux)
-\operatorname{arsinh}(ux_{\beta,u})\\
&-\frac{\beta^2}{(1+u^2)^{3/2}}
\left[
 u(x-x_{\beta,u})
+\frac{u^3}{3}(x^3-x_{\beta,u}^3)
\right].
\end{aligned}
\tag{P1}
\]

The reduced primitive is

\[
I_\beta(x)
=
\log(x/a_\beta)
-
\frac{\beta^2}{3}(x^3-a_\beta^3).
\tag{P2}
\]

Equivalently,

\[
I_\beta(x)
=
\log x+\frac23\log\beta
-
\frac{\beta^2x^3}{3}+\frac13.
\]

## 2. Uniform explicit error bound

### Lemma 2.1

For

\[
\frac9{16}\le\beta\le1,
\qquad
\frac12\le x\le\frac32,
\qquad
u:=u\ge1,
\]

we have

\[
\boxed{
|\mathcal E_{\beta,u}(x)-I_\beta(x)|
\le\frac6{u^2}.
}
\tag{P3}
\]

### Proof

Let \(a=a_\beta\). Because \(\beta\ge9/16>(2/3)^{3/2}\),

\[
1\le a<\frac32.
\]

Also

\[
x_{\beta,u}^2=a^2+\frac{a^2-1}{u^2},
\]

so for \(u\ge1\),

\[
1\le x_{\beta,u}<2.
\]

Define

\[
r(z):=\operatorname{arsinh}z-\log(2z)
=\log\frac{1+\sqrt{1+z^{-2}}}{2}.
\]

For \(z>0\), concavity of the square root and \(\log(1+t)\le t\) give

\[
0\le r(z)\le\frac1{4z^2}.
\]

Writing

\[
\frac{x_{\beta,u}}a
=
\sqrt{1+\frac{d}{u^2}},
\qquad
0\le d:=1-a^{-2}<1,
\]

we obtain

\[
\left|
\operatorname{arsinh}(ux)-\operatorname{arsinh}(ux_{\beta,u})
-\log(x/a)
\right|
\le
\frac1{u^2}+\frac1{4u^2}+\frac1{2u^2}
=
\frac7{4u^2}.
\tag{P4}
\]

For the viscous part set

\[
c_u:=\frac{u^3}{(1+u^2)^{3/2}}
=(1+u^{-2})^{-3/2}.
\]

The linear term is bounded by

\[
\beta^2\frac{u}{(1+u^2)^{3/2}}|x-x_{\beta,u}|
\le\frac{3}{2u^2}.
\tag{P5}
\]

Moreover

\[
0\le1-c_u\le\frac{3}{2u^2},
\]

and, since \(x,a\in[1/2,3/2]\),

\[
|x^3-a^3|\le\frac{27}{8}.
\]

Therefore the error from replacing \(c_u\) by one is at most

\[
\frac{27}{16u^2}.
\tag{P6}
\]

Finally,

\[
x_{\beta,u}^3
=a^3\left(1+\frac d{u^2}\right)^{3/2},
\qquad
\beta^2a^3=1.
\]

For \(0\le t\le1\), the mean value theorem and \(\sqrt2<3/2\) give

\[
(1+t)^{3/2}-1\le\frac94t.
\]

Thus the turning-point displacement contributes at most

\[
\frac{3}{4u^2}.
\tag{P7}
\]

Adding (P4)–(P7),

\[
\frac74+\frac32+\frac{27}{16}+\frac34
=\frac{91}{16}<6,
\]

which proves (P3). ∎

## 3. Relay data

Fix

\[
\rho_0=\frac{17}{12},
\qquad
\beta_1=\frac{41}{48},
\qquad
\beta_2=\frac9{16},
\qquad
x_1=\frac{71}{48}.
\]

For \(y\in[9/10,97/100]\), define

\[
x_c(y)
=
\frac{\beta_1x_1-\beta_2y}{\rho_0}.
\tag{P8}
\]

At the two endpoints,

\[
x_c(9/10)=\frac{8723}{16320},
\qquad
x_c(97/100)=\frac{41347}{81600},
\]

so throughout the interval

\[
\frac12<x_c(y)<\frac35.
\tag{P9}
\]

Define the exact finite-\(u\) resonance function

\[
\boxed{
G_u(y)
=
\mathcal E_{\beta_1,u}(x_1)
+
\mathcal E_{\beta_2,u}(y)
-
\mathcal E_{1,u}(x_c(y)).
}
\tag{P10}
\]

Let \(G\) denote its reduced counterpart obtained by replacing \(\mathcal E\) with \(I\).

By Lemma 2.1,

\[
\boxed{
|G_u(y)-G(y)|\le\frac{18}{u^2}
}
\tag{P11}
\]

uniformly on the whole bracket.

## 4. Certified endpoint margins

The exact-rational logarithm certificate in `reduced_resonance_certificate.md` may be run at the wider rational bracket. It gives the strict bounds

\[
\boxed{
G(9/10)<-\frac{279}{5000}=-0.0558,
}
\tag{P12}
\]

and

\[
\boxed{
G(97/100)>\frac{91}{2000}=0.0455.
}
\tag{P13}
\]

For \(u\ge20\),

\[
\frac{18}{u^2}\le\frac9{200}=0.045.
\]

Hence

\[
G_u(9/10)
<
-\frac{279}{5000}+\frac9{200}
=-\frac{27}{2500}<0,
\tag{P14}
\]

while

\[
G_u(97/100)
>
\frac{91}{2000}-\frac9{200}
=\frac1{2000}>0.
\tag{P15}
\]

Therefore \(G_u\) has at least one zero in the bracket for every \(u\ge20\).

## 5. Exact uniqueness

Differentiate (P1). Define

\[
H_{\beta,u}(x)
:=
\partial_x\mathcal E_{\beta,u}(x)
=
\frac{u}{\sqrt{1+u^2x^2}}
-
\beta^2u\frac{1+u^2x^2}{(1+u^2)^{3/2}}.
\tag{P16}
\]

Its unique zero is exactly \(x_{\beta,u}\); it is positive below the turning point and negative above it.

Since \(\beta_2<1\),

\[
x_{\beta_2,u}>1>y
\]

throughout the bracket, so

\[
H_{\beta_2,u}(y)>0.
\]

For the child, \(x_{1,u}=1\) exactly and (P9) gives

\[
H_{1,u}(x_c(y))>0.
\]

Because

\[
x_c'(y)=-\frac{\beta_2}{\rho_0},
\]

we have

\[
\boxed{
G_u'(y)
=
H_{\beta_2,u}(y)
+
\frac{\beta_2}{\rho_0}H_{1,u}(x_c(y))
>0.
}
\tag{P17}
\]

Thus the finite-\(u\) root is unique.

## 6. Exact growth/decay orientation

Let \(y_u\) be the unique root.

For the first parent, \(a_{\beta_1}<6/5\). For \(u\ge1\),

\[
x_{\beta_1,u}^2
<2(6/5)^2-1
=\frac{47}{25}
<\left(\frac{71}{48}\right)^2,
\]

so

\[
\boxed{H_{\beta_1,u}(x_1)<0.}
\tag{P18}
\]

For the catalyst,

\[
y_u<1<x_{\beta_2,u},
\]

so

\[
\boxed{H_{\beta_2,u}(y_u)>0.}
\tag{P19}
\]

For the child, \(x_c(y_u)<1=x_{1,u}\), hence

\[
\boxed{H_{1,u}(x_c(y_u))>0.}
\tag{P20}
\]

Therefore for every \(u\ge20\) the **exact finite-\(u\) envelope model** has the required relay orientation:

\[
\boxed{
\text{decaying parent}
+
\text{growing catalyst}
\longrightarrow
\text{growing child}.
}
\tag{P21}
\]

## 7. Quantitative persistence toward the reduced root

On the bracket, the reduced derivative obeys

\[
F_{\beta_2}(y)
>
1-\frac{81}{256}
=
\frac{175}{256},
\]

and by (P9),

\[
F_1(x_c)
>
\frac53-\frac9{25}
=
\frac{98}{75}.
\]

Since

\[
\frac{\beta_2}{\rho_0}=\frac{27}{68},
\]

we obtain

\[
G'(y)
>
\frac{175}{256}
+
\frac{27}{68}\frac{98}{75}
=
\frac{130823}{108800}
>
\frac65.
\tag{P22}
\]

Let \(y_0\) be the unique reduced root. Using (P11), (P22), and the mean value theorem,

\[
\boxed{
|y_u-y_0|
\le\frac{15}{u^2}.
}
\tag{P23}
\]

Thus the exact finite-\(u\) relay root converges to the certified reduced root at the explicit rate \(O(u^{-2})\).

## 8. Theorem

### Finite-\(u_*\) Relay Persistence Theorem

For the rational parameters

\[
\rho_0=\frac{17}{12},
\quad
\beta_1=\frac{41}{48},
\quad
\beta_2=\frac9{16},
\quad
x_1=\frac{71}{48},
\]

and every

\[
\boxed{u_*\ge20,}
\]

the exact β-envelope resonance equation

\[
G_{u_*}(y)=0
\]

has a unique solution

\[
\boxed{
\frac9{10}<y_{u_*}<\frac{97}{100}.
}
\]

The corresponding child coordinate lies in \((1/2,3/5)\), the first parent is on its decaying branch, and the catalyst and child are on growing branches. Moreover, if \(y_0\) denotes the certified reduced root, then

\[
|y_{u_*}-y_0|\le15u_*^{-2}.
\]

## 9. Scope

This theorem closes the **finite-\(u_*\) envelope-persistence** question for the model currently used by SOL-UNFORCED-NS.

It does not yet establish an exact Navier–Stokes relay because the following remain open:

1. replace the reference band ratio \(\rho_0\) by the actual rounded carrier relation;
2. phase-lock the full parent sum phase, not only the reference normal;
3. prove the desired growing polarization lower bound for the localized curl waves;
4. solve every non-designated sideband and flat feedback correction exactly rather than absorbing them into an external force.
