# Tail-seed feedback suppression for the corrected difference relay

**Status:** PROVED CONDITIONAL COEFFICIENT-LEVEL LEMMA. It is conditional on the localized PDE embedding and does not itself eliminate the feedback exactly.

## 1. Envelope resonance

At the current v0.4 reduced resonance,

\[
I_{25/16}(x_1)\approx-0.0732893717,
\]

\[
I_{9/16}(y_0)\approx-0.0408250388,
\]

\[
I_1(x_c)\approx-0.1141144105,
\]

and

\[
I_{25/16}(x_1)+I_{9/16}(y_0)=I_1(x_c).
\]

Thus if the common large envelope multiplier is \(\Lambda_*\asymp S_*\), then at the seed collar

\[
P_1P_2\asymp P_c,
\]

with all three factors exponentially small.

## 2. Desired seed versus feedback

For primary waves \(W_j\in W^{1/2}\), one phase derivative costs \(O(\varepsilon^{-1/2})\). The desired parent-parent difference source therefore has coefficient scale

\[
|S_{12}|\lesssim\varepsilon^{1/2}S_*^C P_1P_2.
\]

If the child is started from zero at the entrance of a bounded-\(v\) overlap collar, the linear child inverse gives

\[
|W_c|\lesssim\varepsilon^{1/2}S_*^C P_c
\]

while the collar is active.

The reciprocal parent-child interactions then satisfy schematically

\[
|S_{1c}|\lesssim\varepsilon^{1/2}S_*^C P_1P_c,
\]

\[
|S_{2c}|\lesssim\varepsilon^{1/2}S_*^C P_2P_c.
\]

Using \(P_c\asymp P_1P_2\),

\[
\frac{|S_{1c}|}{|S_{12}|}\lesssim P_1,
\qquad
\frac{|S_{2c}|}{|S_{12}|}\lesssim P_2.
\]

Hence

\[
\boxed{
\frac{|S_{1c}|+|S_{2c}|}{|S_{12}|}
\le S_*^C e^{-cS_*}
}
\]

for some fixed \(c>0\).

Thus the triad is not algebraically one-way, but it is asymptotically one-way during the seeding event.

## 3. Curl remainders

Replacing one principal factor by a curl remainder in \(W^{1-\kappa_s}\) gains the same positive algebraic epsilon exponent as in the source wave calculus, before using any exponential tail gain.

## 4. Unforced caveat

In the forced source construction, flat residuals can be absorbed into the final smooth forcing. SOL-UNFORCED-NS cannot do that. Therefore this lemma only proves **relative suppression**, not exact elimination.

Every sum-sideband, feedback, curl and cutoff residual must eventually be solved by a convergent correction mechanism so that the final equation has exactly zero external force.
