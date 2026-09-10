# Principal growing projection for the desired difference branch

**Status:** PROVED PRINCIPAL ALGEBRA for the reference beta-wave model. Localization/curl remainders are handled separately.

Primary source frame: OpenAI, *Finite Time Blowup for Navier–Stokes*, equations (7.7)–(7.10). The source constant \(c_0\) is **negative**; its sign cancels from the coefficient formula below.

## 1. Reference geometry

Work in the orthogonal frame \((e_r,K,N)\). For signed slope \(s\), use the source growing reference polarization

\[
g(s)=e_r-sK+c_0\sqrt{1+s^2}\,N,
\qquad c_0<0.
\]

Let

\[
k_j=\beta_j(s_je_r+K),
\qquad
k_c=k_1-k_2=s_ce_r+K,
\]

with

\[
\beta_1-\beta_2=1,
\qquad
s_c=\beta_1s_1-\beta_2s_2.
\]

Take \(a_j=g(s_j)\).

## 2. Difference-harmonic vector

Up to the common scalar factor \(i\), the difference-harmonic transport coefficient is

\[
B_-=(a_1\cdot(-k_2))a_2+(a_2\cdot k_1)a_1.
\]

Since

\[
a_1\cdot k_2=\beta_2(s_2-s_1),
\qquad
a_2\cdot k_1=\beta_1(s_1-s_2),
\]

we get

\[
\boxed{B_-=(s_1-s_2)(\beta_1a_1+\beta_2a_2).}
\tag{D1}
\]

Put

\[
M=\beta_1s_1+\beta_2s_2,
\quad
R=\beta_1\sqrt{1+s_1^2}+\beta_2\sqrt{1+s_2^2},
\quad
\beta_+=\beta_1+\beta_2.
\]

Then

\[
B_-=(s_1-s_2)(\beta_+e_r-MK+c_0RN).
\]

## 3. Projection to the child plane

A divergence-free basis for the child plane orthogonal to \(n_c=s_ce_r+K\) is

\[
h_c=e_r-s_cK,\qquad N.
\]

Thus

\[
\Pi_cB_-=(s_1-s_2)
\left[
\frac{\beta_++s_cM}{1+s_c^2}h_c+c_0RN
\right].
\tag{D2}
\]

The source growing/decaying reference vectors are

\[
g_c^+=h_c+c_0\sqrt{1+s_c^2}N,
\qquad
g_c^-=h_c-c_0\sqrt{1+s_c^2}N.
\]

Writing \(\Pi_cB_-=A_+g_c^++A_-g_c^-\) gives

\[
\boxed{
A_+=\frac{s_1-s_2}{2(1+s_c^2)}
\left[\beta_++s_cM+R\sqrt{1+s_c^2}\right].
}
\tag{D3}
\]

The factor \(c_0\) cancels exactly, so the source sign convention does not alter the nondegeneracy conclusion.

## 4. v0.4 quantitative witness

For

\[
\beta_1=25/16,\quad \beta_2=9/16,\quad
s_1=29/32,\quad s_2=y_0\approx1.2260460510,
\]

\[
s_c\approx0.7263647213.
\]

The center value is

\[
A_+\approx-0.77045954,
\]

so a conservative neighborhood bound

\[
\boxed{|A_+|\ge0.38}
\]

is available after fixing a sufficiently small resonance neighborhood. Hence the desired difference harmonic has a robust nonzero growing-child component.

## 5. Scope

This is principal algebra. Exact source-class embedding, curl/localization stability, and zero-force correction closure are separate obligations.
