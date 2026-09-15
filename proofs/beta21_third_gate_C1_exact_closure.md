# Exact `C^1` closure of the third beta-(2,1) active gate

**Status:** PROVED EXACT LOCAL ZERO-RESIDUAL THIRTEEN-CONTROL THIRD-GATE THEOREM FOR A GENERIC ADMISSIBLE SECOND-GATE TARGET `E_*`, CONDITIONAL ON THE SAME COMPUTER-ASSISTED FINITE ENVELOPE/RATE CERTIFICATES USED BY THE FIRST TWO ACTIVE GATES. The third gate starts immediately at the exact second-gate exit section. Choose the prescribed second-gate amplitude `E_*` outside the at-most-one-point frozen PBH exceptional set from `beta21_third_gate_immediate_PBH_rank.md`.

Then thirteen smooth same-character `C` controls give a full-rank exact phase-adapted zero-residual output map on

\[
(P,E,Q,M,X_2,\ldots,X_{10}),
\]

and one may impose exactly

\[
\boxed{
P_{out}=0,
\qquad
E_{out}=0,
\qquad
Q_{out}=Q_*\ne0,
\qquad
M_{out}=X_{2,out}=\cdots=X_{10,out}=0.
}
\]

Thus the third active gate is closed at the same working-research level as the first two. Publication hardening still requires outward-rounded interval arithmetic and source-line auditing of the finite control-profile estimates.

No complete reset cell or unforced Navier--Stokes blowup theorem is claimed.

## 1. Entrance data inherited exactly from gate two

Let the third gate begin at the exact second-gate exit section `s=s_3^-`. By the second-gate theorem,

\[
\boxed{
P(s_3^-)=0,
\quad
E(s_3^-)=E_*,
\quad
M(s_3^-)=X_2(s_3^-)=\cdots=X_{10}(s_3^-)=0,
}
\tag{TG1}
\]

with retained physical parents `C,D`.

Choose

\[
\boxed{E_*\ne0}
\tag{TG2}
\]

outside the at-most-one-point exceptional set of the frozen thirteen-state PBH scalar. Such a choice is available because gate two allows the nonzero output amplitude `E_*` to be prescribed in a fixed admissible neighborhood.

## 2. Thirteen internal controls

Let

\[
p=(p_1,\ldots,p_{13})\in\mathbb C^{13}
\]

parameterize thirteen fixed smooth same-character perturbations of the retained catalyst:

\[
\boxed{
C(p)=C_{base}+\sum_{j=1}^{13}p_jC_j.
}
\tag{TG3}
\]

Each `C_j` has the original `C` character and principal growing polarization, with a fixed smooth source-admissible coefficient profile centered at a distinct point of the third control collar.

As in the first two active gates:

1. the family is finite and introduces no new lattice generator;
2. source packet seminorms are uniform on a fixed parameter neighborhood;
3. same-character principal self-interactions vanish by incompressibility;
4. curl reconstruction produces exact divergence-free physical control packets with lower-source-class remainders;
5. parameter differentiation changes bounded amplitudes/profiles rather than the high carrier phase.

## 3. Designated finite block and action normalization

Use the thirteen-coordinate output vector

\[
\boxed{
\mathcal G_{3,\ell}(p)
=(P,E,Q,M,X_2,\ldots,X_{10})_{out}
\in\mathbb C^{13}.
}
\tag{TG4}
\]

The clean target is

\[
\boxed{
Y_{3,*}=(0,0,Q_*,0,\ldots,0),
\qquad Q_*\ne0.
}
\tag{TG5}
\]

Assign to every coordinate its leading minimal-leaf action at the immediate third section. In particular,

\[
A_P=A_C+A_D,
\qquad
A_E=A_C+2A_D,
\]

\[
A_M=A_C+A_D,
\]

and the promoted target `Q=2D` has

\[
\boxed{A_Q^{prom}=2A_C+2A_D.}
\tag{TG6}
\]

The exact-envelope audit gives

\[
A_Q^{prom}-\mathcal E_{2,4}(z_D)
=0.0644788533\ldots>0,
\]

so `Q` must be normalized on the promoted source-matched scale, not on its smaller natural homogeneous envelope.

Let `N_{3,ell}` be the corresponding diagonal action normalization and define

\[
\widehat{\mathcal G}_{3,\ell}
=N_{3,\ell}\mathcal G_{3,\ell}.
\tag{TG7}
\]

## 4. Frozen full-symbol rank

`beta21_third_gate_immediate_PBH_rank.md` proves that, for the generic choice (TG2), the frozen leading-action thirteen-state pair is controllable. Therefore thirteen distinct smooth control centers may be chosen on a fixed positive-width third collar so that the frozen smooth-profile response matrix satisfies

\[
\boxed{
\det J_{13,0}\ne0.
}
\tag{TG8}
\]

The conservative collar width may be taken as

\[
\boxed{w_3=10^{-4}.}
\tag{TG9}
\]

On this collar the six positive-defect unwanted root modes remain exactly those already included in the designated block, while every uncontrolled naturally-critical mode retains a fixed negative action gap.

The terminal `Q` state has nonzero feed-forward couplings from `E` and `X_2`; all feedback from `Q` to the upstream block loses an additional `C` leaf and is exponentially action-subleading in the leading upstream normalization.

## 5. Parameter derivatives preserve source gains

Differentiating the finite approximate designated field with respect to `p_j` replaces one source-admissible coefficient by another of the same fixed class. Consequently, after action normalization,

\[
\boxed{
\|D_pf_p\|_{norm}
\le
CS_*^A
\left(
\varepsilon^{\delta_*}+e^{-cS_*}
\right),
\qquad \delta_*>0,
}
\tag{TG10}
\]

uniformly on a fixed compact parameter neighborhood.

The direct `E_*-C_j -> Q` derivative is **not** placed in the residual `f_p`; it belongs to the designated thirteen-state block and is precisely the source of the generic terminal PBH transversality. Thus no leading derivative is incorrectly discarded as a small error.

Curl, frame, phase, slow-cutoff and reconstruction derivatives retain the positive source gains already audited in the first two parameter-dependent gate theorems.

## 6. Exact nonzero/stable correction

Extract the complete thirteen-coordinate designated block from the infinite harmonic correction space. The beta-zero root `M` uses its full stable `T=0` propagator. Every retained positive-beta coordinate uses its full finite-symbol propagator. The remaining infinite lattice is the stable complement with stage-uniform inverse and quadratic high-mode smoothing.

For fixed residual mean input the correction equation has the schematic form

\[
\partial_vz
=\mathcal L_{p,m}z+f_{p,m}+\mathcal B(z,z).
\tag{TG11}
\]

After all leading thirteen-state interactions are absorbed into `L_{p,m}`, the forward Duhamel map is a contraction on a ball

\[
\rho_\ell
\le
CS_*^A
\left(
\varepsilon^{\delta_*}+e^{-cS_*}
\right)
\to0.
\tag{TG12}
\]

The parameter-dependent contraction theorem therefore gives a unique `C^1` stable correction

\[
z=z(p,m)
\]

with

\[
\boxed{
\|D_pz(p,m)\|_{norm}=o(1).
}
\tag{TG13}
\]

## 7. Exact residual mean solve

The promoted beta-zero root coordinate is already extracted into the finite designated block. The residual angular mean is solved by the same global fixed-order Leray--Oseen contraction as in gate two.

Its nonlinear Lipschitz constant obeys

\[
q_\ell
\le
CS_*^A
\left[
\varepsilon^{9/50-2\kappa_s}
+\varepsilon^{1/2-\kappa_s}
+\varepsilon^{1-2\kappa_s}
+\rho_\ell
\right]
\to0.
\tag{TG14}
\]

Hence the exact residual mean fixed point is `C^1` in all thirteen controls and

\[
\boxed{
\|D_pm_{corr}(p)\|_{norm}=o(1).
}
\tag{TG15}
\]

## 8. Exact physical zero residual

For every parameter vector in a sufficiently small fixed neighborhood, combine the designated third-gate field, the full thirteen-state finite response, the exact stable nonzero correction and the residual mean correction. Exact phase-adapted reconstruction gives

\[
\boxed{
\mathcal N_{phys}
\bigl(\mathcal R_\ell U_{3,\ell}(p)\bigr)=0
}
\tag{TG16}
\]

on the fixed third control collar.

Thus the controls parameterize a genuine local family of exact unforced solutions rather than a forced approximate gate.

## 9. Exact exit Jacobian

Split the normalized output into designated and correction traces. The frozen full-symbol/smooth-profile theorem and source normalization give

\[
D_p\widehat{\mathcal G}_{3,des,\ell}
=J_{13,0}
+O(S_*^{-1})
+O(S_*^A\varepsilon^{\delta_*})
+O(e^{-cS_*}).
\tag{TG17}
\]

Equations (TG13)--(TG15) imply

\[
\|D_p\widehat{\mathcal G}_{3,corr,\ell}\|=o(1).
\]

Therefore

\[
\boxed{
D_p\widehat{\mathcal G}_{3,\ell}
=J_{13,0}+o(1).
}
\tag{TG18}
\]

Let

\[
d_{13}=|\det J_{13,0}|>0.
\]

For all sufficiently high levels,

\[
\boxed{
|\det D_p\widehat{\mathcal G}_{3,\ell}|
\ge\frac12d_{13}>0.
}
\tag{TG19}
\]

## 10. Exact third-gate target

The quantitative inverse/implicit-function theorem gives a nearby exact control vector `p_ell` such that

\[
\boxed{
P_{out}=0,
\qquad
E_{out}=0,
\qquad
Q_{out}=Q_*\ne0,
}
\tag{TG20}
\]

and simultaneously

\[
\boxed{
M_{out}=X_{2,out}=\cdots=X_{10,out}=0.
}
\tag{TG21}
\]

All uncontrolled naturally-critical modes remain below the fixed negative action margin from the third-gate audit, and the infinite complement remains uniformly forward stable.

## 11. Third active gate closure

The first three local active gates may therefore be concatenated without a free transport interval between gates two and three:

\[
(C,D,P_{tr})
\stackrel{G_2}{\longmapsto}
(C,D,E_*)
\stackrel{G_3}{\longmapsto}
(C,D,Q_*),
\tag{TG22}
\]

where `E_*` is chosen generically as above.

The next nominal edge is

\[
\boxed{Q-C\to H=2D-C.}
\tag{TG23}
\]

The fourth gate should likewise begin immediately at the third-gate exit section. Because `H` is itself the first member `X_2` of the mean-root family, the fourth-gate finite block is not expected to be a simple copy of gate three: the desired output lies inside the previously cancelled root chain. A fresh action/rank audit is therefore mandatory before claiming a fourth gate.
