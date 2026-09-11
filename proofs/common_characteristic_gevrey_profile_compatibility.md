# Common characteristic Gevrey profile compatibility

**Status:** PROVED FOR THE LOCAL FORWARD RELAY ARCHITECTURE, SUBJECT ONLY TO THE ALREADY-FROZEN SOURCE PARAMETER INEQUALITIES.

This note discharges the finite compatibility obligations isolated in `coupled_mean_block_small_factor_audit.md`. The point is not to reproduce the source Borel summation. The local unforced architecture uses one frozen relay design, one bounded characteristic collar, finitely many reserved cutoff/bump families, the exact forward nonzero solve, and one exact mean fixed point. In that setting all fixed auxiliary profiles may be chosen in one compactly supported Gevrey class `G^s`, `s>1`.

No infinite sequence of shrinking supports or repeated Gevrey-radius losses is required.

## 1. One Gevrey profile class is available

Fix any

\[
\boxed{1<s<\infty.}
\]

Nontrivial compactly supported `G^s` bump functions exist. Moreover `G^s` is closed under finite sums, products, differentiation, translation, and composition with analytic coordinate changes on compact sets.

Choose once and for all a base radius `lambda_0>0` and build every fixed local auxiliary profile from compactly supported `G^s_{lambda_0}` bumps.

This includes:

- the radial cutoffs used in compact pressure/stress reconstruction;
- the auxiliary-torus localization profiles;
- the three azimuthal and two axial reserved bump families used by the five-dimensional moment correction;
- the finitely many local packet envelopes required by the frozen v0.8 relay.

Because the local relay contains only finitely many such profiles, after reducing the radius once we may place all of them in one common class

\[
\boxed{G^s_{\lambda_1},\qquad \lambda_1>0.}
\tag{P1}
\]

## 2. Exact finite moment constraints can be imposed inside Gevrey

The five-dimensional source correction requires bump profiles with distinct prescribed radial moments so that a fixed Vandermonde-type matrix is invertible.

Take five pairwise disjoint small radial intervals inside the reserved mean patch and choose nonnegative compactly supported Gevrey bumps `psi_j` concentrated near distinct radii `R_j`. Their finite moment matrix

\[
\mathsf M_{aj}=\int R^{p_a}\psi_j(R)\,dR
\]

converges, as the supports shrink, to a diagonal rescaling of the Vandermonde matrix

\[
(R_j^{p_a})_{a,j}.
\]

For distinct `R_j` this limiting matrix is invertible. Invertibility is open, so sufficiently narrow Gevrey bumps have an invertible exact moment matrix.

Therefore every finite linear moment condition used in the pressure/stress and five-dimensional correction can be solved with **exact coefficients inside the Gevrey class**. No analyticity or arbitrary-jet Borel construction is needed.

## 3. Gevrey partitions and localization identities

A finite partition of unity subordinate to a finite open cover may be chosen in `G^s`, `s>1`. Hence all local support decompositions used on one relay collar can be rebuilt with Gevrey cutoffs while retaining the exact algebraic identity

\[
\sum_j\chi_j=1
\]

on the required compact set.

The source inequalities used by the relay are strict after the design and support margins are frozen. Therefore sufficiently small Gevrey perturbations of the original smooth cutoff shapes preserve those inequalities. Exact identities that are linear, such as partition of unity or moment cancellation, are imposed algebraically after the Gevrey bumps are chosen.

Thus replacing arbitrary smooth fixed profiles by Gevrey profiles does not change the frozen v0.8 resonance/action geometry.

## 4. Common characteristic Gevrey norm

Let

\[
t_*=-\varepsilon\partial_T+c_iN_i
\]

and let `D_char` denote the commuting family consisting of radial/axial derivatives, auxiliary-torus derivatives, and powers of `t_*`, with the usual lower-order commutators when chart coefficients are not exactly constant.

For a coefficient `f` define

\[
\boxed{
\|f\|_{Y_{s,\lambda}}
:=
\sum_{n\ge0}
\frac{\lambda^n}{(n!)^s}
\max_{|\alpha|=n}
\|D_{\rm char}^\alpha f\|_{L^\infty}.
}
\tag{P2}
\]

For the nonzero lattice, combine this with the existing analytic harmonic weight:

\[
\boxed{
\|z\|_{X_{s,\lambda,\sigma,1}}
:=
\sum_{\nu\ne0}e^{\sigma|\nu|_1}(1+|\nu|_1)
\|z_\nu\|_{Y_{s,\lambda};\rm pkt}.
}
\tag{P3}
\]

For fixed `s>1`, both `Y` and `X` are Banach algebras after choosing a fixed smaller radius if necessary. Finite-order differential operators map a larger radius continuously into a smaller one.

## 5. Boundedness of the characteristic inverse

`characteristic_fast_time_mean_inverse.md` gives the exact formula

\[
(\mathcal J_iF)(T,y)
=-\frac1\varepsilon\int_T^{T_0}
F\left(\tau,y+\frac{c_i}{\varepsilon}(T-\tau)v_t\right)d\tau.
\]

Auxiliary-torus translations are isometries in Gevrey norms, and `t_*\mathcal J_iF=F`. Radial/axial derivatives commute with the integral. Consequently for every fixed `lambda<=lambda_1`,

\[
\boxed{
\|\mathcal J_iF\|_{Y_{s,\lambda}}
\le C_L\|F\|_{Y_{s,\lambda}}.
}
\tag{P4}
\]

There is no radius loss in this block.

## 6. Boundedness of finite radial and moment reconstructions

Every pressure/stress reconstruction used after the source moment conditions is a fixed radial integral/differential operator on a compact shell bounded away from the axis. Analytic radial weights and finite Gevrey cutoffs preserve `G^s` after at most one fixed radius reduction.

The five-dimensional correction is multiplication by a fixed inverse matrix followed by addition of five fixed Gevrey profiles. Therefore

\[
\boxed{
\|\mathcal C_{\rm mom}F\|_{Y_{s,\lambda_2}}
\le C_M\|F\|_{Y_{s,\lambda_1}},
\qquad
0<\lambda_2<\lambda_1.
}
\tag{P5}
\]

The same estimate holds for differences.

## 7. One-shot radial compactification fits the same radius budget

`gevrey_radial_compactification_remainder.md` proves that for another fixed radius `0<lambda_3<lambda_2`,

\[
\boxed{
\|A_ef\|_{Y_{s,\lambda_3}}
\le
C e^{-cM_{\rm rad}^{1/(2s)}}
\|f\|_{Y_{s,\lambda_2}}.
}
\tag{P6}
\]

Only this one fixed radial loss is paid. Set

\[
\boxed{\lambda_*:=\lambda_3>0.}
\tag{P7}
\]

and formulate the final fixed point in `Y_{s,lambda_*}`.

## 8. The nonzero forward propagator preserves the common Gevrey class

The full nonzero linearized equation is

\[
\partial_vz=(\mathcal D+\mathcal K_m)z+f.
\]

On the frozen collar, all coefficient fields in `D` and `K_m` are in a bounded `Y_{s,lambda_2}` set when `m` lies in a sufficiently small `Y_{s,lambda_*}` ball. Differentiate the equation by `D_char^alpha`. Leibniz gives

\[
D^\alpha(az)
=\sum_{\beta\le\alpha}{\alpha\choose\beta}
(D^\beta a)(D^{\alpha-\beta}z).
\]

The Gevrey factorial weights satisfy the standard convolution inequality, so summing over `alpha` yields

\[
\|az\|_{X_{s,\lambda_*,\sigma,0}}
\le
C\|a\|_{Y_{s,\lambda_2}}
\|z\|_{X_{s,\lambda_*,\sigma,1}}.
\tag{P8}
\]

The existing angular high-mode parabolic smoothing is unaffected by these slow/characteristic derivatives. Applying the same Volterra subdivision argument as in `nonzero_harmonic_forward_reduction.md` therefore gives

\[
\boxed{
\|V_m(v,w)g\|_{X_{s,\lambda_*,\sigma,1}}
\le
K_M(1+(v-w)^{-1/2})
\|g\|_{X_{s,\lambda_*,\sigma,0}}.
}
\tag{P9}
\]

with `K_M` uniform for `m` in the chosen small ball.

Thus the exact map `m -> z(m)` and the sensitivity estimate in `nonzero_mean_sensitivity.md` live in the same final characteristic Gevrey space.

## 9. Size estimates imply Lipschitz estimates for the signed-stress remainder

After the exact principal signed covariance is removed, the source stress remainder is a finite sum of bilinear or quadratic expressions in the current wave correction, reconstruction remainder, and fixed coefficients.

For every bilinear map `B` bounded on the common Gevrey algebra,

\[
B(x,x)-B(y,y)
=B(x-y,x)+B(y,x-y),
\]

so

\[
\boxed{
\|B(x,x)-B(y,y)\|
\le C(\|x\|+\|y\|)\|x-y\|.
}
\tag{P10}
\]

The source Proposition 9.6 exponent bookkeeping gives a positive `+0.17` gain for precisely these post-principal stress remainders. Because the coefficient maps are fixed and the ball radii obey the same source size classes, the difference estimate carries the same positive exponent:

\[
\boxed{
\|\mathcal R_{\rm stress}(m)-\mathcal R_{\rm stress}(\tilde m)\|_{Y_{s,\lambda_*}}
\le
C_MS_*^C\varepsilon^{0.17}
\|m-\tilde m\|_{Y_{s,\lambda_*}}.
}
\tag{P11}
\]

No new derivative loss appears.

## 10. Finite radius budget

The complete local map uses only finitely many radius-losing operations. Choose in advance

\[
\lambda_0>\lambda_1>\lambda_2>\lambda_* >0.
\]

All fixed profile construction occurs at `lambda_0`; finite pressure/moment reconstruction lands at `lambda_2`; the one-shot radial Fourier estimate lands at `lambda_*`; characteristic integration and the exact forward fixed points are then carried out entirely at `lambda_*`.

Therefore there is no sequence

\[
\lambda_0>\lambda_1>\cdots\downarrow0.
\]

This is exactly the feature that distinguishes the present forward local closure from the source's all-orders finite-stage/Borel architecture.

## 11. Compatibility theorem

For every frozen admissible v0.8 relay design and every `s>1`, the fixed local source profiles may be chosen so that there exists a common positive radius `lambda_*>0` with the following properties:

1. all fixed cutoffs and reserved moment profiles belong to `G^s`;
2. all exact finite moment and partition identities are preserved;
3. pressure, stress, Haar projection, and five-dimensional moment reconstruction are bounded on the corresponding characteristic Gevrey scale after finitely many preassigned radius losses;
4. the exact characteristic inverse is bounded with no radius loss;
5. the one-shot radial compactification remainder is `o(1)` after one fixed radius loss;
6. the nonzero full-linearized forward propagator and `m -> z(m)` sensitivity estimate hold in the same final space;
7. the signed-stress post-principal remainder has a Lipschitz estimate with the same positive source exponent gain as its size estimate.

Hence all four compatibility obligations from Section 9 of `coupled_mean_block_small_factor_audit.md` are discharged.

The local frontier is therefore no longer Gevrey-profile compatibility. The next step is to combine this theorem with the block small-factor audit into the final unconditional Banach contraction theorem for the angular mean.