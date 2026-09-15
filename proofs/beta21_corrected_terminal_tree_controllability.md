# Rooted-tree controllability reduction for the corrected non-turning terminal graph

**Status:** PROVED STRUCTURAL / TREE-TRUNCATED CONTROLLABILITY REDUCTION FOR THE CORRECTED NON-TURNING CANDIDATE. The full physical terminal graph still contains off-tree quadratic couplings, so this note does **not** yet prove the exact terminal gate. It proves that the finite reachable promoted set has no intrinsic rank obstruction: after choosing one nonzero source-matched parent edge for every reachable state, the resulting rooted finite system is single-input controllable because its full-symbol diagonal rates are simple.

The remaining sharp obligation is now only to realize a profile/support homotopy in which the selected tree response stays `O(1)` while all nonselected off-tree responses are a small perturbation, or else to audit the determinant of the complete finite operator directly.

## 1. Working point and finite reachable set

Use the corrected non-turning candidate from `beta21_corrected_nonturning_compact_cell_reduction.md`:

\[
 u=2.5,
 \qquad
 \delta=0.1375,
\]

\[
 x=0.77794450260672482712680064619405\ldots,
\]

and the reset boundary

\[
T=2\delta=0.275.
\]

The boundary unit-beta slopes are

\[
z_D(T)=x+\delta,
\qquad
z_C^{old}(T)=x+3\delta.
\]

The renewed parent target action is

\[
A_*:=\mathcal E_{2,2.5}(x).
\]

Run the reachable source-action dynamic programme from the real seed characters

\[
\pm D,\qquad \pm C,
\]

with the rules:

1. combine only two **distinct signed characters** at a principal quadratic step;
2. assign the child source action as the sum of the parent actions;
3. retain a child only while its action is at least `A_*`;
4. identify conjugate pairs at the output.

For the present candidate the resulting conservative reachable upper graph contains

\[
\boxed{44}
\tag{TC1}
\]

conjugacy classes, one of which is the retained outgoing catalyst `D` itself.

Thus the promoted contaminant/target output space has dimension at most

\[
\boxed{43}
\tag{TC2}
\]

after removing the prescribed `D` coordinate.

This is an upper graph: further polarization zeros can only reduce it.

## 2. A source-matched rooted spanning arborescence

The dynamic programme records, for every non-seed reachable character `K`, one parent decomposition

\[
K=K_1+K_2
\tag{TC3}
\]

with `K_1 != K_2` and with both parents appearing at strictly earlier generation depth.

Choose one such decomposition for every retained state. The resulting directed graph is a rooted acyclic spanning graph over the seed family. Because `D` is treated as a fixed nonzero background channel, every non-`D` state in the selected graph has a genealogy containing at least one `C` or `C^*` leaf.

Hence scaling a localized old-catalyst control packet changes the selected source monomial for every controlled state. There is no state in the 43-dimensional terminal output block whose selected tree monomial is independent of the `C` control.

The selected edges are **source matched**: no direct homogeneous pulse is being enlarged above its natural source envelope. Each descendant is driven by the actual quadratic product of already present parent packets at its promoted leaf action.

## 3. Full-symbol diagonal rates

For a positive-beta character

\[
K=mD+nC,
\qquad
\beta_K=m+n>0,
\]

its boundary reduced slope is

\[
\xi_K
=\frac{m z_D(T)+n z_C^{old}(T)}{m+n}.
\tag{TC4}
\]

Use the exact frozen principal rate

\[
\Gamma_K
=
\frac{1}{\sqrt{1+u^2\xi_K^2}}
-\beta_K^2
\frac{1+u^2\xi_K^2}{(1+u^2)^{3/2}}.
\tag{TC5}
\]

For beta-zero characters use the exact purely viscous diagonal rate determined by the nonzero radial normal.

Direct evaluation on all 44 reachable conjugacy classes gives pairwise distinct rates. The smallest pairwise separation is approximately

\[
\boxed{
\delta_{spec}^{term}
\approx1.40167\times10^{-2}>0.
}
\tag{TC6}
\]

Thus the terminal full-symbol diagonal has simple spectrum on the entire reachable promoted graph.

This numerical value is a reproducibility certificate, not yet outward-rounded interval arithmetic.

## 4. Rooted-tree PBH lemma

Consider a finite directed rooted tree with vertices ordered topologically from the root. Let

\[
A=\operatorname{diag}(\lambda_1,\ldots,\lambda_N)+L,
\]

where `L` contains one nonzero directed parent-to-child coefficient for each non-root vertex and is strictly lower triangular in the topological order. Let

\[
B=e_1
\]

inject at the root. Assume

\[
\lambda_i\ne\lambda_j
\qquad(i\ne j).
\tag{TC7}
\]

Then `(A,B)` is controllable.

### Proof

Let `w` be a left eigenvector of `A` with eigenvalue `lambda_j`. Because the diagonal is simple and the graph is rooted, solve the transpose eigenvector equation recursively backward along the unique selected root-to-`j` path. The `j`th component is nonzero. Every selected edge coefficient on the path is nonzero and every denominator

\[
\lambda_j-\lambda_i
\]

is nonzero by (TC7). Therefore the root component `w_1` is a nonzero product of edge coefficients divided by nonzero spectral differences. Hence

\[
w\cdot B=w_1\ne0.
\]

PBH gives controllability. `□`

The same conclusion holds for a rooted arborescence embedded in a larger lower-triangular DAG if only the selected tree edges are retained.

## 5. Application to the terminal promoted graph

Assume every selected parent edge from Section 2 has nonzero principal Leray projection. Let `A_tree` be the frozen full-symbol operator formed by:

- the exact diagonal rates of all controlled terminal characters;
- only the selected source-matched tree edges;
- the fixed nonzero background amplitudes needed on those edges.

Let `B_C` denote the first localized old-`C` control direction. After adjoining the direct `C` coordinate as the root, the selected graph is rooted at that control.

By (TC6) and the rooted-tree lemma,

\[
\boxed{
(A_{tree},B_C)
\text{ is controllable.}
}
\tag{TC8}
\]

Consequently 43 suitably translated smooth copies of the same admissible catalyst-control profile have a full-rank generalized exponential/Vandermonde response for the tree-truncated finite operator.

There is therefore **no finite-dimensional rank obstruction intrinsic to the corrected terminal lattice.**

## 6. What has not yet been proved

The physical Navier--Stokes finite block is not exactly `A_tree`. It also contains every other leading quadratic coupling between promoted characters that is allowed by support and polarization.

Adding arbitrary `O(1)` off-tree entries to a controllable pair can, at isolated coefficient values, destroy controllability. Hence structural controllability alone is not enough for the exact gate theorem.

The remaining task is sharply one of the following:

### Route A: support/profile homotopy

Construct a finite translated-profile geometry depending on a parameter `eta` such that

\[
A_{full}(\eta)
=A_{tree}+R(\eta),
\qquad
\|R(\eta)\|\to0,
\tag{TC9}
\]

while every selected tree edge and its action-normalized response remain uniformly nonzero. Then controllability persists by openness.

### Route B: complete determinant audit

Compute the entire frozen finite operator with all physically nonzero promoted couplings and verify directly that

\[
\operatorname{rank}
[B,AB,\ldots,A^{N-1}B]=N.
\tag{TC10}
\]

After either route, the existing parameter-dependent exact zero-residual machinery can transfer the finite rank to a `C^1` exact terminal gate.

## 7. Programme frontier

The sequence of obstructions has now narrowed the local active-cell problem to

\[
\boxed{
\textbf{off-tree control of one finite terminal promoted graph.}
}
\tag{TC11}
\]

The former infinite turning-face obstruction is gone; the higher-order clock-reset family is unnecessary for the current preferred route; and the remaining issue is no longer action finiteness or tree-level rank.

No full reset-cell or unforced Navier--Stokes blowup theorem is claimed.
