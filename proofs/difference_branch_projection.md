# Principal growing projection for the desired difference branch

**Status:** PROVED PRINCIPAL ALGEBRA for the reference beta-wave model. Localization/curl remainders are handled separately.

Primary source frame: OpenAI, *Finite Time Blowup for Navier–Stokes*, equations (7.2), (7.7)–(7.10). The source constant `c_0` is negative; its sign cancels from the coefficient formula below.

**Source-normalization correction.** The source frame uses the actual phase slope `s(v)` from (7.2), whose magnitude is of order `u_*`. The reduced envelope coordinate is `x=|s|/u_*`. An earlier version inserted the reduced coordinate `x` directly into the polarization formula. The algebraic structure was correct, but the numerical coefficient was not source-normalized. This file uses the actual slopes throughout.

## 1. Reference geometry

Work in the orthogonal frame `(e_r,K,N)`. For signed source slope `s`, use the source growing reference polarization

\[
g(s)=e_r-sK+c_0\sqrt{1+s^2}\,N,
\qquad c_0<0.
\]

For the v0.4 relay choose

\[
\beta_1=\frac{25}{16},\qquad
\beta_2=\frac9{16},\qquad
\beta_1-\beta_2=1,
\]

and reduced pulse coordinates

\[
x_1=\frac{29}{32},\qquad y>0.
\]

For fixed `u=u_*`, the **actual** parent slopes are

\[
\boxed{s_1=ux_1,\qquad s_2=uy.}
\tag{D1}
\]

The reference parent normals are

\[
k_j=\beta_j(s_je_r+K).
\]

Their desired difference normal is

\[
k_c=k_1-k_2=s_ce_r+K,
\]

where

\[
\boxed{s_c=ux_c,\qquad x_c=\beta_1x_1-\beta_2y.}
\tag{D2}
\]

Thus the common factor `u_*` cancels from the reduced phase-locking relation for `x_c`, but it must remain in the source polarization.

## 2. Difference-harmonic vector

Take the two reference growing polarizations

\[
a_j=g(s_j).
\]

Up to the common scalar factor `i`, the difference-harmonic transport coefficient is

\[
B_-=(a_1\cdot(-k_2))a_2+(a_2\cdot k_1)a_1.
\]

Since

\[
a_1\cdot k_2=\beta_2(s_2-s_1),
\qquad
a_2\cdot k_1=\beta_1(s_1-s_2),
\]

we obtain

\[
\boxed{B_-=(s_1-s_2)(\beta_1a_1+\beta_2a_2).}
\tag{D3}
\]

Put

\[
M=\beta_1s_1+\beta_2s_2,
\quad
R=\beta_1\sqrt{1+s_1^2}+\beta_2\sqrt{1+s_2^2},
\quad
\beta_+=\beta_1+\beta_2=\frac{17}{8}.
\]

Then

\[
B_-=(s_1-s_2)(\beta_+e_r-MK+c_0RN).
\]

## 3. Leray projection to the child plane

A divergence-free basis for the child plane orthogonal to `k_c` is

\[
h_c=e_r-s_cK,\qquad N.
\]

Therefore

\[
\boxed{
\Pi_cB_-=(s_1-s_2)
\left[
\frac{\beta_++s_cM}{1+s_c^2}h_c+c_0RN
\right].
}
\tag{D4}
\]

The child growing/decaying reference vectors are

\[
g_c^+=h_c+c_0\sqrt{1+s_c^2}N,
\qquad
g_c^-=h_c-c_0\sqrt{1+s_c^2}N.
\]

Writing `Pi_c B_- = A_+ g_c^+ + A_- g_c^-` gives

\[
\boxed{
A_+=\frac{s_1-s_2}{2(1+s_c^2)}
\left[
\beta_++s_cM+R\sqrt{1+s_c^2}
\right].
}
\tag{D5}
\]

The factor `c_0` cancels exactly.

## 4. Uniform source-normalized lower bound

Use the wider finite-`u_*` resonance bracket

\[
\frac{11}{10}\le y\le\frac75,
\qquad u\ge20.
\]

On this bracket,

\[
y-x_1\ge\frac{31}{160},
\]

\[
\frac{1609}{2560}\le x_c\le\frac{2041}{2560},
\]

and

\[
m:=\beta_1x_1+\beta_2y\ge\frac{5209}{2560}.
\]

Since `s_c=ux_c` and `M=um`, the positive bracket in (D5) is larger than `s_c M`. Consequently

\[
|A_+|
\ge
\frac{u(y-x_1)}{2}
\frac{u^2x_cm}{1+u^2x_c^2}.
\tag{D6}
\]

Furthermore,

\[
\frac{u^2x_cm}{1+u^2x_c^2}
=
\frac{m}{x_c}
\frac{u^2x_c^2}{1+u^2x_c^2}.
\]

The first factor is bounded below using `m>=5209/2560` and `x_c<=2041/2560`; the second using `u>=20` and `x_c>=1609/2560`. Exact rational arithmetic gives

\[
\frac{m}{x_c}
\frac{u^2x_c^2}{1+u^2x_c^2}
>\frac52.
\tag{D7}
\]

Hence

\[
\boxed{|A_+|>\frac{31}{128}u.}
\tag{D8}
\]

In particular, for every `u>=20`,

\[
\boxed{|A_+|>\frac{155}{32}>4.84.}
\tag{D9}
\]

At `u=20` and the exact finite-`u` resonance root `y_20≈1.2273024423`, direct evaluation gives `A_+≈-18.5`. Thus the desired difference harmonic is very far from a polarization cancellation.

## 5. Scope

This proves principal polarization nondegeneracy using the **actual source slope**. It still does not include curl-generated remainders, slow cutoffs, transport defect, or exact zero-force correction closure. Those perturbations are treated separately in `localized_projection_stability.md`.
