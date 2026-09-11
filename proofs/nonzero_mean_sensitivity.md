# Quantitative mean-to-nonzero sensitivity on the forward relay

**Status:** PROVED ABSTRACT DIFFERENCE ESTIMATE; SMALLNESS APPEARS ON THE RETURN WAVE-TO-MEAN LEG, NOT IN THE FIRST MEAN-TO-WAVE LEG.

This note corrects an earlier overstatement. A perturbation of the angular mean acts not only on the already-small correction `z`, but also on the designated primary wave/background linearization. Therefore one must not assign a factor `rho_ell` to the entire map `m -> z(m)`.

Let

\[
z=z(m),\qquad \tilde z=z(\tilde m),\qquad
\delta z=z-\tilde z,\qquad
\delta m=m-\tilde m.
\]

The full nonzero forward equation is

\[
\partial_v z=\mathcal L_m z+f_m+\mathcal B(z,z),
\qquad \mathcal L_m=\mathcal D+\mathcal K_m.
\tag{S1}
\]

On one fixed relay collar, the previously proved full linearized propagator obeys the truncation-independent bound and one angular derivative of parabolic smoothing.

Subtracting the equations for `m` and `tilde m` gives

\[
\partial_v\delta z
=
\bigl(\mathcal L_m+\mathcal B(z,\cdot)+\mathcal B(\cdot,\tilde z)\bigr)\delta z
+(\mathcal L_m-\mathcal L_{\tilde m})\tilde z
+(f_m-f_{\tilde m}).
\tag{S2}
\]

There is also a linear response of the designated primary-wave coefficients to `delta m`; in source exponent notation this is exactly the rule

\[
\boxed{
W_{1/2}\times M_\mu\longrightarrow W_\mu.
}
\tag{S3}
\]

Thus, if the mean perturbation has source order `M_mu`, the induced nonzero perturbation has the **same exponent order** `W_mu`. The correct quantitative estimate is therefore

\[
\boxed{
\|z(m)-z(\tilde m)\|_{W_\mu}
\le
C_{M,I}\|m-\tilde m\|_{M_\mu}
+
C_{M,I}\rho_\ell\|m-\tilde m\|.
}
\tag{S4}
\]

Equivalently, in the fixed packet/characteristic norm used by the local theorem,

\[
\boxed{
\|z(m)-z(\tilde m)\|_X
\le
C_{M,I}\|m-\tilde m\|_Y,
}
\tag{S5}
\]

with a dyadic-uniform constant after the relay design and collar are frozen. Bare mean-to-wave sensitivity is therefore `O(1)`, not `o(1)`.

The small factor appears when this wave variation returns to the angular mean through a conjugate covariance. Pairing `delta z in W_mu` with the designated primary wave `W_{1/2}` and using the source product rule

\[
\boxed{
W_\alpha\times W_{\alpha'}
\longrightarrow M_{\alpha+\alpha'-\kappa_s}
}
\tag{S6}
\]

gives

\[
W_{1/2}\times W_\mu
\longrightarrow
M_{\mu+1/2-\kappa_s}.
\tag{S7}
\]

Hence the full differentiated round trip

\[
\delta m\longrightarrow\delta z
\longrightarrow\delta W
\longrightarrow\delta m'
\]

has the positive factor

\[
\boxed{
\varepsilon^{1/2-\kappa_s}.
}
\tag{S8}
\]

The interactions involving two small corrections contribute an additional `rho_ell` factor. Thus the covariance-mediated return map obeys

\[
\boxed{
\|\delta\mathcal W_{\rm mean}\|_Y
\le
C_MS_*^C
\left(
\varepsilon^{1/2-\kappa_s}
+\rho_\ell
\right)
\|m-\tilde m\|_Y.
}
\tag{S9}
\]

This is the quantitative estimate needed by `mean_nonlinear_block_small_factor_audit.md`.

The important distinction is:

- `m -> z(m)` is bounded/Lipschitz with `O(1)` norm in exponent-normalized variables;
- `m -> z(m) -> covariance mean feedback` is `o(1)` because the return leg gains `1/2-kappa_s`.

No local zero-force closure is claimed here; this file supplies only the nonzero-wave block of the coupled mean estimate.