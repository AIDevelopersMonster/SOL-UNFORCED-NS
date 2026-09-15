# Cauchy/curl realization of the designated beta-zero mean root in the source-normalized whole-space chart

**Status:** PROVED LOCAL PRINCIPAL CURL REALIZATION + SEMICLASSICAL ERROR REDUCTION IN THE SOURCE-NORMALIZED CARTESIAN CHART / FULL SOURCE-CHART IDENTIFICATION STILL TO BE PINNED.  This revision corrects the coordinate normalization of the previous version.  The small parameter `h=sqrt(epsilon)` normalizes the carrier only **after** the standard isotropic physical dilation by `sqrt(Q)` used by the source.

The low-`u` boundary-layer cell requires a pre-existing beta-zero mean root

\[
M=P-2C
\]

on the incoming physical Cauchy slice.  Such a field can be supplied as genuine initial data by an exact localized curl.  In the source-normalized whole-space chart its principal amplitude is `O(h)`, its beta-zero covector is `O((hS)^{-1})`, and its curl-localization error is smaller by `hS poly(S)->0`.

No exact reset cell or global cascade is claimed here.

## 1. Whole-space source chart

At one dyadic/source level let `Q` be the chart scale and let

\[
A=\frac12+h_{prof}
\]

be the source velocity homogeneity exponent.  Around the physical relay center `x_0`, introduce the isotropically rescaled Cartesian variable

\[
\boxed{
y=\frac{x-x_0}{\sqrt Q}.}
\tag{CR1}
\]

For a physical velocity field `u_phys`, write its chart-normalized representative as

\[
\boxed{
\widetilde u(y)=Q^A u_{phys}(x_0+\sqrt Q\,y).
}
\tag{CR2}
\]

The source carrier calculation in `chart_invariant_carrier_scale.md` gives

\[
D_r,D_z,D_\theta
=\sqrt Q\times(\text{physical spatial derivative})
\]

at the level relevant to the carrier, and

\[
\boxed{h\,kB_s\asymp1,\qquad h:=\sqrt\varepsilon.}
\tag{CR3}
\]

Thus `h nabla_y`, not `h nabla_x`, is the natural semiclassical derivative for the packet carrier.

The chart is still the whole space `R^3`; no artificial spatial boundary is introduced.

## 2. Root phase and normalized covector

Let `Theta_P,Theta_C` be the reconstructed physical phases of the beta-two parent and beta-one catalyst.  Define

\[
\boxed{\Theta_M:=\Theta_P-2\Theta_C.}
\tag{CR4}
\]

Its angular coefficient vanishes because

\[
\beta(P)-2\beta(C)=0.
\]

Let

\[
\widetilde\Theta_M(y)
:=\Theta_M(x_0+\sqrt Q\,y)
\]

and

\[
\boxed{\Xi_M:=\nabla_y\widetilde\Theta_M.}
\tag{CR5}
\]

At the low-`u` boundary-layer point the reduced slope separation is

\[
\delta_S=\kappa/S.
\]

Since the root normal coefficient is a fixed nonzero multiple of that difference and the normalized carrier is `kB_s`, the exact finite-`S` source coefficients give, on a sufficiently small strict core,

\[
\boxed{
\frac{c_-}{S}
\le h|\Xi_M|
\le\frac{c_+}{S}
}
\tag{CR6}
\]

for fixed `0<c_-<=c_+<infty` and all sufficiently large levels.  Equivalently,

\[
\boxed{|\Xi_M|\asymp(hS)^{-1}.}
\tag{CR7}
\]

In raw physical coordinates the covector is `Q^{-1/2}Xi_M`; all estimates below are intentionally carried out in the normalized whole-space `y` chart.

## 3. Principal root polarization

The beta-zero mean-root polarization audit gives, in the frozen source frame,

\[
\boxed{b_M=-S_MK+c_0R_MN,}
\tag{CR8}
\]

with no radial component.  The beta-zero phase normal is radial at principal order, so

\[
\boxed{b_M\cdot\Xi_M=0}
\tag{CR9}
\]

at the frozen principal point.

On the strict core, replace `b_M` by its smooth pointwise orthogonal projection to `Xi_M^perp`; this changes it only by the already allowed finite-`S`/slow-frame perturbation.  Denote the exact transverse polarization by

\[
\widetilde b_M,
\qquad
\widetilde b_M\cdot\Xi_M=0.
\tag{CR10}
\]

## 4. Exact curl in normalized coordinates

Choose a smooth source-admissible cutoff `chi(y)` supported strictly inside the relay core and equal to one on the smaller orbit-interaction core.  Let `a_M` be the normalized complex root amplitude selected by the principal Poincare fixed point.

Define

\[
\boxed{
\widetilde A_M(y)
:=
\chi(y)
\frac{h a_M}{i|\Xi_M(y)|^2}
\bigl(\Xi_M(y)\times\widetilde b_M(y)\bigr)
 e^{i\widetilde\Theta_M(y)}.
}
\tag{CR11}

Set

\[
\boxed{
\widetilde M_{des}
:=2\Re(\nabla_y\times\widetilde A_M).
}
\tag{CR12}

Then

\[
\boxed{\nabla_y\cdot\widetilde M_{des}=0}
\tag{CR13}
\]

exactly.

Pull back to physical coordinates by

\[
\boxed{
M_{des}^{phys}(x)
:=Q^{-A}\widetilde M_{des}
\left(\frac{x-x_0}{\sqrt Q}\right).
}
\tag{CR14}
\]

Because isotropic dilation and multiplication by a scalar preserve zero divergence,

\[
\boxed{\nabla_x\cdot M_{des}^{phys}=0.}
\tag{CR15}
\]

Thus the designated root is honest physical Cauchy data.

## 5. Principal curl term

When `nabla_y` hits the exponential,

\[
\nabla_y e^{i\widetilde\Theta_M}
=i\Xi_Me^{i\widetilde\Theta_M}.
\]

Using

\[
\Xi\times(\Xi\times b)
=-|\Xi|^2b
\]

for `b perpendicular Xi`, the leading curl is

\[
\boxed{
\nabla_y\times\widetilde A_M
=
\chi h a_M\widetilde b_Me^{i\widetilde\Theta_M}
+R_M^{curl}.
}
\tag{CR16}
\]

Hence the normalized source-chart root has size

\[
\boxed{\widetilde M_{des}=O(h)=O(\sqrt\varepsilon),}
\tag{CR17}
\]

i.e. source order `M_{1/2}`.

## 6. Curl-localization remainder

The normalized vector-potential prefactor has size

\[
\frac{h}{|\Xi_M|}
\asymp h^2S
\tag{CR18}
\]

by (CR7).  A derivative falling on the fixed normalized cutoff or on a source-smooth frame/polarization coefficient therefore contributes only a lower-order term.  At every fixed source derivative order,

\[
\boxed{
\|R_M^{curl}\|
\le C h^2S\,\operatorname{poly}(S).
}
\tag{CR19}
\]

Relative to the leading `O(h)` root,

\[
\boxed{
\frac{\|R_M^{curl}\|}{h}
\le ChS\,\operatorname{poly}(S)
\longrightarrow0.
}
\tag{CR20}
\]

This is the same structural conclusion as source Lemma 7.7: exact curl localization preserves the leading packet and introduces only lower source classes.

## 7. Correct semiclassical jets

Define

\[
\boxed{D_h:=h\nabla_y=h\sqrt Q\,\nabla_x.}
\tag{CR21}
\]

When `D_h` hits the root phase it contributes

\[
h\Xi_M=O(S^{-1}).
\]

When it hits a normalized cutoff/frame coefficient it contributes the corresponding source-normalized fixed-order jet.  Thus, for every fixed `a`,

\[
\boxed{
\|D_h^a\widetilde M_{des}\|_{L^\infty_y}
\le
C_a h\,\operatorname{poly}(S)(1+S^{-a}).
}
\tag{CR22}
\]

The pure phase contribution obeys the sharper estimate

\[
\boxed{
\|D_h^a\widetilde M_{des}^{principal}\|_\infty
\le C_a hS^{-a}.
}
\tag{CR23}
\]

No statement of the form `h nabla_x Theta_M=O(S^{-1})` is used; the `sqrt(Q)` chart factor in (CR21) is essential.

## 8. Principal self-advection

Because

\[
\widetilde b_M\cdot\Xi_M=0,
\]

the frozen plane-wave self-advection vanishes, including the conjugate zero-frequency cross term.  Hence

\[
\boxed{
\Pi_{principal}\mathcal B(\widetilde M_{des},\widetilde M_{des})=0.
}
\tag{CR24}

The exact localized root has only lower-order self-interaction generated by (CR19) and slow coefficient variation.

## 9. Short-cell viscous persistence

In the source-normalized chart the viscous coefficient is `epsilon=h^2` and

\[
|\Xi_M|^2\asymp(h^2S^2)^{-1}.
\]

Therefore

\[
\boxed{
\varepsilon|\Xi_M|^2\asymp S^{-2}.
}
\tag{CR25}
\]

Across the `O(1)` stretched boundary-layer collar, viscous damping changes the principal root amplitude by only

\[
\boxed{1+O(S^{-2}).}
\tag{CR26}
\]

## 10. Cauchy realizability and whole-space scaling

The field (CR14) is defined on one genuine physical Cauchy slice.  It is not a future-time control profile.

The dilation `x=x_0+sqrt(Q)y` maps `R^3` to `R^3`.  It therefore preserves the whole-space nature of the pressure problem.  In particular the whole-space Leray projector may be conjugated through this isotropic dilation; its degree-zero Fourier symbol is unchanged up to the corresponding rotation/translation convention.

## 11. Remaining exact source insertion

For a publication-level theorem one must still pin:

1. the exact common-cover identity giving `Theta_M=Theta_P-2Theta_C`;
2. the two-sided normalized covector bound (CR6) from the finite-`S` phase/frame coefficients;
3. the chosen normalized cutoff to the source admissible slow/radial cutoff family;
4. the precise polynomial/source-positive factors in (CR22).

The source carrier identity `h kB_s asy 1`, Lemma 7.7 and `source_localized_action_preservation.md` already provide the required scaling architecture.

## 12. Consequence

The preloaded beta-zero root is Cauchy-realizable as an exact divergence-free field.  In the correct normalized whole-space chart,

\[
\boxed{
\widetilde M_{des}
=h a_Mb_Me^{i\widetilde\Theta_M}+o(h),
}
\]

and

\[
\boxed{
\|(h\nabla_y)^a\widetilde M_{des}\|
\le h\,\operatorname{poly}(S).
}
\]

Its localization error and viscous damping are asymptotically smaller than the finite-principal-map correction.  These are the jet inputs required by the corrected whole-space mean-root Oseen reduction.
