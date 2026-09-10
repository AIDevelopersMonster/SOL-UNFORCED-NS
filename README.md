# SOL-UNFORCED-NS

**Working research branch — v0.4, 2026-09-10**

Goal: investigate whether an **autonomous finite-time cascade** can coexist with viscosity in the 3D incompressible unforced Navier–Stokes equations

\[
\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p=0,
\qquad \nabla\cdot u=0,
\qquad \nu>0.
\]

## Claim discipline

This repository **does not claim a solution** of the unforced 3D Navier–Stokes regularity problem. It studies mechanisms suggested by the 2026 OpenAI forced Navier–Stokes and unforced Euler constructions, with explicit separation between source facts, derived lemmas, numerical checks, and open PDE obligations.

## Major correction in v0.4

The earlier working claim that neighboring dyadic charts supply a physical carrier ratio

\[
2^{(1+h)/2}
\]

has been **retracted**. At a fixed physical point the chart scaling of \(\lambda_0\) cancels the apparent \(Q\)-dependence, giving the intrinsic leading carrier scale

\[
\boxed{\Omega_{\rm phys}\asymp q^{-(1+h)/2}.}
\]

See `proofs/chart_invariant_carrier_scale.md`.

Consequently the old design law \(\beta_1+\beta_2=17/12\) is not used as a physical cross-band locking law.

## Current v0.4 local relay architecture

At one physical scale, use the **difference harmonic** of two beta packets:

\[
\boxed{\beta_1=\frac{25}{16},\qquad \beta_2=\frac9{16},\qquad \beta_1-\beta_2=1.}
\]

Thus the desired interaction is

\[
e^{ik\Phi_1}e^{-ik\Phi_2}=e^{ik(\Phi_1-\Phi_2)},
\]

and the child phase is defined by

\[
\boxed{\Phi_c=\Phi_1-\Phi_2.}
\]

The desired difference branch has unit beta and a nonzero projection onto the child's growing polarization. The unwanted sum branch has

\[
\beta_+=\frac{17}{8},
\]

and lies on a strongly viscously decaying branch for the current local witness.

The local picture is therefore

\[
\boxed{
\text{decaying parent}
+\text{ growing catalyst}
\xrightarrow{\text{difference harmonic}}
\text{ growing unit-beta child}.
}
\]

This is a **local same-physical-scale relay module**. It is not yet a cascade to smaller \(q\). The separate inheritance problem is to transport the generated child so that it becomes a parent at a later physical scale \(q_{j+1}<q_j\), where \(\Omega_{\rm phys}\) is intrinsically larger.

## Current proof frontier

Already established at model/geometric level on the research branch:

- beta-dependent viscous envelope and turning point;
- chart-invariant physical carrier scaling;
- translated auxiliary-torus overlap geometry;
- exact difference-phase locking at the formal phase level;
- certified reduced resonance and finite-\(u_*\) persistence for the v0.4 difference design;
- principal growing-polarization lower bound for the desired difference branch;
- conditional exponential suppression of parent-child feedback during tail seeding.

Still open: the full localized curl-generated PDE interaction estimate, exact treatment of every sum-sideband/feedback correction with zero external force, and physical-scale inheritance \(q_j\to q_{j+1}\).

See `STATUS.md`, `ROADMAP.md`, and `proofs/local_beta_relay_lemma.md`.
