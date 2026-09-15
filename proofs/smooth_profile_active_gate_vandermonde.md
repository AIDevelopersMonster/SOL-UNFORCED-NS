# Smooth-profile active-gate Vandermonde theorem

**Status:** PROVED EXACT FROZEN TRIANGULAR RANK THEOREM FOR FINITE-WIDTH CONTROLS. The point-control limit in `frozen_triangular_active_gate_vandermonde.md` is unnecessary. If the four direct-`P` controls are translates of one fixed smooth compactly supported source profile with nonzero mass, then the exact frozen exit matrix for `(P,E,Q,H)` is a polynomial moment transform of a Vandermonde matrix and has an explicit nonzero determinant for every four distinct control centers.

This removes the narrow-control/Dirac-limit assumption from the principal controllability theorem. It does **not** by itself prove that the OpenAI packet construction supplies four physically free direct-`P` source profiles: that source-realization question remains separate.

## 1. Frozen triangular gate

On a fixed collision interval let the phase-normalized first shortcut block be

\[
P'=q,
\qquad
E'=aP,
\qquad
Q'=bE,
\qquad
H'=gQ,
\tag{SV1}
\]

with

\[
a,b,g\in\mathbb C\setminus\{0\}.
\tag{SV2}
\]

The coefficients are the frozen principal downstream couplings

\[
P+D\to E,
\qquad
E-C\to Q,
\qquad
Q-C\to H.
\]

For the beta-(2,1), `u_*=4` working geometry their nonvanishing is already certified by the polarization and support audits.

Let the exit be `v=v_+`. All response coordinates vanish before the control support.

## 2. One finite-width translated source

Fix

\[
q\in C_c^\infty(\mathbb R)
\tag{SV3}
\]

with compact support contained in a sufficiently short reference subinterval and define its moments

\[
\boxed{
\mu_k:=\int_{\mathbb R} r^k q(r)\,dr,
\qquad k=0,1,2,3.
}
\tag{SV4}
\]

Assume only

\[
\boxed{\mu_0\ne0.}
\tag{SV5}
\]

For a control center `tau`, set

\[
q_\tau(v):=q(v-\tau)
\tag{SV6}
\]

and suppose its support lies strictly before the exit. Put

\[
L:=v_+-\tau.
\tag{SV7}
\]

No small-width limit is taken.

## 3. Exact exit kernels

Integrating (SV1) gives

\[
P(v_+)
=\int q_\tau(s)\,ds
=\mu_0.
\tag{SV8}
\]

For `E`, Fubini gives

\[
E(v_+)
=a\int (v_+-s)q_\tau(s)\,ds.
\]

Writing `s=tau+r`,

\[
\boxed{
K_E(\tau)
=a(\mu_0L-\mu_1).
}
\tag{SV9}
\]

Iterating once more,

\[
Q(v_+)
=ab\int\frac{(v_+-s)^2}{2}q_\tau(s)\,ds,
\]

hence

\[
\boxed{
K_Q(\tau)
=\frac{ab}{2}
\left(
\mu_0L^2-2\mu_1L+\mu_2
\right).
}
\tag{SV10}
\]

Similarly,

\[
H(v_+)
=abg\int\frac{(v_+-s)^3}{6}q_\tau(s)\,ds,
\]

so

\[
\boxed{
K_H(\tau)
=\frac{abg}{6}
\left(
\mu_0L^3-3\mu_1L^2+3\mu_2L-\mu_3
\right).
}
\tag{SV11}
\]

Together with

\[
\boxed{K_P(\tau)=\mu_0,}
\tag{SV12}
\]

the four response kernels are polynomials in `L` of exact degrees `0,1,2,3` with nonzero leading coefficients.

## 4. Exact determinant for four translated profiles

Choose four distinct centers

\[
\tau_1,\tau_2,\tau_3,\tau_4
\tag{SV13}
\]

whose translated supports lie before `v_+`, and put

\[
L_j=v_+-\tau_j.
\tag{SV14}
\]

Let `J_q` be the `4 x 4` exit-response matrix whose `j`th column is

\[
\bigl(K_P(\tau_j),K_E(\tau_j),K_Q(\tau_j),K_H(\tau_j)\bigr)^T.
\]

The passage from the monomial vector

\[
(1,L,L^2,L^3)^T
\]

to the response vector is lower triangular:

\[
\begin{pmatrix}
K_P\\K_E\\K_Q\\K_H
\end{pmatrix}
=
T_q
\begin{pmatrix}
1\\L\\L^2\\L^3
\end{pmatrix},
\tag{SV15}
\]

with diagonal

\[
\boxed{
\operatorname{diag}T_q
=
\left(
\mu_0,
\ a\mu_0,
\ \frac{ab}{2}\mu_0,
\ \frac{abg}{6}\mu_0
\right).
}
\tag{SV16}
\]

Therefore

\[
\det T_q
=
\boxed{
\frac{a^3b^2g}{12}\mu_0^4.
}
\tag{SV17}
\]

Multiplying by the Vandermonde determinant yields the exact identity

\[
\boxed{
\det J_q
=
\frac{a^3b^2g}{12}\mu_0^4
\prod_{1\le i<j\le4}(L_j-L_i).
}
\tag{SV18}
\]

Hence

\[
\boxed{
\mu_0abg\ne0,
\quad
\tau_i\ne\tau_j
\Longrightarrow
\det J_q\ne0.
}
\tag{SV19}
\]

No assumption on `mu_1,mu_2,mu_3` is required. Those moments only perform lower-triangular row operations and cannot change rank.

## 5. Equal-spacing quantitative margin

Take

\[
L_j=L_0+j\Delta,
\qquad j=0,1,2,3,
\tag{SV20}
\]

with fixed `Delta!=0`. Then

\[
\prod_{0\le i<j\le3}(L_j-L_i)
=12\Delta^6.
\tag{SV21}
\]

Thus

\[
\boxed{
\det J_q
=a^3b^2g\,\mu_0^4\Delta^6,
}
\tag{SV22}
\]

and

\[
\boxed{
|\det J_q|
=|a|^3|b|^2|g|\,|\mu_0|^4|\Delta|^6.
}
\tag{SV23}
\]

This supplies an explicit perturbation budget for source-frame, curl, and slowly varying coefficient errors.

## 6. Different smooth profiles

The common-profile hypothesis is convenient but not essential. Suppose

\[
q_j(v)=q_j^0(v-\tau_j)
\]

and each `q_j^0` is close in `L^1` with three moments to one reference profile `q`. Then every entry of the response matrix is close to the corresponding entry of `J_q`. Since determinant is continuous, (SV23) gives a quantitative neighborhood in which rank remains four.

Consequently the eventual source realization may use packet profiles that differ by the `O(S_*^{-1})` frame/envelope drift, provided the normalized profile differences tend to zero uniformly.

## 7. Bounded diagonal transport and slow coefficients

Add bounded diagonal rates and slowly varying downstream coefficients:

\[
P'=\lambda_P(v)P+q,
\]

\[
E'=\lambda_E(v)E+a(v)P,
\]

\[
Q'=\lambda_Q(v)Q+b(v)E,
\]

\[
H'=\lambda_H(v)H+g(v)Q.
\tag{SV24}
\]

On a fixed short collision collar, normalize by the nonzero scalar propagators. If

\[
(a,b,g,\lambda_X)
\]

are uniformly close to frozen values satisfying `abg!=0`, then standard continuous dependence of Volterra kernels implies

\[
J_{\rm var}=J_q+E,
\qquad
\|E\|\to0
\tag{SV25}
\]

as the normalized coefficient variation tends to zero.

Hence, for any reference configuration with determinant margin (SV23), there is an open coefficient/profile neighborhood in which

\[
\boxed{\det J_{\rm var}\ne0.}
\tag{SV26}
\]

This is the form needed before inserting the exact source packet perturbations.

## 8. Relation to the source packet calculus

The OpenAI wave class used throughout this branch is compatible with smooth compactly supported harmonic source profiles and with finite sums at a fixed wave exponent. Proposition 7.2 supplies the forward pulse inverse for such a prescribed harmonic source, while Lemma 7.7 converts the resulting transverse amplitude into an exactly divergence-free curl-generated velocity with a lower-order curl remainder.

However, in the **unforced** relay problem an arbitrary prescribed harmonic source is not a free external control. A legitimate `q_j` must itself arise from internal packet degrees of freedom (for example a controlled designated quadratic overlap or an admissible homogeneous packet parameter), or from a residual that the construction is already entitled to cancel.

Therefore this theorem proves the response-rank statement once four legitimate direct-`P` source profiles exist; it does not manufacture those profiles by adding force.

## 9. Consequence

The active-gate rank theorem no longer depends on singular controls or a limiting localization argument:

\[
\boxed{
\text{four finite-width translated smooth }P\text{-sources}
\Longrightarrow
\text{exact Vandermonde full rank}.
}
\tag{SV27}

The new sharp source-level question is consequently:

\[
\boxed{
\textbf{Can four such }P\textbf{-source profiles be generated internally by source-admissible packet degrees of freedom, without introducing an unreproduced control bank?}
}
\tag{SV28}

This is strictly narrower than the previous source-realization obligation. The determinant side is closed; the remaining issue is the physical/internal origin and repeatability of the four controls.
