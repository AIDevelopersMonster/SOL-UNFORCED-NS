# Reduced β-relay resonance: rigorous interval certificate

**Status:** PROVED REDUCED LEMMA. This is a theorem for the reduced large-\(u_*\) envelope model only. It is not yet the full localized Navier–Stokes relay lemma.

## 1. Reduced envelope

For \(\beta>0\), define

\[
I_\beta(x)
=
\log x+\frac23\log\beta
-
\frac{\beta^2x^3}{3}
+
\frac13,
\qquad x>0.
\]

Then

\[
I_\beta'(x)
=
F_\beta(x)
:=
\frac1x-\beta^2x^2.
\]

The turning point is

\[
x_\beta=\beta^{-2/3}.
\]

## 2. Rational design point

Set

\[
\rho_0=\frac{17}{12},
\qquad
\beta_1=\frac{41}{48},
\qquad
\beta_2=\frac9{16},
\]

so that

\[
\beta_1+\beta_2=\rho_0.
\]

Fix

\[
x_1=\frac{71}{48}.
\]

For \(y>0\), define the child coordinate by exact reference phase closure:

\[
\boxed{
x_c(y)
=
\frac{\beta_1x_1-\beta_2y}{\rho_0}.
}
\tag{R1}
\]

Define the envelope-resonance function

\[
\boxed{
G(y)
=
I_{\beta_1}(x_1)
+
I_{\beta_2}(y)
-
I_1(x_c(y)).
}
\tag{R2}
\]

The desired relay condition is \(G(y)=0\).

## 3. Rational logarithm reduction

For rational \(y\), the quantity \(x_c(y)\) is rational. Multiplying (R2) by three gives

\[
\boxed{
3G(y)=\log Z(y)+P(y),
}
\tag{R3}
\]

where

\[
Z(y)
=
\left(\frac{x_1y}{x_c(y)}\right)^3
(\beta_1\beta_2)^2
\in\mathbb Q_{>0},
\]

and

\[
P(y)
=
1-
\beta_1^2x_1^3
-
\beta_2^2y^3
+
x_c(y)^3
\in\mathbb Q.
\]

Thus the sign of \(G\) at rational test points can be certified using exact rational arithmetic plus a rigorous interval for \(\log Z\).

## 4. Logarithm certificate

For \(Z>1\), put

\[
w=\frac{Z-1}{Z+1}\in(0,1).
\]

The identity

\[
\log Z
=
2\sum_{j=0}^{\infty}
\frac{w^{2j+1}}{2j+1}
\]

has positive terms. Therefore, for every \(N\ge0\),

\[
2\sum_{j=0}^{N}
\frac{w^{2j+1}}{2j+1}
\le
\log Z
\le
2\sum_{j=0}^{N}
\frac{w^{2j+1}}{2j+1}
+
\frac{2w^{2N+3}}{(2N+3)(1-w^2)}.
\tag{R4}
\]

All quantities in (R4) are rational when \(Z\) is rational.

Using \(N=30\), the exact-arithmetic certificate implemented in `experiments/reduced_resonance_certificate.py` yields:

for

\[
y_-:=\frac{469}{500}=0.938,
\]

\[
-1.98590613905684\times10^{-4}
<
G(y_-)
<
-1.98590613901825\times10^{-4},
\]

hence

\[
\boxed{G(y_-)<0.}
\tag{R5}
\]

For

\[
y_+:=\frac{939}{1000}=0.939,
\]

\[
1.24595084809731\times10^{-3}
<
G(y_+)
<
1.24595084810189\times10^{-3},
\]

hence

\[
\boxed{G(y_+)>0.}
\tag{R6}
\]

By continuity, a root exists in \((y_-,y_+)\).

## 5. Uniqueness and transversality

Differentiating (R2) and using

\[
x_c'(y)=-\frac{\beta_2}{\rho_0},
\]

gives

\[
\boxed{
G'(y)
=
F_{\beta_2}(y)
+
\frac{\beta_2}{\rho_0}F_1(x_c(y)).
}
\tag{R7}
\]

On \([y_-,y_+]\),

\[
y<\beta_2^{-2/3},
\]

so

\[
F_{\beta_2}(y)>0.
\]

Also (R1) gives

\[
0<x_c(y)<1
\]

on this interval, hence

\[
F_1(x_c(y))>0.
\]

Therefore

\[
\boxed{G'(y)>0}
\tag{R8}
\]

throughout the bracket. The root is unique and transverse.

Numerically,

\[
\boxed{
y_0\approx0.938137436321536}
\]

and

\[
\boxed{
x_{c,0}\approx0.519354743421351.}
\]

At the root,

\[
G'(y_0)\approx1.44489709545.
\]

## 6. Growth/decay orientation

For the first parent,

\[
\beta_1^{-2/3}\approx1.10009942538
<
x_1=1.479166\ldots,
\]

so

\[
\boxed{F_{\beta_1}(x_1)<0.}
\]

For the catalyst root,

\[
y_0<\beta_2^{-2/3}\approx1.46752322172,
\]

hence

\[
\boxed{F_{\beta_2}(y_0)>0.}
\]

Finally \(x_{c,0}<1\), hence

\[
\boxed{F_1(x_{c,0})>0.}
\]

Thus the reduced resonance has the required orientation:

\[
\boxed{
\text{decaying parent}
+
\text{growing catalyst}
\longrightarrow
\text{growing child}.
}
\tag{R9}
\]

## 7. Consequence

The reduced β-relay resonance is no longer merely a floating-point observation. There is a unique root in the explicit rational interval

\[
\boxed{
\frac{469}{500}<y_0<\frac{939}{1000}
}
\]

with a strictly positive derivative and the required growth/decay signs.

The remaining work is to transport this certified reduced root to:

1. the exact finite-\(u_*\) β-envelope;
2. the actual rounded carrier ratios \(k_{\ell+1}/k_\ell\);
3. the full localized curl-generated PDE packet system.
