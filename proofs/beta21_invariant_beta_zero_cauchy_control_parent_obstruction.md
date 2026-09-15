# Invariant beta-zero Cauchy controls: two-layer feasibility and parent obstruction

**Status:** PROVED PRINCIPAL ACTION/CAUCHY-CONTROL OBSTRUCTION AT THE CORRECTED `u=2.5` WORKING POINT, SUBJECT ONLY TO INTERVAL CERTIFICATION OF THE PRINTED NUMERICAL MARGINS. This note replaces future-time active controls by genuine physical Cauchy coordinates on the reset-invariant beta-zero line and determines exactly how far that repair can go.

At the corrected one-step beta-(2,1) geometry, a preload of the invariant character

\[
M=P-2C,
\qquad \beta(M)=0,
\qquad R(M)=M,
\]

can action-match the spent-catalyst layer. A second invariant preload `2M` can then action-match the resulting `H=C_2` layer. However the remaining renewed-parent character

\[
P_1=P+2M
\]

cannot be cancelled by **any** binary route

\[
kM+Q_k\to P_1,
\qquad k\ge1,
\qquad Q_k=P_1-kM,
\qquad \beta(Q_k)=2,
\]

if both incoming physical Cauchy actions are at most the natural-envelope maximum `0`.

Thus an arbitrarily large bank of positive beta-zero harmonics `M,2M,3M,...`, each paired with one beta-two homogeneous preload, does not repair the parent layer of the current reset geometry.

The companion reproducibility script is

`experiments/beta21_invariant_beta_zero_cauchy_control_audit.py`.

## 1. Working geometry

Freeze

\[
u=2.5,
\qquad
\delta=0.1375,
\]

\[
x=0.7779445026067248271\ldots,
\qquad
T=2\delta=0.275.
\]

The corrected first-relay resonance is

\[
\mathcal E_2(x)+\mathcal E_1(x+\delta)
=\mathcal E_1(x-\delta).
\tag{BZ1}
\]

The reset shear is

\[
R(K)=K+\beta(K)M,
\qquad M=P-2C.
\tag{BZ2}
\]

In particular

\[
R(M)=M,
\qquad
R(kM)=kM.
\tag{BZ3}
\]

Hence every `kM` amplitude is a genuine reset-invariant Fourier Cauchy coordinate rather than a future temporal control.

The principal beta-zero normalized decay rate of `M` is

\[
\boxed{
\lambda_M
=-\frac{(2u\delta)^2}{(1+u^2)^{3/2}}
=-0.02421243094765439\ldots<0.
}
\tag{BZ4}
\]

and `kM` has rate `k^2 lambda_M`.

## 2. First layer: spent catalyst can be action-matched by `M`

Use the physical difference edge

\[
D-M\to C.
\tag{BZ5}
\]

Let `a_1=A_M(0)` be the incoming Cauchy action of `M`. With zero incoming beta-zero action, define the reset-face source functional

\[
\mathfrak C_0(t)
=
\mathcal E_1(x-\delta+t)
+\lambda_M t
+I_1(x+3\delta)-I_1(x+\delta+t).
\tag{BZ6}
\]

Here `I_1` is the unnormalised primitive underlying `mathcal E_1`; the last difference is the homogeneous propagation of the generated beta-one child to the reset face.

The diagnostic maximization gives

\[
\max_{0\le t\le T}\mathfrak C_0(t)
=-0.01521503159\ldots,
\]

with the maximum at the reset endpoint to numerical precision.

The spent old catalyst has reset action

\[
A_C^{old}(T)
=\mathcal E_1(x+3\delta)
=-0.04406251620\ldots.
\]

Therefore the required physical incoming beta-zero action is

\[
\boxed{
a_1
=A_C^{old}(T)-\max\mathfrak C_0
=-0.02884748460\ldots<0.
}
\tag{BZ7}

This is admissible: no positive-above-envelope incoming action is required.

Thus the first Cauchy-control layer is **feasible** at action level.

## 3. Second layer: the induced `H=C_2` mode can be matched by `2M`

The `M` preload necessarily participates in

\[
M+D\to H,
\qquad H=2D-C=C_2.
\tag{BZ8}
\]

The `H` reduced slope first enters the audited positive source window at

\[
\boxed{
t_H
=\frac12-(x-3\delta)
=0.13455549739\ldots.
}
\tag{BZ9}
\]

Using (BZ7), the maximum reset action of this route on `[t_H,T]` is

\[
\boxed{
A_H^{bad}
=0.05467569338\ldots.
}
\tag{BZ10}
\]

Now introduce a second genuine invariant Cauchy coordinate `2M`. The competing route

\[
2M+C\to H
\tag{BZ11}
\]

has beta-zero decay `4 lambda_M`. With zero `2M` input action, its maximum reset action is

\[
0.13121585880\ldots.
\]

Thus exact action matching requires

\[
\boxed{
A_{2M}(0)
=0.05467569338\ldots-0.13121585880\ldots
=-0.07654016542\ldots<0.
}
\tag{BZ12}
\]

Again the required incoming action lies below the natural-envelope ceiling.

Hence the first **two** contamination layers admit honest physical Cauchy cancellation at principal action level.

## 4. Remaining parent layer

After the first two matches, the rooted route

\[
M+D\to H,
\qquad
H+D\to P_1,
\qquad
P_1=P+2M,
\tag{BZ13}
\]

leaves a beta-two parent layer. A conservative same-time action bound, restricted to times at which the `H` intermediate lies in its audited source window, gives

\[
\boxed{
A_{P_1}^{bad}
=-0.05261912928\ldots.
}
\tag{BZ14}
\]

The exact value printed here is diagnostic; what matters for the theorem below is the fixed positive gap to every admissible binary invariant-harmonic cancellation route.

## 5. Complete binary invariant-harmonic family

For any integer `k>=1`, write

\[
\boxed{
P_1=kM+Q_k,
\qquad
Q_k=P_1-kM.
}
\tag{BZ15}
\]

Since `beta(M)=0` and `beta(P_1)=2`,

\[
\beta(Q_k)=2.
\]

The reduced slope of the target parent during the cell is

\[
z_{P_1}(t)=x-2\delta+t,
\]

while

\[
z_{Q_k}(t)=z_{P_1}(t)+k\delta.
\tag{BZ16}
\]

Assume the incoming Cauchy actions obey the natural-envelope ceiling

\[
A_{kM}(0)\le0,
\qquad
A_{Q_k}(0)\le0.
\tag{BZ17}
\]

Because the quadratic source action is monotone in the two input actions, the largest possible reset action in this class occurs at equality in (BZ17).

For zero incoming actions define

\[
\begin{aligned}
F_k(t)
={}&k^2\lambda_M t
+I_2(z_{Q_k}(t))-I_2(z_{Q_k}(0))\\
&+I_2(x)-I_2(z_{P_1}(t)).
\end{aligned}
\tag{BZ18}
\]

This is exactly the reset action of the source event

\[
kM+Q_k\to P_1.
\]

## 6. Exact monotonicity

Let

\[
\Gamma_2(z)
=\frac1{\sqrt{1+u^2z^2}}
-4\frac{1+u^2z^2}{(1+u^2)^{3/2}}.
\tag{BZ19}
\]

Up to the common positive clock normalization used in the primitive derivative,

\[
I_2'(z)=u\Gamma_2(z).
\]

Differentiating (BZ18) gives

\[
\boxed{
F_k'(t)
=k^2\lambda_M
+u\Bigl[\Gamma_2(z_{P_1}(t)+k\delta)
-\Gamma_2(z_{P_1}(t))\Bigr].
}
\tag{BZ20}

For `z>0`,

\[
\Gamma_2'(z)
=-\frac{u^2z}{(1+u^2z^2)^{3/2}}
-\frac{8u^2z}{(1+u^2)^{3/2}}
<0.
\tag{BZ21}
\]

Therefore for every `k>=1`, wherever both beta-two slopes lie in the audited positive source window,

\[
\Gamma_2(z+k\delta)-\Gamma_2(z)<0.
\]

Together with `lambda_M<0`, this yields

\[
\boxed{F_k'(t)<0.}
\tag{BZ22}
\]

Thus every member of the entire infinite family (BZ15) has its maximal reset action at the earliest admissible time. Whenever the route is already source-admissible at `t=0`,

\[
\boxed{
\max F_k
=F_k(0)
=I_2(x)-I_2(x-2\delta),
}
\tag{BZ23}
\]

which is independent of `k`.

For the corrected working point,

\[
\boxed{
F_k(0)
=-0.14103738182\ldots.
}
\tag{BZ24}

The companion script samples (BZ20) for `k=1,...,6` and finds a uniform negative sign, consistent with the exact monotonicity proof.

## 7. Fixed parent obstruction

Comparing (BZ14) and (BZ24),

\[
\boxed{
A_{P_1}^{bad}-\max F_k
=0.08841825254\ldots>0.
}
\tag{BZ25}

for every `k>=1` whose binary route is source-admissible from the entrance section.

Allowing strictly negative incoming actions only decreases `F_k`, so it cannot close the gap.

Hence:

> **Invariant beta-zero binary parent obstruction.** At the corrected `u=2.5`, `delta=0.1375` one-step reset geometry, no binary physical Cauchy cancellation route `kM+Q_k -> P_1` with `k>=1`, `beta(Q_k)=2`, and nonpositive incoming natural actions can cancel the remaining parent layer after the feasible `M` and `2M` first-two-layer matches.

This rules out not merely the specific routes `2M+P` and `M+2D`, but the complete positive beta-zero harmonic/beta-two binary family.

## 8. Scope and the unresolved negative-harmonic caveat

The theorem is deliberately restricted to `k>=1` and to beta-two preloads that are source-admissible from the entrance section.

For formally negative `k`, the beta-two partner `Q_k` can begin below the positive pulse window and enter it later. Such a calculation may give a larger formal reset action. It is **not** automatically a valid Cauchy control: one must first prove that the corresponding homogeneous physical packet is genuinely present on the earlier Cauchy slice rather than being zero there by the actual source/clock cutoff and effectively seeded in the future.

The source formalization `InitialHarmonicContinuation.lean` proves zero jets off the actual clock-window core for attached initial harmonic coefficients. Resolving the precise relation between that clock core and the reduced-slope window for these negative-`k` candidates is therefore the next source-specific obligation.

## 9. Consequence

The current hierarchy is now:

1. future temporal active controls — not autonomous Cauchy controls;
2. delayed separated spatial lobes — cannot create order-one late collisions under common material transport;
3. a single invariant `M` memory — creates a fatal parent shortcut;
4. the enlarged invariant bank `(M,2M)` — **does** action-match the first two layers;
5. every positive `kM + Q_k` binary parent control — blocked by the fixed gap (BZ25).

Thus the first genuinely promising physical-Fourier repair is narrower than before: either exploit a source-admissible negative-harmonic/late-entry channel, change the reset geometry, or move to an asymptotic vanishing-shear regime in which the parent mismatch itself vanishes with the level.

No autonomous reset cell or unforced blowup theorem is claimed here.
