# Designated beta-zero mean-root reduction for the low-`u` boundary-layer orbit cell

**Status:** PROVED HARMONIC-SECTOR IDENTIFICATION + PRINCIPAL SELF-NULL + COUPLED BLOCK REDUCTION / EXACT SOURCE-LEVEL GROWING-ORBIT MEAN ESTIMATE STILL OPEN.  This note corrects the harmonic-sector placement of the reset-invariant character

\[
M=P-2C.
\]

`M` has beta zero, and in the source harmonic realization beta is the tangential/angular coefficient.  Therefore `M` is an angular-mean mode, not a member of the nonzero angular-harmonic correction lattice.  The low-`u` boundary-layer candidate survives this correction because `M` is a **designated mean root** of source order `M_{1/2}`, not the small residual mean correction.  Its principal self-advection vanishes identically, while its mean-wave interaction with the beta-one/beta-two orbit is precisely the order-one index translation already used in the boundary-layer Poincare map.

The corrected decomposition is

\[
\boxed{
U
=U_{base}+M_{des}+U_{orb,S}+m_{corr}+z_{corr}.
}
\]

Here `M_des` belongs to the principal mean block, `U_orb,S` is the designated nonzero beta-one/beta-two orbit, and only `m_corr,z_corr` are solved in the small correction spaces.

No exact unforced reset cell or infinite cascade is claimed in this note.

## 1. Why beta zero is angular mean

The source harmonic field has the literal form

\[
\operatorname{field}(c,k,\Phi,k_p)(x,\theta)
=\sum_j c_j(x)e^{ij k\Phi(x)}e^{ij k_p\theta}.
\]

Thus the physical angular frequency of harmonic `j` is the integer `j k_p`.  Its normalized angular integral retains exactly the zero angular character.

In the beta-relay reduction, beta is the tangential/angular coefficient.  This is already used in the integral-beta architecture: the beta-two/beta-one design makes the first feedback tangential coefficient `1-beta_C=0`.  The later root audit explicitly identifies

\[
\boxed{\beta(M)=0}
\]

as the **zero-tangential / beta-zero mean root**.

Therefore

\[
\boxed{M\in\text{angular mean sector}.}
\tag{DM1}
\]

It must not be counted as a nonzero angular harmonic merely because its rank-two `(P,C)` character is nonzero.

## 2. Physical scale of the designated mean root

The source primary wave is of order

\[
W_{1/2}.
\]

Each designated velocity carries the physical prefactor `sqrt(epsilon)`.  The principal phase derivative contributes `k B_s`, with

\[
\sqrt\varepsilon\, kB_s=O(1)
\]

in source-normalized coordinates.  Therefore one quadratic wave-wave interaction has physical output scale

\[
(\sqrt\varepsilon)^2 kB_s
=O(\sqrt\varepsilon).
\]

The beta-zero root produced by a difference interaction is consequently a mean field of source order

\[
\boxed{M_{des}\in M_{1/2}.}
\tag{DM2}
\]

The normalized root amplitude used in the boundary-layer Poincare calculation is `O(1)`, but the physical mean velocity is still `O(sqrt(epsilon))` in the source normalization.

This is larger than the generic residual mean-correction scale `O(epsilon^{1-kappa_s})`, so `M_des` cannot be hidden inside `m_corr`.  It is nevertheless small relative to the fixed background and tends to zero with the dyadic level.

## 3. Principal polarization of the beta-zero root

The existing mean-root polarization audit gives, before an irrelevant scalar normalization,

\[
\boxed{
b_M
= -S_M K+c_0R_MN,
}
\tag{DM3}
\]

with `S_M,R_M>0`.  The beta-zero target normal is purely radial, hence the root phase vector is proportional to

\[
\xi_M=m e_r.
\tag{DM4}
\]

In particular

\[
\boxed{b_M\cdot\xi_M=0.}
\tag{DM5}
\]

This is the exact principal incompressibility relation for the root.

## 4. Principal self-advection null

For a complex principal plane wave

\[
u_M=b_Me^{i\xi_M\cdot x},
\]

its self-advection is

\[
(u_M\cdot\nabla)u_M
=i(b_M\cdot\xi_M)b_Me^{2i\xi_M\cdot x}=0.
\]

The real field contains the conjugate wave as well.  The zero-frequency cross terms also vanish because

\[
b_M\cdot(-\xi_M)=0,
\qquad
\overline b_M\cdot\xi_M=0.
\]

Hence the complete frozen principal real root satisfies

\[
\boxed{
\Pi_{mean}\,\mathcal B(M_{des},M_{des})=0
}
\tag{DM6}
\]

at principal carrier order.

Thus extracting an `M_{1/2}` mean root does **not** create a new uncancelled `M_{1/2}` inhomogeneous mean source from its own principal Reynolds stress.

Localized cutoff, moving-frame, curl-reconstruction and coefficient-variation terms are lower source-order terms and belong to the already existing source-error audit; their precise growing-orbit packet estimate remains part of the source-level closure obligation.

## 5. Why `M` still produces order-one nonzero orbit translation

The null (DM6) does not make `M` dynamically irrelevant.  For a positive-beta growing wave `W`, the mean-root polarization audit gives a nonzero principal coefficient

\[
A_{M+W}^+
=\frac12(A_h+A_N),
\]

with fixed nonzero margins on compact admissible geometry.

Therefore

\[
M+C_j\longrightarrow C_{j+1},
\]

\[
M+Q_n\longrightarrow Q_{n+1}
\]

remain order-one after source normalization.  These are exactly the shift terms used by the low-`u` bilateral Poincare system.

The source exponent rule

\[
W_{1/2}\times M_{1/2}\to W_{1/2}
\]

explains this scaling: the designated mean root changes the principal nonzero generator rather than acting as a small perturbation.

## 6. Corrected principal decomposition

Let

\[
U_{orb,S}=U_{C,S}+U_{Q,S}
\]

be the truncated beta-one/beta-two bilateral orbit on the strict slope core.  The correct principal state is

\[
\boxed{
U_{des,S}=U_{base}+M_{des}+U_{orb,S}.
}
\tag{DM7}
\]

Write the exact field as

\[
\boxed{
U=U_{des,S}+m_{corr}+z_{corr},
}
\tag{DM8}
\]

where

- `m_corr` is angularly invariant and lies in the small phase-adapted whole-space mean space;
- `z_corr` contains nonzero angular harmonics outside the designated beta-one/beta-two orbit.

The preloaded root `M_des` is not part of either correction unknown.

## 7. Nonzero generator with a designated mean coefficient

Linearizing the nonzero equation about `U_des,S`, include

\[
\mathcal B(M_{des},z)+\mathcal B(z,M_{des})
\]

in the **principal designated/full linear generator**.  On the beta-one/beta-two orbit this is the exact shift system.  On the complement it is an additional bounded first-order coefficient operator, treated in the same full-linearized Volterra propagator as the fixed designated-wave mixed terms.

Thus the nonzero designated set is corrected to

\[
\boxed{
\mathcal O_S^{nz}
=
\{\pm C_j\}\cup\{\pm Q_n\},
}
\tag{DM9}
\]

with no `M` element.  The character projection onto (DM9) still commutes with the mode-diagonal pulse/viscous operator.  The `M_des` coupling is an off-diagonal **mean-to-wave shift inside the designated generator**, not leakage into the analytic complement.

## 8. Mean generator with the root extracted

The full angular mean is

\[
M_{des}+m_{corr}.
\]

Linearize its exact whole-space mean equation about `U_{base}+M_{des}` and include all terms linear in `m_corr` in the mean Oseen generator.  The principal root self-source vanishes by (DM6).

This is not a new architecture.  The earlier exact theorem `beta21_second_gate_mean_root_C1_exact_transfer.md` already uses precisely the same split for a finite beta-zero root block: it states that the leading beta-zero source response is extracted into the designated block and **is not counted as a small generic mean correction**, after which the residual mean fixed point retains the contraction factor

\[
q_\ell
\le
CS_*^A
\left[
\varepsilon^{9/50-2\kappa_s}
+\varepsilon^{1/2-\kappa_s}
+\varepsilon^{1-2\kappa_s}
+\rho_\ell
\right]
\to0.
\tag{DM10}
\]

The present low-`u` cell changes the surrounding nonzero designated family from fixed size to `O(S)`, but it introduces only the source-counting/analytic-weight losses already audited separately.

## 9. Coupling of the residual mean correction to the orbit

A perturbation `delta m_corr` acts on the designated `W_{1/2}` orbit according to

\[
W_{1/2}\times M_\mu\to W_\mu.
\]

Pairing the resulting wave perturbation with a designated wave returns to the mean with gain

\[
\varepsilon^{1/2-\kappa_s}.
\]

The `O(S)` orbit count and fixed-order parameter derivatives multiply this by fixed powers of `S`; they do not change the positive epsilon exponent.  Therefore the target growing-orbit version of the old mean-to-wave-to-mean estimate is

\[
\boxed{
\|\delta\mathcal N_{w\to m}\|
\le
CS^A
\left[
\varepsilon^{1/2-\kappa_s}
+\rho_{S,\ell}
\right]
\|\delta m_{corr}\|.
}
\tag{DM11}
\]

The exact value of the polynomial power `A` is irrelevant asymptotically but must be pinned in the source packet norm for publication.

## 10. New inhomogeneous mean terms from the orbit bank

There are three classes.

### 10.1 Root self-source

The principal term vanishes exactly by (DM6).  Only lower-order localized/curl/frame terms remain.

### 10.2 Conjugate beta-one/beta-two orbit pairs

Their genuine angular means are quadratic in `W_{1/2}` amplitudes.  Source covariance calculus places such terms in the mean class according to

\[
W_{1/2}\times W_{1/2}
\to M_{1-\kappa_s}.
\]

Summing `O(S)` locally active orbit modes and taking fixed derivatives changes this by a polynomial factor only.  Thus the orbit covariance forcing has the admissible form

\[
\boxed{
\|F_{cov}^{orb}\|
\le CS^A\varepsilon^{1-\kappa_s}
+CS^Ae^{-cS}.
}
\tag{DM12}
\]

provided the source-level orbit realization satisfies the polynomial-counting bounds already isolated in `beta21_lowu_orbit_source_polynomial_audit.md`.

### 10.3 Nonconjugate orbit pairings

They remain nonzero angular harmonics and are handled by the designated/nonzero complement split.  The fixed physical action gaps and `sigma_0=0.005` analytic budget make their complementary contributions exponentially small.

## 11. Mean self-map scale

Combining the old inhomogeneous source forcing with (DM12), the residual mean self-map may use a radius

\[
\boxed{
r_{mean,S}
=CS^A\varepsilon^{1-\kappa_s}
+CS^Ae^{-cS}.
}
\tag{DM13}
\]

For fixed `A`, this tends to zero in the source hierarchy.  The old Lipschitz factors acquire at most further polynomial powers of `S` and therefore still tend to zero.

Thus **the presence of the designated `M_{1/2}` root does not by itself destroy the residual mean contraction**.

What is not yet proved here is the exact source-level whole-space Oseen bound after all `S`-dependent orbit coefficients are inserted simultaneously.

## 12. Corrected hybrid state space

The proper coupled space is not

\[
\{M,C_j,Q_n\}\oplus\mathfrak A_\sigma.
\]

It is

\[
\boxed{
\mathcal X_S
=
\underbrace{\{M_{des}\}}_{\text{designated mean}}
\oplus
\underbrace{\ell^2_{C,S}\oplus\ell^2_{Q,S}}_{\text{designated nonzero orbit}}
\oplus
\underbrace{\mathfrak M_{\sigma_0,m_0}}_{m_{corr}}
\oplus
\underbrace{\mathfrak A_{\sigma_0,1}^{\perp}}_{z_{corr}}.
}
\tag{DM14}
\]

`M_des` is a finite macroscopic parameter, not a Banach correction coordinate.

## 13. Remaining exact obligations

The low-`u` candidate now has the following precise PDE frontier:

1. prove the actual curl/Leray off-orbit estimate for the nonzero block after moving `M_des` into the mean generator;
2. prove the whole-space mean propagator bound linearized about `U_base+M_des` with constants polynomial in `S` at fixed derivative order;
3. prove (DM12) directly in the phase-adapted whole-space mean norm for the `O(S)` orbit covariance sum;
4. combine the two contractions and show their `C^1` dependence on `(kappa,theta,A_M)` is `o(1)` after action normalization;
5. only then apply the already established principal transversality to obtain an exact finite-`S` local reset cell.

These are source/operator estimates.  The harmonic-sector mistake has been corrected and no new principal action obstruction is exposed by the correction.

## 14. Consequence

The correct interpretation is

\[
\boxed{
\beta(M)=0
\Rightarrow
M\text{ is a designated angular mean root of size }M_{1/2},
}
\]

not a nonzero harmonic correction.

Its principal self-advection is null, and its only order-one leading role is the intended translation of the beta-one/beta-two orbit.  The residual mean equation remains perturbative after the root is extracted.

The next theorem should close the `S`-dependent whole-space mean propagator and orbit-covariance estimate in (DM12).
