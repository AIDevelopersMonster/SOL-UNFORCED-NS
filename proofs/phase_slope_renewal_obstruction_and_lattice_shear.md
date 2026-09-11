# Phase-slope renewal obstruction and exact lattice-shear mechanism

**Status:** PROVED KINEMATIC OBSTRUCTION + EXACT LATTICE-SHEAR CANDIDATE. The current two-event amplitude-renewal cell regenerates the beta labels and a nonzero amplitude state, but by itself it does not reset the physical phase-slope coordinates to the next source reference geometry. However, the two-generator phase lattice admits exact unimodular shears that preserve the generated character lattice and can change the chosen generator pair without altering the physical field. This converts the phase-renewal problem into a finite integer-basis matching problem.

This note does not yet prove that one fixed shear maps the post-cell slopes exactly to the next v0.8 reference slopes with the required sign/growing orientation. That arithmetic matching is the next sharp task.

## 1. What the two-event cell actually renews

At the first v0.8 event the two incoming generator phases have beta labels

\[
\beta_P=2,
\qquad
\beta_C=1,
\tag{PS1}
\]

and reduced radial coordinates

\[
x_P=x_M,
\qquad
x_C=y_M.
\tag{PS2}
\]

The designated difference child has phase

\[
\Phi_D=\Phi_P-\Phi_C
\tag{PS3}
\]

and beta label `1`, with radial coordinate

\[
x_D=c_M=2x_M-y_M.
\tag{PS4}
\]

The second designated event uses

\[
\Phi_C+\Phi_D=\Phi_P,
\tag{PS5}
\]

so the regenerated beta-two output has **exactly the old parent character** `Phi_P`.

Therefore the current cell renews the beta pair `(2,1)` at the level of character labels, but after the cell the natural surviving unit-beta generator is `Phi_D`, not the original catalyst `Phi_C`.

Thus the post-cell generator pair is naturally

\[
\boxed{(\Phi_P,\Phi_D)}
\tag{PS6}
\]

rather than `(Phi_P,Phi_C)`.

## 2. Exact integer change of basis

Since

\[
\Phi_D=\Phi_P-\Phi_C,
\]

the old and new generator columns are related by

\[
\begin{pmatrix}
\Phi_P\\
\Phi_D
\end{pmatrix}
=
\begin{pmatrix}
1&0\\
1&-1
\end{pmatrix}
\begin{pmatrix}
\Phi_P\\
\Phi_C
\end{pmatrix}.
\tag{PS7}
\]

The matrix

\[
U_0=
\begin{pmatrix}
1&0\\
1&-1
\end{pmatrix}
\]

has determinant `-1`. Hence

\[
\boxed{U_0\in GL(2,\mathbb Z).}
\tag{PS8}
\]

This is not an approximation: the complete two-generator character lattice is unchanged. Every harmonic indexed by `k in Z^2` in one basis is the same physical character as one indexed by `U_0^{-T}k` in the other basis.

Consequently weighted lattice spaces using any norm equivalent under one fixed integer matrix are preserved up to a fixed constant depending only on `U_0` and the analytic weight.

## 3. General unimodular shear freedom

More generally, after one cell we may choose any new integer generator basis

\[
\boxed{
\begin{pmatrix}
\Psi_1\\
\Psi_2
\end{pmatrix}
=U
\begin{pmatrix}
\Phi_P\\
\Phi_D
\end{pmatrix},
\qquad
U\in GL(2,\mathbb Z).
}
\tag{PS9}
\]

The physical Fourier algebra is unchanged. In particular, the elementary shears

\[
S_n=
\begin{pmatrix}
1&n\\
0&1
\end{pmatrix},
\qquad
\widetilde S_n=
\begin{pmatrix}
1&0\\
n&1
\end{pmatrix}
\tag{PS10}
\]

are exact relabellings.

If the generator beta vector is

\[
b=(2,1)^T,
\]

then under `U` the beta vector becomes

\[
\boxed{b'=Ub.}
\tag{PS11}
\]

To preserve the desired ordered beta pair `(2,1)` exactly, one must restrict to the stabilizer

\[
\boxed{
\mathrm{Stab}_{GL(2,\mathbb Z)}(2,1)
:=\{U\in GL(2,\mathbb Z):U(2,1)^T=(2,1)^T\}.
}
\tag{PS12}
\]

This stabilizer is infinite.

## 4. Explicit stabilizer family

Let

\[
v=(2,1)^T.
\]

Choose the integer covector

\[
w=(1,-2)^T,
\qquad w^Tv=0.
\tag{PS13}
\]

For every integer `n`, define

\[
\boxed{
U_n=I+n v w^T
=
\begin{pmatrix}
1+2n&-4n\\
n&1-2n
\end{pmatrix}.
}
\tag{PS14}
\]

Since `w^Tv=0`,

\[
U_nv=v.
\tag{PS15}
\]

Also by the rank-one determinant formula,

\[
\det U_n=1+n w^Tv=1.
\tag{PS16}
\]

Hence

\[
\boxed{
U_n\in SL(2,\mathbb Z),
\qquad
U_n(2,1)^T=(2,1)^T
}
\tag{PS17}
\]

for every `n in Z`.

Thus there is an exact infinite one-parameter family of lattice shears that preserves the beta labels of the two generators.

## 5. Action on phase slopes

Let the reduced radial slope vector of a generator basis be

\[
r=(r_1,r_2)^T.
\tag{PS18}
\]

Because phases transform linearly, the slope vector transforms by the same matrix:

\[
\boxed{r'=Ur.}
\tag{PS19}
\]

For the stabilizer shear (PS14),

\[
\begin{aligned}
r_1'&=(1+2n)r_1-4nr_2,\\
r_2'&=nr_1+(1-2n)r_2.
\end{aligned}
\tag{PS20}
\]

Therefore the ratio of reduced slopes can be changed discretely while preserving the beta vector `(2,1)` exactly.

This is the crucial kinematic degree of freedom absent from the amplitude-only recurrence.

## 6. Post-cell slope vector

Immediately after the two-event cell, the natural `(beta2,beta1)` basis `(Phi_P,Phi_D)` has reduced radial coordinates

\[
\boxed{
r_{\rm out}(\theta)
=
\begin{pmatrix}
x_M+\theta\\c_M+\theta\end{pmatrix}
}
\tag{PS21}
\]

at a common translated pulse offset `theta`.

The next v0.8 input geometry would require, up to a common offset `theta'`,

\[
\boxed{
r_{\rm target}(\theta')
=
\begin{pmatrix}
x_M+\theta'\\y_M+\theta'\end{pmatrix}.
}
\tag{PS22}
\]

The present cell alone cannot achieve this because

\[
c_M\ne y_M.
\tag{PS23}
\]

This is the exact phase-slope renewal obstruction.

## 7. Finite arithmetic matching problem

Using the stabilizer shear `U_n`, exact generator-basis renewal would require numbers `n in Z` and offsets `theta,theta'` such that

\[
\boxed{
U_n
\begin{pmatrix}
x_M+\theta\\c_M+\theta\end{pmatrix}
=
\begin{pmatrix}
x_M+\theta'\\y_M+\theta'\end{pmatrix}.
}
\tag{PS24}
\]

Subtracting the two components eliminates `theta'`. Since

\[
y_M-x_M=\frac{x_M}{2M},
\qquad
x_M-c_M=\frac{x_M}{2M},
\tag{PS25}
\]

this becomes one explicit scalar Diophantine-affine equation for `n` and `theta`.

A direct simplification gives

\[
\boxed{
(r_1'-r_2')
=(1+n)r_1-(1+2n)r_2.
}
\tag{PS26}
\]

For `r_1=x_M+theta`, `r_2=c_M+theta`, the target condition is

\[
r_1'-r_2'=x_M-y_M=-\frac{x_M}{2M}.
\tag{PS27}
\]

Therefore

\[
\boxed{
(1+n)(x_M+\theta)
-(1+2n)(c_M+\theta)
=-\frac{x_M}{2M}.
}
\tag{PS28}
\]

For `n!=0`, solving for the required common offset gives

\[
\boxed{
\theta_n
=
\frac{(1+n)x_M-(1+2n)c_M+x_M/(2M)}{n}.
}
\tag{PS29}
\]

Using

\[
c_M=x_M\left(1-\frac1{2M}\right),
\]

one obtains the exact simplification

\[
\boxed{
\theta_n
=x_M\left(-1+\frac1M+\frac1{nM}\right).
}
\tag{PS30}
\]

For fixed nonzero integer `n` and large `M`,

\[
\theta_n\to-x_M,
\tag{PS31}
\]

which lies far outside the admissible translated pulse interval around the v0.8 event.

Thus **no fixed stabilizer shear `U_n` with bounded nonzero `n` renews the slopes inside the existing pulse rectangle for large `M`.**

If `|n|` is allowed to grow with `M`, the term `1/(nM)` is negligible and the same conclusion persists:

\[
\theta_n=-x_M+O(M^{-1}).
\tag{PS32}
\]

Hence the entire explicit stabilizer family (PS14) fails to produce an in-pulse exact slope reset.

## 8. Consequence

The lattice-shear freedom is real, but the simplest beta-preserving stabilizer does **not** close the current v0.8 phase-slope recurrence.

Therefore the global frontier sharpens to one of the following three possibilities:

1. enlarge the local renewal cell by one additional designated event that regenerates the original catalyst slope `y_M`;
2. allow the beta pair itself to change by a controlled `GL(2,Z)` basis cycle and return to `(2,1)` only after several cells;
3. redesign the v0.8 geometry so that the post-child slope pair is related to the input pair by an admissible unimodular automorphism.

The next attack should test option 2 first because it preserves the exact character lattice and may replace impossible one-cell slope recurrence by a finite-period lattice-basis cycle.