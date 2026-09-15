# Nine-lobe unit-beta bank renewal circuit

**Status:** PROVED FINITE CARDINALITY / SUPPORT-ROUTING ARCHITECTURE, CONDITIONAL ON ONE REMAINING UNIFORM LOBE-NONDEGENERACY ESTIMATE FOR THE DIRTY RESERVE CHILDREN. This theorem combines the unit-beta control replacements and reserve-waste summability into a concrete finite bank whose cardinality is exactly preserved by one corrected beta-(2,1) cell.

The input bank has nine physical support-separated unit-beta lobes

\[
\boxed{
\mathcal B_{in}=\{C_1,\ldots,C_9\}.
}
\tag{LB1}

The output bank has nine physical generated unit-beta children

\[
\boxed{
\mathcal B_{out}=\{D_1,\ldots,D_9\},
}
\tag{LB2}

which are relabeled as the next catalyst bank. No profile-coordinate fixed point is assumed.

## 1. Why nine lobes

The largest exact active control block in the corrected cell is the strong-`H` gate, which needs nine translated unit-beta catalyst controls. The entrance replacement theorem needs only four unit-beta controls, and the terminal replacement theorem needs only three unit-beta controls.

Hence

\[
\boxed{N_{lobe}=9}
\tag{LB3}

is sufficient for all three active gates if the same finite physical bank is routed through the cell.

## 2. Input bank and parent

Start one cell with

\[
(P,C_1,\ldots,C_9),
\]

where all `C_j` have the same beta-one Fourier character, canonical source cone and principal polarization, but distinct support labels/centers.

Their normalized amplitudes lie in one fixed compact nonzero set. Their support geometry is chosen using the same finite translated-rectangle machinery as in the earlier finite-bank theorem.

## 3. Dirty reserve generation for lobes 2 through 9

For each

\[
j=2,\ldots,9,
\]

place one support-separated short source-matched interaction

\[
\boxed{P-C_j\to D_j.}
\tag{LB4}

These eight reserve events need **not** solve an independent four-control exact-clean exit problem.

The desired `D_j` child is retained. The finitely many companion descendants produced in that reserve event are assigned to waste corridors disjoint from every later designated relay supernode.

By `reserve_waste_energy_summability.md`, a fixed finite number of such routed-away normalized descendants per level has total energy

\[
\sum_j E_j^{waste}<\infty.
\]

Therefore no recursive four-profile subbank is required for each reserve lobe.

## 4. One exact clean entrance lane produces `D_1`

After the reserve events, use the four physical catalyst lobes

\[
C_1,C_2,C_3,C_4
\]

as the four translated unit-beta controls of `beta21_corrected_entrance_four_C_control_rank.md`.

The exact entrance map prescribes

\[
\boxed{
(D_1,M,H,R_3)_{out}
=(D_{1,*},0,0,0),
\qquad D_{1,*}\ne0.
}
\tag{LB5}

This is the unique **clean active child** that will remain on the singular relay spine through the strong-`H` and terminal gates.

The dirty reserve children `D_2,...,D_9` are support-separated from this clean entrance supernode after their generation.

## 5. Strong-`H` gate uses the entire nine-lobe catalyst bank

Route the clean active child `D_1` to the strong-`H` collar.

Arrange the nine catalyst lobes

\[
C_1,\ldots,C_9
\]

as the nine translated same-character control lobes of `beta21_corrected_strong_H_nine_control_C1_closure.md`.

The exact gate produces the renewed beta-two parent and removes every promoted strong-`H` trace other than the designated pair:

\[
\boxed{
(P_{new},D_1)
}
\tag{LB6}

with all controlled catalyst/root/sum coordinates at their exact prescribed values.

After this gate the old catalyst lobes are no longer required by the relay state. The output unit-beta bank will be supplied by the already-generated `D_j` family.

## 6. Terminal gate uses three reserve children as controls

Choose

\[
D_2,D_3,D_4
\]

to follow support corridors that avoid the strong-`H` supernode but enter the relocated late terminal collar.

Use them as the three unit-beta controls from `beta21_corrected_terminal_three_D_control_rank.md`. The retained base unit-beta channel is `D_1`.

The exact terminal gate imposes

\[
\boxed{
(P_{new},H,M)_{out}
=(P_*,0,0),
}
\tag{LB7}

while all four unit-beta lobes `D_1,D_2,D_3,D_4` remain physical output packets in their prescribed support lanes.

After the last-overlap exit, parent/support separation prevents regeneration of the cancelled terminal descendants.

## 7. Pure reserve lobes

The remaining children

\[
D_5,\ldots,D_9
\]

are routed outside all strong-`H` and terminal designated supernodes.

They undergo only their own forward transport plus the global exact correction field. Their reserve-generation side products were already routed to waste corridors in Section 3.

Thus all nine unit-beta children reach the reset region as physically present support-separated packets.

## 8. Cardinality renewal

At the reset face, define

\[
\boxed{
\mathcal B_{out}
=\{D_1,D_2,\ldots,D_9\}.
}
\tag{LB8}

Every child has the same beta-one Fourier character after canonical relabeling. The clean child `D_1` has the exact corrected slope/action return. The reserve children were generated by the same source-matched entrance resonance and undergo the same beta-one homogeneous phase drift on their own designated channels, so their target slope/action center is the same unit-beta reset section, modulo the source-small exact correction already present in the full finite circuit.

Relabel

\[
\boxed{
D_j\mapsto C_j^{next},
\qquad j=1,\ldots,9.
}
\tag{LB9}

Then

\[
\boxed{
\#\mathcal B_{out}
=
\#\mathcal B_{in}
=9.
}
\tag{LB10}

No branching of the form `4 -> 16 -> ...` occurs.

## 9. Why the control-profile recursion has disappeared

The previous recursion objection was:

> to make one reserve child exact-clean, one needs four local controls; renewing those controls seems to require still more children.

The present architecture avoids that requirement.

Only the one active entrance lane `D_1` is exact-clean because it will enter later designated collisions on the singular spine. The other eight children need only remain nonzero and source-admissible; their finite unwanted side products are routed away and energy-summable.

Thus the exact control complexity per cell remains fixed:

- one four-control clean entrance solve;
- one nine-control strong-`H` solve;
- one three-control terminal solve;
- eight simple dirty reserve generation events.

No nested clean subproblem is created.

## 10. Remaining lobe theorem

The sole new local obligation is now quantitative rather than combinatorial:

\[
\boxed{
\textbf{uniform lobe nondegeneracy of each dirty reserve }D_j.
}
\tag{LB11}

For every reserve generation lane one must prove, uniformly at high levels, that the outgoing unit-beta packet satisfies:

1. a nonzero normalized complex amplitude bounded away from zero;
2. a strict source-cone/polarization margin;
3. a support width/shape condition sufficient for reuse as one translated control lobe at the next cell;
4. `C^1` stability under the source-small exact correction.

At frozen principal level item 1 follows from the already-audited nonzero coefficient

\[
\kappa_{P-C\to D}\ne0.
\]

Items 2--4 are the next sharp audit.

Once (LB11) is closed, the abstract full-profile fixed-point problem is replaced by a literal finite physical lobe renewal theorem.

No infinite unforced Navier--Stokes cascade or blowup theorem is claimed here.
