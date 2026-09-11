# v0.8 designated difference projection is uniformly nonzero

**Status:** PROVED PRINCIPAL POLARIZATION LEMMA FOR THE CURRENT v0.8 DESIGN. This replaces the v0.4 numerical projection witness wherever the current branch uses `beta_1=2`, `beta_2=1`, `u_*=M^2`.

The existing file `difference_branch_projection.md` proves the generic algebraic formula but its numerical lower bound is for the obsolete v0.4 pair `(25/16,9/16)`. The present note specializes the same exact formula to the actual v0.8 half-step family.

## 1. Current v0.8 geometry

Freeze a sufficiently large integer design parameter `M` and put

\[
u:=u_*=M^2,
\qquad
\beta_1=2,
\qquad
\beta_2=1.
\tag{V8P1}
\]

Let `x=x_M` be the exact resonance root of `integral_beta_v08_large_u_halfstep_family.md`, and set

\[
y=\left(1+\frac1{2M}\right)x,
\qquad
x_c=2x-y=\left(1-\frac1{2M}\right)x.
\tag{V8P2}
\]

The actual source slopes are

\[
s_1=ux,
\qquad
s_2=uy,
\qquad
s_c=u x_c.
\tag{V8P3}
\]

For all sufficiently large `M`, the half-step theorem gives `x_M -> 2^{-2/3}`. Fix once and for all `M_0` so large that

\[
\boxed{\frac12\le x\le\frac34}
\tag{V8P4}
\]

for every `M>=M_0`. Enlarging `M_0` if necessary, assume also `M>=2`, hence

\[
\frac34x\le x_c<x,
\qquad
x<y\le\frac54x.
\tag{V8P5}
\]

## 2. Generic exact projection formula

The algebra in `difference_branch_projection.md` applies to arbitrary positive `beta_1,beta_2` with difference child. In the source growing frame the coefficient of the child growing polarization is

\[
A_+
=\frac{s_1-s_2}{2(1+s_c^2)}
\left[
\beta_1+\beta_2+s_c\mathcal M+\mathcal R\sqrt{1+s_c^2}
\right],
\tag{V8P6}
\]

where

\[
\mathcal M=\beta_1s_1+\beta_2s_2=2s_1+s_2,
\tag{V8P7}
\]

\[
\mathcal R=2\sqrt{1+s_1^2}+\sqrt{1+s_2^2}>0.
\tag{V8P8}
\]

Every term in the square bracket is positive. Therefore there can be no cancellation inside the bracket. Since `y>x`, the prefactor `s_1-s_2` is strictly negative. Thus already

\[
\boxed{A_+<0}
\tag{V8P9}
\]

for every admissible finite `M`.

We now obtain a quantitative lower bound.

## 3. Uniform lower bound

Discard the positive terms `3` and `R sqrt(1+s_c^2)` in (V8P6). Then

\[
|A_+|
\ge
\frac{s_2-s_1}{2(1+s_c^2)}\,s_c\mathcal M.
\tag{V8P10}
\]

By the half-step relation,

\[
s_2-s_1
=u(y-x)
=\frac{ux}{2M}
=\frac{Mx}{2}.
\tag{V8P11}
\]

Also

\[
\mathcal M=u(2x+y)\ge3ux,
\qquad
s_c=ux_c.
\tag{V8P12}
\]

Using `ux_c>=M^2(3/8)>=3/2` for `M>=2`,

\[
\frac{s_c^2}{1+s_c^2}
\ge\frac12.
\tag{V8P13}
\]

Hence

\[
\frac{s_c\mathcal M}{1+s_c^2}
=
\frac{\mathcal M}{s_c}\frac{s_c^2}{1+s_c^2}
\ge
\frac12\frac{3x}{x_c}
\ge\frac32.
\tag{V8P14}
\]

Substitute (V8P11) and (V8P14) into (V8P10):

\[
|A_+|
\ge
\frac{Mx}{4}\cdot\frac32
=\frac{3Mx}{8}.
\tag{V8P15}
\]

By (V8P4),

\[
\boxed{
|A_+|\ge\frac{3}{16}M.
}
\tag{V8P16}
\]

In particular, for every frozen sufficiently large design `M`, the principal designated growing projection is separated from zero by a constant depending only on the frozen design, and in fact the margin grows linearly with `M`.

A sharper asymptotic follows directly from (V8P6): since `x,y,x_c -> 2^{-2/3}` and `u=M^2`,

\[
A_+=-\Theta(M).
\tag{V8P17}
\]

No source-small localization/curl correction can erase this margin at sufficiently high relay level because those corrections are `o(1)` relative to the frozen principal coefficient, as in `source_localized_action_preservation.md`.

## 4. Consequence

The current v0.8 branch no longer needs to inherit the **v0.4** numerical constant from `localized_projection_stability.md`. The actual current design has its own stronger principal estimate:

\[
\boxed{
\beta_1=2,\ \beta_2=1,\ u_*=M^2
\quad\Longrightarrow\quad
|A_+|\ge\frac{3M}{16}.
}
\tag{V8P18}
\]

This closes one internal consistency gap in the branch.

## 5. Scope

This lemma proves only nonvanishing of the designated difference-child polarization for the current v0.8 design. It does not prove autonomous regeneration of the **complete two-input relay state** at the next scale. That separate issue is isolated in `v08_state_renewal_obstruction.md`.