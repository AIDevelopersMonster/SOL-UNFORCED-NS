# Generic PBH rank for the immediate third beta-(2,1) active gate

**Status:** PROVED FROZEN LEADING-ACTION THIRTEEN-STATE CONTROLLABILITY THEOREM FOR GENERIC SECOND-GATE OUTPUT `E_*`. The clean way to concatenate the second and third active gates is to start the third gate **immediately at the exact second-gate exit section**, with no free transport interval.

At that section the exact second gate supplies

\[
P=0,
\qquad
M=X_2=\cdots=X_{10}=0,
\qquad
E=E_*\ne0,
\]

while the physical parents `C,D` remain present. Therefore a same-character `C` control has a direct source-matched terminal projection

\[
E_*-C_{ctrl}\to Q=2D
\]

in addition to the already-audited direct `P` and beta-zero-root responses. The resulting thirteen-state PBH scalar is an affine nonconstant function of the freely prescribed second-gate target `E_*`. Hence at most one value of `E_*` is forbidden; choosing any other admissible nonzero target gives full frozen controllability.

The statement is made in phase-normalized complex coordinates, equivalently in the doubled real system compatible with physical conjugate pairing.

## 1. Immediate concatenation section

Use the exact second-section time

\[
\boxed{
t_3^{in}=t_2
=0.218506242359214\ldots.
}
\tag{IP1}
\]

The second-gate theorem gives the exact section conditions

\[
\boxed{
(P,E,M,X_2,\ldots,X_{10})
=(0,E_*,0,\ldots,0),
\qquad E_*\ne0.
}
\tag{IP2}
\]

The old unit-beta parents `C,D` are deliberately retained.

At this same section

\[
A_C=-0.0660362173740943\ldots,
\qquad
A_D=-0.0240786305040794\ldots.
\tag{IP3}
\]

The promoted third output action is

\[
\boxed{
A_Q^{prom}=2A_C+2A_D
=-0.180229695756347\ldots.
}
\tag{IP4}
\]

whereas the natural beta-two action of `Q=2D` is

\[
\mathcal E_{2,4}(z_D(t_2))
=-0.244708549122414\ldots.
\]

Thus

\[
\boxed{
\Delta_Q^{prom}
=0.0644788533660666\ldots>0.
}
\tag{IP5}
\]

and a natural homogeneous `Q` pulse cannot replace the source-matched third-gate mechanism.

## 2. Upstream twelve-state pair

Let

\[
Y=(P,E,M,X_2,\ldots,X_{10})\in\mathbb C^{12}.
\]

The second-gate full-symbol theorem supplies a frozen controllable pair

\[
\boxed{Y'=A_{12}Y+B_{12}q,}
\tag{IP6}
\]

where `q` is the normalized scalar source produced by a same-character smooth `C` perturbation.

Thus

\[
\boxed{(A_{12},B_{12})\text{ is controllable}.}
\tag{IP7}
\]

The leading coefficients of `A_12` depend on the frozen parent geometry and the designated interaction coefficients. The terminal second-state value `E_*` does not alter the upstream leading matrix: inside the upstream twelve-state block, `E` has no leading outgoing edge retained before `Q` is appended.

Likewise `B_12` is determined by the direct parent-control projections

\[
C_{ctrl}+D\to P,
\qquad
D-C_{ctrl}\to M,
\]

and is independent of the chosen numerical value of `E_*` at leading action.

## 3. Append the promoted `Q` coordinate

At leading action the thirteen-state system has terminal form

\[
\boxed{
\begin{aligned}
Y'&=A_{12}Y+B_{12}q,\\
Q'&=\lambda_QQ+c_Q^TY+b_Q(E_*)q.
\end{aligned}
}
\tag{IP8}
\]

The terminal row contains the nonzero state couplings

\[
E-C\to Q,
\qquad
X_2+C\to Q.
\]

At the working geometry

\[
\kappa_{E-C\to Q}\approx-4.444\ldots\ne0,
\qquad
\kappa_{X_2+C\to Q}\approx+2.09\ldots\ne0.
\tag{IP9}
\]

The terminal diagonal rate satisfies

\[
\lambda_Q\notin\operatorname{spec}(A_{12}),
\tag{IP10}
\]

with a fixed frozen separation.

## 4. Direct `E_*`-control interaction

Because `E=E_*` is already nonzero at the entrance section, differentiating the quadratic edge

\[
E-C\to Q
\]

with respect to the same-character `C` control produces a direct terminal source

\[
\boxed{
D_qF_Q^{dir}
=\alpha_QE_*,
\qquad
\alpha_Q\ne0.
}
\tag{IP11}
\]

Here `alpha_Q` is the fixed source-normalized growing projection times the nonzero frozen profile/base normalization. Its nonvanishing follows from the explicit principal coefficient `kappa_{E-C->Q}` and the source-admissible nonzero control profile.

All other direct terminal source terms at the entrance section are independent of `E_*`; in particular `X_2=0` at (IP2), so the direct linearization of `X_2+C_ctrl -> Q` contributes no `E_*`-dependent term to the entrance input vector.

Therefore

\[
\boxed{
b_Q(E_*)=b_{Q,0}+\alpha_QE_*}
\tag{IP12}
\]

with `alpha_Q != 0`.

## 5. PBH scalar is affine and nonconstant

For the terminal extension, the unique new PBH scalar is

\[
\Theta_Q(E_*)
=b_Q(E_*)
-c_Q^T(\lambda_QI-A_{12})^{-1}B_{12}.
\tag{IP13}
\]

By Sections 2 and 4, the resolvent term is independent of `E_*` at leading action, while `b_Q(E_*)` has the nonzero linear coefficient `alpha_Q`. Hence

\[
\boxed{
\Theta_Q(E_*)
=\Theta_{Q,0}+\alpha_QE_*,
\qquad
\alpha_Q\ne0.
}
\tag{IP14}
\]

Thus

\[
\boxed{
\#\{E_*:\Theta_Q(E_*)=0\}\le1.
}
\tag{IP15}
\]

Choose any admissible nonzero second-gate target outside this at-most-one-point exceptional set. Then

\[
\boxed{
\Theta_Q(E_*)\ne0.
}
\tag{IP16}
\]

The terminal-extension PBH lemma and (IP7) give

\[
\boxed{
(A_{13},B_{13})\text{ controllable on }\mathbb C^{13}.
}
\tag{IP17}

In a strictly real formulation, apply the same argument to the doubled real system. The exceptional set becomes a proper real algebraic subset of the two-real-dimensional complex `E_*` plane; in particular admissible generic targets remain available.

## 6. Positive third-collar width

At the entrance section the weakest controlled positive-defect mode is

\[
10D-7C,
\qquad
\Delta\approx+0.00278376364,
\]

and the closest uncontrolled negative mode is

\[
8D-6C,
\qquad
\Delta\approx-0.0170697093.
\]

Hence by continuity there exists a fixed positive width `w_3>0` on which the critical classification and all frozen nonzero margins persist. The exact-envelope diagnostic permits, conservatively,

\[
\boxed{w_3=10^{-4}.}
\tag{IP18}
\]

This is smaller than the previously certified second-gate width and leaves substantial margin in both signs.

## 7. Smooth-profile controllability

For a controllable finite frozen pair `(A_13,B_13)`, the response curve

\[
K(\tau)
=\int e^{A_{13}(v_+-s)}B_{13}q_0(s-\tau)\,ds
\]

spans the full thirteen-state space as `tau` varies on any sufficiently small nontrivial interval, for a fixed smooth profile whose finite spectral transform does not vanish.

Therefore one may choose thirteen distinct centers

\[
\tau_1,\ldots,\tau_{13}
\]

inside the fixed collar (IP18) such that the smooth response matrix satisfies

\[
\boxed{
\det J_{13,0}\ne0.
}
\tag{IP19}
\]

Slow coefficient variation, frame errors and action-subleading feedback perturb this matrix continuously.

## 8. Finite target

A sufficient clean third-gate target is

\[
\boxed{
(P,E,Q,M,X_2,\ldots,X_{10})_{out}
=(0,0,Q_*,0,\ldots,0),
\qquad Q_*\ne0.
}
\tag{IP20}
\]

The entrance value `E_*` is a deliberately chosen generic relay parameter supplied by the exact second gate; the exit value `E=0` is then one of the thirteen controlled coordinates of the third gate.

Thus the frozen principal/full-symbol rank obstruction for the third active gate is closed generically. The remaining step is the action-normalized parameter-dependent exact zero-residual `C^1` transfer, exactly analogous to the twelve-control second-gate theorem.

No full reset cell is claimed here.
