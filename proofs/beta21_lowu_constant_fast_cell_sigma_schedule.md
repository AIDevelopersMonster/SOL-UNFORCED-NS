# Source-native constant-fast-cell sigma schedule for the low-`u` reset

**Status:** PROVED GLOBAL CLOCK / PACKING / SQUARE-SUMMABILITY THEOREM FOR THE NEW LOW-`u` CELL.  THIS REPLACES THE OLD `epsilon S` STAGE LENGTH WHEN WORKING WITH THE BOUNDARY-LAYER CELL.

The theorem

`beta21_lowu_source_slot_fast_length_bridge.md`

proves that one exact low-`u` reset cell occupies a source fast-coordinate
interval

\[
c_v\le\Delta V_{cell}\le C_v
\tag{CF1}
\]

with fixed positive constants independent of the source level.

Therefore the old schedule

\[
\Delta\sigma\asymp\varepsilon S
\]

is unnecessarily long for the new architecture.  The natural exact global
clock is instead

\[
\boxed{
\Delta\sigma_j
=
\Lambda\varepsilon_j,
\qquad
\varepsilon_j=q_j^h,
}
\tag{CF2}
\]

with one fixed design constant `Lambda` chosen large enough to contain the
cell and fixed buffers.

This note proves that the schedule reaches `sigma=infinity`, accumulates at
physical time `t=1`, has `O(1)` fast length per cell, and has
square-summable increments.

---

## 1. Trapped-spine clock

Use the already-proved exact trapped spine

\[
\boxed{
q(\sigma)
=
\frac{e^{-\sigma}}{d(\eta(\sigma))},
}
\tag{CF3}
\]

with

\[
0<d_-\le d(\eta(\sigma))\le d_+<\infty.
\tag{CF4}
\]

Hence

\[
\boxed{
c_qe^{-\sigma}
\le q(\sigma)
\le C_qe^{-\sigma}.
}
\tag{CF5}
\]

Let

\[
\varepsilon(\sigma)=q(\sigma)^h,
\qquad h>0.
\tag{CF6}
\]

Then

\[
c_\varepsilon e^{-h\sigma}
\le
\varepsilon(\sigma)
\le
C_\varepsilon e^{-h\sigma}.
\tag{CF7}
\]

All constants are level-independent.

---

## 2. Define the cell sequence

Choose a sufficiently late `sigma_0` and one fixed `Lambda>0`.  Define

\[
\boxed{
\sigma_{j+1}
=
\sigma_j+\Lambda\varepsilon_j,
\qquad
\varepsilon_j:=\varepsilon(\sigma_j).
}
\tag{CF8}
\]

Since `epsilon(sigma)->0`, after increasing the starting level,

\[
0<\Delta\sigma_j<1/10.
\tag{CF9}
\]

Thus every late cell is a near-identity move in the exact global logarithmic
clock.

---

## 3. The stages reach `sigma=infinity`

Suppose for contradiction that

\[
\sigma_j\uparrow\sigma_\infty<\infty.
\]

Then (CF7) gives

\[
\varepsilon_j
\ge
c_\varepsilon e^{-h\sigma_\infty}
>0.
\]

Therefore

\[
\Delta\sigma_j
=
\Lambda\varepsilon_j
\ge c>0,
\]

contradicting convergence of `sigma_j`.

Hence

\[
\boxed{
\sigma_j\to\infty.
}
\tag{CF10}
\]

Since

\[
t=1-e^{-\sigma},
\]

we obtain

\[
\boxed{
t_j\uparrow1.
}
\tag{CF11}
\]

Also

\[
\boxed{
q_j\to0,
\qquad
\varepsilon_j\to0.
}
\tag{CF12}
\]

---

## 4. Relative scale and frame change per cell

From

\[
q(\sigma)
=
e^{-\sigma}/d(\eta(\sigma))
\]

and the smooth trapped-spine ODE on one fixed compact rectangle,

\[
\left|
\log\frac{d_{j+1}}{d_j}
\right|
\le
C_d\Delta\sigma_j.
\tag{CF13}
\]

Therefore

\[
\boxed{
\left|
\log\frac{q_{j+1}}{q_j}
\right|
\le
C\Delta\sigma_j
=
C\Lambda\varepsilon_j
=o(1).
}
\tag{CF14}
\]

Every normalized source/frame coefficient changes by `O(epsilon_j)` per
late cell, up to fixed smooth-chart constants.

This is strictly smaller than the old `O(epsilon_j S_j)` stage variation.

---

## 5. Physical duration

The exact global relation is

\[
\frac{dt}{d\sigma}
=
e^{-\sigma}
=
q(\sigma)d(\eta(\sigma)).
\tag{CF15}
\]

Using (CF4), (CF8), and the near-identity variation (CF14),

\[
\boxed{
\Delta t_j
\asymp
q_j\Delta\sigma_j
=
\Lambda q_j\varepsilon_j
=
\Lambda q_j^{1+h}.
}
\tag{CF16}
\]

Hence the physical durations form a positive sequence whose sum is exactly
bounded by the remaining interval to `t=1`, while the cell count is
infinite.

The normalized physical duration relative to the current source scale is

\[
\boxed{
\frac{\Delta t_j}{q_j}
\asymp
\Lambda\varepsilon_j.
}
\tag{CF17}
\]

---

## 6. Fast-coordinate length

The pinned source temporal-coordinate identity used throughout the branch is

\[
dT=\varepsilon,dV,
\tag{CF18}
\]

where `T` is normalized physical time and `V` is the source fast pulse
coordinate.

By (CF17), the exact trapped-spine/chart conversion gives

\[
\Delta T_j
\asymp
\Lambda\varepsilon_j.
\tag{CF19}
\]

Since `epsilon` changes only by `1+o(1)` across one cell,

\[
\boxed{
\Delta V_j
\asymp
\Lambda.
}
\tag{CF20}
\]

Thus every allocated cell interval has source fast length bounded above and
below by fixed positive constants.

Choose `Lambda` once so that the lower comparison constant in (CF20)
satisfies

\[
\boxed{
c_V\Lambda
>
C_v+2B_v,
}
\tag{CF21}
\]

where `C_v` is the uniform upper fast length from (CF1) and `B_v>0` is a
fixed desired buffer length.

Then every late interval contains

1. one complete exact low-`u` core+tail cell;
2. a fixed positive entrance buffer;
3. a fixed positive exit buffer.

No `O(S)` unused gap is forced by the geometry.

---

## 7. Asymptotic stage index

Define

\[
Y_j:=e^{h\sigma_j}.
\]

From (CF8),

\[
Y_{j+1}
=
Y_j e^{h\Lambda\varepsilon_j}.
\]

Since `epsilon_j asymp e^{-h sigma_j}=Y_j^{-1}` and
`h Lambda epsilon_j ->0`,

\[
Y_{j+1}-Y_j
=
Y_j
\left(
h\Lambda\varepsilon_j
+
O(\varepsilon_j^2)
\right).
\]

Using (CF7), there are constants `0<c_Y<C_Y<infinity` such that for all
late `j`,

\[
\boxed{
c_Y
\le
Y_{j+1}-Y_j
\le
C_Y.
}
\tag{CF22}
\]

Therefore

\[
\boxed{
Y_j\asymp j,
}
\tag{CF23}
\]

and hence

\[
\boxed{
e^{-\sigma_j}
\asymp
j^{-1/h},
\qquad
q_j\asymp j^{-1/h},
}
\tag{CF24}
\]

up to the fixed trapped-spine factor `d(eta)`.

Also

\[
\boxed{
\varepsilon_j=q_j^h\asymp j^{-1}.
}
\tag{CF25}
\]

Thus the new constant-fast schedule has an especially transparent stage
asymptotic.

---

## 8. Square summability and higher powers

From (CF25),

\[
\Delta\sigma_j
=
\Lambda\varepsilon_j
\asymp j^{-1}.
\]

Therefore

\[
\boxed{
\sum_j(\Delta\sigma_j)^p<\infty
\qquad
\text{for every }p>1,
}
\tag{CF26}
\]

while

\[
\boxed{
\sum_j\Delta\sigma_j=\infty.
}
\tag{CF27}
\]

In particular,

\[
\boxed{
\sum_j(\Delta\sigma_j)^2<\infty.
}
\tag{CF28}
\]

Hence the first-order covariant motion reaches the singular clock, while all
quadratic Taylor defects are summable.

---

## 9. Compatibility with low-`u` finite-`S` errors

The source slow scale obeys

\[
S(n)=n^2,
\qquad
n\log2=\sigma+O(1)
\]

along the dyadic hierarchy.  Therefore

\[
\boxed{
S_j\asymp(1+\sigma_j)^2
\asymp(\log j)^2.
}
\tag{CF29}
\]

The integrated moving-frame error of one low-`u` cell is `O(S_j^{-1})`.
This tends to zero, but

\[
\sum_j S_j^{-1}
\sim
\sum_j(\log j)^{-2}
\]

does not converge.

Therefore an `O(S^{-1})` error must be treated as part of the exact
one-cell normalized monodromy/covariant characteristic frame, **not** as a
summable forcing.

This is not an obstruction: the exact Gate 1 cell already contains that
finite-`S` monodromy.  Gate 2 should transport the exact characteristic
section, subtract its first-order slow variation, and count only the
quadratic/source-small remainder as forcing.

---

## 10. Consequence for Gate 2

The natural low-`u` architecture is now:

\[
\boxed{
\text{one exact }O(1)\text{-fast cell per stage}
}
\tag{CF30}
\]

with

\[
\boxed{
\Delta\sigma_j
=
\Lambda\varepsilon_j
\asymp j^{-1}.
}
\tag{CF31}
\]

This removes the old `O(S)` within-stage gap from the Gate 2 transport
problem.

Combined with

- exact natural-rebase invariance,
- the `C^2` exact local characteristic family,
- finite-dimensional characteristic rank,
- analytic hyperbolic Green shadowing,

the remaining nonlinear cocycle problem has the correct small-step
structure.

The next theorem is
`beta21_lowu_gate2_exact_characteristic_connection.md`:

> define the exact characteristic connection by differentiating the finite-S
> local fixed-state family along the trapped spine, include the exact
> one-cell finite-S monodromy in the moving frame, and prove that the residual
> one-step characteristic defect is `O((Delta sigma_j)^2)` plus source-small
> terms.

No infinite cascade or blow-up theorem is claimed here.
