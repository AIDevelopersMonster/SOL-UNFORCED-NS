# Exact `C^1` closure of the unrouted second beta-(2,1) active gate

**Status:** PROVED EXACT LOCAL ZERO-RESIDUAL TWELVE-CONTROL GATE THEOREM, CONDITIONAL ONLY ON THE RECORDED COMPUTER-ASSISTED FINITE ENVELOPE/RATE CERTIFICATES. The old catalyst `C` need not be removed from the second overlap. Twelve smooth same-character `C` control profiles produce a full-rank leading response on the fresh `P/E` branch together with the complete ten-state beta-zero mean-root family. In action-normalized coordinates the exact phase-adapted zero-residual output Jacobian is the frozen full-symbol controllable matrix plus `o(1)`. Hence, for every sufficiently high dyadic level, one can impose exactly

\[
\boxed{
P_{out}=0,
\qquad
E_{out}=E_*\ne0,
\qquad
M_{out}=X_{2,out}=\cdots=X_{10,out}=0.
}
\]

All other naturally critical second-collar characters remain uniformly action-subcritical on the certified positive-width collar.

This closes the second active gate at the same working-research level as the first, without a routed-support hypothesis. Publication hardening still requires interval arithmetic for the finite envelope/rate certificates and a source-line audit of the finite control profiles.

No full reset-cell or unforced Navier--Stokes blowup theorem is claimed.

## 1. Twelve internal controls

Work on the unrouted second overlap with old `C,D` physically present. Let

\[
p=(p_1,\ldots,p_{12})\in\mathbb C^{12}
\tag{UC1}
\]

parameterize twelve fixed smooth same-character catalyst perturbations

\[
\boxed{
C(p)
=C_{base}+\sum_{j=1}^{12}p_j C_j.
}
\tag{UC2}

Each `C_j` has the original `C` phase and principal growing polarization, with a fixed smooth source-admissible coefficient profile centered at a distinct point of the second control collar.

Because the family is finite:

1. no new lattice generator is introduced;
2. every source packet seminorm is uniform on a fixed compact parameter neighborhood;
3. same-phase `C_i,C_j` principal self-interactions vanish by incompressibility;
4. curl reconstruction gives exact divergence-free physical control packets with lower-source-class remainders.

The controls are internal approximate-field/design parameters, not external forcing.

## 2. Complete designated finite block

Use the fresh sum branch

\[
P=C+D,
\qquad
E=P+D=C+2D,
\tag{UC3}
\]

and the beta-zero root

\[
M=D-C.
\tag{UC4}
\]

Let the sufficient ten-state root chain be

\[
X_1=M,
\quad X_2=2D-C,
\quad X_3=3D-2C,
\quad X_4=4D-3C,
\]

\[
X_5=5D-4C,
\quad X_6=6D-4C,
\quad X_7=7D-5C,
\]

\[
X_8=8D-6C,
\quad X_9=9D-6C,
\quad X_{10}=10D-7C.
\tag{UC5}
\]

The exact finite output map is

\[
\boxed{
\mathcal G_{2,\ell}(p)
=(P,E,X_1,X_2,\ldots,X_{10})_{out}
\in\mathbb C^{12}.
}
\tag{UC6}

The target is

\[
\boxed{
Y_*=(0,E_*,0,\ldots,0),
\qquad E_*\ne0.
}
\tag{UC7}

The intermediate root coordinates are cancelled for triangular cleanliness; this is sufficient rather than minimal.

## 3. Action normalization

Assign to every finite coordinate its leading minimal-leaf action at the second section. In particular

\[
A_P^{fresh}=A_C+A_D,
\qquad
A_E^{fresh}=A_C+2A_D,
\tag{UC8}
\]

and

\[
A_M=A_C+A_D.
\tag{UC9}
\]

The root-chain actions are obtained additively along the genealogy in `beta21_second_gate_unrouted_full_critical_audit.md`.

Let `N_ell` be the diagonal normalization by the corresponding source packet/action scales and define

\[
\widehat{\mathcal G}_{2,\ell}
=N_\ell\mathcal G_{2,\ell}.
\tag{UC10}
\]

The weaker transported `P` from the first gate lies below the fresh second-collar `P` by the fixed action amount

\[
A_P^{fresh}-A_P^{tr}
=0.0150824235\ldots>0.
\tag{UC11}
\]

Thus the transported contribution is `o(1)` in the fresh-`P` normalized coordinate, but it remains part of the **exact** output in (UC6). Solving `P_out=0` therefore cancels it as well; no post hoc truncation is used.

## 4. Parameter derivatives preserve the source hierarchy

At coefficient level

\[
D_{p_j}C=C_j.
\tag{UC12}
\]

The profiles are fixed smooth source-admissible coefficients. Differentiating any finite designated product replaces one bounded coefficient by another bounded coefficient and leaves its action factor unchanged.

Therefore, after action normalization, every differentiated stage-zero residual satisfies

\[
\boxed{
\|D_pf_p\|_{norm}
\le
CS_*^A
\left(
\varepsilon^{\delta_*}+e^{-cS_*}
\right),
\qquad \delta_*>0.
}
\tag{UC13}
\]

uniformly on a fixed compact parameter set.

The curl, frame, phase, slow-cutoff and reconstruction terms retain their previously audited positive source gains because `p` differentiates amplitude coefficients and not the high carrier phase.

## 5. Finite full-symbol block plus stable complement

Extract all twelve coordinates (UC6) from the infinite harmonic correction space and include their `O(1)` minimal-action linearized couplings in the designated finite operator.

The beta-zero root `M` uses its full strictly stable `T=0` propagator. The positive-beta finite coordinates use their full growing/decaying finite-symbol propagators. The remaining infinite lattice is the stable complement from `finite_critical_block_uniform_stable_inverse.md` and retains its stage-uniform inverse and quadratic high-mode smoothing.

The twelve-state leading frozen pair is controllable by `beta21_second_gate_unrouted_twelve_state_PBH_rank.md`. Let its smooth-profile response matrix be

\[
J_{12,0},
\qquad
\det J_{12,0}\ne0.
\tag{UC14}
\]

The positive collar width is fixed as

\[
\boxed{
w_2
=\min(5\times10^{-4},w_{rank,12})>0.
}
\tag{UC15}

On this collar the full designated propagator and its parameter derivative are uniformly bounded in the action-normalized graph norm.

## 6. `C^1` exact nonzero/stable solve

For fixed residual angular mean input, write the correction equation schematically as

\[
\partial_v z
=\mathcal L_{p,m}z
+f_{p,m}
+\mathcal B(z,z),
\tag{UC16}
\]

where all leading finite second-gate interactions have already been absorbed into the designated block and `L_{p,m}` contains the bounded mixed linearization.

The exact forward Duhamel map is a contraction on a ball of radius

\[
\rho_\ell
\le
CS_*^A
\left(
\varepsilon^{\delta_*}+e^{-cS_*}
\right)
\to0.
\tag{UC17}
\]

Choose the level so that the derivative in `z` has norm at most `1/2`. The parameter-dependent contraction theorem gives a unique `C^1` solution

\[
z=z(p,m)
\]

and

\[
\boxed{
\|D_pz(p,m)\|_{norm}=o(1).
}
\tag{UC18}

The estimate is relative to the promoted action scales, not merely an unweighted physical norm.

## 7. `C^1` residual mean solve

The promoted beta-zero root has been extracted into the designated finite block. The remaining angular mean correction is evolved by the global fixed-order Leray--Oseen propagator.

The nonlinear mean map has dyadically small Lipschitz constant

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
\tag{UC19}
\]

Hence the exact mean fixed point depends `C^1` on all twelve parameters and

\[
\boxed{
\|D_pm_{corr}(p)\|_{norm}=o(1).
}
\tag{UC20}

The finite promoted `M` response is not counted in `m_corr`; it is part of the designated PBH block.

## 8. Exact physical zero residual

For every parameter vector in the fixed neighborhood, combine the designated second-gate field, the finite PBH response, the exact stable nonzero correction and the residual angular mean correction. Exact reconstruction gives

\[
\boxed{
\mathcal N_{phys}
\bigl(\mathcal R_\ell U_\ell(p)\bigr)=0
}
\tag{UC21}

on the fixed positive-width second gate.

Thus the finite controls parameterize a genuine local family of exact unforced solutions.

## 9. Exact exit Jacobian

Split the normalized output map into designated and correction traces:

\[
\widehat{\mathcal G}_{2,\ell}
=\widehat{\mathcal G}_{des,\ell}
+\widehat{\mathcal G}_{corr,\ell}.
\tag{UC22}
\]

The frozen full-symbol/smooth-profile theorem and source normalization give

\[
D_p\widehat{\mathcal G}_{des,\ell}
=J_{12,0}
+O(S_*^{-1})
+O(S_*^A\varepsilon^{\delta_*})
+O(e^{-cS_*}).
\tag{UC23}
\]

Equations (UC18)--(UC20) imply

\[
\boxed{
\|D_p\widehat{\mathcal G}_{corr,\ell}\|=o(1).
}
\tag{UC24}

Therefore

\[
\boxed{
D_p\widehat{\mathcal G}_{2,\ell}
=J_{12,0}+o(1)
}
\tag{UC25}
\]

uniformly on a sufficiently small fixed parameter neighborhood.

## 10. Persistence of rank and exact gate target

Let

\[
d_{12}=|\det J_{12,0}|>0.
\]

For sufficiently large dyadic level,

\[
\boxed{
|\det D_p\widehat{\mathcal G}_{2,\ell}|
\ge\frac12d_{12}>0.
}
\tag{UC26}
\]

Let `p^0` be the frozen finite solution for the normalized target. The quantitative inverse/implicit-function theorem gives

\[
\boxed{
p_\ell=p^0+o(1)}
\tag{UC27}
\]

such that in exact physical coordinates

\[
\boxed{
P_{out}=0,
\qquad
E_{out}=E_*\ne0,
\qquad
M_{out}=X_{2,out}=\cdots=X_{10,out}=0.
}
\tag{UC28}

No leading or subleading transported `P` is retained because the exact total coordinate is prescribed to zero.

## 11. All uncontrolled critical modes are subcritical

The complete unrouted audit contains 50 positive-beta naturally critical center characters. The six positive-defect unwanted characters are all contained in the controlled root block. Every other unwanted critical character has negative center defect; the closest one is about

\[
-0.0170697093.
\]

The width certificate proves that on

\[
0\le t\le5\times10^{-4}
\]

the weakest uncontrolled margin remains below approximately

\[
-0.0160,
\]

and no omitted lattice site enters the critical window.

The twelve controls use only the existing `C` character and do not enlarge the lattice or increase the maximal leaf-action bound. Hence every uncontrolled finite mode remains action-subcritical, while the infinite complement remains uniformly forward-stable.

## 12. Second-gate closure

The unrouted second active gate is therefore closed at working-research level:

\[
\boxed{
(C,D,P_{tr})_{in}
\longmapsto
(C,D,E_*)_{out},
}
\tag{UC29}
\]

where the old `C,D` parents are deliberately retained for later reset events, the obsolete beta-two `P` is cancelled exactly, the desired beta-three `E` is nonzero/prescribed, the entire dangerous beta-zero root family is cancelled, and every other critical output lies below a fixed action gap.

The next event may now be attacked directly:

\[
\boxed{E-C\to Q.}
\tag{UC30}
\]

Before concatenation through the full reset cell, the third collar must receive its own complete critical/action audit; the second-gate control block cannot simply be copied because the input betas and promoted actions have changed.

Publication hardening still requires interval arithmetic for the finite width/rate classifications and an explicit source-line audit of the twelve control-profile derivative estimates.
