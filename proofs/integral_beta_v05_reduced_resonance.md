# v0.5 integral-beta relay: certified reduced resonance

**Status:** PROVED REDUCED LEMMA / NEW CANDIDATE ARCHITECTURE. This file introduces a cleaner same-physical-scale relay candidate designed to kill the first dangerous feedback mode at the principal carrier level. It does not yet replace v0.4 until finite-`u_*` persistence and localized PDE embedding are re-audited.

## 1. Motivation

The v0.4 choice

\[
\beta_1=\frac{25}{16},\qquad \beta_2=\frac9{16},\qquad \beta_1-\beta_2=1
\]

produces the desired unit-beta child, but the first child-minus-catalyst feedback mode has tangential coefficient

\[
1-\beta_2=\frac7{16},
\]

and was proved to be growing.

A natural way to remove this particular instability is to impose

\[
\boxed{\beta_2=1,\qquad \beta_1=2.}
\tag{V1}
\]

Then the desired difference still has unit beta,

\[
\beta_1-\beta_2=1,
\]

while the first child-minus-catalyst mode has tangential coefficient

\[
\boxed{1-\beta_2=0.}
\tag{V2}
\]

In the principal lattice rate formula its inviscid growing term therefore vanishes exactly; that mode is purely viscously damped whenever its radial coefficient is nonzero.

## 2. Reduced design

Take

\[
\boxed{x_1=\frac45.}
\tag{V3}
\]

For catalyst coordinate `y`, the exact principal difference relation gives

\[
\boxed{x_c(y)=2x_1-y=\frac85-y.}
\tag{V4}
\]

Use the corrected reduced envelope primitive

\[
I_\beta(x)=\log x+\frac23\log\beta-\frac{\beta^2x^3}{3}+\frac13.
\]

Define

\[
\boxed{G(y)=I_2(4/5)+I_1(y)-I_1(8/5-y).}
\tag{V5}
\]

## 3. Exact sign certificate

For rational `y`, write `x_c=8/5-y`. Multiplying (V5) by three yields

\[
3G(y)=\log Z(y)+P(y),
\]

where

\[
Z(y)=4\left(\frac{(4/5)y}{x_c}\right)^3\in\mathbb Q_{>0},
\]

\[
P(y)=1-4\left(\frac45\right)^3-y^3+x_c^3\in\mathbb Q.
\]

Using the rigorous atanh-series bounds

\[
\log Z=2\sum_{j=0}^{N}\frac{w^{2j+1}}{2j+1}+R_N,
\qquad w=\frac{Z-1}{Z+1},
\]

with

\[
0<R_N<\frac{2w^{2N+3}}{(2N+3)(1-w^2)},
\]

exact rational arithmetic certifies

\[
\boxed{G\left(\frac{89}{100}\right)<-1.08\times10^{-4}<0,}
\tag{V6}
\]

and

\[
\boxed{G\left(\frac{8901}{10000}\right)>1.53\times10^{-5}>0.}
\tag{V7}
\]

Therefore there exists a root

\[
\boxed{
\frac{89}{100}<y_0<\frac{8901}{10000}.
}
\tag{V8}
\]

Numerically,

\[
\boxed{y_0\approx0.8900876081470894,}
\]

and

\[
\boxed{x_{c,0}=\frac85-y_0\approx0.7099123918529107.}
\]

## 4. Uniqueness and transversality

Since `x_c'(y)=-1`,

\[
G'(y)=F_1(y)+F_1(x_c(y)),
\qquad
F_1(x)=\frac1x-x^2.
\]

On the certified interval,

\[
0<y<1,
\qquad
0<x_c<1,
\]

so both terms are strictly positive. Hence

\[
\boxed{G'(y)>0}
\tag{V9}
\]

throughout the bracket. The reduced root is unique and transverse.

## 5. Growth/decay orientation

At the fixed first-parent coordinate,

\[
F_2(4/5)=\frac54-4\frac{16}{25}
=-\frac{131}{100}<0.
\tag{V10}
\]

At the resonance root,

\[
0<y_0<1,
\qquad 0<x_{c,0}<1,
\]

so

\[
\boxed{F_1(y_0)>0,\qquad F_1(x_{c,0})>0.}
\tag{V11}
\]

Thus the reduced v0.5 relay has

\[
\boxed{
\text{decaying beta-2 parent}
+\text{ growing unit-beta catalyst}
\xrightarrow{\text{difference}}
\text{ growing unit-beta child}.
}
\tag{V12}
\]

Representative values are

\[
F_2(4/5)=-1.31,
\]

\[
F_1(y_0)\approx0.33123,
\qquad
F_1(x_{c,0})\approx0.90465.
\]

## 6. First feedback mode is killed at inviscid level

The dangerous v0.4 mode came from

\[
(1,-1)+(0,-1)=(1,-2).
\]

For v0.5 its tangential coefficient is

\[
T_{1,-2}=\beta_1-2\beta_2=2-2=0.
\]

Its radial coefficient is

\[
R_{1,-2}/u=2x_1-2y_0=2(x_1-y_0)\neq0.
\]

Therefore in the lattice net-rate formula

\[
\Gamma_{a,b}
=
\frac{|T_{a,b}|}{\sqrt{R_{a,b}^2+T_{a,b}^2}}
-
\frac{R_{a,b}^2+T_{a,b}^2}{(1+u^2)^{3/2}},
\]

the inviscid term is exactly zero and

\[
\boxed{
\Gamma_{1,-2}<0.
}
\tag{V13}
\]

Thus the first unstable feedback obstruction of v0.4 is removed by arithmetic design rather than by a compatibility solve.

## 7. Unwanted sum sideband

The sum branch has

\[
\beta_+=3
\]

and local coordinate

\[
x_+(y)=\frac{2x_1+y}{3}.
\]

At the reduced root,

\[
x_+\approx0.8300292027
\]

and

\[
\boxed{F_3(x_+)\approx-4.99576.}
\tag{V14}
\]

Hence the first unwanted sum sideband is even more strongly viscously damped than in v0.4.

## 8. Envelope budget

At the reduced root,

\[
I_2(4/5)\approx-0.1103787643,
\]

\[
I_1(y_0)\approx-0.0181611196,
\]

\[
I_1(x_{c,0})\approx-0.1285398838,
\]

and the first two exponents sum to the child exponent as required.

## 9. Significance and remaining audit

The v0.5 integral-beta design improves the local architecture in three ways:

1. exact desired difference relation `2-1=1`;
2. exact annihilation of the inviscid growth term for the first dangerous feedback mode `(1,-2)`;
3. stronger damping of the first unwanted sum branch `beta_+=3`.

It does **not** prove that every later low harmonic is stable. Higher correction generations still require lattice classification. The immediate next tasks are:

- prove finite-`u_*` persistence for the v0.5 resonance;
- recheck principal growing projection with source slopes `s=u_*x`;
- classify the first several nonlinear generations and determine whether the number of compatibility directions is reduced enough to make v0.5 preferable to v0.4.
