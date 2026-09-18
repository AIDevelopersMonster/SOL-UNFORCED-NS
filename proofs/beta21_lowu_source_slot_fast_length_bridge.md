# Exact source-slot bridge and uniform fast length of the low-`u` cell

**Status:** PROVED DIRECTLY FROM THE PINNED SOURCE DEFINITIONS AND SLOT-LENGTH BOUNDS.

This note identifies the reduced slope variable used throughout the low-`u`
beta-(2,1) action calculus with the literal normalized source slot coordinate.

The consequence is decisive for Gate 2:

> the new boundary-layer exact reset cell has **uniform `O(1)` length in
> the source fast coordinate**, not `O(S)`.

The earlier `O(S)` source-native stage schedule was built for the old
nine-lobe architecture and must not be imported unchanged into the new
low-`u` boundary-layer cell.

Pinned OpenAI source ref:

`openai/NavierStokesAndEuler@f9e8bc5b38b6e212696e8a30e3e91517af887bbd`.

---

## 1. Exact source slot magnitude

The pinned source file

`NavierStokes/PrimaryODE.lean`

uses `PulseGrowth.slotMagnitude`.  Its derivative proof unfolds the
definition as

\[
\boxed{
\operatorname{slotMagnitude}(u,L,v)
=
\frac u2+\frac{uv}{L}.
}
\tag{FL1}
\]

Therefore

\[
\boxed{
\operatorname{slotMagnitude}(u,L,v)
=
u\left(\frac12+\frac vL\right).
}
\tag{FL2}
\]

All low-`u` beta-action formulas are written in terms of the dimensionless
quantity `u z`, through

\[
\Gamma_b(z)
=
\frac1{\sqrt{1+u^2z^2}}
-
b^2\frac{1+u^2z^2}{(1+u^2)^{3/2}}.
\tag{FL3}
\]

Hence the literal source identification is

\[
\boxed{
z(v)=\frac12+\frac vL.
}
\tag{FL4}
\]

No additional scale factor is present.

---

## 2. Boundary-layer cell interval

The low-`u` boundary-layer theorem uses

\[
\boxed{
\delta_S=\frac\kappa S
}
\tag{FL5}
\]

and the complete one-cell reduced-slope interval has length

\[
\boxed{
\Delta z_{cell}=2\delta_S=\frac{2\kappa}{S}.
}
\tag{FL6}
\]

Equivalently, in the stretched cell variable

\[
\tau=St,
\]

the interval is

\[
0\le\tau\le2\kappa.
\]

By (FL4),

\[
\Delta z=\frac{\Delta v}{L},
\]

so the corresponding source fast-coordinate length is exactly

\[
\boxed{
\Delta v_{cell}
=
L\frac{2\kappa}{S}.
}
\tag{FL7}
\]

---

## 3. The source slot length is comparable to `S`

The pinned source file

`NavierStokes/ChartScales.lean`

defines

\[
L_n
=
\operatorname{slotLength}(r_0,h,n)
=
\frac{2r_0}{\operatorname{timeCoefficient}(h,n)}
\]

and proves `slotLength_bounds`:

\[
\boxed{
2r_0S(n)
\le
L_n
\le
2r_0T_gS(n)
}
\tag{FL8}
\]

for every sufficiently large source band.

In the low-`u` cell, the large source parameter `S` is precisely this
source slow scale.

Insert (FL8) into (FL7):

\[
\boxed{
4r_0\kappa
\le
\Delta v_{cell}
\le
4r_0T_g\kappa.
}
\tag{FL9}
\]

Thus there are fixed constants

\[
0<c_v\le C_v<\infty
\]

such that

\[
\boxed{
c_v\le\Delta v_{cell}\le C_v
}
\tag{FL10}
\]

uniformly for all sufficiently large levels.

The cell does not shrink to zero fast-time length, and it does not grow like
`S`.

---

## 4. Consequence for the moving-frame error

The pinned primary ODE estimates give moving-frame / viscosity coefficient
errors of size

\[
O(S^{-1})
\]

in the source fast variable after the exact reference envelope is factored.

On an old full source slot of length `O(S)`, the integrated bound is only
`O(1)`.

On the actual low-`u` reset interval (FL10), however,

\[
\boxed{
\int_{v_{in}}^{v_{out}}
O(S^{-1})\,dv
=
O(S^{-1}).
}
\tag{FL11}
\]

Therefore the normalized within-cell fundamental differs from its frozen
principal fundamental by

\[
\boxed{
I+O(S^{-1})
}
\tag{FL12}
\]

at the level of one-cell linear transport, uniformly on the fixed compact
low-`u` parameter set.

This is consistent with, and conceptually explains, the observed
`O(S^{-1})` finite-`S` multiplier defect in the low-`u` numerical
certificates.

---

## 5. Scale rebase plus one low-`u` cell

Combine (FL12) with

`beta21_lowu_gate2_natural_rebase_characteristic_invariance.md`.

Pure source band/reference rebase has **exactly zero** real amplitude drift
after normalizing by `Q^{-A(h)}`.

Hence a one-cell normalized characteristic transport has the structure

\[
\boxed{
\mathcal B_j
=
\mathcal B_j^{principal}
+
O(S_j^{-1})
+
\mathcal E_j^{slow},
}
\tag{FL13}
\]

where

- the similarity scale factor has already cancelled exactly;
- `B_j^{principal}` is the exact low-`u` local reset/characteristic
  transport;
- `O(S_j^{-1})` is the integrated source moving-frame/viscosity
  perturbation over the constant fast interval;
- `E_j^{slow}` comes only from the slow trapped-spine change between
  adjacent low-`u` cells.

The old `e^{O(1)}` full-slot uncertainty is not intrinsic to the new cell.

---

## 6. Required schedule revision

The old theorem

`sigma_native_exact_stage_schedule.md`

allocates a logarithmic stage of size

\[
\Delta\sigma
=
\Lambda\varepsilon S
\]

because the old complete nine-lobe stage occupied `O(S)` fast time.

For the present cell, (FL10) shows that only `O(1)` fast time is intrinsic.

Since the exact source temporal-coordinate relation is

\[
dT=\varepsilon,dV,
\]

one low-`u` cell requires normalized physical/logarithmic length only

\[
\boxed{
\Delta\sigma_{cell}
\asymp
\varepsilon
}
\tag{FL14}
\]

up to the fixed trapped-spine conversion constants.

Thus the preferred Gate 2/global schedule should be rebuilt with constant
fast-cell length, rather than inheriting the old `epsilon S` stage length.

This schedule is derived in the next theorem layer.

---

## 7. What is proved here

1. The reduced slope variable in the low-`u` action calculus is exactly the
   normalized source slot coordinate:
   \[
   z=1/2+v/L.
   \]
2. Source slot length satisfies `L asymp S`.
3. Since the low-`u` cell uses `Delta z=2 kappa/S`, its fast length is
   bounded above and below by fixed positive constants.
4. Source moving-frame errors of size `O(1/S)` therefore integrate to
   `O(1/S)` over one new cell.
5. The old `O(S)` nine-lobe schedule is not the natural schedule for the
   low-`u` boundary-layer cell.

No infinite packing theorem is claimed in this note.  The next file is

`beta21_lowu_constant_fast_cell_sigma_schedule.md`.
