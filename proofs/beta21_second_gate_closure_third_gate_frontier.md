# Second active-gate closure and the third-gate frontier

**Status:** WORKING-RESEARCH HANDOFF / ARCHITECTURE UPDATE. The unrouted second active gate is now closed at local exact zero-residual level by `beta21_second_gate_unrouted_C1_exact_closure.md`. The attempted strategy of physically routing the old catalyst out of the second overlap is no longer needed and should not be treated as the preferred architecture.

The correct programme-level lesson is stronger: exact active gates need not preserve a perfectly clean state throughout the transport interval between designated events. A gate prescribes a clean finite set of exit coordinates at its own section. If surviving physical parents regenerate previously cancelled characters before the next event, those regenerated modes must be included in the **next gate's actual input/critical audit** rather than assumed absent by routing labels.

## 1. Closed first two local gates

First gate:

\[
C+D\to P
\]

with exact finite control cancellation of its complete dangerous block.

Second gate, with old `C,D` retained:

\[
(C,D,P_{tr})_{in}
\longmapsto
(C,D,E_*)_{out},
\tag{ST1}
\]

where

\[
P_{out}=0,
\]

the complete ten-state beta-zero root family is zero at the exit section, and every uncontrolled naturally critical coordinate has a fixed negative action gap on the certified collar.

Thus the second gate no longer depends on the routed hypothesis `C_old notin I_2`.

## 2. Why a free interval does not stay clean

Immediately after the second exit, the retained physical pair `C,D` is still present. Therefore the quadratic PDE again contains

\[
C+D\to P,
\qquad
D-C\to M,
\]

and their descendants.

Hence the identities

\[
P_{out}=0,
\qquad M_{out}=0
\]

are **section conditions**, not statements that these coefficients remain identically zero forever afterward.

This is not a contradiction. The exact unforced PDE evolves them again from the surviving parents.

## 3. Rejected architectural assumption

The following assumption should no longer be used without a separate theorem:

\[
\boxed{
\text{gate }j\text{ cancels a mode}
\Longrightarrow
\text{that mode is absent at gate }j+1.
}
\tag{ST2}
\]

It is false whenever the physical parents capable of regenerating that mode remain overlapping during the transport interval.

Likewise one should not impose artificial temporal cutoffs merely to enforce (ST2) unless their transition residual is proved action-flat at the relevant scale.

## 4. Correct concatenation principle

For each event section `t_j`, define the **actual incoming leading bank** by propagating the exact designated parents and allowing every source-matched regeneration from the preceding interval.

Then:

1. enumerate the naturally critical characters at `t_j`;
2. compute maximal attainable leaf actions from the actual incoming bank;
3. identify the positive-defect finite block;
4. factor it through useful beta-zero/root families when possible;
5. build an internal active control map at the matching source action;
6. prescribe the desired output and cancel the dangerous finite block exactly at the exit section.

Thus the cell becomes a sequence of exact local input-output gates rather than a passive support-routing circuit.

## 5. Timing flexibility remains available

The exact finite-`u=4` action-reset equation has substantial timing freedom. For example, keeping the original first two event times fixed and moving the third event closer to the second still leaves a causal fourth-event solution.

With

\[
t_1=0.213506242359214\ldots,
\qquad
t_2=t_1+0.005,
\]

choosing

\[
t_3=t_2+0.0005
\]

allows an exact reset-action fourth time approximately

\[
\boxed{t_4\approx0.235536941242592,}
\tag{ST3}
\]

with a large remaining margin before

\[
T=0.351099211738859\ldots.
\]

This numerical observation shows that active-collar placement has room for redesign. It should not yet replace the published ordered timing ledger until the third/fourth critical audits are redone at the chosen times.

## 6. Third-gate problem

The nominal third edge is

\[
\boxed{E-C\to Q=2D.}
\tag{ST4}
\]

But the actual input at the third section is not merely `(E,C)`. At minimum the surviving parents `C,D` have had time to regenerate

\[
P=C+D,
\qquad
M=D-C,
\]

and possibly finite descendants, while `E` is the transported desired output of the second gate.

Therefore the third gate must start with a fresh full audit of the actual bank, schematically

\[
\boxed{(C,D,E;\ P_{regen},M_{regen},\ldots)}
\tag{ST5}
\]

rather than copying either the first or second gate theorem.

## 7. Immediate next task

The next theorem layer should:

1. fix one third-section time consistent with exact reset action;
2. propagate the second-gate output actions to that section;
3. compute the regenerated `P/M` leading actions over the inter-gate interval;
4. reduce the incoming action bank by dominance (discarding only genuinely subleading representations);
5. enumerate the full finite naturally critical set at the third section;
6. identify the positive-defect block for the intended `E-C -> Q` gate.

Only after that enumeration should a third control count or Vandermonde/PBH architecture be proposed.

No claim of a completed five-gate reset cell is made at this stage.
