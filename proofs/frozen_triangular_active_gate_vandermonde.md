# Frozen triangular active-gate Vandermonde theorem

**Status:** PROVED PRINCIPAL FROZEN-COLLAR RANK THEOREM. For the first beta-(2,1) active collision gate, if a localized control packet enters the principal `P` equation as an independently tunable source, then the four exit-response kernels for

\[
(P,E,Q,H)
\]

are linearly independent already in the frozen triangular model. For four distinct control times the exact `4 x 4` principal response determinant is a nonzero scaled Vandermonde determinant.

This closes the abstract kernel-independence question for the natural **direct-`P` control channel** at frozen principal level. It does not yet prove that the exact source packet construction supplies four independently localized direct-`P` controls with the required normalization and `C^1` error bound.

## 1. Frozen shortcut subsystem

Work inside one sufficiently short first collision collar of the active-gate reduction. Freeze the incoming principal amplitudes

\[
C=c\ne0,
\qquad
D=d\ne0
\tag{FV1}
\]

and the principal interaction coefficients

\[
\kappa_2,\kappa_3,\kappa_4\ne0
\tag{FV2}
\]

for the downstream edges

\[
P+D\to E,
\qquad
E-C\to Q,
\qquad
Q-C\to H.
\tag{FV3}
\]

The nonvanishing of these coefficients at the beta-(2,1), `u_*=4` working geometry was established in the polarization/support audits.

Linearize the forbidden-trace response with respect to an additional localized control source `q` injected directly into the growing `P` coordinate. After phase normalization the frozen triangular response system is

\[
\partial_v\,\delta P=q,
\tag{FV4}
\]

\[
\partial_v\,\delta E=a\,\delta P,
\qquad
a:=\kappa_2 d\ne0,
\tag{FV5}
\]

\[
\partial_v\,\delta Q=b\,\delta E,
\qquad
b:=\kappa_3\overline c\ne0,
\tag{FV6}
\]

\[
\partial_v\,\delta H=g\,\delta Q,
\qquad
g:=\kappa_4\overline c\ne0.
\tag{FV7}
\]

All four response coordinates vanish before the control is injected.

The omission of diagonal homogeneous transport terms is only a normalization choice at this stage: they can be removed by multiplying each coordinate by its nonzero frozen propagator. Section 6 below records the corresponding generalization.

## 2. Point control at one time

Let a unit point control be injected at

\[
v=\tau
\]

and let the collar exit be

\[
v=v_+>\tau.
\]

Put

\[
L:=v_+-\tau>0.
\tag{FV8}
\]

Then immediately after the impulse,

\[
\delta P=1.
\]

Successive integration of (FV5)--(FV7) gives at the exit

\[
\boxed{K_P(\tau)=1,}
\tag{FV9}
\]

\[
\boxed{K_E(\tau)=aL,}
\tag{FV10}
\]

\[
\boxed{K_Q(\tau)=\frac{ab}{2}L^2,}
\tag{FV11}
\]

and

\[
\boxed{K_H(\tau)=\frac{abg}{6}L^3.}
\tag{FV12}
\]

Thus the four exit kernels are nonzero scalar multiples of

\[
1,\quad L,\quad L^2,\quad L^3.
\tag{FV13}
\]

They are linearly independent on every nontrivial interval.

## 3. Exact four-control determinant

Choose four distinct injection times

\[
\tau_1,\tau_2,\tau_3,\tau_4<v_+
\]

and put

\[
L_j=v_+-\tau_j.
\tag{FV14}
\]

The principal response matrix is

\[
J_0=
\begin{pmatrix}
1&1&1&1\\
aL_1&aL_2&aL_3&aL_4\\
\frac{ab}{2}L_1^2&\frac{ab}{2}L_2^2&\frac{ab}{2}L_3^2&\frac{ab}{2}L_4^2\\
\frac{abg}{6}L_1^3&\frac{abg}{6}L_2^3&\frac{abg}{6}L_3^3&\frac{abg}{6}L_4^3
\end{pmatrix}.
\tag{FV15}
\]

Factoring the row constants gives

\[
\det J_0
=
\frac{a^3b^2g}{12}
\det
\begin{pmatrix}
1&1&1&1\\
L_1&L_2&L_3&L_4\\
L_1^2&L_2^2&L_3^2&L_4^2\\
L_1^3&L_2^3&L_3^3&L_4^3
\end{pmatrix}.
\tag{FV16}
\]

Hence

\[
\boxed{
\det J_0
=
\frac{a^3b^2g}{12}
\prod_{1\le i<j\le4}(L_j-L_i).
}
\tag{FV17}
\]

Since

\[
a\ne0,
\qquad b\ne0,
\qquad g\ne0
\]

and distinct `tau_j` are equivalent to distinct `L_j`, we obtain

\[
\boxed{
\tau_i\ne\tau_j\ (i\ne j)
\Longrightarrow
\det J_0\ne0.
}
\tag{FV18}
\]

This is a complete principal frozen-collar rank proof; no numerical determinant search is needed.

## 4. Explicit control solve

Let the uncontrolled exit vector be

\[
y^{(0)}=
\begin{pmatrix}
P^{(0)}\\E^{(0)}\\Q^{(0)}\\H^{(0)}
\end{pmatrix}
\]

and prescribe the gated target

\[
y_*=
\begin{pmatrix}
P_*\\0\\0\\0
\end{pmatrix}.
\tag{FV19}
\]

For four point-control amplitudes

\[
p=(p_1,p_2,p_3,p_4)^T,
\]

the frozen linear exit map is

\[
y_{\rm out}=y^{(0)}+J_0p.
\tag{FV20}
\]

By (FV18), the unique exact principal control vector is

\[
\boxed{
p=J_0^{-1}(y_*-y^{(0)}).}
\tag{FV21}
\]

Thus at frozen principal level one may independently prescribe the outgoing `P` coefficient and cancel the three explicit shortcut traces `E,Q,H`.

## 5. Quantitative separated-time margin

Rank nonvanishing is not enough for the eventual packet perturbation argument; one wants a determinant margin. Choose four normalized exit distances

\[
L_j=L_0+j\Delta,
\qquad j=0,1,2,3,
\tag{FV22}
\]

with fixed

\[
L_0>0,
\qquad
\Delta>0
\]

and all four controls inside the collision interval. Then

\[
\prod_{0\le i<j\le3}(L_j-L_i)
=
12\,\Delta^6.
\tag{FV23}
\]

Therefore

\[
\boxed{
|\det J_0|
=|a|^3|b|^2|g|\,\Delta^6.
}
\tag{FV24}
\]

So any fixed principal lower bounds

\[
|a|\ge a_*,
\qquad
|b|\ge b_*,
\qquad
|g|\ge g_*>0
\tag{FV25}
\]

and a fixed normalized spacing `Delta` give an explicit positive determinant margin

\[
\boxed{
|\det J_0|
\ge a_*^3b_*^2g_*\Delta^6>0.
}
\tag{FV26}
\]

At `u_*=4` the audited principal edge coefficients are separated from zero, so the only new quantitative input needed for (FV25) is a lower bound for the normalized incoming amplitudes `|c|,|d|` on the chosen gate background.

## 6. Frozen diagonal transport does not destroy rank

More generally allow constant diagonal transport rates

\[
\partial_v\delta P=\lambda_P\delta P+q,
\]

\[
\partial_v\delta E=\lambda_E\delta E+a\delta P,
\]

\[
\partial_v\delta Q=\lambda_Q\delta Q+b\delta E,
\]

\[
\partial_v\delta H=\lambda_H\delta H+g\delta Q.
\tag{FV27}
\]

Conjugate by the nonvanishing integrating factors

\[
\widetilde P=e^{-\lambda_Pv}\delta P,
\quad
\widetilde E=e^{-\lambda_Ev}\delta E,
\quad
\widetilde Q=e^{-\lambda_Qv}\delta Q,
\quad
\widetilde H=e^{-\lambda_Hv}\delta H.
\tag{FV28}
\]

The off-diagonal coefficients become nonzero exponentials times `a,b,g`. The corresponding point-response kernels are analytic functions of `tau` and converge, as the frozen collar length tends to zero, after row/column normalization, to the polynomial kernels (FV9)--(FV12).

Therefore for four fixed distinct normalized locations the determinant is a continuous perturbation of (FV17). Hence there exists a sufficiently short but nonzero frozen collar for which

\[
\boxed{\det J_{\rm diag}\ne0.}
\tag{FV29}
\]

and the determinant has the same normalized sign/phase as the Vandermonde model.

This establishes robustness with respect to bounded frozen homogeneous transport.

## 7. Slowly varying principal coefficients

Let the exact principal coefficients on a short normalized collar satisfy

\[
|a(v)-a_0|+|b(v)-b_0|+|g(v)-g_0|
+\sum_X|\lambda_X(v)-\lambda_{X,0}|
\le\epsilon_{\rm fr}
\tag{FV30}
\]

with

\[
a_0b_0g_0\ne0.
\]

Standard continuous dependence for triangular linear ODEs implies that the four point-response kernels, and therefore the four-by-four sampling determinant at fixed separated control times, depend continuously on these coefficients. Thus there exists

\[
\epsilon_{\rm fr,*}>0
\]

such that

\[
\boxed{
\epsilon_{\rm fr}<\epsilon_{\rm fr,*}
\Longrightarrow
\det J_{\rm principal}\ne0.
}
\tag{FV31}
\]

This turns the exact frozen Vandermonde identity into an open principal-rank condition for sufficiently slowly varying collision collars.

## 8. Smooth control packets

Replace each point source by a narrow smooth unit-mass bump around `tau_j`. By the same localization limit used in `two_collar_compatibility_rank.md` and `multicollar_finite_critical_transversality.md`, the smooth-packet response matrix converges to the point-response matrix as the subcollar width tends to zero. Hence the nonzero determinant persists for sufficiently narrow smooth controls.

Therefore the rank theorem is compatible simultaneously with

- four separated control centers;
- bounded/slow principal transport;
- smooth localization.

The remaining issue is no longer functional-analytic rank at the frozen level. It is exact **source realization** of the direct-`P` control channel.

## 9. Source-specific realization obligation

To promote this theorem to an exact beta-(2,1) gate, one must construct four independently amplitude-tunable localized packet perturbations whose leading projected effect is the source term `q` in (FV4), with all other direct critical responses either known and included in the response matrix or `C^1`-small after normalization.

Concretely, one must prove:

1. each control is curl-generated/divergence-free in the exact source variables;
2. its leading `P` projection has a fixed nonzero coefficient;
3. the four centers can be placed at fixed separated normalized positions inside the `u_*=4` safe collision collar;
4. direct leakage of a control into `E,Q,H` changes the Vandermonde matrix by a controlled perturbation rather than by an order-one rank-destroying identity;
5. the exact mean/stable-complement solve changes the finite control matrix by `o(1)` in `C^1` at high levels.

If these source-realization estimates hold, the determinant margin (FV26) and a Neumann/implicit-function argument give the exact active exit gate.

## 10. Consequence

The active-gate program has advanced from a purely conditional sampling statement to an explicit principal rank mechanism:

\[
\boxed{
\text{direct }P\text{ injection}
\Longrightarrow
(1,L,L^2,L^3)
\Longrightarrow
\text{Vandermonde full rank}.
}
\tag{FV32}
\]

Thus the first genealogy-breaking gate does **not** suffer an intrinsic finite-dimensional controllability obstruction. The new sharp frontier is narrower:

\[
\boxed{
\textbf{realize the four direct-}P\textbf{ controls by exact source-admissible localized packets.}
}
\tag{FV33}
\]

Until that realization and the full finite critical-block audit are complete, this remains a principal gate theorem rather than an exact Navier--Stokes relay cell, and no autonomous infinite cascade or blowup result is claimed.
