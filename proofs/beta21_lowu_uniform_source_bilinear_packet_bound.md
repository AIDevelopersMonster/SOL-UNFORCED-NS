# Uniform source bilinear packet bound for the low-`u` growing orbit

**Status:** PROVED SOURCE-UNIFORM FIXED-ORDER BILINEAR ESTIMATE + PROVED ACTION-FACTOR PRESERVATION THROUGH THE EXISTING LOCALIZED PIPELINE / FINAL COMMON-NORM NOTATION ALIGNMENT ONLY.

The last common hypothesis in
`beta21_lowu_off_orbit_weighted_convolution_reduction.md`
and
`beta21_lowu_orbit_covariance_weighted_convolution.md`
was an actual source packet estimate of the form

\[
\|\mathcal B^{phys}(f,g)\|_{X_m}
\le C_mS^{A_m}
\|f\|_{X_m}\|g\|_{X_{m+1}}.
\]

This note records that the needed estimate is already contained in the source formalization.  The relevant theorem is

`LabelSumBounds.UniformClass.bilinear`.

Its constants are chosen before both the band and the label.  Therefore enlarging the designated family to `O(S)` labels does not alter the local bilinear constant.  The only `S`-dependence comes from the already permitted finite-order source growth degree and from later summation of output labels, which is handled separately by weighted convolution.

No exact reset cell or global cascade is claimed here.

## 1. Exact source theorem

Let

\[
f_l\in U_\alpha(w_l),
\qquad
g_l\in U_\beta(v_l)
\]

be two uniformly indexed source coefficient families in the notation of
`LabelSumBounds.UniformClass`.

The source theorem states that for every continuous bilinear map

\[
L:E\times F\to G,
\]

one has

\[
\boxed{
L(f_l,g_l)
\in
U_{\alpha+\beta}(w_lv_l)
}
\tag{UB1}
\]

uniformly in the band and label.

At fixed derivative order `m`, if the two input jet bounds use constants `A,B` and growth degrees `p,q`, the proof gives the explicit output constant

\[
\boxed{
C_{bil,m}=\|L\|2^mAB
}
\tag{UB2}
\]

and output growth degree

\[
\boxed{p+q.}
\tag{UB3}
\]

Crucially, neither (UB2) nor (UB3) contains the number of labels.

## 2. Pointwise jet form

The underlying theorem

`LabelSumBounds.bilinear_jet_bound`

gives, for every `j<=m`,

\[
\boxed{
\|D^jL(f,g)\|
\le
\|L\|2^mAB,
}
\tag{UB4}
\]

provided all input jets through order `m` are bounded by `A,B`.

Thus the source already supplies exactly the finite-order Leibniz constant used abstractly in the previous orbit audits.

## 3. First-order Navier--Stokes transport

The quadratic velocity term is first order:

\[
\mathcal B(u,v)
=(u\cdot\nabla)v
\]

plus the cylindrical frame/connection terms before Cartesian reconstruction.

At one fixed source chart, every directional derivative is a continuous linear operator on the coefficient jet family.  Therefore, after taking one extra jet of the differentiated input, (UB4) gives

\[
\boxed{
\|\mathcal B(u,v)\|_{X_m}
\le
C_mS^{A_m}
\|u\|_{X_m}
\|v\|_{X_{m+1}}.
}
\tag{UB5}
\]

The exponent `A_m` is finite and depends only on the frozen publication derivative order and the existing source growth degrees.  It is independent of the orbit cardinality.

Symmetrizing gives

\[
\boxed{
\|\mathcal B(u,v)+\mathcal B(v,u)\|_{X_m}
\le
C_mS^{A_m}
\left(
\|u\|_{X_m}\|v\|_{X_{m+1}}
+
\|v\|_{X_m}\|u\|_{X_{m+1}}
\right).
}
\tag{UB6}
\]

## 4. Deliberate cross-label overlap

The published source construction often makes distinct labels disjoint and therefore sets their product equal to zero.  The low-`u` relay deliberately changes this one support relation for a prescribed finite family of labels.

This does **not** change the local estimate.  On a common-torus overlap, (UB4) is a direct pointwise Leibniz theorem and applies without any same-label hypothesis.

This was already isolated in
`source_localized_action_preservation.md`, where the selected cross-label product is retained and bounded by the product of the two source majorants.

Thus the low-`u` supernode modification changes which products are present, not the coefficient estimate for a present product.

## 5. Curl realization

For the nonzero primary waves, the source files

- `CurlClassBounds.lean`,
- `PrimaryPulseBounds.lean`,
- `WaveInteractionBounds.lean`

show that the actual cutoff-curl velocity remains in a source weighted class with only the displayed positive epsilon shift and finite polynomial growth loss.

At fixed publication order this means

\[
\boxed{
\|u_{realized}\|_{X_m}
\le
C_mS^{a_m}
\|u_{stripped}\|_{X_{m+c}},
}
\tag{UB7}
\]

for one fixed finite derivative offset `c` determined by the curl construction.

There is no factor exponential in `S` introduced by the curl step.

The designated beta-zero mean root is not covered by the nonzero-harmonic curl theorem because its angular harmonic is zero.  Its separate exact Cauchy/curl realization and normalized jet estimate are proved in
`beta21_lowu_designated_mean_root_cauchy_curl_realization.md`.

## 6. Preservation of action factors

`source_localized_action_preservation.md` proves that if a source coefficient carries an additional physical action factor

\[
e^{-\gamma S},
\qquad \gamma>0,
\]

then:

1. localization preserves the factor;
2. common-torus pullback preserves the factor;
3. curl realization preserves the factor up to polynomial source losses;
4. the forward pulse inverse preserves the same envelope/action factor;
5. no `e^{+cS}` inverse is introduced.

Therefore an off-orbit source satisfying

\[
\|F\|_{X_m}
\le
C_mS^{A_m}e^{-\gamma S}
\]

produces a response of the form

\[
\boxed{
\|u_F\|_{X_m}
\le
C'_mS^{A'_m}e^{-\gamma S}.
}
\tag{UB8}
\]

This is the exact property needed in the off-orbit reduction.

## 7. Whole-space Leray

The whole-space Leray projector is treated exactly after reconstruction.

`phase_adapted_whole_space_leray_intertwining.md`
proves that modewise conjugated Leray commutes with the exact covariant derivatives and has norm at most one in the phase-adapted fixed-order Sobolev coefficient norm.

`beta21_lowu_anisotropic_leray_graph_norm.md`
and
`beta21_lowu_phase_adapted_mean_root_oseen_propagator.md`
show that the same norm-one property survives the source and parabolic anisotropic dilations.

Hence

\[
\boxed{
\|\mathbb P_{ws}F\|_{X_m}
\le
\|F\|_{X_m}
}
\tag{UB9}
\]

in the normalized coefficient formulation.  Leray cannot erase an action gap or introduce an orbit-cardinality loss.

## 8. Uniform packet theorem

Combining Sections 1--7 gives the actual common estimate required by the growing-orbit programme:

\[
\boxed{
\|\mathbb P_{ws}\mathcal B^{phys}(u,v)\|_{X_m}
\le
C_mS^{A_m}
\|u\|_{X_{m+c}}
\|v\|_{X_{m+1+c}},
}
\tag{UB10}
\]

for fixed finite `c,A_m`, uniformly in:

- dyadic level;
- source band;
- common-cover label;
- orbit index inside the strict core.

If the input interaction carries the previously established weighted physical action deficit `e^{-gamma S}`, then the right-hand side of (UB10) carries the same factor:

\[
\boxed{
\|\mathbb P_{ws}\mathcal B^{phys}_{off}(u,v)\|_{X_m}
\le
C_mS^{A_m}e^{-\gamma S}
\|u\|_{X_{m+c}}
\|v\|_{X_{m+1+c}}.
}
\tag{UB11}
\]

This is precisely the source hypothesis `(OC19)` from
`beta21_lowu_off_orbit_weighted_convolution_reduction.md`.

## 9. Consequence for the two remaining ports

Insert (UB11) into the weighted discrete reductions.

### Nonzero off-orbit block

`beta21_lowu_off_orbit_weighted_convolution_reduction.md` immediately gives

\[
\boxed{
\|B_S\|+\|C_S\|
\le
S^Ae^{-c_*S},
}
\tag{UB12}

and

\[
\boxed{
\|\mathcal N_{S,off}^{nz}\|
\le
S^Ae^{-c_*S}
(\|a\|+\|z\|)^2.
}
\tag{UB13}

Thus targets `(DN15)--(DN16)` are closed at the source-estimate level.

### Mean covariance

`beta21_lowu_orbit_covariance_weighted_convolution.md` gives

\[
\boxed{
\|F_{rM}^{tail}\|
\le
S^A\left(e^{-0.176S}+e^{-0.233S}\right),
}
\tag{UB14}
\]

while the genuine zero-character covariance remains at the ordinary source scale

\[
\boxed{
\|F_0^{cov}\|
\le
S^A\varepsilon^{1-\kappa_s}.
}
\tag{UB15}
\]

Thus the common source bilinear estimate is no longer an open conceptual port.

## 10. Remaining bookkeeping caveat

For publication, the abstract symbol `X_m` should be replaced by one explicitly named common norm and the finite derivative offset `c` and polynomial powers `A_m` should be recorded from the selected source theorem chain.

This is finite bookkeeping.  It cannot change any exponent sign or action gap because:

- `m` is fixed;
- `c` is fixed;
- all source growth losses are polynomial in `S`;
- every relevant epsilon exponent is strictly positive;
- every off-orbit action gap is fixed positive after the `sigma_0=0.005` analytic budget.

## 11. Updated frontier

The low-`u` local PDE frontier is no longer the off-orbit or covariance source estimate.  Those reduce to proved source-uniform bilinear calculus.

The next task is now to assemble the **coupled mean/nonzero Banach map** in one product norm, insert:

- the root-augmented mean propagator;
- the designated/nonzero hybrid propagator;
- the weighted orbit covariance;
- the `O(1)` mean-to-wave sensitivity;
- the `epsilon^{1/2-kappa_s}` wave-to-mean return gain;

and prove that the full product-map Lipschitz constant tends to zero.

Only after that coupled contraction is closed should the `C^1` dependence on `(kappa,theta,A_M)` and the final finite-dimensional implicit-function step be executed.
