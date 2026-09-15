# Backward-heat obstruction to the prearranged future-bank route

**Status:** PROVED MECHANISM OBSTRUCTION / ARCHITECTURAL CORRECTION. This note corrects the global interpretation of `beta21_corrected_finite_bank_three_collar_cell.md`. A finite preloaded same-character support bank is legitimate for one local cell, but repeating such a bank independently at every future physical scale cannot be treated as a harmless initial-data summability problem. Unless those future packets are generated forward by the nonlinear dynamics, prescribing order-one normalized high-frequency packets at times tending to the singular time requires backward heat amplification in the initial data.

This does **not** invalidate the one-cell finite-bank theorem. It invalidates only the claim that a countable family of independently prearranged future packets is automatically a viable autonomous unforced global route.

## 1. Linear heat benchmark

For

\[
\partial_t u-\nu\Delta u=0,
\]

a Fourier mode satisfies

\[
\widehat u(K,t)=e^{-\nu |K|^2 t}\widehat u(K,0).
\]

Hence prescribing a later amplitude `a_K(t_j)` at frequency `K_j` by storing that same Fourier component at the initial time requires

\[
\boxed{
\widehat u(K_j,0)=e^{+\nu |K_j|^2 t_j}a_{K_j}(t_j).
}
\tag{BH1}
\]

This is the mechanism already recorded in `notes/02_backward_heat_barrier.md`.

## 2. Application to the corrected relay scaling

The corrected physical carrier law is

\[
\Omega_j\asymp q_j^{-\gamma},
\qquad
\gamma=\frac{1+h}{2}>0,
\]

with

\[
q_j\downarrow0,
\qquad
t_j\uparrow1.
\]

Therefore

\[
\Omega_j^2\asymp q_j^{-(1+h)}.
\]

If an auxiliary support packet needed only in cell `j` were supplied independently from the initial time with an order-one normalized amplitude at `t_j`, then the linear heat benchmark assigns the backward factor

\[
\boxed{
\exp\!\left(c\,q_j^{-(1+h)}t_j\right).
}
\tag{BH2}
\]

for some positive scale constant `c` at the carrier level.

For a geometric relay sequence

\[
q_j=q_0\vartheta^j,
\qquad 0<\vartheta<1,
\]

(BH2) is super-geometric in `j`:

\[
\exp\!\left(cq_0^{-(1+h)}\vartheta^{-j(1+h)}t_j\right).
\]

No polynomial packet weight, fixed positive power of `q_j`, or fixed positive power of the source `epsilon_j=q_j^h` can compensate this growth.

Thus ordinary scale summability of the future packet amplitudes is not the correct global criterion.

## 3. Why source localization does not remove the issue

The OpenAI forced construction can create a high-frequency packet late because its source is itself localized late in physical time. The local pulse inverse is a **forward** Volterra solve. It does not furnish a bounded backward heat propagator from the late packet to the initial time.

Our unforced programme cannot import the late source as external forcing. Therefore every packet that is absent from the incoming dynamical state of a cell but is nevertheless assumed to appear at a later scale must be justified by one of two mechanisms:

1. it is generated forward by nonlinear interaction of already present packets; or
2. a separate theorem proves a special backward history whose initial trace remains smooth and finite energy despite viscosity.

No theorem of type 2 is presently available in this branch.

## 4. Consequence for the finite-bank theorem

`beta21_corrected_finite_bank_three_collar_cell.md` is still valid as a **one-cell theorem** with input bank

\[
C^{ent},\qquad C^H.
\]

What must be withdrawn as a sufficient global continuation is the informal option

\[
\text{one independent prearranged bank at every future scale}
\]

unless an initial-trace theorem overcoming (BH2) is supplied.

Accordingly the preferred global route is now

\[
\boxed{
\textbf{forward support-bank renewal.}
}
\tag{BH3}
\]

The outgoing cell must dynamically generate the finite support carriers required by the next cell.

## 5. The corrected cell already suggests a finite renewal mechanism

The two-copy catalyst bank of the one-cell theorem can potentially be renewed without increasing bank cardinality. Denote the two incoming catalyst copies by

\[
C^A,\qquad C^B.
\]

Run two spatially separated copies of the exact source-matched entrance gate,

\[
P-C^A\to D^A,
\qquad
P-C^B\to D^B.
\]

Then use `D^A` together with the retained `C^B` in the already proved late strong-`H` gate, while routing `D^B` completely outside the strong-`H` and terminal supernodes.

At the reset face both generated unit-beta packets satisfy the same slope/action return,

\[
z_{D^A}(T)=z_{D^B}(T)=x+\delta,
\]

\[
A_{D^A}(T)=A_{D^B}(T)=\mathcal E_{1,u}(x+\delta).
\]

Thus the candidate renewal is

\[
(P,C^A,C^B)
\longmapsto
(P_{new},D^A,D^B)
\longmapsto
(P,C^A,C^B)_{next}.
\]

The companion note `beta21_two_copy_catalyst_bank_renewal.md` isolates this finite renewal theorem and its remaining control-profile caveat.

## 6. New global frontier

After this correction, the relevant hierarchy is:

1. exact one-cell Fourier renewal — already proved;
2. finite catalyst-carrier bank renewal — next finite theorem;
3. renewal of the **localized control-profile degrees of freedom** used by the exact gate Jacobians;
4. near-one cross-scale transport of that complete finite state;
5. infinite sparse packing and exact global assembly.

The prearranged-future-bank summability problem should not be used as a substitute for items 2--3.

## 7. Claim discipline

This note proves only the backward-heat mechanism obstruction to an independently preloaded future bank. It does not prove that every conceivable nonlocal initial-data encoding is impossible, and it does not prove finite-time blowup for unforced Navier--Stokes.
