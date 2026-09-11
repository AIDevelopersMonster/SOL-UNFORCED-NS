# Gevrey control of the radial compactification remainder

**Status:** PROVED QUANTITATIVE GE VREY ESTIMATE / CONDITIONAL EXACT-CLOSURE INPUT. This theorem upgrades the source's repeated-iteration flatness mechanism for the radial compactification remainder to an explicit stretched-exponential bound in a compactly supported Gevrey class.

It does not yet prove the complete nonlinear mean fixed point, but it removes the need to iterate the derivative-losing radial torus inverse indefinitely inside one Banach space.

## 1. Abstract radial remainder operator

Let `A_1` denote the source radial compactification remainder operator appearing in the axial mean construction, schematically of the form

\[
A_1=\mathcal R\circ (v_r\cdot\partial_y)^{-1}\circ \mathcal E,
\]

where `mathcal E` is a fixed finite-order differential/error operator and `mathcal R` is a fixed compactly supported reconstruction operator. The source iteration shows that repeated application of `A_1` gains a positive power of the small parameter while paying finitely many torus derivatives at each step.

We isolate the only structural input needed below:

there exist constants `r>=1`, `delta>0`, and `C>=1` such that for every integer `m>=0`,

\[
\boxed{
\|A_1 f\|_{C^m}
\le
C^{m+1}\varepsilon^\delta
\|f\|_{C^{m+r}}.
}
\tag{G1}

The source finite-stage calculus supplies estimates of this form, with fixed derivative loss and positive epsilon gain.

## 2. Compactly supported Gevrey class

Fix `s>1`. A compactly supported coefficient `f` belongs to the Gevrey class `G^s_L` if

\[
\boxed{
\|f\|_{G^s_L}
:=
\sup_{m\ge0}
\frac{L^m\|f\|_{C^m}}{(m!)^s}
<\infty.
}
\tag{G2}

Compactly supported nontrivial functions exist for every `s>1`.

For `0<L'<L`, the standard factorial inequality gives

\[
\boxed{
\|f\|_{C^{m+r}}
\le
\|f\|_{G^s_L}
L^{-(m+r)}((m+r)!)^s.
}
\tag{G3}

Using

\[
(m+r)!\le C_r^{m+1}m!\,(m+1)^r,
\]

we obtain

\[
\frac{(L')^m(m+r)!^s}{L^{m+r}m!^s}
\le
C_{r,s}L^{-r}
\left(\frac{L'}L\right)^m
(m+1)^{rs}.
\tag{G4}

The right-hand side is uniformly bounded in `m` because `L'/L<1`.

Therefore (G1) implies the radius-losing Gevrey estimate

\[
\boxed{
\|A_1f\|_{G^s_{L'}}
\le
C_{s,r,L,L'}\varepsilon^\delta
\|f\|_{G^s_L}.
}
\tag{G5}

Thus one application of the radial remainder loses Gevrey radius but **not** Gevrey order.

## 3. Iterated remainder and optimized truncation

Choose a decreasing sequence of radii

\[
L=L_0>L_1>\cdots>L_N>L_\infty>0
\]

with equal decrements

\[
L_j-L_{j+1}=\frac{L-L_\infty}{N}.
\]

The constant in (G5) grows at most polynomially in the inverse radius loss. Therefore for some exponent `p=p(r,s)` and constant `C_*`,

\[
\boxed{
\|A_1^Nf\|_{G^s_{L_\infty}}
\le
\left(C_*\varepsilon^\delta N^p\right)^N
\|f\|_{G^s_L}.
}
\tag{G6}

Choose

\[
\boxed{
N=N(\varepsilon)
=\left\lfloor c\varepsilon^{-\delta/(2p)}\right\rfloor
}
\tag{G7}

with `c>0` sufficiently small. Then

\[
C_*\varepsilon^\delta N^p
\le C_*c^p\varepsilon^{\delta/2}
<\frac12
\]

for sufficiently small `epsilon`.

Hence

\[
\|A_1^Nf\|_{G^s_{L_\infty}}
\le
2^{-N}\|f\|_{G^s_L}.
\]

Since `N~epsilon^{-delta/(2p)}`, we obtain

\[
\boxed{
\|A_1^Nf\|_{G^s_{L_\infty}}
\le
\exp\!\left(-c\varepsilon^{-\mu}\right)
\|f\|_{G^s_L},
\qquad
\mu=\frac{\delta}{2p}>0.
}
\tag{G8}

This is a quantitative stretched-exponential remainder.

## 4. Consequence for the axial mean correction

Suppose the source compact axial reconstruction gives

\[
\Delta\gamma
=\gamma_d-A_1\gamma_d.
\]

Iterating the correction `N` times gives a finite exact telescoping identity

\[
\boxed{
\sum_{j=0}^{N-1}\Delta\gamma[A_1^j\gamma_d]
=
\gamma_d-A_1^N\gamma_d.
}
\tag{G9}

The unresolved tail is therefore precisely `A_1^N gamma_d`, and (G8) yields

\[
\boxed{
\|A_1^N\gamma_d\|_{G^s_{L_\infty}}
\le
\exp(-c\varepsilon^{-\mu})
\|\gamma_d\|_{G^s_L}.
}
\tag{G10}

Thus the radial compactification defect can be made smaller than every algebraic power of `epsilon` by a **finite**, epsilon-dependent number of Gevrey corrections while preserving a positive limiting Gevrey radius.

## 5. Why this is stronger than C-infinity flatness for the unforced program

The source only needs the statement

\[
A_1^N\gamma_d=O(\varepsilon^A)
\]

for any prescribed finite `A`, because the remaining flat term may be left in the external force.

For the unforced program, a merely formal all-orders statement is insufficient unless the constants are controlled with the correction depth. The Gevrey estimate (G10) supplies such control and turns the arbitrary-order source iteration into one explicit stretched-exponential estimate.

This does **not** make the remainder exactly zero. Its role is different: it produces a tail small enough to be inserted into the exact forward mean fixed-point problem, where the characteristic inverse from `characteristic_fast_time_mean_inverse.md` has no torus derivative loss.

## 6. Hybrid exact mean closure strategy

The mean block can now be organized as follows.

1. Use the exact characteristic inverse `mathcal J_i` for the fast-time zero-average correction. This is derivative-loss free in the characteristic Gevrey norm.
2. Use the source finite-dimensional radial moment/Vandermonde correction exactly.
3. Apply only `N(epsilon)` radial compactification corrections, obtaining the stretched-exponential tail (G10).
4. Treat that tail, together with the ordinary algebraically small nonlinear mean residual, as the source term of one final forward contraction in the characteristic Gevrey space.

Because the final forward inverse does not lose torus derivatives, no infinite chain of radius losses is required.

## 7. Remaining estimate needed for exact closure

Let `m` denote the full mean correction and `z(m)` the already-constructed exact nonzero-harmonic forward solution. To finish the local zero-force theorem it now suffices to prove a local Lipschitz bound in one fixed positive-radius characteristic Gevrey space:

\[
\boxed{
\|\mathcal N_{\rm mean}(m)-\mathcal N_{\rm mean}(\tilde m)\|_{G^s_{L_\infty}}
\le
\eta_\ell
\|m-\tilde m\|_{G^s_{L_\infty}},
\qquad
\eta_\ell\to0.
}
\tag{G11}

The source exponent gain `0.9-2kappa_s`, the nonzero-wave smallness, and the stretched-exponential radial tail are precisely the available small factors for (G11).

Therefore the sharp remaining local task is no longer a Nash--Moser theorem. It is a **single-space Gevrey Lipschitz estimate for the coupled mean/nonzero forward map**.
