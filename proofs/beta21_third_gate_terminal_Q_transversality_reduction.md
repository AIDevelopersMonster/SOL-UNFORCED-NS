# Terminal-`Q` transversality reduction for the third beta-(2,1) active gate

**Status:** PROVED FINITE-DIMENSIONAL RANK REDUCTION. The third-gate full critical audit shows that the naturally-critical unwanted family is the same six-mode beta-zero-root family already controlled in the second gate. The only new designated leading coordinate is

\[
Q=2D.
\]

At leading minimal-leaf action, `Q` receives nonzero feed-forward contributions from both the positive-`C` designated branch and the root branch,

\[
E-C\to Q,
\qquad
X_2+C\to Q,
\]

while every feedback edge from `Q` into the upstream twelve-state block loses at least one additional `C` leaf and is action-subleading. Hence the frozen thirteen-state system is a one-state terminal extension of the already controllable upstream twelve-state pair.

The complete third-gate rank question is therefore equivalent to one explicit scalar PBH/transmission condition. This note proves that reduction and records the exact frozen margins. It does **not** yet prove that the scalar is nonzero for the exact source-normalized controlled base trajectory; that is the unique remaining principal rank obligation before the third `C^1` transfer.

## 1. Upstream controlled block

Let

\[
Y=(P,E,M,X_2,\ldots,X_{10})\in\mathbb C^{12}
\tag{QTR1}
\]

be the leading action-normalized block from the exact unrouted second-gate architecture.

At the shifted third-section geometry `t_3=t_2+5e-4`, all nonzero edge coefficients, full-symbol rate separations, and the finite control projections persist by continuity. Thus there is a frozen pair

\[
\boxed{Y'=A_{12}Y+B_{12}q}
\tag{QTR2}
\]

with

\[
\boxed{(A_{12},B_{12})\text{ controllable}.}
\tag{QTR3}
\]

Here `q` denotes the scalar same-character parent-control source after the usual smooth-profile reduction. Twelve translated profiles produce the finite locally onto upstream response proved in the second-gate PBH theorem.

## 2. The new terminal coordinate

Append

\[
Q=2D.
\]

At leading action the frozen equation has the form

\[
\boxed{
Q'=\lambda_Q Q+c_Q^TY+b_Qq.
}
\tag{QTR4}
\]

The vector `c_Q` contains at least the two nonzero entries associated to

\[
E-C\to Q,
\qquad
X_2+C\to Q.
\tag{QTR5}
\]

At `u_*=4`, `t=t_3`, source-frame evaluation gives

\[
\boxed{
\kappa_{E-C\to Q}\approx-4.4472992211,
}
\tag{QTR6}
\]

\[
\boxed{
\kappa_{X_2+C\to Q}\approx+2.0914308271.
}
\tag{QTR7}
\]

Both are fixed distances from zero.

The full-symbol normalized diagonal rate of `Q` is

\[
\boxed{
\lambda_Q
=\Gamma_2(z_D(t_3))
\approx-0.4680577722.
}
\tag{QTR8}
\]

The diagnostic upstream rates at the same section include

\[
\lambda_P\approx-0.8182308168,
\qquad
\lambda_E\approx-1.8753867041,
\qquad
\lambda_M\approx-0.0281388477,
\]

and the root-side positive-beta rates lie approximately in the interval `0.34...0.95`. Thus

\[
\boxed{
\lambda_Q\notin\operatorname{spec}(A_{12})
}
\tag{QTR9}
\]

for the frozen leading model, with a fixed positive separation.

## 3. Why `Q` is terminal at leading action

The leading promoted `Q` action is

\[
A_Q^{prom}=2A_C+2A_D.
\]

The edge

\[
X_2+C\to Q
\]

uses exactly the minimal leaves of that action class.

By contrast, sending `Q` back to

\[
X_2=Q-C
\]

requires an additional conjugate `C` leaf beyond the minimal leading representation of `X_2`. Since

\[
A_C<0,
\]

this carries a fixed action deficit. The same conclusion holds for any feedback path from `Q` to the upstream root or `P/E` blocks: reversing the `C`-coefficient sign requires extra cancelling leaves.

Therefore all `Q -> Y` couplings are `o(1)` after upstream leading-action normalization. The leading frozen finite matrix is block lower triangular:

\[
\boxed{
A_{13}
=
\begin{pmatrix}
A_{12}&0\\
c_Q^T&\lambda_Q
\end{pmatrix},
\qquad
B_{13}
=
\binom{B_{12}}{b_Q}.
}
\tag{QTR10}
\]

## 4. Exact PBH reduction

Because `(A_12,B_12)` is controllable, every left eigenvector of `A_13` associated to an eigenvalue in `spec(A_12)` has nonzero pairing with `B_13` after restriction to the upstream block.

The only new PBH test occurs at the terminal eigenvalue `lambda_Q`. Since (QTR9) holds, a left eigenvector for `lambda_Q` may be normalized as

\[
\boxed{
w_Q^T
=\left(-c_Q^T(\lambda_QI-A_{12})^{-1},\ 1\right).
}
\tag{QTR11}
\]

Hence

\[
w_Q^TB_{13}
=
\boxed{
\Theta_Q
:=
 b_Q
-c_Q^T(\lambda_QI-A_{12})^{-1}B_{12}.
}
\tag{QTR12}
\]

(Sign conventions change if the state equation is written with the opposite resolvent orientation; only nonvanishing matters.)

Therefore

\[
\boxed{
(A_{13},B_{13})\text{ controllable}
\iff
\Theta_Q\ne0.
}
\tag{QTR13}
\]

This is the complete frozen thirteen-state rank condition.

## 5. Interpretation of the scalar

The scalar `Theta_Q` is the source-normalized transfer from one parent-control impulse to the terminal promoted `Q` mode evaluated at the terminal full-symbol pole `lambda_Q`.

Its terms include:

1. any direct instantaneous `C`-control interaction with a nonzero base `E` or `X_2` trace, contributing to `b_Q`;
2. the chain
   \[
   C_{ctrl}+D\to P\to E\to Q;
   \]
3. the root chain
   \[
   D-C_{ctrl}\to M\to X_2\to Q;
   \]
4. further leading minimal-action feed-forward paths already contained in the twelve-state finite operator.

The two shortest indirect paths are individually nonzero because every mandatory edge has a fixed nonzero source-frame projection.

A diagnostic constant-coefficient evaluation retaining only those two shortest paths gives contributions of opposite sign and very different magnitude (approximately `-3.5` versus `+1.4e2` under one convenient normalization), far from a visible cancellation. This diagnostic is **not** used as a proof because the exact action-normalized base amplitudes and direct `b_Q` term must be inserted consistently.

## 6. Why this is now the only principal rank obligation

The third full critical audit proves:

- no new naturally-critical unwanted family appears;
- the six positive-defect unwanted modes are already contained in the upstream ten-state root block;
- every other naturally-critical mode is separated by a fixed negative action margin on a positive collar;
- `Q` is the only new promoted designated coordinate;
- `Q` is terminal at leading action.

Therefore no new large Vandermonde or lattice enumeration is required. The principal third-gate frontier is exactly

\[
\boxed{\Theta_Q\ne0.}
\tag{QTR14}
\]

Once (QTR14) is source-certified, thirteen translated smooth parent controls give a locally onto frozen response map on

\[
(P,E,Q,M,X_2,\ldots,X_{10}),
\]

and the existing parameter-dependent exact zero-residual argument transfers rank to the physical PDE exactly as in the second gate.

No exact third gate is claimed in this note.
