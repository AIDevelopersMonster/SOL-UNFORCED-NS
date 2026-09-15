# Seven-control Vandermonde theorem for the beta-zero mean-root chain

**Status:** PROVED FROZEN PRINCIPAL LINEARIZED RANK THEOREM. Assume a direct scalar source channel into the beta-zero root `M` at the source-matched action scale. Linearizing the complete finite mean-root genealogy

\[
M\to H_1\to H_2\to H_3\to J_4\to K_4\to H_4
\]

about its nonzero reference trajectory gives a lower-triangular seven-state system with nonzero first subdiagonal. Seven translated copies of one fixed smooth root-source profile therefore give an exact ordinary degree-six Vandermonde response determinant.

The source-native realization of the direct `M` source by small same-character `C_new` homogeneous subpackets is treated separately.

## 1. Linearized root-chain state

Use the ordered state

\[
X_1=M,
\quad X_2=H_1,
\quad X_3=H_2,
\quad X_4=H_3,
\quad X_5=J_4,
\quad X_6=K_4,
\quad X_7=H_4.
\tag{RV1}
\]

Freeze one sufficiently short second-gate collision collar and normalize diagonal homogeneous transport by integrating factors. Linearization about the nonzero reference genealogy has the form

\[
\boxed{X'=AX+Bq,}
\tag{RV2}
\]

where

\[
B=be_1,
\qquad b\ne0,
\tag{RV3}
\]

and `A` is strictly lower triangular up to harmless diagonal terms already removed.

The crucial structural property is

\[
\boxed{A_{j+1,j}=c_j\ne0,
\qquad j=1,\ldots,6.}
\tag{RV4}
\]

The coefficients `c_j` are the linearized first-subdiagonal responses of the six mandatory edges. Their principal interaction factors were audited in `beta21_second_gate_mean_root_polarization_audit.md`; the remaining multiplicative base amplitudes are nonzero because the reference genealogy itself is generated through those same nonzero edges.

Entries farther below the first subdiagonal are allowed and do not affect controllability.

## 2. Controllability matrix

Let

\[
\mathcal C_7=[B,AB,A^2B,\ldots,A^6B].
\tag{RV5}
\]

Because `A` is lower triangular and has nonzero first subdiagonal, the `k`th column `A^kB` has its first possible new component in row `k+1`, equal to

\[
\boxed{
bc_1c_2\cdots c_k.}
\tag{RV6}
\]

All additional lower-triangular couplings contribute only to rows below that pivot. Therefore `C_7` is lower triangular in the controllability basis with diagonal

\[
b,
\quad bc_1,
\quad bc_1c_2,
\quad\ldots,
\quad bc_1c_2\cdots c_6.
\tag{RV7}
\]

Hence

\[
\boxed{
\det\mathcal C_7
=b^7c_1^6c_2^5c_3^4c_4^3c_5^2c_6
\ne0.
}
\tag{RV8}
\]

Thus one scalar root-source channel controls the full seven-state frozen linearization.

## 3. Smooth translated source profile

Fix

\[
q\in C_c^\infty(\mathbb R),
\qquad
\mu_k=\int r^kq(r)\,dr,
\quad0\le k\le6,
\tag{RV9}
\]

with

\[
\boxed{\mu_0\ne0.}
\tag{RV10}
\]

For a translated source

\[
q_\tau(v)=q(v-\tau),
\qquad
L=v_+-\tau,
\tag{RV11}
\]

the exact frozen exit response is

\[
K(\tau)
=\int e^{A(L-r)}Bq(r)\,dr.
\tag{RV12}
\]

Since `A^7=0`,

\[
K(\tau)
=\sum_{k=0}^6
\frac{A^kB}{k!}
\int(L-r)^kq(r)\,dr.
\tag{RV13}
\]

The `k`th moment polynomial has exact degree `k` in `L`, with leading coefficient `mu_0`. Thus the response basis differs from

\[
B,AB,\ldots,A^6B
\]

only by an invertible lower-triangular moment transform.

## 4. Seven-control determinant

Choose seven distinct source centers

\[
\tau_1,\ldots,\tau_7,
\]

write

\[
L_j=v_+-\tau_j,
\]

and let `J_7` be the `7 x 7` matrix with columns `K(tau_j)`.

Then

\[
\boxed{
\det J_7
=
\frac{
 b^7c_1^6c_2^5c_3^4c_4^3c_5^2c_6
}{1!2!3!4!5!6!}
\mu_0^7
\prod_{1\le i<j\le7}(L_j-L_i).
}
\tag{RV14}

Consequently

\[
\boxed{
\mu_0bc_1\cdots c_6\ne0,
\quad \tau_i\ne\tau_j
\Longrightarrow
\det J_7\ne0.
}
\tag{RV15}

This is a finite-width smooth-profile theorem; no Dirac-source limit is used.

## 5. Equal spacing

For

\[
L_j=L_0+(j-1)\Delta,
\qquad j=1,\ldots,7,
\tag{RV16}
\]

we have

\[
\prod_{i<j}(L_j-L_i)
=\Delta^{21}\prod_{k=1}^6k!.
\tag{RV17}
\]

The factorials cancel, giving

\[
\boxed{
\det J_7
=b^7c_1^6c_2^5c_3^4c_4^3c_5^2c_6
\,\mu_0^7\Delta^{21}.
}
\tag{RV18}

Hence any fixed nonzero center spacing gives an explicit determinant margin.

## 6. Slowly varying coefficients

Restore the actual slowly varying interaction coefficients and diagonal transport on a sufficiently short fixed normalized collar. The corresponding Volterra kernels depend continuously on these coefficients.

Therefore if the frozen determinant margin is `d_7>0`, there is a positive perturbation threshold `eta_7` such that

\[
\boxed{|\det J_{7,var}|\ge d_7/2>0}
\tag{RV19}
\]

for coefficient/profile perturbations below `eta_7`.

This is the same finite-dimensional stability mechanism used in the first active gate.

## 7. Desired root-chain cancellation

Let

\[
X_{out}
=(M,H_1,H_2,H_3,J_4,K_4,H_4)_{out}.
\tag{RV20}
\]

For seven complex normalized root controls `p in C^7`, the frozen linearized map is

\[
X_{out}=X^{(0)}+J_7p.
\tag{RV21}
\]

Thus there is a unique linearized control vector

\[
\boxed{p^0=-J_7^{-1}X^{(0)}}
\tag{RV22}
\]

that annihilates all seven root-family exit coordinates.

This sufficient formulation deliberately cancels the two intermediate coordinates `J_4,K_4` as well as the four dangerous audited outputs. It is not claimed minimal.

## 8. Coupling to the desired `E` output

The root controls will be realized through small `C_new` packets. Their unavoidable sum interaction with `D` produces an additional beta-two `P` trace at the root action scale

\[
A_M=A_P+2A_D.
\]

Relative to the transported designated `P`,

\[
A_M-A_P=2A_D<0.
\tag{RV23}
\]

Thus the root-control side `P` is exponentially below the designated `P`. Any subsequent contribution of this side trace to the desired `E=P+D` output is likewise below the designated `E` by the same fixed action gap.

Therefore, in action-normalized coordinates, the derivative of the leading `E` output with respect to the seven root controls is `o(1)`. One independent main-collision amplitude parameter may be used to prescribe `E_*` while the seven root controls cancel (RV20).

At frozen principal level the resulting eight-parameter/eight-output Jacobian is block triangular:

\[
\begin{pmatrix}
\partial_\alpha E & 0\\
* & J_7
\end{pmatrix},
\tag{RV24}
\]

with

\[
\partial_\alpha E\ne0,
\qquad
\det J_7\ne0.
\]

Hence the full leading finite-dimensional second-gate control map has nonzero rank once the source realization of the root controls is supplied.

## 9. Remaining obligation

The rank problem has now been reduced to source realization:

\[
\boxed{
\textbf{construct seven same-character }C_{new}\textbf{ homogeneous subpackets, scaled to the generated }C_{new}\textbf{ action, whose interaction with }D\textbf{ yields the direct root sources }q_j.
}
\]

After that realization, the exact finite-parameter `C^1` zero-residual transfer can be repeated in action-normalized coordinates.
