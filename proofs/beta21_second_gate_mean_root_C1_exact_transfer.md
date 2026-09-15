# Action-normalized `C^1` exact transfer for the routed second active gate

**Status:** PROVED PARAMETER-DEPENDENT EXACT LOCAL GATE THEOREM CONDITIONAL ON THE ROUTED SUPPORT HYPOTHESIS `C_old notin I_2`. The finite-dimensional control architecture consists of one main second-collision amplitude parameter and seven source-matched `C_new` root controls. In action-normalized coordinates the exact phase-adapted zero-residual output map has Jacobian equal to a fixed invertible block-triangular designated matrix plus `o(1)`. Hence the desired `E` output and the complete seven-state mean-root sideband chain can be prescribed exactly at sufficiently high dyadic level.

This theorem closes the **PDE/rank/action-scale** part of the routed second gate. It does not yet construct the global support handoff that removes the old catalyst from the second overlap and later supplies catalyst copies to the third/fourth events.

## 1. Finite parameter vector

Let

\[
\theta=(\alpha,p_1,\ldots,p_7)
\in\mathbb C^8.
\tag{C2G1}
\]

The parameter `alpha` varies one normalized incoming/main `P-D` collision amplitude and is used to prescribe the desired beta-three output `E`.

The parameters `p_j` multiply the seven source-matched `C_new` homogeneous subpackets constructed in `beta21_second_gate_mean_root_source_realization.md`:

\[
C_{ctrl}
=\eta_\ell\sum_{j=1}^7p_j\widehat C_j,
\qquad
\eta_\ell=e^{-\delta_C\Lambda_\ell},
\quad
\delta_C=0.0632396845\ldots.
\tag{C2G2}
\]

Choose a fixed compact parameter neighborhood `K_theta` around one frozen principal solution. All normalized packet seminorms are uniform on this compact set; the physical root-control coefficients are smaller by `eta_ell<=1`.

## 2. Designated finite block

Treat the complete root family as part of the designated finite block rather than hiding the beta-zero root inside the stable correction:

\[
X_{root}
=(M,H_1,H_2,H_3,J_4,K_4,H_4).
\tag{C2G3}
\]

The desired finite output vector is

\[
\boxed{
Y_\ell(\theta)
=(E,M,H_1,H_2,H_3,J_4,K_4,H_4)_{out}.
}
\tag{C2G4}
\]

The target is

\[
\boxed{
Y_*
=(E_*,0,0,0,0,0,0,0),
\qquad E_*\ne0.
}
\tag{C2G5}
\]

Cancelling the two intermediate root coordinates `J_4,K_4` is sufficient rather than minimal; it makes the finite map triangular.

## 3. Action normalization

Assign to each designated root-family coordinate its minimal genealogical promoted action from `beta21_second_gate_mean_root_factorization.md`. In particular

\[
A_M=A_P+2A_D,
\tag{C2G6}
\]

\[
A_{H_1}=A_P+3A_D,
\qquad
A_{H_2}=2A_P+5A_D,
\qquad
A_{H_3}=3A_P+7A_D,
\tag{C2G7}
\]

with analogous additive actions for `J_4,K_4,H_4` along the displayed root genealogy.

Let `N_ell` denote the diagonal action normalization that divides each physical exit coefficient by its corresponding source packet scale

\[
\varepsilon^{\alpha_j}S_*^{c_j}e^{A_j\Lambda_\ell}
\]

and divides `E` by its designated second-collision scale.

Define

\[
\boxed{
\widehat Y_\ell=N_\ell Y_\ell.
}
\tag{C2G8}
\]

In these coordinates the seven root controls have `O(1)` response. Without this normalization their physical Jacobian entries are exponentially small, which is a harmless scale effect rather than a loss of rank.

## 4. Parameter differentiation preserves every promoted action factor

Every `p_j` derivative replaces one control coefficient by

\[
\eta_\ell\widehat C_j.
\]

Products with `D` therefore carry exactly the root action `A_M`; subsequent differentiated products along the finite root genealogy carry the corresponding additive promoted action. Source localization, phase/frame errors, curl reconstruction and finite packet derivatives introduce only polynomial `S_*` losses and positive epsilon powers. They do not introduce inverse action factors.

Consequently, after applying `N_ell`, the differentiated stage-zero residual satisfies a uniform estimate of the form

\[
\boxed{
\|D_\theta f_\theta\|_{norm}
\le
CS_*^A
\left(
\varepsilon^{\delta_*}+e^{-cS_*}
\right),
\qquad \delta_*>0.
}
\tag{C2G9}
\]

Here the norm uses the designated promoted action weight on the finite root block and the previously established analytic/stable weights on the complement.

This is the action-normalized analogue of the source-derivative estimate in the six-control first-gate theorem.

## 5. Full nonzero/stable propagator with the root block extracted

Extract the finite root family from the stable complement and include all of its `O(1)` frozen couplings in the designated finite linear operator. The remaining infinite lattice is unchanged and retains the uniform stable inverse with quadratic high-mode smoothing.

For the beta-zero root itself use the full-symbol stable propagator from `beta21_second_gate_beta_zero_fullsymbol_rank_bridge.md`. For the positive-beta root descendants use their full designated linearized propagators. The combined finite/infinite linear propagator therefore obeys a uniform bound

\[
\boxed{
\|V_{\theta,m}(v,w)\|
+\|D_\theta V_{\theta,m}(v,w)\|
\le C_{K_\theta,I_2}
}
\tag{C2G10}
\]

in the action-normalized graph norm.

All parameter derivatives of the finite coefficients are bounded because the normalized control vector lies in a fixed compact set.

## 6. `C^1` nonzero fixed point

The exact nonzero/stable correction map is a contraction on the same source-small ball as in the local zero-residual theorem, with the finite root block now absorbed into the designated linearization. Its radius obeys

\[
\rho_\ell
\le
CS_*^A
\left(
\varepsilon^{\delta_*}+e^{-cS_*}
\right)
\to0.
\tag{C2G11}
\]

Choose the level so that the derivative in the correction unknown has norm at most `1/2`. The parameter-dependent contraction theorem gives a unique `C^1` correction `z=z(theta,m)` and

\[
\boxed{
\|D_\theta z\|_{norm}
=o(1).
}
\tag{C2G12}
\]

The `o(1)` is measured **after action normalization**, so it is small relative to each promoted root-family coordinate rather than merely small in an unweighted physical norm.

## 7. `C^1` mean solve

The exact angular-mean equation is evolved by the whole-space Leray--Oseen propagator. Its fixed-order forward bound is dyadically uniform, and the nonlinear source has Lipschitz constant

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
\tag{C2G13}
\]

The beta-zero root has already been extracted into the designated finite block, so its leading source response is not counted as a small mean correction. The remaining mean fixed point therefore satisfies the same parameter-dependent contraction estimate as before:

\[
\boxed{
\|D_\theta m_{corr}(\theta)\|_{norm}=o(1).
}
\tag{C2G14}
\]

This avoids the false inference that the promoted beta-zero root itself must be of the small generic mean-correction size.

## 8. Exact local zero residual

For every `theta in K_theta`, combine the designated field, the exact root-family finite response, the nonzero stable correction and the residual angular mean correction. Exact reconstruction gives

\[
\boxed{
\mathcal N_{phys}
\bigl(\mathcal R_\ell U_\ell(\theta)\bigr)=0
}
\tag{C2G15}
\]

on the routed second collision collar.

No external forcing is present. The eight parameters are internal incoming/subpacket design data.

## 9. Exact action-normalized output Jacobian

Let

\[
\widehat{\mathcal G}_{2,\ell}(\theta)
=N_\ell Y_\ell(\theta).
\tag{C2G16}
\]

At frozen full-symbol level the finite designated Jacobian has block form

\[
\boxed{
J_{2,0}
=
\begin{pmatrix}
\kappa_E & 0\\
* & J_{7,full}
\end{pmatrix},
}
\tag{C2G17}
\]

where

\[
\kappa_E\ne0
\]

is the principal `P+D -> E` response and

\[
\det J_{7,full}\ne0
\]

by the beta-zero full-symbol rank bridge.

The zero in the upper-right block is the leading action-normalized limit: every root-control contribution to `E` passes through the side `P` trace whose action is below the designated `P` by

\[
2|A_D|=0.0481572610\ldots.
\]

Hence that block is exponentially small.

Equations (C2G12)--(C2G14) and the source/frame audit give

\[
\boxed{
D_\theta\widehat{\mathcal G}_{2,\ell}
=J_{2,0}+o(1)
}
\tag{C2G18}
\]

uniformly on a sufficiently small fixed normalized parameter neighborhood.

## 10. Persistence of rank and exact target

Let

\[
d_2:=|\det J_{2,0}|>0.
\]

For sufficiently large dyadic level,

\[
\boxed{
|\det D_\theta\widehat{\mathcal G}_{2,\ell}|
\ge\frac12d_2>0.
}
\tag{C2G19}
\]

Let `theta^0` be the frozen finite solution of

\[
\widehat Y_0(\theta^0)=\widehat Y_*.
\]

The quantitative inverse/implicit-function theorem yields

\[
\boxed{
\theta_\ell=\theta^0+o(1)
}
\tag{C2G20}
\]

such that, in physical coordinates,

\[
\boxed{
(E,M,H_1,H_2,H_3,J_4,K_4,H_4)_{out}
=(E_*,0,0,0,0,0,0,0).
}
\tag{C2G21}

## 11. Remaining critical modes

The full second-gate critical audit is finite. Apart from the designated `E` and the four positive-defect dangerous characters contained in the root family, every naturally critical uncontrolled character has a strict negative center action defect; the closest recorded margin is approximately

\[
-0.0291470855.
\]

By continuity over this finite set there exists a positive action-safe collar width `w_action,2>0`. Intersect it with the positive full-symbol rank width from the root-control theorem:

\[
\boxed{
w_2:=\min(w_{action,2},w_{full})>0.}
\tag{C2G22}
\]

On this collar all uncontrolled critical modes remain action-subcritical. Since the `C_new` controls use an existing lattice character at no larger leaf action than the already audited `P,D` genealogy, they create no new maximal-action character outside this finite audit.

A publication-final version should interval-certify an explicit numerical value of `w_action,2`; existence is already rigorous from finiteness and strict center margins once the exact center computations are certified.

## 12. Closure statement and remaining architectural barrier

Conditional on the routed support hypothesis

\[
\boxed{C_{old}\notin I_2,}
\tag{C2G23}
\]

the second active gate is closed at the same local PDE/control level as the first:

\[
\boxed{
(P,D)_{in}
\longmapsto
E_{out}=E_*\ne0,
}
\]

with the entire beta-zero root family cancelled at exit and every other critical output action-subcritical.

The remaining barrier to inserting this theorem into the full five-event reset cell is now **support architecture**: construct source-admissible delayed catalyst copies so that the old `C` is absent from the second `P-D` overlap but same-character catalyst packets are available for the later `E-C` and `Q-C` events, without introducing a leading cutoff residual or a refreshed early collision.

No autonomous infinite cascade and no unforced Navier--Stokes blowup theorem is claimed.
