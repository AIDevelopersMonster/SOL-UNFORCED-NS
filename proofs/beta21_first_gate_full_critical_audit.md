# Full first-gate critical-mode audit for the finite-u beta-(2,1) cleanup cell

**Status:** COMPUTER-ASSISTED EXACT-ENVELOPE CLASSIFICATION / FINITE CRITICAL BLOCK IDENTIFIED. At the source-safe working point `u_*=4`, the first active `C+D -> P` collision gate has only finitely many center modes that can be principal-growing or neutral. Among that finite set, the exact leaf-action audit finds only two non-designated characters with positive action defect at the gate center:

\[
H=2D-C,
\qquad
R_3=3D-2C.
\]

The previously controlled block `(E,Q,H)` is therefore incomplete: `R_3` is a second genuinely supercritical shortcut descendant. A sufficient clean active-gate output block is

\[
\boxed{(P,E,Q,H,P_{new},R_3)}
\]

with six complex controls. `P_new` itself is action-subcritical at the first gate center, but including it keeps the controlled shortcut chain triangular and gives a consecutive-degree Vandermonde response theorem.

The companion exact-arithmetic script is `experiments/beta21_first_gate_critical_audit.py`.

## 1. Exact finite-u working point

Use the turning-point cleanup gauge

\[
x+\delta=1
\]

and the exact finite-`u` resonance

\[
\mathcal E_{2,4}(1-\delta)
=
\mathcal E_{1,4}(1-2\delta).
\tag{FC1}
\]

High-precision solution gives

\[
\boxed{
\delta
=0.1755496058694293259805486194\ldots
}
\tag{FC2}
\]

and

\[
\boxed{
x=1-\delta
=0.8244503941305706740194513806\ldots.}
\tag{FC3}
\]

At the first late gate section,

\[
z_C=1,
\qquad
z_D=1-2\delta,
\tag{FC4}
\]

with

\[
A_C=\mathcal E_{1,4}(1)=0,
\]

\[
\boxed{
A_D:=\mathcal E_{1,4}(1-2\delta)
=-0.1713153638562057966442330517\ldots.
}
\tag{FC5}
\]

## 2. Character parametrization

Every lattice character generated from `D,C` has the form

\[
K_{m,n}=mD+nC,
\qquad m,n\in\mathbb Z.
\tag{FC6}
\]

Its signed beta is

\[
\boxed{B=m+n.}
\tag{FC7}
\]

For `B>0`, its normalized reduced slope at the first gate center is

\[
\boxed{
\xi_{B,m}
=\frac{m(1-2\delta)+(B-m)}{B}
=1-\frac{2m\delta}{B}.
}
\tag{FC8}

The beta-`B` principal growing rate is nonnegative only when

\[
|\xi_{B,m}|
\le x_{B,4},
\tag{FC9}
\]

where

\[
\boxed{
x_{B,4}
=\frac1{4}
\sqrt{17B^{-4/3}-1}.}
\tag{FC10}

For `B>=9` the expression under the square root is negative. Hence every mode with

\[
\boxed{|B|\ge9}
\tag{FC11}

is strictly principal-decaying at `u=4`, independent of its radial character.

Thus only

\[
1\le |B|\le8
\tag{FC12}

can enter the principal critical block.

## 3. Finite center-critical enumeration

For each `1<=B<=8`, solve the integer inequality

\[
\left|1-\frac{2m\delta}{B}\right|
\le x_{B,4}.
\tag{FC13}

The exact numerical enumeration is:

\[
\begin{array}{c|c|c}
B&m\text{-range}&\#\\ \hline
1&0,\ldots,5&6\\
2&3,\ldots,9&7\\
3&5,\ldots,12&8\\
4&8,\ldots,15&8\\
5&11,\ldots,17&7\\
6&14,\ldots,20&7\\
7&18,\ldots,22&5\\
8&22,\ldots,24&3
\end{array}
\tag{FC14}

Therefore the positive-beta center-critical set contains exactly

\[
\boxed{51}
\tag{FC15}

integer characters before identifying conjugates. Negative `B` gives the conjugate real-field partners and does not double the number of independent complex controls.

This is the finite set that must be action-audited; no infinite search remains.

## 4. Maximal leaf action

A genealogy producing `K_{m,B-m}` contains at least `|m|` leaves of type `D` and `|B-m|` leaves of type `C`. Since

\[
A_C=0,
\qquad A_D<0,
\]

its largest possible leaf-product action is

\[
\boxed{
S_{B,m}=|m|A_D.
}
\tag{FC16}

Any extra cancelling pair of leaves makes the action strictly more negative and therefore cannot create a worse defect.

Define the center action defect

\[
\boxed{
\Delta_{B,m}
:=|m|A_D
-\mathcal E_{B,4}(|\xi_{B,m}|).
}
\tag{FC17}

A positive value means that the genealogy lies exponentially above the natural beta-`B` envelope and cannot be placed in the action-subcritical remainder.

## 5. Exact outcome of the 51-mode audit

Among all 51 center-critical characters, apart from the input/designated modes, the only positive defects are

\[
\boxed{
(B,m,n)=(1,2,-1),
}
\tag{FC18}

and

\[
\boxed{
(B,m,n)=(1,3,-2).
}
\tag{FC19}

The first is

\[
\boxed{H=2D-C}
\tag{FC20}
\]

with

\[
\boxed{
\Delta_H
=0.4053578727752794922875740161\ldots>0.
}
\tag{FC21}

The second is

\[
\boxed{R_3=3D-2C}
\tag{FC22}
\]

with the much larger defect

\[
\boxed{
\Delta_{R_3}
=1.010820667384140717665080894\ldots>0.
}
\tag{FC23}

Every other non-designated center-critical character has strictly negative defect.

The closest negative cases include

\[
\boxed{
\Delta_{B=2,m=6}
=-0.0176368841207849543\ldots,
}
\tag{FC24}

and

\[
\boxed{
\Delta_{B=1,m=4}
=-0.1670363174790024984\ldots.
}
\tag{FC25}

Thus the classification has a nonzero exact-envelope margin, although the beta-two margin (FC24) is relatively small and must be preserved when the physical gate collar is chosen.

## 6. The missing descendant is structurally reachable

The already identified shortcut chain is

\[
C+D\to P,
\qquad
P+D\to E,
\qquad
E-C\to Q,
\qquad
Q-C\to H.
\tag{FC26}

But it continues:

\[
\boxed{H+D\to P_{new}=3D-C,}
\tag{FC27}

then

\[
\boxed{P_{new}-C\to R_3=3D-2C.}
\tag{FC28}

The first new edge is a sum of two beta-one modes; the second is a positive-slope beta-two minus beta-one difference edge whenever evaluated before its slope crosses zero. Difference-edge nonvanishing follows from the generic polarization formula whenever the slopes are unequal. At the first-section geometry the corresponding principal projection is nonzero.

Therefore `R_3` is not merely an arithmetic lattice witness. It lies on a bounded rooted quadratic genealogy extending the already active shortcut chain.

## 7. Why `(E,Q,H)` was insufficient

Cancelling

\[
E_{out}=Q_{out}=H_{out}=0
\]

at the first gate exit removes the explicit fourth-order shortcut trace, but it does not by itself provide a closed triangular control model for the next two descendant coordinates generated inside the same open collar.

Because `R_3` has the larger positive action defect (FC23), it must be included explicitly in the finite exit audit unless a separate theorem proves that its generation coefficient or support vanishes identically. No such structural zero is currently available.

The intermediate

\[
P_{new}=3D-C
\tag{FC29}

has beta two and is action-subcritical at the first gate center. It could in principle be left in the stable finite remainder. However `P_new` is the immediate parent of the supercritical `R_3`. Including it in the controlled block makes the gate dynamics strictly triangular and avoids relying on a secondary cancellation through an uncontrolled intermediate coordinate.

Hence a sufficient clean controlled block is

\[
\boxed{
\mathcal Y_{gate}
=(P,E,Q,H,P_{new},R_3)\in\mathbb C^6.
}
\tag{FC30}

## 8. Consequence for the control count

Prescribing one complex desired output `P_*` and killing the five complex shortcut coordinates gives six complex equations:

\[
\boxed{
P_{out}=P_*\ne0,
\quad
E_{out}=Q_{out}=H_{out}=P_{new,out}=R_{3,out}=0.
}
\tag{FC31}

Therefore a generic locally onto clean-gate map requires at least

\[
\boxed{6\ \text{complex controls}}
\tag{FC32}

for this sufficient triangular formulation.

This is a **sufficient clean budget**, not yet a theorem that six is absolutely minimal. A sharper formulation may omit the action-subcritical `P_new` row and attempt a five-control generalized-Vandermonde solve for `(P,E,Q,H,R_3)`. The six-control route is preferred first because its downstream response kernels have consecutive orders `0,1,2,3,4,5`.

## 9. Stability scope of the center audit

This file classifies the exact first-section/center action defects. A physical control profile occupies a short but nonzero interval. Since the finite set (FC15) is finite and every non-designated negative defect has a strict center margin, continuity gives a sufficiently short fixed normalized gate collar on which all modes except `H,R_3` remain action-subcritical.

The smallest displayed center margin is about

\[
1.76\times10^{-2},
\]

so the collar must be chosen quantitatively small relative to the derivatives of the finitely many exact envelope-defect functions. Establishing one explicit admissible width is the next quantitative robustness step; no infinite-lattice continuity argument is needed.

## 10. New frontier

The first active-gate problem is now finite and explicit:

\[
\boxed{
\textbf{prove a six-control smooth-profile Vandermonde theorem for}
\ (P,E,Q,H,P_{new},R_3),
}
\tag{FC33}

then transfer it to the exact catalyst-subpacket source realization and compute an explicit gate-width margin preserving the negative defect (FC24).

If these two steps close, the first genealogy-breaking collar is source-level complete for the full center-critical block. It can then be inserted as the first stage of the ordered reset circuit.
