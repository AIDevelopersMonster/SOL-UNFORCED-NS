# Note 07 — historical interior-turning search and v0.4 replacement

**Status:** historical record; v0.1–v0.3 physical interpretations are deprecated.

Earlier searches imposed \(\beta_1+\beta_2=17/12\) in order to match a supposed neighboring-band physical carrier ratio. That ratio was later shown to be a chart artefact; see `proofs/chart_invariant_carrier_scale.md`.

The useful lesson that survives is the beta-dependent turning geometry:

\[
x_\beta\to\beta^{-2/3}
\]

in the reduced large-\(u_*\) model, and more generally

\[
x_{\beta,u}
=\frac1{u}\sqrt{(1+u^2)\beta^{-4/3}-1}.
\]

The current v0.4 design does **not** require both beta values below one. It chooses

\[
\beta_1=25/16,
\qquad
\beta_2=9/16,
\qquad
\beta_1-\beta_2=1.
\]

The first parent is deliberately placed to the decaying side of its turning point, while the smaller-beta catalyst and unit-beta child are placed on growing sides. The unwanted sum branch has beta \(17/8\) and is strongly decaying.

Current proof files:

- `proofs/reduced_resonance_certificate.md`
- `proofs/finite_u_relay_persistence.md`
- `proofs/difference_phase_locking.md`
- `proofs/difference_branch_projection.md`

The remaining issue is no longer an interior-turning search. It is the full localized PDE embedding and exact zero-force correction closure.
