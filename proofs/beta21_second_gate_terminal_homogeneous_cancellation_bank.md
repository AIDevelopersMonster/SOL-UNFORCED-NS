# Terminal homogeneous cancellation bank for the routed second beta-(2,1) gate

**Status:** PROVED PRINCIPAL/SOURCE-CLASS REDUCTION ARCHITECTURE; EXACT MULTI-COLLAR `C^1` TRANSFER REMAINS. The full second-gate critical audit identifies only four unwanted positive-defect naturally-critical complex characters after the routed `P-D` collision:

\[
H_1:=2D-C,
\qquad
H_2:=3D-2C,
\qquad
H_3:=4D-3C,
\qquad
H_4:=7D-5C.
\]

Together with the desired beta-three output `E=C+2D`, this gives five critical growing exit coordinates. Rather than controlling the entire difference-rooted genealogy through one indirect `P-D` source channel, use a **terminal homogeneous correction bank**: first complete the principal `P-D` collision, then route the parents `P,D` out of the terminal correction zone, and finally use one source-native homogeneous growing pulse in each of the five output characters to set the five growing exit coordinates directly.

At frozen principal level the resulting control map is diagonal with nonzero diagonal. The construction uses the homogeneous pulse class already supplied by the pinned source and introduces no new lattice generator. The remaining theorem is to concatenate the finite terminal microcollars with the exact phase-adapted zero-residual solve and prove the diagonal exit Jacobian is perturbed only by `o(1)`.

## 1. Critical output vector

Let

\[
\boxed{
Y_2=(E,H_1,H_2,H_3,H_4)\in\mathbb C^5
}
\tag{TH1}
\]

be the phase-normalized **growing** exit coordinates, where

\[
\begin{aligned}
E&=C+2D,\\
H_1&=2D-C,\\
H_2&=3D-2C,\\
H_3&=4D-3C,\\
H_4&=7D-5C.
\end{aligned}
\tag{TH2}
\]

The target is

\[
\boxed{
Y_*=(E_*,0,0,0,0),
\qquad E_*\ne0.
}
\tag{TH3}
\]

`beta21_second_gate_full_critical_audit.md` proves that every other naturally growing/neutral positive-beta lattice character has a strictly negative center leaf-action defect. High-beta modes `|B|>=9` are uniformly forward-decaying.

Thus (TH1) is the finite critical growing output that must be prescribed, provided the terminal correction bank itself does not reintroduce the routed parents.

## 2. Separate collision and correction zones

Decompose the routed second stage into

\[
I_{coll}
\prec
I_{corr,1}
\prec\cdots\prec
I_{corr,5},
\tag{TH4}
\]

with strict causal ordering in the auxiliary pulse coordinate.

On `I_coll`, the physical leading parents are

\[
P,D
\]

and the intended quadratic generation `P+D -> E` occurs together with all unavoidable finite sidebands.

After `I_coll`, impose the handoff condition

\[
\boxed{
P,D\notin I_{corr,j}
\quad(j=1,\ldots,5).
}
\tag{TH5}
\]

This is the same type of support-routing obligation already forced by the second-gate refresh obstruction. It is essential: the terminal correction pulses must not meet the old parents and restart the `P-D` or `C-D` collision trees.

## 3. Source-native direct controls

For each output character `Y_j` in (TH1), choose a phase label carrying exactly that lattice character and use the homogeneous `m=1` growing pulse supplied by the pinned source pulse lemma. Denote its phase-normalized growing coefficient by

\[
U_j^{hom}.
\]

Scale it by a complex control amplitude `p_j` (with the usual conjugate partner for a real physical field):

\[
\boxed{
U_{ctrl}(p)
=\sum_{j=1}^{5}p_jU_j^{hom}.
}
\tag{TH6}
\]

These are not compactly hand-cut arbitrary profiles. They are source-native homogeneous pulses with their allowed envelope/cutoff architecture.

Each control has

1. the same lattice character as the coordinate it controls;
2. no new independent lattice generator;
3. exact divergence-free realization after the source curl construction;
4. a nonzero growing exit trace by the homogeneous pulse estimate;
5. polynomial source derivative bounds with the same pulse envelope.

## 4. No principal self-interaction obstruction

A homogeneous control pulse and the existing generated wave in the same character may be represented in the same principal growing polarization. Their sum is simply another amplitude in that one plane-wave character. The principal self-advection of one incompressible plane-wave polarization vanishes:

\[
(a\cdot k)a=0.
\tag{TH7}
\]

Therefore cancellation within one character does not itself create an order-one doubled-character source.

Localized/curl/frame corrections are lower source order and belong to the exact correction solve.

## 5. Separate different-character correction controls

Different correction characters should not all be superposed in one uncontrolled common overlap, because their cross-products could generate new finite sidebands. Instead place the five source-native controls in strictly ordered terminal microcollars.

The already-used auxiliary-rectangle translation lemma permits a finite family of phase labels to be positioned at prescribed pulse coordinates. Generic label-center choices retain support separation between correction supernodes not intentionally overlapped.

Thus one may arrange that, at principal coefficient-product level,

\[
\boxed{
U_i^{hom}U_j^{hom}=0
\quad(i\ne j)
}
\tag{TH8}
\]

outside any deliberately designated same-character cancellation overlap.

In each `I_{corr,j}` only the existing `Y_j` trace and the matching homogeneous control are intentionally co-located. The routed parents have already left by (TH5).

## 6. Frozen principal exit map

Let

\[
y^{pre}=(E^{pre},H_1^{pre},H_2^{pre},H_3^{pre},H_4^{pre})
\]

be the growing amplitudes leaving `I_coll` before terminal correction.

Normalize each homogeneous control so that unit control amplitude produces unit growing trace at the final exit after its deterministic homogeneous transport. Then the principal terminal map is exactly

\[
\boxed{
Y_{out}^{principal}
=y^{pre}+p,
\qquad p\in\mathbb C^5.
}
\tag{TH9}
\]

Hence

\[
\boxed{
D_pY_{out}^{principal}=I_5,
\qquad
\det D_pY_{out}^{principal}=1.
}
\tag{TH10}
\]

The unique principal control vector is therefore

\[
\boxed{
p^0=Y_*-y^{pre}.}
\tag{TH11}
\]

This is stronger and simpler than a Vandermonde rank argument: control authority is direct in character space.

## 7. Why this does not conflict with the polarization-null source audit

The rejected polarization-null shortcut required an arbitrary order-one growing/decaying mixture **inside one beta-two P character**. The pinned homogeneous pulse lemma does not supply that mixture with the needed localized source estimates.

The present bank uses only the distinguished growing homogeneous pulse that the source does supply. Each control acts directly on its own growing output character. No decaying polarization freedom is assumed.

## 8. Remaining nonlinear/source terms

The exact local field contains lower-order terms from

- curl remainders;
- source-frame errors;
- slow coefficient variation;
- finite terminal handoff cutoffs;
- the exact mean correction;
- interactions of the controlled finite block with the stable complement.

The branch already has stage-uniform inverses for the stable nonzero lattice and the angular mean. What remains is to prove that, under the ordered support routing (TH4)--(TH8), differentiating the exact multi-collar correction solve in the five terminal amplitudes gives

\[
\boxed{
D_p\mathcal G_{2,\ell}
=I_5+o(1)
}
\tag{TH12}
\]

in the phase-normalized growing coordinates.

If (TH12) holds, then for all sufficiently high levels

\[
|\det D_p\mathcal G_{2,\ell}|\ge\frac12
\]

and the implicit-function theorem yields an exact nearby control vector

\[
p_\ell=p^0+o(1)
\]

with

\[
\boxed{
(E,H_1,H_2,H_3,H_4)_{out}
=(E_*,0,0,0,0).
}
\tag{TH13}
\]

## 9. Sharp remaining obligations

The second gate has therefore been reduced to two explicit tasks:

1. **support handoff:** prove the routed parents `P,D` can leave the terminal correction zone while the five generated critical traces are transported into their matching cancellation microcollars;
2. **five-parameter exact transfer:** extend the existing parameter-dependent local zero-residual theorem across the finite ordered collision-plus-correction chain and establish (TH12).

The full lattice enumeration and finite principal control rank are no longer the bottleneck under this architecture.

No exact second active gate, full reset cell, or unforced Navier--Stokes blowup theorem is claimed yet.
