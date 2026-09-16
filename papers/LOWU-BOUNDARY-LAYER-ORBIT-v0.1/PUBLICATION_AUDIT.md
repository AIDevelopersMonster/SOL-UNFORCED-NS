# Publication audit — LOWU-BOUNDARY-LAYER-ORBIT v0.1

**Snapshot date:** 2026-09-16  
**Paper branch:** `paper/lowu-boundary-layer-orbit-v0.1`  
**Research baseline:** `9add88598582959095c418a252a5d0d13ed9596f`  
**Additional theorem after snapshot:** `4451d359a4e9d9b114476808ca6cb2d6bd744bde`

## 1. Publication verdict

**Status:** publication candidate is justified as a local mechanism / obstruction paper.

**Do not publish it as:**

- an unforced Navier–Stokes blow-up theorem;
- an exact full-state finite-`S` reset theorem;
- an infinite cascade theorem;
- a Clay Millennium solution;
- a proof that the compact primary orbit resets exactly.

**Safe publication framing:**

> A low-`u` beta-(2,1) boundary-layer Fourier-orbit mechanism is derived, physically localized, and coupled to an exact phase-adapted source/PDE correction architecture.  A compact-support obstruction proves that no nonzero finite primary orbit can be an exact reset fixed state.  This forces a core-plus-analytic-tail Lyapunov–Schmidt formulation.  The limiting analytic tail operator is shown to be spectrally invertible in a weighted Wiener lattice.

## 2. Main proved theorem layers used in the manuscript

### Reset and low-u mechanism

- exact reset shear `R(K)=K+beta(K)M`, `M=P-2C`;
- low-`u` working point `u=1.8`, `x=0.70`;
- boundary-layer scaling `delta_S=kappa/S`;
- bilateral catalyst and parent orbit equations;
- principal dispersion data and transversality;
- single-root coupling ratio fixed by polarization tuning;
- common source positive-coordinate normalization.

### Finite-S central profile

- central scaling `y=j/sqrt(S)`;
- first-order profile normal form `v_b d_y+B_b y+C_b`;
- explicit `v_C,v_P,B_C,B_P`;
- physical Gaussian admissibility margin.

### PDE/source interface

- exact source graph to viscosity-one physical residual bridge;
- anisotropic whole-space Leray norm-one conjugacy;
- beta-zero root placement in the angular-mean sector;
- exact divergence-free Cauchy/curl realization of `M_des`;
- phase-adapted mean-root Oseen reduction;
- uniform source bilinear packet bound;
- weighted orbit covariance and off-orbit convolution bounds;
- coupled residual mean/nonzero contraction around a prescribed principal state.

### Corrective obstruction and tail architecture

- no nonzero finitely supported catalyst fixed vector;
- no nonzero finitely supported parent fixed vector;
- compact physical primary bank therefore cannot be exact reset state;
- central bilateral profile has transverse expanding spectrum;
- limiting analytic tail spectrum at `sigma_0=0.005` is separated from all reset-symbol zeros;
- limiting analytic tail operators are Wiener-invertible.

## 3. Retracted or superseded interpretation

The commit/file historically named `beta21_lowu_exact_finiteS_local_reset.md` must **not** be cited as proving exact equality of every finite designated orbit coordinate.

The subsequent theorem chain proves that this interpretation was too strong.  The correct conclusion from that layer is only:

- exact zero-residual coupled PDE correction around a prescribed designated principal state;
- exact/macroscopic scalar reset observables after parameter tuning;
- not a complete compact-bank fixed-vector theorem.

The publication manuscript already uses the corrected interpretation.

## 4. Open theorem that must remain explicit

The exact local target is

\[
\mathcal P_S(U_{core,S}+z_{tail,S})
=U_{core,S}+z_{tail,S}.
\]

Still missing:

1. finite-`S` variable-coefficient tail perturbation estimate after the tangent-Gaussian core is removed;
2. corresponding Neumann/Wiener or block-Volterra inverse;
3. simultaneous core-profile and analytic-tail Lyapunov–Schmidt solve;
4. reinsertion of the source-small PDE correction into that full fixed-state equation.

This is the next **local** publication threshold for an exact reset theorem.

## 5. Global status

Even after an exact local core+tail reset, an infinite chain is not automatic.  The central bilateral Poincare maps possess transverse expanding directions.

A global construction still requires one of:

- an exact scale-dependent invariant cocycle/profile;
- a nonautonomous stable/center-manifold construction compatible with Cauchy data and the backward-heat obstruction;
- a single forward sequence-space evolution that generates the visible orbit tails dynamically.

## 6. Numerical audit requirements before Zenodo

All displayed decimal constants are presently reproducible numerical diagnostics.  Before archival release:

- replace sign-sensitive decimals by outward-rounded intervals;
- certify the working-point inequalities for high-beta stability;
- certify Gaussian localization inequalities;
- certify parent/catalyst transversality determinants;
- optionally certify lower bounds for `|F_C|` and `|F_P|` on the analytic annulus.  The manuscript's strict nonvanishing argument is analytic, so the decimal lower bounds are not logically required.

## 7. Bibliography audit

Mandatory items:

- OpenAI forced Navier–Stokes paper;
- exact OpenAI source snapshot `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`;
- repository theorem files used for the low-u chain;
- prior programme/background Zenodo article DOI `10.5281/zenodo.22673644` only as background, not as proof support.

Before final release, add formal bibliographic metadata for the OpenAI paper (title, authorship convention, release date/version) from its publication page/PDF.

## 8. Author/version audit

English author form:

`Malachevsky, A.A.`

Russian author form:

`Малачевский А.А.`

ORCID:

`0009-0008-6009-3196`

Version naming recommendation:

`SOL-UNFORCED-NS-LOWU-ORBIT-v0.1`

Recommended Zenodo title:

**Low-u Boundary-Layer Orbit Mechanics for an Unforced Navier–Stokes Relay**

Recommended Russian companion title:

**Низко-u гранично-слойная орбитальная механика для автономного реле Навье–Стокса**

## 9. AI-assistance disclosure

Safe wording:

> The research workflow used extensive AI-assisted symbolic manipulation, code search, source-code comparison, numerical exploration, and proof auditing. Mathematical claims are limited to the theorem chain and computations frozen in the cited repository snapshot.

Do not imply autonomous experimental verification or independent formal certification of branch Markdown proofs.

## 10. Publication readiness

**GitHub publication candidate:** YES.  
**Zenodo preprint:** YES after interval/numerical certification and bibliography normalization.  
**Claim as exact local reset theorem:** NO.  
**Claim as global unforced blow-up theorem:** NO.
