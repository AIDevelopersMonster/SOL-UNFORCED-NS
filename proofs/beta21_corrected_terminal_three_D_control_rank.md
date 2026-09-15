# Corrected terminal rank from three unit-beta `D` controls

**Status:** PROVED PRINCIPAL/FROZEN RANK REPLACEMENT THEOREM; EXACT `C^1` PERSISTENCE FOLLOWS BY THE SAME FINITE-PARAMETER ARGUMENT AS THE EXISTING TERMINAL THEOREM. The three beta-two `P_new` controls used in `beta21_corrected_terminal_three_control_C1_closure.md` are not structurally necessary. The late terminal block can instead be driven by three localized copies of the already-present unit-beta child `D`.

Together with `beta21_corrected_entrance_four_C_control_rank.md`, this reduces the complete corrected active-control character set to one self-renewing unit-beta sector.

## 1. Late terminal state

Use the relocated terminal collar

\[
I_{term}=[0.272,0.274]
\]

from `beta21_corrected_late_terminal_relocation.md`. The promoted state is

\[
(P,H,M)
\]

with

\[
H=P-D,
\qquad
M=H-D=P-2D.
\]

At the center `t=0.273`,

\[
z_D=0.9134445026067249\ldots,
\]

\[
z_P=0.7759445026067249\ldots,
\]

\[
z_H=0.6384445026067248\ldots.
\]

The already-audited difference edge satisfies throughout the collar

\[
\boxed{|κ_{P-D\to H}|>1.2475.}
\tag{TD1}
\]

The beta-zero edge satisfies

\[
\boxed{\|b_{H-D\to M}\|>4.016.}
\tag{TD2}
\]

## 2. The return edge `H+D -> P` is nonzero

Linearizing with respect to a localized perturbation of `D` creates the root coordinate `H` through the difference event `P-D_ctrl -> H`. To recover rank in the full three-state block we also need the in-block return edge

\[
H+D\to P.
\]

Using the same positive-beta sum formula as in the earlier gate audits, at the late center

\[
\boxed{
\kappa_{H+D\to P}
\approx +0.1922449871\ne0.
}
\tag{TD3}

At the collar endpoints the values are approximately

\[
0.1923877076,
\qquad
0.1921023409.
\]

Hence throughout `I_term`,

\[
\boxed{|κ_{H+D\to P}|>0.1921.}
\tag{TD4}

Thus the root `H` has nonzero leading couplings to both children `P` and `M`.

## 3. Simple frozen diagonal

At the center the normalized full-symbol rates are approximately

\[
\lambda_P=-0.5177742012,
\]

\[
\lambda_H=+0.3491976052,
\]

\[
\lambda_M=-0.02421243095.
\]

On the whole collar their pairwise separation remains larger than

\[
\boxed{δ_{spec}>0.372.}
\tag{TD5}

Therefore the frozen three-state graph has a simple diagonal with a root `H` coupled nontrivially to `P` and `M`.

## 4. Direct `D`-control input

Perturb the physically present unit-beta child by one localized same-character profile,

\[
D\mapsto D+pD_{ctrl}.
\]

The difference event

\[
P-D_{ctrl}\to H
\]

has the nonzero coefficient (TD1). Therefore the action-normalized control vector has a nonzero `H` component:

\[
\boxed{
B=b_He_H+b_Pe_P+b_Me_M,
\qquad b_H\ne0.
}
\tag{TD6}

The additional direct components are harmless.

## 5. Rooted-star PBH rank

Order the state as

\[
X=(H,P,M).
\]

The leading directed graph contains

\[
H\to P
\]

through (TD4), and

\[
H\to M
\]

through (TD2).

Because the diagonal rates are simple, the rooted-tree PBH lemma already proved in `beta21_corrected_terminal_tree_controllability.md` applies directly: a simple diagonal plus nonzero root-to-child tree edges is controllable from the root coordinate.

Thus

\[
\boxed{(A_{3,D},B_{3,D})\text{ is controllable}.}
\tag{TD7}

Equivalently, three suitable translated copies of one fixed smooth `D` profile produce an invertible `3 x 3` principal response matrix.

No special cancellation among direct lower components in (TD6) can remove controllability: the root component is nonzero and the rooted star spans the complete promoted block.

## 6. Smooth translated `D` profiles

Choose a fixed compact smooth profile `q` with nonzero transform on the three frozen spectral values and three distinct translated centers in `I_term`.

The response columns are

\[
K(\tau_j)=\int e^{A_{3,D}(v_+-s)}B_{3,D}q(s-\tau_j)\,ds.
\]

Controllability of `(A_{3,D},B_{3,D})` implies that three centers can be chosen with

\[
\boxed{\det J_{3,D}\ne0.}
\tag{TD8}

The fixed margins (TD1), (TD2), (TD4), (TD5) preserve this determinant under the actual slow coefficient variation on a sufficiently narrow positive collar.

## 7. Source realization

Every terminal control has exactly the same beta-one character, phase and principal polarization as the already present `D` packet.

Therefore:

1. no new lattice generator is introduced;
2. same-phase `D_i,D_j` principal self-interactions vanish;
3. finite smooth coefficient localization preserves the source wave classes;
4. curl realization restores exact divergence freedom with only the existing lower-order remainder;
5. finite parameter derivatives obey the same source exponents as the original terminal `P` controls.

Thus the replacement is source-admissible and internal to the designated field.

## 8. Exact `C^1` persistence

Define the exact terminal map driven by the three `D` amplitudes,

\[
\mathcal G^{term,D}_\ell(p)
=(P,H,M)_{out}.
\]

The proof of `beta21_corrected_terminal_three_control_C1_closure.md` uses only a fixed finite admissible profile family, a nonzero frozen determinant, the fixed action gap to omitted modes, and uniform parameter-differentiated nonzero/mean contraction estimates.

All these hypotheses hold here. Hence

\[
D_p\mathcal G^{term,D}_\ell
=J_{3,D}+o(1),
\]

and for sufficiently high levels the exact Jacobian is invertible.

Therefore one may prescribe

\[
\boxed{
(P,H,M)_{out}=(P_*,0,0),
\qquad P_*\ne0,
}
\tag{TD9}

while retaining the nonzero base `D` channel.

## 9. Global significance

The terminal gate no longer requires a separately renewed beta-two control-profile bank. Together with the entrance replacement theorem and the existing strong-`H` theorem, every active gate in the corrected cell can be parameterized by localized profiles of the same unit-beta character.

Thus the control-character problem collapses to one sector:

\[
\boxed{
\text{entrance controls: }C,\qquad
\text{strong-H controls: }C,\qquad
\text{terminal controls: }D\sim C_{next}.
}

The remaining autonomous issue is not mixed-character renewal. It is whether the finite translated **profile shapes/support lobes** required inside that one unit-beta sector can be realized from a fixed self-renewing carrier bank without independent future seeds.
