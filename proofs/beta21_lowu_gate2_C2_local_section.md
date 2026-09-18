# Gate 2 uniform `C^2` regularity of the exact local full-state section

**Status:** PROVED FINITE-ORDER PARAMETER REGULARITY UPGRADE FROM THE EXISTING CONTRACTION / TAIL-PARAMETRIX ESTIMATES.

This note supplies the regularity input isolated in
`beta21_lowu_gate2_native_step_square_summability.md`.

The Gate 1 proof recorded only the `C^1` parameter transfer needed for its
finite-dimensional implicit-function theorem.  Gate 2 needs one further
derivative in order to subtract the exact first-order characteristic motion
and leave a summable `O((Delta sigma_j)^2)` one-step Taylor defect.

No new inverse problem appears.  The nonlinear Navier--Stokes map is
quadratic, the exact correction map is uniformly contractive, and every
fixed parameter derivative of source coefficients/tail parametrices costs
only a fixed power of `S`.  Positive epsilon powers and action gaps absorb
all such fixed polynomial losses.

---

## 1. Total finite parameter chart

Let `eta` denote the finite collection of parameters used to describe one
late exact Gate 1 state:

\[
\eta
=
(p_{slow},\kappa,\theta,A_M,\tau,A_C,A_P,G_P).
\tag{C2-1}
\]

Here

- `p_slow` is the slow trapped-spine profile point on a fixed compact
  source rectangle;
- `(kappa,theta,A_M,tau)` are the Gate 1 macroscopic reset/root variables;
- `A_C,A_P` are the complex central-profile normalization coordinates;
- `G_P` is the complex secondary-parent Gaussian gauge coordinate.

Work on one fixed compact parameter neighborhood `K_eta` on which all
strict source, action, transversality and localization margins from Gate 1
remain valid.

The negative-frequency coefficients are determined by reality and are not
independent parameters.

---

## 2. Exact correction equation including the analytic tail

Write the exact infinite-dimensional Gate 1 correction as

\[
\boxed{
W_S(\eta)
=
(T_S,m_S,z_S)
}
\tag{C2-2}
\]

and its fixed-point equation as

\[
\boxed{
W=\mathfrak T_S(\eta;W).
}
\tag{C2-3}
\]

The exact Gate 1 theorem gives, in the weighted product norm,

\[
\boxed{
\|D_W\mathfrak T_S\|
\le q_S<\frac12
}
\tag{C2-4}
\]

for all sufficiently large `S`, uniformly on the invariant correction ball
and `K_eta`.  Therefore

\[
\boxed{
\|(I-D_W\mathfrak T_S)^{-1}\|
\le2.
}
\tag{C2-5}
\]

The correction radius has the form

\[
\boxed{
R_S
\le
S^A\varepsilon^{a_*}
+
S^Ae^{-cS},
\qquad a_*>0.
}
\tag{C2-6}
\]

The polynomial exponent may increase from line to line below.

---

## 3. Two parameter derivatives of the building blocks

The source coefficient maps are smooth functions of the finite slow/frame
variables on a fixed compact strict-cone set.

At every fixed physical/source derivative order and every fixed parameter
derivative order `r`, the source jet calculus gives a bound of the form

\[
\boxed{
C_{m,r}^{param}(S)
\le C_{m,r}S^{B_{m,r}}.
}
\tag{C2-7}
\]

For `r=1` this is the estimate already used in the Gate 1 `C^1` theorem.
The same statement for `r=2` follows from the same finite Leibniz/Faa di
Bruno expansion: only finitely many normalized source coefficients are
differentiated and the publication derivative order is fixed.

The Navier--Stokes nonlinearity is quadratic.  Consequently

\[
D_W^r\mathfrak T_S=0
\quad\text{for }r\ge3
\tag{C2-8}
\]

at the algebraic nonlinear-source level; propagation/reconstruction maps
remain smooth finite-order maps with the polynomial source bounds (C2-7).

---

## 4. Two derivatives of the finite-`S` tail parametrix

The tail right inverse is assembled from

1. frozen Wiener inverses on ordinary windows;
2. slowly varying cutoffs;
3. one secondary-parent Gaussian/Volterra model inverse.

The Gate 1 theorem gives

\[
\|\mathcal G_{tail,S}\|
\le CS^{A_t}.
\tag{C2-9}
\]

Differentiate the frozen inverse identity

\[
F(\eta)^{-1}F(\eta)=I.
\]

One derivative yields

\[
D(F^{-1})
=
-F^{-1}(DF)F^{-1},
\]

and two derivatives yield a finite sum of terms containing at most three
copies of `F^{-1}` and two derivatives of `F`.  Thus, using (C2-7),
there are fixed exponents `B_1,B_2` such that

\[
\boxed{
\|D_\eta\mathcal G_{tail,S}\|
\le CS^{B_1},
\qquad
\|D_\eta^2\mathcal G_{tail,S}\|
\le CS^{B_2}.
}
\tag{C2-10}
\]

The same conclusion holds in the secondary resonant chart after fixing or
retaining the Gaussian gauge `G_P`: variation of constants is smooth in
the transverse coefficient and its finite-`S` loss is polynomial.

Therefore no parameter differentiation introduces an exponential inverse
loss.

---

## 5. First derivative of the fixed point

Differentiate (C2-3):

\[
(I-D_W\mathfrak T_S)D_\eta W_S
=
D_\eta\mathfrak T_S.
\tag{C2-11}
\]

The existing `C^1` theorem, now with the tail block included, gives

\[
\boxed{
\|D_\eta W_S\|
\le
S^{B_1'}
\left(
\varepsilon^{a_*}+e^{-cS}
\right)
=o(1).
}
\tag{C2-12}
\]

This includes derivatives with respect to the slow profile variables,
because those enter the same smooth compact coefficient field.

---

## 6. Second derivative equation

Differentiate (C2-11) once more.  In bilinear notation,

\[
\begin{aligned}
(I-D_W\mathfrak T_S)D_\eta^2W_S
={}&
D_\eta^2\mathfrak T_S
+2D_{\eta W}^2\mathfrak T_S[D_\eta W_S]\\
&+
D_W^2\mathfrak T_S[D_\eta W_S,D_\eta W_S].
\end{aligned}
\tag{C2-13}
\]

All terms are evaluated at `(eta,W_S(eta))`.

Each coefficient in the right side costs only a fixed polynomial in `S`.
Every inhomogeneous twice-differentiated source still contains either

- a positive epsilon power;
- a fixed action gap `e^{-cS}`;
- the shrinking correction radius.

Using (C2-12), the two terms containing `D_eta W_S` are no larger.

Hence for a fixed exponent `B_2'`,

\[
\boxed{
\|\text{RHS of (C2-13)}\|
\le
CS^{B_2'}
\left(
\varepsilon^{a_*}+e^{-cS}
\right).
}
\tag{C2-14}
\]

Apply (C2-5):

\[
\boxed{
\|D_\eta^2W_S\|
\le
CS^{B_2'}
\left(
\varepsilon^{a_*}+e^{-cS}
\right)
=o(1).
}
\tag{C2-15}
\]

Thus the exact infinite-dimensional correction is uniformly `C^2` on
`K_eta`, up to the harmless fixed polynomial source weights.

---

## 7. `C^2` exact finite-dimensional parameter solve

Let

\[
\mathcal O_S(\eta)
\]

collect the exact Gate 1 reset observables after inserting `W_S(eta)`.
Output extraction at fixed derivative order has only polynomial `S` cost.
Therefore (C2-12)--(C2-15) give

\[
\boxed{
\|\mathcal O_S-\mathcal O_S^{prin}\|_{C^2(K_\eta)}
\le
S^B\left(
\varepsilon^{a_*}+e^{-cS}
\right)
=o(1).
}
\tag{C2-16}
\]

The principal finite-dimensional reset Jacobian is uniformly nonsingular.
The quantitative implicit-function theorem with parameters therefore
produces the exact local parameter section

\[
\boxed{
p_S^{exact}
=
p_S^{exact}(p_{slow},A_C,A_P,G_P)
}
\tag{C2-17}
\]

with uniform `C^2` bounds on the fixed compact characteristic chart.

Substituting into the full state yields a `C^2` family

\[
\boxed{
\mathscr S_S
:
(p_{slow},A_C,A_P,G_P)
\longmapsto
U_S^{Gate1}.
}
\tag{C2-18}
\]

This is the exact local section required by Gate 2.

---

## 8. Along the trapped spine

The realized-background trapped-spine ODE has a smooth vector field on one
fixed compact rectangle.  Hence

\[
p_{slow}=p_{slow}(\sigma)
\]

is `C^2` (indeed smooth) with uniformly bounded derivatives on every late
stage in normalized source coordinates.

Compose (C2-18) with the slow spine and with the exact characteristic
parallel-transport frame from
`beta21_lowu_gate2_characteristic_reduced_map.md`.

Taylor's theorem over one source-native step gives

\[
\boxed{
\widehat{\mathscr S}_{j+1}
-
\widehat{\mathscr S}_{j}
-
D_\sigma\widehat{\mathscr S}_{j}\,
\Delta\sigma_j
=
O((\Delta\sigma_j)^2),
}
\tag{C2-19}
\]

uniformly for all sufficiently late stages, apart from the separately
recorded dyadic resampling and source-small terms.

By
`beta21_lowu_gate2_native_step_square_summability.md`,

\[
\sum_j(\Delta\sigma_j)^2<\infty.
\tag{C2-20}
\]

Therefore the first-order covariant subtraction leaves a summable
characteristic forcing.

---

## 9. Consequence

The exact local Gate 1 family has sufficient regularity for nonlinear Gate 2:

\[
\boxed{
\text{exact Gate 1 section is uniformly }C^2
\text{ in the finite slow/characteristic parameters.}
}
\tag{C2-21}
\]

No Nash--Moser loss or new inverse theorem appears in taking the second
parameter derivative.

The remaining Gate 2 task is now genuinely dynamical:

- couple the summable characteristic forcing (C2-19) to the finite center
  recurrence;
- couple that recurrence to the analytic stable/unstable Green operator;
- prove a nonlinear Lyapunov--Perron contraction on the infinite stage
  sequence;
- reconstruct the resulting bounded sequence from one initial Cauchy state.

The preferred next file is

`beta21_lowu_gate2_nonlinear_invariant_cocycle.md`.
