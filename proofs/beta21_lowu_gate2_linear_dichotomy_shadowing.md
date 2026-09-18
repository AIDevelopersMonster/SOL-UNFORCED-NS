# Gate 2 linear exponential-dichotomy shadowing for the low-`u` inter-cell cocycle

**Status:** PROVED PRINCIPAL SPECTRAL-DICHOTOMY / SUMMABLE LINEAR SHADOWING THEOREM.  NONLINEAR EXACT FINITE-`S` INVARIANT COCYCLE AND REAL CHARACTERISTIC-MOMENT MATCHING REMAIN OPEN.

This note continues
`beta21_lowu_gate2_principal_fredholm_reduction.md`.

The exact local Gate 1 cell is not transversely attracting.  Nevertheless,
after the finitely many characteristic modes are separated, the limiting
inter-cell linearization has a genuine stable/unstable spectral dichotomy.
The canonical dyadic profile drift is already summable by
`beta21_lowu_dyadic_profile_resampling.md`.

Consequently the linear nonautonomous inter-cell equation has a bounded
shadowing solution.  The forward-unstable component is selected once in the
initial state by a convergent backward Green series.  This does not require
backward inversion of a parabolic high-frequency operator: only the bounded
inverse of the unstable orbit-modulation cocycle appears.

No nonlinear or global Navier--Stokes theorem is claimed here.

---

## 1. Catalyst multiplier: one center and an expanding complement

The catalyst limiting multiplier on its natural spectral circle is

\[
m_C(\rho_Ce^{i\phi})
=
\frac{e^{\lambda_C\rho_Ce^{i\phi}}}
{\rho_Ce^{i\phi}},
\]

with

\[
0<\rho_C<1,
\qquad
\lambda_C\rho_C=\log\rho_C<0.
\]

Therefore

\[
\log|m_C|
=
\log\rho_C(\cos\phi-1).
\tag{LD1}
\]

Hence

\[
\boxed{
|m_C|=1
\iff
\phi=0,
}
\tag{LD2}
\]

and

\[
\boxed{
|m_C|>1
\quad\text{for }\phi\ne0.
}
\tag{LD3}
\]

Fix a small spectral neighborhood `N_C` of the characteristic point.
On the compact complement,

\[
\boxed{
|m_C|\ge1+\gamma_C
}
\tag{LD4}
\]

for some `gamma_C>0`.

Thus, after the single catalyst characteristic coordinate is removed, the
remaining catalyst modulation spectrum is uniformly forward-unstable.

---

## 2. Parent multiplier: two centers, stable and unstable arcs

Write

\[
A_P:=\mu_P\rho_P
=
a+ib
=
1.814829007127034
-1.044351775683794,i.
\]

On the natural parent spectral circle,

\[
\log|m_P(\rho_Pe^{i\phi})|
=
\Re\left(A_P(e^{i\phi}-1)\right).
\tag{LD5}
\]

The unit-modulus equation is

\[
a(\cos\phi-1)-b\sin\phi=0.
\tag{LD6}
\]

It has exactly two solutions modulo `2pi`,

\[
\boxed{\phi_1=0}
\tag{LD7}
\]

and

\[
\boxed{
\phi_2
=
2\pi-2\arg\rho_P
=
1.044351775683794\ldots .
}
\tag{LD8}
\]

At both points the full multiplier is in fact equal to `1`; these are the
two parent characteristic roots already isolated in the Fredholm reduction.

Remove small disjoint neighborhoods `N_{P,1},N_{P,2}`.  The remaining
compact parent circle splits into stable and unstable arcs, and there is
`gamma_P>0` such that

\[
\boxed{
|m_P|\le1-\gamma_P
}
\tag{LD9}
\]

on the stable arcs and

\[
\boxed{
|m_P|\ge1+\gamma_P
}
\tag{LD10}
\]

on the unstable arcs.

Thus the parent analytic modulation system has a two-dimensional
characteristic block plus a uniformly hyperbolic complement.

---

## 3. Thin analytic annulus and Riesz splitting

The multipliers are analytic functions of the normalized shift spectral
variable.  By continuity, after taking a sufficiently thin analytic annulus
around the natural circle and sufficiently small characteristic
neighborhoods, the same strict estimates persist.

Functional calculus in the bilateral Wiener algebra therefore gives bounded
spectral projections

\[
\Pi^s,\qquad \Pi^c,\qquad \Pi^u,
\tag{LD11}
\]

where

- `Pi^c` is the finite characteristic block from the previous Fredholm
  theorem;
- `Pi^s` is the parent stable analytic bundle;
- `Pi^u` contains the catalyst complement and parent unstable bundle.

For the frozen principal map `A_*` there are constants

\[
K<\infty,
\qquad
0<\alpha<1,
\tag{LD12}
\]

such that

\[
\boxed{
\|A_*^n\Pi^s\|
\le K\alpha^n,
\qquad n\ge0,
}
\tag{LD13}
\]

and

\[
\boxed{
\|A_*^{-n}\Pi^u\|
\le K\alpha^n,
\qquad n\ge0.
}
\tag{LD14}
\]

The inverse in (LD14) is an inverse only on the unstable orbit-modulation
bundle, where the forward multiplier is bounded away from the unit circle.

---

## 4. Scale-dependent perturbation

Let `A_j` be the exact linearized normalized inter-cell map after:

1. exact local Gate 1 reset;
2. exact physical gap transport;
3. source normalization at the next scale;
4. tangent/profile normalization.

The branch already proves:

- inside one dyadic slab, the full designated transfer is uniformly
  near-identity over a sufficiently short logarithmic gap;
- at a dyadic boundary, the canonical tangent-Gaussian profile change is
  `O(n^-2)` in the common continuum profile norm;
- source/PDE corrections carry positive epsilon powers or action gaps.

Thus, after the principal frozen profile and the finite characteristic block
are extracted, the exact complement linearization has the form

\[
\boxed{
A_j=A_*+E_j,
}
\tag{LD15}
\]

with

\[
\boxed{
\|E_j\|\to0.
}
\tag{LD16}
\]

For all sufficiently late levels the perturbation is smaller than the
spectral gap in (LD13)--(LD14).  Standard roughness of exponential
dichotomies then yields scale-dependent projections

\[
\Pi_j^s,\qquad\Pi_j^u
\tag{LD17}
\]

and evolution operators `Phi(j,k)` satisfying

\[
\boxed{
\|\Phi(j,k)\Pi_k^s\|
\le K_1\alpha_1^{j-k},
\qquad j\ge k,
}
\tag{LD18}
\]

and

\[
\boxed{
\|\Phi(j,k)\Pi_k^u\|
\le K_1\alpha_1^{k-j},
\qquad j\le k,
}
\tag{LD19}
\]

for one `0<alpha_1<1`.

The finite characteristic block is kept separate and is not included in
this dichotomy claim.

---

## 5. Summable forcing from canonical profile drift

Let `d_j` denote the exact inter-cell inhomogeneous defect after canonical
profile normalization and after removing its characteristic projection.

The dyadic resampling theorem gives

\[
\|F_{b,n+1}-F_{b,n}\|
\le Cn^{-2}.
\tag{LD20}
\]

There are only finitely many near-one relay substeps per dyadic slab.  The
source-small transport, tail, mean and nonzero errors are dominated by
positive epsilon powers or action-gap factors and are summable after taking
the starting level sufficiently high.

Hence the analytic-complement defect obeys

\[
\boxed{
\sum_{j\ge j_0}\|d_j\|<\infty.
}
\tag{LD21}
\]

This is stronger than merely `d_j -> 0`.

---

## 6. Green operator for the stable/unstable complement

Consider the inhomogeneous complement recurrence

\[
e_{j+1}=A_je_j+d_j.
\tag{LD22}
\]

Define

\[
e_j^s
=
\sum_{k=j_0}^{j-1}
\Phi(j,k+1)\Pi_{k+1}^s d_k,
\tag{LD23}
\]

and

\[
e_j^u
=
-
\sum_{k=j}^{\infty}
\Phi(j,k+1)\Pi_{k+1}^u d_k.
\tag{LD24}
\]

The second series uses backward propagation only on the uniformly expanding
bundle, so (LD19) makes it a contraction.

By (LD18)--(LD21), both sums converge absolutely and

\[
\boxed{
\sup_{j\ge j_0}
\left(\|e_j^s\|+\|e_j^u\|\right)
\le
C_G
\sum_{k\ge j_0}\|d_k\|.
}
\tag{LD25}
\]

Moreover `e_j=e_j^s+e_j^u` solves (LD22).

Thus every summable complement forcing has one bounded shadowing solution
after the unstable initial coordinate is selected by the convergent Green
series.

---

## 7. Why this is not the backward-heat obstruction

The earlier backward-heat obstruction concerned attempts to pre-store future
high-frequency packet data by reversing a dissipative parabolic evolution.
That requires exponentially large earlier physical amplitudes.

Equation (LD24) is different.

1. The inverse is taken only on the orbit-modulation unstable bundle where
   the **forward inter-cell multiplier already has modulus strictly larger
   than one**.
2. Therefore the inverse multiplier has norm strictly smaller than one.
3. The forcing is summable.
4. The selected initial correction is bounded by (LD25), not exponentially
   large.
5. After analytic reconstruction it is a legitimate low-modulation
   correction of the initial Cauchy state.

Hence the linear shadowing selection does not by itself reintroduce hidden
future-time forcing or backward heat.

It does use the full future coefficient sequence to identify the one initial
shadowing coordinate, exactly as an ordinary stable-manifold construction
does.  Once selected, the subsequent PDE evolution is forward and
autonomous.

---

## 8. Characteristic block

The Green operator above solves only the hyperbolic analytic complement.

The remaining characteristic coordinates are the finite moments isolated in

`beta21_lowu_gate2_principal_fredholm_reduction.md`:

\[
\ell_1(C),
\qquad
\ell_1(P),
\qquad
\ell_{z_2}(P).
\tag{LD26}
\]

On the complexified positive-beta system this is one catalyst complex
coordinate and two parent complex coordinates.

Their physical real parameter/gauge ledger is still to be audited.  In
particular, this note does **not** assume that all three complex moments can
be set to zero independently by the four Gate 1 macroscopic parameters and
the two torus phases; the Gate 1 parameters already satisfy local reset
equations.

The correct next task is to derive the reduced finite-dimensional
nonautonomous characteristic map after the exact local Gate 1 solve and
determine its real rank.

---

## 9. Consequence for Gate 2

The infinite-dimensional part of the *linear* inter-cell shadowing problem
is now closed modulo standard persistence of the already-established
spectral gaps:

\[
\boxed{
\text{summable forcing}
+
\text{analytic complement dichotomy}
\Longrightarrow
\text{bounded exact linear shadowing correction}.
}
\tag{LD27}
\]

Gate 2 has therefore narrowed to:

1. the finite characteristic-coordinate dynamics/rank;
2. nonlinear persistence of the dichotomy/Green operator;
3. reconstruction as one physical Cauchy state;
4. global energy/smoothness summability.

The next theorem layer should be

`beta21_lowu_gate2_characteristic_reduced_map.md`.

No infinite cascade or singularity theorem is claimed here.
