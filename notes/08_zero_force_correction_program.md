# Note 08 — zero-force correction program after low-mode audit

The corrected v0.4 relay has a strongly damped unwanted sum harmonic

\[
\beta_+=17/8,
\]

with a bounded local forward inverse. That remains valid; see `proofs/sum_sideband_local_inverse.md`.

However, the next low-mode audit exposed a more delicate fact: the correction lattice is **not forward-stable as a whole**. In particular, the parent-child/catalyst feedback mode

\[
(1,-2)
\]

is uniformly growing on the certified relay bracket. See `proofs/feedback_mode_instability_and_compact_inverse_obstruction.md`.

Therefore the earlier naive target

\[
Z=\mathcal T(Z)
\]

with a single stable inverse for every non-designated mode was too optimistic.

## 1. Revised linear decomposition

Write the correction space schematically as

\[
\mathfrak X
=\mathfrak X_s\oplus\mathfrak X_u\oplus\mathfrak X_c,
\]

where:

- `X_s` contains uniformly forward-stable nonzero lattice modes;
- `X_u` contains finitely many low modes with positive local growth, including `(1,-2)`;
- `X_c` contains mean/neutral and endpoint compatibility directions.

The high harmonic tail is still favorable: lattice separation plus quadratic viscous damping shows that only finitely many low nonzero modes can fail to be strongly stable.

## 2. One-sided dichotomy inverses

For a stable scalar coordinate

\[
z'=a(v)z+f,
\qquad a\le-\gamma<0,
\]

use the forward inverse with entrance condition `z(v_-)=0`.

For an unstable scalar coordinate

\[
z'=a(v)z+f,
\qquad a\ge\gamma>0,
\]

use the terminal/backward inverse with `z(v_+)=0`.

Both are bounded by `gamma^{-1}` in the corresponding direction.

But these inverses do **not** automatically yield a correction vanishing at both ends of the collar.

## 3. Exact compact-support compatibility

For

\[
z'=a(v)z+f(v)
\]

on `[v_-,v_+]`, imposing

\[
z(v_-)=z(v_+)=0
\]

requires the exact moment condition

\[
\boxed{
\int_{v_-}^{v_+}
\exp\left(-\int_{v_-}^{w}a(s)\,ds\right)f(w)\,dw=0.
}
\]

This condition is generic neither for stable nor unstable forcing. Thus exact zero-force closure contains a finite-dimensional solvability problem that cannot be removed by saying that a tail is exponentially small.

## 4. Revised nonlinear architecture

The local residual equation should be organized as a Lyapunov-Schmidt / exponential-dichotomy system.

First project onto the complementary stable/unstable range and solve there using the one-sided inverses. Then collect the resulting finite family of endpoint/mean compatibility functionals

\[
\mathcal M_j(\mathbf p,Z)=0,
\qquad j=1,\dots,N_c,
\]

where `p` denotes adjustable relay parameters such as relative pulse translations, amplitudes/phases, or amplitudes of deliberately added compensating packets.

Only after those finite equations are solved exactly should one run a contraction for the remaining infinite-dimensional correction.

Schematic form:

\[
Z=\mathcal G_{\mathbf p}
\big(R_0+\mathcal N(Z)\big),
\]

subject to

\[
\boxed{
\mathcal M(\mathbf p,Z)=0.
}
\]

The operator `G_p` is the forward/backward dichotomy inverse on the complement of the compatibility block.

## 5. Small parameters that remain useful

The following gains still survive the revised architecture:

1. the first sum-sideband inverse has a fixed stable gap;
2. curl/localization remainders gain at least `epsilon^(1/2-kappa_s)` relative to the principal relay source;
3. parent-child feedback is generated in Gaussian tails and therefore carries an additional `exp(-c S_*)` factor;
4. high lattice harmonics become increasingly viscously stable.

These gains should make the infinite-dimensional complement contractive. The new difficulty is the finite compatibility system, not the high-mode tail.

## 6. Next theorem-level target

### Finite compatibility transversality lemma

Choose a minimal set of adjustable relay parameters `p_1,...,p_m` and a matching finite set of compatibility moments `M_1,...,M_m`. Prove that at the reference relay configuration

\[
\boxed{
\det\left(\frac{\partial M_i}{\partial p_j}\right)\ne0.
}
\]

Then the implicit-function theorem can solve the exact endpoint/mean constraints simultaneously with the small nonlinear correction.

This is now the correct local zero-force closure target.

## Warning

The forced source construction does not require this finite compatibility solve because exponentially flat residuals can be retained in the prescribed external force. The compatibility system is therefore genuinely new work for SOL-UNFORCED-NS.
