# Reduced beta-difference relay resonance: rigorous interval certificate

**Status:** PROVED REDUCED LEMMA for the corrected v0.4 same-physical-scale design. This is not yet the full localized Navier–Stokes relay lemma.

## 1. Reduced envelope

For \(\beta>0\), define

\[
I_\beta(x)
=\log x+\frac23\log\beta-\frac{\beta^2x^3}{3}+\frac13,
\qquad
F_\beta(x)=I_\beta'(x)=\frac1x-\beta^2x^2.
\]

## 2. Corrected difference design

Set

\[
\boxed{
\beta_1=\frac{25}{16},
\qquad
\beta_2=\frac9{16},
\qquad
\beta_1-\beta_2=1,
}
\]

and fix

\[
\boxed{x_1=\frac{29}{32}.}
\]

For the desired difference harmonic, define

\[
\boxed{x_c(y)=\beta_1x_1-\beta_2y.}
\tag{R1}
\]

The reduced envelope-resonance function is

\[
\boxed{
G(y)=I_{\beta_1}(x_1)+I_{\beta_2}(y)-I_1(x_c(y)).
}
\tag{R2}
\]

## 3. Exact rational sign certificate

For rational \(y\), \(x_c(y)\) is rational and

\[
3G(y)=\log Z(y)+P(y),
\]

where

\[
Z(y)=\left(\frac{x_1y}{x_c(y)}\right)^3(\beta_1\beta_2)^2\in\mathbb Q_{>0},
\]

\[
P(y)=1-\beta_1^2x_1^3-\beta_2^2y^3+x_c(y)^3\in\mathbb Q.
\]

Using

\[
\log Z=2\sum_{j=0}^{\infty}\frac{w^{2j+1}}{2j+1},
\qquad
w=\frac{Z-1}{Z+1},
\]

with the explicit positive-tail bound recorded in `experiments/reduced_resonance_certificate.py`, one obtains

\[
\boxed{
G\!\left(\frac{613}{500}\right)<0
}
\]

with certified value near

\[
-3.76534608122\times10^{-5},
\]

and

\[
\boxed{
G\!\left(\frac{1227}{1000}\right)>0
}
\]

with certified value near

\[
7.79811209016\times10^{-4}.
\]

Hence a root exists in

\[
\boxed{
1.226<y_0<1.227.
}
\tag{R3}
\]

## 4. Uniqueness and transversality

Since

\[
x_c'(y)=-\beta_2,
\]

we have

\[
\boxed{
G'(y)=F_{\beta_2}(y)+\beta_2F_1(x_c(y)).
}
\tag{R4}
\]

On the wider interval \([1.1,1.3]\),

\[
y<\beta_2^{-2/3},
\]

so \(F_{\beta_2}(y)>0\). Also

\[
0.684<x_c(y)<0.798<1,
\]

so \(F_1(x_c(y))>0\). Therefore

\[
\boxed{G'(y)>0}
\]

throughout that interval. The root is unique and transverse.

Numerically,

\[
\boxed{
y_0\approx1.2260460510205621,}
\]

\[
\boxed{x_{c,0}\approx0.7263647213009338,}
\]

and

\[
G'(y_0)\approx0.8176378187.
\]

## 5. Growth/decay orientation

The turning points are

\[
\beta_1^{-2/3}\approx0.7426542134,
\qquad
\beta_2^{-2/3}\approx1.4675232217.
\]

Since

\[
x_1=0.90625>\beta_1^{-2/3},
\]

the first parent is decaying. Since

\[
y_0<\beta_2^{-2/3},
\]

the catalyst is growing. Since

\[
x_{c,0}<1,
\]

the unit-beta child is growing.

Numerically,

\[
F_{25/16}(x_1)\approx-0.901652,
\]

\[
F_{9/16}(y_0)\approx+0.340012,
\]

\[
F_1(x_{c,0})\approx+0.849113.
\]

Thus

\[
\boxed{
\text{decaying parent}
+\text{ growing catalyst}
\xrightarrow{\text{difference harmonic}}
\text{ growing child}.
}
\]

## 6. Unwanted sum sideband

The same real parent pair also produces a sum harmonic with

\[
\beta_+=\beta_1+\beta_2=\frac{17}{8}.
\]

Its induced reduced coordinate is

\[
x_+(y)=\frac{\beta_1x_1+\beta_2y}{\beta_+}.
\]

At the resonance root,

\[
x_+\approx0.9909018958583841,
\]

while

\[
\beta_+^{-2/3}\approx0.6050074331.
\]

Therefore the sum sideband is on the decaying branch, with

\[
\boxed{F_{17/8}(x_+)\approx-3.42465.}
\]

This is a strong viscous filter, but exact zero-force disposal of that sideband is still an open PDE obligation.

## 7. Scope

This certificate replaces the obsolete `17/12` cross-band resonance. It establishes only a **same-physical-scale difference-harmonic relay resonance**. The physical cascade to smaller \(q\) is a separate inheritance problem.
