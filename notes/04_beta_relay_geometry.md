# Note 04 — β-relay geometry

Introduce an intermediate carrier scaling

\[
n_{\Phi,\beta}\approx \beta B_s(s e_r+K).
\]

At principal level:

- the direction of the shear-sensitive phase normal is unchanged;
- viscous damping scales like \(\beta^2\);
- two parent β-values can be selected so their sum matches the next physical band ratio.

## 1. Band ratio

Choose

\[
r=\frac{17}{12}.
\]

Then

\[
2^{(1+h)/2}=\frac{17}{12},
\qquad
h=2\log_2\frac{17}{12}-1
\approx0.005000681058366707<\frac1{100}.
\]

## 2. Correction to the v0.1 witness

The original bootstrap candidate

\[
\beta_1=0.93,
\qquad
\beta_2=\frac{73}{150}\approx0.4867
\]

is **deprecated** for the β-pulse stability program.

The reason is structural. In the large-\(u_*\) model, the β-dependent turning point is

\[
x_\beta=\beta^{-2/3}.
\]

The raw OpenAI pulse interval has

\[
\frac{|s(v)|}{u_*}\in\left[\frac12,\frac32\right].
\]

For \(\beta_2=73/150\),

\[
\beta_2^{-2/3}\approx1.6163>\frac32.
\]

Thus the second parent has no internal growth-to-decay turning point on the published raw pulse interval. The old row remains historically reproducible but should not be used as the preferred relay witness.

A sufficient asymptotic condition for an internal turning point is

\[
\boxed{\beta>\left(\frac23\right)^{3/2}\approx0.544331.}
\]

## 3. New rational relay pair

Use

\[
\boxed{
\beta_1=\frac56,
\qquad
\beta_2=\frac7{12}.
}
\]

Then

\[
\beta_1+\beta_2=\frac{17}{12}=r,
\qquad
\beta_-:=\beta_1-\beta_2=\frac14.
\]

Both parent turning points lie inside the raw interval:

\[
\beta_1^{-2/3}\approx1.1292432347,
\qquad
\beta_2^{-2/3}\approx1.4323708386.
\]

## 4. Reduced large-\(u_*\) model

Set

\[
F_\beta(x)=\frac1x-\beta^2x^2.
\]

For the reduced envelope bookkeeping define

\[
J_\beta(x)
=
\beta^{2/3}
\left[
\log\!\left(x\beta^{2/3}\right)
-
\frac{\beta^2}{3}
\left(x^3-\beta^{-2}\right)
\right].
\]

Choose the child coordinate

\[
x_c=\frac{17}{32}=0.53125.
\]

Solve the two reduced resonance equations

\[
\beta_1x_1-\beta_2y_2=rx_c,
\]

\[
J_{\beta_1}(x_1)+J_{\beta_2}(y_2)=J_1(x_c),
\]

with \(x_1,y_2\in[1/2,3/2]\). The unique root in the working bracket is

\[
\boxed{
x_1\approx1.4227047612075736,
\qquad
y_2\approx0.742256801725105.
}
\]

Equivalently the second signed parent coordinate is \(x_2=-y_2\).

The residuals are at numerical roundoff level.

## 5. Growth/decay signs

At this witness,

\[
F_{5/6}(x_1)\approx-0.7027307273<0,
\]

\[
F_{7/12}(y_2)\approx+1.1597682277>0,
\]

\[
F_1(x_c)\approx+1.6001263787>0.
\]

Thus the reduced mechanism has the desired orientation:

\[
\boxed{
\text{decaying old parent}
+
\text{growing catalyst}
\longrightarrow
\text{growing child}.
}
\]

For the formal difference branch,

\[
x_-=
\frac{\beta_1x_1+\beta_2y_2}{\beta_-}
\approx6.4742817414,
\]

and

\[
F_{1/4}(x_-)\approx-2.4653129661<0.
\]

This supports the **viscous triad filter** intuition, but note carefully that \(x_-\) lies far outside the standard raw pulse interval. Therefore this sign check is not yet a proof that the sideband belongs to an admissible correction class; the generated sideband requires a separate nonresonant/damped-source analysis.

## 6. Status

- Rational β-pair and turning-point admissibility: **DERIVED / NUMERICAL CHECKED**.
- Reduced resonance witness: **NUMERICAL**.
- β-pulse PDE embedding: **NOT YET PROVED**.
- Sideband disposal: **OPEN**.

Reproduce the witness with `experiments/relay_parameter_scan.py`.
