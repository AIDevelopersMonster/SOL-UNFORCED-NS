# Exact three-control `C^1` closure of the corrected post-strong-`H` terminal gate

**Status:** PROVED EXACT LOCAL ZERO-RESIDUAL THREE-CONTROL TERMINAL GATE THEOREM AT THE CORRECTED NON-TURNING WORKING POINT, SUBJECT TO THE BRANCH-WIDE NUMERICAL-CERTIFICATION CAVEAT. After `beta21_corrected_strong_H_nine_control_C1_closure.md`, the spent old catalyst has already been set exactly to zero. The only leading designated bank entering the remaining short interval is therefore

\[
(P_{new},D),
\]

with beta weights `(2,1)`. On `t_*<t<T`, the only new source-promoted characters above the renewed beta-two target are

\[
H=P_{new}-D,
\qquad
M=P_{new}-2D=H-D.
\]

Hence the complete terminal leading block is only

\[
(P_{new},H,M).
\]

Three translated same-character `P_new` subpackets give a direct root control in `P_new`; the nonzero difference edge `P_new-D -> H` and the nonzero beta-zero edge `H-D -> M` form a two-step chain. The frozen controllability determinant is therefore nonzero. The exact phase-adapted parameter-dependent zero-residual solve is `C^1`, and the full exit Jacobian differs from this three-state principal matrix by `o(1)`. Consequently one may prescribe

\[
\boxed{
(P_{new},H,M)_{out}=(P_*,0,0),
\qquad P_*\ne0,
}
\]

while retaining the nonzero `D` channel.

Together with the nine-control strong-`H` theorem, this removes the previous large terminal `C`-forest obstruction. The remaining local obligation is the corrected entrance `P-C -> D` gate and finite-collar concatenation.

## 1. Post-strong-`H` incoming bank

At the corrected point

\[
u=2.5,
\qquad
\delta=0.1375,
\qquad
x=0.7779445026067248271\ldots,
\]

the exact strong-`H` gate ends at

\[
t_*=0.2251291169828679798\ldots
\]

with

\[
C=0,
\qquad
P_{new}\ne0,
\qquad
D\ne0,
\]

and every other source-promoted coordinate above the target action equal to zero.

The clock-reset face is

\[
T=2\delta=0.275,
\qquad
T-t_*=0.0498708830\ldots>0.
\tag{T3-1}
\]

The surviving designated slopes are

\[
z_D(t)=x-\delta+t,
\qquad
z_P(t)=x-2\delta+t.
\tag{T3-2}
\]

At `T`,

\[
z_D(T)=x+\delta,
\qquad
z_P(T)=x,
\tag{T3-3}
\]

which is exactly the input slope pair of the corrected beta-(2,1) section.

## 2. Exact propagated-action audit

Because both surviving channels leave the strong-`H` gate on their natural action levels, at any later generation time `s` their actions are

\[
A_D(s)=\mathcal E_{1,u}(z_D(s)),
\qquad
A_P(s)=\mathcal E_{2,u}(z_P(s)).
\tag{T3-4}
\]

For a descendant

\[
K=mD+nP_{new},
\qquad
\beta_K=m+2n,
\]

use the actual source action at its generation time and exact homogeneous propagation to `T` when `beta_K !=0`. For `beta_K=0`, ignoring the additional stable damping gives a conservative upper bound.

The companion audit `experiments/beta21_corrected_terminal_three_state_audit.py` gives:

### Difference child

\[
H=P_{new}-D
\]

has maximal boundary action

\[
A_H^{max}(T)
\approx-0.0638891341162304,
\]

so

\[
A_H^{max}(T)-A_{P_*}(T)
\approx+0.0824496679741289.
\tag{T3-5}
\]

Thus `H` must be controlled.

### Beta-zero root

\[
M=P_{new}-2D=H-D
\]

has conservative maximal action

\[
A_M^{max}
\approx-0.131924862616088,
\]

hence

\[
A_M^{max}-A_{P_*}(T)
\approx+0.014413939474272.
\tag{T3-6}
\]

Thus `M` must also be controlled even though its homogeneous beta-zero propagator is stable.

### Nearest omitted sum child

\[
S=P_{new}+D
\]

satisfies

\[
A_S^{max}(T)
\approx-0.154895415172560,
\]

and therefore

\[
\boxed{
A_S^{max}(T)-A_{P_*}(T)
\approx-0.00855661308220035<0.
}
\tag{T3-7}

### Regenerated old catalyst

The first algebraic route back to the old catalyst is

\[
C_{regen}=3D-P_{new}.
\]

Its maximal propagated action satisfies

\[
A_{C_{regen}}^{max}(T)-A_{P_*}(T)
\approx-0.02312<0.
\tag{T3-8}
\]

All higher mixed descendants require at least the leaves of one of these omitted branches or an extra cancelling pair and are still lower in action. Identical `D+D` and `P+P` principal self-interactions vanish for the same-phase incompressible packets.

Hence

\[
\boxed{
\text{the complete post-}t_*\text{ promoted block is }(P_{new},H,M).
}
\tag{T3-9}

## 3. Choose a positive terminal collar

Fix, for definiteness,

\[
t_{term}=t_*+0.005
=0.23012911698286798\ldots
\tag{T3-10}
\]

and the collar

\[
\boxed{|t-t_{term}|\le10^{-3}.}
\tag{T3-11}
\]

It lies strictly after the strong-`H` collar and strictly before the reset face, with more than `0.043` normalized time remaining after its right endpoint.

The action classification (T3-9) is stable under such a small displacement because the nearest omitted gap (T3-7) is fixed and the envelope functions are smooth on the compact source interval.

## 4. Nonzero principal chain

The first mandatory edge is

\[
P_{new}-D\to H.
\tag{T3-12}
\]

Using the positive-beta difference formula from `beta21_microcascade_polarization_audit.md`, at the terminal center

\[
\boxed{
\kappa_{P-D\to H}
\approx-1.25466\ne0.
}
\tag{T3-13}

On the whole collar (T3-11),

\[
\boxed{|\kappa_{P-D\to H}|>1.2545.}
\tag{T3-14}

The second edge is

\[
H-D\to M,
\tag{T3-15}
\]

where `M` has beta zero. The exact projected beta-zero source vector has norm approximately

\[
3.8266
\]

at the center and satisfies

\[
\boxed{\|b_{H-D\to M}\|>3.82}
\tag{T3-16}
\]

throughout (T3-11).

Thus neither edge is near a polarization zero.

## 5. Frozen three-state control system

Order the state as

\[
X=(P_{new},H,M).
\]

Split the outgoing parent into three localized same-character control subpackets,

\[
P_{new}(p)
=P_{base}+\sum_{j=1}^{3}p_jP_j,
\qquad p\in\mathbb C^3,
\tag{T3-17}
\]

with distinct translated centers inside the terminal collar.

At frozen principal level, after including the full-symbol diagonal and all leading in-block feedbacks, the linearized operator has the schematic form

\[
A_3=
\begin{pmatrix}
\lambda_P & c & 0\\
a&\lambda_H&d\\
0&b&\lambda_M
\end{pmatrix},
\qquad
B_3=e_P,
\tag{T3-18}
\]

where

\[
a=\kappa_{P-D\to H}\,D\ne0,
\qquad
b=\kappa_{H-D\to M}\,D\ne0.
\]

The optional coefficients `c,d` represent leading in-block return interactions such as `H+D -> P` and `M+D -> H`; they need not vanish.

The controllability matrix begins

\[
B_3=e_P,
\]

\[
A_3B_3
=(\lambda_P,a,0)^T,
\]

and the `M` component of `A_3^2B_3` is exactly

\[
ab.
\]

Therefore

\[
\boxed{
\det[B_3,A_3B_3,A_3^2B_3]
=a^2b\ne0.
}
\tag{T3-19}

This identity is independent of the diagonal rates and of the in-block feedback coefficients `c,d`.

Thus the complete frozen three-state leading system is controllable.

## 6. Smooth translated controls

For a controllable constant finite pair `(A_3,B_3)`, translated compact profiles generate response columns

\[
K(\tau)
=
\int e^{A_3(v_+-s)}B_3q(s-\tau)\,ds.
\]

There exist three distinct centers inside the fixed terminal collar for which the `3 x 3` response matrix is invertible. Choose such centers and write

\[
J_{3,0},
\qquad
\boxed{d_3:=|\det J_{3,0}|>0.}
\tag{T3-20}

Because the two edge margins (T3-14), (T3-16) are fixed positive and all source coefficients vary smoothly, a sufficiently short positive collar gives

\[
\boxed{
|\det J_{3,var}|\ge\frac34d_3>0.
}
\tag{T3-21}

## 7. Internal source realization

Every `P_j` in (T3-17) carries exactly the same beta-two character and principal polarization as the already generated `P_new` packet. Hence

- the control bank introduces no new lattice generator;
- same-phase `P_i,P_j` principal self-interactions vanish by incompressibility;
- each control admits the same source-native coefficient localization and curl realization used for earlier finite control banks;
- finite profile derivatives change only fixed design constants;
- no external forcing is introduced.

The direct root coordinate is now the parent `P_new` itself, so the controls enter the first state directly.

## 8. Exact `C^1` zero-residual transfer

Let `K_p` be a fixed compact neighborhood of the frozen principal three-control vector. The designated field remains a finite sum of the branch source packet classes.

As in `six_control_C1_exact_first_gate_closure.md` and `beta21_corrected_strong_H_nine_control_C1_closure.md`, parameter differentiation does not change the source exponents:

\[
\|f_p\|+\|D_pf_p\|
\le
CS_*^A(\varepsilon^{1/5}+e^{-cS_*}),
\tag{T3-22}
\]

\[
\|F_{mean,p}\|+\|D_pF_{mean,p}\|
\le
CS_*^A\varepsilon^{1-\kappa_s}.
\tag{T3-23}
\]

The nonzero and mean correction maps are uniform contractions for high levels. Their fixed points are `C^1` in the three parameters and obey

\[
\boxed{
\|D_pz\|+\|D_pm\|=o(1).
}
\tag{T3-24}
\]

Define the exact terminal exit map

\[
\mathcal G^{term}_{\ell}(p)
=(P_{new},H,M)_{out}.
\tag{T3-25}

The fixed negative gap to every omitted source genealogy and the exact correction estimate give

\[
\boxed{
D_p\mathcal G^{term}_{\ell}
=J_{3,var}+o(1).
}
\tag{T3-26}

Hence for all sufficiently high dyadic levels,

\[
\boxed{
|\det D_p\mathcal G^{term}_{\ell}|
\ge\frac12d_3>0.
}
\tag{T3-27}

## 9. Exact terminal target

At frozen principal level choose the unique nearby control vector sending

\[
(P_{new},H,M)_{out}
\]

to

\[
(P_*,0,0),
\qquad P_*\ne0.
\]

By the quantitative inverse-function theorem, the exact map has a control vector

\[
\boxed{p_\ell=p^0+o(1)}
\tag{T3-28}

with

\[
\boxed{
\mathcal G^{term}_{\ell}(p_\ell)
=(P_*,0,0).
}
\tag{T3-29}

The designated `D` channel remains uniformly nonzero by the same compact-neighborhood argument used in the strong-`H` theorem.

After this collar, every source-promoted coordinate other than `(P_new,D)` is zero or separated below the renewed-parent action by a fixed gap.

Free homogeneous propagation to `T` then gives the exact slope handoff

\[
\boxed{
(P_{new},D)_T
\text{ has reduced slopes }
(x,x+\delta).
}
\tag{T3-30}

## 10. Consequence

The previously feared terminal problem has collapsed from a large old-`C` promoted forest to a rigorously controlled three-state local gate:

\[
\boxed{
(P_{new},D)
\longmapsto
(P_{new},D),
\qquad
H=M=0.
}
\tag{T3-31}

Thus the corrected non-turning architecture now has exact local closure from the strong-`H` generation through the reset face.

The remaining local barrier is upstream: verify and, if necessary, actively close the corrected entrance difference event

\[
P-C\to D
\]

at the same `u=2.5, delta=0.1375` working point, then concatenate the finite collars and audit their mutual support/action separation.

No global infinite cascade or unforced Navier--Stokes blowup theorem is claimed. Publication-final use still requires outward-rounded certification of the numerical action and polarization margins.
