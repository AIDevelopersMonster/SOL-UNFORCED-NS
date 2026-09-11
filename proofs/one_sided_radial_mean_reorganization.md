# One-sided radial reorganization of the complete mean block

**Status:** PROVED ALGEBRAIC/LOCAL REDUCTION. This note shows that the three source compatibility defects `P, J_theta, J_z` and the radial cutoff remainders arise from the requirement of **two-sided compact radial support**. On a bounded radial input-output collar they can be replaced by exact one-sided characteristic inverses and outgoing traces.

This does not yet prove the full coupled temporal-radial contraction. It removes the second remaining obligation in `mean_nonlinear_block_small_factor_audit.md`: no hidden global radial moment condition is needed for the local forward problem.

## 1. Source mean equations

Write the angularly invariant velocity correction as

\[
m=(\beta,v,\gamma)
\]

and the exact nonzero wave field as `w`, with covariance

\[
W_{ab}=\langle w_aw_b\rangle_\theta.
\]

Source Proposition 8.1 writes the angular mean residual as

\[
\boxed{(D_rp_m-g_r,\ E_\theta,\ E_z).}
\tag{R1}
\]

The explicit formulas for `E_theta`, `E_z`, and `g_r` contain the base flow, the mean correction, the wave covariance, pressure, transport, and viscosity.

In the source construction all corrections are required to extend by zero outside the active annulus. That condition forces weighted integral solvability conditions for equations of the form

\[
(D_r+e/R)\phi=f,
\qquad e\in\{0,1,2\}.
\tag{R2}
\]

The resulting scalar obstructions are exactly the quantities later denoted `P`, `J_theta`, and `J_z`.

## 2. One-sided weighted radial inverse

Use the one-sided inverse from `radial_characteristic_forward_inverse.md`. On a bounded shell

\[
R\in[R_-,R_+],
\qquad R_->0,
\]

let

\[
\boxed{\mathcal K_{r,e}f}
\]

denote the exact entrance-value solution of

\[
\boxed{
(D_r+e/R)\mathcal K_{r,e}f=f,
\qquad
(\mathcal K_{r,e}f)|_{R=R_-}=0.
}
\tag{R3}
\]

The characteristic formula proves

\[
\boxed{
\|\mathcal K_{r,e}f\|_{\mathfrak R^m_{\rm char}}
\le C_{m,I}\|f\|_{\mathfrak R^m_{\rm char}},
}
\tag{R4}
\]

with no Diophantine denominator and no torus derivative loss. The constants depend only on the fixed collar and the frozen smooth radial weights.

The price is the outgoing trace

\[
\boxed{
\operatorname{Tr}_{r,+}(\mathcal K_{r,e}f)
:=(\mathcal K_{r,e}f)|_{R=R_+},
}
\tag{R5}
\]

which is retained as part of the relay output state.

## 3. Pressure: the defect `P` disappears as a solvability condition

Instead of source equation (8.12), which subtracts a bump `rho P` to make the compact radial integral vanish, define directly

\[
\boxed{p_m:=\mathcal K_{r,0}g_r.}
\tag{R6}
\]

Then

\[
\boxed{D_rp_m-g_r=0}
\tag{R7}
\]

identically throughout the collar.

No scalar condition

\[
P=\int\langle g_r\rangle_YdR=0
\]

is required. The information formerly encoded by `P` is now carried by the exit pressure trace

\[
\boxed{p_{+,m}:=p_m(R_+,\cdot).}
\tag{R8}
\]

Thus the source pressure compatibility defect is a boundary artifact of two-sided compactification, not a local PDE obstruction.

## 4. Auxiliary-averaged tangential equations: `J_theta` and `J_z` disappear as radial solvability conditions

After pressure is fixed by (R6), take Haar averages of the tangential residuals and define

\[
\boxed{
H_\theta:=-\mathcal K_{r,2}\langle E_\theta\rangle_Y,
\qquad
H_z:=-\mathcal K_{r,1}\langle E_z\rangle_Y.
}
\tag{R9}
\]

Then exactly

\[
\boxed{
(D_r+2/R)H_\theta=-\langle E_\theta\rangle_Y,
\qquad
(D_r+1/R)H_z=-\langle E_z\rangle_Y.
}
\tag{R10}
\]

In the compact source construction, the corresponding right-hand sides first had to be modified by normalized bump terms involving

\[
\varepsilon\partial_ZJ_\theta,
\qquad
\varepsilon\partial_Z(J_z+c_\rho P),
\]

so that their weighted radial integrals vanished. In the one-sided formulation no such subtraction is needed.

The old scalar quantities `J_theta`, `J_z` are replaced by the two outgoing stress traces

\[
\boxed{
H_{\theta,+}:=H_\theta(R_+,\cdot),
\qquad
H_{z,+}:=H_z(R_+,\cdot).
}
\tag{R11}
\]

Hence there is no hidden global moment condition in the radial inversion itself.

## 5. Zero-Haar-average temporal update and exact divergence-free axial realization

The zero-Haar-average pair

\[
E_\theta^\circ,
\qquad
E_z^\circ
\]

is handled by the derivative-loss-free temporal characteristic inverse already proved in `characteristic_fast_time_mean_inverse.md`:

\[
\boxed{
\Delta v_{\rm des}=-\mathcal J_iE_\theta^\circ,
\qquad
\gamma_d=-\mathcal J_iE_z^\circ.
}
\tag{R12}
\]

Thus

\[
t_*\Delta v_{\rm des}=-E_\theta^\circ,
\qquad
t_*\gamma_d=-E_z^\circ.
\tag{R13}
\]

To realize the desired axial increment without the source cutoff remainder `A_1`, use the one-sided radial vector-potential primitive instead of a compact two-sided primitive. Define `Psi` by

\[
\boxed{
(D_r+1/R)\Psi=\gamma_d,
\qquad
\Psi|_{R=R_-}=0,
}
\tag{R14}
\]

and set

\[
\boxed{
\Delta\beta=-\varepsilon\partial_Z\Psi,
\qquad
\Delta\gamma=(D_r+1/R)\Psi=\gamma_d.
}
\tag{R15}
\]

The same commutation identity used in source Proposition 8.3(ii) gives

\[
\boxed{
(D_r+1/R)\Delta\beta+D_z\Delta\gamma=0,
}
\tag{R16}
\]

so the increment is exactly divergence-free.

Crucially, there is now **no** term

\[
-A_1\gamma_d.
\]

It has been exchanged for the outgoing potential/velocity trace at `R=R_+`.

## 6. What becomes of the two velocity moments

The source imposes

\[
M_\theta=\int R^2\langle v\rangle_YdR=0,
\qquad
M_z=\int R\langle\gamma\rangle_YdR=0
\tag{R17}
\]

because compactly supported corrections must match zero outside the active shell and because these identities simplify the integrated tangential equations.

For a local one-sided radial relay, (R17) is not a solvability condition for (R3), (R6), (R9), or (R14). If these moments are not zero, their evolution is determined by the entrance data and the outgoing radial traces.

Accordingly define the enlarged radial trace state

\[
\boxed{
r:=(p_+,H_{\theta,+},H_{z,+},\Psi_+,M_\theta,M_z).}
\tag{R18}
\]

The local map carries `r_in` to `r_out`; it does not reset these quantities to zero at every collar.

This is the radial analogue of retaining `Z_out` in the temporal/nonzero forward architecture.

## 7. The five-dimensional moment correction is not locally required for radial solvability

Source Lemma 8.7 uses five fixed profiles to do two things simultaneously:

1. preserve the two zero moments (R17);
2. cancel the three compact-support compatibility defects `(P,J_theta,J_z)`.

After the one-sided replacements (R6) and (R9), the second role disappears. After the moments are promoted to trace/state variables, the first role is no longer a local solvability requirement either.

Therefore the **pure local forward PDE problem** does not require the five-dimensional moment correction.

This does not make Lemma 8.7 useless. Its finite-dimensional map may still be valuable later as a **normalization/reset map** at an interface between physical scales, if physical-scale inheritance requires selected outgoing moments to be returned to a canonical class.

That is a global inheritance issue, not a local radial inverse issue.

## 8. Exact local radial cancellation identities

Collecting the preceding definitions, the radial/mean linear correction layer satisfies exactly

\[
\boxed{
D_rp_m=g_r,
}
\tag{R19}
\]

\[
\boxed{
(D_r+2/R)H_\theta=-\langle E_\theta\rangle_Y,
\qquad
(D_r+1/R)H_z=-\langle E_z\rangle_Y,
}
\tag{R20}
\]

\[
\boxed{
t_*\Delta v_{\rm des}=-E_\theta^\circ,
\qquad
t_*\gamma_d=-E_z^\circ,
}
\tag{R21}
\]

and the axial realization obeys

\[
\boxed{
\Delta\gamma=\gamma_d,
\qquad
(D_r+1/R)\Delta\beta+D_z\Delta\gamma=0.
}
\tag{R22}
\]

There is no compactification remainder and no scalar radial moment solvability condition in these identities.

## 9. Boundedness and differentiated nonlinear sources

Every one-sided inverse above is `O(1)` in the corresponding characteristic norm. Therefore smallness is required only for the nonlinear source **after the full O(1) linear mean coupling has been moved into the forward linear operator**.

The non-radial audit already isolates the available positive factors:

\[
\boxed{
\varepsilon^{0.17},
\quad
\varepsilon^{1/2-\kappa_s},
\quad
\varepsilon^{1-2\kappa_s},
\quad
\rho_\ell.
}
\tag{R23}
\]

The `epsilon^(0.9-2kappa_s)` moment factor is no longer needed for local radial solvability if the five-dimensional reset is omitted from the local map; it remains available if one chooses to retain that finite normalization.

Thus the radial forwardization itself introduces **no new smallness loss**.

## 10. Precise remaining local obligation

After this reorganization, the unresolved local theorem is narrower than stated in `radial_characteristic_forward_inverse.md`.

It is no longer necessary to prove that all radial pressure/stress equations can use a one-sided boundary condition simultaneously: equations (R19)--(R22) give that simultaneous formulation explicitly.

The remaining task is to construct the **full coupled linear mean propagator** containing the O(1) base-mean couplings, pressure reconstruction, and signed covariance response, and then prove that the residual nonlinear map has Lipschitz norm

\[
\boxed{
\eta_\ell
\le
C_MS_*^C
\left[
\varepsilon^{0.17}
+\varepsilon^{1/2-\kappa_s}
+\varepsilon^{1-2\kappa_s}
+\rho_\ell
\right]
\longrightarrow0.
}
\tag{R24}
\]

in one fixed temporal-radial characteristic Gevrey space.

## 11. Consequence for the project frontier

The compact radial obstruction has been converted into an enlarged boundary state:

\[
\boxed{
(m_{\rm in},z_{\rm in},r_{\rm in})
\longmapsto
(m_{\rm out},z_{\rm out},r_{\rm out}).
}
\tag{R25}
\]

No hidden `P/J_theta/J_z` compatibility equation remains in the local radial solve.

The next attack should therefore be directed at one object only:

\[
\boxed{
\textbf{bounded full linear mean propagator on the temporal-radial characteristic collar.}
}
\]

If that propagator is obtained with dyadic-uniform constants, the already-audited nonlinear factors are small enough for the final Banach contraction.