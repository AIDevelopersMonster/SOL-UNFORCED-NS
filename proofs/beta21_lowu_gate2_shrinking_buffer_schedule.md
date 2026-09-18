# Gate 2 shrinking-buffer refinement of the constant-fast-cell schedule

**Status:** PROVED SCHEDULE REFINEMENT.  THE FIXED POSITIVE BUFFER LENGTH USED IN THE EARLIER CONSTANT-FAST SCHEDULE IS A DESIGN CHOICE, NOT A SOURCE-IMPOSED LOWER BOUND.  ONE MAY CHOOSE POSITIVE SHRINKING BUFFERS \(b_j=\varepsilon_j^2\), WHICH MAKE ALL BUFFER-ONLY CHARACTERISTIC DRIFT ABSOLUTELY SUMMABLE.

This note repairs the buffer part of the source-line audit in

\[
\texttt{beta21_lowu_global_claim_source_line_audit.md}.
\]

It does **not** yet close the within-stage characteristic monodromy of the slowly varying exact active-cell family.  That is the next theorem.

---

## 1. Intrinsic active-cell fast length

The source-slot bridge proves that one exact low-\(u\) active cell has source-fast length

\[
\ell_{cell,j}
\]

with fixed bounds

\[
\boxed{
0<c_v\le \ell_{cell,j}\le C_v<\infty
}
\tag{SB1}
\]

for all sufficiently late levels.

This lower bound belongs to the active reset cell itself.

The earlier constant-fast schedule introduced an **additional desired buffer**

\[
B_v>0
\]

and chose the total allocation constant \(\Lambda\) large enough that

\[
c_V\Lambda>C_v+2B_v.
\]

No source theorem used in that proof imposes a level-independent lower bound on the extra entrance/exit buffer.

Thus \(B_v\) may be replaced by any positive sequence tending to zero.

---

## 2. Choose square-small fast buffers

Set

\[
\boxed{
b_j:=\varepsilon_j^2.
}
\tag{SB2}
\]

On the constant-fast schedule,

\[
\varepsilon_j\asymp j^{-1},
\]

so

\[
\boxed{
b_j\asymp j^{-2},
\qquad
\sum_j b_j<\infty.
}
\tag{SB3}
\]

Choose \(\Lambda\) once so that

\[
c_V\Lambda>C_v+1.
\tag{SB4}
\]

For all sufficiently late \(j\),

\[
2b_j<1,
\]

hence

\[
c_V\Lambda
>
C_v+2b_j.
\tag{SB5}
\]

Therefore every allocated stage still contains

1. one complete exact active low-\(u\) cell;
2. one positive entrance buffer of fast length \(b_j\);
3. one positive exit buffer of fast length \(b_j\).

No packing or source-support estimate is lost.

---

## 3. Buffer flow is a summable perturbation

Let

\[
\mathcal B_{j}^{in}(b),
\qquad
\mathcal B_{j}^{out}(b)
\]

be the normalized physical unforced Navier--Stokes flow maps on the source-safe buffer chart.

On the fixed compact smooth Gate 1 state neighborhood, standard local wellposedness and smooth dependence give, at the fixed finite derivative order used in Gate 2,

\[
\boxed{
\|\mathcal B_j^\pm(b)-I\|
\le C b
}
\tag{SB6}
\]

and

\[
\boxed{
\|D_U\mathcal B_j^\pm(b)-I\|
\le C b
}
\tag{SB7}
\]

for \(0\le b\le b_0\), after using the same normalized chart and one fixed regularity reserve.

The constant is uniform for late stages because the normalized Gate 1 family remains in one fixed compact source chart.

At \(b=b_j\),

\[
\boxed{
\|\mathcal B_j^\pm(b_j)-I\|
+
\|D_U\mathcal B_j^\pm(b_j)-I\|
\le
C\varepsilon_j^2.
}
\tag{SB8}
\]

Therefore

\[
\boxed{
\sum_j
\left(
\|\mathcal B_j^\pm(b_j)-I\|
+
\|D_U\mathcal B_j^\pm(b_j)-I\|
\right)
<\infty.
}
\tag{SB9}
\]

This estimate treats the **entire** bounded normalized buffer generator, not only the \(O(S^{-1})\) modal error.

---

## 4. Source modal error on the shrinking buffer

The pinned source gives normalized moving-frame/modal errors

\[
|error_{\alpha\beta}|
\le
C/S_j
\]

on the actual source slot.

Over a fast interval \(b_j\),

\[
\boxed{
\int_{buffer}
|error_{\alpha\beta}|\,dv
\le
C\frac{b_j}{S_j}.
}
\tag{SB10}
\]

Thus

\[
\sum_j\frac{b_j}{S_j}
<\infty
\tag{SB11}
\]

a fortiori.

No sign analysis of the buffer modal error is required.

---

## 5. The global clock is unchanged

The total source-fast allocation per stage remains \(O(1)\):

\[
\ell_{cell,j}+2b_j
\le
C_v+o(1).
\]

Hence the logarithmic schedule remains

\[
\boxed{
\Delta\sigma_j=\Lambda\varepsilon_j.
}
\tag{SB12}
\]

All earlier clock conclusions remain valid:

\[
\sigma_j\to\infty,
\qquad
t_j\uparrow1,
\qquad
q_j\asymp j^{-1/h},
\qquad
\varepsilon_j\asymp j^{-1},
\qquad
S_j\asymp(\log j)^2,
\tag{SB13}
\]

and

\[
\sum_j(\Delta\sigma_j)^2<\infty.
\tag{SB14}
\]

The buffers consume only a summable subportion of the available fast time.

---

## 6. Updated Gate 2 one-step decomposition

Let

\[
\mathcal F_j^{act}
\]

denote the exact active-cell map, including the exact Gate 1 reset and natural rebase conventions, but excluding the two extra source-safe buffers.

With shrinking buffers, the complete one-step map is

\[
\boxed{
\mathcal F_j
=
\mathcal B_j^{out}(b_j)
\circ
\mathcal F_j^{act}
\circ
\mathcal B_j^{in}(b_j).
}
\tag{SB15}
\]

Equations (SB8)--(SB9) imply

\[
\boxed{
\mathcal F_j
=
\mathcal F_j^{act}
+
\mathcal E_j^{buf},
\qquad
\sum_j
\|\mathcal E_j^{buf}\|_{C^1}
<\infty
}
\tag{SB16}
\]

on the fixed characteristic/state chart.

Thus the buffers are now ordinary summable forcing and do not contribute to the long-time characteristic exponent.

---

## 7. What remains

This refinement removes the buffer term from the Gate 2 kill criterion.

The only remaining monodromy question concerns the variation of the **exact active-cell characteristic family itself** along the slow trapped spine.

The next theorem must prove that its Hermitian connection rate satisfies at least

\[
\boxed{
\|\operatorname{Herm}\mathcal A_{c,S}^{act}\|
\le
C/S
+
CS^B(\varepsilon^{a_*}+e^{-cS}).
}
\tag{SB17}
\]

Since

\[
S(\sigma)\asymp\sigma^2,
\]

the \(C/S\) rate is integrable in \(\sigma\).

If (SB17) holds, bounded nonzero characteristic transport follows and the nonlinear Gate 2 cocycle can be restored, with the shrinking buffers contributing only the summable correction (SB16).

If instead the exact active-cell family has a nonintegrable \(O(1)\) positive Hermitian connection rate, the global line fails even though the buffers have been neutralized.

No Gate 2 closure or singularity claim is made in this note.
