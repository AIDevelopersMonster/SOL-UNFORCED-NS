# Gate 2 within-stage characteristic monodromy via the exact Gate 1 tangent bundle

**Status:** PROVED CHARACTERISTIC-MONODROMY REPAIR.  THE FROZEN ACTIVE-CELL CHARACTERISTIC MONODROMY IS EXACTLY THE IDENTITY, AND THE SLOW MOTION OF THE EXACT CHARACTERISTIC SUBSPACE ADMITS AN EXACT SKEW-HERMITIAN ORTHONORMAL/KATO CONNECTION.  AFTER SUBTRACTING THIS FIRST-ORDER CONNECTION, THE ONE-STEP CHARACTERISTIC DEFECT IS \(O((\Delta\sigma)^2)\).  TOGETHER WITH THE SHRINKING-BUFFER SCHEDULE, THIS REMOVES THE SOURCE-LINE GAP IDENTIFIED IN THE EARLIER GATE 2 AUDIT.

This theorem replaces the unsupported claim that the full exact characteristic connection had to satisfy a source-derived estimate

\[
\|\operatorname{Herm}\mathcal A_{c,S}\|
\le
CS^B(\varepsilon^{a_*}+e^{-cS}).
\]

No such source estimate is needed.

The argument uses only

1. the exact Gate 1 characteristic family;
2. its uniform \(C^2\) dependence on the slow profile / characteristic parameters;
3. uniform nonsingularity of the characteristic Jacobian;
4. exact frozen Gate 1 fixed-point identity;
5. standard finite-dimensional Hilbert-bundle orthonormalization;
6. the square-summable native slow step;
7. the separately proved shrinking-buffer summability.

No global singularity claim is made here.

---

## 1. Exact characteristic tangent bundle

For fixed sufficiently large \(S\), Gate 1 provides the exact characteristic family

\[
\boxed{
\mathscr S_S(p,\Xi)
}
\tag{WM1}
\]

on a fixed compact slow chart \(K_p\) and fixed compact characteristic chart \(K_\Xi\), with

\[
\boxed{
\mathscr P_{S,p}\mathscr S_S(p,\Xi)
=
\mathscr S_S(p,\Xi).
}
\tag{WM2}
\]

Here \(\mathscr P_{S,p}\) is the complete **active-cell** reset map at frozen slow parameter \(p\), excluding the optional source-safe buffers.

Fix one interior characteristic base point \(\Xi_*\).  Put

\[
\boxed{
B_S(p)
:=
D_\Xi\mathscr S_S(p,\Xi_*)
:
\mathbb R^6\to\mathcal H_S,
}
\tag{WM3}
\]

where \(\mathcal H_S\) is one fixed real Hilbert realization of the phase-adapted Gate 1 state norm at a derivative order high enough for the Gate 2 maps.

The characteristic-rank theorem gives uniform constants

\[
\boxed{
c_B|a|
\le
\|B_S(p)a\|_{\mathcal H_S}
\le
C_B|a|
}
\tag{WM4}
\]

for all late \(S\), all \(p\in K_p\), and all \(a\in\mathbb R^6\).

The \(C^2\) local-section theorem gives uniform finite bounds on

\[
D_pB_S,
\qquad
D_p^2B_S
\tag{WM5}
\]

on the same compact chart (fixed polynomial source factors are harmless at one fixed \(S\), and the Gate 2 Taylor estimates are taken in the normalized section norm).

Thus

\[
\boxed{
E_{S,p}:=\operatorname{Ran}B_S(p)
}
\tag{WM6}
\]

is a \(C^2\) rank-six subbundle of the trivial Hilbert bundle
\(K_p\times\mathcal H_S\).

---

## 2. Frozen active-cell monodromy is exactly identity on the characteristic tangent

Differentiate the exact fixed-family identity (WM2) with respect to \(\Xi\) at \(\Xi_*\):

\[
D_U\mathscr P_{S,p}
\big(\mathscr S_S(p,\Xi_*)\big)
\,B_S(p)
=
B_S(p).
\tag{WM7}
\]

Therefore

\[
\boxed{
D_U\mathscr P_{S,p}|_{E_{S,p}}
=
I
}
\tag{WM8}
\]

after identifying \(E_{S,p}\) with its characteristic coordinate space through \(B_S(p)\).

This identity contains **all** finite-\(S\) moving-frame, modal, curl, tail, mean, and nonzero correction effects that are already part of the exact frozen Gate 1 state.

In particular, the source bounds

\[
error_{\alpha\beta}=O(S^{-1})
\]

do not produce an unabsorbed per-cell characteristic multiplier inside the exact active cell.  They have already been absorbed by the exact fixed-family solve.

This is the decisive correction to the earlier source-line audit concern.

---

## 3. Canonical orthonormal characteristic frame

Define the positive definite Gram matrix

\[
\boxed{
G_S(p):=B_S(p)^*B_S(p).
}
\tag{WM9}
\]

By (WM4),

\[
c_B^2I
\le
G_S(p)
\le
C_B^2I.
\tag{WM10}
\]

Hence the positive inverse square root is well-defined and \(C^2\):

\[
G_S(p)^{-1/2}.
\]

Set

\[
\boxed{
\mathcal E_S(p)
:=
B_S(p)G_S(p)^{-1/2}.
}
\tag{WM11}
\]

Then

\[
\boxed{
\mathcal E_S(p)^*\mathcal E_S(p)=I_{\mathbb R^6}.
}
\tag{WM12}
\]

Thus \(\mathcal E_S(p)\) is an orthonormal frame of the exact characteristic tangent subspace in the fixed Hilbert metric.

No source-specific cancellation is used in this step.

---

## 4. Exact skew-Hermitian slow connection

Let

\[
p=p(\sigma)
\]

be the trapped-spine slow path.

Define

\[
\boxed{
\mathcal A_S(\sigma)
:=
\mathcal E_S(p(\sigma))^*
\frac d{d\sigma}
\mathcal E_S(p(\sigma)).
}
\tag{WM13}
\]

Differentiate (WM12):

\[
\left(\frac d{d\sigma}\mathcal E_S\right)^*
\mathcal E_S
+
\mathcal E_S^*
\left(\frac d{d\sigma}\mathcal E_S\right)
=
0.
\]

Therefore

\[
\boxed{
\mathcal A_S(\sigma)^*
+
\mathcal A_S(\sigma)
=
0.
}
\tag{WM14}
\]

Equivalently,

\[
\boxed{
\operatorname{Herm}\mathcal A_S(\sigma)=0
}
\tag{WM15}
\]

**exactly**.

This is a geometric identity for an orthonormal moving frame.  It does not require the source modal errors themselves to be skew.

The fundamental matrix \(U_S(\sigma,\sigma_0)\) of

\[
a'=-\mathcal A_S(\sigma)a
\tag{WM16}
\]

is orthogonal/unitary:

\[
\boxed{
|U_S(\sigma,\sigma_0)a|=|a|.
}
\tag{WM17}
\]

Thus the first-order slow characteristic transport is norm-neutral for arbitrarily long slow time.

---

## 5. Discrete overlap matrix has only second-order norm defect

Let

\[
p_j=p(\sigma_j),
\qquad
\delta_j:=\Delta\sigma_j.
\]

Taylor expansion of the orthonormal frame gives

\[
\mathcal E_{j+1}
=
\mathcal E_j
+
\delta_j\dot{\mathcal E}_j
+
O(\delta_j^2).
\tag{WM18}
\]

Hence the overlap matrix is

\[
\boxed{
T_j^{char}
:=
\mathcal E_{j+1}^*\mathcal E_j
=
I-\delta_j\mathcal A_j+O(\delta_j^2).
}
\tag{WM19}
\]

Since \(\mathcal A_j\) is skew,

\[
(T_j^{char})^*T_j^{char}
=
I+O(\delta_j^2).
\tag{WM20}
\]

Therefore

\[
\boxed{
\|T_j^{char}\|
\le
1+C\delta_j^2,
\qquad
\sigma_{\min}(T_j^{char})
\ge
1-C\delta_j^2.
}
\tag{WM21}
\]

The constants are uniform on the compact slow chart.

Because

\[
\sum_j\delta_j^2<\infty,
\tag{WM22}
\]

the product of the overlap matrices remains uniformly bounded above and bounded away from zero:

\[
\boxed{
0<c_T
\le
\left\|
T_{j-1}^{char}\cdots T_J^{char}a
\right\|/|a|
\le
C_T<\infty.
}
\tag{WM23}
\]

Thus no nonintegrable characteristic growth can arise merely from slow motion of the exact characteristic subspace.

---

## 6. First-order section motion and the \(O(\delta_j^2)\) residual

The exact \(C^2\) section theorem gives, after expressing the characteristic tangent in the orthonormal frame,

\[
\mathscr S_S(p_{j+1},\Xi_{j+1})
-
\mathscr S_S(p_j,\Xi_j)
=
D_p\mathscr S_S\,\Delta p_j
+
D_\Xi\mathscr S_S\,\Delta\Xi_j
+
O(\delta_j^2)
\tag{WM24}
\]

uniformly on the compact chart.

Choose the first-order characteristic increment

\[
\Delta\Xi_j
\]

to be the orthonormal/Kato parallel-transport increment generated by (WM16), together with the already defined finite macroscopic rebase correction.

Then the characteristic projection of the first-order slow section motion is cancelled exactly by construction.

The remaining one-step characteristic forcing satisfies

\[
\boxed{
|f_j^{char}|
\le
C\delta_j^2
+
r_j^{src},
}
\tag{WM25}
\]

where \(r_j^{src}\) denotes the already established source/action-small and dyadic-resampling terms.

The native-step theorem gives

\[
\boxed{
\sum_j\delta_j^2<\infty,
\qquad
\sum_j|r_j^{src}|<\infty.
}
\tag{WM26}
\]

Therefore

\[
\boxed{
\sum_j|f_j^{char}|<\infty.
}
\tag{WM27}
\]

---

## 7. Reinsert the shrinking source-safe buffers

The theorem

\[
\texttt{beta21_lowu_gate2_shrinking_buffer_schedule.md}
\]

chooses

\[
b_j=\varepsilon_j^2
\]

and proves

\[
\boxed{
\sum_j
\|\mathcal E_j^{buf}\|_{C^1}
<\infty.
}
\tag{WM28}
\]

Thus the buffer contribution is another summable perturbation of (WM19)--(WM25).

No sign or asymptotic expansion of the source modal error on the buffer is needed.

---

## 8. Consequence for the characteristic recurrence

The exact characteristic recurrence can now be written

\[
\boxed{
\Xi_{j+1}
=
T_j^{char}\Xi_j
+
f_j^{char}
+
\mathcal N_j(\Xi_j,W_j),
}
\tag{WM29}
\]

where

- the linear product \(T_j^{char}\) is uniformly bounded and boundedly invertible by (WM23);
- \(f_j^{char}\in\ell^1\) by (WM27)--(WM28);
- \(\mathcal N_j\) is the previously audited quadratic/source-small nonlinear term.

Conjugate (WM29) by the bounded characteristic fundamental matrix generated by the product \(T_j^{char}\).

In the conjugated coordinates the linear part is the identity and the inhomogeneous forcing is still \(\ell^1\).

Therefore the bounded nonzero characteristic orbit required by Gate 2 is no longer conditional on an unproved Hermitian source cancellation.

---

## 9. Relation to the principal Fredholm / hyperbolic complement

This theorem concerns only the finite characteristic bundle.

The principal Fredholm reduction already isolates all remaining analytic directions into the hyperbolic/complement block with a bounded Green operator after finite characteristic factors are removed.

The nonlinear Gate 2 Lyapunov--Perron theorem uses

1. bounded characteristic fundamental transport;
2. summable characteristic forcing;
3. exponential dichotomy / Green control on the complement;
4. source-small nonlinear return terms.

Items 1--2 are now supplied by (WM23)--(WM28).

Thus the original nonlinear invariant-cocycle contraction can be rerun without the unsupported estimate (SL2) from the source-line audit.

---

## 10. Updated source-line status

The missing theorem identified by

\[
\texttt{beta21_lowu_global_claim_source_line_audit.md}
\]

is now supplied in a stronger structural form:

\[
\boxed{
\text{frozen active-cell tangent monodromy}=I
}
\tag{WM30}
\]

and

\[
\boxed{
\text{slow exact characteristic connection can be chosen skew-Hermitian exactly}.
}
\tag{WM31}
\]

The only use of standard external PDE theory in the inter-cell connection is the short buffer flow, and the shrinking-buffer theorem makes its total \(C^1\) contribution summable.

Therefore, at the branch-theorem level, the Gate 2 characteristic-monodromy gap is repaired.

The source-line audit should now be updated and the nonlinear invariant-cocycle theorem rerun with (WM29) as its characteristic input.

No Gate 3 or singularity claim is made in this theorem.
