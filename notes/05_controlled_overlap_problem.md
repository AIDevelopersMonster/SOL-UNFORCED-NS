# Note 05 — controlled-overlap problem

The forced construction deliberately separates labels so that unwanted cross-products vanish by support geometry.

An autonomous relay requires the opposite operation for one designated pair:

\[
(\gamma_j^{(1)},\gamma_j^{(2)})
\longrightarrow
\gamma_{j+1}.
\]

Proposed replacement:

\[
F_\gamma F_{\gamma'}=0
\]

for all non-designated pairs, while one assigned parent pair has a small intentional overlap inside the child seed collar.

## Sparse relay graph

Each child has exactly one permitted incoming relay edge:

\[
P_j^{(1)}+P_j^{(2)}
\to
C_{j+1}.
\]

The core proof obligations are:

1. designated overlap produces the desired child source;
2. non-designated cross-products remain zero;
3. correction steps do not create extra uncontrolled relay edges;
4. localization/curl remainders improve in the wave hierarchy;
5. the difference branch stays in a quantitatively decaying region.

This is now the main architectural target.
