# LOWU-BOUNDARY-LAYER-ORBIT v0.1

Publication package for the low-`u` boundary-layer orbit mechanism in `SOL-UNFORCED-NS`.

## Files

- `MANUSCRIPT_EN.md` — English publication candidate.
- `MANUSCRIPT_RU.md` — Russian companion version.
- `PUBLICATION_AUDIT.md` — claim ledger, corrected theorem status, open obligations, and release checklist.

## Frozen research scope

The manuscript is based on the theorem chain through research commit

`9add88598582959095c418a252a5d0d13ed9596f`

and additionally uses the limiting analytic-tail invertibility theorem

`4451d359a4e9d9b114476808ca6cb2d6bd744bde`.

Later research commits must not silently change this manuscript.  Any material change to the claim set requires a new publication version.

## Central publication claim

The paper derives and audits a low-`u` beta-(2,1) boundary-layer Fourier-orbit mechanism, proves a compact-primary-bank exact-reset obstruction, and formulates the corrected core-plus-analytic-tail local target.  It also proves limiting analytic-tail spectral invertibility in the weighted Wiener lattice.

It does **not** claim an exact finite-`S` full-state reset, an infinite cascade, an unforced Navier–Stokes singularity, or a Millennium Prize solution.

## Next research theorem

The active research branch should next prove the finite-`S` variable-coefficient core+tail Lyapunov–Schmidt theorem

\[
\mathcal P_S(U_{core,S}+z_{tail,S})
=U_{core,S}+z_{tail,S}.
\]

That theorem belongs to a later publication version unless it is intentionally folded into v0.2 after a new audit.
