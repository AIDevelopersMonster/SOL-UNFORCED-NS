# Note 03 — retracted chart-frequency obstruction

**Status: RETRACTED AS A PHYSICAL OBSTRUCTION.**

The bootstrap argument treated

\[
Q=2^{-\ell},\qquad \varepsilon=Q^h,\qquad k\sim\varepsilon^{-1/2}
\]

and inferred a physical carrier

\[
Q^{-1/2}k\sim Q^{-(1+h)/2},
\]

leading to the supposed neighboring-chart ratio \(2^{(1+h)/2}\).

That comparison omitted the chart scaling of the source shear parameter \(\lambda_0\), and therefore of \(B_s\). With the full source normalization,

\[
k_QB_{s,Q}
=\frac{\sqrt{\lambda_{0,Q}}}{\sqrt{\varepsilon_Q}(1+u_*^2)^{3/4}},
\]

and the \(Q\)-dependence cancels after conversion back to physical derivatives. See `proofs/chart_invariant_carrier_scale.md`.

Thus two overlapping dyadic charts at the same physical point do **not** define distinct physical carrier scales merely because their chart labels differ.

## Replacement design constraint

For collinear principal carriers at one physical point, a unit-beta child must satisfy the harmonic relation

\[
\epsilon_1\beta_1+\epsilon_2\beta_2=1,
\qquad \epsilon_j\in\{\pm1\}.
\]

The current v0.4 design uses the difference branch

\[
\boxed{\beta_1-\beta_2=1}
\]

with \(\beta_1=25/16\), \(\beta_2=9/16\).

The true increase of physical carrier occurs when the physical variable \(q\) decreases, through

\[
\Omega_{\rm phys}(q)\asymp q^{-(1+h)/2}.
\]

Accordingly, cross-\(q\) inheritance is now a separate proof obligation.
