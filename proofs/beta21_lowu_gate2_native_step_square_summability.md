# Gate 2 square summability of the source-native stage steps

**Status:** PROVED FROM THE EXISTING `sigma` SCHEDULE AND DYADIC SOURCE HIERARCHY.

The nonlinear characteristic cocycle should not count the full
`O(Delta sigma_j)` variation of the exact local section as an error.  That
first-order variation is transported by the covariant characteristic frame.
The remaining Taylor defect is quadratic in the source-native stage length.
This note proves that those quadratic defects are summable.

The result uses only the already-proved schedule

\[
\Delta\sigma_j
:=\sigma_{j+1}-\sigma_j
=\Lambda\varepsilon_jS_j,
\qquad
\varepsilon_j=q_j^h,
\tag{SS1}
\]

the trapped-spine comparison `q(sigma) asymp e^{-sigma}`, and the source
choice `S(n)=n^2`.

---

## 1. Dyadic index is linear in logarithmic time

On the source hierarchy

\[
Q_n=2^{-n}.
\]

Along the trapped spine,

\[
c_qe^{-\sigma}
\le q(\sigma)
\le C_qe^{-\sigma}.
\tag{SS2}
\]

If stage `j` lies in dyadic band `n_j`, then

\[
Q_{n_j+1}\le q_j\le Q_{n_j},
\]

so

\[
n_j\log2
=
\sigma_j+O(1).
\tag{SS3}
\]

Consequently

\[
\boxed{
S_j=n_j^2
\le C(1+\sigma_j)^2.
}
\tag{SS4}
\]

The same estimate holds for the finite number of physical substeps carried
inside one dyadic band.

---

## 2. Pointwise upper bound for one stage length

From (SS2),

\[
\varepsilon_j=q_j^h
\le C e^{-h\sigma_j}.
\]

Combining with (SS1), (SS4),

\[
\boxed{
0<\Delta\sigma_j
\le
C_\Lambda
e^{-h\sigma_j}(1+\sigma_j)^2.
}
\tag{SS5}
\]

In particular `Delta sigma_j ->0`, as already used in the source-native
stage theorem.

Put

\[
f(\sigma)
:=
C_\Lambda e^{-h\sigma}(1+\sigma)^2.
\tag{SS6}
\]

After increasing the starting level beyond `2/h`, the function `f` is
strictly decreasing.

---

## 3. Quadratic stage lengths form a convergent series

Because

\[
\Delta\sigma_j
\le f(\sigma_j),
\]

we have

\[
(\Delta\sigma_j)^2
\le
f(\sigma_j)\Delta\sigma_j.
\tag{SS7}
\]

For late `j`, monotonicity of `f` gives the elementary upper Riemann-sum
comparison

\[
f(\sigma_j)\Delta\sigma_j
\le
C
\int_{\sigma_j}^{\sigma_{j+1}}
f(s)\,ds
\tag{SS8}
\]

with one harmless fixed constant, since
`Delta sigma_j ->0` and the logarithmic derivative of `f` is bounded on
the late half-line.

Summing,

\[
\sum_{j\ge j_0}
(\Delta\sigma_j)^2
\le
C
\int_{\sigma_{j_0}}^\infty
e^{-hs}(1+s)^2\,ds.
\tag{SS9}
\]

The integral is finite for every fixed `h>0`.  Therefore

\[
\boxed{
\sum_{j\ge j_0}
(\Delta\sigma_j)^2
<\infty.
}
\tag{SS10}
\]

Moreover its tail tends to zero as `j_0->infinity`:

\[
\boxed{
\sum_{j\ge J}
(\Delta\sigma_j)^2
\longrightarrow0.
}
\tag{SS11}
\]

No geometric q-decay in the stage index is required.

---

## 4. More general powers

Exactly the same argument gives, for every `p>1`,

\[
\boxed{
\sum_j(\Delta\sigma_j)^p<\infty.
}
\tag{SS12}
\]

Indeed,

\[
(\Delta\sigma_j)^p
\le
f(\sigma_j)^{p-1}\Delta\sigma_j,
\]

and

\[
\int^\infty
e^{-(p-1)hs}(1+s)^{2(p-1)},ds
<\infty.
\]

The borderline `p=1` diverges, as it must, because

\[
\sum_j\Delta\sigma_j
=
\sigma_\infty-\sigma_0
=
\infty.
\tag{SS13}
\]

Thus the source-native schedule has precisely the desired structure:

- first-order stage motion accumulates and reaches the singular clock;
- every superlinear Taylor remainder is summable.

---

## 5. Consequence for characteristic transport

Let `S_exact(sigma)` denote a `C^2` family of exact local Gate 1
characteristic sections in a covariant characteristic frame.  Taylor's
formula over one stage gives

\[
S_{exact}(\sigma_{j+1})
=
S_{exact}(\sigma_j)
+
D_\sigma S_{exact}(\sigma_j)\Delta\sigma_j
+
O((\Delta\sigma_j)^2).
\tag{SS14}
\]

If the first-order term is included in the characteristic parallel
transport, the residual canonical forcing obeys

\[
\boxed{
\|d_j^c\|
\le
C(\Delta\sigma_j)^2
+d_j^{dyad}
+d_j^{src},
}
\tag{SS15}
\]

where the dyadic profile term is already `O(n^{-2})` and the source
correction has positive epsilon/action gain.

By (SS10), the first term in (SS15) is summable.

Hence the only new regularity needed for the center part of Gate 2 is a
uniform `C^2` exact-section theorem.  One does **not** need
`sum Delta sigma_j<infinity`, and one must not treat the first-order center
motion as an error.

---

## 6. What is proved and what remains

### Proved here

\[
\boxed{
\sum_j(\Delta\sigma_j)^2<\infty.
}
\]

More generally all powers greater than one are summable.

### Remaining Gate 2 use

1. upgrade the exact Gate 1 parameter/state map from the recorded uniform
   `C^1` dependence to uniform `C^2` (or any `C^{1,alpha}` with
   `alpha>0`);
2. define the exact first-order characteristic parallel transport along that
   section;
3. combine the summable quadratic remainder with the analytic hyperbolic
   Green operator and the finite characteristic coordinates.

The preferred next theorem is

`beta21_lowu_gate2_C2_local_section.md`.
