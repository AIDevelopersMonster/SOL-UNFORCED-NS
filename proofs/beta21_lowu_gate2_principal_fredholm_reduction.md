# Gate 2 principal Fredholm reduction for the low-`u` orbit cocycle

**Status:** PROVED PRINCIPAL COHOMOLOGICAL/FREDHOLM REDUCTION / FINITE CHARACTERISTIC-MOMENT MATCHING STILL OPEN.

This note starts Gate 2 from the exact local full-state theorem
`beta21_lowu_exact_finiteS_core_tail_local_reset.md`.

The spectral audit
`beta21_lowu_intercell_spectral_stability_audit.md`
shows that the canonical bilateral profile is not transversely attracting.
That fact kills naive accumulation of small inter-cell errors, but it does
**not** imply that the exact invariant-cocycle equation has an
infinite-dimensional obstruction.

The point of this note is that, in the natural analytic modulation space,
the principal cohomological operators have only finitely many characteristic
zeros.  After the corresponding finite moment conditions are removed, the
entire bilateral analytic complement has a bounded inverse.

No global cocycle is claimed here.  The remaining Gate 2 problem is reduced
to finite characteristic-moment matching plus source-small/finite-`S`
perturbation.

---

## 1. Principal reset symbols

For the low-`u` catalyst sector,

\[
\mathcal P_C=R^{-1}e^{\lambda_C R},
\qquad
\rho_C=0.3510126502440001\ldots,
\qquad
\lambda_C=-2.982607649202283\ldots .
\]

The canonical shift eigenvalue satisfies

\[
e^{\lambda_C\rho_C}=\rho_C .
\]

Put

\[
L_C:=\lambda_C\rho_C=\log\rho_C<0
\]

and normalize the shift spectral variable by

\[
\zeta=\rho_C z .
\]

Then the catalyst fixed-point/cohomological symbol is

\[
\boxed{
F_C(z)
:=
1-\frac{e^{L_C z}}{\rho_C z}.
}
\tag{G2F1}
\]

For the parent sector,

\[
\mathcal P_P=R^{-2}e^{\mu_P R},
\]

\[
\rho_P
=-2.147691668824314
+1.235899139340218,i,
\qquad
\mu_P=-0.845013757547658\ldots ,
\]

and

\[
e^{\mu_P\rho_P}=\rho_P^2 .
\]

Write

\[
A_P:=\mu_P\rho_P
=
1.814829007127034
-1.044351775683794,i
\]

and normalize

\[
\zeta=\rho_P z .
\]

Then

\[
\boxed{
F_P(z)
:=
1-\frac{e^{A_Pz}}{\rho_P^2z^2}.
}
\tag{G2F2}
\]

The exact invariant-profile equation at principal frozen scale is the
cohomological equation

\[
F_b(R_{\rm mod})w=f,
\tag{G2F3}
\]

where `R_mod` is the shift after removal of the canonical geometric factor.

---

## 2. Catalyst characteristic set on the modulation circle

Let

\[
|z|=1,
\qquad
z=e^{i\phi}.
\]

If `F_C(z)=0`, then

\[
e^{L_Cz}=\rho_C z.
\]

Taking absolute values and using `L_C=log rho_C` gives

\[
L_C\cos\phi=L_C.
\]

Since `L_C != 0`,

\[
\cos\phi=1.
\]

Hence

\[
\boxed{
F_C(z)=0, |z|=1
\quad\Longleftrightarrow\quad
z=1.
}
\tag{G2F4}
\]

The zero is simple.  Indeed

\[
F_C'(1)
=
1-L_C
\ne0.
\tag{G2F5}
\]

Thus the catalyst neutral/characteristic set on the natural modulation circle
contains exactly one point.

Notice that this is fully consistent with the instability audit.  Away from
`phi=0` the multiplier can have modulus larger than one; Fredholm
invertibility of `I-P_C` is governed by the equation `m_C=1`, not by
whether `|m_C|<1`.

---

## 3. Parent characteristic set on the modulation circle

Let again

\[
|z|=1.
\]

If `F_P(z)=0`, then

\[
e^{A_Pz}=\rho_P^2z^2.
\tag{G2F6}
\]

Because `mu_P` is real, complex conjugation of the canonical relation gives

\[
e^{\mu_P\bar\rho_P}=\bar\rho_P^2.
\]

Therefore both

\[
\boxed{z_1=1}
\tag{G2F7}
\]

and

\[
\boxed{
z_2=\frac{\bar\rho_P}{\rho_P}
=e^{-2i\arg\rho_P}
}
\tag{G2F8}
\]

are roots on the unit circle.

They are the only unit-circle roots.

Indeed, write

\[
A_P=a+ib,
\qquad b\ne0,
\qquad z=e^{i\phi}.
\]

Taking moduli in (G2F6) gives

\[
\Re(A_Pz)=\Re(A_P).
\tag{G2F9}
\]

Equivalently,

\[
a(\cos\phi-1)-b\sin\phi=0.
\]

The intersection of this nontrivial affine real condition with the unit
circle consists of exactly two points: `z=1` and the reflected point
`z=bar(A_P)/A_P=bar(rho_P)/rho_P`.  Both are already known to satisfy the
full complex equation.

Numerically,

\[
\arg\rho_P
=
2.619416765747896\ldots ,
\]

so

\[
\boxed{
\arg z_2
=
2\pi-2\arg\rho_P
=
1.044351775683794\ldots .
}
\tag{G2F10}
\]

Both zeros are simple.  At a root `z_*`,

\[
F_P'(z_*)
=
-\left(A_P-\frac2{z_*}\right).
\]

At `z_1=1` this is nonzero because

\[
2-A_P
=
0.185170992872966
+1.044351775683794,i
\ne0.
\]

At `z_2`,

\[
2-A_Pz_2
=
2-\mu_P\bar\rho_P
=
\overline{(2-A_P)}
\ne0.
\]

Hence

\[
\boxed{
\{F_P=0\}\cap\{|z|=1\}
=
\{1,z_2\},
}
\tag{G2F11}
\]

with two simple characteristic roots.

---

## 4. A zero-free annulus after finite factorization

The zeros of `F_C` and `F_P` are isolated.  Sections 2--3 identify all
zeros on the compact unit circle.

Therefore there exists

\[
\boxed{\sigma_2>0}
\tag{G2F12}
\]

such that in the closed annulus

\[
\mathfrak A_{\sigma_2}
=
\{e^{-\sigma_2}\le|z|\le e^{\sigma_2}\}
\tag{G2F13}
\]

the catalyst symbol has no zeros except `1`, and the parent symbol has no
zeros except `1,z_2`.

Hence one may factor

\[
\boxed{
F_C(z)=(z-1)G_C(z),
}
\tag{G2F14}
\]

and

\[
\boxed{
F_P(z)=(z-1)(z-z_2)G_P(z),
}
\tag{G2F15}
\]

where `G_C,G_P` are analytic and nonvanishing on
`mathfrak A_{sigma_2}`.

By the weighted Wiener lemma, the corresponding operators

\[
G_C(R_{mod}),
\qquad
G_P(R_{mod})
\]

have bounded inverses on every bilateral analytic sequence space with
radius

\[
0<\sigma<\sigma_2.
\tag{G2F16}
\]

Thus all possible loss of invertibility is concentrated in the explicit
linear shift factors in (G2F14)--(G2F15).

---

## 5. Exact division by one unit-circle shift factor

Let

\[
\mathcal A_\sigma
=
\left\{
f=(f_j)_{j\in\mathbb Z}:
\|f\|_\sigma
:=
\sum_j e^{\sigma|j|}|f_j|<\infty
\right\}.
\]

For a unit complex number `omega`, let

\[
\ell_\omega(f)
\]

denote evaluation of the bilateral Laurent transform at the corresponding
unit-circle character.  Equivalently, after the phase conjugation
`f_j -> omega^{-j}f_j`, it is the ordinary coefficient sum.

### Lemma

If

\[
\ell_\omega(f)=0,
\tag{G2F17}
\]

then

\[
(R-\omega)u=f
\tag{G2F18}
\]

has a solution `u in A_sigma` with

\[
\boxed{
\|u\|_\sigma
\le
\frac{C}{1-e^{-\sigma}}
\|f\|_\sigma .
}
\tag{G2F19}
\]

### Proof

Phase-conjugate to `omega=1`.  The condition becomes

\[
\sum_{j\in\mathbb Z}f_j=0.
\]

Choose the discrete antiderivative using the right tail for nonnegative
indices and, by the zero-sum identity, the left tail for negative indices.
For example, up to the harmless convention for whether `R` shifts
`j -> j-1` or `j -> j+1`,

\[
u_j=-\sum_{k>j}f_k
\]

on one side and the equivalent left-tail formula on the other.

Then

\[
\sum_{j\ge0}
e^{\sigma j}|u_j|
\le
\sum_{k>0}|f_k|
\sum_{0\le j<k}e^{\sigma j}
\le
\frac{1}{1-e^{-\sigma}}
\sum_{k>0}e^{\sigma k}|f_k|.
\]

The negative indices are identical after using the zero-sum condition.
This proves (G2F19).

So a unit-circle root costs **one finite characteristic moment**, not an
infinite-dimensional loss.

---

## 6. Catalyst and parent Fredholm complements

Define the catalyst characteristic-moment subspace

\[
\boxed{
Y_C
=
\ker\ell_1
\subset\mathcal A_\sigma .
}
\tag{G2F20}
\]

Using (G2F14), the Wiener inverse for `G_C`, and the division lemma,

\[
\boxed{
F_C(R_{mod})
:
X_C^{\perp}
\longrightarrow
Y_C
}
\tag{G2F21}
\]

has a bounded right inverse after one normalization of the catalyst
characteristic mode.

For the parent define

\[
\boxed{
Y_P
=
\ker\ell_1
\cap
\ker\ell_{z_2}.
}
\tag{G2F22}
\]

If `f in Y_P`, division by `R-1` produces a quotient that still vanishes
at `z_2`, because

\[
f(z_2)=0
\]

and `z_2 != 1`.  A second application of the division lemma therefore
removes `R-z_2`.  Combining with the Wiener inverse of `G_P` gives a
bounded right inverse on the parent complement:

\[
\boxed{
F_P(R_{mod})
:
X_P^{\perp}
\longrightarrow
Y_P .
}
\tag{G2F23}
\]

The constants depend on the chosen analytic radius and the separation
`|1-z_2|>0`, but are independent of the source level `S`.

Thus the principal frozen Gate 2 cohomological operator is Fredholm with a
finite characteristic block.

---

## 7. Interpretation of the earlier transverse instability

The spectral stability audit found

\[
|m_C|>1
\]

on the catalyst natural spectral circle away from the canonical point, and a
mixed stable/unstable parent spectrum.

This remains true.  It means that **forward errors cannot simply be
accumulated**.

But the exact invariant-profile equation does not ask for forward
attraction.  It asks to solve

\[
(I-\mathcal P_b)w=f.
\]

Sections 2--6 prove that, in the analytic modulation space, the obstruction
to this equation is finite-dimensional:

- one catalyst characteristic moment;
- two parent characteristic moments in the complexified orbit space.

All remaining bilateral analytic directions admit a bounded
cohomological inverse.

On the physical real slice the parent roots form a conjugate pair.  The
precise real parameter/gauge ledger for cancelling these characteristic
moments is the next finite-dimensional Gate 2 task and is **not** assumed in
this note.

---

## 8. Consequence for the exact inter-cell problem

Let the exact normalized gap transport over one near-one step be

\[
\widehat T_j=I+\mathcal D_j,
\qquad
\|\mathcal D_j\|
\le C\delta+r_j,
\qquad
r_j\to0,
\tag{G2F24}
\]

as targeted in
`cross_scale_renewal_section_shadowing_reduction.md`.

The inter-cell defect generated by transporting the exact local Gate 1 state
is therefore source-small/near-one:

\[
d_j=O(\delta)+o_j(1).
\tag{G2F25}
\]

The present theorem says that the projection of `d_j` onto the infinite
analytic complement can be corrected with a bounded operator.  One does
**not** have to tune infinitely many unstable orbit coordinates
independently.

The remaining obstruction is exactly the characteristic projection

\[
\boxed{
\big(
\ell_1(d_{C,j}),
\ell_1(d_{P,j}),
\ell_{z_2}(d_{P,j})
\big).
}
\tag{G2F26}
\]

Gate 2 is therefore reduced, at principal frozen-profile level, to:

1. derive the exact normalized short-log transport generator from the pinned
   source variables;
2. compute the characteristic moments (G2F26);
3. show that the available physical modulation parameters/gauges have full
   rank onto the real characteristic block;
4. apply the bounded analytic complement inverse above;
5. then perturb from the frozen principal operator to the exact finite-`S`
   source/PDE cocycle.

This is a finite-rank matching problem plus an already-controlled analytic
complement, not an infinite family of independent compatibility conditions.

---

## 9. What is proved and what remains open

### Proved here

1. The catalyst principal cohomological symbol has exactly one simple
   characteristic root on its natural modulation circle.
2. The parent symbol has exactly two simple roots there, the canonical root
   and its conjugate partner.
3. A sufficiently thin analytic annulus contains no additional roots.
4. After factoring those roots, the remaining symbol is Wiener-invertible.
5. Each unit-circle shift factor is invertible on the corresponding
   zero-moment subspace with an explicit analytic-lattice bound.
6. Hence the principal Gate 2 cohomological obstruction is finite-dimensional.

### Still open

1. The exact source-derived short-log normalized transport generator.
2. The real characteristic-moment/gauge rank for the low-`u` full-state
   cell.
3. Uniform finite-`S` persistence of the principal Fredholm decomposition.
4. The nonlinear nonautonomous invariant graph/cocycle.
5. Cauchy realizability and finite-energy summability of the resulting
   infinite sequence.
6. Any infinite cascade or singularity theorem.

The sharp next file should be

`beta21_lowu_gate2_characteristic_matching_rank.md`.

It must compute the transport defect moments and the derivative of those
moments with respect to the genuine physical modulation parameters.