# Gate 2 exact finite-dimensional characteristic connection

**Status:** PROVED REDUCTION TO A SMOOTH FINITE-DIMENSIONAL CHARACTERISTIC ODE WITH SUMMABLE DISCRETIZATION DEFECT.  EXISTENCE OF A GLOBAL BOUNDED NONZERO CHARACTERISTIC ORBIT REMAINS OPEN.

This note combines the exact Gate 1 characteristic family with the new
constant-fast-cell source schedule.

It is important not to assume that the characteristic amplitudes are
automatically bounded over infinitely many cells.  The correct statement is
that the exact physical inter-cell transport induces a finite-dimensional
connection on the six-real-dimensional characteristic bundle.

Following that connection removes the full first-order one-cell drift.  The
remaining discrete defect is quadratic in the logarithmic cell step and is
therefore summable.

Thus Gate 2 is reduced to one explicit finite-dimensional dynamical question:

> does the characteristic connection admit a bounded nonzero forward orbit
> remaining inside the exact Gate 1 characteristic chart?

If the answer is no for every nonzero relay state, the global cascade line
stops here.  No bounded-orbit claim is made in this note.

---

## 1. Exact local characteristic bundle

By

`beta21_lowu_gate1_characteristic_family.md`

there is, for every sufficiently large `S`, an exact local fixed-state
family

\[
\boxed{
\mathscr S_S(p_{slow},\Xi),
\qquad
\Xi=(A_C,A_P,G_P)\in\mathbb C^3,
}
\tag{EC1}
\]

on one fixed small compact characteristic chart `K_Xi`.

The Gate 1 macroscopic variables

\[
(\kappa,\theta,A_M,\tau)
\]

have already been solved as smooth functions of `(p_slow,Xi)`.

By

`beta21_lowu_gate2_C2_local_section.md`,

\[
\boxed{
\mathscr S_S
\text{ is uniformly }C^2
}
\tag{EC2}
\]

at the fixed finite derivative order required below, modulo only harmless
fixed powers of `S` multiplying source-small terms.

Its characteristic differential

\[
D_\Xi\mathscr S_S
\]

has full real rank six uniformly for large `S`.

---

## 2. Exact normalized physical inter-cell map

Let

\[
\mathcal G_{\Delta\sigma,S,p}
\]

denote the exact physical evolution from the outgoing section of one local
Gate 1 cell to the incoming section of the next cell, including

1. the actual physical Navier--Stokes evolution on the allocated fixed-fast
   buffer;
2. exact source chart/cover rebase;
3. exact `Q^{-A(h)}` velocity normalization;
4. relabelling to the next low-`u` characteristic chart.

The exact scale factor in item 3 is neutral by

`beta21_lowu_gate2_natural_rebase_characteristic_invariance.md`.

The low-`u` cell/buffer has uniformly bounded source fast length by

`beta21_lowu_source_slot_fast_length_bridge.md`

and

`beta21_lowu_constant_fast_cell_sigma_schedule.md`.

On one fixed compact source chart, ordinary local wellposedness and the
already-used source coefficient calculus therefore give `C^2` dependence
of

\[
(\Delta\sigma,p,U)
\longmapsto
\mathcal G_{\Delta\sigma,S,p}(U)
\tag{EC3}
\]

for small `Delta sigma`, uniformly at the fixed normalized derivative
order used by the branch.

At zero gap,

\[
\boxed{
\mathcal G_{0,S,p}=I.
}
\tag{EC4}
\]

Define the exact normalized gap generator

\[
\boxed{
\mathcal X_{S,p}(U)
:=
\left.
\partial_{\Delta\sigma}
\mathcal G_{\Delta\sigma,S,p}(U)
\right|_{\Delta\sigma=0}.
}
\tag{EC5}
\]

The pure band-scale similarity part has zero real characteristic drift by
the exact natural-rebase theorem; it is already removed in (EC5).

---

## 3. Slow-spine derivative of the exact Gate 1 family

Let

\[
p_{slow}=p_{slow}(\sigma)
\]

be the exact trapped-spine slow profile.

Define

\[
\mathscr S_S(\sigma,\Xi)
:=
\mathscr S_S(p_{slow}(\sigma),\Xi).
\tag{EC6}
\]

Then

\[
\partial_\sigma
\mathscr S_S(\sigma,\Xi)
\tag{EC7}
\]

exists and is continuous, with one further derivative uniformly controlled
on compact characteristic subsets.

The difference

\[
\boxed{
\mathcal D_S(\sigma,\Xi)
:=
\mathcal X_{S,p(\sigma)}
\bigl(\mathscr S_S(\sigma,\Xi)\bigr)
-
\partial_\sigma\mathscr S_S(\sigma,\Xi)
}
\tag{EC8}
\]

is the genuine first-order mismatch between physical normalized transport
and the motion of the exact local fixed-state section.

All source scale similarity drift has already cancelled before (EC8).

---

## 4. Characteristic projection and connection

Let

\[
\mathfrak C_{S,\sigma}
\]

be the finite characteristic coordinate map given by the three Riesz
functionals from

`beta21_lowu_gate2_characteristic_reduced_map.md`.

On the characteristic tangent bundle,

\[
D_\Xi
\bigl(
\mathfrak C_{S,\sigma}
\circ
\mathscr S_S(\sigma,\cdot)
\bigr)
\tag{EC9}
\]

is a uniformly invertible real `6 x 6` matrix.

Define the characteristic connection vector field by

\[
\boxed{
\mathcal A_{c,S}(\sigma,\Xi)
:=
\left[
D_\Xi
(\mathfrak C_{S,\sigma}\circ\mathscr S_S)
\right]^{-1}
\,
\mathfrak C_{S,\sigma}
\bigl(
\mathcal D_S(\sigma,\Xi)
\bigr).
}
\tag{EC10}
\]

This is a smooth finite-dimensional vector field on every compact subset of
the characteristic chart.

The exact characteristic parallel-transport equation is

\[
\boxed{
\frac{d\Xi}{d\sigma}
=
\mathcal A_{c,S}(\sigma,\Xi).
}
\tag{EC11}
\]

No sign or boundedness property of `A_c,S` is assumed here.

---

## 5. Complement part of the first-order mismatch

By construction, after inserting (EC10),

\[
\mathcal R_S(\sigma,\Xi)
:=
\mathcal D_S(\sigma,\Xi)
-
D_\Xi\mathscr S_S(\sigma,\Xi)
\mathcal A_{c,S}(\sigma,\Xi)
\tag{EC12}
\]

has zero characteristic projection:

\[
\boxed{
\mathfrak C_{S,\sigma}
\bigl(
\mathcal R_S(\sigma,\Xi)
\bigr)
=0.
}
\tag{EC13}
\]

Therefore `R_S` lies in the analytic hyperbolic/Fredholm complement already
handled by

- `beta21_lowu_gate2_principal_fredholm_reduction.md`, and
- `beta21_lowu_gate2_linear_dichotomy_shadowing.md`.

At first order, no unresolved infinite-dimensional center component remains.

---

## 6. One-step Taylor expansion

Let `Xi(sigma)` solve (EC11) while remaining in a fixed compact subchart.
Over one low-`u` cell step

\[
\Delta\sigma_j
=
\Lambda\varepsilon_j,
\]

Taylor expansion of the exact physical gap map and the exact local section
gives

\[
\begin{aligned}
&
\mathcal G_{\Delta\sigma_j,S_j,p_j}
\left(
\mathscr S_{S_j}(\sigma_j,\Xi_j)
\right)
-
\mathscr S_{S_{j+1}}
\left(
\sigma_{j+1},\Xi(\sigma_{j+1})
\right)
\\
&=
\Delta\sigma_j\,
\mathcal R_{S_j}(\sigma_j,\Xi_j)
+
O((\Delta\sigma_j)^2)
+
d_j^{dyad}
+
d_j^{src}.
\end{aligned}
\tag{EC14}
\]

Here

- `d_j^dyad` is the already-proved canonical dyadic resampling defect,
  `O(n^{-2})`;
- `d_j^src` carries positive epsilon powers and/or fixed action gaps;
- finite-`S` local monodromy is included in the exact section/gap generator
  rather than treated as a summable error.

The characteristic projection of the first-order term is zero by (EC13).

Hence the **characteristic** one-step defect is

\[
\boxed{
d_{j,c}
=
O((\Delta\sigma_j)^2)
+
\Pi^c d_j^{dyad}
+
\Pi^c d_j^{src}.
}
\tag{EC15}
\]

By the constant-fast schedule,

\[
\sum_j(\Delta\sigma_j)^2<\infty.
\tag{EC16}
\]

The dyadic term is summable and the source-small term remains summable after
a sufficiently late starting level in every branch estimate used here.

Thus

\[
\boxed{
\sum_j\|d_{j,c}\|<\infty
}
\tag{EC17}
\]

provided the characteristic ODE solution stays in the fixed compact Gate 1
chart.

---

## 7. Analytic complement correction

The complement first-order term in (EC14) is not required to be summable
before inversion.  It is a small near-identity forcing in the hyperbolic
bundle.

Use the exact scale-dependent exponential dichotomy and Green operator.
The complement correction is obtained from the stable-past / unstable-future
Lyapunov--Perron sum.

After the characteristic first-order component has been removed by (EC11),
all remaining nonlinear return cycles contain one of the already-proved
small factors:

- `Delta sigma_j`;
- a positive epsilon power;
- a fixed action gap;
- the `O(S^{-1/2})` central/tail commutator.

This is the correct infinite-dimensional complement equation for the later
nonlinear cocycle theorem.

---

## 8. Exact Gate 2 kill criterion

The whole infinite-dimensional Gate 2 problem has now been reduced to a
finite-dimensional forward ODE.

The exact remaining question is:

\[
\boxed{
\text{Does (EC11) admit a nonzero forward solution }
\Xi(\sigma)
\text{ that remains in one compact Gate 1 chart for all }
\sigma\ge\sigma_0?
}
\tag{EC18}
\]

If yes, then the characteristic forcing after parallel transport is
summable and the analytic complement can be shadowed.

If every nonzero relay solution of (EC11) leaves every admissible Gate 1
chart (for example by unavoidable positive real exponential growth), the
infinite cascade architecture fails at Gate 2 even though Gate 1 remains
valid.

This is now a precise finite-dimensional kill criterion, not an
infinite-dimensional ambiguity.

---

## 9. What is proved

1. The exact physical inter-cell map induces a well-defined smooth
   six-real-dimensional characteristic connection.
2. Following that connection removes the full first-order characteristic
   mismatch.
3. The remaining characteristic discretization defect is quadratic in
   `Delta sigma` and hence summable on the constant-fast schedule.
4. All first-order non-characteristic mismatch lies in the already-audited
   analytic hyperbolic complement.

### Still open

1. Explicit evaluation / structural sign analysis of `A_c,S`.
2. A bounded nonzero global characteristic orbit.
3. Nonlinear Lyapunov--Perron coupling to the analytic complement.
4. Reconstruction of one smooth finite-energy Cauchy state.
5. Any infinite cascade or singularity theorem.

The next file should be

`beta21_lowu_gate2_characteristic_connection_audit.md`

and must attack (EC18) directly.
