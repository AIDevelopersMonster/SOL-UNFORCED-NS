# Gate 3 exact beta-zero root-phase separation on the common cover

**Status:** PROVED EXACT SOURCE-PHASE PINNING FOR THE LOW-\`u\` BETA-ZERO CHARACTER / TWO-SIDED ROOT-COVECTOR BOUND.  THIS CLOSES THE PHASE-IDENTIFICATION CAVEAT LEFT IN \`beta21_lowu_designated_mean_root_cauchy_curl_realization.md\`.

Pinned external source:

\[
\texttt{openai/NavierStokesAndEuler@f9e8bc5b38b6e212696e8a30e3e91517af887bbd}.
\]

The decisive source identity is the literal phase formula from
\`NavierStokes/PhaseCalculus.lean\`:

\[
\Phi_{\varepsilon,p,p_z,x_0}
=
p\theta+\frac{p_z}{\varepsilon}Z+x_0R
-v\,[pF+p_zG].
\]

Its cylindrical phase normal is

\[
n_\Phi
=
\left(
x_0-v(pF_R+p_zG_R),
\frac pR,
p_z-\varepsilon v(pF_Z+p_zG_Z)
\right).
\]

Because both the phase and the normal are exactly linear in the phase parameters, the beta-zero character \(M=P-2C\) has an exact purely radial phase on the low-\(u\) common cover.

No singularity theorem is claimed here.

---

## 1. Exact linearity of the source phase

For fixed \(\varepsilon,F,G\), the source phase satisfies

\[
\Phi(p_1+p_2,p_{z,1}+p_{z,2},x_{0,1}+x_{0,2})
=
\Phi(p_1,p_{z,1},x_{0,1})
+
\Phi(p_2,p_{z,2},x_{0,2})
\tag{RP1}
\]

and the same identity holds for arbitrary integer linear combinations.

The source theorem \`PhaseCalculus.phaseNormal_formula\` gives

\[
\boxed{
n_\Phi(\varepsilon,p,p_z,x_0)
=
\left(
x_0-v[pF_R+p_zG_R],
\frac pR,
p_z-\varepsilon v[pF_Z+p_zG_Z]
\right).
}
\tag{RP2}
\]

Hence \(n_\Phi\) is exactly linear in \((p,p_z,x_0)\) as well.

The periodized physical phase agrees to all jets with this native phase on the core by the source germ theorem
\`PhysicalSignedWave.ReferencePhase.phase_native_germ\` /
\`phase_native_jets\`.  Therefore the calculations below are exact on the active common-cover core, not merely WKB approximations.

---

## 2. Beta-\((2,1)\) common-cover parameterization

On one low-\(u\) orbit chart use one common tangential unit direction \(K\) and one common positive phase scale \(B_s\).

A beta-\(b\) character at reduced slope \(z\) has reference phase-normal parameters

\[
(p_b,p_{z,b})=bB_sK_{\rm tan},
\qquad
x_{0,b}=bB_sz,
\tag{RP3}
\]

where \(K_{\rm tan}\) denotes the two tangential components encoded by
\((p/R,p_z)\).  This is exactly the character convention underlying the branch formula

\[
n_{b,z}=B_sb(z\,e_r+K).
\tag{RP4}
\]

The parent and catalyst have

\[
\beta(P)=2,\qquad \beta(C)=1.
\]

In the low-\(u\) boundary-layer geometry their reduced slopes differ by

\[
z_C-z_P=\delta_S,
\qquad
\delta_S=\frac{\kappa_S}{S}.
\tag{RP5}
\]

(The orientation only changes the sign below.)

Thus

\[
(p_M,p_{z,M})
:=
(p_P,p_{z,P})-2(p_C,p_{z,C})
=(0,0),
\tag{RP6}
\]

while

\[
x_{0,M}
=
x_{0,P}-2x_{0,C}
=
\pm 2B_s\delta_S.
\tag{RP7}
\]

Therefore the exact character relation \(M=P-2C\) gives

\[
\boxed{
\Phi_M
=
\pm 2B_s\delta_S\,R
+\text{constant gauge},
}
\tag{RP8}
\]

and by (RP2)

\[
\boxed{
n_{\Phi_M}
=
\pm 2B_s\delta_S\,e_r.
}
\tag{RP9}
\]

All \(v\)-dependent terms disappear identically because they are proportional to \(p_M,p_{z,M}\).

This proves that the beta-zero root is not merely angular mean: its full common-cover phase normal is exactly radial.

---

## 3. Include the literal carrier

The actual complex carrier is

\[
e^{ik\Phi}.
\]

Hence the reconstructed root covector in normalized source coordinates is

\[
\boxed{
\Xi_M
=
\pm 2kB_s\delta_S\,e_r.
}
\tag{RP10}
\]

Put

\[
h_\varepsilon:=\sqrt\varepsilon.
\]

The exact source normalization, already audited in
\`source_normalized_two_event_coefficients.md\`, gives

\[
\boxed{
h_\varepsilon kB_s
=
\rho(p)
:=
\frac{\sqrt{\lambda_0(p)}}{(1+u^2)^{3/4}}.
}
\tag{RP11}
\]

On the fixed strict slow compact set,

\[
\boxed{
0<\rho_-\le\rho(p)\le\rho_+<\infty.
}
\tag{RP12}
\]

Therefore

\[
\boxed{
h_\varepsilon|\Xi_M|
=
2\rho(p)\delta_S
=
\frac{2\rho(p)\kappa_S}{S}.
}
\tag{RP13}
\]

Gate 1 gives

\[
\kappa_S=\kappa_*+O(S^{-1}),
\qquad
\kappa_*=0.894049167184884\ldots>0.
\tag{RP14}
\]

After increasing the starting level,

\[
\frac{\kappa_*}{2}\le\kappa_S\le2\kappa_*.
\]

Hence there are fixed positive constants \(c_M,C_M\) with

\[
\boxed{
\frac{c_M}{S}
\le
h_\varepsilon|\Xi_M|
\le
\frac{C_M}{S}.
}
\tag{RP15}
\]

Equivalently,

\[
\boxed{
|\Xi_M|
\asymp
\frac1{h_\varepsilon S}.
}
\tag{RP16}
\]

This is the two-sided bound previously left as an exact-source notation task in the Cauchy/curl realization theorem.

---

## 4. Separation of distinct orbit characters

For catalyst characters

\[
C_j=C+jM
\]

and parent characters

\[
Q_n=P+nM,
\]

phase linearity gives exactly

\[
\Phi_{C_j}-\Phi_{C_k}
=(j-k)\Phi_M,
\tag{RP17}
\]

\[
\Phi_{Q_n}-\Phi_{Q_m}
=(n-m)\Phi_M.
\tag{RP18}
\]

Thus the reconstructed covector separation satisfies

\[
\boxed{
|\Xi_{C_j}-\Xi_{C_k}|
=
|j-k|\,|\Xi_M|,
}
\tag{RP19}
\]

and identically for the parent orbit.

By (RP16),

\[
\boxed{
|\Xi_{C_j}-\Xi_{C_k}|
\asymp
\frac{|j-k|}{h_\varepsilon S}.
}
\tag{RP20}
\]

There is no small-divisor cancellation in the radial direction: the difference phase is affine in \(R\) with a constant nonzero derivative.

---

## 5. Growth along the constant-fast schedule

Gate 2 uses

\[
\varepsilon_j\asymp j^{-1},
\qquad
S_j\asymp(\log j)^2.
\]

Therefore

\[
h_{\varepsilon,j}
=
\sqrt{\varepsilon_j}
\asymp j^{-1/2},
\]

and

\[
\boxed{
|\Xi_{M,j}|
\asymp
\frac{\sqrt j}{(\log j)^2}
\longrightarrow\infty.
}
\tag{RP21}
\]

Hence distinct orbit indices become increasingly separated in actual reconstructed radial frequency even though their reduced slopes differ only by \(O(S^{-1})\).

This resolves the apparent paradox between

- the tangent-Gaussian continuum index spacing \(j/\sqrt S\), and
- physical oscillatory separation.

The profile is slowly varying in reduced slope but increasingly oscillatory in the physical/source-normalized radial variable.

---

## 6. Consequence for Gate 3 extraction

Let \(\chi\) be a fixed normalized radial cutoff supported inside the common-cover core.

For two distinct orbit indices, every physical cross pairing contains the exact oscillatory factor

\[
e^{i(j-k)\Phi_M}.
\]

Since

\[
\partial_R[(j-k)k\Phi_M]
=
(j-k)\Xi_M\cdot e_r
\]

is a nonzero constant on the native core, repeated integration by parts in \(R\) has no stationary-point term.

At every fixed derivative order \(N\), source amplitude/cutoff jets cost only a fixed polynomial in \(S\).  Thus the exact phase identity gives the schematic bound

\[
\boxed{
|\langle W_j,W_k\rangle|
\le
C_N S^{A_N}
\left(
\frac{h_\varepsilon S}{|j-k|}
\right)^N
\|W_j\|_{\rm diag}\|W_k\|_{\rm diag},
\qquad j\ne k.
}
\tag{RP22}
\]

The same statement holds for fixed-order derivative pairings after extracting the common physical carrier powers.

Because on the Gate 2 schedule

\[
h_{\varepsilon,j}S_j
\asymp
\frac{(\log j)^2}{\sqrt j}
\to0,
\tag{RP23}
\]

one may choose one fixed \(N\) larger than the finite source-jet polynomial degree plus the orbit-counting loss.  Then the sum of all off-diagonal pairings over the \(O(S_j)\) source-supported orbit tends to zero relative to the diagonal Gram part.

The next theorem must make (RP22) quantitative in the exact physical \(H^1\) pairing and include the analytic tail/correction terms.  No additional phase-identification hypothesis remains.

---

## 7. Updated Gate 3 frontier

The exact source phase has now been pinned:

\[
\boxed{
M=P-2C
\Longrightarrow
\Phi_M\text{ is exactly radial on the common-cover core,}
}
\]

and

\[
\boxed{
\sqrt\varepsilon\,|\Xi_M|
\asymp S^{-1}.
}
\]

Therefore the last Gate 3 kill criterion is no longer a possible hidden root-phase cancellation.

The remaining theorem is an almost-orthogonal physical characteristic extraction estimate:

\[
\boxed{
\texttt{beta21_lowu_gate3_physical_characteristic_H1_extraction.md}.
}
\]

No finite-time singularity or Clay-prize claim is made here.
