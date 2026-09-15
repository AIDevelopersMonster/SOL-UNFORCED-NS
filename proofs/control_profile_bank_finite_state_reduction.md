# Control-profile bank renewal as a fixed finite-state problem

**Status:** PROVED REDUCTION THEOREM / FINITE FIXED-POINT EXISTENCE STILL OPEN. After `beta21_two_copy_catalyst_bank_renewal.md`, the remaining local support-state issue is not an infinite packet bank. It is a fixed finite family of localized same-character profile degrees of freedom used to obtain full rank in the entrance, strong-`H`, and terminal gate Jacobians.

This note proves that the entire issue can be packaged into one finite-dimensional autonomous renewal map whose dimension is independent of physical scale. It also clarifies which controls may be treated as residual-source particular waves and which genuinely belong to the renewed designated state. Existence of a nonzero fixed point of the resulting full profile map is not claimed here.

## 1. Why the profile issue is finite

The exact corrected cell uses only finitely many localized control directions:

- four same-character beta-two profiles for each entrance gate;
- nine same-character beta-one profiles for the strong-`H` gate;
- three same-character beta-two profiles for the terminal gate;
- finitely many phase/amplitude coordinates.

After doubling the entrance lane for catalyst-bank renewal, the total number of localized complex control amplitudes is still one fixed integer independent of relay level.

Let

\[
r_{prof}<\infty
\]

denote the total complex profile-control count after all duplicated finite lanes are included.

The complete local support state may therefore be written as

\[
\boxed{
\mathfrak S
=
(A_P,A_{C^A},A_{C^B},\mathbf a_{prof},\boldsymbol\phi),
\qquad
\mathbf a_{prof}\in\mathbb C^{r_{prof}}.
}
\tag{CP1}

No component of `S` grows with the physical scale index.

## 2. Residual-source particular waves are not independent future seeds

The source formalization `ParticularWaveAssembly.lean` constructs its actual particular velocities and pressures from

\[
\operatorname{residualSource}(c,u,b,G,A),
\]

that is, from the **current harmonic residual** of the present state. The reference and band particular fields are forward Volterra solves of that residual source.

Therefore any control direction that can be represented as a variation of the current residual-source particular construction is an **internal forward correction direction**, not an independently prearranged future high-frequency packet.

This distinction matters globally because `prearranged_future_bank_backward_heat_obstruction.md` rules out treating an arbitrary late high-frequency control bank as free initial data.

## 3. The exact active controls currently proved are slightly more general

The active gate theorems were proved using independently localized same-character packet perturbations. Their rank arguments require only:

1. source-admissible smooth localization;
2. independent complex amplitudes;
3. fixed nonzero principal coupling margins;
4. `C^1`-small exact correction perturbations.

They do **not yet prove** that every chosen basis vector in the finite control family is literally the image of a residual-source variation under the source particular operator.

Thus the control directions split conceptually into two classes:

\[
\boxed{
\mathbf a_{prof}
=(\mathbf a_{res},\mathbf a_{state}),
}
\tag{CP2}

where

- `a_res` denotes directions realizable as current-residual particular waves;
- `a_state` denotes any remaining independent localized profiles that must be carried as part of the autonomous state until such a realization is proved.

Both blocks are finite.

## 4. One complete exact cell defines a finite output map

Fix the support incidence pattern of `beta21_two_copy_catalyst_bank_renewal.md` and the finite localized profile shapes/centers used by the gate Jacobians.

Conditional on an incoming finite state `S`, solve the exact nonzero/mean correction problem across the whole finite circuit. The existing parameter-dependent contraction theorems give a unique exact solution depending `C^1` on all finite profile amplitudes.

Reading off the renewed beta-two parent, the two renewed beta-one catalyst carriers, their phases, and the outgoing amplitudes of the finite profile/lobe bank gives a map

\[
\boxed{
\mathscr F_\ell:
\mathcal U\subset\mathbb C^{N_{state}}
\to
\mathbb C^{N_{state}},
}
\tag{CP3}

for one fixed finite

\[
N_{state}=3+r_{prof}+N_{phase}.
\]

The dimension is independent of level `ell`.

## 5. Scale-stationary leading map

After source normalization, the local corrected cell has the same frozen beta/slope/action geometry at every sufficiently high level. The exact source corrections satisfy the already-used estimates

\[
S_*^C\varepsilon^\delta\to0,
\qquad
S_*^Ce^{-cS_*}\to0.
\]

Hence on each fixed compact state neighborhood,

\[
\boxed{
\mathscr F_\ell
=
\mathscr F_0+\mathcal E_\ell,
\qquad
\|\mathcal E_\ell\|_{C^1}\to0.
}
\tag{CP4}

The whole autonomous profile-renewal problem is therefore governed by one **fixed finite normalized map** `F_0`, not by infinitely many unrelated control systems.

## 6. Cross-scale transport does not enlarge the state

`beta21_corrected_two_channel_small_log_transfer.md` proves that the designated beta-two/beta-one Fourier block has an invertible near-identity normalized cross-scale transfer.

The same bounded-coefficient argument applies to every fixed finite profile/lobe coordinate carried in the same source packet class: over a sufficiently small fixed logarithmic step, its normalized finite-dimensional transport matrix has the form

\[
\boxed{
G_{prof,j}=I+K_{prof,j},
\qquad
\|K_{prof,j}\|<\eta_{prof}<1
}
\tag{CP5}

provided the profile basis is chosen inside the same strict source cone and the starting level is increased if necessary.

Thus one full scale step is represented by the finite map

\[
\boxed{
\mathscr R_\ell
:=
\mathscr F_{\ell+1}\circ G_{state,\ell},
}
\tag{CP6}

on the same finite state space.

## 7. Autonomous renewal becomes a fixed-point problem

A strict self-renewing profile bank is equivalent to finding a nonzero finite state

\[
\mathfrak S_*
\]

such that, after the canonical character relabeling,

\[
\boxed{
\mathscr R_0(\mathfrak S_*)=\mathfrak S_*.
}
\tag{CP7}

or, if one keeps one scalar normalization parameter free,

\[
\boxed{
\mathscr R_0(\mathfrak S_*)
=\lambda_*\mathfrak S_*,
\qquad
\lambda_*\ne0,
}
\tag{CP8}

with the physical q-weight absorbed by the source normalization as in `q_transport_renormalization_reduction.md`.

If such a fixed point is transverse,

\[
\det(D\mathscr R_0(\mathfrak S_*)-I)\ne0,
\]

then the `C^1` convergence (CP4) and the near-identity cross-scale perturbation imply a unique nearby exact fixed state for all sufficiently high levels by the implicit-function theorem.

## 8. Why this is better than preloading future controls

The prearranged route would require a new high-frequency profile bank at each future scale and therefore runs into backward heat.

The finite-state route instead carries only one fixed-dimensional normalized state forward:

\[
\mathfrak S_j
\longmapsto
\mathfrak S_{j+1}.
\]

All late high-frequency structure is generated from the immediately preceding state and current residual. No independently prescribed future Fourier packet is required if (CP7) closes.

## 9. Sharp next theorem

The remaining finite problem is now explicit:

\[
\boxed{
\textbf{compute the principal full-profile renewal map }\mathscr R_0
\textbf{ and prove a nonzero transverse fixed point/fixed ray.}
}
\tag{CP9}

This requires tracking the finite localized profile amplitudes through:

1. the doubled entrance control blocks;
2. the active strong-`H` block;
3. the reserve-child route;
4. the late terminal block;
5. the small-log cross-scale transfer.

No infinite-dimensional PDE obstruction remains at this stage beyond the exact correction estimates already used to derive (CP4). The unresolved issue is a finite algebraic/dynamical fixed-point calculation.

## 10. Claim discipline

This note does not prove the fixed point (CP7). It proves only that autonomous control-profile renewal has been reduced to a fixed finite-dimensional normalized map. Until that map is computed and shown to possess a transverse nonzero fixed state, an infinite autonomous unforced relay chain remains unproved.
