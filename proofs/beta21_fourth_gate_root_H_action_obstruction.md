# Root-`H` action obstruction at the fourth beta-(2,1) gate

**Status:** PROVED LEADING-ACTION OBSTRUCTION TO A NAIVE CONTINUATION OF THE ORIGINAL `Q-C -> H` RESET GENEALOGY AFTER THE FIRST THREE EXACT ACTIVE GATES. The third gate can prescribe a promoted nonzero

\[
Q=2D
\]

while cancelling the leading mean-root family at its exit section. However the retained physical parents `C,D` immediately regenerate the beta-zero root and hence the character

\[
H=2D-C
\]

through a shorter genealogy whose action is exponentially larger than the nominal `Q-C -> H` genealogy.

Therefore the fourth active gate is intrinsically a **two-action-scale problem**. One cannot merely regard the strong root-generated `H` as a perturbation of the weaker intended `Q-C` output. Either the gate must cancel the strong root-scale `H` down to a prescribed weaker `Q-C`-scale residue, or the final reset architecture must be redesigned to use the strong root-generated `H` as the actual parent.

No fourth-gate closure is claimed here.

## 1. Immediate fourth-gate entrance

Concatenate gates two and three without a free transport interval. At the exact third-gate exit section,

\[
P=E=0,
\qquad
Q=Q_*\ne0,
\qquad
M=X_2=\cdots=X_{10}=0,
\tag{H4O1}
\]

while the physical unit-beta parents `C,D` remain present.

The relevant parent actions at the working finite-`u=4` section are, to leading frozen precision,

\[
A_C=-0.0660362173740943\ldots,
\qquad
A_D=-0.0240786305040794\ldots.
\tag{H4O2}
\]

The third-gate promoted `Q` is normalized on

\[
\boxed{
A_Q^{prom}=2A_C+2A_D
=-0.180229695756347\ldots.
}
\tag{H4O3}
\]

The exact values drift only continuously over the short active collars and the fixed action inequalities below persist after reducing the collar widths if necessary.

## 2. Nominal fourth edge

The original ordered reset genealogy prescribes

\[
\boxed{Q-C\to H=2D-C.}
\tag{H4O4}
\]

Using the promoted `Q` action (H4O3), this path carries

\[
\boxed{
A_H^{Q-C}
=A_Q^{prom}+A_C
=3A_C+2A_D.
}
\tag{H4O5}

Numerically,

\[
A_H^{Q-C}
=-0.246265913130442\ldots.
\tag{H4O6}

## 3. Shorter unavoidable mean-root path

The same retained parents generate

\[
D-C\to M=D-C
\tag{H4O7}
\]

at action

\[
A_M=A_C+A_D.
\]

The next nonzero mean-wave edge is

\[
D+M\to H=2D-C.
\tag{H4O8}
\]

Therefore the shorter root genealogy carries

\[
\boxed{
A_H^{root}
=A_C+2A_D.
}
\tag{H4O9}

Numerically,

\[
A_H^{root}
=-0.114193478382253\ldots.
\tag{H4O10}

This is the same leading action scale on which `H=X_2` appeared as a dangerous positive-defect mode in the second/third full critical audits.

## 4. Fixed exponential dominance

Subtracting (H4O5) from (H4O9),

\[
\boxed{
A_H^{root}-A_H^{Q-C}
=-2A_C.
}
\tag{H4O11}

Since `A_C<0`,

\[
\boxed{
A_H^{root}-A_H^{Q-C}
=0.132072434748189\ldots>0.
}
\tag{H4O12}

On the source action scale `Lambda_ell ~ c S_*`, the ratio of the root-generated `H` amplitude to the nominal `Q-C` amplitude is therefore

\[
\boxed{
\exp\{(0.13207\ldots)\Lambda_\ell\}.
}
\tag{H4O13}

No polynomial source loss, fixed epsilon power or ordinary perturbative correction can make the root contribution negligible relative to the nominal `Q-C` contribution.

## 5. Both mandatory root edges are genuinely nonzero

The beta-zero root projection `D-C -> M` is nonzero by the mean-root source audit. The next edge

\[
D+M\to H
\]

has source-frame growing coefficient near

\[
-17.96
\]

at the working geometry and remains a fixed distance from zero on the short active collars.

Thus the larger action (H4O9) is dynamically realized; it is not merely a formal absolute-leaf upper bound.

## 6. Consequence for a fourth active gate

At the fourth entrance the desired character `H` therefore has **two parametrically separated source scales**:

\[
\boxed{
\text{leading root scale: }A_C+2A_D,
}
\tag{H4O14}
\]

and

\[
\boxed{
\text{subleading nominal }Q-C\text{ scale: }3A_C+2A_D.
}
\tag{H4O15}

A one-scale IFT normalized on the nominal `Q-C` output fails immediately: the root-generated contribution is exponentially large in that normalization.

A one-scale IFT normalized on the root action can cancel/prescribe the leading `H`, but a target of the weaker scale (H4O15) appears as an exponentially small residual in that normalized coordinate. Retaining that residue with sufficient accuracy requires a second action layer or a different final genealogy.

## 7. Two legitimate research routes

The fourth-gate frontier splits cleanly.

### Route A: two-scale active cancellation

First solve a leading root-scale gate imposing

\[
H^{root}_{out}=0
\]

(and cancelling the rest of the dangerous root family) in the action normalization `A_C+2A_D`. Then, inside the kernel/near-kernel left after leading cancellation, use a second finite control layer normalized on

\[
3A_C+2A_D
\]

to leave a prescribed nonzero

\[
H_{out}=H_*^{weak}
\]

coming from the `Q-C` genealogy.

This route needs a **nested/two-scale implicit-function theorem** and a source-matched secondary control direction.

### Route B: redesign the final renewal using strong `H`

Accept the root-generated `H` at action `A_C+2A_D` as the actual fourth-gate output. Then recompute the final edge

\[
H+D\to P_{new}
\]

and the reset-face action equation using this stronger `H` action rather than the original weaker `Q-C` ledger.

If a causal reset timing/root exists with the renewed pair `(P_new,D)` on the desired action section, this route avoids the two-scale cancellation entirely.

## 8. Preferred next attack

Route B is the cheaper and more structural test: before building a nested two-scale IFT, solve the exact finite-`u=4` reset equation with

\[
A_H=A_C+2A_D
\]

and determine whether any causal fourth/final event can return `P_new=H+D` to the renewed beta-two parent action at the reset face.

If no such timing exists, Route A becomes mandatory. If such a timing exists, the original five-edge genealogy can be replaced by an active-gate renewal in which the fourth output is the strong mean-root `H`.

No complete reset cell is claimed in this note.
