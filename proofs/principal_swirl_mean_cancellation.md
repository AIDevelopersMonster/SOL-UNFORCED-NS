# Principal swirl coupling in the mean block is zeroth order

**Status:** PROVED EXACT ALGEBRAIC CANCELLATION.

This note removes the apparent first-order radial derivative from the only visibly `O(1)` base/mean coupling isolated in `full_linear_mean_propagator_reduction.md`.

Source Proposition 8.1 contains in the angular mean equation the linear base/mean terms

\[
\boxed{
(D_r+2/R)(\beta V)+D_z(V\gamma)
}
\tag{SW1}
\]

when the fixed base azimuthal velocity is `V` and the meridional mean correction is `(beta,gamma)`.

The mean correction is exactly divergence-free:

\[
\boxed{
(D_r+1/R)\beta+D_z\gamma=0.
}
\tag{SW2}
\]

Expand (SW1):

\[
\begin{aligned}
(D_r+2/R)(\beta V)+D_z(V\gamma)
={}&V D_r\beta+\beta D_rV+\frac{2V\beta}{R}\\
&+V D_z\gamma+\gamma D_zV.
\end{aligned}
\tag{SW3}
\]

By (SW2),

\[
D_r\beta+D_z\gamma=-\frac{\beta}{R}.
\tag{SW4}
\]

Therefore the two derivatives falling on the unknown cancel exactly:

\[
V(D_r\beta+D_z\gamma)+\frac{2V\beta}{R}
=\frac{V\beta}{R}.
\tag{SW5}
\]

Hence

\[
\boxed{
(D_r+2/R)(\beta V)+D_z(V\gamma)
=\beta\left(D_rV+\frac VR\right)
+\gamma D_zV.
}
\tag{SW6}
\]

This is a **zeroth-order** operator on the mean unknown.

On the reserved mean patch used in source Section 8.6, `G=0` and `V` is the fixed power-law swirl profile. Thus the principal non-small coupling in the angular equation is multiplication by fixed smooth coefficients; it does not consume a radial or torus derivative of the perturbation.

The reciprocal principal coupling in the radial source is

\[
\boxed{\frac{2V}{R}v,}
\tag{SW7}
\]

which is also zeroth order.

Consequently the principal `O(1)` swirl subsystem coupling `(v,beta,gamma)` is an algebraic matrix coupling after the divergence-free constraint is imposed. It can be absorbed into the full linear mean propagator by an ordinary Gronwall/Volterra argument on the bounded characteristic collar.

The remaining derivative-bearing linear pieces all carry one of the already-audited structures:

- `b`-weighted radial transport, with `b=O(epsilon)` on the source shell;
- axial derivatives, which gain one source power;
- viscosity, with source gain `1-2 kappa_s` and favorable parabolic sign when included in the linear evolution;
- characteristic commutators with fixed smooth chart coefficients.

Therefore the obstruction anticipated in `full_linear_mean_propagator_reduction.md` from a first-order `V`-coupling is absent.

The sharp remaining linear issue is now the pressure/viscosity characteristic propagator, not the swirl coupling.