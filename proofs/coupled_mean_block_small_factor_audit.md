# Coupled angular-mean contraction: block-by-block small-factor audit

**Status:** CONDITIONAL NEAR-CLOSURE THEOREM. This note assembles the small factors already available in the branch and in Sections 8--9 of the OpenAI source construction. It does **not** yet declare the local zero-force relay closed, because one common Gevrey-profile compatibility statement for all fixed cutoffs/coefficient maps remains to be written.

The mean unknown is denoted by `m`, and the exact nonzero-harmonic correction conditional on `m` by

\[
z=z(m).
\]

Let `Y_{s,\lambda}` denote one fixed positive-radius characteristic Gevrey space controlling the radial variables, auxiliary torus variables, and the physical characteristic derivative `t_*`.

We study the exact reduced map

\[
\boxed{
\mathcal T_\ell(m)
:=
\mathcal J_i\,\mathcal R_{\rm mean}\bigl(m,z(m)\bigr),
}
\tag{C1}
\]

where all bounded radial pressure/stress reconstruction, Haar projections, and the finite five-dimensional moment correction are included inside `R_mean`, while `J_i` is the derivative-loss-free characteristic inverse from `characteristic_fast_time_mean_inverse.md`.

The target is

\[
\boxed{
\|\mathcal T_\ell(m)-\mathcal T_\ell(\tilde m)\|_{Y_{s,\lambda_*}}
\le
\eta_\ell
\|m-\tilde m\|_{Y_{s,\lambda_*}},
\qquad
\eta_\ell\to0.
}
\tag{C2}
\]

## 1. Characteristic inverse block

The exact causal inverse satisfies

\[
\|\mathcal J_iF\|_{Y_{s,\lambda_*}}
\le L\|F\|_{Y_{s,\lambda_*}}
\tag{C3}
\]

on a fixed normalized characteristic strip. Hence the fast-time inversion contributes **no small divisor and no derivative loss**. It multiplies the final Lipschitz constant only by the fixed factor `L`.

Thus no Nash--Moser smoothing is needed for this block.

## 2. Pressure, Haar projection, and finite moment inverses

The source mean construction contains bounded radial pressure/stress inversions, Haar-average projections, and a five-dimensional moment map inverted by a fixed Vandermonde matrix on reserved profiles.

All these operations are order-zero on a fixed compact support class, after one fixes the source profiles. Therefore they contribute only a polynomial bookkeeping factor

\[
C_MS_*^C,
\tag{C4}
\]

and do not destroy a positive epsilon gain already present in the nonlinear residual.

## 3. Five-dimensional nonlinear recomputation block

Source Lemma 8.8 states that if the current target lies in source class `S^alpha`, `alpha>=0.9`, then the nonlinear defects after the exact five-dimensional linear correction improve to

\[
(P_{\rm new},J_{\theta,\rm new},J_{z,\rm new})
\in
S^{\alpha+0.9-2\kappa_s}.
\]

The corresponding local difference estimate therefore has the schematic form

\[
\boxed{
\eta_{\rm mom,\ell}
\le
C_MS_*^C\varepsilon^{0.9-2\kappa_s}.
}
\tag{C5}
\]

This tends to zero in the source parameter regime.

## 4. Mean-to-nonzero-to-mean covariance block

`nonzero_mean_sensitivity.md` quantifies the dependence of the exact forward nonzero solution on the mean input. The small correction itself satisfies

\[
\|z(m)-z(\tilde m)\|
\le
C\rho_\ell\|m-\tilde m\|.
\]

However the full covariance variation also contains the designated primary wave `w_pr`, of source size `W_{1/2}`. The source product law

\[
W_\alpha\times W_{\alpha'}
\longrightarrow
M_{\alpha+\alpha'-\kappa_s}
\]

therefore gives the larger but still small feedback scale

\[
\boxed{
\eta_{\rm wave,\ell}
\le
C_MS_*^C
\left(
\varepsilon^{1/2-\kappa_s}
+ho_\ell
\right).
}
\tag{C6}
\]

The conservative nonzero defect parameter is

\[
\boxed{
\rho_\ell
\lesssim
S_*^C\varepsilon^{1/5}
+S_*^Ce^{-c_MS_*}.
}
\tag{C7}
\]

Hence this entire feedback block is `o(1)`.

## 5. Signed stress correction block

The source signed stress correction is exact at principal covariance level. The residual after the correction comes from interaction with the previous wave remainder, curl/reconstruction remainders, and self-covariance of the new correction. In the source induction this block receives a conservative positive exponent gain recorded in Proposition 9.6 as `+0.17`.

For the local Lipschitz audit we therefore assign

\[
\boxed{
\eta_{\rm stress,\ell}
\le
C_MS_*^C\varepsilon^{0.17}.
}
\tag{C8}
\]

This is deliberately conservative: the purpose is only to retain one explicit positive exponent that is certified by the source finite-stage stress calculus.

## 6. Slow-time/transport remainder block

After the exact characteristic temporal correction, the remaining slow-time and transport terms inherit a positive source epsilon gain. The weakest gain is no worse than the already-listed positive exponents in the mean correction hierarchy, so for the contraction theorem they may be absorbed into

\[
C_MS_*^C\varepsilon^{0.9-2\kappa_s}
\]

or, if one wishes to avoid identifying a sharper exponent before a final source-by-source transcription, into a generic term

\[
C_MS_*^C\varepsilon^{\delta_{\rm tr}},
\qquad
\delta_{\rm tr}>0.
\tag{C9}
\]

No zero-order `O(1)` nonlinear transport feedback has been identified in the current audit.

## 7. Radial compactification block

The repaired one-shot Fourier--Gevrey theorem in `gevrey_radial_compactification_remainder.md` gives

\[
\boxed{
\eta_{\rm rad,\ell}
\le
\tau_{\rm rad,\ell}
:=
C\exp\{-cM_{\rm rad}^{1/(2s)}\}.
}
\tag{C10}
\]

With the source radial scaling

\[
M_{\rm rad}^{-1}
\lesssim
\varepsilon^{\kappa_s}S_*^{\rho_g},
\]

this becomes

\[
\boxed{
\tau_{\rm rad,\ell}
\le
C\exp\!\left[
-c\varepsilon^{-\kappa_s/(2s)}
S_*^{-\rho_g/(2s)}
\right]
=o(1).
}
\tag{C11}
\]

Only one fixed Gevrey-radius loss is paid.

## 8. Combined contraction constant

Combining (C3)--(C11), the full reduced map obeys the conditional estimate

\[
\boxed{
\eta_\ell
\le
C_MS_*^C
\left[
\varepsilon^{0.17}
+
\varepsilon^{1/2-\kappa_s}
+
\varepsilon^{0.9-2\kappa_s}
+
\rho_\ell
+
\varepsilon^{\delta_{\rm tr}}
\right]
+
\tau_{\rm rad,\ell}.
}
\tag{C12}
\]

Since

\[
S_*=\ell^2,
\qquad
\varepsilon=Q^h=2^{-h\ell},
\]

all fixed polynomial powers of `S_*` are dominated by every positive power of `epsilon`. Therefore, provided

\[
\boxed{
\kappa_s<\frac12
\quad\text{and}\quad
0.9-2\kappa_s>0,
}
\tag{C13}
\]

and the source profile parameters satisfy the already-used radial scaling, one obtains

\[
\boxed{\eta_\ell\to0.}
\tag{C14}
\]

Thus for sufficiently large dyadic level the numerical small-factor structure required for Banach contraction is present.

## 9. What still prevents an unconditional closure claim

The only remaining local functional-analytic obligation identified by this audit is **profile compatibility in one common characteristic Gevrey space**.

Concretely, one must verify that:

1. every fixed compact cutoff used by the pressure/stress/radial reconstruction can be chosen in one `G^s` class;
2. products, reserved bump profiles, coordinate changes, and the finite Vandermonde correction map preserve a fixed positive final radius after finitely many losses;
3. the nonzero forward propagator estimates used in `nonzero_mean_sensitivity.md` hold uniformly with the same finite collection of Gevrey/characteristic seminorms;
4. the source signed-stress estimate with the `+0.17` gain can be transcribed as a Lipschitz difference estimate, not only as a size estimate, in that same space.

These are finite compatibility checks, not a new infinite derivative-loss mechanism.

## 10. Conditional local theorem

Assume the four common-space compatibility statements in Section 9. Then there exist `lambda_*>0`, `r_ell->0`, and `ell_0` such that for every `ell>=ell_0`, the reduced mean map `T_ell` maps the closed ball

\[
B_{r_\ell}(0)\subset Y_{s,\lambda_*}
\]

into itself and is a strict contraction. Hence there exists a unique exact angular mean

\[
\boxed{m_\ell=T_\ell(m_\ell).}
\tag{C15}
\]

Substitution into the already exact nonzero forward solution yields

\[
\boxed{z_\ell=z(m_\ell).}
\tag{C16}
\]

and therefore exact local zero-force closure on the relay collar.

Because Section 9 has not yet been fully discharged in the repository, (C15)--(C16) are at present a **conditional theorem**, not the publication-final Controlled-Overlap Local Difference-Relay Theorem.

## 11. Immediate next move

The next mathematical task is now sharply finite: write `proofs/common_characteristic_gevrey_profile_compatibility.md` and either prove all four items in Section 9 or isolate the first one that fails. If they all close, the local zero-force relay crosses its theorem threshold and the project can move to physical-scale inheritance.