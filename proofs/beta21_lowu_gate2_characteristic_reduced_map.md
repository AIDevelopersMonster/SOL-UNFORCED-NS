# Gate 2 characteristic reduced map and physical parameter ledger

**Status:** PROVED CHARACTERISTIC PARAMETER LEDGER / PRINCIPAL FULL-RANK CENTER CHART / COVARIANT CENTER-TRANSPORT REDUCTION.  NONLINEAR GLOBAL INVARIANT COCYCLE STILL OPEN.

This note closes the parameter-count ambiguity left by

- `beta21_lowu_gate2_principal_fredholm_reduction.md`, and
- `beta21_lowu_gate2_linear_dichotomy_shadowing.md`.

The principal Gate 2 cohomological operator has one catalyst and two parent
complex characteristic coordinates.  These are **not** to be killed by
reusing the four Gate 1 macroscopic parameters
`(kappa,theta,A_M,tau)`.

They are already represented by three genuine complex state coordinates
present in the exact Gate 1 construction:

1. the catalyst central-profile normalization;
2. the parent central-profile normalization;
3. the Gaussian gauge of the secondary parent tail resonance.

Thus the real characteristic block has six real dimensions and the incoming
Cauchy state already contains six independent real characteristic
coordinates.  The principal characteristic chart has full rank.

No infinite cascade is claimed here.

---

## 1. Characteristic block from the Fredholm theorem

The principal catalyst symbol has one simple characteristic root

\[
z_C=1.
\]

The parent symbol has two simple characteristic roots

\[
z_{P,1}=1,
\qquad
z_{P,2}
=
\frac{\bar\rho_P}{\rho_P}
=
e^{,i1.044351775683794\ldots}.
\]

Hence the complexified characteristic space is

\[
\boxed{
E^c
=
E_C\oplus E_{P,1}\oplus E_{P,2},
}
\tag{CR1}
\]

with

\[
\dim_{\mathbb C}E^c=3,
\qquad
\dim_{\mathbb R}E^c_{\rm phys}=6.
\tag{CR2}
\]

The physical real field is reconstructed by adding the negative-frequency
conjugates.  Therefore one complex coefficient in the positive-beta sector
is one legitimate pair of real Cauchy coordinates; no extra independent
negative-beta parameter is introduced.

---

## 2. Two central normalization coordinates already exist

The exact discrete central-profile theorem constructs sectorwise normalized
kernels

\[
f_{C,S},
\qquad
f_{P,S},
\]

after choosing one normalization functional per sector.

That theorem explicitly records that the two normalization constants are
not new root controls: they are the overall complex amplitudes/phases
already present in the designated Cauchy data.

Write these physical state coordinates as

\[
\boxed{
A_C\in\mathbb C,
\qquad
A_P\in\mathbb C.
}
\tag{CR3}
\]

Infinitesimally,

\[
\partial_{A_C}U_{des}
=
f_{C,S}
\]

lies in the catalyst characteristic direction, while

\[
\partial_{A_P}U_{des}
=
f_{P,S}
\]

lies in the canonical parent characteristic direction.

After choosing the Riesz coordinate functionals
`chi_C,chi_{P,1}` dual to these normalized kernels, rescale the
normalizations so that

\[
\boxed{
\chi_C(\partial_{A_C}U_{des})=1,
\qquad
\chi_{P,1}(\partial_{A_P}U_{des})=1.
}
\tag{CR4}
\]

Cross-sector pairings vanish at principal frozen level because beta one and
beta two are distinct orbit sectors.

Thus `A_C,A_P` give four independent real center coordinates.

---

## 3. The secondary parent resonance supplies the third complex coordinate

The finite-`S` tail-parametrix theorem isolates one secondary parent
resonance.  Its local normal form has a one-dimensional complex Gaussian
kernel and no cokernel.  The theorem fixes this kernel by one harmless
normalization, but it also states that the coefficient may equivalently be
retained as a finite-dimensional Lyapunov--Schmidt coordinate.

Denote this coefficient by

\[
\boxed{
G_P\in\mathbb C.
}
\tag{CR5}
\]

The corresponding tangent vector

\[
\partial_{G_P}U_{tail}
\]

is exactly the finite-`S` continuation of the second parent characteristic
mode `E_{P,2}`.

Choose the dual Riesz coordinate `chi_{P,2}` so that

\[
\boxed{
\chi_{P,2}(\partial_{G_P}U_{tail})=1.
}
\tag{CR6}
\]

This contributes the remaining two real characteristic degrees of freedom.

---

## 4. Principal characteristic Jacobian

Put

\[
\boxed{
\Xi
=
(A_C,A_P,G_P)\in\mathbb C^3.
}
\tag{CR7}
\]

Let

\[
\mathfrak C(U)
=
\bigl(
\chi_C(U),
\chi_{P,1}(U),
\chi_{P,2}(U)
\bigr).
\]

By (CR4), (CR6), and sector separation,

\[
\boxed{
D_\Xi\mathfrak C
=
I_3
}
\tag{CR8}
\]

at principal frozen level, after the harmless normalization choices above.

Therefore

\[
\boxed{
\det_{\mathbb R}
D_{(\Re\Xi,\Im\Xi)}
(\Re\mathfrak C,\Im\mathfrak C)
=1\ne0.
}
\tag{CR9}
\]

This is the desired six-real-dimensional characteristic rank.

It is a state-coordinate rank theorem, not a new control theorem.

---

## 5. Independence from the Gate 1 macroscopic parameter solve

The Gate 1 theorem uses

\[
p=(\kappa,\theta,A_M,\tau)
\tag{CR10}
\]

to solve the local dispersion/root-coupling/reset observables.

The characteristic coordinates (CR7) are different variables:

- `A_C,A_P` are the already-present overall complex
  profile normalizations/phases;
- `G_P` is the secondary parent Gaussian tail gauge.

The exact discrete-profile theorem explicitly leaves the macroscopic
parameters available after profile normalization, and the tail-parametrix
theorem explicitly identifies the secondary Gaussian coefficient as a
gauge/Lyapunov--Schmidt coordinate.

Hence the six real coordinates in `Xi` are not obtained by double-counting
the four Gate 1 parameters.

This removes the apparent `6 equations vs 4 parameters` obstruction.

---

## 6. Finite-`S` persistence

All central kernels, Riesz projections, tail gauges and exact PDE corrections
depend `C^1`-smoothly on the finite macroscopic parameter vector on a fixed
compact neighborhood.

The Gate 1 `C^1` transfer theorem gives only source-small/polynomially
controlled changes in these normalized coordinates.  Therefore

\[
\boxed{
D_\Xi\mathfrak C_S
=
I_3+o(1)
}
\tag{CR11}
\]

uniformly for sufficiently large `S`.

Consequently, after increasing the starting level,

\[
\boxed{
\left|
\det_{\mathbb R}
D_\Xi\mathfrak C_S
\right|
\ge\frac12.
}
\tag{CR12}
\]

Thus the full six-real-dimensional characteristic chart remains
nondegenerate at finite `S`.

---

## 7. One-step reduced characteristic map

Let

\[
\mathcal F_j
\]

denote exact physical gap transport followed by the exact local Gate 1 map
and normalization at the next stage.

Project the resulting full-state map to the characteristic chart:

\[
\boxed{
\Xi_{j+1}
=
\mathcal B_j\Xi_j
+b_j
+N_j(\Xi_j,W_j),
}
\tag{CR13}
\]

where

- `W_j` is the stable/unstable analytic complement;
- `B_j` is the exact linear characteristic transport matrix;
- `b_j` is the canonical profile/scale drift;
- `N_j` contains nonlinear and source-small coupling.

The characteristic-rank theorem proves that (CR13) is a genuine local
coordinate representation of the physical state, not an underdetermined
compatibility condition.

The existing dyadic profile theorem gives a summable canonical contribution

\[
\boxed{
\sum_j\|b_j^{dyad}\|<\infty.
}
\tag{CR14}
\]

The source-small correction contribution is likewise summable after a
sufficiently high starting level.

---

## 8. Covariant characteristic frame removes the harmless gap rotation

Inside one dyadic slab the exact normalized gap transport is generated by a
bounded finite-dimensional characteristic matrix.  Its `O(delta)`
near-identity part should not be counted repeatedly as an error.

Let `Q_j` solve the exact finite-dimensional transport equation on the
characteristic bundle,

\[
\boxed{
Q_{j+1}
=
\mathcal B_j^{gap}Q_j,
\qquad
Q_{j_0}=I.
}
\tag{CR15}
\]

Define covariant characteristic coordinates

\[
\boxed{
\widehat\Xi_j
=
Q_j^{-1}\Xi_j.
}
\tag{CR16}
\]

Then the pure gap transport is removed exactly from the coordinate
recurrence.  What remains is only:

1. the local reset/normalization mismatch relative to the transported
   characteristic frame;
2. the summable dyadic canonical-profile change;
3. source-small finite-`S` corrections;
4. coupling to the already-shadowed analytic complement.

Thus the reduced center equation has the schematic form

\[
\boxed{
\widehat\Xi_{j+1}
=
\widehat\Xi_j
+\widehat b_j
+\widehat N_j,
}
\tag{CR17}
\]

with

\[
\sum_j\|\widehat b_j\|<\infty
\tag{CR18}
\]

at linear canonical level.

This is the correct center formulation.  A fixed near-one gap rotation is
parallel transport, not a cumulative defect.

---

## 9. Consequence

Gate 2 no longer has a parameter-count obstruction.

The full linearized inter-cell problem splits into

\[
\boxed{
\text{finite }\mathbb C^3\text{ characteristic coordinates}
\oplus
\text{analytic hyperbolic complement}.
}
\tag{CR19}
\]

The hyperbolic complement has the Green shadowing operator from
`beta21_lowu_gate2_linear_dichotomy_shadowing.md`.

The characteristic block has a full-rank physical Cauchy coordinate chart
`Xi=(A_C,A_P,G_P)`, and after exact parallel transport its canonical forcing
is summable.

The remaining theorem is nonlinear:

> construct a bounded/convergent solution of the coupled nonautonomous map
> (CR17) together with the analytic Green correction, and prove that the
> resulting infinite sequence is reconstructed from one smooth finite-energy
> Cauchy state.

The next file should be

`beta21_lowu_gate2_nonlinear_invariant_cocycle.md`.

No infinite cascade or singularity claim is made here.
