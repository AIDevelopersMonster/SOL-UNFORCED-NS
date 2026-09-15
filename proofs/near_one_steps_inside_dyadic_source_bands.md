# Near-one relay steps inside dyadic source bands

**Status:** PROVED GEOMETRIC/CHART-COMPATIBILITY THEOREM. The corrected cross-scale theorem uses a fixed physical shrink ratio `vartheta` sufficiently close to one, whereas the source primary labeling uses dyadic reference bands `Q_n=2^{-n}`. These two discretizations are compatible: finitely many near-one physical relay steps fit inside each dyadic slab, and the exact source chart-change identities identify all of them with one common physical field. No new independent packet family is required merely because a relay step does not land on a dyadic reference value.

This theorem concerns physical/chart packing only. It does not by itself close support-bank or control-profile renewal.

## 1. Two scale sequences

The source dyadic reference scales are

\[
Q_n=2^{-n}.
\]

Fix one corrected relay shrink factor

\[
\vartheta\in(\vartheta_*,1)
\]

from `beta21_corrected_two_channel_small_log_transfer.md`, and define

\[
q_j=q_0\vartheta^j.
\]

Then both sequences decrease to zero.

## 2. Uniformly finite number of relay steps per dyadic slab

A dyadic slab is

\[
[Q_{n+1},Q_n]=[Q_n/2,Q_n].
\]

One near-one relay step changes logarithmic scale by

\[
L_\vartheta=\log(1/\vartheta)>0,
\]

whereas one dyadic slab has logarithmic width

\[
\log 2.
\]

Therefore the number of relay centers that can lie in any one dyadic slab is bounded by the fixed integer

\[
\boxed{
N_\vartheta
:=
1+\left\lceil\frac{\log2}{\log(1/\vartheta)}\right\rceil.
}
\tag{DB1}

In particular this bound is independent of `n`.

Thus a near-one cascade does not require infinitely many labels inside a single source band; it requires only a fixed finite number of relay substeps per dyadic level.

## 3. Exact source chart changes are defined for arbitrary positive scales

The source formalization `PhysicalParticularWave.lean` defines

\[
\operatorname{chartChange}(h,Q,Q_r,\mathrm{gap})
\]

and the corresponding cylinder change for arbitrary positive real scales `Q,Q_r`, not only for dyadic values.

The exact identity `cylinderChange_graph` states that the physical graph at scale `Q` is carried to the physical graph at scale `Q_r` by the chart change, with the expected radial, axial and temporal rescalings. The identities are algebraic consequences of the source similarity graph and do not require `Q/Q_r=2^k`.

Therefore, inside a fixed dyadic reference slab, every physical relay center

\[
q\in[Q_{n+1},Q_n]
\]

may be represented in the same reference construction by conjugating through the exact continuous scale change from `Q_n` to `q`.

## 4. Native covering refinement remains discrete and bounded

The torus covering index remains the source's discrete native index. The physical relay substeps do not require a new covering power at each near-one physical scale.

Within one dyadic slab the same native reference label is retained, while the continuous physical scale parameter is changed by the exact chart map. At the next dyadic boundary, the source's already-proved band/cover covariance changes the reference band and native covering index.

Hence the two operations are separated:

- continuous `q` motion inside one dyadic slab;
- one discrete source band/refinement change at the dyadic boundary.

No inconsistency arises from using a near-one physical relay ratio together with dyadic source labeling.

## 5. Temporal packing inside a physical scale gap

The source phase geometry gives the normalized temporal direction

\[
e_V-\varepsilon_n e_T,
\qquad
\varepsilon_n=Q_n^h,
\]

and `ChartScales.timeCoefficient` satisfies

\[
c_n\asymp S_n^{-1},
\qquad S_n=n^2,
\]

while the pulse length obeys

\[
c_nL_n=2r_0.
\]

Thus a fixed normalized active-cell width occupies physical time

\[
\boxed{
\Delta t_n^{cell}\le C Q_n^{1+h}S_n.
}
\tag{DB2}

For a near-one relay step the physical scale/time separation along the trapped spine is of order

\[
\Delta t_n^{gap}\asymp(1-\vartheta)Q_n.
\]

Consequently

\[
\boxed{
\frac{\Delta t_n^{cell}}{\Delta t_n^{gap}}
\le
\frac{C}{1-\vartheta}Q_n^hS_n
\longrightarrow0.
}
\tag{DB3}

Thus, after increasing the starting level, all relay cells in every dyadic slab can be placed with pairwise disjoint active time collars and positive transport gaps.

The fixed multiplicity bound (DB1) means only a fixed finite separation/coloring cost is added in each slab.

## 6. Compatibility with the trapped spine

`trapped_material_characteristic.md` gives an exact background material spine satisfying

\[
q(\sigma)\asymp e^{-\sigma},
\qquad
\sigma=-\log(1-t).
\]

Hence every prescribed sufficiently small `q_j` is crossed once up to the fixed comparability constants of the trapped spine. The source cone margins are uniform on the compact trapped rectangle.

Combining this with (DB2)--(DB3), the infinite sequence of near-one relay centers can be placed along the same physical spine and accumulates only at the terminal physical time.

## 7. Consequence

The discretization mismatch

\[
\text{near-one relay ratio}
\quad\text{vs}\quad
\text{dyadic source labels}
\]

is not a global obstruction.

The corrected programme may use a fixed `vartheta` sufficiently close to one for two-channel transfer while retaining the source's dyadic reference hierarchy. A uniformly finite number of physical relay steps is inserted into each dyadic slab, with exact continuous chart conjugation inside the slab and the standard source band change at its boundary.

## 8. Remaining global frontier

After this theorem and `beta21_two_copy_catalyst_bank_renewal.md`, the unresolved support-state issue is no longer dyadic packing or catalyst-cardinality growth. It is the autonomous renewal/realization of the finite localized **control-profile bank** used by the exact active gate Jacobians.

No infinite unforced Navier--Stokes cascade or blowup theorem is claimed here.
