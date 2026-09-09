# Tail-seed feedback suppression

**Status:** PROVED CONDITIONAL COEFFICIENT-LEVEL LEMMA. The proof uses the published wave/envelope calculus and the translated-overlap geometry already recorded in this branch. It is conditional on the unresolved exact phase-locking of the parent sum branch to the child phase. It is not a proof of an unforced Navier–Stokes relay.

Primary source ingredients: OpenAI, *Finite Time Blowup for Navier–Stokes*, (6.11), Definition 6.5 / (6.29), Proposition 6.6, (7.16), (7.19), Lemma 7.7 / (7.39), Proposition 9.1, Lemma 9.2.

## 1. Why reciprocity looked dangerous

For three real Fourier packets with frequencies satisfying a triad relation, once the child exists it interacts back with its parents. Algebraically there is no reason for

\[
W_1\cdot\nabla W_c,
\qquad
W_2\cdot\nabla W_c
\]

to vanish merely because

\[
W_1\cdot\nabla W_2
\]

creates the child. Since a phase derivative costs

\[
k=O(\varepsilon^{-1/2}),
\]

three waves whose coefficient exponents are all \(1/2\) would naively generate cross-interactions at the same algebraic order \(W^{1/2}\).

The relay therefore cannot rely on algebraic one-wayness alone.

The missing separation is supplied by the **envelopes**.

## 2. Bounded-v relay collar

By (6.11),

\[
L_s=\frac{2r_0}{c_i}\asymp S_*.
\]

The translated-overlap lemma permits a common auxiliary overlap. We now choose the actual interaction collar \(\mathcal C_\ell\) to have **bounded local pulse length**:

\[
\boxed{
|v_j-v_j^0|\le L_0
}
\tag{F1}
\]

for a fixed \(L_0>0\) independent of the band.

In the auxiliary \(\eta\)-coordinate this has width

\[
O(c_iL_0)=O(r_0/S_*).
\]

Thus a cutoff adapted to this collar costs only powers of \(S_*\), which are already allowed in Definition 6.5. No new negative power of \(\varepsilon\) is introduced.

Because

\[
x=\frac12+\frac{v}{L_s},
\]

we have uniformly on \(\mathcal C_\ell\)

\[
\boxed{
x_j(v)=x_j^0+O(S_*^{-1}).}
\tag{F2}
\]

## 3. Tail hypothesis and envelope resonance

Assume the relay center satisfies, for some fixed \(a_1,a_2,a_c>0\),

\[
\log P_1(v_1^0)\le-a_1S_*+O(1),
\]

\[
\log P_2(v_2^0)\le-a_2S_*+O(1),
\]

\[
\log P_c(v_c^0)\le-a_cS_*+O(1),
\]

and the center is chosen so that

\[
\boxed{
a_c=a_1+a_2}
\tag{F3}
\]

at principal envelope level. Equivalently,

\[
P_1(v_1^0)P_2(v_2^0)\asymp P_c(v_c^0).
\]

Since the logarithmic derivatives of the envelopes are uniformly bounded on a fixed β-range, (F1)–(F2) imply

\[
\boxed{
P_1P_2\asymp P_c
}
\tag{F4}
\]

throughout the bounded-v collar, with constants independent of the band.

The Gaussian estimate (7.16), together with \(L_s\asymp S_*\), gives the exponential tail bounds whenever the selected normalized coordinates remain a fixed distance from their β-turning points:

\[
\boxed{
P_j\le C e^{-c_jS_*}
\qquad(j=1,2,c).
}
\tag{F5}
\]

## 4. Desired parent-parent source

Let the two parent amplitudes be curl-generated waves in the primary scale

\[
W_1,W_2\in W^{1/2}.
\]

Inside the deliberately permitted overlap, a cross-label phase derivative costs one factor

\[
k=O(\varepsilon^{-1/2}).
\]

Using Definition 6.5, the principal coefficient of

\[
S_{12}:=(W_1\cdot\nabla_*)W_2+(W_2\cdot\nabla_*)W_1
\]

therefore obeys

\[
\boxed{
|S_{12}|
\le
C\varepsilon^{1/2}S_*^C\zeta P_1P_2.
}
\tag{F6}
\]

Since \(0\le\zeta\le1\), the extra factor \(\zeta\) is stronger than the \(\sqrt\zeta\) required of a wave coefficient. If the sum phase is phase-locked to the child label, (F4) identifies the desired component as an admissible child source of order \(W^{1/2}\).

Although (F6) is algebraically order \(W^{1/2}\), it is exponentially small in the relay collar:

\[
|S_{12}|\le C\varepsilon^{1/2}S_*^C e^{-c_cS_*}.
\]

This is precisely the size needed for a tail seed: the later unstable homogeneous propagator may amplify it by the reciprocal envelope ratio.

## 5. Child remains tail-sized while overlap is active

Start the child coefficient from zero at the entrance of \(\mathcal C_\ell\). For the phase-locked desired component, Proposition 7.2 / the fundamental-matrix estimate (7.19) gives schematically

\[
|t_c(v)|
\le
C P_c(v)
\int_{v_-}^{v}
\frac{|f_c(w)|}{P_c(w)}\,dw.
\]

By (F1), the integration interval has length at most \(2L_0\), and by (F4)–(F6), \(|f_c|/P_c\) has only the usual algebraic \(\varepsilon^{1/2}S_*^C\) size. Hence

\[
\boxed{
|t_c(v)|
\le
C_{L_0}\varepsilon^{1/2}S_*^C P_c(v)
\qquad(v\in\mathcal C_\ell).
}
\tag{F7}
\]

After the parents leave the common collar, this tail-sized coefficient is free to evolve along the child homogeneous growing branch.

## 6. Parent-child feedback is exponentially smaller than the seed source

During the relay collar, the principal parent-child interactions have the bounds

\[
|S_{1c}|
\le
C\varepsilon^{1/2}S_*^C P_1P_c,
\]

\[
|S_{2c}|
\le
C\varepsilon^{1/2}S_*^C P_2P_c.
\]

Divide by the desired source scale in (F6). Using (F4),

\[
\boxed{
\frac{|S_{1c}|}{|S_{12}|}
\lesssim P_1,
\qquad
\frac{|S_{2c}|}{|S_{12}|}
\lesssim P_2.
}
\tag{F8}
\]

Therefore, by (F5),

\[
\boxed{
\frac{|S_{1c}|+|S_{2c}|}{|S_{12}|}
\le
CS_*^C e^{-c_{\rm fb}S_*}
}
\tag{F9}
\]

for some fixed \(c_{\rm fb}>0\).

Thus the triad is not algebraically one-way, but it is **asymptotically one-way during the seeding event**.

The same argument gives

\[
|S_{cc}|
\le C\varepsilon^{1/2}S_*^C P_c^2,
\]

which is even smaller.

## 7. Curl remainders do not spoil the separation

Lemma 7.7 gives, for a principal \(W^{1/2}\) coefficient,

\[
r\in W^{1-\kappa_s}.
\]

Replacing any principal factor in the above interactions by a curl remainder therefore gains at least

\[
\frac12-\kappa_s>0
\]

in the algebraic \(\varepsilon\)-exponent before using any tail gain. Hence all principal-remainder and remainder-remainder feedback terms are smaller than the corresponding principal feedback bounds.

## 8. Flatness of the feedback source

The source paper observes that, with

\[
S_*=\ell^2,
\qquad Q=2^{-\ell},
\]

an estimate of the form

\[
Q^{-M}S_*^C e^{-cS_*}
\]

vanishes faster than every power of \(q\asymp Q\) after taking any fixed physical derivative.

Combining this fact with (F9) gives:

### Tail-seed feedback suppression lemma

Under assumptions (F1)–(F4), and conditional on phase-locking the desired parent sum branch to the child phase, every parent-child feedback term generated while the child is being seeded is **flat to all algebraic orders at the singular scale**, whereas the desired parent-parent source remains an admissible \(W^{1/2}\) tail source for the unstable child inverse.

Symbolically,

\[
\boxed{
\text{parent} + \text{parent}
\longrightarrow
\text{child seed},
\qquad
\text{child feedback}
=
\text{flat relative leakage}.
}
\tag{F10}
\]

## 9. Current numerical witness

For the current reduced candidate

\[
\beta_1=\frac{55}{64},
\qquad
\beta_2=\frac{107}{192},
\]

\[
x_1=1.475,
\qquad
y_2\approx0.9498544185190722,
\qquad
x_c\approx0.5211050633031591,
\]

the corrected reduced primitives are

\[
I_{\beta_1}(x_1)\approx-0.1690294746,
\]

\[
I_{\beta_2}(y_2)\approx-0.1966095705,
\]

\[
I_1(x_c)\approx-0.3656390451,
\]

with

\[
I_{\beta_1}(x_1)+I_{\beta_2}(y_2)=I_1(x_c)
\]

to numerical precision. Thus each parent is itself in an exponential tail at the relay event, and the child tail exponent is their sum.

This is stronger than merely having a small child: both reciprocal feedback channels gain an additional exponential factor.

## 10. Important unforced caveat

In the forced OpenAI construction, exponentially flat residual terms may be retained in the final smooth force. Our target equation has **zero force**, so we cannot dispose of flat leakage by simply declaring it harmless.

The present lemma shows that feedback does not obstruct the leading relay mechanism. It does **not** eliminate the leakage exactly.

A future exact construction must either:

1. solve for all flat sidebands/feedback corrections by a convergent correction scheme, or
2. prove a separate exact flat-residual elimination theorem.

This distinction is essential for SOL-UNFORCED-NS.
