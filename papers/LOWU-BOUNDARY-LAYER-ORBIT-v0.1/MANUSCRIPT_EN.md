# Low-`u` Boundary-Layer Orbit Mechanics for an Unforced Navier–Stokes Relay

**Version:** v0.1 publication candidate  
**Date:** 2026-09-16  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**Repository:** `AIDevelopersMonster/SOL-UNFORCED-NS`  
**Research snapshot:** `9add88598582959095c418a252a5d0d13ed9596f`

## Abstract

We study a low-parameter boundary-layer relay mechanism for the three-dimensional incompressible Navier–Stokes equations in the source geometry developed around the OpenAI forced blow-up construction.  The present work does **not** claim an unforced singularity or a solution of the Navier–Stokes Millennium problem.  Instead, it isolates and analyzes a local Fourier-orbit mechanism that can be initialized from Cauchy data and that avoids the future-time control defects encountered in earlier finite-state relay designs.

The mechanism is organized by the beta-(2,1) reset shear and the invariant beta-zero character

\[
M=P-2C.
\]

In the low-`u` regime we identify a boundary-layer scaling

\[
\delta_S=\kappa/S
\]

for which the beta-one catalyst and beta-two parent sectors admit a simultaneous bilateral orbit description.  At the working point

\[
u=1.8,\qquad x=0.70,
\]

we derive explicit limiting Poincare operators, compute a compatible single-root polarization, prove physical Gaussian localization of the central orbit profile, and establish phase-adapted whole-space Leray/Oseen bounds for the designated beta-zero mean root and the coupled residual mean/nonzero correction.

A structural obstruction then appears: no nonzero finitely supported bilateral orbit vector can be an exact fixed vector of the limiting reset operator.  Since the physical primary source bank has compact slope support at every finite `S`, an exact compact-primary-bank reset is impossible already at the principal homogeneous level.  The correct local target is therefore a **core-plus-analytic-tail** state.  We prove that the limiting analytic tail operator is spectrally separated from the central tangent-Gaussian instability and is invertible in the weighted Wiener lattice at analytic radius `sigma_0=0.005`.

The remaining local theorem is the finite-`S` variable-coefficient Lyapunov–Schmidt completion of the central tangent-Gaussian core by an exponentially small analytic tail.  This theorem is explicitly left open.

## 1. Scope and claim discipline

The results of this paper concern a local relay mechanism and its finite-`S` spectral architecture.  They do **not** prove:

1. an exact global unforced Navier–Stokes solution with a singularity;
2. an infinite forward cascade;
3. an exact finite-`S` compact-primary-bank Poincare fixed point;
4. a Clay Millennium Prize solution.

The strongest proved conclusions are:

- the low-`u` beta-(2,1) boundary-layer mechanism has a physically admissible tangent-Gaussian central profile;
- one Cauchy-realizable beta-zero root can generate the required beta-one and beta-two orbit translations after polarization tuning;
- the associated source/physical residual, Leray projection, mean/nonzero correction, and fixed-order bilinear estimates are compatible with the low-`u` architecture;
- nonzero finitely supported orbit states cannot reset exactly;
- the analytic tail equation is spectrally invertible at limiting constant-coefficient level.

## 2. Background and source framework

The OpenAI source repository `openai/NavierStokesAndEuler` contains a Lean formalization of forced finite-time blow-up constructions for Navier–Stokes and unforced blow-up for Euler.  The Navier–Stokes result is forced; the present programme asks whether some of its relay and chart technology can be repurposed in an unforced direction.

We use the exact source graph framework, including:

- dyadic scales `Q(n)=2^{-n}`;
- slowly varying stage length `S(n)`;
- small parameter `epsilon=Q^h`;
- exact physical graph pullback identities;
- phase-adapted harmonic and mean classes;
- whole-space Leray projection;
- source-localized wave and covariance estimates.

A crucial source identity is that the graph residual is exactly conjugate to the viscosity-one physical Navier–Stokes residual.  Thus the `epsilon Delta` term in graph coordinates is a coordinate coefficient, not a modified physical viscosity.

## 3. Reset algebra

Let the principal parent and catalyst characters be denoted by `P` and `C`, with

\[
\beta(P)=2,
\qquad
\beta(C)=1.
\]

The reset acts by

\[
R(P)=3P-4C,
\qquad
R(C)=P-C.
\]

Define

\[
\boxed{M:=P-2C.}
\]

Then for every lattice character `K`,

\[
\boxed{R(K)=K+\beta(K)M.}
\]

Since

\[
\beta(M)=0,
\]

we have

\[
\boxed{R(M)=M.}
\]

The beta-zero character belongs to the angular-mean sector.  It is therefore not a nonzero angular harmonic control.  Its correct role is a designated mean root that acts as an order-one translation coefficient on the nonzero beta-one and beta-two orbit sectors.

Define bilateral orbit characters

\[
C_j=C+jM,
\qquad
Q_n=P+nM.
\]

Then

\[
R(C_j)=C_{j+1},
\qquad
R(Q_n)=Q_{n+2}.
\]

## 4. Why the low-`u` regime is selected

At the earlier working point `u=2.5`, two neighboring beta-two parent modes generate a beta-four sector with a fixed positive action advantage.  Polynomial smallness of the interaction coefficient cannot overcome that exponential action gain.

At

\[
\boxed{u=1.8}
\]

the beta-three and beta-four full-symbol sectors have no real turning branches on the chosen source interval, while the beta-one and beta-two sectors retain the structure needed for the relay.

We choose

\[
\boxed{x=0.70}
\]

inside the source Gaussian support

\[
2/3\le z\le4/3,
\]

and use the strict orbit core

\[
|z-x|\le0.03.
\]

## 5. Boundary-layer scaling

The key scale is

\[
\boxed{\delta_S=\kappa/S.}
\]

With stretched clock

\[
\tau=St,
\]

the one-cell interval remains order one.  Orbit slope separation is order `S^{-1}`, while the number of source-supported orbit characters is order `S`.

The limiting beta-one and beta-two orbit equations are constant-coefficient shift equations

\[
\partial_\tau c=a_C Rc,
\qquad
\partial_\tau q=a_P Rq.
\]

Writing the full-cell coefficients as

\[
\lambda_C=2\kappa a_C,
\qquad
\mu_P=2\kappa a_P,
\]

the limiting Poincare maps are

\[
\boxed{\mathcal P_C=R^{-1}e^{\lambda_CR},}
\]

\[
\boxed{\mathcal P_P=R^{-2}e^{\mu_PR}.}
\]

## 6. Limiting fixed profiles

Seek formal geometric shift profiles

\[
Rc=\rho_Cc,
\qquad
Rq=\rho_Pq.
\]

The limiting fixed equations reduce to

\[
\boxed{\frac{e^{\lambda_C\rho_C}}{\rho_C}=1,}
\]

\[
\boxed{\frac{e^{\mu_P\rho_P}}{\rho_P^2}=1.}
\]

At the selected low-`u` working point one obtains

\[
\boxed{\rho_C=0.3510126502440001\ldots,}
\]

\[
\boxed{\rho_P=-2.147691668824314+1.235899139340218\,i,}
\]

\[
\boxed{\lambda_C=-2.982607649202283\ldots,}
\]

\[
\boxed{\mu_P=-0.845013757547658\ldots.}
\]

The associated boundary-layer parameters are

\[
\boxed{\kappa_*=0.894049167184884\ldots,}
\]

\[
\boxed{\theta_*=2.619416765747896\ldots.}
\]

The parent transversality determinant is nonzero, and the catalyst scalar dispersion derivative is also nonzero.  Thus the macroscopic dispersion data are nondegenerate.

## 7. Single-root coupling compatibility

The beta-zero root must generate both the catalyst and parent translations.  A single scalar root amplitude is therefore insufficient unless the principal polarization ratio is tuned.

Using the source positive growing-coordinate normalization, the beta-one and beta-two growing coordinates carry no hidden sector-dependent scalar.  The required ratio is achieved by the transverse polarization parameter

\[
\boxed{\tau_*=-0.2087411867089201\ldots.}
\]

This resolves the principal single-root compatibility condition.

## 8. Finite-`S` tangent-Gaussian normal form

The physically relevant orbit mass is localized at

\[
|j|=O(\sqrt S).
\]

Introduce

\[
h_S=S^{-1/2},
\qquad
y=jh_S.
\]

After removing the limiting geometric factors, the finite-`S` Poincare operator has the leading expansion

\[
\boxed{
\mathcal P_{b,S}^{tan}
=I+h_S\left(v_b\partial_y+B_by+C_b\right)+O(h_S^2).
}
\]

The transport coefficients are

\[
\boxed{v_C=-2.046933015584520\ldots,}
\]

\[
\boxed{v_P=-0.185170992872966-1.044351775683794\,i.}
\]

The Gaussian-drift coefficients satisfy

\[
\boxed{B_C=1.509777659068068\ldots,}
\]

\[
\boxed{B_P=-4.618831967884313+2.657928294237038\,i.}
\]

The corresponding continuum profile equation is

\[
\boxed{
v_bf_b'(y)+(B_by+C_b)f_b(y)=0,
}
\]

with explicit Gaussian/shifted-Gaussian solution.

## 9. Physical localization margin

Let

\[
H_b'(z)=u\bigl(\Gamma_b(z)-\Gamma_b(x)\bigr).
\]

At the working point,

\[
H_1''(x)=-1.915959376503904\ldots,
\]

\[
H_2''(x)=-4.721509426848687\ldots.
\]

The coefficient normal form alone is mildly anti-Gaussian, but the physical large-deviation envelope is stronger.  The sufficient localization condition

\[
\Re(B_b/v_b)>-2\alpha_bd_b^2
\]

holds with substantial margin in both beta-one and beta-two sectors.

Thus the tangent-Gaussian central profile is physically admissible.

## 10. Mean-root and residual PDE architecture

The beta-zero root is an angular-mean mode of source order `M_{1/2}`.  Its principal polarization is orthogonal to its phase normal, so the principal root self-advection vanishes.

The root is realized by an exact divergence-free Cauchy/curl construction.  It is absorbed into the source mean base and enters the nonzero orbit equation as a designated shift coefficient.

In a phase-adapted, source-normalized whole-space norm:

- the Leray projector is an exact norm-one Fourier multiplier after the anisotropic graph dilation;
- the root Oseen transport is a uniformly bounded first-order coefficient;
- root multiplication shifts the beta-zero lattice by one fixed character and costs only the constant `exp(3 sigma_0)`;
- the coupled residual mean/nonzero correction has a Banach contraction because the mean-to-wave leg is `O(1)` while the return covariance gains a positive power of `epsilon`.

These estimates justify solving zero-residual corrections around a prescribed low-`u` principal state.  They do not by themselves prove exact reset of the entire finite primary orbit profile.

## 11. Compact-orbit exact-reset obstruction

At every fixed `S`, the source primary bank has compact slope support.  Therefore the designated primary orbit sequence is finitely supported.

However, no nonzero finitely supported catalyst vector can satisfy

\[
e^{\lambda_CR}c=Rc.
\]

Indeed, let `j_0` be its leftmost nonzero index.  Then

\[
(e^{\lambda_CR}c)_{j_0}=c_{j_0}\ne0,
\]

whereas

\[
(Rc)_{j_0}=0.
\]

Hence

\[
\boxed{
\ker_{c_{00}}(e^{\lambda_CR}-R)=\{0\}.
}
\]

The parent sector is identical:

\[
\boxed{
\ker_{c_{00}}(e^{\mu_PR}-R^2)=\{0\}.
}
\]

Therefore an exact reset state cannot consist only of the compact primary bank.

## 12. Correct local target: core plus analytic tail

The correct finite-`S` ansatz is

\[
\boxed{
U_S=U_{core,S}+z_{tail,S},
}
\]

where

- `U_core,S` is the source-supported tangent-Gaussian primary profile;
- `z_tail,S` lies in the completed analytic correction lattice;
- the full state, not the compact core alone, must satisfy the one-cell fixed equation.

The core truncation defect is exponentially small:

\[
\|d_{bd,S}\|
\le S^Ae^{-cS}.
\]

This is compatible with the already available correction scale.

## 13. Spectral instability of the central bilateral profile

The central bilateral profile is not transversely attracting.  The catalyst multiplier is

\[
m_C(\zeta)=\frac{e^{\lambda_C\zeta}}{\zeta}.
\]

On the natural spectral circle through `rho_C`, every nontrivial phase has modulus greater than one, with maximum expansion greater than eight per cell.

The parent sector is mixed stable/unstable as well.

Therefore a global cascade cannot be justified by merely showing that inter-cell profile mismatch tends to zero.  One needs an exact invariant cocycle or a genuine stable/shadowing construction.

## 14. Analytic-tail spectral separation

The analytic tail uses a different Banach geometry.  At

\[
\boxed{\sigma_0=0.005}
\]

the shift spectrum is the annulus

\[
\boxed{
e^{-3\sigma_0}\le|\zeta|\le e^{3\sigma_0},
}
\]

that is approximately

\[
0.98511\le|\zeta|\le1.01512.
\]

The catalyst fixed-equation symbol

\[
F_C(\zeta)
=1-\frac{e^{\lambda_C\zeta}}{\zeta}
\]

has no zero in this annulus.  The parent symbol

\[
F_P(\zeta)
=1-\frac{e^{\mu_P\zeta}}{\zeta^2}
\]

also has no zero there.

Therefore the weighted Wiener lemma yields bounded inverses

\[
\boxed{(I-\mathcal P_C)^{-1}:\mathcal A_{\sigma_0}\to\mathcal A_{\sigma_0},}
\]

\[
\boxed{(I-\mathcal P_P)^{-1}:\mathcal A_{\sigma_0}\to\mathcal A_{\sigma_0}.}
\]

This proves a genuine spectral separation:

\[
\boxed{
\text{central tangent-profile instability}
\not\Rightarrow
\text{analytic-tail noninvertibility}.
}
\]

At limiting constant-coefficient level, an exponentially small boundary defect therefore produces an exponentially small analytic tail.

## 15. Open finite-`S` theorem

The remaining local publication-level theorem is the variable-coefficient finite-`S` Lyapunov–Schmidt completion:

\[
\boxed{
\mathcal P_S(U_{core,S}+z_{tail,S})
=U_{core,S}+z_{tail,S}.
}
\]

The missing step is to prove that, after the tangent-Gaussian core is split off, the exact tail operator is a small perturbation of the invertible limiting analytic-tail operator, or to prove an equivalent block Volterra theorem near the core boundary.

Until that step is completed, no exact full-state finite-`S` reset theorem is claimed.

## 16. Relation to inter-cell transfer

The inter-cell transfer has been reduced to dyadic profile resampling in the tangent-Gaussian variable, and the resampling error is summable in that profile norm.  Nevertheless, because the central limiting Poincare operator has expanding directions, summable mismatch alone is insufficient for an infinite-chain theorem.

A global construction must therefore produce either:

1. an exact scale-dependent invariant orbit profile;
2. a nonautonomous stable/center manifold compatible with the Cauchy-data constraints; or
3. one forward sequence-space evolution whose physical localization reveals the required orbit tails dynamically.

## 17. Conclusions

The low-`u` boundary-layer analysis changes the local unforced relay problem in three ways.

First, it replaces future-time control profiles by a genuine Cauchy-realizable beta-zero root.  Second, it identifies a source-supported tangent-Gaussian central profile with explicit dispersion and localization margins.  Third, it exposes a structural finite-support obstruction that forces the exact state to contain an analytic tail.

The resulting core-plus-tail Lyapunov–Schmidt problem is narrower and more precise than the original finite-state relay problem.  Its limiting tail operator is invertible, so the remaining obstruction is finite-`S` variable-coefficient control rather than a limiting spectral-size obstruction.

## Acknowledgements and computational assistance

The research workflow used extensive AI-assisted symbolic manipulation, code search, source-code comparison, numerical exploration, and proof auditing.  Mathematical claims in this manuscript are stated only at the level supported by the theorem chain and explicit computations frozen in the referenced repository snapshot.

## References

1. OpenAI, *Finite time blowup for Navier–Stokes*, 2026.  Source and Lean formalization: `openai/NavierStokesAndEuler`, source snapshot `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`.
2. OpenAI, `NavierStokesAndEuler` Lean source files cited throughout this project, including `PhysicalResidualBridge.lean`, `CommonBaseContext.lean`, `WeightedClasses.lean`, `LabelSumBounds.lean`, `PrimaryPulseBounds.lean`, and `PhysicalMeanJetBounds.lean`.
3. Malachevsky, A.A., *When 10,000 AI Mathematicians Went After Navier–Stokes*, Zenodo, DOI 10.5281/zenodo.22673644, 2026.  Background/programme note; not a source for the mathematical claims of the present manuscript.

## Reproducibility snapshot

The publication candidate is built from branch

`research/physical-scale-inheritance-v0.1`

through commit

`9add88598582959095c418a252a5d0d13ed9596f`

plus the analytic-tail theorem

`4451d359a4e9d9b114476808ca6cb2d6bd744bde`.

Numerical constants are diagnostics unless explicitly backed by analytic inequalities.  Decimal margins should be interval-certified before archival publication.
