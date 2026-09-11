# Principal polarization audit for the beta-(2,1) clock-reset microcascade

**Status:** PASSED PRINCIPAL SOURCE-FRAME POLARIZATION AUDIT. After correcting the genealogy in `beta21_clock_reset_microcascade_candidate.md`, every mandatory quadratic edge has a nonzero projection onto the target growing polarization. No mandatory edge is killed by Leray projection or by the source growing/decaying frame decomposition.

This is a principal WKB statement. It does not yet include curl remainders, slow cutoffs, ordered micro-collar separation, or the exact phase-adapted zero-residual solve.

## 1. Source reference frame

Work in the orthogonal frame `(e_r,K,N)` used in `difference_branch_projection.md`. For reduced coordinate `z>0` and source shear parameter `u=u_*`, put

\[
s=uz,
\]

and use the growing reference polarization

\[
g(s)=e_r-sK+c_0\sqrt{1+s^2}\,N,
\qquad c_0<0.
\tag{PA1}
\]

A beta-`b` phase has principal normal

\[
k=b(se_r+K).
\tag{PA2}
\]

For a target normal with reduced source slope `s_t`, the divergence-free target plane is spanned by

\[
h_t=e_r-s_tK,\qquad N.
\tag{PA3}
\]

All calculations below are exact at this principal reference level.

## 2. Generic difference interaction

For positive signed betas `b_1>b_2>0`, let the target be the difference phase, with

\[
b_t=b_1-b_2,
\qquad
b_ts_t=b_1s_1-b_2s_2.
\tag{PA4}
\]

The real quadratic difference branch is

\[
B_-=(s_1-s_2)(b_1g(s_1)+b_2g(s_2)).
\tag{PA5}
\]

Projecting to the target plane and resolving into its growing/decaying basis gives the growing coefficient

\[
\boxed{
A_-^+
=\frac{s_1-s_2}{2(1+s_t^2)}
\left[
 b_1+b_2
+s_t(b_1s_1+b_2s_2)
+igl(b_1\sqrt{1+s_1^2}+b_2\sqrt{1+s_2^2}\bigr)
\sqrt{1+s_t^2}
\right].
}
\tag{PA6}
\]

Every term in the square bracket is positive when the slopes are positive. Hence

\[
\boxed{s_1\ne s_2\Longrightarrow A_-^+\ne0.}
\tag{PA7}
\]

This immediately covers every difference edge in the corrected reset tree.

## 3. Generic sum interaction

For a sum target

\[
b_t=b_1+b_2,
\qquad
b_ts_t=b_1s_1+b_2s_2,
\tag{PA8}
\]

the corresponding principal quadratic vector can be written

\[
B_+=(s_1-s_2)(b_1g(s_1)-b_2g(s_2)).
\tag{PA9}
\]

After Leray projection to the target plane, the growing coordinate is

\[
\boxed{
A_+^+
=\frac{s_1-s_2}{2}
\left[
\frac{b_1-b_2+s_t(b_1s_1-b_2s_2)}{1+s_t^2}
+
\frac{b_1\sqrt{1+s_1^2}-b_2\sqrt{1+s_2^2}}
{\sqrt{1+s_t^2}}
\right].
}
\tag{PA10}
\]

Unlike the difference formula, the bracket in (PA10) can in principle cancel. Therefore the sum edges require an actual audit.

## 4. Correct reset geometry

Use the transverse reduced root from `beta21_clock_reset_microcascade_candidate.md`:

\[
x\approx0.7859855569295219140,
\]

\[
\delta\approx0.07069967306663885738,
\]

\[
s_*\approx0.14119460888766346057,
\qquad
T=2\delta.
\tag{PA11}
\]

Near the late microcascade point `s_*`, the reduced slopes are

\[
\begin{aligned}
z_C&=x+\delta+s_*,\\
z_D&=x-\delta+s_*,\\
z_P&=x+s_*,\\
z_E&=x-\delta/3+s_*,\\
z_Q&=x-\delta+s_*,\\
z_H&=x-3\delta+s_*.
\end{aligned}
\tag{PA12}
\]

At the final reset face,

\[
z_H(T)=x-\delta,
\qquad
z_D(T)=x+\delta,
\qquad
z_{P_{new}}(T)=x.
\tag{PA13}
\]

All these numbers are positive and lie strictly inside the source pulse interval.

## 5. Edge-by-edge audit

### 5.1 `C+D -> P`

This is a sum of two unit-beta modes. Their slopes satisfy

\[
z_C-z_D=2\delta>0.
\]

Substituting `b_1=b_2=1` into (PA10), the bracket reduces to a nonzero odd slope-difference expression. Direct source-normalized evaluation gives a positive growing coefficient. Hence

\[
\boxed{\kappa_{CD\to P}\ne0.}
\tag{PA14}
\]

### 5.2 `P+D -> E`

Here `(b_1,b_2,b_t)=(2,1,3)` and

\[
z_P-z_D=\delta>0.
\]

Formula (PA10) has no cancellation at the candidate geometry; its value is positive. Therefore

\[
\boxed{\kappa_{PD\to E}\ne0.}
\tag{PA15}
\]

### 5.3 `E-C -> Q`

This is a difference edge `(3,1)->2`. Since

\[
z_E-z_C=-\frac43\delta\ne0,
\]

( PA6 )--( PA7 ) imply immediately

\[
\boxed{\kappa_{EC\to Q}\ne0.}
\tag{PA16}
\]

with fixed negative sign for the ordering used here.

### 5.4 `Q-C -> H`

This is the corrected difference edge `(2,1)->1`. Since

\[
z_Q-z_C=-2\delta\ne0,
\]

again (PA6)--(PA7) give

\[
\boxed{\kappa_{QC\to H}\ne0.}
\tag{PA17}
\]

with fixed negative sign.

### 5.5 `H+D -> P_new`

At the reset face both inputs have beta one, with

\[
z_H(T)-z_D(T)=-2\delta\ne0.
\]

This is a sum interaction. Substitution into (PA10) gives a strictly positive coefficient for the chosen ordering, hence

\[
\boxed{\kappa_{HD\to P_{new}}\ne0.}
\tag{PA18}
\]

No final Leray cancellation occurs.

## 6. Diagnostic finite-`u_*` margins

To test whether the nonvanishing is merely infinitesimal, evaluate the exact principal formulas at the moderate source value

\[
u_*=100.
\]

Using the root (PA11), the five late-edge growing coefficients are approximately

\[
\boxed{
\begin{array}{c|r}
\text{edge}&A^+\\ \hline
C+D\to P& 2.1562\\
P+D\to E& 7.8074\\
E-C\to Q& -40.8186\\
Q-C\to H& -53.6018\\
H+D\to P_{new}& 2.5434
\end{array}}
\tag{PA19}
\]

The values are far from zero. Repeating at `u_*=10` still gives approximately

\[
0.2132,\quad0.7799,\quad-4.0778,\quad-5.3401,\quad0.2503,
\tag{PA20}
\]

with the same signs. Thus the candidate is not sitting near a principal polarization zero.

For large fixed `u_*`, the margins increase rather than collapse in these source coordinates. Consequently, once `u_*` is frozen, the source-small `O(S_*^{-1})` frame error and the already-established curl/localization errors cannot erase the sign at sufficiently high dyadic levels.

## 7. First relay edge

The initial edge

\[
P+C^*\to D
\]

is also a difference interaction `(2,1)->1`. Here

\[
z_P-z_C=-\delta\ne0,
\]

so (PA6) already gives nonvanishing. Thus the entire six-edge character path

\[
P+C^*\to D,
\quad
C+D\to P,
\quad
P+D\to E,
\quad
E-C\to Q,
\quad
Q-C\to H,
\quad
H+D\to P_{new}
\tag{PA21}
\]

passes the principal polarization test.

## 8. Consequence and next barrier

A possible fatal obstruction has therefore been removed:

\[
\boxed{
\text{no mandatory edge of the finite reset microcascade is killed by principal polarization.}
}
\tag{PA22}
\]

This upgrades the construction from a purely envelope/character candidate to a **principal-level physical quadratic supercell candidate**.

The next barrier is temporal rather than polarization algebra. The four late intermediate generations in the reduced bookkeeping were idealized at one common offset `s_*`, while a causal quadratic cascade requires ordered micro-collars. The available interval

\[
T-s_*\approx2.05\times10^{-4}
\]

is positive but small. The next task is to unfold the common-offset collision into distinct times

\[
s_1<s_2<s_3<s_4<T,
\]

add those timing variables to the resonance system, and use transversality to determine whether exact action renewal persists. Only after that should the full non-designated action filter be redone.