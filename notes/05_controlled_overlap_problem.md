# Note 05 — controlled-overlap problem, v0.4

The source forced construction deliberately separates most labels so cross-products vanish by support geometry. An autonomous relay instead permits one designated interaction family.

The v0.4 local relay uses the **difference harmonic**:

\[
(P_j^{(1)},\overline{P_j^{(2)}})
\longrightarrow C_j,
\]

with

\[
\Phi_{C_j}=\Phi_{P_j^{(1)}}-\Phi_{P_j^{(2)}},
\qquad
\beta_1-\beta_2=1.
\]

All non-designated pairs should still satisfy exact auxiliary-support separation.

## Sparse relay supernodes

Treat each permitted relay family as a finite supernode. Relative auxiliary offsets inside a supernode are prescribed by the translated-overlap lemma; distinct supernodes remain disjoint whenever their slow supports meet.

The core local obligations are now:

1. the designated **difference** harmonic produces a unit-beta child source with a scale-uniform growing-polarization lower bound;
2. the unwanted **sum** harmonic \(\beta_+=17/8\) is solved as a strongly damped correction, not discarded;
3. parent-child feedback remains exponentially suppressed during the seed collar and is then solved exactly;
4. curl, cutoff, transport-defect and Leray errors improve in the wave hierarchy;
5. every correction step preserves the sparse support graph.

After local closure, a separate physical-scale inheritance theorem must transport the child from \(q_j\) to a later \(q_{j+1}<q_j\).
