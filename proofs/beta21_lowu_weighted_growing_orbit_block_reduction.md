# Weighted growing-orbit block reduction for the low-`u` boundary-layer cell

**Status:** PROVED FUNCTIONAL-ANALYTIC REDUCTION FOR THE PRINCIPAL `O(S)` ORBIT BLOCK / UNIFORM SOURCE-NORM AND EXACT ZERO-RESIDUAL VERIFICATION STILL OPEN. This note addresses the first objection to `beta21_lowu_boundary_layer_bilateral_orbit_reset.md`: the designated beta-one/beta-two orbit block contains `O(S)` Fourier characters, whereas the earlier phase-adapted closure theorems were stated for fixed finite critical blocks.

The dimension growth is not itself an obstruction. After conjugation by the physical large-deviation weights, the only order-one operator is the beta-zero `M`-translation shift, which is solved exactly by its semigroup. Every other orbit interaction has either a fixed negative action gap or belongs to the uniformly stable beta-three-and-higher complement. The `O(S)` mode count then contributes only polynomial factors, which are dominated by the fixed exponential gaps.

The remaining PDE obligation is source-specific: verify that the curl reconstruction, nonzero stable inverse, mean return, and their parameter derivatives retain the same polynomial-in-`S` constants for this growing packet family. This note does not silently assume that verification.

## 1. Working point and core

Freeze

\[
u=1.8,
\qquad
x=0.70,
\qquad
\kappa=0.894049167184884\ldots,
\]

and

\[
\delta_S=\kappa/S.
\]

Use the strict orbit core

\[
\boxed{|z-x|\le w,\qquad w=0.03.}
\]

The beta-one orbit `C_j=C+jM` has slope spacing

\[
|z_{j+1}-z_j|=2\delta_S=\frac{2\kappa}{S}.
\]

Therefore the number of beta-one indices in the core satisfies

\[
\boxed{
N_{C,S}
\le 2+\frac{wS}{\kappa}
=O(S).
}
\tag{GB1}
\]

Numerically,

\[
\frac{w}{\kappa}=0.0335552\ldots.
\]

The beta-two orbit has spacing `delta_S`, and hence also contains only `O(S)` indices on the same fixed core.

## 2. Physical large-deviation weights

For `b=1,2` define

\[
H_b(z)
=\mathcal E_b(z)-\mathcal E_b(x)+(x-z)g_b,
\qquad
g_b=u\Gamma_b(x).
\]

By the strict decrease of `Gamma_b` on positive slopes,

\[
H_b(z)\le0,
\]

with equality only at `z=x`.

For an orbit coefficient vector `a=(a_j)` define the physical weighted norm

\[
\boxed{
\|a\|_{b,S}^2
:=\sum_j |a_j|^2 e^{2S H_b(z_j)}.
}
\tag{GB2}
\]

This norm records the actual exponential size of the bilateral fixed profile rather than the possibly growing normalized geometric coefficient.

## 3. Uniform boundedness of the shift

Let `R` be the unit orbit shift. Because the slope step is `O(S^{-1})`, the mean-value theorem gives

\[
S\bigl(H_b(z_{j+1})-H_b(z_j)\bigr)
=O(1)
\]

uniformly in `S` and in every index contained in the compact core.

More explicitly, if

\[
L_b:=\sup_{z\in[x-w,x+w]}|H_b'(z)|,
\]

then

\[
\left|
S(H_b(z_{j+1})-H_b(z_j))
\right|
\le c_b\kappa L_b
\]

with `c_1=2` and `c_2=1` for the beta-one and beta-two orbit spacings.

Consequently there exists a design constant `K_R`, independent of `S`, such that

\[
\boxed{
\|R\|_{\ell^2_{b,S}\to\ell^2_{b,S}}
+\|R^{-1}\|_{\ell^2_{b,S}\to\ell^2_{b,S}}
\le K_R.
}
\tag{GB3}
\]

The principal `M`-translation semigroups

\[
e^{\lambda_C R},
\qquad
e^{\mu_P R}
\]

therefore have `S`-uniform operator norms on the weighted spaces:

\[
\boxed{
\|e^{\lambda_C R}\|
\le e^{|\lambda_C|K_R},
\qquad
\|e^{\mu_P R}\|
\le e^{|\mu_P|K_R}.
}
\tag{GB4}

Thus no `N_S`-dependent matrix inverse is required for the only order-one part of the critical dynamics.

## 4. Truncation at the physical core boundary

At `x=0.70`, `w=0.03`, the physical localization audit gives

\[
H_1(x\pm w)\le-8.61\times10^{-4},
\]

\[
H_2(x\pm w)\le-2.106\times10^{-3}.
\]

Hence the truncated bilateral eigenprofile has boundary size

\[
\boxed{
O\!\left(e^{-c_{bd}S}\right),
\qquad
c_{bd}=8.6\times10^{-4}.
}
\tag{GB5}

Any fixed power of `S` is dominated by this boundary loss:

\[
S^A e^{-c_{bd}S}\to0
\]

for every fixed `A`.

This is the correct interpretation of the finite orbit core: it is not a hard algebraic cut in normalized coefficient space; it is an exponentially accurate physical truncation.

## 5. Convolution counting in an `O(S)` block

Quadratic orbit interactions are discrete convolutions of coefficient sequences. For a finite sequence supported on at most `N_S=O(S)` indices,

\[
\|a\|_{\ell^1}
\le N_S^{1/2}\|a\|_{\ell^2}.
\]

Therefore Young's inequality gives schematically

\[
\boxed{
\|a*b\|_{\ell^2}
\le C S^{1/2}
\|a\|_{\ell^2}\|b\|_{\ell^2}.
}
\tag{GB6}

The same estimate holds in the physical weighted norms after conjugating by the smooth core weights; the weight-ratio constants are uniform by compactness and (GB3).

Thus the growth of the critical dimension costs only a polynomial factor `S^{1/2}` at quadratic order, not an exponential factor.

Even a cruder direct pair count would cost only a fixed power of `S` and leads to the same asymptotic conclusion below.

## 6. Fixed action gaps beat growing dimension

The principal core audit in the companion theorem gives

\[
\gamma_{11}
\ge0.05925018225\ldots
\]

for non-`M` beta-one sum feedback

\[
C+C\to Q,
\]

and

\[
\gamma_{21}
\ge0.11675015251\ldots
\]

for beta-two/beta-one difference feedback

\[
Q-C\to C.
\]

Put

\[
\gamma_{crit}=0.05925.
\]

After physical action normalization, every such non-`M` quadratic contribution carries

\[
e^{-\gamma_{crit}S}.
\]

Combining with (GB6),

\[
\boxed{
\|\mathcal N_{crit}^{nonM}(a)\|_S
\le C S^{1/2}e^{-\gamma_{crit}S}
\|a\|_S^2.
}
\tag{GB7}

Therefore

\[
S^{1/2}e^{-0.05925S}\to0.
\]

In particular the complete non-`M` critical orbit feedback is a small perturbation of the exact shift semigroup uniformly as `S->infinity`, despite `N_S->infinity`.

## 7. Higher-beta stable complement

At `u=1.8` and on the full orbit core, direct full-symbol bounds give

\[
\Gamma_3(z)\le-1.8918,
\]

\[
\Gamma_4(z)\le-3.8597,
\]

and increasingly negative bounds for higher beta.

Hence all beta-three-and-higher sum sectors have a uniform normalized dissipative gap independent of `S` and of orbit index.

This is stronger than merely saying that beta-three and beta-four have no real turning points. It yields a genuine uniform stable propagator bound on the compact core.

Thus the growing orbit block does **not** generate a second growing family at higher beta.

## 8. Generated beta-zero harmonics

Differences of equal-beta orbit packets create beta-zero harmonics. The preloaded `M` is the only beta-zero channel retained at order one.

At the orbit center, source actions for newly generated beta-zero harmonics obey the fixed ceilings

\[
2\mathcal E_1(x)
\approx-0.17695,
\]

\[
2\mathcal E_2(x)
\approx-0.23457.
\]

By compactness these remain bounded away from zero on the core. Consequently the generated beta-zero family is exponentially smaller than the preloaded `M` channel, whose boundary-layer action is `O(S^{-1})`.

The number of possible generated beta-zero differences is only polynomial in `S`, so the same exponential-over-polynomial argument places them in the stable/error complement.

## 9. Reduced orbit fixed-point equation

Let

\[
\mathcal L_S
\]

be the finite-`S` principal orbit operator after exact extraction of the `M`-shift semigroup and reset relabelling. Then the preceding estimates give the schematic decomposition

\[
\boxed{
\mathcal L_S
=
\mathcal P_{shift,S}
+\mathcal E_S,
}
\tag{GB8}

where

\[
\|\mathcal E_S\|
\le
C\left(
S^{-1}
+S^A e^{-c_{bd}S}
+S^A e^{-\gamma_{crit}S}
\right)
\tag{GB9}

for some fixed design power `A`, **provided** the source/curl realization of the full orbit bank obeys the same polynomial derivative counting.

The `S^{-1}` term is the already observed finite-`S` coefficient variation; the other two terms are boundary truncation and non-`M` nonlinear feedback.

The limiting shift Poincare map has the transverse fixed point proved in `beta21_lowu_boundary_layer_bilateral_orbit_reset.md`. Its scalar catalyst derivative is separated from zero by approximately `5.83`, while the real parent `(kappa,theta)` Jacobian has determinant approximately `1.22`.

Therefore any exact realization satisfying (GB9) inherits a unique nearby principal fixed state for all sufficiently large `S`.

## 10. What remains to upgrade (GB9) from reduction to theorem

The only unverified input in (GB9) is no longer lattice/action algebra. It is the uniform source/PDE bookkeeping for a packet family whose cardinality grows linearly with `S`.

One must prove, in the existing phase-adapted norms, that:

1. summing `O(S)` curl-generated beta-one/beta-two packets changes source derivative constants by at most a fixed power of `S`;
2. Leray/curl lower-order remainders preserve the fixed action gaps;
3. the infinite nonzero stable inverse is uniform after adjoining the weighted orbit block;
4. the angular-mean forcing acquires only polynomial `S` factors;
5. parameter differentiation in `(kappa,theta,M-amplitude)` also costs only polynomial powers of `S`.

If these hold, every new factor is absorbed by either the existing positive powers of `epsilon` or the fixed exponential action gaps above.

## 11. New frontier

The boundary-layer programme has reduced the autonomy problem to a single explicit estimate family:

\[
\boxed{
\textbf{prove polynomial-in-}S\textbf{ source and correction constants for the }O(S)\textbf{ orbit bank.}
}
\]

No future controls, support-bank renewal, or new lattice generator is required at the principal level.

This is now the preferred next attack.
