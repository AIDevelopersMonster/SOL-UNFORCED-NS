# Note 04 — β-relay geometry

Introduce an intermediate carrier scaling

\[
n_{\Phi,\beta}
\approx
\beta B_s(s e_r+K).
\]

At principal level, the intended effect is:

- direction of the shear-sensitive phase normal is unchanged;
- viscous damping scales like \(\beta^2\);
- two parent β-values can be selected so their sum matches the next physical band ratio.

## Rational relay choice

Choose

\[
r=\frac{17}{12}.
\]

Then set

\[
2^{(1+h)/2}=\frac{17}{12},
\]

so

\[
h
=
2\log_2\frac{17}{12}-1
\approx0.005000681058366707
<
\frac1{100}.
\]

Take

\[
\beta_1=\frac{93}{100},
\qquad
\beta_2=\frac{73}{150}.
\]

Then

\[
\beta_1+\beta_2=\frac{17}{12},
\]

and

\[
\beta_-=\beta_1-\beta_2=\frac{133}{300}.
\]

## Reduced large-\(u_*\) growth model

With \(s=u_*x\), the current reduced model is

\[
F_\beta(x)
=
\frac1x-\beta^2x^2.
\]

Use

\[
x_c=\frac{17}{32},
\quad
x_1\approx1.550891747,
\quad
x_2\approx-1.417243476.
\]

The phase relation is

\[
\beta_1x_1+\beta_2x_2
=
rx_c
\]

up to the recorded numerical residual.

The signs are

\[
F_{\beta_1}(x_1)<0,
\]

\[
F_{\beta_2}(|x_2|)>0,
\]

\[
F_1(x_c)>0.
\]

Interpretation:

\[
\text{decaying old packet}
+
\text{live catalyst}
\to
\text{growing child}.
\]

The difference branch in the present bookkeeping satisfies

\[
x_-\approx4.80914545044,
\qquad
F_{\beta_-}(x_-)<0,
\]

suggesting a **viscous triad filter**.

## Status

The arithmetic and reduced-model numerics are reproducible.

The PDE embedding is **not proved**.
