# Cauchy/curl realization of the designated beta-zero mean root

**Status:** PROVED LOCAL PRINCIPAL CURL REALIZATION + SEMICLASSICAL ERROR REDUCTION / FULL SOURCE-CHART INSERTION STILL TO BE PINNED.  The low-`u` boundary-layer cell requires a pre-existing beta-zero mean root

\[
M=P-2C
\]

on the incoming physical Cauchy slice.  Unlike the rejected future-time gate controls, such a field is legitimate initial data.  This note gives an exact divergence-free localized curl realization whose principal amplitude, phase and polarization are precisely those used in the boundary-layer Poincare map.

The key boundary-layer scale is

\[
h:=\sqrt\varepsilon,
\qquad
\delta_S=\kappa/S.
\]

The root phase has zero angular frequency but a nonzero radial reconstructed covector of size

\[
|\Xi_M|\asymp (hS)^{-1}.
\]

Consequently a standard oscillatory vector-potential construction has a localization remainder smaller than the desired `O(h)` root by the factor `hS->0` along the source hierarchy.

No exact reset cell or global cascade is claimed here.

## 1. Root phase and carrier scale

Let `Theta_P,Theta_C` be the physical phases of the beta-two parent and beta-one catalyst at the incoming section.  Define

\[
\boxed{\Theta_M:=\Theta_P-2\Theta_C.}
\tag{CR1}
\]

Because

\[
\beta(P)-2\beta(C)=2-2=0,
\]

`Theta_M` has no physical angular oscillation.  Its remaining fast covector is the radial/normal mismatch of the two close phases.

At the low-`u` boundary-layer point the reduced slope separation is

\[
\delta_S=\kappa/S.
\]

The source normalization proves

\[
\boxed{h\,kB_s\asymp1}
\tag{CR2}
\]

uniformly on a fixed compact slow set.  The beta-zero root normal coefficient is a fixed nonzero multiple of the slope difference, hence on a sufficiently small strict core

\[
\boxed{
\frac{c_-}{S}
\le h|\Xi_M|
\le \frac{c_+}{S},
\qquad
\Xi_M:=\nabla\Theta_M,
}
\tag{CR3}
\]

for fixed constants `0<c_-<=c_+<infty` and all sufficiently large levels.

Equivalently,

\[
\boxed{|\Xi_M|\asymp (hS)^{-1}.}
\tag{CR4}
\]

Since `h` decreases exponentially in the dyadic level while `S` grows polynomially, the root still has a genuinely large physical radial frequency even though its normalized separation is only `O(S^{-1})`.

## 2. Principal root polarization

The beta-zero mean-root polarization audit gives, in the frozen source frame,

\[
\boxed{
b_M=-S_MK+c_0R_MN,}
\tag{CR5}
\]

with fixed nonzero tangential/axial components and no radial component.  The beta-zero phase normal is radial at principal order. Therefore

\[
\boxed{b_M\cdot\Xi_M=0}
\tag{CR6}
\]

at the frozen principal point.

On the strict physical core the exact frame and phase vary smoothly.  Replacing `b_M` by its pointwise orthogonal projection to `Xi_M^perp` changes it only by the already allowed `O(S^{-1})`/slow-source perturbation.  Denote this exact smooth transverse polarization by

\[
\widetilde b_M,
\qquad
\widetilde b_M\cdot\Xi_M=0.
\tag{CR7}
\]

## 3. Exact vector potential

Choose a fixed smooth physical cutoff `chi` supported strictly inside the relay core and equal to one on the smaller orbit interaction core.  Let `a_M` be the normalized complex root amplitude selected by the principal Poincare fixed point.

Define the complex vector potential

\[
\boxed{
A_M
:=
\chi\,
\frac{h a_M}{i|\Xi_M|^2}
(\Xi_M\times\widetilde b_M)
 e^{i\Theta_M}.
}
\tag{CR8}

The physical real root is

\[
\boxed{
M_{des}:=2\Re(\nabla\times A_M).
}
\tag{CR9}

By construction,

\[
\boxed{\nabla\cdot M_{des}=0}
\tag{CR10}
\]

exactly, including the cutoff region.  No post-hoc Leray projection is required to make the incoming root divergence free.

## 4. Principal curl term

When the derivative in the curl hits the exponential,

\[
\nabla e^{i\Theta_M}=i\Xi_Me^{i\Theta_M}.
\]

Using

\[
\Xi\times(\Xi\times b)
=\Xi(\Xi\cdot b)-|\Xi|^2b
=-|\Xi|^2b
\]

for `b perpendicular Xi`, the oscillatory curl gives, up to the sign fixed in (CR8),

\[
\boxed{
\nabla\times A_M
=
\chi h a_M\widetilde b_Me^{i\Theta_M}
+R_M^{curl}.
}
\tag{CR11}
\]

Thus the desired root has the physical size

\[
\boxed{M_{des}=O(h)=O(\sqrt\varepsilon).}
\tag{CR12}
\]

This is exactly source order `M_{1/2}`.

## 5. Localization remainder

The vector-potential prefactor has size

\[
\left|
\frac{ha_M}{|\Xi_M|^2}
(\Xi_M\times\widetilde b_M)
\right|
\lesssim
\frac{h}{|\Xi_M|}.
\]

By (CR4),

\[
\boxed{
\frac{h}{|\Xi_M|}
\asymp h^2S.
}
\tag{CR13}
\]

A derivative falling on the fixed cutoff, the slowly varying frame or the slowly varying exact polarization therefore contributes

\[
\boxed{
|R_M^{curl}|
\le C h^2S\,\operatorname{poly}(S)
}
\tag{CR14}
\]

at fixed source derivative order.  Relative to the principal root amplitude `h`,

\[
\boxed{
\frac{|R_M^{curl}|}{h}
\le C hS\,\operatorname{poly}(S)
\longrightarrow0.
}
\tag{CR15}
\]

because `h=sqrt(epsilon)` decays exponentially in the band level whereas all source/localization losses recorded for the fixed derivative order are polynomial in `S`.

Thus exact divergence-free localization does not alter the principal root amplitude or phase at leading order.

## 6. Semiclassical root jets

Let

\[
D_h:=h\nabla.
\]

When `D_h` hits the oscillatory exponential it contributes

\[
h\Xi_M=O(S^{-1}).
\]

When it hits a fixed/slow cutoff or frame coefficient it contributes an additional factor `h` times an already polynomial source jet.  Repeated Leibniz expansion therefore gives, for every fixed integer `a`,

\[
\boxed{
\|D_h^aM_{des}\|_{L^\infty}
\le
C_a h\,\operatorname{poly}(S)
\left(1+S^{-a}\right).
}
\tag{CR16}
\]

More sharply, the pure phase part contributes

\[
\boxed{
\|D_h^aM_{des}^{principal}\|_\infty
\le C_a hS^{-a}.
}
\tag{CR17}
\]

Equations (CR16)--(CR17) are the jet input required by `beta21_lowu_semiclassical_mean_root_oseen_reduction.md`.

## 7. Principal self-advection

Because the principal polarization is transverse,

\[
\widetilde b_M\cdot\Xi_M=0,
\]

the plane-wave self-advection vanishes.  The same holds for the conjugate cross term.  Hence

\[
\boxed{
\Pi_{principal}\mathcal B(M_{des},M_{des})=0.
}
\tag{CR18}

The exact localized root has only the lower-order self-interaction generated by `R_M^{curl}` and slow coefficient variation.  By (CR15), these terms gain at least one factor `hS poly(S)=o(1)` relative to the principal mean-root scale.

## 8. Short-cell viscous persistence

The root physical frequency satisfies

\[
|\Xi_M|^2\asymp (h^2S^2)^{-1}.
\]

Therefore the viscous damping rate is

\[
\varepsilon|\Xi_M|^2
=h^2|\Xi_M|^2
\asymp S^{-2}.
\tag{CR19}
\]

On the boundary-layer cell, whose stretched duration is `O(1)`, this changes the principal root amplitude by only

\[
\boxed{1+O(S^{-2}).}
\tag{CR20}
\]

Thus the incoming Cauchy root remains available throughout the local reset at the precision already permitted by the finite-`S` implicit-function tuning.

## 9. Cauchy realizability

The field (CR9) is defined directly on one genuine physical spatial slice.  Its amplitude and phase are incoming state data, not a future-time source profile.  Forward evolution of the unforced equation therefore does not violate Cauchy uniqueness.

This is the key distinction from the rejected `chi_j(v)` active controls: `M_des` is present in the physical initial state before the cell begins.

## 10. Remaining exact source insertion

To turn the reduction into a publication-level source theorem, the following identities must be pinned to the exact source chart notation:

1. identify `Theta_M=Theta_P-2Theta_C` with the reconstructed beta-zero auxiliary character in the common-cover chart;
2. derive the two-sided covector estimate (CR3) from the exact finite-`S` phase/frame coefficients at `u=1.8`, `x=0.70`;
3. translate the generic physical cutoff `chi` into one of the source-admissible compact slow/radial cutoffs;
4. propagate the exact source weighted-class exponents through (CR8)--(CR16).

The source Lemma 7.7 and the branch theorem `source_localized_action_preservation.md` already establish the necessary principle: curl localization preserves the packet envelope and introduces only algebraic/polynomial losses plus positive source powers.

## 11. Consequence

There is no Cauchy-realizability obstruction to the preloaded beta-zero root.  At the boundary-layer scale it admits an exact divergence-free localized realization with

\[
\boxed{
M_{des}=h\,a_M b_Me^{i\Theta_M}+o(h)
}

and

\[
\boxed{
\|(h\nabla)^aM_{des}\|\le h\,\operatorname{poly}(S).
}

Its localization error and viscous damping are asymptotically smaller than the `O(S^{-1})` finite-principal-map correction already handled by transversality.

The next step is to insert these jets into the whole-space semiclassical mean-root Oseen propagator and close the common mean/nonzero graph norm.
