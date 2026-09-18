# Gate 2 characteristic-connection audit: no nonintegrable real amplitude drift

**Status:** PROVED BOUNDED CHARACTERISTIC TRANSPORT FROM SOURCE MOVING-FRAME STRUCTURE, NATURAL REBASE, AND SOURCE-SMALL FINITE-`S` CORRECTIONS.

This note attacks the finite-dimensional kill criterion isolated in

`beta21_lowu_gate2_exact_characteristic_connection.md`.

The danger was that the exact characteristic ODE

\[
\Xi_\sigma
=
\mathcal A_{c,S}(\sigma,\Xi)
\]

might contain a persistent positive real linear growth rate.  Such a rate
would drive every nonzero relay state out of the compact Gate 1
characteristic chart as `sigma -> infinity`.

The source structure excludes that mechanism at principal normalized order.

The result has four ingredients.

1. Exact band/reference similarity is modulus-neutral after the natural
   `Q^{-A(h)}` normalization.
2. The source moving orthonormal frame has a skew connection.
3. The derivative of the moving eigenvector scale is explicitly removed by
   the source `eigenRate` term in modal coordinates.
4. All remaining Gate 1 section corrections have source-small parameter
   derivatives; dyadic finite-`S` profile changes are summable.

Consequently the Hermitian/logarithmic growth part of the characteristic
connection is integrable in `sigma`.  Its fundamental matrix and inverse
remain uniformly bounded.

No nonlinear infinite cocycle is claimed here; this is the bounded center
transport input for that theorem.

Pinned source ref:

`openai/NavierStokesAndEuler@f9e8bc5b38b6e212696e8a30e3e91517af887bbd`.

---

## 1. Principal normalized scalar coefficients are slow-profile independent

The low-`u` orbit normal form is expressed in the local source
orthonormal/tangent frame.

Its scalar principal coefficients are functions only of the fixed
dimensionless design data

\[
\boxed{
u=1.8,quad
x=0.70,quad
\kappa_*,\quad
\theta_*,\quad
\tau_*,
}
\tag{CA1}
\]

and of the orbit beta label.

For example,

\[
\Gamma_b(x)
=
\frac1{\sqrt{1+u^2x^2}}
-
b^2\frac{1+u^2x^2}{(1+u^2)^{3/2}},
\tag{CA2}
\]

and the limiting reset coefficients
`lambda_C,mu_P,rho_C,rho_P` are determined by these dimensionless data.

Thus the leading catalyst/parent/secondary-resonance characteristic scalar
model is the same at every slow profile point in the fixed source-safe
region.  Slow profile motion changes the physical source frame and the
higher-order exact coefficients, not the principal scalar orbit map.

---

## 2. Exact moving-frame rotation is skew

The pinned `PrimaryODE.FrameData.Kinematics` uses an orthonormal moving
frame `(K,N)` satisfying

\[
\boxed{
K' = \omega N,
\qquad
N' = -\omega K.
}
\tag{CA3}
\]

Equivalently, in the `(K,N)` plane the frame connection is

\[
\Omega
=
\begin{pmatrix}
0&-\omega\\
\omega&0
\end{pmatrix},
\qquad
\Omega^*=-\Omega.
\tag{CA4}
\]

Therefore physical rotation of the normalized source frame contributes no
real logarithmic amplitude growth.

For a complex scalar characteristic coefficient this part is phase/gauge
transport.

---

## 3. Eigenvector-scale derivative is removed in modal coordinates

The same source file defines

\[
h'=\mathrm{rate}\,h
\]

for the moving eigenvector scalar and then defines

\[
\begin{aligned}
\mathrm{modal11}
&=\frac{a+h b+c/h-\mathrm{rate}}2,\\
\mathrm{modal12}
&=\frac{a-h b+c/h+\mathrm{rate}}2,\\
\mathrm{modal21}
&=\frac{a+h b-c/h+\mathrm{rate}}2,\\
\mathrm{modal22}
&=\frac{a-h b-c/h-\mathrm{rate}}2.
\end{aligned}
\tag{CA5}
\]

The theorem `MovingFrameODE.modal_equations_iff` proves that this is the
**exact** change to the moving eigenbasis.

Thus the derivative of the eigenvector normalization is not an unrecorded
real amplitude drift.  It is explicitly included with the correct sign in
the modal operator.

At the ideal principal frame, the errors `a,b,c` vanish and the normalized
growing/decaying coordinates have only the intended principal
eigenvalue/damping dynamics.  In the low-`u` exact local cell that intended
principal dynamics is already part of the exact Gate 1 fixed-state map.

---

## 4. Exact local characteristic family removes absolute one-cell monodromy

By

`beta21_lowu_gate1_characteristic_family.md`,

for every characteristic coordinate

\[
\Xi=(A_C,A_P,G_P)
\]

in one fixed compact chart,

\[
\boxed{
\mathscr P_{S,p}
\mathscr S_S(p,\Xi)
=
\mathscr S_S(p,\Xi).
}
\tag{CA6}
\]

Differentiate in `Xi`:

\[
\boxed{
D\mathscr P_{S,p}
\big|_{\mathscr S_S}
\,
D_\Xi\mathscr S_S
=
D_\Xi\mathscr S_S.
}
\tag{CA7}
\]

Hence the **absolute finite-`S` within-cell characteristic monodromy is
exactly identity on the characteristic tangent family**.

In particular an `O(S^{-1})` moving-frame correction inside one cell is
not to be accumulated over cells.  It has already been absorbed into the
exact finite-`S` fixed-state family.

Gate 2 only sees the *change of that exact family* from one slow profile
point/band to the next.

---

## 5. Pure scale change is exactly neutral

By

`beta21_lowu_gate2_natural_rebase_characteristic_invariance.md`,

the normalized velocity coefficient

\[
\widetilde a_Q=Q^{-A(h)}a_Q
\]

satisfies the exact source rebase identity

\[
\boxed{
\widetilde a_Q
=
\widetilde a_{Q_r}^{ref}\circ\mathcal C_{Q,Q_r}.
}
\tag{CA8}
\]

Thus dyadic/source scale change contributes no positive real scalar to the
characteristic amplitude.

The cover/chart argument changes, but the amplitude modulus does not acquire
a scale factor.

---

## 6. Principal slow connection has zero Hermitian part

Use the exact Gate 1 characteristic basis

\[
e_{C,S}(p),qquad
e_{P,S}(p),qquad
e_{G,S}(p)
\]

with the principal central/tail normalizations from the Gate 1 family.

At principal normalized order:

1. catalyst and parent live in distinct beta sectors, so they do not mix;
2. the principal scalar orbit coefficients are independent of `p);
3. physical variation of the source orthonormal frame is skew by (CA3);
4. eigenvector-length variation is removed by (CA5);
5. the secondary resonant Gaussian scalar normal form is likewise universal
   in the fixed `u,x,tau` variables and lies at a fixed negative action.

Therefore the principal characteristic connection matrix
`A_c^(0)(sigma)` satisfies

\[
\boxed{
\frac{
A_c^{(0)}
+
(A_c^{(0)})^*
}{2}
=0.
}
\tag{CA9}
\]

It may contain phase/rotation transport, but no real principal amplitude
growth.

This statement is in the normalized characteristic coordinates; it is not a
claim that the raw physical vector field is norm-preserving.

---

## 7. Size of the exact real correction

The exact Gate 1 `C^2` section theorem gives source-small parameter
derivatives of the tail/mean/nonzero correction:

\[
\boxed{
\|D_pW_S\|
+
\|D_p^2W_S\|
\le
S^B
\left(
\varepsilon^{a_*}+e^{-cS}
\right),
\qquad a_*>0.
}
\tag{CA10}
\]

The exact source profile/frame coefficient perturbations entering the local
fixed state obey the same finite-order source ledger.

Within one fixed dyadic band, `S` is constant.  Hence the Hermitian part of
the exact characteristic connection obeys

\[
\boxed{
\left\|
\operatorname{Herm}
\left(
\mathcal A_{c,S}
\right)
\right\|
\le
C S^B
\left(
\varepsilon^{a_*}+e^{-cS}
\right).
}
\tag{CA11}
\]

At a dyadic band change, the exact tangent-Gaussian resampling theorem gives

\[
\boxed{
\|J_{n+1}J_n^{-1}-I\|
\le
Cn^{-2}
+
\text{source-small terms}.
}
\tag{CA12}
\]

The `n^{-2}` series is summable.

---

## 8. Integrability along the constant-fast schedule

By

`beta21_lowu_constant_fast_cell_sigma_schedule.md`,

\[
\Delta\sigma_j
\asymp
j^{-1},
\qquad
\varepsilon_j\asymp j^{-1},
\qquad
S_j\asymp(\log j)^2.
\tag{CA13}
\]

The continuous logarithmic growth accumulated inside the fixed bands is
bounded by

\[
\sum_j
\Delta\sigma_j
S_j^B\varepsilon_j^{a_*}.
\]

Using (CA13),

\[
\boxed{
\sum_j
\frac{(\log j)^{2B}}
{j^{1+a_*}}
<\infty.
}
\tag{CA14}
\]

Similarly,

\[
\sum_j
\Delta\sigma_j S_j^Be^{-cS_j}
<\infty.
\tag{CA15}
\]

Adding the dyadic jump series,

\[
\sum_n n^{-2}<\infty,
\]

gives one finite total real logarithmic growth budget

\[
\boxed{
\int_{\sigma_0}^{\infty}
\|
\operatorname{Herm}\mathcal A_c
\|,d\sigma
+
\sum_{n\ge n_0}
\|J_{n+1}J_n^{-1}-I\|
<\infty.
}
\tag{CA16}
\]

---

## 9. Bounded characteristic fundamental matrix

Let `Q_c(sigma,sigma_0)` be the fundamental matrix of the exact
characteristic connection, including the dyadic jump maps.

The skew principal part contributes only unitary/phase transport.  Standard
logarithmic-norm estimates and (CA16) yield

\[
\boxed{
\sup_{\sigma\ge\sigma_0}
\|Q_c(\sigma,\sigma_0)\|
\le C_c<\infty.
}
\tag{CA17}
\]

Apply the same argument to the inverse connection.  Since the Hermitian part
changes sign but has the same norm,

\[
\boxed{
\sup_{\sigma\ge\sigma_0}
\|Q_c(\sigma,\sigma_0)^{-1}\|
\le C_c'<\infty.
}
\tag{CA18}
\]

Therefore every nonzero characteristic vector remains comparable to its
initial size:

\[
\boxed{
(C_c')^{-1}|\Xi_0|
\le
|\Xi(\sigma)|
\le
C_c|\Xi_0|.
}
\tag{CA19}
\]

Choose the initial characteristic point in a sufficiently small compact
subchart whose multiplicative `C_c,C_c'` enlargement remains inside the
Gate 1 characteristic neighborhood.  Then the exact characteristic orbit
never leaves the admissible chart.

Thus the kill criterion (EC18) is passed.

---

## 10. Consequence for Gate 2

The finite-dimensional center is no longer an obstruction:

\[
\boxed{
\text{there exist nonzero global characteristic trajectories that remain
inside the exact Gate 1 chart for all late }\sigma.
}
\tag{CA20}
\]

Together with the earlier Gate 2 layers we now have

1. finite Fredholm characteristic block;
2. hyperbolic analytic complement with Green operator;
3. a genuine exact Gate 1 family over the characteristic block;
4. constant-fast-cell global schedule;
5. square-summable one-step Taylor defects;
6. uniformly bounded center/characteristic transport.

The next theorem is the nonlinear Lyapunov--Perron gluing of the bounded
characteristic orbit to the analytic hyperbolic complement:

`beta21_lowu_gate2_nonlinear_invariant_cocycle.md`.

That theorem must still prove that all nonlinear return-cycle Lipschitz
coefficients are small enough on the infinite sequence space and that the
resulting sequence reconstructs one forward Cauchy state.

No infinite cascade or singularity claim is made here.
