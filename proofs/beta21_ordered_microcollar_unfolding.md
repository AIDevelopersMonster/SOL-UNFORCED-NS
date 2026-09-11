# Causal ordered-microcollar unfolding of the beta-(2,1) reset supercell

**Status:** COMPUTER-ASSISTED REDUCED THEOREM / CAUSAL UNFOLDING PASSES. The simultaneous late reset collision point from `beta21_clock_reset_microcascade_candidate.md` persists when the four late generations are separated into strictly ordered micro-collars

\[
t_1<t_2<t_3<t_4<T.
\]

At reduced-envelope level the exact first relay resonance, exact final parent-action renewal, and stationarity with respect to the common late shift can all be retained simultaneously. The principal polarization margins remain nonzero under this unfolding. This is still not the full localized Navier--Stokes supercell: the next obligations are the promoted/non-designated action filter, finite-`u_*` exact-source persistence, and the phase-adapted zero-residual solve.

## 1. Ordered timing ansatz

Let

\[
t_1=s,
\qquad
t_2=s+\eta,
\qquad
t_3=s+2\eta,
\qquad
t_4=s+3\eta,
\tag{OC1}
\]

with

\[
\eta>0,
\qquad
T=2\delta.
\tag{OC2}
\]

The late causal chain is

\[
C+D\to P \quad\text{at }t_1,
\]

\[
P+D\to E \quad\text{at }t_2,
\]

\[
E-C\to Q \quad\text{at }t_3,
\]

\[
Q-C\to H \quad\text{at }t_4,
\]

\[
H+D\to P_{\rm new} \quad\text{at }T.
\tag{OC3}
\]

The strict causal condition is

\[
\boxed{
t_1<t_2<t_3<t_4<T.}
\tag{OC4}
\]

## 2. Exact action transport between collars

Keep the reduced source primitive

\[
I_\beta(x)
=\log(x\beta^{2/3})
-\frac{\beta^2}{3}(x^3-\beta^{-2}).
\]

Let

\[
C(t)=I_1(x+\delta+t),
\qquad
D(t)=I_1(x-\delta+t).
\tag{OC5}
\]

At `t_1`, the first late feedback gives

\[
A_P(t_1)=C(t_1)+D(t_1).
\tag{OC6}
\]

Propagate `P` homogeneously to `t_2`:

\[
A_P(t_2)=A_P(t_1)
+I_2(x+t_2)-I_2(x+t_1).
\tag{OC7}
\]

Generate `E=P+D` at `t_2`:

\[
A_E(t_2)=A_P(t_2)+D(t_2).
\tag{OC8}
\]

Propagate `E` to `t_3`:

\[
A_E(t_3)=A_E(t_2)
+I_3(x-\delta/3+t_3)-I_3(x-\delta/3+t_2).
\tag{OC9}
\]

Generate `Q=E-C` at `t_3`:

\[
A_Q(t_3)=A_E(t_3)+C(t_3).
\tag{OC10}
\]

Propagate `Q` to `t_4`:

\[
A_Q(t_4)=A_Q(t_3)
+I_2(x-\delta+t_4)-I_2(x-\delta+t_3).
\tag{OC11}
\]

Generate `H=Q-C` at `t_4`:

\[
A_H(t_4)=A_Q(t_4)+C(t_4).
\tag{OC12}
\]

Propagate `H` to the reset face `T=2\delta`:

\[
A_H(T)=A_H(t_4)
+I_1(x-\delta)-I_1(x-3\delta+t_4).
\tag{OC13}
\]

Finally

\[
\boxed{
A_{P_{\rm new}}(T)=A_H(T)+I_1(x+\delta).
}
\tag{OC14}
\]

Exact action reset is

\[
\boxed{A_{P_{\rm new}}(T)=I_2(x).}
\tag{OC15}
\]

At `eta=0`, formulas (OC6)--(OC15) collapse exactly to the simultaneous-collision ledger in the previous note.

## 3. Three-equation ordered system

For fixed small `eta>=0`, solve in `(x,delta,s)` the system

\[
\boxed{
F_0(x,\delta)
:=I_2(x)+I_1(x+\delta)-I_1(x-\delta)=0,
}
\tag{OC16}
\]

\[
\boxed{
F_1(x,\delta,s;\eta)
:=A_{P_{\rm new}}(T)-I_2(x)=0,
}
\tag{OC17}
\]

and the stationarity condition

\[
\boxed{
F_2(x,\delta,s;\eta)
:=\partial_s F_1(x,\delta,s;\eta)=0.
}
\tag{OC18}
\]

At `eta=0` the known transverse solution is

\[
(x_0,\delta_0,s_0)
\approx
(0.785985556929522,
0.0706996730666389,
0.141194608887663).
\]

The Jacobian determinant there is about `65.533`, so the implicit-function theorem predicts a unique local ordered branch for sufficiently small `eta`.

## 4. High-precision ordered solutions

The companion script `experiments/beta21_ordered_microcollar_unfolding.py` solves (OC16)--(OC18) directly. Representative values are:

\[
\begin{array}{c|c|c|c|c}
\eta & x & \delta & s & T-t_4\\ \hline
10^{-6}
&0.7859885342081823
&0.07070339947458162
&0.1411839261721631
&2.1987277700\times10^{-4}\\
5\times10^{-6}
&0.7860004415957326
&0.07071830450840642
&0.1411411975290172
&2.80411487796\times10^{-4}\\
10^{-5}
&0.7860153219449904
&0.07073693445470553
&0.1410877917171212
&3.56077192290\times10^{-4}\\
2\times10^{-5}
&0.7860450696978172
&0.07077418985688456
&0.1409809967309833
&5.07382982786\times10^{-4}\\
4\times10^{-5}
&0.7861045134569037
&0.07084868267153449
&0.1407674732910808
&8.09892051988\times10^{-4}
\end{array}
\tag{OC19}
\]

Every displayed solution has

\[
\boxed{T-t_4>0.}
\tag{OC20}
\]

Thus the simultaneous collision is not destroyed by causality. In fact the available final margin grows on this local branch over the tested range.

## 5. A concrete certified working point for the next stage

Choose

\[
\boxed{\eta=10^{-5}.}
\tag{OC21}
\]

Then

\[
\boxed{
\begin{aligned}
x&\approx0.7860153219449903870,\\
\delta&\approx0.0707369344547055350,\\
s&\approx0.1410877917171212372,\\
T&\approx0.1414738689094110699.
\end{aligned}}
\tag{OC22}
\]

The ordered event times are

\[
\begin{aligned}
t_1&\approx0.1410877917171212,\\
t_2&\approx0.1410977917171212,\\
t_3&\approx0.1411077917171212,\\
t_4&\approx0.1411177917171212,
\end{aligned}
\tag{OC23}
\]

and

\[
\boxed{T-t_4\approx3.56077192290\times10^{-4}.}
\tag{OC24}
\]

At this ordered solution the three-equation Jacobian is approximately

\[
\begin{pmatrix}
-1.65230027&1.31960802&0\\
2.51864854&1.36039599&0\\
-11.76655691&-13.00639413&-11.76655691
\end{pmatrix},
\]

with

\[
\boxed{\det J\approx65.5563301261\ne0.}
\tag{OC25}
\]

so the ordered branch remains strongly transverse.

## 6. Ordered action headroom

At the working point (OC22), the promoted modes retain substantial positive headroom over their natural envelopes. The action defects `A_promoted-I_beta` are approximately

\[
\begin{array}{c|r}
\text{state}&\text{headroom}\\ \hline
P(t_1)&0.31167084\\
P(t_2)&0.31167084\\
E(t_2)&1.18640613\\
E(t_3)&1.18640613\\
Q(t_3)&0.13480265\\
Q(t_4)&0.13480265\\
H(t_4)&0.06179769\\
H(T)&0.06179769
\end{array}
\tag{OC26}
\]

The final reset is exact at the working precision:

\[
\boxed{A_{P_{\rm new}}(T)-I_2(x)=O(10^{-60}).}
\tag{OC27}
\]

Thus causal propagation between the micro-collars does not consume the available reduced action margin.

## 7. Principal polarization persists under ordering

At the same `eta=10^-5` point, evaluation of the exact principal source-frame formulas gives, for `u_*=100`, approximately

\[
\boxed{
\begin{array}{c|r}
C+D\to P& 2.15861\\
P+D\to E& 7.81199\\
E-C\to Q& -40.8421\\
Q-C\to H& -53.6384\\
H+D\to P_{\rm new}& 2.54596
\end{array}}
\tag{OC28}
\]

and at `u_*=10`

\[
0.21340,\quad0.78031,\quad-4.08016,\quad-5.34375,\quad0.25057.
\tag{OC29}
\]

Hence no mandatory edge approaches a principal polarization zero when the simultaneous collision is unfolded into ordered collars.

## 8. Consequence

The previous temporal objection is removed at reduced/principal level:

\[
\boxed{
\text{finite reset genealogy}
+
\text{exact phase reset}
+
\text{exact action reset}
+
\text{nonzero polarization}
+
\text{strict causal ordering}
}
\tag{OC30}
\]

can hold simultaneously.

This upgrades the construction to a **causal principal-level finite reset supercell candidate**.

The next sharp barrier is no longer event ordering. It is the complete promoted/non-designated action audit: one must prove that, after declaring the finite set `P,C,D,E,Q,H,P_new` as designated/promoted channels, every other quadratic descendant generated during the ordered supercell remains below them by a uniform positive action margin. If that closes, the next step is exact finite-`u_*` source persistence and then the phase-adapted zero-residual PDE solve.