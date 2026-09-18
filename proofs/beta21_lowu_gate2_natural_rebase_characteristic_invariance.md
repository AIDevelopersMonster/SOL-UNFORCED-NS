# Gate 2 exact natural-rebase invariance of normalized characteristic amplitudes

**Status:** PROVED DIRECTLY FROM THE PINNED OPENAI PHYSICAL REBASE IDENTITIES.

This note removes one of the main Gate 2 kill criteria.

A priori, an exact local characteristic coordinate could remain bounded in a
moving chart but acquire a systematic positive real growth every time the
source band/reference scale changes.  Such a factor would accumulate over
`sigma -> infinity` and drive the characteristic state out of the compact
Gate 1 family.

The pinned OpenAI source rules this out for the **pure band/reference
similarity change**.  The physical velocity amplitude carries exactly the
natural similarity factor `Q^{A(h)}`, with no additional real scalar.
After the standard source normalization by `Q^{-A(h)}`, the amplitude is
exactly invariant under rebase.

This does not yet control genuine within-stage moving-frame evolution.
It proves that scale change itself is not an inter-cell amplitude-growth
obstruction.

Pinned source ref:

`openai/NavierStokesAndEuler@f9e8bc5b38b6e212696e8a30e3e91517af887bbd`.

---

## 1. Source velocity exponent

In the pinned source,

`NavierStokes/CoordinateAlgebra.lean`

defines

\[
\boxed{
A(h)=\frac12+h.
}
\tag{NR1}
\]

For positive source scales `Q,Q_r`,

`NavierStokes/PhysicalParticularWave.lean`

defines

\[
\operatorname{ratioPower}(Q,Q_r,a)
=
\frac{Q^a}{Q_r^a}
\tag{NR2}
\]

and

\[
\boxed{
\operatorname{velocityWeight}(h,Q,Q_r)
=
\operatorname{ratioPower}(Q,Q_r,A(h)).
}
\tag{NR3}
\]

Thus

\[
\boxed{
\operatorname{velocityWeight}(h,Q,Q_r)
=
\frac{Q^{A(h)}}{Q_r^{A(h)}}.
}
\tag{NR4}
\]

---

## 2. Exact physical band-amplitude rebase identity

Let `D` be one physical particular-wave assembly datum and let `j` be a
nonzero harmonic for which the reference frequency is nonzero.

The pinned theorem

`PhysicalParticularWave.bandAmplitude_eq_reference`

states, under the literal source `ReferenceODE` hypotheses,

\[
\boxed{
a_Q(p,Y)
=
\operatorname{velocityWeight}(h,Q,Q_r),
a_{Q_r}^{ref}
\bigl(
\operatorname{parameterChange}(h,Q,Q_r)p,,
\operatorname{coverPower}(gap)Y
\bigr).
}
\tag{NR5}
\]

There is no further scalar prefactor.

The transported residual source obeys the analogous exact naturality law

\[
F_Q
=
\operatorname{sourceWeight}(h,Q,Q_r)
F_{Q_r}^{ref}\circ\mathcal C_{Q,Q_r},
\tag{NR6}
\]

by
`PhysicalParticularWave.transportedResidualSource_apply`.

The source also proves

\[
\operatorname{sourceWeight}
=
\operatorname{velocityWeight}^2
\operatorname{bandScale}
\tag{NR7}
\]

in
`ActualReferenceRebase.state_sourceWeight`, exactly as required by the
physical quadratic residual scaling.

Thus (NR5) is part of the exact physical similarity covariance, not a
heuristic WKB normalization.

---

## 3. Exact cancellation in the normalized velocity amplitude

Define the source-normalized velocity coefficient

\[
\boxed{
\widetilde a_Q
:=
Q^{-A(h)}a_Q.
}
\tag{NR8}
\]

Insert (NR4)--(NR5):

\[
\begin{aligned}
\widetilde a_Q(p,Y)
&=
Q^{-A(h)}
\frac{Q^{A(h)}}{Q_r^{A(h)}}
a_{Q_r}^{ref}(\mathcal C_{Q,Q_r}(p,Y))\\
&=
Q_r^{-A(h)}
a_{Q_r}^{ref}(\mathcal C_{Q,Q_r}(p,Y)).
\end{aligned}
\tag{NR9}
\]

The pinned source contains this cancellation algebraically as

`PhysicalParticularWave.ratioPower_cancel`.

Therefore

\[
\boxed{
\widetilde a_Q
=
\widetilde a_{Q_r}^{ref}\circ\mathcal C_{Q,Q_r}.
}
\tag{NR10}
\]

This equality is exact.

In particular, the pure change of source scale contributes

\[
\boxed{
\Delta\log|\widetilde a|_{\rm pure\ rebase}=0.
}
\tag{NR11}
\]

There is no hidden positive real scale exponent.

---

## 4. Compatibility with the actual reference-rebase layer

The pinned file

`NavierStokes/ActualReferenceRebase.lean`

identifies the actual coefficients with the physical band amplitude:

\[
(\mathrm{actualCoefficients}).\mathrm{amplitude}_n
=
\mathrm{bandAmplitude}
\tag{NR12}
\]

at the corresponding common-reference point.

It also proves forward and backward source coherence using the same

- `bandChartEquiv`,
- `bandVelocityScale`,
- `bandScale`,

with

\[
\boxed{
\operatorname{bandVelocityScale}(h,n,m)
=
\operatorname{ratioPower}(Q_n,Q_m,A(h)).
}
\tag{NR13}
\]

Hence the exact physical-cycle rebase used by the source is precisely the
normalization in (NR10).

The cover change acts on the torus/copy argument; it introduces no positive
real scalar in the amplitude identity.

---

## 5. Characteristic coordinates

The Gate 2 characteristic coordinates

\[
\Xi=(A_C,A_P,G_P)
\]

are coefficients of normalized central/tail profile vectors.

When those profile vectors are written in the source-normalized velocity
scale, (NR10) shows that changing only the source band/reference does not
alter the real modulus of `Xi`.  The coordinate chart and torus argument
are transported, but the similarity amplitude factor cancels exactly.

Thus the characteristic parallel transport naturally decomposes as

\[
\boxed{
\mathcal B_j
=
\mathcal B_j^{dyn}
\mathcal B_j^{geom},
}
\tag{NR14}
\]

where

- `B_j^{geom}` contains the exact source chart/cover rebase and is
  modulus-neutral after natural normalization;
- `B_j^{dyn}` is the genuine physical evolution relative to that
  normalized moving reference.

Any long-time real growth obstruction must therefore come from
`B_j^{dyn}`, not from `q` or the dyadic scale ratio itself.

---

## 6. Relation to the source envelope

The pinned primary fundamental has reference envelope

\[
P(t)
=
\mathrm{referenceP}(\lambda,u,L,t),
\qquad
P'=\mathrm{referenceRate}\,P.
\]

The theorem
`PrimaryPulseBounds.fundamental_envelope_jets`
shows that, after factoring this exact envelope, moving-frame and viscosity
errors may contribute an extra rate of size `O(S^{-1})` in the fast
coordinate.

Over an `O(S)` fast interval this estimate permits an `O(1)` transfer.
Therefore the envelope theorem alone does **not** prove
`B_j^{dyn}=I+o(1)` over an old full source stage.

This distinction is essential:

\[
\boxed{
\text{pure scale rebase: exact neutral after normalization;}
}
\]

\[
\boxed{
\text{within-stage normalized dynamics: still requires analysis.}
}
\tag{NR15}
\]

---

## 7. Gate 2 consequence

The feared scale-growth scenario

\[
|\Xi_j|
\sim
q_j^{-c}
\]

cannot arise merely from repeatedly rebasing the same physical coefficient
between source scales.  Natural similarity covariance cancels that factor
exactly.

Hence Gate 2 has one fewer possible obstruction.

The remaining characteristic-growth question is:

> what is the real part of the genuine normalized within-stage monodromy
> after the exact reference envelope and exact band similarity factors have
> been removed?

This must be studied on the actual low-`u` Gate 1 stage geometry.  It
cannot be replaced by the coarse `O(S^{-1})` envelope-error bound if the
fast interval remains `O(S)`.

The preferred next theorem layer is

`beta21_lowu_gate2_within_stage_characteristic_monodromy.md`.

No global invariant cocycle, infinite cascade, or blow-up theorem is claimed
here.
