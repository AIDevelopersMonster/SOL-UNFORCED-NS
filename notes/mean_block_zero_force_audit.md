# Angular-mean block audit for exact zero-force closure

**Status:** SOURCE AUDIT / CORRECTION OF PREVIOUS OVERCLAIM. This note identifies what remains after the nonzero-harmonic forward reduction. The angular mean is not a minor bookkeeping detail: it has its own pressure, radial-moment, auxiliary-torus, and five-dimensional correction system in Section 8 of the OpenAI construction.

The previous statement in `forward_relay_input_output_closure.md` that the full local residual was already exactly zero was premature. What is now proved is exact forward closure of the **nonzero-harmonic block conditional on the mean**. The mean block still requires an exact infinite correction argument.

## 1. Why the mean cannot be omitted

Let `w` be the real nonzero-harmonic wave field. Even if every non-designated nonzero harmonic is action-subcritical,

\[
\langle w_a w_b\rangle_\theta
\]

is generally nonzero because every harmonic interacts with its conjugate. Hence the angular Fourier index `0` is generated quadratically and is not represented by the nonzero two-generator lattice used in the v0.8 action-filter theorem.

The source explicitly separates the actual velocity as

\[
u=(b+\beta,V+v,G+\gamma)+w,
\qquad \langle w\rangle_\theta=0,
\]

with an angularly invariant mean correction `(beta,v,gamma)` and covariance

\[
W_{ab}=\langle w_aw_b\rangle_\theta.
\]

Thus exact local closure must solve both the nonzero wave equations and the mean equations.

## 2. The source mean system has three distinct pieces

Section 8 contains three logically different inversions.

### 2.1 Radial pressure/stress inversion

For auxiliary-averaged sources, compact radial inversion of

\[
(D_r+e/R)\phi=f,
\qquad e\in\{0,1,2\},
\]

requires a weighted radial moment condition. Proposition 8.3 reconstructs the mean pressure from the radial source and produces divergence-free meridional corrections. Corollary 8.5 reconstructs the auxiliary-averaged tangential stress after the required weighted moments are removed.

### 2.2 Torus-dependent zero-average temporal inversion

The part of the angular mean with zero auxiliary-torus average is inverted along the fast auxiliary direction. The source divisor estimate is only polynomial:

\[
|(v_t\cdot k)^{-1}|\le C(1+|k|).
\]

Therefore the inverse is smooth on `C^infty`, but it **loses torus derivatives**. The source handles this at every fixed finite stage by requesting finitely many additional input derivatives.

### 2.3 Five-dimensional moment correction

After pressure, stress, and zero-auxiliary-average corrections, three scalar defects remain:

\[
P,\qquad J_\theta,\qquad J_z.
\]

Lemma 8.7 chooses three fixed azimuthal bump profiles and two fixed axial bump profiles. Their five coefficients solve

\[
\int R^2\Delta v\,dR=0,
\qquad
\int R\gamma_d\,dR=0,
\]

and simultaneously cancel the three displayed linear defect contributions. The source proves invertibility by a Vandermonde argument using distinct radial power moments.

This part is therefore **not** a new rank obstruction for SOL-UNFORCED-NS: the required finite linear map is already explicit and invertible on the reserved mean patch.

## 3. Nonlinear recomputation has a genuine gain

Lemma 8.8 computes the defects after the five-dimensional update. If the current target triple belongs to `S^alpha`, with `alpha>=0.9`, then the recomputed nonlinear defects satisfy

\[
\boxed{
(P_{\rm new},J_{\theta,\rm new},J_{z,\rm new})
\in S^{\alpha+0.9-2\kappa_s}.
}
\tag{M1}

Thus the finite-dimensional defect map has a strong small-parameter gain. Likewise, the temporal mean update leaves slow-time and transport errors with a positive epsilon gain.

This is exactly the structure one would want for an exact nonlinear mean solve.

## 4. Why the source does not already give the exact unforced solve

The published construction only needs a finite correction at each stage and later a Borel/shrinking-cutoff summation whose residual is **flat**, because that flat residual is retained as external forcing.

The source explicitly allows constants in the coefficient estimates to depend on the correction stage and on the requested derivative order. Consequently one may not infer, from the finite-stage exponent gain alone, convergence of an infinite unforced correction series at one fixed physical scale.

The derivative loss of the auxiliary-torus inverse is the sharp technical issue. At finite stage this is harmless: ask for four more torus derivatives. In an infinite exact fixed point, repeatedly paying derivative loss in a single Banach norm is not legitimate.

Therefore the statement

\[
\text{“positive epsilon gain at every finite stage”}
\]

does **not** by itself imply

\[
\text{“there exists an exact infinite mean correction”.}
\]

## 5. Correct decomposition of the initial defect

A second correction to the previous forward theorem concerns the size of the defect.

After the source-style initialization, Proposition 9.5 gives the conservative stage-zero orders

\[
\boxed{B_0=0.7,\qquad C_0^*=1.2.}
\tag{M2}

The primary nonzero wave amplitude has exponent `1/2`. Hence the supported wave residual is only algebraically smaller than the primary wave by

\[
\varepsilon^{B_0-1/2}=\varepsilon^{1/5},
\]

not necessarily by `e^{-cS_*}`.

The correct local small parameter is therefore schematically

\[
\boxed{
\rho_\ell
\lesssim
S_*^C\varepsilon^{1/5}
+
S_*^Ce^{-c_MS_*}.
}
\tag{M3}

The first term comes from ordinary supported source residuals; the second is the stronger v0.8 action-subcritical suppression and the truly flat source cutoff/base pieces.

Both tend to zero as the dyadic level grows, so this correction does not destroy the forward fixed-point strategy. It does change the outgoing error class: before physical-scale inheritance is proved, one should only claim an **algebraically small plus flat** outgoing correction, not a purely flat one.

## 6. Correct local reduction

The current local theorem architecture is now:

\[
\boxed{
\text{nonzero harmonics }z=z(m)
}
\]

from `nonzero_harmonic_forward_reduction.md`, where `m` is the angular mean.

Substitute this solution into the exact mean equations of Section 8. The full local zero-force problem reduces to one mean equation

\[
\boxed{
\mathcal F_{\rm mean}(m;z(m))=0.
}
\tag{M4}

The radial pressure/stress inverses and the five-dimensional moment map are already source-certified bounded operations. The only unresolved functional-analytic step is to solve (M4) **with the derivative-losing auxiliary-torus inverse included**.

## 7. Two plausible routes

### Route A: tame `C^infty` / Nash--Moser

The directional inverse loses only a fixed finite number of torus derivatives, while the nonlinear remainder gains the positive power

\[
\varepsilon^{0.9-2\kappa_s}.
\]

This is a natural tame small-parameter problem. One can try to build a Nash--Moser iteration using the Fourier truncation on the auxiliary torus as the smoothing operator. The five-dimensional moment correction and radial inverse are tame of order zero; only the directional inverse carries the derivative loss.

### Route B: compactly supported Gevrey auxiliary profiles

The auxiliary rectangle cutoffs cannot be real analytic and compactly supported, but they can be chosen Gevrey of order `s>1`. Fourier decay of a Gevrey bump beats every polynomial small divisor. A decreasing-Gevrey-radius iteration may therefore absorb the factor `1+|k|` of the directional inverse while retaining exact compact auxiliary support.

This route may be technically shorter than a full Nash--Moser theorem if the source partitions can be rebuilt within a fixed Gevrey class.

## 8. Immediate theorem target

The correct next target is now:

### Tame mean inverse theorem

Construct a scale of mean spaces `Y_s` and an exact mean correction operator `G_mean` such that

\[
\|G_{\rm mean}F\|_{Y_s}
\le C_s\|F\|_{Y_{s+r}}
\]

for one fixed derivative loss `r`, and prove that the nonlinear recomputation map has the tame gain

\[
\boxed{
\|\mathcal R_{\rm mean}(m)-\mathcal R_{\rm mean}(\tilde m)\|_{Y_s}
\le
C_s\varepsilon^\delta
\|m-\tilde m\|_{Y_{s+r}}
}
\tag{M5}

with some `delta>0` independent of the iteration step.

A Nash--Moser or Gevrey-scale inverse theorem would then solve (M4) exactly and restore the full local zero-force relay theorem.

## 9. Research consequence

The local program has not failed. The large harmonic critical block is no longer the issue, and the nonzero oscillatory system can be reduced forward with its full designated linearization.

The remaining local obstruction is much more specific:

\[
\boxed{
\textbf{exact angular-mean closure with one fixed auxiliary-torus derivative loss.}
}
\]

Until that is solved, the publication threshold for a theorem claiming exact local unforced Navier--Stokes closure is **not crossed**.
