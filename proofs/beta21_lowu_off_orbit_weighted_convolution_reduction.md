# Weighted-convolution reduction of the low-`u` off-orbit nonzero operator

**Status:** PROVED DISCRETE OPERATOR-NORM REDUCTION FROM POINTWISE ACTION GAP TO `S^A e^{-cS}` OFF-BLOCK BOUND / ACTUAL SOURCE PACKET BILINEAR CONSTANT STILL TO BE PINNED.

The corrected nonzero block in
`beta21_lowu_designated_orbit_complement_propagator_reduction.md`
requires

\[
\|B_S\|+\|C_S\|
\le S^Ae^{-c_*S}
\]

for the off-diagonal transfers between the designated beta-one/beta-two orbit and the analytic nonzero complement.

This note proves that no `O(S) x O(S)` operator analysis is needed.  Once a single source-local bilinear packet estimate and the already established weighted pointwise action gap are available, the complete off-block operator follows by weighted convolution.  The only dimension loss from the designated orbit is the harmless finite-support embedding

\[
\ell^2\hookrightarrow\ell^1
\]

with factor `O(S^{1/2})`.

No exact low-`u` reset cell is claimed here.

## 1. Character addition

Every quadratic/mixed harmonic interaction obeys character addition

\[
K_{out}=K_1+K_2.
\]

The designated nonzero orbit consists of

\[
C_j=C+jM,
\qquad
Q_n=P+nM
\]

on index sets of cardinality

\[
N_S=O(S).
\]

The analytic complement uses

\[
W_\sigma(K):=e^{\sigma|K|_1}(1+|K|_1)^r,
\qquad \sigma=\sigma_0=0.005.
\]

The exponential factor is submultiplicative:

\[
\boxed{
 e^{\sigma|K_1+K_2|_1}
\le
 e^{\sigma|K_1|_1}e^{\sigma|K_2|_1}.
}
\tag{OC1}
\]

At fixed integer `r`, the polynomial factor satisfies the standard estimate

\[
1+|K_1+K_2|_1
\le
(1+|K_1|_1)(1+|K_2|_1),
\]

hence

\[
\boxed{
W_\sigma(K_1+K_2)
\le
W_\sigma(K_1)W_\sigma(K_2).
}
\tag{OC2}
\]

## 2. Abstract packet bilinear estimate

Let `X_r` be the fixed-order packet norm at one common physical chart.  Assume the realized quadratic/mixed operator obeys

\[
\boxed{
\|\mathcal B_{K_1,K_2}(f,g)\|_{X_r}
\le C_r S^{A_r}
\|f\|_{X_r}\|g\|_{X_r}.
}
\tag{OC3}
\]

The fixed power `S^{A_r}` includes:

- fixed-order coefficient derivatives;
- curl reconstruction;
- frame differentiation;
- common-cover pullback;
- local overlap multiplicity.

`beta21_lowu_orbit_source_polynomial_audit.md` proves that every such loss is polynomial in `S`.  What remains for the final source theorem is only to identify one explicit `A_r` for the actual packet norm; the argument below is independent of its value.

## 3. Complement analytic norm

For complement coefficients `z_K`, define

\[
\boxed{
\|z\|_{\mathfrak A_{\sigma,r}}
:=
\sum_{K\in\mathcal C_S}
W_\sigma(K)\|z_K\|_{X_r},
}
\tag{OC4}
\]

where `C_S` is the nonzero angular complement of the designated `C/Q` orbit.

By (OC2)--(OC3), ordinary convolution with an analytic `l^1` coefficient sequence satisfies

\[
\boxed{
\|\mathcal B(a,z)\|_{\mathfrak A_{\sigma,r}}
\le
C_rS^{A_r}
\|a\|_{\ell^1_\sigma(X_r)}
\|z\|_{\mathfrak A_{\sigma,r}}.
}
\tag{OC5}
\]

The same estimate holds for `B(z,a)`.

## 4. Designated large-deviation norm

For one designated family write

\[
\|a\|_{des}^2
=
\sum_{j\in O_S}|a_j|^2e^{2SH(z_j)}.
\tag{OC6}
\]

Define the action-normalized coefficients

\[
\widetilde a_j:=a_je^{SH(z_j)}.
\]

Then

\[
\|\widetilde a\|_{\ell^2}=\|a\|_{des}.
\]

Since

\[
|O_S|\le C_OS,
\]

Cauchy--Schwarz gives

\[
\boxed{
\|\widetilde a\|_{\ell^1}
\le C_O^{1/2}S^{1/2}\|a\|_{des}.
}
\tag{OC7}
\]

This `S^{1/2}` is the only unavoidable support-cardinality loss in the discrete convolution step.

## 5. Weighted action-gap hypothesis

The principal boundary-layer audit proves that every off-designated nonzero target generated from the designated orbit has a strict physical action deficit.

After inserting the analytic weight at `sigma_0=0.005`, the established margins are

\[
c_{bd,C}-\sigma_0C_C>6.0\times10^{-4},
\]

\[
c_{bd,Q}-\sigma_0C_Q>1.5\times10^{-3},
\]

and

\[
\gamma_{crit}-\sigma_0C_{quad}>0.058.
\]

Choose once and for all

\[
\boxed{
0<c_*<6.0\times10^{-4}.
}
\tag{OC8}
\]

Then every off-designated source term has, after action normalization and analytic weighting, the pointwise factor

\[
\boxed{e^{-c_*S}.}
\tag{OC9}
\]

for all sufficiently large `S`.

The exact source-local transfer of the physical action factor through localization/curl/pulse inversion is already established in `source_localized_action_preservation.md`; the current growing-orbit task is to apply that same local estimate uniformly over the finite `O(S)` family.

## 6. Designated-to-complement leakage

Let `a` be a designated perturbation and let `U_{orb}` be the frozen designated orbit coefficient sequence.  The linearized leakage is schematically

\[
C_Sa
=
\Pi_{comp}
\left[
\mathcal B(U_{orb},a)+\mathcal B(a,U_{orb})
\right].
\tag{OC10}
\]

After action normalization, each contributing off-orbit coefficient contains the factor (OC9).

Apply (OC3), then sum by convolution and use (OC7) for each designated sequence.  One obtains

\[
\boxed{
\|C_Sa\|_{\mathfrak A_{\sigma_0,r}}
\le
C_rS^{A_r+1}
 e^{-c_*S}
\|U_{orb}\|_{des}\|a\|_{des}.
}
\tag{OC11}
\]

The displayed `S^1` is the crude product of two `S^{1/2}` embeddings.  If one factor is kept in its frozen uniformly bounded `l^1` large-deviation profile, this improves to `S^{1/2}`.  No improvement is needed.

Since the frozen normalized designated orbit has bounded `des` norm,

\[
\boxed{
\|C_S\|
\le
C_rS^{A_r+1}e^{-c_*S}.
}
\tag{OC12}
\]

## 7. Complement-to-designated leakage

Let `z` lie in the analytic complement.  The off-block return is

\[
B_Sz
=
\Pi_{des}
\left[
\mathcal B(U_{orb},z)+\mathcal B(z,U_{orb})
\right].
\tag{OC13}
\]

Only interactions landing in the finite designated windows contribute.  The same character-addition law and the same weighted action deficit apply to every such non-native return path; the principal `M_des` shift is excluded because it is already part of `G_{des,S}`.

Using one designated `l^1` embedding and the analytic `l^1` norm for `z` yields

\[
\boxed{
\|B_Sz\|_{des}
\le
C_rS^{A_r+1/2}e^{-c_*S}
\|U_{orb}\|_{des}
\|z\|_{\mathfrak A_{\sigma_0,r}}.
}
\tag{OC14}
\]

Hence

\[
\boxed{
\|B_S\|
\le
C_rS^{A_r+1/2}e^{-c_*S}.
}
\tag{OC15}
\]

## 8. Combined off-block estimate

Absorbing the harmless half-power into one fixed polynomial exponent gives

\[
\boxed{
\|B_S\|+\|C_S\|
\le
S^Ae^{-c_*S}
}
\tag{OC16}
\]

for some fixed finite `A`, exactly the target `(DN15)`.

The important point is that the proof uses only:

1. one source-local bilinear packet estimate (OC3);
2. the already proved physical action gap;
3. submultiplicativity of analytic weights;
4. the finite-support `l^2 -> l^1` factor `S^{1/2}`.

There is no matrix inversion and no exponential dependence on the orbit cardinality.

## 9. Quadratic off-orbit nonlinearity

The same argument applies to two varying designated/complement inputs.  Every off-designated quadratic output has the weighted action deficit (OC9), so

\[
\boxed{
\|\mathcal N_{S,off}^{nz}(a,z)\|_{
\mathcal X_{S,0}^{nz}}
\le
S^Ae^{-c_*S}
\left(\|a\|_{des}+\|z\|_{\mathfrak A_{\sigma_0,1}}\right)^2.
}
\tag{OC17}
\]

This is the target `(DN16)`, again modulo the single actual source packet bound (OC3).

Beta-zero quadratic outputs are not included in (OC17); they are routed to the mean lattice and controlled by `beta21_lowu_orbit_covariance_weighted_convolution.md`.

## 10. Parameter derivatives

Differentiating in `(kappa,theta,A_M)` produces a finite Leibniz sum.  Each derivative of a designated sequence costs at most a fixed power of `S`, while the action margins persist on a sufficiently small fixed parameter neighborhood.

Therefore for first parameter derivatives,

\[
\boxed{
\|D_pB_S\|+\|D_pC_S\|
\le
S^{A'}e^{-c_*S}.
}
\tag{OC18}
\]

The same holds for the derivative of the quadratic off-orbit remainder.

Thus the off-block reduction is compatible with the final `C^1` implicit-function argument.

## 11. Exact remaining source obligation

The discrete/operator part of `(DN15)--(DN16)` is now closed.  The only missing input is an exact source statement of the form (OC3) for the realized growing-orbit packets, with one fixed polynomial power `A_r` and the already proved action factor carried through:

\[
\boxed{
\|\mathcal B_{K_1,K_2}^{phys}(f,g)\|_{X_r}
\le
C_rS^{A_r}
\|f\|_{X_r}\|g\|_{X_r}.
}
\tag{OC19}
\]

The source repository already supplies the ingredients separately:

- `LabelSumBounds.bilinear_jet_bound`;
- `WaveInteractionBounds`;
- `CurlClassBounds`;
- `PhysicalWaveSum` local overlap;
- exact common-cover reconstruction;
- exact whole-space Leray intertwining.

What remains is to place them in one common packet norm and record the resulting polynomial exponent.  No new spectral, action, dimensional, or combinatorial obstruction remains in the nonzero off-block estimate.

## 12. Consequence

Once (OC19) is written in the actual source norm, equations (OC16)--(OC17) immediately give `(DN15)--(DN16)`.  The hybrid nonzero propagator then follows from the already stated Volterra/Neumann argument.

The local frontier is therefore reduced to **one common source packet estimate**, shared by the nonzero off-orbit and mean-covariance closures, followed by assembly of the coupled Banach map.
