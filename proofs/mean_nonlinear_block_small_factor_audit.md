# Mean nonlinear map: blockwise small-factor audit

**Status:** PARTIAL THEOREM / REDUCED PROOF OBLIGATION.

This note carries out the next local reduction after the exact nonzero-harmonic forward solve. The goal is to decompose the differentiated angular-mean map into explicit blocks and identify the small factor attached to each block.

The conclusion is deliberately narrower than a full closure theorem. All non-radial nonlinear blocks admit a positive small factor in the source exponent calculus. The only block that cannot yet be assigned an `o(1)` factor in one unrestricted fixed-radius compactly supported Gevrey space is the radial compactification block. That obstruction is isolated in `radial_gevrey_radius_loss_and_same_space_obstruction.md`. A one-sided radial input-output alternative is developed in `radial_characteristic_forward_inverse.md`.

## 1. Reduced mean map

Let `m` denote the full angularly invariant correction and let

\[
\boxed{z=z(m)}
\tag{MB1}
\]

be the exact nonzero-harmonic forward solution from `nonzero_harmonic_forward_reduction.md`.

The exact mean residual may be schematically decomposed as

\[
\mathcal F_{\rm mean}(m,z)
=
F_{\rm tr}
+F_{\rm cov}
+F_{\rm mom}
+F_{\rm rad}
+F_{\rm rem},
\tag{MB2}
\]

where:

- `F_tr` contains the zero-Haar-average temporal/transport mean equations;
- `F_cov` contains wave-covariance and signed-stress feedback;
- `F_mom` is the finite five-dimensional moment-defect recomputation;
- `F_rad` contains the compact radial pressure/stress realization and its cutoff remainder;
- `F_rem` contains the already supported algebraic/action-flat source residuals.

After inserting the exact characteristic temporal inverse and the finite moment inverse, the nonlinear mean map has the form

\[
\boxed{
\mathcal N_{\rm mean}(m)
=\mathcal G_{\rm tr}F_{\rm tr}(m,z(m))
+\mathcal G_{\rm mom}F_{\rm mom}(m,z(m))
+\mathcal G_{\rm cov}F_{\rm cov}(m,z(m))
+\mathcal G_{\rm rad}F_{\rm rad}(m,z(m))
+F_{\rm rem}.
}
\tag{MB3}
\]

The point of the audit is to estimate the Fréchet difference of each block.

## 2. Source exponent rules used in the audit

The source Section 9 calculus supplies the following structural rules at the orders relevant here.

The primary designated wave is of order

\[
\boxed{W_{1/2}.}
\tag{MB4}
\]

The mixed mean-wave product satisfies schematically

\[
\boxed{
W_\alpha\times M_\mu
\longrightarrow
W_{\alpha+\mu-1/2},
}
\tag{MB5}
\]

while a conjugate wave pair contributes to the mean according to

\[
\boxed{
W_\alpha\times W_{\alpha'}
\longrightarrow
M_{\alpha+\alpha'-\kappa_s}.
}
\tag{MB6}
\]

The five-dimensional defect recomputation from source Lemma 8.8 gains

\[
\boxed{
0.9-2\kappa_s>0.
}
\tag{MB7}
\]

The supported nonzero defect entering the exact forward solve obeys

\[
\boxed{
\rho_\ell
\lesssim
S_*^C\varepsilon^{1/5}
+S_*^Ce^{-c_MS_*}.
}
\tag{MB8}
\]

All constants below may depend on the frozen relay design and the fixed collar, but not on harmonic truncation or nonlinear iteration step.

## 3. Block A: temporal/transport mean correction

The zero-Haar-average temporal equation is inverted by the exact characteristic operator

\[
\mathcal J_i=t_*^{-1},
\qquad
t_*=-\varepsilon\partial_T+c_iN_i.
\]

`characteristic_fast_time_mean_inverse.md` proves

\[
\boxed{
\|\mathcal J_iF\|_{G^s_L}
\le C_L\|F\|_{G^s_L}
}
\tag{MB9}
\]

in characteristic Gevrey norms, with no torus derivative loss.

Hence the temporal inverse itself contributes no adverse power of `epsilon`. The smallness of this block comes entirely from the differentiated nonlinear source. The source slow-time/transport bookkeeping yields a positive gain; at the level needed for the present audit we record conservatively

\[
\boxed{
\eta_{\rm tr,\ell}
\lesssim
C_MS_*^C\varepsilon^{1-2\kappa_s}.
}
\tag{MB10}
\]

The exact numerical exponent is not the bottleneck; only positivity is used below.

## 4. Block B: finite five-dimensional moment correction

The linear five-dimensional map is invertible by the source Vandermonde construction. Its inverse is a fixed bounded operator on the reserved mean patch.

The important point is that the **linear defect is removed exactly**. Source Lemma 8.8 then places the recomputed nonlinear defect at a higher exponent:

\[
(P_{\rm new},J_{\theta,\rm new},J_{z,\rm new})
\in
S^{\alpha+0.9-2\kappa_s}.
\]

Therefore the differentiated moment block satisfies

\[
\boxed{
\|\delta\mathcal N_{\rm mom}\|
\le
C_MS_*^C
\varepsilon^{0.9-2\kappa_s}
\|\delta m\|.
}
\tag{MB11}
\]

Thus

\[
\boxed{
\eta_{\rm mom,\ell}
\lesssim
C_MS_*^C\varepsilon^{0.9-2\kappa_s}
=o(1).
}
\tag{MB12}
\]

This block is closed modulo routine translation of the source `S^alpha` notation into the chosen characteristic Gevrey norm.

## 5. Block C: mean-to-wave-to-mean feedback

Let

\[
\delta m=m-\widetilde m,
\qquad
\delta z=z(m)-z(\widetilde m).
\]

The full linearized nonzero propagator already absorbs the designated parent/catalyst/child linearization. A mean perturbation acts as a first-order coefficient perturbation. By (MB5) with the primary wave order `1/2`, an input mean perturbation of order `M_mu` generates a wave perturbation of the **same exponent order**:

\[
W_{1/2}\times M_\mu
\longrightarrow W_\mu.
\tag{MB13}
\]

Accordingly the quantitative refinement required from the forward theorem is

\[
\boxed{
\|\delta z\|_{W_\mu}
\le C_M\|\delta m\|_{M_\mu}
+O(\rho_\ell)\|\delta m\|.
}
\tag{MB14}
\]

Now pair `delta z` with the primary `W_{1/2}` wave. By (MB6),

\[
W_{1/2}\times W_\mu
\longrightarrow
M_{\mu+1/2-\kappa_s}.
\]

Therefore the principal mean feedback gains

\[
\boxed{
\varepsilon^{1/2-\kappa_s}.
}
\tag{MB15}
\]

The remaining interactions contain either two small corrections or one supported defect and hence gain at least `rho_l` in addition. Consequently the target Lipschitz estimate is

\[
\boxed{
\|\delta\mathcal N_{w\to m}\|
\le
C_MS_*^C
\left(
\varepsilon^{1/2-\kappa_s}
+\rho_\ell
\right)
\|\delta m\|.
}
\tag{MB16}
\]

This is the precise quantitative statement still to be inserted into `nonzero_harmonic_forward_reduction.md`; its qualitative local Lipschitz dependence is already proved there.

## 6. Block D: signed-stress covariance correction

The source signed-stress construction removes the prescribed principal covariance exactly near the primary waves. The remaining terms are interactions with the pre-existing wave remainder, curl/reconstruction remainders, and the self-covariance of the correcting wave packet.

The source Proposition 9.6 records a conservative positive gain of approximately

\[
\boxed{0.17}
\tag{MB17}
\]

in the relevant defect order after the stress correction. For the present local audit this gives the safe bound

\[
\boxed{
\eta_{\rm stress,\ell}
\lesssim
C_MS_*^C\varepsilon^{0.17}.
}
\tag{MB18}
\]

No claim is made that `0.17` is optimal. It is used only because it is explicitly positive and source-supported.

A publication version should replace the decimal shorthand by the exact source rational/exponent combination once all source parameters are frozen.

## 7. Block E: supported algebraic and action-flat remainder

Every already-supported source remainder entering the mean equations is bounded by the same conservative local defect scale as the nonzero system:

\[
\boxed{
\eta_{\rm rem,\ell}
\lesssim C_M\rho_\ell.
}
\tag{MB19}
\]

Since

\[
\rho_\ell
\lesssim
S_*^C\varepsilon^{1/5}+S_*^Ce^{-c_MS_*},
\]

this tends to zero at large dyadic level.

## 8. Block F: radial compactification

This block is qualitatively different.

If one keeps the source requirement of two-sided compact radial support, the cutoff remainder `A_e` is tiny across a fixed Gevrey radius gap:

\[
\boxed{
\|A_ef\|_{G^s_{L_2}}
\le
C\exp[-cM_r^{1/(2s)}]
\|f\|_{G^s_{L_0}},
\qquad L_2<L_0.
}
\tag{MB20}
\]

However `radial_gevrey_radius_loss_and_same_space_obstruction.md` proves that, on the unrestricted one-radius space, near-resonant torus modes prevent

\[
\|A_ef\|_{G^s_L}
\le\eta(M_r)\|f\|_{G^s_L},
\qquad \eta(M_r)\to0.
\]

Thus the compact radial block cannot presently be included in a one-space Banach contraction merely by assigning it a stretched-exponential small factor.

There are only three legitimate routes:

1. prove a spectral restriction on the actual nonlinear range excluding the near-resonant family;
2. use a scale of Gevrey spaces and pay controlled radius loss;
3. remove the two-sided compact radial condition and use the one-sided radial characteristic inverse from `radial_characteristic_forward_inverse.md`.

The third route is currently preferred because it matches the already-adopted temporal input-output architecture.

## 9. Aggregate non-radial contraction constant

Excluding the compact radial boundary mechanism, the differentiated nonlinear mean map has the bound

\[
\boxed{
\eta_{\rm nr,\ell}
\le
C_MS_*^C
\left[
\varepsilon^{0.17}
+\varepsilon^{1/2-\kappa_s}
+\varepsilon^{0.9-2\kappa_s}
+\varepsilon^{1-2\kappa_s}
+\rho_\ell
\right].
}
\tag{MB21}
\]

For the source parameter range all displayed exponents are positive, and `rho_l -> 0`. Therefore

\[
\boxed{
\eta_{\rm nr,\ell}\to0.
}
\tag{MB22}
\]

This is the main result of the block audit: **there is no remaining visible O(1) nonlinear feedback outside the radial compact-support mechanism.**

## 10. Preferred next theorem

The sharp target is now the following.

### Coupled temporal-radial characteristic mean theorem

Reorganize the full mean system on a bounded temporal-radial collar so that:

1. all linear mean terms are absorbed into a bounded characteristic forward propagator;
2. the temporal zero-average inverse uses `mathcal J_i`;
3. radial pressure/stress inversions use the one-sided radial characteristic inverse;
4. the five-dimensional moment block is solved exactly;
5. the nonzero harmonic field is `z=z(m)`;
6. the differentiated nonlinear source obeys the aggregate estimate (MB21).

Then

\[
\boxed{
\|\mathcal N_{\rm mean}(m)-\mathcal N_{\rm mean}(\widetilde m)\|
\le
\eta_{\rm nr,\ell}
\|m-\widetilde m\|,
\qquad
\eta_{\rm nr,\ell}\to0,
}
\tag{MB23}
\]

and Banach contraction closes the exact local mean equation.

## 11. Remaining proof obligations

The local zero-force theorem is **not yet closed**. The remaining obligations are now sharply identified:

- prove the quantitative exponent-preserving `m -> z(m)` difference estimate (MB14) in the actual packet/Gevrey norm;
- rewrite the radial pressure/stress part of the complete source mean equations with a simultaneous one-sided radial boundary condition and verify that no hidden global moment condition re-enters;
- verify the signed-stress block in the same norm and pin the exact positive exponent replacing the conservative `0.17` shorthand;
- combine all bounded linear pieces into one forward mean propagator and prove (MB23).

If these four items close, the local zero-force relay is closed. The next frontier would then become physical-scale inheritance.
