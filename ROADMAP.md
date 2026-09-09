# ROADMAP

## Phase I — local mechanism

1. Re-audit all scale definitions against the primary OpenAI forced Navier–Stokes paper.
2. Formalize the β-generalized phase and damping model.
3. Derive the quadratic interaction after Leray projection for unequal β.
4. Replace plane waves by localized curl-generated packets.
5. Quantify:
   - desired sum branch,
   - undesired difference branch,
   - phase defects,
   - curl remainders,
   - cutoff errors.
6. Prove or disprove the Controlled-Overlap Local β-Relay Lemma.

## Phase II — sparse relay graph

If Phase I succeeds:

1. Replace complete label separation by a sparse controlled-overlap graph.
2. Assign one permitted parent pair to each child.
3. Prove all non-designated cross-interactions remain exactly zero by support separation.
4. Bound all designated relay interactions.
5. Check that correction steps do not create secondary uncontrolled relay edges.

## Phase III — autonomous chain

1. Construct a finite relay chain.
2. Uniformize constants across levels.
3. Prove summability of time intervals and energy.
4. Pass to an infinite chain.
5. Audit smoothness of initial data and compact support.

## Phase IV — exact unforced closure

Target:
\[
R(u,p)
=
\partial_tu+(u\cdot\nabla)u-\nu\Delta u+\nabla p
\equiv0.
\]

No publication claim of a Navier–Stokes solution is allowed before this phase is complete and independently audited.
