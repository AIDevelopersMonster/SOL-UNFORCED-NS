# Phase-slope renewal obstruction and the limits of lattice relabelling

**Status:** CORRECTED KINEMATIC THEOREM. This file replaces the earlier unweighted slope calculation. The source phase normal is `beta B_s(s e_r+K)`, so under an integer change of phase basis the quantities that transform linearly are the **beta weights and beta-weighted radial coefficients**, not the reduced slope coordinates `s` by themselves.

The corrected calculation shows two things. First, an orientation-reversing beta-preserving lattice shear can change the common reduced offset by an integer multiple of the half-step. Second, a pure basis change is only a relabelling of the Fourier lattice: except for the low-order involution returning `(Phi_P,Phi_C)`, it does not create nonzero designated amplitudes on the new generator characters. Thus it is not by itself a physical state-renewal mechanism.

Primary source normalization: OpenAI, Section 7.1, especially (7.2)--(7.4) and Lemma 7.1, where

\[
n_\Phi=B_s(s(v)e_r+K)+O(S_*^{-1})
\]

for the reference packet, and beta scaling gives `beta B_s(s e_r+K)`.

## 1. Current v0.8 phase triangle

At the first event let

\[
\beta_P=2,\qquad \beta_C=1,
\]

with reduced radial coordinates

\[
x_P=x_M,\qquad x_C=y_M,
\qquad
y_M=x_M+d_M,
\qquad d_M=\frac{x_M}{2M}.
\tag{PS1}
\]

The difference child

\[
\Phi_D=\Phi_P-\Phi_C
\tag{PS2}
\]

has beta `1` and reduced coordinate

\[
c_M=x_M-d_M.
\tag{PS3}
\]

The feedback identity is

\[
\Phi_C+\Phi_D=\Phi_P.
\tag{PS4}
\]

Thus the three low-order characters form the exact triangle

\[
P=C+D.
\tag{PS5}
\]

At a later common pulse offset `theta`, their reference normals have beta-weighted radial coefficients

\[
\boxed{
R_P=2(x_M+\theta),\qquad
R_C=y_M+\theta,\qquad
R_D=c_M+\theta.
}
\tag{PS6}

The factor `B_s` is common at principal order and is omitted from this purely algebraic calculation.

## 2. Correct change-of-basis rule

For a two-generator basis write

\[
b=(\beta_1,\beta_2)^T,
\qquad
r=(\beta_1x_1,\beta_2x_2)^T.
\tag{PS7}
\]

If

\[
\Psi=U\Phi,
\qquad U\in GL(2,\mathbb Z),
\]

then phase linearity gives

\[
\boxed{b'=Ub,\qquad r'=Ur.}
\tag{PS8}
\]

Only after this transformation may the new reduced coordinates be formed as

\[
x_j'=r_j'/b_j'
\tag{PS9}
\]

when `b_j'!=0`.

The earlier rule `x'=Ux` was therefore incorrect whenever the beta weights are not all equal. All conclusions below use (PS8).

## 3. Post-cell basis

The amplitude renewal calculation naturally names the post-cell pair

\[
(\Phi_P,\Phi_D).
\]

Its beta vector is again

\[
b=(2,1)^T,
\]

while at common offset `theta` its beta-weighted radial vector is

\[
\boxed{
r_{\rm out}(\theta)
=\begin{pmatrix}
2(x_M+\theta)\\
c_M+\theta
\end{pmatrix}.}
\tag{PS10}

The v0.8 input family at common offset `theta'` would have

\[
\boxed{
r_{\rm in}(\theta')
=\begin{pmatrix}
2(x_M+\theta')\\
y_M+\theta'
\end{pmatrix}.}
\tag{PS11}

## 4. The beta stabilizer

Let

\[
v=(2,1)^T,
\qquad w=(1,-2)^T,
\qquad w^Tv=0.
\]

The orientation-preserving stabilizer contains

\[
\boxed{
U_n=I+n v w^T
=\begin{pmatrix}
1+2n&-4n\\
n&1-2n
\end{pmatrix},
\qquad n\in\mathbb Z,
}
\tag{PS12}
\]

with

\[
U_nv=v,
\qquad\det U_n=1.
\]

The elementary orientation-reversing involution

\[
J=\begin{pmatrix}1&0\\1&-1\end{pmatrix}
\tag{PS13}
\]

also fixes `v` and satisfies `J^2=I`, `det J=-1`. Therefore

\[
\boxed{
V_n:=U_nJ
=\begin{pmatrix}
1-2n&4n\\
1-n&2n-1
\end{pmatrix}
}
\tag{PS14}
\]

is an orientation-reversing beta-preserving family.

## 5. Exact action on the reduced half-step geometry

Put

\[
X=x_M+\theta,
\qquad C=c_M+\theta=X-d_M.
\]

Applying `U_n` to `(2X,C)^T` and dividing by the unchanged beta entries `(2,1)` gives

\[
\boxed{
U_n:\quad
(X,C)
\mapsto
\left(X+2nd_M,\ C+2nd_M\right).
}
\tag{PS15}
\]

Thus `U_n` preserves the post-cell orientation and shifts the common reduced offset by

\[
2nd_M=\frac{nx_M}{M}.
\]

Applying `V_n` instead gives

\[
\boxed{
V_n:\quad
(X,C)
\mapsto
\left(X-2nd_M,\ X+d_M-2nd_M\right).
}
\tag{PS16}
\]

Since `X+d_M=y_M+theta`, this is exactly

\[
\boxed{
V_n r_{\rm out}(\theta)
=r_{\rm in}\!\left(\theta-\frac{nx_M}{M}\right).
}
\tag{PS17}
\]

Therefore an orientation-reversing stabilizer **can** restore the relative v0.8 slope orientation. Exact reset to the first-event offset `0` would require the arithmetic condition

\[
\boxed{
\frac{M\theta}{x_M}=n\in\mathbb Z.
}
\tag{PS18}
\]

This corrects the previous claim that the entire stabilizer necessarily demanded an out-of-pulse offset.

## 6. The low-order involution does not reset the pulse clock

For `n=0`, `V_0=J` and

\[
J(\Phi_P,\Phi_D)=(\Phi_P,\Phi_P-\Phi_D)=(\Phi_P,\Phi_C).
\tag{PS19}
\]

Thus the original catalyst character is recovered exactly and, importantly, it is physically present: the second feedback event used the surviving catalyst `C`.

However (PS17) with `n=0` gives

\[
\boxed{\theta'=\theta.}
\tag{PS20}
\]

At the second renewal event `theta=theta_M^{ren}>0`. The first-event envelope resonance was imposed at `theta=0`; returning to `(P,C)` at `theta_M^{ren}` does not rewind the source pulse clock. Hence the simple involution closes the **character triangle** but not the temporal/envelope recurrence.

## 7. Why a large lattice shear is not automatically a physical renewal

Suppose (PS18) happens to hold for some nonzero `n`. The new basis generators are

\[
\begin{aligned}
\Psi_1&=(1-2n)\Phi_P+4n\Phi_D,\\
\Psi_2&=(1-n)\Phi_P+(2n-1)\Phi_D.
\end{aligned}
\tag{PS21}
\]

A change of basis says only that every old Fourier character can be reindexed in the new integer lattice. It does **not** say that the physical solution has order-one Fourier amplitudes at `Psi_1` and `Psi_2`.

For `|n|>=1`, these are non-designated high genealogical characters. The branch action-filter theorems place such descendants in the subcritical remainder unless they are explicitly promoted by additional designated interactions. Therefore

\[
\boxed{
\text{lattice relabelling}\neq\text{physical regeneration of generator amplitudes}.}
\tag{PS22}
\]

This is the decisive limitation of the pure `GL(2,Z)` route.

## 8. Correct frontier

The phase problem has two distinct layers:

1. **relative slope geometry:** a beta-preserving orientation-reversing shear can restore it exactly, by (PS17);
2. **physical state renewal:** the required new generator characters must actually carry nonzero designated amplitudes, and the pulse/envelope clock must be reset.

The present two-event cell solves neither issue merely by changing basis. The only low-order basis return `J` keeps the same positive pulse offset; the nontrivial shears capable of changing that offset select high characters that are not designated outputs.

Thus the next correct question is not a finite-period basis cycle in `GL(2,Z)` alone. It is whether the nonlinear phase algebra admits a **clock-resetting designated event** that creates a new order-one phase bank with an earlier source reference offset while retaining action control.