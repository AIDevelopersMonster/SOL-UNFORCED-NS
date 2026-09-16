# Inter-cell transfer reduction for the exact low-`u` bilateral orbit reset

**Status:** PROVED UNIFORM FULL-ORBIT NEAR-IDENTITY TRANSFER INSIDE ONE DYADIC SLAB / IDENTIFIED AND CORRECTED THE DYADIC-BOUNDARY RESAMPLING OBSTRUCTION / GLOBAL INFINITE ASSEMBLY STILL OPEN.

The exact local theorem

`beta21_lowu_exact_finiteS_local_reset.md`

closes one unforced finite-`S` relay cell.  The next global question is whether the exact outgoing state can be transported to the next exact incoming cell without prearranging future high-frequency data.

The old theorem

`beta21_corrected_two_channel_small_log_transfer.md`

is not sufficient for this purpose: it transports only a two-generator designated block from an earlier finite-bank architecture.  The exact low-`u` cell carries the larger canonical state

\[
M_{des}
\oplus
\{C_j\}_{j\in O_{C,S}}
\oplus
\{Q_n\}_{n\in O_{Q,S}}.
\]

This note proves that the complete `O(S)` orbit bank has a dyadically uniform near-identity transfer **while the source length `S` is fixed inside one dyadic slab**.  It also shows why the dyadic boundary `S_n=n^2 -> S_{n+1}=(n+1)^2` requires a separate physical-profile resampling theorem; naive same-index identification is not uniformly bounded in the large-deviation norm.

No infinite cascade or global blowup theorem is claimed.

## 1. Full designated state at fixed source length

Fix one sufficiently large source level and write

\[
\mathcal X_{des,S}
:=
\mathbb C M_{des}
\oplus
\ell^2_{C,S}
\oplus
\ell^2_{Q,S}.
\tag{IT1}
\]

The two orbit norms are the large-deviation norms already used in
`beta21_lowu_designated_orbit_complement_propagator_reduction.md`:

\[
\|c\|_{C,S}^2
=\sum_{j\in O_{C,S}}|c_j|^2e^{2S H_1(z_j)},
\]

\[
\|q\|_{Q,S}^2
=\sum_{n\in O_{Q,S}}|q_n|^2e^{2S H_2(z_n)}.
\tag{IT2}
\]

The beta-zero root is measured in its action-normalized scalar coordinate.

The strict slope core is fixed:

\[
|z-x|\le w,
\qquad
x=0.70,
\qquad
w=0.03.
\]

## 2. Uniform shift bounds remove the `O(S)` dimension

The orbit shifts are

\[
R_Cc=(c_{j-1})_j,
\qquad
R_Qq=(q_{n-1})_n.
\]

Because one orbit index changes reduced slope by `O(S^{-1}))`, while `H_b` has bounded derivative on the fixed compact core,

\[
S\bigl(H_b(z_{k+1})-H_b(z_k)\bigr)=O(1)
\]

uniformly in `S` and the interior index.

Hence the already proved designated-orbit estimate gives

\[
\boxed{
\|R_C^{\pm1}\|_{\ell^2_{C,S}}
+
\|R_Q^{\pm1}\|_{\ell^2_{Q,S}}
\le K_R
}
\tag{IT3}
\]

with one constant `K_R` independent of `S`.

Thus any fixed finite Laurent polynomial in the shifts has operator norm bounded independently of the cardinality

\[
|O_{C,S}|+|O_{Q,S}|=O(S).
\]

This is the key replacement for finite-dimensional compactness.

## 3. Cross-scale evolution inside one dyadic slab

Let the physical relay scale move by

\[
q' = \vartheta q,
\qquad
L_\vartheta:=\log(1/\vartheta),
\]

with both `q,q'` inside the same source dyadic slab.  The reference source level, and therefore `S`, remains fixed.

Exact continuous source chart changes are available for arbitrary positive physical scales inside the slab by `PhysicalParticularWave.chartChange` and `cylinderChange_graph`.

After the same q-normalization used in
`small_log_step_designated_transfer.md`, the complete designated state obeys

\[
\partial_\sigma A
=\mathcal G_S(\sigma)A,
\qquad
0\le\sigma\le L_\vartheta.
\tag{IT4}
\]

The generator consists of:

1. bounded diagonal/source-frame coefficient variation;
2. the designated beta-zero root translation, a fixed linear combination of `R_C^{\pm1}` and `R_Q^{\pm1}`;
3. source-small finite-`S` coefficient errors;
4. no non-`M` order-one orbit feedback, by the fixed action gaps of the low-`u` theorem.

By (IT3), compactness of the normalized source cone, and the fixed compact parameter neighborhood of the exact local theorem, there is one constant `C_orb` such that

\[
\boxed{
\sup_{\sigma\in[0,L_\vartheta]}
\|\mathcal G_S(\sigma)\|_{\mathcal X_{des,S}\to\mathcal X_{des,S}}
\le C_{orb}+\eta_S,
\qquad
\eta_S\to0.
}
\tag{IT5}
\]

The constant does not grow with `O(S)` orbit cardinality.

## 4. Full-orbit near-identity transfer

Let

\[
\mathcal U_S(L_\vartheta,0)
\]

be the fundamental operator of (IT4).  Duhamel and Gronwall yield

\[
\boxed{
\|\mathcal U_S(L_\vartheta,0)-I\|
\le
\exp[(C_{orb}+\eta_S)L_\vartheta]-1.
}
\tag{IT6}

Choose one fixed

\[
\vartheta\in(\vartheta_{orb},1)
\]

so close to one that

\[
\exp[2C_{orb}\log(1/\vartheta)]-1
<\epsilon_{tr}
\tag{IT7}
\]

for a prescribed strict transfer radius `epsilon_tr` inside the common source cone and local-reset parameter neighborhood.

Then for all sufficiently large source levels,

\[
\boxed{
\|\mathcal U_S-I\|<\epsilon_{tr}.
}
\tag{IT8}
\]

This estimate holds on the **entire designated root-plus-orbit bank**, not merely on two Fourier generators.

## 5. Complement leakage during the gap

The low-`u` action audit gives fixed gaps for every non-`M` beta-one/beta-two feedback and uniform stability for beta-three and higher sectors.  The analytic lattice budget uses

\[
\sigma_0=0.005.
\]

Therefore the designated-to-complement transfer over one bounded logarithmic gap has the form

\[
\boxed{
\|\Pi_{comp}\mathcal U_S\Pi_{des}\|
\le
S^A e^{-cS}
+S^A\varepsilon^{a_*}
}
\tag{IT9}
\]

for fixed `A,c,a_*>0`, after the exact coupled local correction is included in the background.

This is source-small and belongs to the next-cell correction class.

## 6. Physical scale growth is retained

The physical carrier scale is

\[
\Omega_{phys}(q)\asymp q^{-\gamma},
\qquad
\gamma=\frac{1+h}{2}.
\]

Thus one near-one step gives

\[
\frac{\Omega_{phys}(\vartheta q)}{\Omega_{phys}(q)}
=\vartheta^{-\gamma}>1.
\tag{IT10}
\]

The uniform full-orbit transfer (IT8) changes only normalized coefficients by an order-one near-identity operator.  It does not remove geometric physical carrier growth.

## 7. Finitely many near-one steps per dyadic slab

`near_one_steps_inside_dyadic_source_bands.md` gives the fixed multiplicity bound

\[
N_\vartheta
=
1+\left\lceil
\frac{\log2}{\log(1/\vartheta)}
\right\rceil.
\tag{IT11}
\]

Hence only a fixed finite number of operators satisfying (IT8) is composed before the next source-level change.

The composition norm over one complete slab is bounded by

\[
\boxed{
\|\mathcal U_{slab,S}\|
\le
\exp(C_{orb}\log2+o(1)),
}
\tag{IT12}
\]

uniformly in the dyadic level.

Thus no exponential-in-`S` transfer constant is produced inside a slab.

## 8. The source-length change at a dyadic boundary

At the next dyadic reference level,

\[
S_n=n^2,
\qquad
S_{n+1}=(n+1)^2,
\]

so

\[
\boxed{
\frac{S_{n+1}-S_n}{S_n}
=
\frac{2n+1}{n^2}
=O(S_n^{-1/2}).
}
\tag{IT13}
\]

The orbit spacing changes from

\[
\delta_n=\kappa_{S_n}/S_n
\]

to

\[
\delta_{n+1}=\kappa_{S_{n+1}}/S_{n+1}.
\]

The fixed slope core therefore contains a slightly different number of integer orbit characters.

This is **not** merely another application of (IT8), because the Banach spaces themselves change:

\[
\ell^2_{C,S_n}\oplus\ell^2_{Q,S_n}
\quad\to\quad
\ell^2_{C,S_{n+1}}\oplus\ell^2_{Q,S_{n+1}}.
\tag{IT14}
\]

## 9. Why naive same-index identification is invalid

Suppose one identifies an old orbit index `j` with the same integer `j` at the new source length.

For an index with

\[
|j|=O(S_n),
\]

the corresponding reduced slopes differ by

\[
|z_j(S_{n+1})-z_j(S_n)|
=O(S_n^{-1/2}).
\tag{IT15}
\]

The large-deviation norm contains

\[
\exp\{S H_b(z)\}.
\]

Away from the orbit center, `H_b'(z)` is a fixed nonzero number.  Consequently the exponent change under (IT15) may be

\[
S_n H_b'(z)\,O(S_n^{-1/2})
=O(S_n^{1/2}).
\tag{IT16}
\]

Thus the same-index map can have norm as large as

\[
e^{O(\sqrt S)}
\]

on tail coordinates.

Therefore the statement

\[
\text{“dyadic boundary transfer }=I+O(S^{-1/2})\text{”}
\]

is false in the raw integer-index large-deviation norm.

This is a genuine normalization issue, not a new Navier--Stokes instability.

## 10. Correct boundary identification must use physical slope

The canonical comparison must match approximately equal **physical reduced slopes**, not equal raw indices.

For each old catalyst index `j`, choose an integer `j'` at the new level with

\[
|z_{C,j'}(S_{n+1})-z_{C,j}(S_n)|
\le C/S_{n+1}.
\tag{IT17}
\]

Likewise choose `n'` for the parent orbit with

\[
|z_{Q,n'}(S_{n+1})-z_{Q,n}(S_n)|
\le C/S_{n+1}.
\tag{IT18}
\]

Such choices exist because both new orbit grids have spacing `Theta(S_{n+1}^{-1})`.

Under slope matching, the large-deviation exponent mismatch from the `H_b` factor is only `O(1)` per matched mode, rather than `O(sqrt S)`.

The new/removed characters that have no partner occur only in an `O(S^{-1/2})`-width strip near the fixed slope-core boundary.  There

\[
H_1\le-c_{bd,C}<0,
\qquad
H_2\le-c_{bd,Q}<0,
\]

so their total physical contribution is bounded by

\[
\boxed{
S^A e^{-c_{bd}S}.
}
\tag{IT19}
\]

for a fixed polynomial multiplicity.

## 11. Remaining dyadic profile-resampling theorem

Slope matching alone does not yet prove that the **canonical bilateral eigenprofile amplitudes** at `S_n` and `S_{n+1}` are close in one common normalized sequence space.

The remaining theorem must combine:

1. the exact geometric eigenprofile factors `rho_C^j` and `rho_P^n`;
2. the tangent/action normalization already built into `H_1,H_2`;
3. slope-matched reindexing (IT17)--(IT18);
4. concentration of the physical profile around `z=x`;
5. the exponentially small unmatched boundary tails (IT19);
6. the finite-`S` parameter drift
   \[
   p_S^{exact}=p_*+O(S^{-1}).
   \]

The desired output is a canonical comparison operator

\[
\boxed{
\mathcal J_{S_n\to S_{n+1}}:
\mathcal X_{des,S_n}
\to
\mathcal X_{des,S_{n+1}}
}
\tag{IT20}
\]

with

\[
\boxed{
\|\mathcal J_{S_n\to S_{n+1}}U_{can,S_n}
-U_{can,S_{n+1}}\|
\to0.
}
\tag{IT21}
\]

A stronger summable rate would be preferable for the global shadowing theorem.

Until (IT21) is proved, the exact local reset cells cannot yet be concatenated across infinitely many source-band boundaries without an additional shadowing argument.

## 12. Consequence

The inter-cell problem has now been split sharply:

\[
\boxed{
\text{inside one dyadic slab: full low-`u` orbit transfer is closed uniformly;}
}
\]

\[
\boxed{
\text{at a dyadic boundary: physical-slope profile resampling is the remaining transfer problem.}
}
\]

This replaces the obsolete two-channel global picture by the correct exact-root plus bilateral-orbit state.

The next mathematical target is `beta21_lowu_dyadic_profile_resampling.md`.  Only after that theorem should one attempt the infinite forward shadowing / single-initial-datum assembly.
