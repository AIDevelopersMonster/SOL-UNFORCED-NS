# Six-control smooth active-gate Vandermonde theorem

**Status:** PROVED EXACT FROZEN TRIANGULAR RANK THEOREM FOR THE FULL FIRST-GATE CONTROLLED CHAIN. For the sufficient clean first-gate block

\[
(P,E,Q,H,P_{new},R_3),
\]

six translated copies of one fixed smooth compactly supported direct-`P` source profile give an exact `6 x 6` response matrix with determinant equal to a nonzero triangular prefactor times the ordinary degree-five Vandermonde determinant.

This closes the finite-dimensional rank problem for the full sufficient first-gate block at frozen principal level. The remaining tasks are source transfer of the six catalyst-subpacket controls and a quantitative nonzero-width action-margin audit.

## 1. Frozen six-state shortcut chain

On a fixed collision interval let

\[
P'=q,
\tag{S6V1}
\]

\[
E'=aP,
\tag{S6V2}
\]

\[
Q'=bE,
\tag{S6V3}
\]

\[
H'=gQ,
\tag{S6V4}
\]

\[
N'=hH,
\tag{S6V5}
\]

\[
R'=rN,
\tag{S6V6}
\]

where

\[
N=P_{new},
\qquad R=R_3,
\]

and

\[
\boxed{a,b,g,h,r\ne0.}
\tag{S6V7}

The coefficients are the frozen principal growing projections of

\[
P+D\to E,
\quad
E-C\to Q,
\quad
Q-C\to H,
\quad
H+D\to P_{new},
\quad
P_{new}-C\to R_3.
\tag{S6V8}

The first four are already audited in the beta-(2,1) support/polarization calculations. The last difference edge is nonzero whenever the two positive-slope inputs are unequal, by the generic difference-interaction formula.

All six response coordinates vanish before the control support.

## 2. One translated smooth source

Fix

\[
q\in C_c^\infty(\mathbb R)
\tag{S6V9}
\]

with moments

\[
\mu_k:=\int r^kq(r)\,dr,
\qquad 0\le k\le5,
\tag{S6V10}

and assume only

\[
\boxed{\mu_0\ne0.}
\tag{S6V11}

For a translated source

\[
q_\tau(v)=q(v-\tau)
\]

whose support lies before the exit `v_+`, put

\[
L=v_+-\tau.
\tag{S6V12}

## 3. Exact iterated-response formulas

Repeated Duhamel integration gives

\[
\boxed{K_P(\tau)=\mu_0,}
\tag{S6V13}

\[
\boxed{K_E(\tau)=a\int(L-r)q(r)\,dr,}
\tag{S6V14}

\[
\boxed{K_Q(\tau)=ab\int\frac{(L-r)^2}{2!}q(r)\,dr,}
\tag{S6V15}

\[
\boxed{K_H(\tau)=abg\int\frac{(L-r)^3}{3!}q(r)\,dr,}
\tag{S6V16}

\[
\boxed{K_N(\tau)=abgh\int\frac{(L-r)^4}{4!}q(r)\,dr,}
\tag{S6V17}

and

\[
\boxed{K_R(\tau)=abghr\int\frac{(L-r)^5}{5!}q(r)\,dr.}
\tag{S6V18}

Each row is therefore a polynomial in `L` of exact degree equal to its row index minus one. The leading coefficients are

\[
\mu_0,
\quad a\mu_0,
\quad \frac{ab}{2!}\mu_0,
\quad \frac{abg}{3!}\mu_0,
\quad \frac{abgh}{4!}\mu_0,
\quad \frac{abghr}{5!}\mu_0.
\tag{S6V19}

The lower moments `mu_1,...,mu_5` only affect lower-degree terms.

## 4. Triangular moment transform

Let

\[
V(L)=(1,L,L^2,L^3,L^4,L^5)^T.
\]

There is a lower triangular matrix `T_q` such that

\[
\begin{pmatrix}
K_P\\K_E\\K_Q\\K_H\\K_N\\K_R
\end{pmatrix}
=T_qV(L).
\tag{S6V20}

Its diagonal is given by (S6V19). Therefore

\[
\begin{aligned}
\det T_q
&=
\mu_0^6
\left(a\right)
\left(\frac{ab}{2!}\right)
\left(\frac{abg}{3!}\right)
\left(\frac{abgh}{4!}\right)
\left(\frac{abghr}{5!}\right)\\
&=
\boxed{
\frac{a^5b^4g^3h^2r}{2!3!4!5!}\mu_0^6.
}
\end{aligned}
\tag{S6V21}

In particular `T_q` is invertible whenever (S6V7), (S6V11) hold.

## 5. Exact six-control determinant

Choose six distinct control centers

\[
\tau_1,\ldots,\tau_6
\]

and write

\[
L_j=v_+-\tau_j.
\]

Let `J_6` be the `6 x 6` matrix whose `j`th column is the six-state exit response to `q_{tau_j}`. Then

\[
J_6
=T_q
\begin{pmatrix}
1&\cdots&1\\
L_1&\cdots&L_6\\
\vdots&&\vdots\\
L_1^5&\cdots&L_6^5
\end{pmatrix}.
\tag{S6V22}

Hence

\[
\boxed{
\det J_6
=
\frac{a^5b^4g^3h^2r}{2!3!4!5!}\mu_0^6
\prod_{1\le i<j\le6}(L_j-L_i).
}
\tag{S6V23}

Therefore

\[
\boxed{
\mu_0abghr\ne0,
\quad
\tau_i\ne\tau_j
\Longrightarrow
\det J_6\ne0.
}
\tag{S6V24}

This is an exact finite-width theorem; no point-source limit is used.

## 6. Equal-spacing determinant margin

Choose

\[
L_j=L_0+(j-1)\Delta,
\qquad j=1,\ldots,6.
\tag{S6V25}

Then

\[
\prod_{1\le i<j\le6}(L_j-L_i)
=
\Delta^{15}
\prod_{k=1}^{5}k!.
\tag{S6V26}

Since

\[
\prod_{k=1}^{5}k!
=1!2!3!4!5!,
\]

cancelling the denominator in (S6V23) leaves

\[
\boxed{
\det J_6
=a^5b^4g^3h^2r\,\mu_0^6\Delta^{15}.
}
\tag{S6V27}

Thus fixed lower bounds on `|a|,|b|,|g|,|h|,|r|`, a fixed nonzero profile mass, and a fixed normalized center spacing give the explicit determinant margin

\[
\boxed{
|\det J_6|
=|a|^5|b|^4|g|^3|h|^2|r|\,|\mu_0|^6|\Delta|^{15}.
}
\tag{S6V28}

## 7. Slowly varying source coefficients

Allow bounded diagonal homogeneous transport and slowly varying nonzero downstream coefficients. Normalize the diagonal transport by integrating factors. On a sufficiently short fixed normalized collision collar, the six Volterra response kernels depend continuously on the coefficient functions in the uniform topology.

Therefore, for any frozen reference configuration with determinant margin `d_6>0`, there exists `eta_6>0` such that coefficient/profile perturbations smaller than `eta_6` give

\[
\boxed{|\det J_{6,var}|\ge d_6/2>0.}
\tag{S6V29}

The source frame, phase, curl and envelope perturbations are already `O(S_*^{-1})` plus positive powers of `epsilon` at fixed normalized packet geometry. Thus once the six catalyst-subpacket controls are realized in the same audited class, the principal rank is robust at sufficiently high level.

## 8. Exact finite-dimensional solve

Let

\[
y_{out}
=(P,E,Q,H,P_{new},R_3)_{out}
\]

and prescribe

\[
y_*=(P_*,0,0,0,0,0).
\tag{S6V30}

For six complex control amplitudes `p in C^6`, the frozen linearized map has the form

\[
y_{out}=y^{(0)}+J_6p.
\]

By (S6V24),

\[
\boxed{p=J_6^{-1}(y_*-y^{(0)})}
\tag{S6V31}

is the unique frozen principal control vector.

The parameter-dependent zero-residual theorem proved for the four-control bank extends verbatim to any fixed finite number of source-admissible catalyst subpackets: differentiating the Volterra/Banach fixed point in six finite parameters introduces no new negative power of `epsilon`. Hence, once the source realization and small-width action audit are supplied,

\[
D_p\mathcal G_\ell
=J_6+o(1)
\tag{S6V32}

in the exact phase-adapted local problem.

## 9. Consequence

The finite-dimensional obstruction for the complete sufficient first-gate block is closed:

\[
\boxed{
6\ \text{smooth internal }P\text{-controls}
\Longrightarrow
\text{full rank on }(P,E,Q,H,P_{new},R_3).
}
\tag{S6V33}

The sharp remaining quantitative step is no longer rank. It is to choose one nonzero physical gate width for which the exact action audit keeps every uncontrolled center-critical mode uniformly below its natural envelope, with particular attention to the closest mode

\[
(B,m,n)=(2,6,-4)
\]

whose center defect is only about `-0.0176369`.
