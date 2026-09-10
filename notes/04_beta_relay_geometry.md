# Note 04 — v0.4 same-scale beta difference relay

## 1. Historical correction

The v0.1–v0.3 relay witnesses were tied, directly or indirectly, to the now-retracted interpretation that neighboring dyadic charts produce the physical ratio \(17/12\). Their algebra remains useful as history, but they are **not current physical relay candidates**.

The current design works at one physical \(q\) and uses an exact difference harmonic.

## 2. Current rational beta pair

Choose

\[
\boxed{
\beta_1=\frac{25}{16},
\qquad
\beta_2=\frac9{16},
\qquad
\beta_1-\beta_2=1.
}
\]

The desired difference branch is therefore a unit-beta child. The unwanted sum branch has

\[
\boxed{\beta_+=\frac{17}{8}.}
\]

Fix the decaying-parent coordinate

\[
\boxed{x_1=\frac{29}{32}=0.90625.}
\]

For the catalyst coordinate \(y\), set

\[
\boxed{x_c(y)=\beta_1x_1-\beta_2y.}
\]

Use the corrected reduced envelope primitive

\[
I_\beta(x)=\log x+\frac23\log\beta-\frac{\beta^2x^3}{3}+\frac13,
\qquad
F_\beta=I_\beta'=\frac1x-\beta^2x^2.
\]

## 3. Certified reduced resonance

Define

\[
G(y)=I_{\beta_1}(x_1)+I_{\beta_2}(y)-I_1(x_c(y)).
\]

The exact-rational certificate proves

\[
G(613/500)<0<G(1227/1000),
\]

and \(G'>0\) on the bracket. Hence there is a unique root

\[
\boxed{1.226<y_0<1.227.}
\]

Numerically,

\[
y_0\approx1.2260460510205621,
\qquad
x_{c,0}\approx0.7263647213009338.
\]

At the root,

\[
F_{25/16}(x_1)\approx-0.901652<0,
\]

\[
F_{9/16}(y_0)\approx+0.340012>0,
\]

\[
F_1(x_{c,0})\approx+0.849113>0.
\]

Thus

\[
\boxed{
\text{decaying parent}
+\text{ growing catalyst}
\xrightarrow{\text{difference}}
\text{ growing child}.
}
\]

The reduced envelope budget is

\[
I_{25/16}(x_1)\approx-0.07328937,
\quad
I_{9/16}(y_0)\approx-0.04082504,
\]

\[
I_1(x_{c,0})\approx-0.11411441,
\]

with the first two summing to the child exponent.

## 4. Unwanted sum sideband

Its induced local coordinate is

\[
x_+(y)=\frac{\beta_1x_1+\beta_2y}{\beta_+}.
\]

At the root,

\[
x_+\approx0.9909018959,
\qquad
\beta_+^{-2/3}\approx0.6050074331,
\]

and

\[
\boxed{F_{17/8}(x_+)\approx-3.42465.}
\]

So the non-designated sum harmonic lies deep in a viscously decaying region. This is a much cleaner sideband geometry than the obsolete v0.3 design, but exact zero-force disposal remains open.

## 5. Geometric advantage

The three desired local coordinates \(x_1\), \(y_0\), \(x_{c,0}\) all lie well inside \((1/2,3/2)\). The smallest endpoint margin is about \(0.226\), giving substantially more room for an overlap collar than the earlier witnesses.

## 6. Scope

This is a **same-physical-scale relay**. It does not by itself prove a cascade to larger physical frequency. The next-scale mechanism must use transport to smaller physical \(q\), where the intrinsic carrier grows as \(q^{-(1+h)/2}\).
