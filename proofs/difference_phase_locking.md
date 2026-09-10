# Difference-harmonic phase locking

**Status:** DERIVED PHASE LEMMA. This is an exact algebraic statement about the phase ansatz; admissibility inside the full source packet class still requires the localized PDE estimates.

## 1. Parent phases

Take two source-type phases using the same local chart, same base shear data and same \(u_*\), but beta-scaled frequency parameters:

\[
\Phi_j
=p_j\theta+p_{z,j}Z/\varepsilon+x_{0,j}R-v(p_jF+p_{z,j}G),
\qquad j=1,2.
\]

The source rounding convention makes

\[
kp_j\in\mathbb Z.
\]

The axial coefficient \(p_{z,j}\) is not subject to the angular periodicity constraint.

## 2. Exact desired difference phase

Define

\[
\boxed{\Phi_c:=\Phi_1-\Phi_2.}
\tag{L1}
\]

Then

\[
\Phi_c
=(p_1-p_2)\theta
+(p_{z,1}-p_{z,2})Z/\varepsilon
+(x_{0,1}-x_{0,2})R
-v((p_1-p_2)F+(p_{z,1}-p_{z,2})G).
\]

Therefore \(\Phi_c\) is again of the same affine phase form, with child parameters equal to the exact differences of the parent parameters.

Moreover,

\[
k(p_1-p_2)=kp_1-kp_2\in\mathbb Z,
\]

so angular periodicity is preserved **exactly**. No additional Diophantine condition is needed at this level.

## 3. Exact transport-defect inheritance

Let

\[
L:=t_*+bD_r+F\partial_\theta+GD_z.
\]

By linearity,

\[
L\Phi_c=L\Phi_1-L\Phi_2.
\]

Thus if the parent phase transport defects satisfy

\[
L\Phi_j=E_j,
\]

then

\[
\boxed{L\Phi_c=E_1-E_2.}
\tag{L2}
\]

Hence the child difference phase has the same error class as the parents.

## 4. Principal beta locking

If the parent phase normals satisfy

\[
n_j=\beta_jB_s(s_j e_r+K)+O(S_*^{-1}),
\]

then

\[
n_c=n_1-n_2
=B_s\big((\beta_1s_1-\beta_2s_2)e_r+(\beta_1-\beta_2)K\big)+O(S_*^{-1}).
\]

With

\[
\boxed{\beta_1-\beta_2=1}
\]

and the translated overlap relation

\[
s_c=\beta_1s_1-\beta_2s_2,
\]

we obtain

\[
\boxed{
n_c=B_s(s_c e_r+K)+O(S_*^{-1}),}
\tag{L3}
\]

which is the unit-beta child normal at principal order.

## 5. Harmonic branch

For real packets, the product of the positive harmonic of parent 1 with the negative harmonic of parent 2 contains

\[
e^{ik\Phi_1}e^{-ik\Phi_2}=e^{ik\Phi_c}.
\]

Thus the desired relay branch is the **difference harmonic**. The other real cross term creates the sum phase \(\Phi_1+\Phi_2\), whose beta is \(\beta_+=17/8\) in the current design.

## 6. Consequence

The earlier concern that separate nearest-integer angular rounding destroys exact parent-to-child phase closure is removed if the child phase is **defined as the exact harmonic difference** of the rounded parent phases rather than independently rounded afterward.

What remains is to show that the resulting child phase parameters satisfy all quantitative source packet admissibility bounds and that the quadratic source has a uniform nonzero projection onto the child growing polarization.
