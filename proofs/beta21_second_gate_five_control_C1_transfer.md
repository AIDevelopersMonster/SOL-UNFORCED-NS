# Five-control `C^1` exact transfer for the terminal second-gate cancellation bank

**Status:** PROVED CONDITIONAL PARAMETER-TRANSFER THEOREM. Assume the finite support handoff architecture of `beta21_second_gate_terminal_homogeneous_cancellation_bank.md`: the routed `P-D` collision is completed first, the parent packets are absent from the terminal correction microcollars, and the five direct homogeneous controls are placed in ordered source-admissible microcollars with no undesignated order-one cross-overlap. Then the exact phase-adapted zero-residual solve depends `C^1` on the five complex terminal control amplitudes and the exact second-gate exit Jacobian is

\[
D_p\mathcal G_{2,\ell}=I_5+o(1).
\]

Hence the finite terminal correction map is locally invertible for all sufficiently high dyadic levels. Under the handoff hypothesis, the second gate is therefore closed at the exact local PDE level.

The only remaining second-gate obstruction is the support/handoff theorem itself.

## 1. Parameterized designated field

Let

\[
p=(p_1,\ldots,p_5)\in\mathbb C^5
\]

be the amplitudes of the five source-native homogeneous growing controls for

\[
(E,H_1,H_2,H_3,H_4).
\]

Fix a compact neighborhood

\[
K_p=\{p:|p-p^0|\le r_p\}
\]

of the principal cancellation vector

\[
p^0=Y_*-y^{pre}.
\]

By construction each control is a fixed allowed homogeneous pulse multiplied only by its scalar amplitude. Therefore every source packet seminorm of the designated field and its first `p` derivative is bounded uniformly on `K_p`:

\[
\boxed{
\sup_{p\in K_p}
\bigl(
\|U_{des}(p)\|_{pkt}
+\|D_pU_{des}(p)\|_{pkt}
\bigr)
\le C_{K_p}.
}
\tag{T5C1}
\]

No high phase is differentiated with respect to `p`.

## 2. Finite ordered microcollars do not change source exponents

The collision collar plus the five terminal correction collars form one fixed finite ordered family. On each microcollar the source packet calculus is the same as in the one-collar theorem; between collars one uses homogeneous forward transport in the envelope-renormalized norm.

A finite concatenation changes only polynomial powers of `S_*`. Therefore the stage-zero nonzero residual and its parameter derivative obey

\[
\boxed{
\|f_p\|_{\mathfrak A_{\sigma,0}}
+\|D_pf_p\|_{\mathfrak A_{\sigma,0}}
\le
CS_*^A
\left(
\varepsilon^{1/5}+e^{-cS_*}
\right).
}
\tag{T5C2}
\]

Likewise the mean forcing satisfies

\[
\boxed{
\|F_{mean,p}\|
+\|D_pF_{mean,p}\|
\le
CS_*^A\varepsilon^{1-\kappa_s}.
}
\tag{T5C3}
\]

The support-handoff assumption is essential here: it excludes any new order-one designated overlap not already present in the finite principal map.

## 3. `C^1` nonzero solve

For fixed mean input `m`, the full nonzero coefficient equation has the form

\[
\partial_vz
=\mathcal L_{p,m}(v)z
+f_{p,m}
+\mathcal B(z,z).
\]

Uniform boundedness of the finite designated coefficients gives

\[
\boxed{
\|\mathcal K_{p,m}z\|_{\mathfrak A_{\sigma,0}}
+
\|D_p\mathcal K_{p,m}z\|_{\mathfrak A_{\sigma,0}}
\le C\|z\|_{\mathfrak A_{\sigma,1}}.
}
\tag{T5C4}
\]

The full linear propagator and its parameter derivative are therefore uniformly bounded on the finite ordered stage:

\[
\boxed{
\|V_{p,m}(v,w)\|
+\|D_pV_{p,m}(v,w)\|
\le C.
}
\tag{T5C5}
\]

The nonlinear Duhamel map is a contraction on a ball of radius

\[
\rho_\ell
\le
CS_*^A
\left(
\varepsilon^{1/5}+e^{-cS_*}
\right)
\to0.
\]

The parameter-dependent contraction theorem yields a unique `C^1` solution

\[
z=z(p,m)
\]

with

\[
\boxed{
\|D_pz(p,m)\|_X
\le
CS_*^{A'}
\left(
\varepsilon^{1/5}+e^{-cS_*}
\right)
=o(1).
}
\tag{T5C6}
\]

## 4. `C^1` mean solve

Insert the exact nonzero solution into the phase-adapted mean fixed-point map. The finite number of additional microcollars introduces only polynomial factors in `S_*`, while every nonlinear mean Lipschitz term retains a positive epsilon exponent.

Thus the contraction factor still tends to zero, and for high enough levels there is a unique `C^1` mean correction

\[
m=m(p)
\]

with

\[
\boxed{
\|D_pm(p)\|=o(1).
}
\tag{T5C7}
\]

Consequently

\[
\boxed{
\|D_pz(p,m(p))\|_X=o(1).
}
\tag{T5C8}
\]

## 5. Exact zero residual

For every `p\in K_p`, define

\[
U_\ell(p)
=U_{des,\ell}(p)+z_\ell(p)+m_\ell(p).
\]

The nonzero fixed point kills all nonzero harmonic residuals and the mean fixed point kills the angular mean. Therefore

\[
\boxed{
\mathcal N_{phys}(\mathcal R_\ell U_\ell(p))=0
}
\tag{T5C9}
\]

through the entire finite ordered second-gate stage.

The five terminal controls are internal homogeneous packet amplitudes, not external forcing terms.

## 6. Exact five-coordinate exit map

Let

\[
\mathcal G_{2,\ell}(p)
=(E,H_1,H_2,H_3,H_4)_{out}.
\]

At frozen principal level the terminal homogeneous bank was normalized so that

\[
D_p\mathcal G_{2,0}=I_5.
\tag{T5C10}
\]

The designated source-frame/curl corrections contribute

\[
O(S_*^{-1})+O(S_*^A\varepsilon^\delta)
\]

to the finite exit Jacobian. The exact nonzero and mean corrections contribute `o(1)` by (T5C7)--(T5C8). Hence

\[
\boxed{
D_p\mathcal G_{2,\ell}
=I_5+o(1)
}
\tag{T5C11}
\]

uniformly on a sufficiently small fixed neighborhood of `p^0`.

Therefore, for sufficiently high levels,

\[
\boxed{
|\det D_p\mathcal G_{2,\ell}|
\ge\frac12.
}
\tag{T5C12}
\]

## 7. Exact terminal cancellation

The exact exit map differs from the principal map by `o(1)` in `C^1`. The quantitative inverse/implicit-function theorem therefore gives a unique nearby vector

\[
\boxed{p_\ell=p^0+o(1)}
\tag{T5C13}
\]

such that

\[
\boxed{
(E,H_1,H_2,H_3,H_4)_{out}
=(E_*,0,0,0,0).
}
\tag{T5C14}
\]

Every other naturally critical lattice character has a negative leaf-action margin by the full second-gate audit; high-beta modes lie in the forward-stable complement.

## 8. Conditional closure statement

Assuming the support handoff conditions

\[
P,D\notin I_{corr,j}
\]

and the ordered source-admissible separation of the five terminal controls, the routed second stage has the exact local input-output property

\[
\boxed{
(P,D)_{in}
\longmapsto
E_{out}=E_*\ne0
}
\tag{T5C15}
\]

with every positive-defect naturally-critical unwanted growing coordinate zero at exit.

Thus **no further PDE inverse, finite-lattice enumeration, or finite-dimensional rank theorem is missing for the second gate** once the handoff geometry is supplied.

## 9. Sole remaining second-gate barrier

The remaining theorem is geometric/source-support:

\[
\boxed{
\textbf{construct the support handoff from the P-D collision into five terminal homogeneous cancellation microcollars without reintroducing an order-one parent overlap.}
}
\tag{T5C16}
\]

This must show simultaneously that

1. the generated critical traces survive into their matching correction collars;
2. `P,D` have left before the terminal controls become active;
3. the five correction controls can be ordered/separated without losing their required exit traces;
4. all transition/cutoff errors are source-small or exponentially flat.

Once (T5C16) is proved, the second active gate is closed at the same working level as the first gate.
