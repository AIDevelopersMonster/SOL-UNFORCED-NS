# Proof obligation — Controlled-Overlap Local Difference-Relay Lemma

## Corrected v0.4 target

Let \(U\) be the local background flow in a source-type pulse cell. Construct two localized divergence-free parent packets \(W_1,W_2\) with

\[
\beta_1=25/16,
\qquad
\beta_2=9/16,
\]

one deliberately permitted auxiliary-support overlap, and define the desired child phase by

\[
\Phi_c=\Phi_1-\Phi_2.
\]

The target is to prove that the difference-harmonic part of

\[
\mathbb P\big[(W_1\cdot\nabla)W_2+(W_2\cdot\nabla)W_1\big]
\]

has the form

\[
S_c+E
\]

where:

1. \(S_c\) has the exact child phase \(\Phi_c\) and unit-beta principal normal;
2. its projection onto the child growing polarization satisfies
   \[
   |\Pi_+S_c|\ge c_0A_1A_2\Omega
   \]
   with a scale-uniform \(c_0>0\);
3. the unwanted sum harmonic has \(\beta_+=17/8\) and is solved as a strongly damped correction;
4. curl, cutoff, phase-transport and Leray remainders lie in a strictly improved class;
5. all non-designated label pairs remain support-disjoint;
6. the entire local correction scheme closes with **zero external force**.

## Layers already established

- chart-invariant physical carrier law;
- beta-envelope/turning-point formula;
- translated overlap geometry;
- exact difference-phase locking at phase level;
- certified reduced resonance;
- finite-u envelope persistence;
- principal growing-polarization nondegeneracy;
- conditional tail-feedback suppression.

## Still missing

The decisive missing step is the full **localized curl-generated interaction estimate plus exact correction closure**. Until this is proved, the local autonomous relay remains unproved.

A further independent problem remains after local closure: transport the generated child from \(q_j\) into a valid parent at a later physical scale \(q_{j+1}<q_j\).
