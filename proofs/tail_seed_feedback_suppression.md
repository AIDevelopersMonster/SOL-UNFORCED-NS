# Tail-seed feedback suppression for the v0.4 difference relay

**Status:** PROVED CONDITIONAL COEFFICIENT-LEVEL LEMMA. It assumes the generalized beta packet classes and designated-overlap source embedding. It does not remove the feedback exactly.

Primary source ingredients: Definition 6.5 / (6.29), Proposition 7.2 / (7.14), Lemma 7.7 / (7.39), and Proposition 9.1 of OpenAI, *Finite Time Blowup for Navier–Stokes*.

## 1. Tail relay collar

Choose the designated overlap so that each local pulse coordinate stays within \(O(S_*^{-1})\) of its resonance value over a bounded \(v\)-length collar. Derivatives of the corresponding auxiliary cutoff cost only powers of \(S_*\), not powers of \(\varepsilon^{-1}\).

At the v0.4 resonance,

\[
I_{25/16}(29/32)\approx-0.0732893717,
\]

\[
I_{9/16}(y_0)\approx-0.0408250388,
\]

\[
I_1(x_c)\approx-0.1141144105,
\]

and

\[
I_{25/16}(29/32)+I_{9/16}(y_0)=I_1(x_c).
\]

Thus both parents are in exponential tails and

\[
P_1P_2\asymp P_c
\]

throughout a bounded relay collar.

## 2. Seed and feedback scales

For two primary amplitudes of order \(W^{1/2}\), the cross-phase derivative in the deliberately overlapping **distinct-label** interaction costs \(k=O(\varepsilon^{-1/2})\). Hence the desired parent-parent source has leading size

\[
|S_{12}|\lesssim \varepsilon^{1/2}S_*^C P_1P_2.
\]

Once the child has been generated at tail size, the reciprocal parent-child interactions satisfy schematically

\[
|S_{1c}|\lesssim\varepsilon^{1/2}S_*^C P_1P_c,
\qquad
|S_{2c}|\lesssim\varepsilon^{1/2}S_*^C P_2P_c.
\]

Using \(P_c\asymp P_1P_2\),

\[
\boxed{
\frac{|S_{1c}|}{|S_{12}|}\lesssim P_1,
\qquad
\frac{|S_{2c}|}{|S_{12}|}\lesssim P_2.
}
\tag{F1}
\]

Since each parent tail is \(\le CS_*^Ce^{-cS_*}\),

\[
\boxed{
\frac{|S_{1c}|+|S_{2c}|}{|S_{12}|}
\le CS_*^Ce^{-c_{\rm fb}S_*}.
}
\tag{F2}
\]

Thus the triad is not algebraically one-way, but it is asymptotically one-way during the seeding event.

## 3. Curl remainder audit

The source Lemma 7.7 states exactly that if a prescribed transverse amplitude belongs to \(W^\alpha\), its curl remainder belongs to

\[
W^{\alpha+1/2-\kappa_s}.
\]

For a primary \(\alpha=1/2\) wave this is \(W^{1-\kappa_s}\). Therefore replacing one principal factor by a curl remainder gains \(1/2-\kappa_s\) in the epsilon exponent in a distinct-phase interaction. The source fixes \(\kappa_s=10^{-5}\) in Section 9, so this gain is strictly positive.

## 4. Unforced caveat

The source forced construction keeps Gaussian cutoff tails as a separate flat residual and ultimately includes them in the smooth external force. We cannot do that in an unforced construction.

Therefore (F2) proves only **suppression**, not exact elimination. The feedback and sum-sideband corrections must eventually be solved as part of the zero-force state rather than discarded as flat forcing.
