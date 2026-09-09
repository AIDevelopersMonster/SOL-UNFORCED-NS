# Note 07 — interior-turning relay candidate

## Why the previous β-pair was not good enough

The v0.1 pair matched the next-band ratio algebraically, but one parent had

\[
\beta_2^{-2/3}>\frac32,
\]

so its principal β-dependent growth/decay turning point lay outside the raw pulse interval

\[
\frac{|s(v)|}{u_*}\in\left[\frac12,\frac32\right].
\]

That makes it unsuitable as the preferred starting point for a rigorous β-pulse continuation of the published construction.

## Interior-turning threshold

The large-\(u_*\) turning point is

\[
x_\beta=\beta^{-2/3}.
\]

To place it below the raw endpoint \(3/2\), it is enough that

\[
\beta>\left(\frac23\right)^{3/2}\approx0.544331.
\]

This simple inequality is now part of the relay design constraints.

## New rational pair

The pair

\[
\boxed{\beta_1=\frac56,\qquad \beta_2=\frac7{12}}
\]

is convenient because

\[
\beta_1+\beta_2=\frac{17}{12}=r,
\]

while both β-values exceed the interior-turning threshold.

The associated turning locations are

\[
x_{\beta_1}\approx1.12924,
\qquad
x_{\beta_2}\approx1.43237.
\]

Both are inside the raw pulse interval.

## Reduced resonance witness

With

\[
x_c=\frac{17}{32},
\]

solve

\[
\beta_1x_1-\beta_2y_2=rx_c
\]

and

\[
J_{\beta_1}(x_1)+J_{\beta_2}(y_2)=J_1(x_c).
\]

The numerical root is

\[
\boxed{x_1\approx1.4227047612,\qquad y_2\approx0.7422568017.}
\]

The reduced net-growth signs are

\[
F_{\beta_1}(x_1)<0,
\qquad
F_{\beta_2}(y_2)>0,
\qquad
F_1(x_c)>0.
\]

So the candidate retains the desired orientation:

\[
\text{decaying old parent}
+
\text{live catalyst}
\to
\text{growing child}.
\]

## Important caveat: the difference branch

For \(\beta_-=1/4\), the formal reduced difference coordinate is

\[
x_-\approx6.47428,
\]

far outside the standard pulse interval.

The reduced quantity \(F_{1/4}(x_-)<0\) indicates strong damping, but this is **not** enough to declare the sideband controlled. The correct treatment is probably not to model the sideband as another standard pulse. Instead it should be estimated as an off-resonant, strongly diffusive forced response.

This changes the next proof target.

## Next target: Nonresonant Sideband Disposal Lemma

Given two designated β-parent packets whose sum branch matches the child carrier, estimate the difference-frequency response by Duhamel/heat damping and show that it belongs to an improved error class.

Schematic target:

\[
\|W_-\|_{X}
\le
C\frac{\|S_-\|_X}{\nu|\xi_-|^2-\Lambda_-}
\]

whenever the effective viscous gap satisfies

\[
\nu|\xi_-|^2-\Lambda_-\ge c\,\nu|\xi_-|^2>0.
\]

If this can be made uniform in the relay scaling, the unwanted branch need not be embedded as a pulse at all.

## Status

The v0.2 relay candidate is a better reduced witness than v0.1, but the PDE relay lemma is still unproved.
