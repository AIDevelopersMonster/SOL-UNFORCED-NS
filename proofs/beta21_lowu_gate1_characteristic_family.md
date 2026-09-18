# Gate 1 characteristic family: exact local resets with free center normalizations

**Status:** PROVED PARAMETER-DEPENDENT EXTENSION OF THE EXACT GATE 1 THEOREM TO A SMALL COMPACT CHARACTERISTIC CHART.

This note fills a parameter-ledger gap needed by Gate 2.

The published Gate 1 theorem fixed one normalization in each central
tangent-Gaussian sector and fixed the secondary-parent Gaussian tail gauge.
Gate 2 needs to know whether the corresponding coefficients are genuine
nearby Cauchy-state coordinates or whether they were consumed by the local
reset equations.

They are genuine state coordinates.

More precisely, after restricting to a sufficiently small compact
neighborhood of the canonical state, the exact Gate 1 contraction and
finite-dimensional implicit-function theorem are uniform in

\[
\boxed{
\Xi=(A_C,A_P,G_P)\in\mathbb C^3,
}
\tag{GF1}
\]

where

- `A_C` is the catalyst central-profile complex normalization;
- `A_P` is the parent central-profile complex normalization;
- `G_P` is the secondary-parent Gaussian resonant-tail gauge.

For each such `Xi` and every sufficiently large `S`, the four
macroscopic Gate 1 variables

\[
p=(\kappa,\theta,A_M,\tau)
\]

can be chosen smoothly as `p=p_S(Xi)` so that the complete local
core+tail state is an exact zero-residual one-cell reset.

This theorem is local in `Xi`.  It does not yet construct an inter-cell
cocycle.

---

## 1. Central normalizations are genuine Cauchy coordinates

The exact discrete central-profile theorem constructs normalized kernels

\[
f_{C,S},\qquad f_{P,S}
\]

with one normalization functional per sector.

The theorem explicitly records that the normalization constants represent
the overall profile amplitudes/phases already present in the designated
Cauchy data; they are not additional root controls.

Thus the designated central state may be written

\[
\boxed{
U_{core,S}(A_C,A_P)
=
A_C f_{C,S}
+
A_P f_{P,S}
}
\tag{GF2}
\]

together with the reality-determined negative-frequency conjugates.

Fix a small compact product annulus

\[
K_{CP}
\Subset
(\mathbb C\setminus\{0\})^2
\tag{GF3}
\]

around the canonical pair.  All designated amplitudes remain uniformly
bounded above and away from zero on `K_CP`.

The source bilinear estimates used in Gate 1 are uniform on every such fixed
compact amplitude set: Navier--Stokes is quadratic and the source constants
are chosen independently of orbit cardinality.

Hence varying `A_C,A_P` in `K_CP` does not change any epsilon/action
exponent or invertibility margin.

---

## 2. Secondary parent Gaussian gauge is a genuine finite coordinate

The finite-`S` tail-parametrix theorem isolates one secondary parent
resonant window.  Its leading model

\[
L_+=2\partial_y+a_0y
\]

has a one-dimensional complex Gaussian kernel and no cokernel.

The local right inverse becomes unique after fixing one normalization, but
the same theorem explicitly permits retaining the kernel coefficient as a
finite-dimensional Lyapunov--Schmidt coordinate.

Write that coefficient as

\[
\boxed{G_P\in\mathbb C.}
\tag{GF4}
\]

Because the secondary resonant window lies at a strictly negative physical
action,

\[
H_2(z_0)<0,
\]

the physical field associated with a bounded `G_P` carries an
`e^{-c_{res}S}` action factor.  Therefore varying `G_P` in any fixed
compact disk

\[
|G_P-G_{P,*}|\le r_G
\tag{GF5}
\]

changes the Gate 1 contraction only by terms already inside the
source/action-small radius.

Thus `G_P` is a genuine bounded Cauchy/tail coordinate, not a solvability
condition.

---

## 3. Uniform infinite-dimensional contraction over `Xi`

Put

\[
K_\Xi:=K_{CP}\times\overline{B_{r_G}(G_{P,*})}.
\]

For fixed macroscopic `p` and characteristic coordinate `Xi`, write the
exact tail/mean/nonzero correction equation as

\[
\boxed{
W=\mathfrak T_S(p,\Xi;W).
}
\tag{GF6}
\]

The Gate 1 proof uses only:

1. bounded designated amplitudes on a fixed compact set;
2. fixed action gaps;
3. the polynomially bounded tail inverse;
4. source-positive epsilon powers;
5. the coupled return-cycle small factors.

All five are uniform on `K_\Xi`.  Hence, after increasing the starting
level once,

\[
\boxed{
\sup_{p,\Xi,W}
\|D_W\mathfrak T_S(p,\Xi;W)\|
\le q_S<\frac12
}
\tag{GF7}
\]

and

\[
\boxed{
\|\mathfrak T_S(p,\Xi;0)\|
\le
S^A\varepsilon^{a_*}+S^Ae^{-cS}
}
\tag{GF8}
\]

uniformly on the same compact set.

Therefore Banach's theorem gives a unique exact correction

\[
\boxed{
W_S(p,\Xi)
}
\tag{GF9}
\]

for every `(p,Xi)` in the fixed neighborhood.

Since all source coefficient maps and the tail parametrix are smooth in
these finite coordinates, the parameter-dependent contraction theorem gives
smooth finite-order dependence of `W_S` on `(p,Xi)`.  The first two
orders are used later.

---

## 4. Principal reset observables do not consume `Xi`

Let

\[
\mathcal O_S^{full}(p,\Xi)
\]

denote the four real macroscopic Gate 1 observables after inserting the
exact correction:

- the catalyst scalar reset/dispersion condition;
- the two real parent reset/dispersion conditions;
- the single-root catalyst/parent coupling-ratio condition.

At principal level the equations determine

\[
(\kappa,\theta,A_M,\tau)
\]

through the already-proved transverse dispersion/root-coupling map.

The overall central amplitudes `A_C,A_P` multiply solutions of the
homogeneous orbit fixed equation.  They do not enter the principal
multiplier equations.  Likewise the secondary Gaussian gauge lies in a
physical action-subcritical resonant tail and does not enter the principal
macroscopic reset equations.

Thus

\[
\boxed{
\mathcal O_0(p,\Xi)=\mathcal O_0(p)
}
\tag{GF10}
\]

and

\[
\boxed{
D_p\mathcal O_0(p_*)
\text{ is invertible uniformly, independently of }\Xi.
}
\tag{GF11}
\]

The exact PDE/tail correction introduces only source-small
`Xi`-dependence.

---

## 5. Uniform implicit-function theorem

The Gate 1 `C^1` transfer estimates extend uniformly over `K_\Xi`:

\[
\boxed{
\sup_{\Xi\in K_\Xi}
\|
\mathcal O_S^{full}(p,\Xi)-\mathcal O_0(p)
\|_{C_p^1}
\to0.
}
\tag{GF12}
\]

Hence the quantitative implicit-function theorem, with `Xi` as an external
parameter, gives one exact macroscopic section

\[
\boxed{
p_S=p_S(\Xi)
}
\tag{GF13}
\]

on a possibly smaller but fixed compact characteristic neighborhood, such
that

\[
\boxed{
\mathcal O_S^{full}(p_S(\Xi),\Xi)=0.
}
\tag{GF14}
\]

Moreover

\[
p_S(\Xi)=p_*+O(S^{-1})+o(1)
\tag{GF15}
\]

uniformly, and `p_S` is as smooth in `Xi` as the fixed finite source
coefficient chart.

No Gate 1 equation has been spent to fix `Xi`.

---

## 6. Exact characteristic family of local fixed states

Define

\[
\boxed{
\mathscr S_S(\Xi)
:=
U_{base,S}
+M_{des,S}(p_S(\Xi))
+U_{core,S}(A_C,A_P;p_S(\Xi))
+T_S
+m_S+z_S,
}
\tag{GF16}
\]

where `(T_S,m_S,z_S)=W_S(p_S(\Xi),\Xi)`.

Then for every sufficiently large `S` and every `Xi` in the fixed small
compact chart,

\[
\boxed{
\mathscr P_S\mathscr S_S(\Xi)
=
\mathscr S_S(\Xi),
}
\tag{GF17}
\]

and the physical viscosity-one incompressible Navier--Stokes residual
vanishes exactly on the local relay collar.

Thus Gate 1 does not produce one isolated local state; it produces a local
six-real-dimensional characteristic family of exact local fixed states.

---

## 7. Characteristic chart rank

At principal level,

\[
D_{A_C}\mathscr S_S
\to f_C,
\qquad
D_{A_P}\mathscr S_S
\to f_P,
\]

while

\[
D_{G_P}\mathscr S_S
\]

is the secondary parent Gaussian resonant kernel.

These three complex tangent vectors belong to the three simple
characteristic sectors isolated by the Gate 2 Fredholm theorem.

Choose the dual characteristic Riesz functionals normalized on these three
vectors.  Then

\[
\boxed{
D_\Xi\mathfrak C\circ\mathscr S_S
=
I_3+o(1),
}
\tag{GF18}
\]

so for sufficiently large `S` the real six-dimensional characteristic
Jacobian is uniformly nonsingular.

This validates the characteristic-coordinate statement in
`beta21_lowu_gate2_characteristic_reduced_map.md`.

---

## 8. Consequence and correction of logical order

The correct theorem order is:

1. Gate 1 exact core+tail reset;
2. **this parameter-dependent characteristic-family extension**;
3. Gate 2 principal Fredholm reduction;
4. Gate 2 characteristic reduced map;
5. nonlinear invariant-cocycle construction.

Thus the Gate 2 characteristic coordinates are genuine free incoming-state
coordinates after the local exact reset equations have been imposed.

The next regularity upgrade is
`beta21_lowu_gate2_C2_local_section.md`, now interpreted as differentiating
the family (GF16), not as assuming that family without proof.

No global cascade is claimed here.
