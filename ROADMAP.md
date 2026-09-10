# ROADMAP

## Phase I — exact local difference relay

1. Keep the corrected physical carrier law
   \[
   \Omega_{\rm phys}\asymp q^{-(1+h)/2}
   \]
   separate from dyadic chart bookkeeping.
2. Use the exact local difference relation
   \[
   \beta_1-\beta_2=1
   \]
   and define \(\Phi_c=\Phi_1-\Phi_2\).
3. Certify the envelope resonance in the reduced and exact finite-\(u_*\) models.
4. Prove a uniform lower bound for the desired difference interaction projected onto the child growing polarization.
5. Replace principal waves by the actual localized curl-generated packets and track phase, curl, cutoff, and Leray errors.
6. Prove or kill the **Controlled-Overlap Local Difference-Relay Lemma**.

## Phase II — exact local correction closure

1. Treat the unwanted sum branch \(\beta_+=17/8\) as a strongly damped response.
2. Control parent-child feedback using tail separation.
3. Build a convergent correction scheme for every non-designated sideband and localization residual.
4. Require exact zero-force closure inside the local relay module; flat errors may not simply be left in an external forcing term.
5. Preserve sparse support separation outside designated relay supernodes.

## Phase III — physical-scale inheritance

The local relay at one physical \(q\) does not itself create the next \(q\)-scale. Prove a separate transport/inheritance statement:

\[
C_j(q_j)\longrightarrow P_{j+1}(q_{j+1}),
\qquad q_{j+1}<q_j.
\]

Required checks:

- phase/advection compatibility;
- amplitude and envelope inheritance;
- growth of intrinsic carrier \(\Omega_{\rm phys}(q)\);
- viscosity budget across the transport interval;
- support nesting and absence of backward-heat storage.

## Phase IV — autonomous chain

1. Construct a finite relay chain.
2. Uniformize constants across levels.
3. Prove summability of time intervals and kinetic energy.
4. Pass to an infinite chain if the estimates close.
5. Audit smooth compactly supported initial data.

## Phase V — exact unforced closure

Target:

\[
R(u,p)
=\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p
\equiv0.
\]

No claim of solving the unforced Navier–Stokes problem is allowed before this phase is complete and independently audited.
