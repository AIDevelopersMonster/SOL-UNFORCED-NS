# Polynomial source-loss audit for the low-`u` growing orbit bank

**Status:** PROVED FIXED-DERIVATIVE POLYNOMIAL-COUNTING AUDIT / EXACT SOURCE-INDEX REALIZATION AND FULL ZERO-RESIDUAL CLOSURE STILL OPEN. This note verifies that the `O(S)` orbit cardinality in the low-`u` boundary-layer candidate does not by itself introduce exponential source constants. At every fixed derivative order, the source multiplicity, character differentiation, finite products, curl reconstruction, and the weakest beta-zero inverse contribute only fixed powers of `S`.

Combined with the fixed negative action gaps in `beta21_lowu_boundary_layer_bilateral_orbit_reset.md`, all such losses are asymptotically harmless. What remains is to insert these polynomial bounds into the exact phase-adapted nonzero/mean fixed-point norms with the precise rank-two character-to-source-index realization.

## 1. Orbit size and source harmonic cutoff

On the fixed slope core

\[
|z-x|\le0.03
\]

with

\[
\delta_S=\kappa/S,
\]

the beta-one and beta-two orbit indices have magnitude

\[
|j|+|n|\le C_0 S.
\]

Thus a source harmonic/character cutoff sufficient to contain the complete designated orbit bank may be chosen as

\[
\boxed{H_S\le C_H S.}
\tag{SP1}
\]

The source formalization `PhysicalWaveSum.lean` proves the exact pointwise overlap bound

\[
\boxed{
\#\{\text{active wave indices at one physical point}\}
\le2250(2H+1).
}
\tag{SP2}
\]

Consequently, after inserting (SP1),

\[
\boxed{N_{loc}(S)=O(S).}
\tag{SP3}
\]

This is an actual physical local-finiteness bound, not merely the cardinality of an abstract lattice box.

## 2. Fixed-order character derivatives

`PhysicalGraphBounds.norm_character_jet` gives the exact identity

\[
\left\|D^m e^{ic\phi}\right\|
=|c|^m
\]

for the scalar character before composition with the physical phase map.

For every designated orbit mode, the integer character coefficients have size `O(S)`. Therefore for every **fixed** derivative order `m`,

\[
\boxed{
\|D^m\operatorname{char}_K\|
\le C_m S^m
}
\tag{SP4}
\]

up to the already-existing physical chart/frequency powers that are present in the source wave classes independently of the orbit cardinality.

The important point is that increasing the orbit depth from fixed size to `O(S)` changes constants by a polynomial `S^m`, not by `e^{cS}`.

## 3. Summing the orbit family

`LabelSumBounds.UniformClass.sum` proves that finite sums preserve the same weighted source class by adding the individual finite-jet constants. Combining (SP3) and (SP4) gives the crude but sufficient fixed-order bound

\[
\boxed{
C_m^{orbit}(S)
\le C_m S^{m+1}.
}
\tag{SP5}

This bound is intentionally conservative. The physical large-deviation localization and local support coloring make the true sum smaller, but no improvement is needed for asymptotic closure.

## 4. Bilinear source terms

`LabelSumBounds.bilinear_jet_bound` gives the exact fixed-order Leibniz estimate

\[
\|D^j B(f,g)\|
\le
\|B\|\,2^m A B,
\qquad j\le m,
\]

when all derivatives up to order `m` of the factors are bounded by `A,B`.

Thus the derivative order itself contributes only the fixed factor `2^m`. If one uses the crude total-sum bound (SP5) for both orbit factors, then

\[
\boxed{
C_m^{quad}(S)
\le C_m S^{2m+2}.
}
\tag{SP6}

A convolution/weighted-`ell^2` argument improves this to a smaller power, but (SP6) is already enough because every non-`M` critical quadratic source carries a fixed exponential action loss.

## 5. Curl and potential reconstruction

The exact divergence-free realization takes a fixed finite number of derivatives of the scalar/vector potential. At a fixed publication derivative order this raises the power of `S` by only a fixed integer.

Therefore there is a fixed `r_m` such that the complete curl-generated designated orbit field and its lower-order reconstruction remainder obey source constants of the form

\[
\boxed{
C_m^{curl}(S)\le C_m S^{r_m}.
}
\tag{SP7}

No orbit-count mechanism produces an exponential-in-`S` derivative loss.

## 6. Stable high-beta sectors

For beta at least three the selected low-`u` core has the fixed full-symbol bounds

\[
\Gamma_3(z)\le-1.8918,
\]

\[
\Gamma_4(z)\le-3.8597
\]

and stronger negativity at higher beta.

Thus the high-beta stable inverse has an `S`-independent spectral denominator on the core. The only `S`-dependence comes from source summation/derivatives and is therefore polynomial by Sections 1--5.

## 7. Nearly neutral beta-zero harmonics

Differences of orbit characters produce beta-zero modes

\[
rM,
\qquad |r|=O(S).
\]

Because

\[
\delta_S=\kappa/S,
\]

the normalized viscous rate has the form

\[
\lambda_{rM}
=-c_M\left(\frac rS\right)^2.
\tag{SP8}

For `r=O(S)` this has an `O(1)` stable denominator. The weakest nonzero denominator occurs for `|r|=1`:

\[
\boxed{
|\lambda_M|^{-1}=O(S^2).
}
\tag{SP9}

Thus adjoining the entire generated beta-zero family can cost at worst an additional factor `S^2` in the stable solve.

But every **generated** beta-zero mode other than the designated/preloaded `M` channel comes from a pair of exponentially small beta-one or beta-two orbit packets. The center source-action ceilings are

\[
2\mathcal E_1(x)\approx-0.17695,
\]

\[
2\mathcal E_2(x)\approx-0.23457.
\]

Hence even the weakest beta-zero inverse satisfies

\[
\boxed{
S^2 e^{-0.176S}\to0.
}
\tag{SP10}

The almost-neutral beta-zero spectrum is therefore not a new leading critical block.

## 8. Mean forcing

The angular mean is quadratic in oscillatory coefficients. A worst-case direct count of all active orbit pairs is `O(S^2)`. Combining this with fixed-order derivatives gives only another fixed polynomial factor.

Schematically, for every fixed mean derivative order,

\[
\boxed{
\|F_{mean}^{orbit}\|
\le S^{A_m}\times
(\text{existing source small factor})
}
\tag{SP11}

for a fixed exponent `A_m`.

Moreover the non-designated pairings have the fixed action gaps from the boundary-layer audit, so their contribution is exponentially smaller than this crude polynomial majorant.

The remaining exact task is to insert the designated `M`-orbit contribution into the already proved causal mean inverse and verify that its source exponent remains positive after the extra polynomial `S^{A_m}`. No exponential loss arises from mode count.

## 9. Parameter differentiation

The finite principal tuning uses only three macroscopic parameters:

\[
\kappa,
\qquad
\theta,
\qquad
A_M.
\]

Differentiating with respect to these parameters differentiates orbit slopes/weights and fixed principal coefficients. Since orbit indices are `O(S)`, each parameter derivative introduces at worst one additional power of `S` at fixed physical derivative order.

Therefore for every fixed number of parameter derivatives,

\[
\boxed{
C_{m,r}^{param}(S)\le C_{m,r}S^{B_{m,r}}
}
\tag{SP12}

for some fixed exponent `B_{m,r}`.

This is exactly the form needed for a finite-dimensional `C^1` implicit-function correction of the transverse principal fixed point.

## 10. Exponential gaps dominate every audited loss

Let `A` be the maximum of the finitely many polynomial exponents required by the chosen publication norm. The non-`M` critical action gap satisfies

\[
\gamma_{crit}\ge0.05925,
\]

while the physical boundary truncation gap satisfies

\[
c_{bd}\ge8.6\times10^{-4}.
\]

Hence

\[
\boxed{
S^A e^{-\gamma_{crit}S}\to0,
\qquad
S^A e^{-c_{bd}S}\to0.
}
\tag{SP13}

Similarly, generated beta-zero sources retain fixed negative actions large enough to absorb their worst `S^2` inverse loss.

Thus **every new loss identified from growing orbit cardinality is polynomial and asymptotically dominated by an already established fixed exponential action gap.**

## 11. Remaining source-specific gap

This audit deliberately stops one step before an exact PDE theorem. The rank-two orbit characters must be embedded into the source's actual harmonic/common-cover index family with the following facts checked uniformly:

1. character coefficient size is bounded by `C S` in every source phase direction;
2. the chosen common-cover depth remains within the already bounded neighboring-band range;
3. the physical curl realization of the complete orbit bank satisfies the same polynomial bounds derived abstractly above;
4. the exact nonzero and mean fixed-point maps accept these `S`-dependent constants without changing the sign of their small exponents.

These are now **bookkeeping/source-index obligations**, not new action or polarization obstructions.

## 12. Consequence

The growing-block objection has narrowed substantially. At fixed derivative order,

\[
\boxed{
O(S)\text{ orbit modes}
\Longrightarrow
\text{only polynomial source/correction losses}.
}

Therefore the preferred next theorem is to port the existing phase-adapted exact zero-residual contraction to this explicitly polynomial `S`-dependent packet family.

No exact unforced reset cell is claimed until that port is complete.
