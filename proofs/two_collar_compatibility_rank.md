# Two-collar compatibility rank for the first unstable feedback mode

**Status:** PROVED ABSTRACT ODE CONTROLLABILITY LEMMA / DERIVED PRINCIPAL RELAY APPLICATION. The rank theorem below is rigorous for the scalar child/feedback system under its stated sign hypotheses. The v0.4 principal packet algebra satisfies the required nonvanishing signs. Realizing the two controls by exact localized curl-generated packets and closing the remaining correction system is still open.

## 1. Why one complex amplitude is generically insufficient

Let `p in C` be the only adjustable amplitude of a single relay collar. Suppose the outgoing child coefficient and one complex compact-support compatibility moment are

\[
C(p)=c\,p,
\qquad
M(p)=\mu\,p,
\]

with `c != 0` and `mu != 0`.

Then

\[
M(p)=0\implies p=0\implies C(p)=0.
\]

Hence one complex amplitude cannot simultaneously produce a prescribed nonzero child and annihilate a nontrivial complex compatibility moment.

This is a rank-one obstruction, not a smallness issue. For the first unstable feedback mode `(1,-2)`, the compatibility functional is nontrivial by `feedback_mode_instability_and_compact_inverse_obstruction.md` and the principal coupling computation in Section 5 below.

## 2. Two separated relay collars

Let

\[
I=[v_-,v_+]
\]

and consider the scalar child equation

\[
c'(v)=a_c(v)c(v)+p_1q_1(v)+p_2q_2(v),
\qquad c(v_-)=0,
\tag{T1}
\]

where `p_1,p_2 in C` are independent control amplitudes and `q_j` are smooth sources supported in two disjoint narrow collars centered at

\[
v_-<\tau_1<\tau_2<v_+.
\]

Write

\[
c(v)=p_1c_1(v)+p_2c_2(v)
\]

for the two unit-control responses.

The outgoing desired-child functional is

\[
\boxed{
C(p_1,p_2)=C_1p_1+C_2p_2,
\qquad C_j:=c_j(v_+).
}
\tag{T2}

Let the first dangerous feedback coordinate satisfy

\[
z'(v)=a_m(v)z(v)+b(v)c(v),
\tag{T3}
\]

where `m=(1,-2)`. Requiring the correction to vanish at both ends gives the exact moment condition

\[
M(p_1,p_2)=0,
\]

with

\[
\boxed{
M(p_1,p_2)=\mu_1p_1+\mu_2p_2,
}
\tag{T4}
\]

\[
\mu_j
:=
\int_{v_-}^{v_+}
 e^{-A_m(v)}b(v)c_j(v)\,dv,
\qquad
A_m(v):=\int_{v_-}^{v}a_m(s)\,ds.
\tag{T5}
\]

Thus the control Jacobian is the complex `2 x 2` matrix

\[
\boxed{
J=
\begin{pmatrix}
C_1&C_2\\
\mu_1&\mu_2
\end{pmatrix}.
}
\tag{T6}

Because the coefficients can be phase-normalized to be real at principal level, the same matrix acts on real and imaginary parts. Therefore `det J != 0` supplies the four real degrees of freedom required to prescribe one complex child amplitude and kill one complex compatibility moment.

## 3. Point-collar limit

The mechanism behind the rank is clearest for point sources. Replace `q_j` by unit impulses at `tau_j`. Let

\[
A_c(v)=\int_{v_-}^{v}a_c(s)\,ds.
\]

The unit response generated at time `tau` is

\[
c_\tau(v)
=
\mathbf 1_{v\ge\tau}
\exp\big(A_c(v)-A_c(\tau)\big).
\]

Hence

\[
C(\tau)
=
\exp\big(A_c(v_+)-A_c(\tau)\big)>0,
\tag{T7}
\]

and

\[
\mu(\tau)
=
\int_{\tau}^{v_+}
 e^{-A_m(v)}b(v)
 e^{A_c(v)-A_c(\tau)}\,dv.
\tag{T8}
\]

Divide by the child transfer coefficient:

\[
\boxed{
\rho(\tau)
:=\frac{\mu(\tau)}{C(\tau)}
=
\int_{\tau}^{v_+}
 e^{-A_m(v)}b(v)
 e^{A_c(v)-A_c(v_+)}\,dv.
}
\tag{T9}

Differentiating with respect to the injection time gives the exact identity

\[
\boxed{
\rho'(\tau)
=-e^{-A_m(\tau)}b(\tau)
 e^{A_c(\tau)-A_c(v_+)}.
}
\tag{T10}

All exponential factors are strictly positive. Therefore, on every interval on which `b` has a fixed nonzero sign,

\[
\boxed{\rho'(\tau)\neq0.}
\tag{T11}

Thus `rho` is strictly monotone.

For two distinct injection times `tau_1 != tau_2`, the point-source determinant is

\[
\begin{aligned}
\det J_0
&=C(\tau_1)\mu(\tau_2)-C(\tau_2)\mu(\tau_1)\\
&=C(\tau_1)C(\tau_2)
\big(\rho(\tau_2)-\rho(\tau_1)\big).
\end{aligned}
\tag{T12}

Since both `C(tau_j)` are positive and `rho` is strictly monotone,

\[
\boxed{\det J_0\neq0.}
\tag{T13}

This proves exact rank two in the point-collar model.

## 4. Smooth narrow collars

Let `psi in C_c^infty((-1,1))` satisfy

\[
\int\psi=1,
\]

and put

\[
q_j^{(\delta)}(v)
=\delta^{-1}\psi\!\left(\frac{v-\tau_j}{\delta}\right).
\]

For fixed distinct `tau_1,tau_2` and smooth coefficients `a_c,a_m,b`, the corresponding quantities

\[
C_j^{(\delta)},\qquad
\mu_j^{(\delta)}
\]

converge to the point-source values as `delta -> 0`. Hence

\[
\det J_\delta\longrightarrow\det J_0\neq0.
\]

Therefore there exists `delta_0>0` such that

\[
\boxed{
0<\delta<\delta_0
\quad\Longrightarrow\quad
\det J_\delta\neq0.
}
\tag{T14}

So the rank mechanism survives smooth localization.

## 5. The v0.4 feedback coupling has fixed nonzero sign

The abstract theorem requires the coupling `b(v)` in (T3) to be nonzero with fixed phase/sign on the two-collar interval. This is satisfied by the principal v0.4 algebra.

Let the desired child have normal

\[
k_c=s_ce_r+K,
\]

and the catalyst have

\[
k_2=\beta_2(s_2e_r+K),
\qquad
\beta_2=\frac9{16}.
\]

The dangerous feedback harmonic is

\[
k_m=k_c-k_2
=(1-\beta_2)(s_me_r+K),
\]

where

\[
1-\beta_2=\frac7{16},
\qquad
s_m=\frac{s_c-\beta_2s_2}{1-\beta_2}.
\]

Using the source reference growing polarization

\[
g(s)=e_r-sK+c_0\sqrt{1+s^2}N,
\]

the interaction of the positive child harmonic with the negative catalyst harmonic is

\[
B_m
=(s_c-s_2)\big(g(s_c)+\beta_2g(s_2)\big).
\tag{T15}

Projecting onto the growing coordinate of `k_m` gives

\[
\boxed{
A_m^+
=\frac{s_c-s_2}{2(1+s_m^2)}
\left[
1+\beta_2
+s_m(s_c+\beta_2s_2)
+R_m\sqrt{1+s_m^2}
\right],
}
\tag{T16}

with

\[
R_m=\sqrt{1+s_c^2}+\beta_2\sqrt{1+s_2^2}>0.
\]

On the finite-`u_*` relay bracket,

\[
s_c=ux_c,
\qquad s_2=uy,
\qquad x_c<1<y,
\]

so

\[
s_c-s_2<0.
\]

The square bracket in (T16) is strictly positive for the positive-slope v0.4 geometry. Hence

\[
\boxed{A_m^+<0}
\tag{T17}
\]

throughout a sufficiently small neighborhood of the relay configuration. The coupling is therefore nonzero and has fixed phase/sign. This is precisely the hypothesis needed in (T10)–(T13).

Likewise, the parent-parent difference interaction producing the child has a fixed nonzero growing projection by `difference_branch_projection.md`. Thus the child source coefficient in each narrow collar can be phase-normalized consistently.

## 6. Minimality and explicit solve

For one unstable complex compatibility moment and a prescribed nonzero complex child output, two independent complex collar amplitudes are generically minimal.

When `det J != 0`, the unique controls solving

\[
C(p_1,p_2)=C_*,
\qquad
M(p_1,p_2)=0
\]

are

\[
\boxed{
p_1=\frac{C_*\mu_2}{\det J},
\qquad
p_2=-\frac{C_*\mu_1}{\det J}.}
\tag{T18}

No external forcing is introduced by the algebraic control solve: the parameters are amplitudes of the two designated parent subpackets.

The translated auxiliary-torus lemma already allows finitely many prescribed overlap collars. Thus there is no support-geometric obstruction to placing two independently amplitude-tunable parent-1 subpackets at two distinct pulse times while keeping all non-designated labels separated.

## 7. What is proved and what remains

### Proved here

1. One complex collar amplitude is generically rank-deficient once both nonzero child output and one complex compact-support moment are imposed.
2. Two separated complex collar amplitudes give a full-rank `2 x 2` control matrix whenever the feedback coupling has fixed nonzero sign.
3. The determinant remains nonzero for sufficiently narrow smooth collars.
4. The v0.4 principal `(1,-2)` feedback coupling has the required fixed nonzero sign.

### Still open

1. Embed two translated controls as exact source-type curl-generated packets with the derivative and wave-class estimates required by the branch.
2. Prove a **uniform quantitative lower bound** for the normalized determinant after all packet perturbations, not merely nonvanishing.
3. Enumerate every low unstable/neutral compatibility block. More than one independent unstable complex mode may require additional collar controls.
4. Include the mean block and all correction-generated low modes in one finite-dimensional Jacobian.
5. Combine that finite solve with the stable high-lattice inverse and a contraction on the infinite-dimensional complement.

The next decisive object is therefore the full **low-mode compatibility matrix**, with this two-collar lemma providing its first nontrivial rank block.
