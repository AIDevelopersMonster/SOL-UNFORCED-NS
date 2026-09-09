# Note 02 — backward-heat barrier

For the linear heat part

\[
\partial_tu-\nu\Delta u=0,
\]

a Fourier mode evolves as

\[
\widehat u(K,t)
=
e^{-\nu |K|^2t}
\widehat u(K,0).
\]

To prescribe a high-frequency seed \(a\) at a later time \(t_j\) by storing it at the same frequency in the initial data would require

\[
\widehat u(K,0)
=
e^{+\nu|K|^2t_j}a.
\]

Thus high-frequency future seeds cannot be cheaply hidden in \(u_0\) in the same backward-history spirit as an inviscid construction.

## Research consequence

A high-frequency child should be generated **late and forward in time** by nonlinear interaction.

## Status

**DERIVED from the heat semigroup.**

This is a mechanism obstruction, not a theorem excluding all autonomous cascades.
