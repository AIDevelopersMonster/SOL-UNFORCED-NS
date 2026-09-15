# Uniform nondegeneracy of dirty reserve unit-beta lobes

**Status:** PROVED ONE-LANE PRINCIPAL + EXACT-`C^1` PERSISTENCE THEOREM, SUBJECT TO THE SAME BRANCH-WIDE NUMERICAL-CERTIFICATION CAVEAT AS THE CORRECTED ENTRANCE GATE. This closes the local nondegeneracy obligation (LB11) from `beta21_nine_lobe_unit_beta_bank_renewal.md`.

A reserve lane uses the exact source-matched corrected entrance interaction

\[
P-C_j\to D_j
\]

but does **not** impose exact cancellation of every companion descendant. The child `D_j` is retained, while the finite companion waste is routed away and controlled by `reserve_waste_energy_summability.md`.

The theorem proves that every such retained child is uniformly nonzero, stays in the strict source cone, has scale-uniform normalized support geometry, and survives the exact finite-circuit correction with the same properties.

## 1. Corrected reserve generation geometry

Freeze

\[
u=2.5,
\qquad
\delta=0.1375,
\qquad
x=0.7779445026067248271\ldots.
\]

At the entrance section,

\[
z_P=x,
\qquad
z_C=x+\delta,
\qquad
z_D=x-\delta.
\]

Numerically,

\[
\boxed{
z_D(0)=0.6404445026067248\ldots.}
\tag{RL1}

The exact source-action resonance is

\[
\mathcal E_{2,u}(x)
+
\mathcal E_{1,u}(x+\delta)
=
\mathcal E_{1,u}(x-\delta).
\tag{RL2}

Hence the direct difference child is generated on its natural unit-beta source action.

## 2. Uniform principal coupling

The positive-beta difference coefficient for

\[
P-C\to D
\]

was audited in `beta21_corrected_entrance_four_control_C1_closure.md` and `beta21_corrected_entrance_four_state_audit.py`.

At the collar center,

\[
\kappa_{P-C\to D}
\approx-1.24742865925.
\]

On the fixed entrance collar

\[
0\le t\le10^{-3},
\]

the sampled conservative margin is

\[
\boxed{
|\kappa_{P-C\to D}|>1.2472.
}
\tag{RL3}

Thus the direct child source is uniformly separated from every principal polarization zero.

## 3. One reserve bump gives a nonzero child

Let `q` be one fixed smooth nonnegative compact profile of nonzero mass, supported inside a sufficiently short subinterval of the entrance collar.

Let the normalized parent and catalyst amplitudes satisfy

\[
|A_P|\ge a_P>0,
\qquad
|A_{C_j}|\ge a_C>0,
\]

inside the fixed compact nonzero renewal neighborhood.

Choose the relative control phase so that the principal direct source has constant phase across the narrow support up to the already-audited slow variation. Then the principal Duhamel output in the `D_j` coordinate satisfies

\[
A_{D_j}^{prin}
=
\int q(s)
\kappa_{P-C\to D}(s)
A_P(s)A_{C_j}(s)
G_D(v_+,s)\,ds,
\tag{RL4}

where `G_D` is the normalized unit-beta forward propagator over the fixed short collar.

All factors other than the chosen bump are continuous and nonzero at the frozen center. Shrink the fixed bump support, once and for all, so that their phase variation is less than `pi/4` and their moduli remain above fixed fractions of their center values.

Then there exists a design constant

\[
\boxed{c_D^{prin}>0}
\tag{RL5}

such that

\[
\boxed{
|A_{D_j}^{prin}|
\ge c_D^{prin}
}
\tag{RL6}

uniformly for all input amplitudes in the chosen compact renewal set.

No multi-control determinant is needed for a reserve lane; this is a scalar nonvanishing estimate.

## 4. Strict source-window margin through the whole cell

After generation, a reserve child follows the unit-beta reduced slope

\[
z_D(t)=x-\delta+t.
\]

On the corrected cell interval

\[
0\le t\le T=2\delta=0.275,
\]

one has

\[
\boxed{
0.6404445\ldots
\le z_D(t)
\le0.9154445\ldots.
}
\tag{RL7}

Therefore its distance from the raw source endpoints `(1/2,3/2)` is bounded below by

\[
\boxed{
d_{src}>0.1404.}
\tag{RL8}

Thus every reserve child stays uniformly inside the same strict source cone throughout its transport to the reset region.

The phase/polarization data depend smoothly on this compact slope interval. Since the entrance difference projection has the fixed nonzero margin (RL3), the generated child polarization also remains in one compact admissible unit-beta polarization set.

## 5. Scale-uniform support geometry

The source formalization used in `beta21_corrected_finite_bank_three_collar_cell.md` keeps the broad label carrier independent of harmonic index. A descendant harmonic attached to one label therefore remains inside the same scale-normalized carrier family.

The reserve child is generated inside one fixed normalized overlap lobe and thereafter transported on that carrier without any designated later collision in its reserve corridor.

Consequently there are constants

\[
0<w_-<w_+<\infty
\]

independent of relay level such that the normalized support diameter/width of every retained reserve `D_j` lies in the same admissible interval

\[
\boxed{
w_-\le w(D_j)\le w_+.}
\tag{RL9}

After physical rescaling the lobe shrinks with the source chart exactly as every other primary packet; there is no scale-dependent normalized broadening.

This is the support property needed for reuse as one translated unit-beta control lobe at the next level.

## 6. Exact finite-circuit correction preserves nonvanishing

Add any fixed finite number of reserve lanes to the corrected exact cell. This changes only the finite design constant in the already proved nonzero/mean contraction estimates.

The exact designated/correction solution depends `C^1` on the finite reserve amplitudes, and the exact outgoing reserve coordinate satisfies

\[
\boxed{
A_{D_j}^{exact}
=A_{D_j}^{prin}+o(1)
}
\tag{RL10}

uniformly on the compact input amplitude set as the relay level tends to infinity.

Increase the starting level so that

\[
|o(1)|\le\frac12c_D^{prin}.
\]

Then

\[
\boxed{
|A_{D_j}^{exact}|
\ge
c_D:=\frac12c_D^{prin}>0.
}
\tag{RL11}

The same `C^1` smallness preserves the strict source-cone and support-width margins (RL8)--(RL9).

Hence every dirty reserve lane produces a reusable physical unit-beta lobe with uniform level-independent nondegeneracy constants.

## 7. Reuse as a translated control lobe

The entrance, strong-`H`, and terminal rank theorems require only a finite family of unit-beta lobes satisfying:

1. the correct character and principal polarization sector;
2. smooth source-admissible coefficients;
3. nonzero normalized amplitudes;
4. support centers that can be placed at distinct prescribed positions inside a finite collar;
5. fixed positive coupling/spectral margins.

The outgoing reserve children satisfy items 1--3 by Sections 3--6. Item 4 is supplied by the finite translated support-routing geometry at the next scale, while item 5 follows from the same compact normalized beta/slope geometry after canonical relabeling.

Therefore the output `D_j` is an admissible next-generation control lobe.

## 8. Consequence for the nine-lobe bank

For each dirty reserve lane `j=2,...,9`, there is a uniform constant

\[
\boxed{c_D>0}
\]

such that the exact outgoing child is nonzero and reusable.

The clean active child `D_1` already has stronger exact exit control from the four-control entrance theorem.

Hence all nine output lobes

\[
\boxed{D_1,\ldots,D_9}
\]

satisfy the same qualitative lobe admissibility conditions required for the next cell.

This closes the local nondegeneracy condition (LB11) and upgrades the nine-lobe circuit from a cardinality architecture to a **literal finite physical lobe renewal mechanism**, subject still to the global sparse-packing/exact-infinite-assembly problem.

No claim of a completed infinite unforced cascade or finite-time blowup is made here.
