# Exact physical-residual bridge for the root-augmented low-`u` mean base

**Status:** PROVED SOURCE-OPERATOR / VISCOSITY-ONE PHYSICAL-RESIDUAL IDENTIFICATION AFTER ROOT ABSORPTION; WHOLE-SPACE PRESSURE-NORM PROPAGATOR STILL OPEN.  This note removes the remaining scaling ambiguity between the source mean graph equation and the physical Navier--Stokes equation.

The source already proves that its actual common-cover mean operators match the `PhysicalResidualBridge.commonGraph` coefficients **definitionally**, and that the latter graph residual is exactly the pullback of the viscosity-one Cartesian Navier--Stokes residual.  Therefore the root-augmented base

\[
b^\sharp=b+M_{des}
\]

from `beta21_lowu_mean_root_basebounds_absorption.md` may be inserted into the exact source graph equation without introducing a new PDE scaling or an additional guessed semiclassical viscosity.

What remains is functional-analytic rather than coordinate-algebraic: reconstruct the root-augmented source base globally on `R^3`, eliminate pressure by the whole-space Leray projector in a norm compatible with the source class, and prove the forward propagator bound.  No exact unforced reset cell is claimed here.

## 1. The actual common-cover operators

For a source profile exponent `h`, common integer-cover map `index : N -> N`, radial interval `(a,b)`, and band `n`, `CommonBaseContext` defines

\[
\operatorname{radialFrequency}(n)
=\Lambda^{\operatorname{index}(n)}
 Q_n^{\operatorname{radialExponent}(h)/2},
\]

\[
\operatorname{fastCoefficient}(n)
=T_g^{\operatorname{index}(n)}Q_n^{1+h},
\]

and

\[
\operatorname{operators}(h,index,a,b)
=
\operatorname{graphOperators}
(\operatorname{reconstruction})
(\operatorname{epsilon})
(\operatorname{fastCoefficient})
\cdots.
\]

The source theorem

`CommonBaseContext.operators_match_physical`

states exactly

\[
\boxed{
\operatorname{MatchesAtTZ}
\left(
\operatorname{operators}(h,index,a,b),
\operatorname{commonGraph}(Q_n,h,index(n)),
 n
\right).
}
\tag{PB1}
\]

Its proof is literal coefficient equality (`constructor <;> rfl`).

Thus the `epsilon`, radial frequency, fast coefficient and graph directions used by `MeanIncrementBounds` are exactly those of the physical scaled graph at the same band and cover index.

## 2. Exact source-to-physical graph map

`PhysicalResidualBridge.commonGraph` has

\[
\operatorname{radialScale}=Q^{-1/2},
\]

\[
\operatorname{velocityScale}=Q^{-A(h)},
\]

\[
\operatorname{epsilon}=Q^h,
\]

\[
\operatorname{frequency}=\Lambda^kQ^{\operatorname{radialExponent}(h)/2},
\]

\[
\operatorname{fastCoefficient}=T_g^kQ^{1+h}.
\]

The exact map into the lifted graph coordinates is

\[
G.map(t,q)
=
\left(
Q^{-1/2}q_r,
\left(
Q^{-D(h)}q_z,
\frac{1-t}{Q},
\operatorname{cover}^k[\,q_r^{\operatorname{radialExponent}}v_r+t v_t\,]
\right),
q_\theta
\right).
\tag{PB2}
\]

The source theorem `commonGraph_eq_physicalToChart` identifies this map with the actual mean-chart reconstruction.

Consequently the source graph variables are not a separate model PDE; they are the exact chart coordinates of the physical spacetime field.

## 3. Why the source `epsilon` is compatible with viscosity one

The scaled graph satisfies the exact identity

\[
\boxed{
\operatorname{radialScale}
=\operatorname{velocityScale}\,\operatorname{epsilon}.
}
\tag{PB3}
\]

`PhysicalResidualBridge.graphResidual_scaled_pull` proves that under this identity the viscosity-one physical cylindrical residual is the scaled graph residual with coefficient `epsilon`.

More precisely, for graph velocity `a` and pressure `p`,

\[
\boxed{
R_{phys}
=
\operatorname{velocityScale}^2
\operatorname{radialScale}
\,R_{graph}^{(\epsilon)}.
}
\tag{PB4}
\]

The theorem `commonGraph_residualScale` gives

\[
Q^{2A(h)+1/2}
\left(
\operatorname{velocityScale}^2
\operatorname{radialScale}
\right)=1.
\tag{PB5}
\]

Therefore `commonGraph_physical_residual` identifies the normalized graph residual with the literal viscosity-one Cartesian Navier--Stokes residual, with the exact source homogeneity factor and no missing power of `Q` or `epsilon`.

This resolves the earlier ambiguity caused by seeing `epsilon Delta` in the graph equation: `epsilon` is a coordinate-scaling coefficient, not a replacement of physical viscosity one.

## 4. Root absorption happens before the physical bridge

The designated beta-zero root is an angular mean field.  The previous theorem proves

\[
\boxed{
\operatorname{BaseBounds}(s,b^\sharp),
\qquad
b^\sharp=b+M_{des}.
}
\tag{PB6}

The root changes only the velocity coefficient fields stored in the mean base.  It does **not** change:

- the source operators;
- `epsilon`;
- radial frequency;
- fast coefficient;
- the common-cover index;
- the physical graph map.

Hence (PB1)--(PB5) continue to apply unchanged after replacing `b` by `b^sharp`.

The exact source residual algebra with the root-augmented base therefore reconstructs to the exact physical viscosity-one residual with the same scaling identity.

## 5. Residual source exponent ledger survives the bridge algebra

Let `h_corr` be the small residual mean increment with

\[
\operatorname{IncrementBounds}(s,H,h_{corr}),
\qquad H\ge9/10.
\]

Since `b^sharp` satisfies the same `BaseBounds`, the exact source theorems give

\[
\operatorname{radialRemainder}
\in M_{H+9/10-2\kappa_s},
\tag{PB7}
\]

\[
\operatorname{thetaRemainder}
\in M_{H+1-2\kappa_s},
\tag{PB8}
\]

\[
\operatorname{axialRemainder}
\in M_{H+1-2\kappa_s}.
\tag{PB9}
\]

The physical bridge multiplies the **entire residual identity** by the one common nonzero homogeneity factor in (PB4)--(PB5).  It does not distinguish root terms from old-base terms and therefore introduces no new relative epsilon loss inside the residual ledger.

Thus the designated root creates no hidden scaling degradation between source residuals and the physical viscosity-one equation.

## 6. Exact local zero-residual implication

On a chart region where the representation hypotheses of `PhysicalResidualBridge.physical_residual` hold, if the complete root-augmented graph residual vanishes,

\[
R_{graph}^{(\epsilon)}[b^\sharp+h_{corr}+u_{osc},p]=0,
\]

then, by (PB4),

\[
\boxed{
R_{NS}^{phys}[U,P]=0
}
\tag{PB10}
\]

on the corresponding physical region.

This implication is exact.  It uses neither asymptotic WKB identification nor a separate approximation of physical derivatives.

## 7. What this does **not** yet prove

The source-to-physical residual identity is local in the chart representation.  It does not alone prove the whole-space functional estimates required by the branch's global pressure formulation.

The still-open whole-space tasks are:

1. reconstruct the root-augmented mean base and residual correction as global fields on `R^3` in the same class used by the whole-space Leray projector;
2. prove that pressure elimination by
   \[
   \mathbb P_{ws}=I-\nabla\Delta^{-1}\operatorname{div}
   \]
   preserves the source-small factors in a norm compatible with the graph reconstruction;
3. prove the forward mean propagator bound for the root-augmented base;
4. couple the resulting mean solve to the growing beta-one/beta-two nonzero orbit.

The exact physical bridge removes **coordinate scaling** as an obstruction, but not these whole-space operator estimates.

## 8. Preferred next norm bridge

Because the source already tracks the anisotropic derivative costs exactly through `MeanClass` and `OperatorBounds`, the preferred next step is not to invent a second PDE scaling.  Instead define a reconstructed whole-space graph norm by transporting the finite family of source graph derivatives through `commonGraph` and applying them to the physical reconstruction.

Schematically,

\[
\boxed{
\|m\|_{\mathcal Y_{m,\sigma}}
:=
\sum_k e^{\sigma|k|_1}
\sum_{|I|\le m}
\left\|
\mathcal D_I^{graph}
\left(M_{\ell,k}m_k\right)
\right\|_{L^2(\mathbb R^3)}.
}
\tag{PB11}
\]

The graph derivatives are exactly those matched to physical directions by (PB1).  The whole-space Leray projector is an order-zero Fourier multiplier; after reconstruction one must prove boundedness in this finite graph-derivative norm, using the exact physical direction identities rather than raw unweighted high derivatives.

This is now the principal local analytic frontier.

## 9. Consequence

The root-augmented source mean equation and the physical viscosity-one Navier--Stokes residual are now connected by an exact theorem chain already present in the source:

\[
\boxed{
\text{BaseBounds}(b^\sharp)
\to
\text{graphOperators}
\equiv
\text{commonGraph}
\to
R_{graph}=0
\Longrightarrow
R_{NS}^{phys}=0.
}
\]

No additional semiclassical rescaling is required to justify the PDE identity itself.

The next attack is the whole-space Leray bound in the reconstructed graph-derivative norm (PB11), followed by the forward root-augmented mean propagator.
