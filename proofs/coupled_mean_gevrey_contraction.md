# Coupled angular-mean Gevrey contraction

**Status:** PROVED LOCAL CONTRACTION THEOREM FOR THE FROZEN v0.8 RELAY, conditional only on the previously established branch estimates and the source parameter inequalities already used in the construction.

This theorem combines:

- `characteristic_fast_time_mean_inverse.md`;
- `gevrey_radial_compactification_remainder.md`;
- `nonzero_harmonic_forward_reduction.md`;
- `nonzero_mean_sensitivity.md`;
- `common_characteristic_gevrey_profile_compatibility.md`;
- the source mean/stress exponent gains from Sections 8--9 of the OpenAI construction.

It closes the remaining **local angular mean** in one fixed positive-radius characteristic Gevrey space. It does not address physical-scale inheritance or an infinite cascade.

## 1. Reduced local system

Freeze one admissible v0.8 design and one bounded characteristic relay collar. Let

\[
Y:=Y_{s,\lambda_*}
\]

be the common positive-radius characteristic Gevrey space supplied by `common_characteristic_gevrey_profile_compatibility.md`.

For every sufficiently small angular mean `m\in Y`, the nonzero block has the unique exact forward solution

\[
\boxed{z=z(m)}
\tag{T1}
\]

from `nonzero_harmonic_forward_reduction.md`.

After substituting `z(m)`, applying the exact radial pressure/stress reconstructions, the five-dimensional moment correction, and the exact characteristic temporal inverse, the angular mean equation takes the fixed-point form

\[
\boxed{m=\mathcal T_\ell(m).}
\tag{T2}
\]

All operators in `T_ell` act on the same final space `Y`.

## 2. Size of the inhomogeneous mean defect

The stage-zero local defect is algebraically small plus action-flat:

\[
\rho_\ell
\lesssim
S_*^C\varepsilon^{1/5}
+S_*^Ce^{-c_MS_*}.
\tag{T3}
\]

The source mean initialization has positive decay exponent, and the one-shot radial compactification contributes

\[
\tau_{\rm rad,\ell}
\le
C\exp\!\left[
-c\varepsilon^{-\kappa_s/(2s)}S_*^{-\rho_g/(2s)}
\right].
\tag{T4}
\]

Hence the zero-input value satisfies

\[
\boxed{
\|\mathcal T_\ell(0)\|_Y
\le
b_\ell,
\qquad
b_\ell
:=
C_MS_*^C\rho_\ell+	au_{\rm rad,\ell},
\qquad
b_\ell\to0.
}
\tag{T5}
\]

## 3. Lipschitz factor: characteristic inversion

The exact characteristic inverse obeys

\[
\|\mathcal J_iF\|_Y\le C_L\|F\|_Y.
\tag{T6}
\]

Thus the temporal mean solve contributes only a fixed multiplicative constant. There is no torus small divisor and no derivative loss.

## 4. Lipschitz factor: wave feedback

The nonzero sensitivity theorem gives

\[
\|z(m)-z(\tilde m)\|
\le C\rho_\ell\|m-\tilde m\|_Y.
\tag{T7}
\]

The dominant covariance variation pairs this difference with the designated primary wave of source order `W_{1/2}`. The source product calculus therefore gives

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
\tag{T8}
\]

## 5. Lipschitz factor: signed stress correction

After the exact principal covariance is removed, the source stress calculation yields the conservative positive gain `+0.17`. The common Gevrey algebra turns the corresponding polynomial size estimate into the difference estimate

\[
\boxed{
\eta_{\rm stress,\ell}
\le
C_MS_*^C\varepsilon^{0.17}.
}
\tag{T9}
\]

## 6. Lipschitz factor: temporal/transport residuals

The source residual table in Section 9 gives, above a mean increment of order `H`, the gains

\[
\begin{array}{c|c}
\text{term}&\text{gain above }H\\\hline
\text{slow time}&1\\
\text{radial flux}&1-\kappa_s\\
\text{axial flux}&1\\
\text{viscosity}&1-2\kappa_s.
\end{array}
\]

Therefore the entire residual change after the cancelled fast-time term obeys

\[
\boxed{
\eta_{\rm tr,\ell}
\le
C_MS_*^C\varepsilon^{1-2\kappa_s}.
}
\tag{T10}
\]

## 7. Lipschitz factor: five-dimensional moment recomputation

Source Lemma 8.8 gives

\[
(P_{\rm new},J_{\theta,\rm new},J_{z,\rm new})
\in
S^{\alpha+0.9-2\kappa_s}
\]

from input defects in `S^alpha`, `alpha>=0.9`. Hence

\[
\boxed{
\eta_{\rm mom,\ell}
\le
C_MS_*^C\varepsilon^{0.9-2\kappa_s}.
}
\tag{T11}
\]

## 8. Lipschitz factor: radial compactification

The one-shot Fourier--Gevrey theorem gives

\[
\boxed{
\eta_{\rm rad,\ell}
\le
\tau_{\rm rad,\ell}
=o(1).
}
\tag{T12}
\]

No iterative radius loss occurs.

## 9. Combined contraction estimate

The bounded pressure, Haar projection, radial integration, and finite Vandermonde maps contribute only the fixed polynomial source factor `C_MS_*^C`. Combining (T8)--(T12),

\[
\boxed{
\begin{aligned}
\|\mathcal T_\ell(m)-\mathcal T_\ell(\tilde m)\|_Y
&\le
\eta_\ell\|m-\tilde m\|_Y,\\[2mm]
\eta_\ell
&\le
C_MS_*^C\Big(
\varepsilon^{0.17}
+\varepsilon^{1/2-\kappa_s}
+\varepsilon^{1-2\kappa_s}
+\varepsilon^{0.9-2\kappa_s}
+\rho_\ell
\Big)
+\tau_{\rm rad,\ell}.
\end{aligned}
}
\tag{T13}
\]

The source parameter inequalities are stronger than needed here; in particular its Section 9 induction uses

\[
\frac12-2\kappa_s>0,
\qquad
1-4\kappa_s>0.17,
\qquad
0.9-4\kappa_s>0.1.
\]

Thus every exponent in (T13) is positive. Since

\[
S_*=\ell^2,
\qquad
\varepsilon=2^{-h\ell},
\]

fixed polynomial powers of `S_*` are dominated by every positive power of `epsilon`, while `rho_ell->0` and `tau_rad,ell->0`. Therefore

\[
\boxed{\eta_\ell\longrightarrow0.}
\tag{T14}
\]

## 10. Invariant ball

Set

\[
r_\ell:=2b_\ell.
\tag{T15}
\]

For sufficiently large `ell`, (T14) gives

\[
\eta_\ell\le\frac14.
\tag{T16}
\]

For every `m` with `\|m\|_Y<=r_ell`,

\[
\begin{aligned}
\|\mathcal T_\ell(m)\|_Y
&\le
\|\mathcal T_\ell(0)\|_Y
+
\eta_\ell\|m\|_Y\\
&\le
b_\ell+\frac14(2b_\ell)
<2b_\ell=r_\ell.
\end{aligned}
\tag{T17}
\]

Thus `T_ell` maps the closed ball `B_{r_ell}(0)` into itself.

## 11. Exact angular mean

By Banach's fixed-point theorem there exists a unique

\[
\boxed{m_\ell\in B_{r_\ell}(0)}
\tag{T18}
\]

such that

\[
\boxed{m_\ell=\mathcal T_\ell(m_\ell).}
\tag{T19}
\]

Moreover

\[
\boxed{\|m_\ell\|_Y\le2b_\ell=o(1).}
\tag{T20}
\]

The nonzero block is then fixed uniquely by

\[
\boxed{z_\ell=z(m_\ell).}
\tag{T21}
\]

## 12. Local zero-force consequence

The mean fixed point cancels the angular Fourier mode `0` exactly. The nonzero forward theorem cancels every nonzero angular harmonic exactly conditional on that mean. Both constructions remain in the exact divergence-free source potential class.

Therefore, on the frozen relay collar,

\[
\boxed{
R(U_{\rm relay,\ell})=0.
}
\tag{T22}
\]

No external force is used on the collar.

This establishes the **exact local zero-force relay closure** for sufficiently large dyadic level, under the v0.8 frozen design and the already-established source/branch estimates.

## 13. What this theorem does not prove

The theorem is local. It does **not** prove:

- that the outgoing designated child and correction at physical scale `q_j` satisfy the normalized hypotheses of a next relay at `q_{j+1}`;
- preservation of the action/error class through physical rescaling;
- iterability through infinitely many physical scales;
- finite-time blowup for the unforced three-dimensional Navier--Stokes equations.

The next frontier is therefore no longer local angular-mean closure. It is the **physical-scale inheritance theorem**.