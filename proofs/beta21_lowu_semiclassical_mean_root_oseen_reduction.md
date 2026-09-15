# Semiclassical whole-space mean-root Oseen reduction for the low-`u` cell

**Status:** PROVED FUNCTIONAL-ANALYTIC REDUCTION AND POSITIVE-EXPONENT BUDGET / SOURCE-SPECIFIC JET INSERTION STILL OPEN.  The designated beta-zero root in the low-`u` boundary-layer architecture is an angular mean mode of physical size `O(sqrt(epsilon))`, but it is rapidly oscillatory in the reconstructed radial direction.  Consequently the previously proved fixed physical `H^{m_0}` Oseen estimate cannot simply be reused with this root inserted into the background coefficient: high ordinary derivatives of the root carry powers of the physical carrier frequency.

This note introduces the natural whole-space semiclassical `W^{m,p}` norm with `p>3`.  In that norm the designated root is a uniformly admissible Oseen coefficient, the whole-space Leray projector remains bounded, the mean-root transport is an `O(1)` first-order operator, and the nonlinear Sobolev-algebra loss leaves a strictly positive source exponent.  The preferred concrete choice below is `p=6`.

The remaining task is to pin the abstract semiclassical root-jet bounds to the exact source curl/frame realization and to couple the resulting mean norm to the nonzero orbit fixed point.  No exact reset cell or blowup theorem is claimed here.

## 1. Semiclassical scale

Let

\[
\boxed{h_\ell:=\sqrt{\varepsilon_\ell}.}
\tag{SO1}
\]

For `1<p<infty` and an integer `m>=0`, define

\[
\boxed{
\|f\|_{W^{m,p}_{h}}
:=
\sum_{|\alpha|\le m}
\|(h\nabla)^\alpha f\|_{L^p(\mathbb R^3)}.
}
\tag{SO2}
\]

The viscosity term becomes

\[
\varepsilon\Delta=h^2\Delta,
\]

so this is the scale naturally adapted to the physical parabolic operator.

For the auxiliary coefficient lattice, define the phase-adapted norm

\[
\boxed{
\|a\|_{\mathfrak M^{p}_{\sigma,m,h}}
:=
\sum_{k\in\mathbb Z^2}
 e^{\sigma|k|_1}
 \|M_{\ell,k}a_k\|_{W^{m,p}_{h}}.
}
\tag{SO3}
\]

The physical modulation `M_{ell,k}` is the same exact reconstruction modulation used in `phase_adapted_whole_space_leray_intertwining.md`.

## 2. Whole-space Leray projector

For every `1<p<infty`, the whole-space Leray projector is a matrix of the identity and Riesz-transform products and is bounded on `L^p`.  It commutes with ordinary derivatives and therefore with the scaled derivatives `h partial_j`.

Consequently its exact conjugate on mode `k`,

\[
\mathbb P_{\ell,k}^{cov}
=M_{\ell,k}^{-1}\mathbb P M_{\ell,k},
\]

obeys

\[
\boxed{
\|\mathbb P_{\ell,k}^{cov}a_k\|_{W^{m,p}_{h,\ell,k}}
\le C_p\|a_k\|_{W^{m,p}_{h,\ell,k}}
}
\tag{SO4}
\]

where the mode norm is the physical `W_h^{m,p}` norm after modulation.  Summing with the positive lattice weights gives

\[
\boxed{
\|\mathbb P_{coeff,\ell}a\|_{\mathfrak M^{p}_{\sigma,m,h}}
\le C_p\|a\|_{\mathfrak M^{p}_{\sigma,m,h}}.
}
\tag{SO5}
\]

The constant is independent of the dyadic level, auxiliary index and reconstructed covector.

## 3. Semiclassical Sobolev embedding and product loss

For `p>3` and `m` large enough for the usual integer Sobolev product calculus, scaling `x=h y` gives

\[
\boxed{
\|f\|_{L^\infty}
\le C_{m,p}h^{-3/p}\|f\|_{W^{m,p}_{h}}.
}
\tag{SO6}
\]

The same scaling and Leibniz rule yield

\[
\boxed{
\|fg\|_{W^{m,p}_{h}}
\le
C_{m,p}h^{-3/p}
\|f\|_{W^{m,p}_{h}}
\|g\|_{W^{m,p}_{h}}.
}
\tag{SO7}
\]

Because the phase indices add exactly and

\[
e^{\sigma|k+j|_1}
\le e^{\sigma|k|_1}e^{\sigma|j|_1},
\]

the same estimate holds in the analytic coefficient lattice:

\[
\boxed{
\|ab\|_{\mathfrak M^p_{\sigma,m,h}}
\le
C_{m,p}h^{-3/p}
\|a\|_{\mathfrak M^p_{\sigma,m,h}}
\|b\|_{\mathfrak M^p_{\sigma,m,h}}.
}
\tag{SO8}
\]

Thus the price of using a whole-space `L^p` algebra is an explicit power `h^{-3/p}`, not an uncontrolled high-frequency coefficient constant.

## 4. Physical scale of the designated root

The source normalization gives

\[
\sqrt\varepsilon\,kB_s=O(1).
\]

The designated beta-zero root has physical amplitude

\[
\boxed{\|M_{des}\|_{L^\infty}=O(h).}
\tag{SO9}
\]

In the boundary-layer geometry its normalized radial phase increment is proportional to

\[
\delta_S=\kappa/S.
\]

Therefore its reconstructed physical phase satisfies at principal order

\[
\boxed{
h|\nabla\theta_M|=O(\delta_S)=O(S^{-1}).}
\tag{SO10}
\]

After the exponential phase is factored out, the source envelope/frame coefficients vary only on the slow packet scale.  The target source-specific jet estimate is therefore

\[
\boxed{
\|(h\nabla)^a M_{des}\|_{L^\infty}
\le C_a h(1+S^{-a})
}
\tag{SO11}
\]

for every fixed `a<=m+1`, up to the already audited positive source powers and fixed polynomial `S` factors from slow coefficient jets.

Equation (SO10) is exact at frozen principal level; proving (SO11) for the complete curl/localized root is the remaining source-embedding step.

## 5. Transport by the designated root

Consider the projected mean linearization contribution

\[
\mathcal L_M m
:=-\mathbb P\left[(M_{des}\cdot\nabla)m+(m\cdot\nabla)M_{des}\right].
\]

Write

\[
\nabla=h^{-1}(h\nabla).
\]

The first term has coefficient `M_des/h=O(1)` by (SO9).  Applying scaled derivatives and using the divergence-free principal transport structure gives a standard semiclassical transport commutator in which each derivative falling on `M_des` gains one factor from (SO11).  Hence

\[
\boxed{
\|\mathcal L_Mm\|_{W^{m-1,p}_{h}}
\le C_m\|m\|_{W^{m,p}_{h}},
}
\tag{SO12}
\]

with a constant independent of `S` and `ell` once (SO11) is inserted.

The stretching term is smaller at principal root scale because

\[
\|\nabla M_{des}\|_\infty
=O(S^{-1})
\tag{SO13}
\]

by (SO9)--(SO10).

In coefficient space, multiplication by the root shifts auxiliary index by

\[
M=(1,-2),
\qquad |M|_1=3.
\]

Therefore the analytic lattice penalty is the fixed factor

\[
\boxed{e^{3\sigma_0},}
\tag{SO14}
\]

not `e^{cS}`.  At `sigma_0=0.005` this is an innocuous absolute constant.

## 6. Semiclassical whole-space Oseen estimate

Let the mean background be

\[
U_{bg}=U_{base}+M_{des}.
\]

The fixed slow base is handled as in `global_fixed_order_leray_oseen_propagator.md`.  Its principal divergence-free transport is skew/conservative at the undifferentiated level, and fixed derivatives produce only bounded slow-base commutators.

Add the root operator (SO12) to the full linear generator rather than treating it perturbatively.  Standard forward parabolic/transport estimates in integer `W^{m,p}` then give the target bound

\[
\boxed{
\|\mathcal V_{M}(s,s_0)f\|_{
\mathfrak M^p_{\sigma_0,m,h}}
\le K_{p,m,I}
\|f\|_{
\mathfrak M^p_{\sigma_0,m,h}}
}
\tag{SO15}
\]

on one bounded normalized collar, with `K_{p,m,I}` independent of `S,ell`, provided the source-specific jet estimate (SO11) holds.

The viscous term has favorable sign/sectorial smoothing and is not inverted backward in time.

This is the exact linear theorem still to be written against the full source coefficient formula; the functional-analytic scaling shows that no high-derivative frequency obstruction remains once the correct norm is used.

## 7. Residual mean nonlinearity

Let the residual mean correction have source size

\[
\|m_{corr}\|
\sim \varepsilon^{1-\kappa_s}
=h^{2-2\kappa_s}
\]

up to fixed powers of `S`.

A quadratic convective term contains one physical derivative, hence (SO8) gives the worst semiclassical factor

\[
h^{-1-3/p}.
\]

Therefore

\[
\boxed{
\|(m_{corr}\cdot\nabla)m_{corr}\|
\lesssim
S^A
h^{3-4\kappa_s-3/p}.
}
\tag{SO16}
\]

For every

\[
p>3
\]

the exponent is strictly positive.  With the concrete choice

\[
\boxed{p=6,}
\tag{SO17}
\]

it is

\[
\boxed{
3-4\kappa_s-\frac12
=2.5-4\kappa_s
=2.49996>0.
}
\tag{SO18}
\]

Thus the residual mean quadratic map remains strongly perturbative.

## 8. Orbit covariance forcing

The designated beta-one/beta-two waves remain of order `W_{1/2}`.  Their genuine conjugate covariance lies in

\[
M_{1-\kappa_s}.
\]

The `O(S)` orbit cardinality and fixed derivatives add only fixed powers of `S`; the analytic lattice budget for generated `rM` modes was proved separately in `beta21_lowu_mean_orbit_harmonic_split_and_covariance_audit.md`.

Passing from the source covariance estimate to the semiclassical `W^{m,6}` mean norm costs at worst the same explicit fixed scaling powers already displayed above.  The available mean exponent `1-kappa_s` remains positive after any single algebra/derivative loss required by the local Duhamel map.

The exact source-level inequality should be recorded in the final coupled theorem as

\[
\boxed{
\|F_{cov}^{orb}\|_{
\mathfrak M^6_{\sigma_0,m,h}}
\le
S^A\varepsilon^{\eta_{cov}}
+S^Ae^{-cS}
}
\tag{SO19}
\]

for one explicit `eta_cov>0`.  Determining the sharp `eta_cov` from the existing source packet seminorm is bookkeeping, not a new principal obstruction.

## 9. Coupling back to the nonzero orbit

The same designated root that enters the mean generator produces the intended order-one translations

\[
M+C_j\to C_{j+1},
\qquad
M+Q_n\to Q_{n+1}.
\]

These terms are already part of the nonzero designated shift generator.  A residual mean perturbation enters the nonzero equation with its old source gain; the additional `W_h^{m,6}` scaling changes this only by fixed explicit powers of `h` and polynomial powers of `S`.

The target mean-to-wave-to-mean Lipschitz factor therefore retains a positive epsilon exponent.  This must be verified in the final common graph norm, but no exponentially large lattice or carrier factor is introduced by `M_des` itself.

## 10. Remaining exact obligations

The oscillatory-root linear problem has been reduced to four source-specific checks:

1. prove (SO11) for the exact localized/curl beta-zero root at `delta_S=kappa_S/S`;
2. write the projected mean equation in the phase-adapted semiclassical `W^{m,6}` coefficient norm and prove (SO15) directly;
3. translate the existing covariance and mean-to-wave-to-mean source estimates into that norm, recording an explicit positive `eta_cov` and Lipschitz exponent;
4. combine this mean contraction with the designated nonzero orbit/complement propagator and then apply the already proved principal `C^1` transversality.

No ordinary fixed-`H^m` estimate should be cited for the root-augmented mean background without this rescaling.

## 11. Consequence

The high ordinary derivatives of the designated angular-mean root are a real issue, but they do not produce a new action or Cauchy obstruction.  In the natural parabolic scale

\[
\boxed{h=\sqrt\varepsilon,}
\]

the root has `O(h)` amplitude and `O(S^{-1})` scaled carrier increment.  Whole-space `W^{m,p}`, `p>3`, gives a uniform linear Oseen framework and leaves a strictly positive nonlinear smallness exponent.

The next attack is the exact source jet estimate (SO11), followed by the common coupled graph norm.
