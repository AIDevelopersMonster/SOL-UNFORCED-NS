# Reduced v0.4 difference-relay resonance: rigorous interval certificate

**Status:** PROVED REDUCED LEMMA. This theorem is for the corrected large-\(u_*\) envelope model and the same-physical-scale difference relay. It is not the full localized Navier–Stokes relay lemma.

## 1. Reduced envelope

For \(\beta>0\), define

\[
I_\beta(x)=\log x+\frac23\log\beta-\frac{\beta^2x^3}{3}+\frac13,
\qquad
F_\beta(x)=I_\beta'(x)=\frac1x-\beta^2x^2.
\]

## 2. Corrected difference design

Set

\[
\beta_1=\frac{25}{16},\qquad
\beta_2=\frac9{16},\qquad
\beta_1-\beta_2=1,
\qquad
x_1=\frac{29}{32}.
\]

For \(y>0\), exact principal difference-phase closure gives the unit-beta child coordinate

\[
\boxed{x_c(y)=\beta_1x_1-\beta_2y.}
\tag{R1}
\]

Define

\[
\boxed{G(y)=I_{\beta_1}(x_1)+I_{\beta_2}(y)-I_1(x_c(y)).}
\tag{R2}
\]

## 3. Exact rational sign certificate

For rational \(y\), \(x_c(y)\) is rational and

\[
3G(y)=\log Z(y)+P(y),
\tag{R3}
\]

where

\[
Z(y)=\left(\frac{x_1y}{x_c(y)}\right)^3(\beta_1\beta_2)^2\in\mathbb Q_{>0},
\]

\[
P(y)=1-\beta_1^2x_1^3-\beta_2^2y^3+x_c(y)^3\in\mathbb Q.
\]

For \(Z>1\), put \(w=(Z-1)/(Z+1)\). Then

\[
\log Z=2\sum_{j=0}^{N}\frac{w^{2j+1}}{2j+1}+R_N,
\]

with

\[
0<R_N<\frac{2w^{2N+3}}{(2N+3)(1-w^2)}.
\tag{R4}
\]

All terms are rational. With \(N=60\), `experiments/reduced_resonance_certificate.py` certifies

\[
G\left(\frac{613}{500}\right)<-3.7653\times10^{-5}<0,
\]

\[
G\left(\frac{1227}{1000}\right)>7.7981\times10^{-4}>0.
\]

Hence a root exists in

\[
\boxed{\frac{613}{500}<y_0<\frac{1227}{1000}.}
\tag{R5}
\]

The same exact-arithmetic certificate also gives the wider endpoint margins

\[
\boxed{G(11/10)<-1/10,\qquad G(7/5)>13/100.}
\tag{R6}
\]

These margins are used in the finite-\(u_*\) persistence theorem.

## 4. Uniqueness and transversality

Since \(x_c'(y)=-\beta_2\),

\[
\boxed{G'(y)=F_{\beta_2}(y)+\beta_2F_1(x_c(y)).}
\tag{R7}
\]

On \([613/500,1227/1000]\),

\[
y<\beta_2^{-2/3},\qquad 0<x_c(y)<1.
\]

Therefore both terms in (R7) are positive and

\[
\boxed{G'(y)>0.}
\tag{R8}
\]

The root is unique and transverse.

Numerically,

\[
\boxed{y_0\approx1.2260460510205621,}
\]

\[
\boxed{x_{c,0}\approx0.7263647213009338.}
\]

## 5. Growth/decay orientation

At the root,

\[
F_{25/16}(29/32)\approx-0.9016519744<0,
\]

\[
F_{9/16}(y_0)\approx0.3400116795>0,
\]

\[
F_1(x_{c,0})\approx0.8491131364>0.
\]

Thus the corrected reduced model has

\[
\boxed{
\text{decaying parent}
+\text{ growing catalyst}
\xrightarrow{\text{difference harmonic}}
\text{ growing unit-beta child}.
}
\tag{R9}
\]

## 6. Unwanted sum branch

The same parent pair creates the sum harmonic with

\[
\beta_+=\beta_1+\beta_2=\frac{17}{8},
\]

and induced coordinate

\[
x_+(y)=\frac{\beta_1x_1+\beta_2y}{\beta_+}.
\]

At the root,

\[
x_+\approx0.9909018959,
\qquad
F_{17/8}(x_+)\approx-3.4246498904.
\]

So the non-designated sum branch lies on a strongly viscously decaying side of its envelope.

## 7. Scope

This replaces the obsolete `17/12` neighboring-chart certificate. The present theorem concerns a same-physical-scale difference harmonic. Physical-scale growth must later come from transport to smaller physical \(q\), not from changing dyadic chart labels.
