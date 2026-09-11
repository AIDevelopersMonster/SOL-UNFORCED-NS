# Physical-scale inheritance update v0.2

**Branch:** `research/physical-scale-inheritance-v0.1`  
**Date:** 2026-09-11

The cross-scale program has advanced beyond the first inheritance status note.

## New closed reductions

`proofs/q_transport_renormalization_reduction.md` proves that the explicit physical gain

\[
\vartheta^{-(1+h)/2}
\]

required between `q_j` and `q_{j+1}=vartheta q_j` is not an additional scale-dependent dynamical amplification problem after exact source normalization. It is the change of physical units between the two q-levels. The genuine dynamical requirement is a fixed normalized transfer coefficient

\[
g_\vartheta^{(0)}
\]

between the outgoing unit-beta child and incoming unit-beta primary sectors.

`proofs/small_log_step_designated_transfer.md` then closes this nonvanishing requirement for every fixed shrink factor sufficiently close to one. In logarithmic q-time the normalized WKB/phase evolution has bounded generator on the frozen compact source cone, so its propagator is near the identity over a sufficiently short fixed interval. Since child and next primary are canonically the same unit-beta normalized datum at zero separation,

\[
|g_{j,\vartheta}-1|
\le e^{(C_M+o(1))\log(1/\vartheta)}-1.
\]

Thus one can choose a fixed `vartheta<1`, sufficiently near one, such that

\[
\boxed{\frac34<|g_{j,\vartheta}|<\frac54}
\]

for all sufficiently high relay levels, while phase/polarization leakage remains inside the strict admissible margins.

The geometric sequence

\[
q_j=q_0\vartheta^j
\]

still satisfies `q_j -> 0`, and the intrinsic physical carrier obeys

\[
\Omega_{\rm phys}(q_j)\asymp q_j^{-(1+h)/2}\to\infty.
\]

Hence using a near-one scale ratio does not remove the frequency cascade; it only uses more relay stages.

## Current frontier

The dominant remaining global obligation is no longer mean/pressure inheritance and no longer nonvanishing of the designated q-transfer coefficient.

It is now the **relay-collar packing and global assembly theorem**:

1. place infinitely many local exact relay windows along the q-characteristic with fixed near-one ratio;
2. control overlap between neighboring windows and exclude uncontrolled simultaneous supernode interactions;
3. prove that the accumulated whole-space mean/nonzero tails remain in the admissible incoming background class (the mean/pressure part is already subcritical);
4. prove summability/smoothness of the assembled field on every compact pre-accumulation time interval;
5. verify finite-energy initial data and identify whether the relay accumulation actually forces loss of regularity at the terminal time.

## Publication status

The single-relay local-method result remains a publication candidate pending source-line audit.

The new small-log-step transfer theorem is strong enough to belong in a second/global-development paper or in an expanded version of the first paper, but it does not by itself establish an autonomous infinite cascade or unforced Navier--Stokes blowup.
