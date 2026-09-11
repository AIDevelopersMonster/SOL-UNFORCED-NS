# Local zero-residual publication status

**Branch:** `research/mean-vorticity-forward-v0.1`  
**Date:** 2026-09-11

## Threshold decision

The branch has now crossed the publication threshold for a **local-method / one-relay theorem**. It has **not** crossed the threshold for an unforced Navier--Stokes blowup theorem.

The decisive chain is now:

1. exact nonzero-harmonic forward solve conditional on the angular mean;
2. quantitative `m -> z(m)` sensitivity with the small factor on the covariance return leg;
3. correction of the false one-sided radial pressure route by an explicit modified-Bessel Cauchy instability;
4. bounded whole-space Leray formulation at fixed Sobolev order;
5. exact signed-stress Lipschitz gain
   \[
   \delta_{\rm stress}=\frac9{50}-2\kappa_s;
   \]
6. exact phase-adapted Leray/reconstruction intertwining;
7. coupled Banach fixed point yielding zero residual on one frozen relay time collar.

The local theorem is recorded in:

`proofs/coupled_phase_adapted_local_zero_residual_theorem.md`.

## What can be claimed in a first paper

A defensible first preprint may claim a **single-relay exact zero-force closure theorem in a phase-adapted coefficient realization**, together with the pressure-architecture result that one-sided radial pressure propagation is ill posed in the required smooth/Gevrey classes and must be replaced by a time-forward, spatially elliptic whole-space Leray formulation.

It must explicitly state that the following remain open:

- physical-scale inheritance of the noncompact whole-space mean/pressure tail;
- summability across infinitely many relays;
- preservation of the relay action gap under inherited backgrounds;
- global smooth finite-energy assembly;
- finite-time blowup for unforced 3D Navier--Stokes.

## Mandatory pre-publication audit

Before a public PDF/Zenodo release, perform a line-by-line audit of every source-dependent statement against the exact OpenAI paper version. In particular:

- pin exact pages/equations for source derivative normalization;
- pin the packet product laws;
- pin Section 8 mean equations and pressure/stress identities;
- pin Proposition 9.6 Step-2 exponents used for `9/50-2 kappa_s`;
- distinguish exact algebraic identities proved in this branch from source-transferred coefficient bounds;
- verify that the fixed-order covariant Sobolev norm used in the final theorem is equivalent to the finite source packet seminorm actually required by the nonzero forward theorem.

Until that audit is complete, the mathematical threshold is crossed but the manuscript should be treated as **publication candidate**, not final publication version.

## Next research frontier

The next theorem target is:

\[
\boxed{
\text{whole-space pressure/mean tail inheritance from relay }\ell\text{ to relay }\ell+1.
}
\]

A successful scale-inheritance theorem would move the project from a local closure paper toward a genuine autonomous multi-scale relay theorem.