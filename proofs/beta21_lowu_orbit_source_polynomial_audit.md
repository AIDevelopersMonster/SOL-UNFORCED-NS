# Source-loss and analytic-weight audit for the low-`u` growing orbit bank

**Status:** PROVED FIXED-DERIVATIVE POLYNOMIAL-COUNTING AUDIT + PROVED SMALL-`sigma` ANALYTIC-WEIGHT BUDGET / EXACT GROWING-BLOCK ZERO-RESIDUAL CLOSURE STILL OPEN.  This revision corrects an overstatement in the previous version.  The `O(S)` orbit cardinality introduces only polynomial losses in source multiplicity, fixed-order differentiation, finite products, curl reconstruction and the weakest beta-zero inverse, but the phase-adapted correction norm also contains the analytic lattice factor `exp(sigma |nu|_1)`.  Since the designated orbit indices themselves are `O(S)`, this factor is exponential in `S` and must be budgeted against the already proved physical action gaps.

At the selected low-`u` point this budget closes for every sufficiently small fixed `sigma>0`; a conservative explicit choice is

\[
\boxed{\sigma=0.005.}
\]

The growing bilateral orbit must be treated as part of the designated state, not as a correction in the analytic lattice norm.  Only the residual/complement is measured with the exponential lattice weight.

No exact unforced reset cell is claimed in this note.

## 1. Orbit size and source harmonic cutoff

Use the working point from `beta21_lowu_boundary_layer_bilateral_orbit_reset.md`,

\[
u=1.8,\qquad x=0.70,\qquad w=0.03,
\]

and

\[
\delta_S=\kappa/S,
\qquad
\kappa=0.894049167184884\ldots.
\]

The designated beta-one and beta-two orbit characters are

\[
C_j=C+jM,
\qquad
Q_n=P+nM,
\qquad M=P-2C.
\]

On the fixed slope core `|z-x|<=w`, their relevant indices satisfy

\[
|j|+|n|\le C_0S.
\]

Thus a source harmonic cutoff containing the complete designated core may be chosen as

\[
\boxed{H_S\le C_HS.}
\tag{SP1}
\]

The source formalization `PhysicalWaveSum.lean` gives the exact local overlap estimate

\[
\boxed{
\#\{\text{active wave indices at one physical point}\}
\le2250(2H+1).
}
\tag{SP2}
\]

Hence

\[
\boxed{N_{loc}(S)=O(S).}
\tag{SP3}
\]

This is a physical local-finiteness statement, not merely an abstract lattice count.

## 2. Fixed-order character derivatives

`PhysicalGraphBounds.norm_character_jet` gives the exact scalar identity

\[
\|D^m e^{ic\phi}\|=|c|^m.
\]

The integer coefficients of all designated orbit characters are `O(S)`. Therefore, at every fixed derivative order `m`,

\[
\boxed{
\|D^m\operatorname{char}_K\|
\le C_mS^m
}
\tag{SP4}
\]

up to the physical chart/frequency factors that are already present in the source wave classes independently of the orbit size.

Thus increasing the designated block from fixed cardinality to `O(S)` changes fixed-order source constants polynomially.

## 3. Summing the orbit family

`LabelSumBounds.UniformClass.sum` preserves the source class under finite summation by adding the individual constants.  Combining (SP3) and (SP4) gives the crude bound

\[
\boxed{
C_m^{orbit}(S)\le C_mS^{m+1}.
}
\tag{SP5}
\]

This is deliberately conservative.  Large-deviation localization makes the true physical sum smaller, but no improvement is needed below.

## 4. Bilinear source terms

`LabelSumBounds.bilinear_jet_bound` gives

\[
\|D^jB(f,g)\|
\le \|B\|2^mAB,
\qquad j\le m,
\]

when all derivatives up to order `m` of the factors are bounded by `A,B`.  Hence a crude use of (SP5) for both factors yields

\[
\boxed{
C_m^{quad}(S)\le C_mS^{2m+2}.
}
\tag{SP6}
\]

The derivative-order factor `2^m` is fixed because the publication norm uses a fixed finite derivative order.

## 5. Curl and physical reconstruction

The exact divergence-free realization uses a fixed finite number of derivatives of the vector potential. Therefore for every fixed publication derivative order there is a finite exponent `r_m` such that

\[
\boxed{
C_m^{curl}(S)\le C_mS^{r_m}.
}
\tag{SP7}
\]

Again, this is a polynomial loss.

## 6. Stable high-beta sectors

On the selected core one has the fixed full-symbol estimates

\[
\Gamma_3(z)\le-1.8918,
\qquad
\Gamma_4(z)\le-3.8597,
\]

with stronger negativity for larger beta. Thus high-beta stable inversion has an `S`-independent spectral denominator; only the polynomial source constants above remain.

## 7. Nearly neutral beta-zero harmonics

Differences of orbit characters generate beta-zero modes

\[
rM,
\qquad |r|=O(S).
\]

Since `delta_S=kappa/S`, their normalized viscous rates have the form

\[
\lambda_{rM}=-c_M(r/S)^2.
\tag{SP8}
\]

The weakest nonzero denominator is therefore the `|r|=1` mode:

\[
\boxed{|\lambda_M|^{-1}=O(S^2).}
\tag{SP9}
\]

Every generated beta-zero mode other than the designated preloaded `M` comes from exponentially small beta-one/beta-two packets.  At the center,

\[
2\mathcal E_1(x)\approx-0.17695,
\qquad
2\mathcal E_2(x)\approx-0.23457.
\]

Consequently even the weakest beta-zero inverse obeys

\[
\boxed{S^2e^{-0.176S}\to0.}
\tag{SP10}
\]

The almost-neutral beta-zero spectrum is therefore not a new leading critical block.

## 8. Mean forcing and parameter differentiation

A worst-case direct count of orbit pairs is `O(S^2)`.  At fixed mean derivative order this changes the forcing estimate only by a fixed power of `S`:

\[
\boxed{
\|F_{mean}^{orbit}\|
\le S^{A_m}\times(\text{existing source small factor}).
}
\tag{SP11}
\]

The principal tuning uses only the macroscopic parameters

\[
\kappa,\qquad\theta,\qquad A_M.
\]

At fixed physical derivative order and fixed parameter-differentiation order, orbit indices `O(S)` contribute only additional fixed powers:

\[
\boxed{
C_{m,r}^{param}(S)\le C_{m,r}S^{B_{m,r}}.
}
\tag{SP12}
\]

This is the correct scale for the finite-dimensional `C^1` implicit-function correction already justified by the principal transversality determinant.

## 9. The analytic lattice weight is not polynomial

The phase-adapted nonzero-harmonic space uses

\[
\|z\|_{\mathfrak A_{\sigma,r}}
=
\sum_{\nu\ne0}
 e^{\sigma|\nu|_1}(1+|\nu|_1)^r\|z_\nu\|_{pkt}.
\]

For the reset basis `(P,C)`,

\[
C_j=(j,1-2j),
\qquad
Q_n=(1+n,-2n).
\]

The slope spacing of the catalyst orbit is `2delta_S`, whereas the slope spacing of the parent orbit is `delta_S`.  Hence on `|z-x|<=w`,

\[
|j|\le \frac{wS}{2\kappa}+O(1),
\]

\[
|n|\le \frac{wS}{\kappa}+O(1).
\]

Therefore

\[
\boxed{
|C_j|_1
\le C_CS+O(1),
\qquad
C_C:=\frac{3w}{2\kappa}
\approx0.05033,
}
\tag{SP13}
\]

and

\[
\boxed{
|Q_n|_1
\le C_QS+O(1),
\qquad
C_Q:=\frac{3w}{\kappa}
\approx0.10067.
}
\tag{SP14}
\]

For a quadratic target it is enough to use the conservative character bound

\[
\boxed{C_{quad}:=2C_Q\approx0.20134.}
\tag{SP15}
\]

Thus `exp(sigma |nu|_1)` is an exponential-in-`S` factor.  It must be paid from the physical action margins.

## 10. Small-`sigma` budget

The interior non-`M` critical feedback gap is

\[
\gamma_{crit}\ge0.05925.
\]

The bilateral physical localization at the two core boundaries gives the smaller truncation margins

\[
c_{bd,C}\ge8.61\times10^{-4},
\]

\[
c_{bd,Q}\ge2.106\times10^{-3}.
\]

For the analytically weighted complement to remain exponentially small it is sufficient that

\[
\sigma C_C<c_{bd,C},
\]

\[
\sigma C_Q<c_{bd,Q},
\]

and

\[
\sigma C_{quad}<\gamma_{crit}.
\]

Numerically these require approximately

\[
\sigma<0.0171,
\qquad
\sigma<0.0209,
\qquad
\sigma<0.294.
\]

The boundary catalyst tail is therefore the binding condition.  Fix once and for all

\[
\boxed{\sigma_0=0.005.}
\tag{SP16}
\]

Then, after absorbing the `O(1)` character offsets for sufficiently large `S`,

\[
e^{\sigma_0|C_j|_1}e^{-c_{bd,C}S}
\le
\exp[-(6.0\times10^{-4})S],
\tag{SP17}
\]

\[
e^{\sigma_0|Q_n|_1}e^{-c_{bd,Q}S}
\le
\exp[-(1.5\times10^{-3})S],
\tag{SP18}
\]

and every interior quadratic residual has the much larger weighted gap

\[
\boxed{
\gamma_{crit}-\sigma_0C_{quad}>0.058.
}
\tag{SP19}
\]

Thus the analytic lattice weight does not destroy any established physical exponential margin when `sigma` is chosen sufficiently small.

## 11. The designated orbit must be split off before applying the correction norm

The bilateral orbit itself contains `O(S)` characters with `|nu|=O(S)` and is not small in the analytic correction norm merely by counting.  It must therefore be included in the designated principal state

\[
U_{des,S}=U_M+U_{C\text{-orbit},S}+U_{Q\text{-orbit},S}.
\]

The correction unknown contains only the complementary non-designated harmonics.  The order-one beta-zero translation by the preloaded `M` is also part of the designated linear propagator, not a perturbative correction term.

With this split, only boundary leakage, non-`M` orbit feedback, reconstruction remainders and generated stable harmonics enter the `A_{sigma_0,r}` correction forcing.  Equations (SP17)--(SP19) show that all of them retain a fixed positive exponential gap after analytic weighting.

## 12. Compatibility with the already proved local contraction scales

The existing local theorem uses factors of the form

\[
S_*^C\varepsilon^{9/50-2\kappa_s},
\qquad
S_*^C\varepsilon^{1/2-\kappa_s},
\qquad
S_*^C\varepsilon^{1-2\kappa_s},
\]

and

\[
\rho_\ell\lesssim
S_*^C\varepsilon^{1/5}+S_*^Ce^{-cS_*}.
\]

Replacing the fixed designated block by the growing orbit bank only changes the fixed powers of `S_*` in the source/jet estimates above.  For every fixed additional power `A`, the source hierarchy already used in the local theorem gives

\[
S_*^{C+A}\varepsilon^a\to0
\]

for each displayed positive exponent `a`; likewise a fixed polynomial is dominated by the weighted exponential gaps (SP17)--(SP19).

Therefore the **small-exponent signs in the Banach contraction are unchanged** by the audited growing-block losses.

This is an asymptotic reduction statement.  It does not by itself prove that the full designated `M`-shift propagator has been inserted into every source-level coefficient equation.

## 13. Remaining exact PDE obligations

The remaining tasks are now sharply identified:

1. realize every rank-two orbit character in the actual source harmonic/common-cover index family with coefficient size `O(S)`;
2. define the `S`-dependent designated projection and insert the preloaded `M` translation into the full nonzero linearized propagator;
3. prove that the complementary mixed operator from the beta-one/beta-two orbit bank has the weighted exponentially small norm predicted by (SP17)--(SP19), rather than merely a pointwise action estimate;
4. pass the same designated/complement split through the angular-mean forcing and whole-space Leray--Oseen solve;
5. run the finite-dimensional `(kappa,theta,A_M)` tuning after the exact correction and verify that its `C^1` perturbation is `o(1)`.

These are source-embedding and operator-norm obligations.  No new principal action obstruction is presently visible.

## 14. Consequence

The corrected conclusion is

\[
\boxed{
O(S)\text{ designated orbit modes}
\Longrightarrow
\begin{cases}
\text{polynomial fixed-order source losses},\\
\text{plus a controllable analytic factor }e^{\sigma O(S)}.
\end{cases}
}
\]

For the explicit choice `sigma=0.005`, the analytic factor is strictly dominated by the physical boundary and nonlinear action gaps.

The preferred next theorem is therefore an **exact designated-orbit/complement propagator theorem** for the phase-adapted nonzero block, followed by the already proved mean fixed point.

No exact unforced reset cell or infinite cascade is claimed until that port is complete.
