# Research protocol

## 1. Separate four levels of status

Every mathematical statement should be marked, where relevant, as one of:

- **SOURCE** — directly stated in a cited paper.
- **DERIVED** — obtained by an explicit derivation from source definitions.
- **NUMERICAL** — checked computationally for given parameters.
- **CONJECTURAL** — mechanism or lemma not yet proved.

Do not silently upgrade one level to another.

## 2. No theorem without proof

A result enters `proofs/` as a theorem only after the proof is complete enough for independent checking.

Before that, use:

- Candidate lemma
- Proof obligation
- Working proposition
- Numerical witness

## 3. Publication threshold

A technical preprint becomes justified when the project has at least one independent result such as:

- a proved local relay lemma;
- a proved obstruction excluding a natural class of autonomous viscous cascades;
- a rigorous scale theorem reducing the problem to a new finite set of inequalities.

A Millennium-problem claim requires a much higher threshold: exact closure, full regularity/energy audit, independent proof review, and ideally formal verification of the final theorem statement.

## 4. Reproducibility

Every numerical witness must have:

- exact rational parameters when possible;
- a script;
- printed residuals;
- a machine-readable row in `results/`.
