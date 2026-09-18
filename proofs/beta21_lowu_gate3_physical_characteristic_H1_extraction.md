# Gate 3 physical characteristic \(H^1\) extraction by angular projection and radial almost-orthogonality

**Status:** PROVED PHYSICAL \(H^1\) LOWER-BOUND / SINGULAR-OBSERVABLE THEOREM WITHIN THE CURRENT GATE 1--2 PROOF CHAIN.  THIS CLOSES THE INTERNAL GATE 3 EXTRACTION OBLIGATION.  A FINAL UNFORCED NAVIER--STOKES BLOW-UP CLAIM IS **NOT** PROMOTED IN THIS NOTE; THE COMPLETE DEPENDENCY CHAIN MUST FIRST UNDERGO A SEPARATE ADVERSARIAL AUDIT.

This note uses the exact root-phase pinning from

\[
\texttt{beta21_lowu_gate3_root_phase_separation_pinning.md}
\]

to turn the uniformly nonzero Gate 2 characteristic amplitude into a physical \(H^1\) lower bound.

The key observation is that one does not need to extract a single orbit coefficient by inverting the whole common-torus reconstruction.  The physical angular Fourier projection first isolates one beta sector exactly.  Within that sector, distinct orbit characters differ by integer multiples of the beta-zero root \(M\), whose reconstructed phase is exactly radial and increasingly oscillatory.  Repeated radial integration by parts makes the orbit Gram matrix asymptotically diagonal.

---

## 1. Choose the catalyst characteristic sector

Gate 2 produces an exact nonlinear invariant cocycle

\[
U_j^*
\]

and the characteristic-family theorem identifies the catalyst central amplitude \(A_{C,j}\) as one of its genuine Cauchy coordinates.

The nonlinear cocycle theorem records that the renewed beta-one / beta-two characteristic amplitudes stay uniformly nonzero.  After choosing the late starting level once,

\[
\boxed{
0<c_C\le |A_{C,j}|\le C_C<\infty.
}
\tag{HX1}
\]

We use the beta-one catalyst sector.  The parent sector could be treated similarly but is unnecessary.

---

## 2. Exact physical angular projection

Let \(m_C\ne0\) be the physical integer angular harmonic of the catalyst generator on the common cover.

Because

\[
\beta(M)=0,
\]

every catalyst orbit character

\[
C_r=C+rM
\]

has the same angular harmonic \(m_C\).

The beta-two parent sector has angular harmonic \(2m_C\), and all beta-zero mean modes have angular harmonic zero.

Let \(\Pi_{\theta,m_C}\) be the physical angular Fourier projector, defined invariantly by the rotation group around the symmetry axis:

\[
\boxed{
\Pi_{\theta,m_C}f
=
\frac1{2\pi}
\int_0^{2\pi}
e^{-im_C\alpha}\,
\mathcal R_\alpha f\,d\alpha,
}
\tag{HX2}
\]

where \(\mathcal R_\alpha\) is the unitary physical rotation representation, including rotation of vector components.

Since rotations are isometries of \(H^1(\mathbb R^3)\),

\[
\boxed{
\|\Pi_{\theta,m_C}f\|_{H^1}
\le
\|f\|_{H^1}.
}
\tag{HX3}
\]

Thus it suffices to lower-bound the beta-one projection of \(U_j^*\).

The negative-frequency reality conjugate lies in the opposite angular harmonic and is separated by the same projection convention after complexification.  Passing back to the real field changes only one fixed factor.

---

## 3. Catalyst core decomposition

At stage \(j\), write the projected catalyst central core as

\[
V_j
=
\sum_{r\in I_j}
a_{j,r}(x)
e^{i\Theta_{C_r,j}(x)},
\tag{HX4}
\]

where \(I_j\) is the source-supported orbit index set.

The exact character identity gives

\[
\Theta_{C_r,j}
=
\Theta_{C,j}+r\Theta_{M,j}.
\tag{HX5}
\]

By the root-phase pinning theorem,

\[
\boxed{
\nabla_R\Theta_{M,j}
=
\Xi_{M,j}\cdot e_R
}
\tag{HX6}
\]

is constant on the native common-cover core and

\[
\boxed{
|\Xi_{M,j}|
\asymp
\frac1{\sqrt{\varepsilon_j}S_j}.
}
\tag{HX7}
\]

The exact discrete central-profile theorem gives

\[
f_{C,S_j}
=
\phi_C+O(S_j^{-1/2})
\tag{HX8}
\]

in the physical tangent-Gaussian graph norm.  Since \(\phi_C(0)\ne0\), (HX1) implies that the central coefficient \(r=0\) has a uniform nonzero normalized amplitude:

\[
\boxed{
|a_{j,0}|_{\rm norm}\ge c_0>0.
}
\tag{HX9}
\]

---

## 4. Robust diagonal physical \(H^1\) lower bound with only polynomial localization loss

Put

\[
\gamma=\frac{1+h}{2}.
\]

The chart-invariant carrier theorem gives

\[
\Omega_j\asymp q_j^{-\gamma},
\tag{HX10}
\]

and the physical velocity normalization of one bounded nonzero designated packet has the same amplitude scale

\[
U_{{\rm pkt},j}\asymp q_j^{-\gamma}.
\tag{HX11}
\]

For the lower bound we do **not** use a global fixed-volume lower bound on the entire source support.  The pinned OpenAI source only gives pointwise positivity of the primary weight on the open strip, and explicitly warns that no positive minimum need persist at the support boundary.  The argument therefore uses a central point plus finite-order jet control.

Choose the allowed normalization functional in the exact discrete central-profile theorem to be evaluation at the tangent-Gaussian profile center after fixing the common phase:

\[
\ell_C(f)=f(0).
\tag{HX12}
\]

Then

\[
\ell_C(\phi_C)=1,
\qquad
f_{C,S}=\phi_C+O(S^{-1/2})
\]

in a graph norm controlling one more coefficient derivative.  Together with the compact-annulus bound \( |A_{C,j}|\ge c_C>0\), this gives a physical/source-normalized center coefficient satisfying

\[
\boxed{
|a_{j,0}(x_{j,*})|_{\rm norm}\ge c_*>0
}
\tag{HX13}
\]

for all sufficiently late \(j\).

The source finite-jet calculus gives, at every fixed order used here, a polynomial bound

\[
\boxed{
\|\nabla_{\rm norm} a_{j,0}\|_{L^\infty}
\le C S_j^{B_0}
}
\tag{HX14}
\]

on one fixed compact central chart.  Therefore there is a normalized ball

\[
B_j^{\rm norm}
=
B\!\left(x_{j,*},cS_j^{-B_0}\right)
\]

on which

\[
\boxed{
|a_{j,0}(x)|_{\rm norm}\ge c_*/2.
}
\tag{HX15}
\]

Under the exact source graph dilation, this normalized ball has physical volume bounded below by

\[
\boxed{
|B_j^{\rm phys}|
\ge
c S_j^{-A_0} q_j^{3/2-h}
}
\tag{HX16}
\]

for one fixed finite \(A_0\).  The factor \(q_j^{3/2-h}\) is the intrinsic packet-volume scale; all loss from shrinking the central normalized ball is only polynomial in \(S_j\).

On \(B_j^{\rm phys}\), the principal physical oscillatory derivative has size

\[
\asymp
U_{{\rm pkt},j}\Omega_j
\asymp
q_j^{-2\gamma},
\]

while amplitude/cutoff/curl derivatives are lower by the already-audited source powers and fixed polynomial factors.  Increasing the starting level once, the principal derivative dominates those remainders on a smaller concentric ball.  Hence

\[
\boxed{
\|\nabla W_{j,0}\|_2^2
\ge
c S_j^{-A_0}
q_j^{3/2-h}
q_j^{-2\gamma}
q_j^{-2\gamma}.
}
\tag{HX17}
\]

Since \(4\gamma=2+2h\),

\[
\boxed{
\|\nabla W_{j,0}\|_2^2
\ge
c S_j^{-A_0}q_j^{-1/2-3h},
}
\tag{HX18}
\]

and therefore

\[
\boxed{
\|\nabla W_{j,0}\|_2
\ge
c S_j^{-A_0/2}q_j^{-1/4-3h/2}.
}
\tag{HX19}
\]

This polynomial-loss lower bound is the form used below.  It avoids any unsupported claim of a band-uniform positive amplitude on the full packet support.

---

## 5. Off-diagonal Gram estimate

Consider two distinct catalyst orbit indices \(r\ne s\).

After one physical derivative is taken, every term in the cross pairing

\[
\langle\nabla W_{j,r},\nabla W_{j,s}\rangle
\]

contains the phase factor

\[
e^{i(r-s)\Theta_{M,j}}.
\]

The common base phase \(\Theta_C\) cancels exactly.

By (HX6),

\[
\partial_R[(r-s)\Theta_{M,j}]
=
(r-s)(\Xi_{M,j}\cdot e_R)
\]

is a nonzero constant on the native core.

Use the fixed normalized radial coordinate and integrate by parts \(N\) times.  Compact source cutoffs eliminate boundary terms.  At every fixed \(N\), the source coefficient/curl/frame jet calculus gives only one fixed polynomial loss \(S_j^{B_N}\).  Thus

\[
\boxed{
\frac{
|\langle\nabla W_{j,r},\nabla W_{j,s}\rangle|
}{
\|\nabla W_{j,r}\|_2\,
\|\nabla W_{j,s}\|_2
}
\le
C_N S_j^{B_N}
\left(
\frac{\sqrt{\varepsilon_j}S_j}{|r-s|}
\right)^N.
}
\tag{HX20}
\]

This is the physical \(H^1\) version of the nonstationary-phase estimate anticipated in the root-phase theorem.

The estimate is uniform on the tangent-Gaussian central window.  On the farther source-supported orbit tails, the physical action Gaussian supplies an additional factor and only improves the Schur sum.

---

## 6. Schur smallness despite \(O(S)\) orbit cardinality

Define the normalized off-diagonal Gram kernel

\[
K_{rs}
=
\frac{
\langle\nabla W_{j,r},\nabla W_{j,s}\rangle
}{
\|\nabla W_{j,r}\|_2
\|\nabla W_{j,s}\|_2
},
\qquad r\ne s.
\]

For \(N>1\),

\[
\sup_r\sum_{s\ne r}|K_{rs}|
\le
C_N S_j^{B_N}
(\sqrt{\varepsilon_j}S_j)^N
\sum_{d\ne0}|d|^{-N}.
\tag{HX21}
\]

The constant-fast schedule gives

\[
\varepsilon_j\asymp j^{-1},
\qquad
S_j\asymp(\log j)^2.
\]

Hence, for every fixed \(N\),

\[
S_j^{B_N}(\sqrt{\varepsilon_j}S_j)^N
\asymp
(\log j)^{2B_N+2N}j^{-N/2}
\longrightarrow0.
\tag{HX22}
\]

Therefore

\[
\boxed{
\sup_r\sum_{s\ne r}|K_{rs}|
=o(1).
}
\tag{HX23}
\]

This bound is independent of the number of orbit indices.  The \(O(S_j)\) cardinality does not appear as a dangerous factor because the summable \(|r-s|^{-N}\) kernel is handled by Schur's test.

For all sufficiently late stages, the Gram matrix is therefore coercive:

\[
\boxed{
\left\|
\sum_r \nabla W_{j,r}
\right\|_2^2
\ge
\frac12
\sum_r
\|\nabla W_{j,r}\|_2^2.
}
\tag{HX24}
\]

In particular,

\[
\boxed{
\|\nabla V_j\|_2
\ge
2^{-1/2}\|\nabla W_{j,0}\|_2
\ge
cS_j^{-A_0/2}q_j^{-1/4-3h/2}.
}
\tag{HX25}
\]

---

## 7. Analytic tail and nonlinear correction cannot cancel the core

The exact Gate 1 state is not only the compact central orbit.  In the beta-one angular sector write

\[
\Pi_{\theta,m_C}U_j^*
=
V_j+T_j+Z_j,
\tag{HX26}
\]

where

- \(T_j\) is the analytic reset-tail contribution;
- \(Z_j\) is the beta-one part of the source-small mean/nonzero correction.

The tail is generated by an exponentially small compact-core boundary defect and a polynomially bounded finite-\(S\) tail inverse.  Hence in the phase-adapted physical \(H^1\) norm,

\[
\boxed{
\|T_j\|_{H^1}
\le
S_j^{A} e^{-cS_j}\,
q_j^{-1/4-3h/2}.
}
\tag{HX27}
\]

The coupled correction radius carries a positive source power:

\[
\boxed{
\|Z_j\|_{H^1}
\le
S_j^A
\left(
\varepsilon_j^{a_*}
+e^{-cS_j}
\right)
q_j^{-1/4-3h/2},
\qquad a_*>0.
}
\tag{HX28}
\]

The equality between the coefficient covariant \(H^1\) norm and the reconstructed physical \(H^1\) norm is exact modewise by
\`phase_adapted_whole_space_leray_intertwining.md\`; whole-space Leray has norm at most one there.

Using the schedule,

\[
S_j^A\varepsilon_j^{a_*}\to0,
\qquad
S_j^Ae^{-cS_j}\to0.
\tag{HX29}
\]

Thus

\[
\boxed{
\|T_j+Z_j\|_{H^1}
=
o\!\left(
S_j^{-A_0/2}q_j^{-1/4-3h/2}
\right).
}
\tag{HX30}
\]

Combining (HX15), (HX25), and (HX30),

\[
\boxed{
\|\Pi_{\theta,m_C}U_j^*\|_{H^1}
\ge
cS_j^{-A_0/2}q_j^{-1/4-3h/2}
}
\tag{HX31}
\]

for all sufficiently late \(j\).

Finally (HX3) gives

\[
\boxed{
\|U_j^*\|_{H^1}
\ge
cS_j^{-A_0/2}q_j^{-1/4-3h/2}.
}
\tag{HX32}
\]

The polynomial factor in (HX32) is intentional: it is the price of deriving the lower bound from a central nonzero point and polynomial jet control rather than assuming a uniform lower bound on the entire source support.

---

## 8. Divergence of the physical \(H^1\) observable

Since

\[
q_j\asymp j^{-1/h},
\]

(HX32) implies

\[
\boxed{
\|U_j^*\|_{H^1}
\gtrsim
(\log j)^{-A_0}
j^{(1/4+3h/2)/h}
\longrightarrow\infty.
}
\tag{HX33}
\]

The section times satisfy

\[
t_j\uparrow1.
\]

Therefore the exact Gate 2 forward solution obeys

\[
\boxed{
\|u(t_j)\|_{H^1(\mathbb R^3)}
\longrightarrow\infty
\qquad
(t_j\uparrow1).
}
\tag{HX34}
\]

This is compatible with the finite integrated enstrophy from the energy identity because the high-\(H^1\) states occur on shrinking time scales.

---

## 9. Internal Gate 3 conclusion

Within the current Gate 1--2 theorem chain, the last singular-observable extraction obligation is closed:

\[
\boxed{
\text{Gate 3 physical characteristic }H^1\text{ extraction: CLOSED.}
}
\tag{HX35}
\]

Together with
\`beta21_lowu_gate3_global_cauchy_energy_reduction.md\`, the branch now contains an internal derivation of

1. one smooth finite-energy divergence-free Cauchy datum at \(t_J<1\);
2. one exact smooth unforced viscosity-one Navier--Stokes solution on every compact interval \([t_J,T]\), \(T<1\);
3. bounded kinetic energy and finite integrated enstrophy;
4. a sequence \(t_j\uparrow1\) on which the physical \(H^1\) norm diverges.

---

## 10. Publication / claim discipline

The conclusion (HX35) is mathematically much stronger than the earlier local papers and sits at the level of the global unforced singularity question.

For that reason this file **does not itself promote a Clay-prize or final blow-up claim**.

Before any such promotion, the complete dependency chain must be audited adversarially, in particular:

1. verify the repaired center-point/jet-ball lower bound (HX13)--(HX19) against the literal realized primary-wave/curl formulas and exact graph dilation;
2. verify the relative-jet form needed for the normalized Gram estimate (HX20) uniformly over the exact central profile;
3. verify (HX27)--(HX28) in the same physical \(H^1\) norm with no hidden inverse factor;
4. re-audit the Gate 2 one-Cauchy-state interpretation and finite-prefix exact concatenation;
5. check every theorem used above against the pinned OpenAI source ref and mark any derived extension not literally formalized there.

The next file should therefore be an audit, not another constructive theorem:

\[
\boxed{
\texttt{beta21_lowu_gate3_global_singularity_dependency_audit.md}.
}
\]

If any one of the five checks fails with a nonabsorbable loss, the global singularity claim must be withheld and the branch rolled back to the strongest verified gate.

No Clay-prize claim is made here.
