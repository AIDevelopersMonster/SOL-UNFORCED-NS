# Physical carrier scaling — correction notice

**Status:** the original bootstrap derivation in this file is retracted.

The earlier argument held the chart shear parameter \(\lambda_0\) fixed while changing the dyadic chart scale \(Q\). That is not the source normalization at a fixed physical point.

The corrected derivation is in

`proofs/chart_invariant_carrier_scale.md`.

Its governing conclusion is

\[
\boxed{
\Omega_Q
=
\frac{q^{-(1+h)/2}\sqrt{\lambda_{0,\rm prof}}}
{(1+u_*^2)^{3/4}},
}
\]

so the leading physical carrier is independent of the overlapping chart label \(Q\) and grows intrinsically only as the physical variable \(q\) decreases.

Accordingly,

\[
2^{(1+h)/2}
\]

must **not** be used as a neighboring-chart physical relay ratio.
