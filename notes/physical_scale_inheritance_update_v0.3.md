# Physical-scale inheritance update v0.3

**Branch:** `research/physical-scale-inheritance-v0.1`  
**Date:** 2026-09-11

The physical-scale program has moved beyond generic packing. Four points are now separated cleanly.

First, `profile_characteristic_trapped_spine.md` derives the exact leading similarity-coordinate material system

\[
D_tX=\frac{XW}{qL},\qquad D_t\eta=\frac{H_c}{qL},
\]

and uses the source sign structure to obtain a simultaneous zero of `(W,H_c)`. For the realized background `u_B`, strict boundary signs plus the `O(q^{2h})` source correction yield an exact late-time material characteristic trapped in a fixed compact part of the active similarity annulus. Thus infinite-scale geometry is not forced to escape the source cone.

Second, `v08_designated_projection_nonvanishing.md` repairs an internal version mismatch: the old numerical projection estimate was for v0.4, whereas the current architecture uses

\[
\beta_1=2,\qquad\beta_2=1,\qquad u_*=M^2.
\]

For the actual v0.8 family the desired difference-child growing coefficient satisfies

\[
|A_+|\ge\frac{3M}{16}
\]

for sufficiently large frozen `M`.

Third, `v08_state_renewal_obstruction.md` notes that the first difference event alone regenerates only a unit-beta channel. A one-child iteration is therefore not a closed autonomous state recurrence.

Fourth, `v08_beta2_feedback_renewal.md` finds the missing complementary channel inside the same lattice. Since

\[
e_2+(e_1-e_2)=e_1,
\]

the old unit-beta catalyst and the new unit-beta child can undergo a second, later **sum** interaction and regenerate the beta-two parent. The exact finite-`M` renewal resonance occurs at

\[
\theta_M^{\rm ren}\to\theta_*\approx0.1742136425,
\]

where the two beta-one inputs are growing and the beta-two output is decaying. Its principal target projection is bounded away from zero.

Hence the minimal current relay object is no longer a single interaction collar but a **two-event renewal cell**:

\[
(2,1)\xrightarrow{\rm difference}1,
\qquad
(1,1)\xrightarrow{\rm sum}2.
\]

The next theorem must solve the exact zero-force equations on two separated interaction collars plus the transport interval, prove an order-one two-channel outgoing state, and control the additional lattice modes created by the second event. Only after that should infinite packing and terminal global assembly be attempted.

Publication status is unchanged: the one-collar local-method result remains a publication candidate pending source audit. The two-event autonomous renewal architecture is a new research result but is not yet publication-final and does not establish unforced Navier--Stokes blowup.