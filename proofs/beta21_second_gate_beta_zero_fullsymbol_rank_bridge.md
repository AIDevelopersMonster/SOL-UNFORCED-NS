# Full-symbol rank bridge for the beta-zero root control

**Status:** PROVED LOCAL RANK-PERSISTENCE BRIDGE. The root `M=2D-P` has signed beta zero and therefore belongs to the strictly viscous `T=0` sector rather than to the positive-beta growing pulse sector. This does not invalidate the seven-control root Vandermonde. The beta-zero linear mode has a stage-uniform forward-stable propagator; after an integrating-factor normalization its scalar source-generated component is a bounded nonvanishing perturbation of the frozen root coordinate. On a sufficiently short fixed source collar the full-symbol seven-control response remains invertible.

This note corrects the interpretation of `M` in the preceding root-control notes: `M` is a beta-zero viscous harmonic/mean-sector mode, not a positive-beta pulse. Its **source** is nevertheless generated at the promoted leaf action and must be controlled because polynomial stable inversion cannot erase a positive `e^{Delta S_*}` downstream action advantage.

## 1. Exact status of `T=0`

For a lattice character with signed tangential beta `T=0`, the inviscid growing contribution vanishes. `finite_critical_block_uniform_stable_inverse.md` proves that every nonzero such lattice index has a nonzero radial normal and is purely viscously damped.

For the specific root

\[
M=2D-P,
\]

the radial normal is nonzero because `z_D != z_P`. Thus there exists a fixed design-dependent stable rate and a full localized forward inverse on the `M` harmonic.

In particular the exact localized linear propagator obeys

\[
\boxed{
\|V_M(v,w)\|\le C_M
}
\tag{BZ1}
\]

uniformly in the dyadic level on one fixed bounded source collar. At high radial lattice index the inverse even gains the quadratic smoothing recorded in the stable-complement theorem; for this one fixed root only boundedness is required.

## 2. Why stable inversion does not remove the action danger

Let the root source carry action `A_M`. Applying the stable inverse changes its packet norm by a design-dependent polynomial/bounded factor, not by a fixed factor

\[
e^{-cS_*}.
\]

Hence the resulting root response still has action `A_M` in the exponential bookkeeping. Subsequent mean-root sidebands therefore retain the exact leaf actions recorded in `beta21_second_gate_mean_root_factorization.md`.

Thus the positive defects of `H_1,...,H_4` cannot be dismissed merely because the intermediate root is linearly stable.

## 3. Source-generated scalar root direction

The difference interaction `D-C_new -> M` produces a fixed nonzero divergence-free beta-zero source polarization `b_M`. Choose a bounded output functional `lambda_M` on the finite polarization space such that

\[
\lambda_M(b_M)=1.
\tag{BZ2}
\]

At zero propagation length,

\[
\lambda_M V_M(w,w)b_M=1.
\]

By continuity of the finite-dimensional/full-symbol propagator, there exists a positive source-collar length `L_M` such that

\[
\boxed{
|\lambda_M V_M(v,w)b_M|\ge\frac12
}
\tag{BZ3}
\]

whenever `0<=v-w<=L_M`.

All other beta-zero polarization components produced by the full symbol remain in the uniformly stable complement and may be included in the exact correction state.

Thus the root control has a genuine nonvanishing scalar input-output channel on a sufficiently short fixed collar.

## 4. Integrating-factor form

In a frozen scalar reference model write the selected root coordinate as

\[
M'+d_M M=q_M,
\qquad d_M>0.
\tag{BZ4}
\]

Set

\[
\widetilde M(v)=e^{d_Mv}M(v).
\]

Then

\[
\widetilde M'=e^{d_Mv}q_M(v).
\tag{BZ5}
\]

For a translated source `q(v-tau)`,

\[
e^{d_Mv}q(v-\tau)
=e^{d_M\tau}\,\widetilde q(v-\tau),
\qquad
\widetilde q(r):=e^{d_Mr}q(r).
\tag{BZ6}
\]

Hence stable damping changes only

1. one nonzero column factor `e^{d_M tau}`; and
2. the common smooth profile from `q` to `tilde q`.

Its mass is

\[
\widetilde\mu_0=\int e^{d_Mr}q(r)dr,
\]

which is nonzero for a nonnegative/nontrivial source profile and, generically, after arbitrarily small profile perturbation.

Therefore the ordinary translated-profile Vandermonde determinant is not destroyed by the beta-zero viscous diagonal.

## 5. Full root-chain linearization

Restore the six downstream root-family states. After integrating-factor normalization of every diagonal homogeneous transport, the linearized state has the form

\[
X'=A_{full}(v)X+B_{full}(v)q,
\tag{BZ7}
\]

on a fixed short collar, with

\[
A_{full}(v)=A_0+E_A(v),
\qquad
B_{full}(v)=b_0e_1+E_B(v).
\tag{BZ8}
\]

Here `A_0` is the frozen lower-triangular matrix from the seven-control theorem, with all six first-subdiagonal coefficients nonzero, and `b_0 != 0` is the selected scalar root source coefficient.

By continuity of the exact source/frame coefficients, for every frozen determinant margin `d_7>0` there is a positive collar width `w_{full}` such that

\[
\|E_A\|+\|E_B\|<\eta(d_7)
\tag{BZ9}
\]

throughout that collar. The seven translated full-symbol Volterra columns then satisfy

\[
J_{7,full}=J_{7,0}+E_7,
\qquad
\|E_7\|<\eta_7.
\tag{BZ10}
\]

Taking the collar/profile perturbation threshold sufficiently small gives

\[
\boxed{
|\det J_{7,full}|
\ge\frac12|\det J_{7,0}|>0.
}
\tag{BZ11}

The collar width is fixed after the finite-`u` design is frozen and is independent of the dyadic level.

## 6. Dyadic frame perturbations

The actual source frame, curl realization and phase transport differ from the frozen full-symbol coefficients by

\[
O(S_*^{-1})
+O(S_*^C\varepsilon^{\delta})
\]

in the fixed packet norms. Therefore, after the positive collar is fixed, the exact designated linear response satisfies

\[
\boxed{
J_{7,des,\ell}
=J_{7,full}+o(1).
}
\tag{BZ12}

Consequently

\[
\boxed{
|\det J_{7,des,\ell}|
\ge\frac14|\det J_{7,0}|>0
}
\tag{BZ13}
\]

for all sufficiently high dyadic levels.

## 7. Consequence

The beta-zero nature of `M` changes the propagator but not the finite rank conclusion:

\[
\boxed{
\text{source-matched }C_{new}\text{ controls}
\to
\text{stable beta-zero root source}
\to
\text{full mean-root sideband chain}
}
\]

still has a seven-dimensional locally onto designated response map.

The remaining step is no longer principal/full-symbol rank. It is the parameter-dependent exact zero-residual transfer, in action-normalized coordinates, including the stable beta-zero response inside the designated finite block rather than hiding it in the small correction.
