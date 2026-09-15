# Corrected designated-nonzero-orbit/complement propagator reduction

**Status:** PROVED HYBRID NONZERO-BLOCK REDUCTION AFTER BETA-ZERO SECTOR CORRECTION / EXACT SOURCE-LEVEL OFF-BLOCK OPERATOR ESTIMATE STILL OPEN.  This file supersedes its previous revision, which incorrectly included the beta-zero root `M=P-2C` in the nonzero angular-harmonic designated set.

The correction is structural:

\[
\boxed{\beta(M)=0}
\]

means that `M` and every multiple `rM` belong to the angular-mean sector.  The preloaded `M` is now the designated mean root of `beta21_lowu_designated_mean_root_coupled_reduction.md`; generated `rM` coefficients are handled by `beta21_lowu_mean_orbit_harmonic_split_and_covariance_audit.md`.

The nonzero designated block contains only the beta-one and beta-two bilateral orbits

\[
C_j=C+jM,
\qquad
Q_n=P+nM.
\]

The designated mean root still acts on this nonzero block as the order-one index-shift coefficient.  With this correction, the apparent `O(S)`-dimensional inverse problem remains absent.

No exact unforced reset cell or global cascade is claimed here.

## 1. Working geometry and nonzero designated set

Fix

\[
u=1.8,\qquad x=0.70,\qquad w=0.03,
\]

and

\[
\delta_S=\kappa_S/S,
\qquad
\kappa_S=\kappa_*+O(S^{-1}),
\qquad
\kappa_*=0.894049167184884\ldots.
\]

Let `O_{C,S}` and `O_{Q,S}` be the indices whose reduced slopes lie in

\[
|z-x|\le w.
\]

The designated **nonzero angular-harmonic** set is

\[
\boxed{
\mathcal O_S^{nz}
=
\{\pm C_j:j\in O_{C,S}\}
\cup
\{\pm Q_n:n\in O_{Q,S}\}.
}
\tag{DN1}
\]

Its cardinality is `O(S)`.

The beta-zero root pair

\[
\{\pm M\}
\]

is not part of (DN1); it is the designated angular mean.

Let `Pi_S^{nz}` denote exact character projection onto (DN1).  Because the source pulse/frame/viscous operator is diagonal in the nonzero character index,

\[
\boxed{[\Pi_S^{nz},\mathcal D]=0.}
\tag{DN2}
\]

This identity has no dimensional constant.

## 2. Designated orbit norm

For `b=1,2`, use

\[
H_b(z)=\mathcal E_b(z)-\mathcal E_b(x)+(x-z)g_b,
\qquad
g_b=u\Gamma_b(x).
\]

Define

\[
\|a\|_{C,S}^2
=\sum_{j\in O_{C,S}}|a_j|^2e^{2SH_1(z_j)},
\]

\[
\|q\|_{Q,S}^2
=\sum_{n\in O_{Q,S}}|q_n|^2e^{2SH_2(z_n)}.
\]

Consecutive slopes differ by `O(S^{-1})`, so the shift operators satisfy

\[
\boxed{
\|R^{\pm1}\|_{C,S}+\|R^{\pm1}\|_{Q,S}\le K_R
}
\tag{DN3}
\]

uniformly in `S`.

## 3. The designated mean root as a nonzero-orbit generator coefficient

Let `M_des` be the exact Cauchy/curl root constructed in

`beta21_lowu_designated_mean_root_cauchy_curl_realization.md`.

It is an angular mean field of source order `M_{1/2}`.  Its principal mixed interactions are

\[
M_{des}+C_j\to C_{j+1},
\]

\[
M_{des}+Q_n\to Q_{n+1},
\]

with nonzero source-normalized coefficients.  Include the complete finite-`S` versions of these interactions, together with the diagonal beta-one/beta-two pulse rates, in the designated nonzero generator

\[
\boxed{G_{des,S}(v;M_{des}).}
\tag{DN4}
\]

Thus `M_des` is a **coefficient of the nonzero generator**, not a vector in the nonzero state space.

Let

\[
U_{des,S}(v,w)
\]

be the corresponding forward orbit propagator.  The boundary-layer shift analysis gives the target uniform bound

\[
\boxed{
\|U_{des,S}(v,w)\|_{
\ell^2_{C,S}\oplus\ell^2_{Q,S}}
\le K_{des}.
}
\tag{DN5}
\]

The limiting propagator is exactly the bilateral shift semigroup whose Poincare fixed point was solved in `beta21_lowu_boundary_layer_bilateral_orbit_reset.md`.

## 4. Analytic nonzero complement

On non-designated **nonzero angular** harmonics use

\[
\boxed{
\|z\|_{\mathfrak A_{\sigma_0,r}}
=
\sum_{\nu\notin\mathcal O_S^{nz}\atop \beta(\nu)\ne0}
 e^{\sigma_0|\nu|_1}
 (1+|\nu|_1)^r
 \|z_\nu\|_{pkt},
\qquad r=0,1,
}
\tag{DN6}
\]

with

\[
\boxed{\sigma_0=0.005.}
\tag{DN7}
\]

All beta-zero outputs are excluded from (DN6) and routed to the angular-mean equation.

The hybrid nonzero space is therefore

\[
\boxed{
\mathcal X_{S,r}^{nz}
=
\ell^2_{C,S}
\oplus
\ell^2_{Q,S}
\oplus
\mathfrak A_{\sigma_0,r}^{\perp,nz}.
}
\tag{DN8}

## 5. Stable nonzero complement

At the selected low-`u` point,

\[
\Gamma_3\le-1.8918,
\qquad
\Gamma_4\le-3.8597
\]

on the strict core, with stronger negativity for larger beta.  Non-designated beta-one/beta-two feedback has the fixed action gaps established in the principal boundary-layer audit.

Therefore, after extracting the designated `C/Q` orbit and the `M_des`-driven shift, the remaining nonzero operator retains the forward parabolic smoothing mechanism of `nonzero_harmonic_forward_reduction.md`.  At fixed publication derivative order the expected form is

\[
\boxed{
\|U_{comp,S}(v,w)f\|_{\mathfrak A_{\sigma_0,0}}
\le K S^{A_0}\|f\|_{\mathfrak A_{\sigma_0,0}},
}
\tag{DN9}
\]

\[
\boxed{
\|U_{comp,S}(v,w)f\|_{\mathfrak A_{\sigma_0,1}}
\le KS^{A_1}(1+(v-w)^{-1/2})
\|f\|_{\mathfrak A_{\sigma_0,0}}.
}
\tag{DN10}
\]

No beta-zero static inverse occurs in this nonzero complement after the sector correction.

## 6. Analytic-weight budget

The orbit-index bounds are

\[
|C_j|_1\le C_CS+O(1),
\qquad C_C\approx0.05033,
\]

\[
|Q_n|_1\le C_QS+O(1),
\qquad C_Q\approx0.10067.
\]

A conservative nonzero quadratic target bound is

\[
C_{quad}\approx0.20134.
\]

The physical boundary and interior gaps are

\[
c_{bd,C}\ge8.61\times10^{-4},
\qquad
c_{bd,Q}\ge2.106\times10^{-3},
\]

\[
\gamma_{crit}\ge0.05925.
\]

At `sigma_0=0.005`,

\[
\boxed{c_{bd,C}-\sigma_0C_C>6.0\times10^{-4},}
\tag{DN11}
\]

\[
\boxed{c_{bd,Q}-\sigma_0C_Q>1.5\times10^{-3},}
\tag{DN12}
\]

\[
\boxed{\gamma_{crit}-\sigma_0C_{quad}>0.058.}
\tag{DN13}
\]

Hence every already identified **nonzero-sector** off-orbit residual remains exponentially small after analytic weighting.

Generated beta-zero differences are not estimated by (DN11)--(DN13); their separate and much larger mean-sector margins are proved in `beta21_lowu_mean_orbit_harmonic_split_and_covariance_audit.md`.

## 7. Corrected block form

With

\[
\mathcal X_{S,1}^{nz}
=\mathcal X_{des,S}^{nz}
\oplus\mathfrak A_{\sigma_0,1}^{\perp,nz},
\]

the nonzero linearization about the full principal state

\[
U_{base}+M_{des}+U_{orb,S}
\]

has the form

\[
\partial_v
\begin{pmatrix}a\\z\end{pmatrix}
=
\begin{pmatrix}
G_{des,S}(M_{des})&B_S\\
C_S&G_{comp,S}(M_{des})
\end{pmatrix}
\begin{pmatrix}a\\z\end{pmatrix}
+
\begin{pmatrix}f_{des}\\f_{comp}\end{pmatrix}
+\mathcal N_S^{nz}(a,z;m_{corr}).
\tag{DN14}
\]

Here:

- `G_des,S` contains the complete order-one mean-root shift;
- `G_comp,S` contains the stable/full-linearized nonzero complement;
- `B_S,C_S` contain only nonzero-sector off-orbit transfers;
- every beta-zero quadratic output is sent to the coupled mean equation;
- dependence on the residual mean correction is perturbative and carries the old positive source exponent.

## 8. Remaining nonzero operator estimate

The source action/analytic audits reduce the exact nonzero theorem to

\[
\boxed{
\|B_S\|+\|C_S\|
\le S^Ae^{-c_*S},
}
\tag{DN15}
\]

and

\[
\boxed{
\|\mathcal N_{S,off}^{nz}(a,z)\|_{
\mathcal X_{S,0}^{nz}}
\le
S^Ae^{-c_*S}
(\|a\|+\|z\|)^2
}
\tag{DN16}
\]

for one fixed `c_*>0`, after the exact physical curl/Leray packet seminorm is inserted.

The source multiplicity and fixed-order derivative losses are polynomial in `S`; the analytic exponential has already been paid in (DN11)--(DN13).

## 9. Uniform hybrid propagator once (DN15) is source-pinned

Let

\[
U_{0,S}=U_{des,S}\oplus U_{comp,S}.
\]

Its norm grows at most polynomially in `S`, while the off-diagonal operator is `S^Ae^{-c_*S}`.  Therefore the Volterra/Neumann series for the full block propagator converges for sufficiently large `S`, yielding

\[
\boxed{
\|U_S(v,w)\|
\le KS^{A'}
}
\tag{DN17}
\]

with no exponential dependence on the orbit cardinality.

The nonzero correction fixed point then has forcing radius of the form

\[
\boxed{
\rho_{S,\ell}^{nz}
\le
S^A\varepsilon^{1/5}
+S^Ae^{-c_*S}.
}
\tag{DN18}
\]

This tends to zero in the source hierarchy.

## 10. Coupling to the corrected mean block

The angular mean is decomposed as

\[
M_{des}+m_{corr}.
\]

The root `M_des` is already included in `G_des,S`.  The residual mean `m_corr` enters the nonzero system through the same mean-to-wave coefficient perturbation as in the proved local theorem.  Conversely, every conjugate/orbit-difference zero-beta output of the nonzero system is routed to the residual mean equation.

The correct common state space is therefore

\[
\boxed{
\{M_{des}\}
\oplus
\ell^2_{C,S}\oplus\ell^2_{Q,S}
\oplus
\mathfrak M_{\sigma_0}^{mean}
\oplus
\mathfrak A_{\sigma_0}^{\perp,nz}.
}
\tag{DN19}
\]

The whole-space mean norm for the oscillatory root is further refined to the semiclassical `W^{m,p}` scale in `beta21_lowu_semiclassical_mean_root_oseen_reduction.md`.

## 11. Current frontier

After the beta-zero correction, the nonzero growing-block problem is cleaner than in the previous revision.  The exact remaining nonzero obligation is

\[
\boxed{
\text{prove (DN15)--(DN16) in the actual curl/Leray packet norm.}
}
\]

The separate mean obligation is the semiclassical whole-space Oseen/covariance theorem around the Cauchy-realized `M_des`.

Only after both are closed may the principal finite-dimensional transversality be promoted to an exact finite-`S` zero-residual reset cell.
