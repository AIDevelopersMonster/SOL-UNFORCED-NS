# Finite-\(u_*\) persistence for the corrected v0.4 difference relay

**Status:** PROVED MODEL THEOREM. This upgrades the corrected reduced difference resonance to the exact beta-envelope model. It does not yet prove the full localized PDE relay.

## 1. Exact envelope

For \(\beta>0\), put

\[
a_\beta=\beta^{-2/3},
\qquad
x_{\beta,u}=\sqrt{a_\beta^2+\frac{a_\beta^2-1}{u^2}}.
\]

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

## 2. Uniform explicit approximation

### Lemma 2.1

For

\[
\frac9{16}\le\beta\le\frac{25}{16},
\qquad
\frac12\le x\le\frac32,
\qquad
u:=u\ge2,
\]

we have

\[
\boxed{|\mathcal E_{\beta,u}(x)-I_\beta(x)|\le\frac{10}{u^2}.}
\tag{P3}
\]

### Proof

Write \(a=a_\beta\) and \(d=1-a^{-2}\). The beta range implies

\[
\frac23<a<\frac32,
\qquad |d|\le\frac54.
\]

Also

\[
x_{\beta,u}=a\sqrt{1+d/u^2}.
\]

For \(u\ge2\), \(|d|/u^2\le5/16\), and direct bounds give

\[
\frac12<x_{\beta,u}<\frac{13}{8}.
\]

Set

\[
r(z)=\operatorname{arsinh}z-\log(2z).
\]

For \(z>0\),

\[
0\le r(z)\le\frac1{4z^2}.
\]

Hence the inverse-hyperbolic-sine part differs from \(\log(x/a)\) by at most

\[
\frac1{u^2}+\frac{10}{11u^2}<\frac2{u^2}.
\]

The linear viscous term is bounded by

\[
\beta^2u(1+u^2)^{-3/2}|x-x_{\beta,u}|<\frac3{u^2}.
\]

For the cubic term use

\[
c_u=(1+u^{-2})^{-3/2},
\qquad 0\le1-c_u\le\frac{3}{2u^2}.
\]

The error from replacing \(c_u\) by one is less than

\[
\frac{625}{256}\frac{27}{16u^2}<\frac{4.2}{u^2}.
\]

Finally, because \(\beta^2a^3=1\) and \(|d|/u^2\le5/16\), the turning-point displacement contributes less than

\[
\frac{35}{48u^2}<\frac{0.73}{u^2}.
\]

The four bounds sum to less than \(10/u^2\). ∎

## 3. Exact finite-u resonance

Fix

\[
\beta_1=25/16,
\quad\beta_2=9/16,
\quad x_1=29/32,
\]

and

\[
x_c(y)=\beta_1x_1-\beta_2y.
\]

Define

\[
G_u(y)=\mathcal E_{\beta_1,u}(x_1)+\mathcal E_{\beta_2,u}(y)-\mathcal E_{1,u}(x_c(y)).
\tag{P4}
\]

On \(y\in[11/10,7/5]\),

\[
\frac{1609}{2560}\le x_c(y)\le\frac{2041}{2560},
\]

so all arguments stay in \([1/2,3/2]\). Lemma 2.1 gives

\[
\boxed{|G_u(y)-G(y)|\le\frac{30}{u^2}.}
\tag{P5}
\]

The exact rational certificate proves

\[
G(11/10)<-1/10,
\qquad
G(7/5)>13/100.
\]

For \(u\ge20\), \(30/u^2\le3/40\), hence

\[
G_u(11/10)<-1/40<0,
\]

\[
G_u(7/5)>11/200>0.
\]

Therefore a root exists in \((11/10,7/5)\).

## 4. Exact uniqueness and orientation

Differentiate (P1):

\[
H_{\beta,u}(x):=\partial_x\mathcal E_{\beta,u}(x)
=\frac{u}{\sqrt{1+u^2x^2}}
-\beta^2u\frac{1+u^2x^2}{(1+u^2)^{3/2}}.
\tag{P6}
\]

Its unique positive zero is \(x_{\beta,u}\). Since \(\beta_2=9/16\),

\[
x_{\beta_2,u}>\beta_2^{-2/3}>7/5
\]

for every \(u\ge20\). Also \(x_c(y)<1=x_{1,u}\). Thus

\[
\boxed{G_u'(y)=H_{\beta_2,u}(y)+\beta_2H_{1,u}(x_c(y))>0.}
\tag{P7}
\]

The root \(y_u\) is unique.

For the first parent \(\beta_1>1\),

\[
x_{\beta_1,u}<\beta_1^{-2/3}<3/4<x_1,
\]

so

\[
H_{\beta_1,u}(x_1)<0.
\]

At the root,

\[
H_{\beta_2,u}(y_u)>0,
\qquad
H_{1,u}(x_c(y_u))>0.
\]

Hence for every \(u\ge20\),

\[
\boxed{
\text{decaying parent}
+\text{ growing catalyst}
\xrightarrow{\text{difference}}
\text{ growing child}.
}
\tag{P8}
\]

## 5. Convergence to the reduced root

On the wide bracket,

\[
G'(y)\ge F_{\beta_2}(7/5)+\beta_2F_1(2041/2560)>0.44.
\]

Let \(y_0\) be the unique reduced root. From (P5) and the mean value theorem,

\[
\boxed{|y_u-y_0|\le\frac{69}{u^2}.}
\tag{P9}
\]

## 6. Theorem

For the v0.4 parameters above and every

\[
\boxed{u_*\ge20,}
\]

the exact beta-envelope resonance equation has a unique solution

\[
\boxed{\frac{11}{10}<y_{u_*}<\frac75,}
\]

with a decaying first parent, growing catalyst, and growing unit-beta child. The exact root converges to the certified reduced root at rate \(O(u_*^{-2})\), quantitatively as in (P9).

Numerically, the roots are approximately

\[
y_{20}=1.2273024423,
\quad y_{50}=1.2262469526,
\quad y_{100}=1.2260962721,
\]

and tend to \(y_0\approx1.2260460510\).
