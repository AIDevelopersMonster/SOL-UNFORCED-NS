# Designated-orbit/complement propagator reduction for the low-`u` boundary-layer cell

**Status:** PROVED HYBRID-BLOCK OPERATOR REDUCTION / SOURCE-LEVEL OFF-BLOCK ESTIMATE AND EXACT MEAN COUPLING STILL TO BE INSERTED.  This note combines the low-`u` bilateral orbit construction with the existing phase-adapted nonzero-harmonic forward theorem.  Its purpose is to remove the apparent `O(S)`-dimensional inverse problem.

The growing beta-one/beta-two orbit is **not** placed in the analytic correction norm.  It is treated as a designated physical block with its own large-deviation weighted `ell^2` norm and exact beta-zero shift semigroup.  The analytic lattice norm is retained only on the complementary non-designated harmonics.  With the corrected choice

\[
\boxed{\sigma_0=0.005,}
\]

the established physical action gaps dominate the analytic factor `exp(sigma_0 |nu|_1)` even at the orbit-core boundary.

The remaining source-specific obligation is to convert the already established action margins into the precise mixed operator bounds stated in Section 8 below for the actual curl/Leray coefficient realization.  No `O(S) x O(S)` matrix inverse is required.

No exact unforced reset cell or global cascade is claimed here.

## 1. Designated character set

Fix the working point

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

Let

\[
M=P-2C,
\qquad
C_j=C+jM,
\qquad
Q_n=P+nM.
\]

Let `O_{C,S}` and `O_{Q,S}` be the indices whose reduced slopes lie in

\[
|z-x|\le w.
\]

The designated nonzero character set is

\[
\boxed{
\mathcal O_S
=
\{\pm M\}
\cup\{\pm C_j:j\in O_{C,S}\}
\cup\{\pm Q_n:n\in O_{Q,S}\}.
}
\tag{DC1}
\]

Its cardinality is `O(S)`.

Let `Pi_S` denote exact Fourier/character projection onto `O_S` and let

\[
\Pi_S^\perp=I-\Pi_S.
\]

Because the source pulse/frame/viscous operator is diagonal in character index,

\[
\boxed{[\Pi_S,\mathcal D]=0.}
\tag{DC2}
\]

This is an algebraic identity; it has no dimensional constant.

## 2. Designated physical norms

For `b=1,2` use the large-deviation weights

\[
H_b(z)=\mathcal E_b(z)-\mathcal E_b(x)+(x-z)g_b,
\qquad
g_b=u\Gamma_b(x).
\]

Define

\[
\|a\|_{C,S}^2
:=\sum_{j\in O_{C,S}}|a_j|^2e^{2SH_1(z_j)},
\]

\[
\|q\|_{Q,S}^2
:=\sum_{n\in O_{Q,S}}|q_n|^2e^{2SH_2(z_n)}.
\]

The shift ratios are uniformly bounded because consecutive slopes differ by `O(S^{-1})`.  Hence there is `K_R`, independent of `S`, such that

\[
\|R^{\pm1}\|_{C,S}+\|R^{\pm1}\|_{Q,S}\le K_R.
\tag{DC3}
\]

The exact order-one beta-zero translation therefore generates uniformly bounded semigroups on the designated blocks.

## 3. Complement norm

On non-designated nonzero harmonics use the existing analytic packet norm

\[
\boxed{
\|z\|_{\mathfrak A_{\sigma_0,r}}
=
\sum_{\nu\notin\mathcal O_S}
 e^{\sigma_0|\nu|_1}
 (1+|\nu|_1)^r
 \|z_\nu\|_{pkt},
\qquad r=0,1.
}
\tag{DC4}
\]

with

\[
\boxed{\sigma_0=0.005.}
\tag{DC5}
\]

The full hybrid nonzero space is

\[
\boxed{
\mathcal X_{S,r}
=
\ell^2_{C,S}
\oplus
\ell^2_{Q,S}
\oplus
\mathfrak A_{\sigma_0,r}^{\perp}.
}
\tag{DC6}
\]

The designated orbit is thus not penalized by the analytic factor `exp(sigma |nu|)`; only leakage into the complement is.

## 4. Exact designated generator

Write the preloaded beta-zero amplitude as `A_M`.  At principal order, interaction with `M` translates orbit index.  Include the complete finite-`S` beta-zero translation coefficients, diagonal beta-one/beta-two pulse rates, and the reset-compatible coefficient variation in a designated generator

\[
\mathcal G_{des,S}(v).
\]

Its limiting operator is the shift system from `beta21_lowu_boundary_layer_bilateral_orbit_reset.md`, and the finite-`S` coefficient variation is `O(S^{-1})` on the fixed core.

Let

\[
U_{des,S}(v,w)
\]

be its forward propagator.  The uniform shift estimates and compactness of the coefficient range give

\[
\boxed{
\|U_{des,S}(v,w)\|_{\ell^2_{C,S}\oplus\ell^2_{Q,S}}
\le K_{des}
}
\tag{DC7}
\]

on the full stretched collar, with `K_des` independent of `S`.

The important point is structural: this propagator is solved as an `O(S)` shift system, not by inverting a dense `O(S) x O(S)` matrix.

## 5. Complement propagator

On `Pi_S^perp`, retain the full linearized nonzero propagator from `nonzero_harmonic_forward_reduction.md`.  High beta sectors have uniform negative rates on the chosen core:

\[
\Gamma_3\le-1.8918,
\qquad
\Gamma_4\le-3.8597,
\]

and generated beta-zero modes have at worst the polynomial inverse loss `O(S^2)` already audited.

Thus, after removing the designated orbit and the preloaded `M` translation, the diagonal/stable complement retains the same parabolic smoothing structure:

\[
\boxed{
\|U_{comp,S}(v,w)f\|_{\mathfrak A_{\sigma_0,0}}
\le K_{comp}S^{A_0}\|f\|_{\mathfrak A_{\sigma_0,0}},
}
\tag{DC8}
\]

\[
\boxed{
\|U_{comp,S}(v,w)f\|_{\mathfrak A_{\sigma_0,1}}
\le K_{comp}S^{A_1}(1+(v-w)^{-1/2})
\|f\|_{\mathfrak A_{\sigma_0,0}}.
}
\tag{DC9}
\]

The powers `A_0,A_1` are fixed at fixed publication derivative order.  Establishing these precise powers in the actual source realization is one of the remaining bookkeeping tasks; no exponential-in-`S` inverse is required.

## 6. Analytic-weight budget for off-block modes

For catalyst orbit characters

\[
|C_j|_1\le C_CS+O(1),
\qquad C_C\approx0.05033,
\]

and parent orbit characters satisfy

\[
|Q_n|_1\le C_QS+O(1),
\qquad C_Q\approx0.10067.
\]

A conservative quadratic target bound is

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
\boxed{
c_{bd,C}-\sigma_0C_C>6.0\times10^{-4},}
\tag{DC10}
\]

\[
\boxed{
c_{bd,Q}-\sigma_0C_Q>1.5\times10^{-3},}
\tag{DC11}
\]

and

\[
\boxed{
\gamma_{crit}-\sigma_0C_{quad}>0.058.
}
\tag{DC12}
\]

Thus every already identified off-block physical residual remains exponentially small after insertion into the analytic complement norm.

## 7. Exact block form of the linearized nonzero problem

With respect to

\[
\mathcal X_{S,1}
=
\mathcal X_{des,S}
\oplus
\mathfrak A_{\sigma_0,1}^{\perp},
\]

the full nonzero linearization has the form

\[
\partial_v
\begin{pmatrix}a\\z\end{pmatrix}
=
\begin{pmatrix}
G_{des,S}&B_{S}\\
C_{S}&G_{comp,S}
\end{pmatrix}
\begin{pmatrix}a\\z\end{pmatrix}
+
\begin{pmatrix}f_{des}\\f_{comp}\end{pmatrix}
+\mathcal N_S(a,z).
\tag{DC13}
\]

Here:

- `G_des,S` contains the complete order-one `M` shift;
- `G_comp,S` is the stable/full-linearized complement;
- `B_S` and `C_S` contain only off-block character transfers;
- the non-`M` designated self-interactions are included in `N_S` and carry the fixed action gap.

There is no diagonal commutator loss because of (DC2).

## 8. Required off-block estimate

The action and analytic-weight audits reduce the source-specific operator theorem to

\[
\boxed{
\|B_S\|+\|C_S\|
\le S^A e^{-c_*S},
}
\tag{DC14}
\]

for some fixed `A` and some

\[
\boxed{c_*>0.}
\]

One may conservatively take `c_*` below the smallest weighted boundary margin in (DC10)--(DC12).

Likewise the non-`M` nonlinear orbit feedback must satisfy

\[
\boxed{
\|\mathcal N_S^{nonM}(a,z)\|_{\mathcal X_{S,0}}
\le S^A e^{-c_*S}
\bigl(\|a\|+\|z\|\bigr)^2.
}
\tag{DC15}
\]

The source multiplicity, character derivatives, bilinear Leibniz factors and beta-zero inverse contribute only the fixed powers of `S` already proved in `beta21_lowu_orbit_source_polynomial_audit.md`.  What remains is to pin the physical action factor to the exact source packet seminorm term by term.

## 9. Uniform hybrid propagator once (DC14) holds

Let

\[
U_{0,S}
=
U_{des,S}\oplus U_{comp,S}.
\]

Its norm grows at most polynomially in `S` by (DC7)--(DC9).  Variation of constants for the off-diagonal block gives the kernel

\[
U_{0,S}(v,s)
\begin{pmatrix}0&B_S\\C_S&0\end{pmatrix}.
\]

By (DC14), its integral norm is bounded by

\[
S^{A'}e^{-c_*S}\to0.
\]

Hence for all sufficiently large `S`, the Volterra/Neumann series converges uniformly and yields a full propagator

\[
U_S(v,w)
\]

with

\[
\boxed{
\|U_S(v,w)\|_{\mathcal X_{S,0}\to\mathcal X_{S,0}}
\le S^{A''}K,
}
\tag{DC16}
\]

and the same one-derivative parabolic smoothing on the complement.

No constant depends exponentially on `N_S`.

## 10. Nonzero fixed point after the split

The supported source defect consists of:

1. finite-`S` designated coefficient error, removed by the transverse `(kappa,theta,A_M)` principal tuning;
2. boundary truncation leakage;
3. non-`M` orbit feedback;
4. the original algebraically small source residuals and reconstruction remainders.

After the exact principal tuning, items 2--4 have norm

\[
\rho_{S,\ell}
\le
S^A\varepsilon^{1/5}
+S^Ae^{-c_*S}.
\tag{DC17}
\]

For fixed `A`, this tends to zero in the source hierarchy.  The quadratic Duhamel map then has Lipschitz constant

\[
O(S^A\rho_{S,\ell})=o(1),
\]

provided (DC14)--(DC15) are established in the actual packet seminorm.

Thus the nonzero problem reduces to the same Banach fixed-point mechanism as the proved fixed-block theorem, now in the hybrid space (DC6).

## 11. Interaction with finite-dimensional tuning

The limiting principal fixed point is transverse:

\[
\lambda_C-\rho_C^{-1}\approx-5.8315\ne0,
\]

and

\[
\det D_{(\kappa,\theta)}(\Re F_P,\Im F_P)
\approx1.2199\ne0.
\]

The source/parameter audit shows that every fixed parameter derivative costs at most a polynomial in `S`.  Hence an exact nonzero correction of size (DC17) perturbs the three macroscopic exit equations by `o(1)` in `C^1`.

Therefore the finite-dimensional implicit-function theorem survives the exact nonzero correction once the hybrid propagator theorem is closed.

## 12. Remaining frontier

The growing-block inverse problem has been removed.  The remaining exact nonzero theorem is now the single source estimate family

\[
\boxed{
\text{prove (DC14)--(DC15) in the actual curl/Leray packet seminorm.}
}
\]

After that, the nonzero harmonic closure follows by the existing Volterra/Banach argument in the hybrid space.

The next separate obligation is then to insert the same designated/complement split into the angular-mean forcing and verify that the whole-space Leray--Oseen mean fixed point retains its positive epsilon exponent.

No exact unforced reset cell, infinite cascade, or Navier--Stokes blowup theorem is claimed before those two source-level steps are complete.
