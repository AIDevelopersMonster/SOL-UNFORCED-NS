# Absorption of the designated beta-zero root into source `BaseBounds`

**Status:** PROVED SOURCE-CLASS REDUCTION / WHOLE-SPACE LERAY--OSEEN REALIZATION STILL OPEN.  The exact source mean-increment calculus does not require the designated beta-zero root to be part of the small cumulative mean correction.  The root can be absorbed into the old mean base while preserving exactly the `BaseBounds` hypotheses used by `MeanIncrementBounds`.

This is the correct source-level interpretation of the low-`u` designated root:

\[
\boxed{
b^\sharp=b+M_{des}.}
\]

The residual mean correction is then solved with the **same source exponent ledger** as before.  In particular the root does not lower the signs of the radial/theta/axial remainder exponents.

No exact whole-space reset cell is claimed here; the remaining issue is to realize this source-admissible enlarged base in the exact whole-space Leray--Oseen framework.

## 1. Source classes used by the mean equation

The source `MeanIncrementBounds.BaseBounds` requires

\[
\boxed{
 b_r\in U_1,
\qquad
 b_\theta\in U_0,
\qquad
 b_z\in U_0,
}
\tag{BB1}
\]

where `U_alpha` denotes the source unweighted class with epsilon exponent `alpha`.

For a mean weighted class `M_alpha`, `LinearWaveBounds.mean_unweighted` gives

\[
M_\alpha\subset U_\alpha
\]

whenever the source mean weight satisfies `zeta<=1`.  Since `epsilon<=1`, monotonicity in the epsilon exponent gives

\[
\boxed{
\alpha\ge\beta
\Longrightarrow
U_\alpha\subset U_\beta.
}
\tag{BB2}
\]

Thus any positive mean exponent may be weakened to the order-zero base class.

## 2. Angular and axial components of the root

The designated root has normalized physical size

\[
O(h)=O(\varepsilon^{1/2}).
\]

Its principal polarization is

\[
b_M=-S_MK+c_0R_MN,
\]

with no radial component.  The angular/axial components therefore belong to the mean class

\[
\boxed{
M_{des,\theta},M_{des,z}\in M_{1/2}
}
\tag{BB3}
\]

at principal order, with the exact curl/localization remainder in a strictly smaller source class.

By `mean_unweighted` and (BB2),

\[
M_{1/2}\subset U_{1/2}\subset U_0.
\]

Hence

\[
\boxed{
M_{des,\theta},M_{des,z}\in U_0.
}
\tag{BB4}
\]

This is precisely the angular/axial requirement in (BB1).

## 3. Radial component

The principal root polarization has zero radial component.  A radial component is created only by exact curl localization, frame variation and the pointwise transverse projection.

The direct curl theorem gives in the normalized source chart

\[
R_M^{curl}
=O(h^2S\,\operatorname{poly}(S)).
\]

Since

\[
h^2=\varepsilon,
\]

this is an order-one epsilon field up to the polynomial factors already permitted in a source class majorant.  Thus

\[
\boxed{M_{des,r}\in U_1.}
\tag{BB5}
\]

This is exactly the radial requirement in (BB1).

## 4. Enlarged base

Let the old source base be

\[
b=(b_r,b_\theta,b_z)
\]

with `BaseBounds s b`.  Define

\[
\boxed{
b^\sharp
:=(b_r+M_{des,r},
   b_\theta+M_{des,\theta},
   b_z+M_{des,z}).
}
\tag{BB6}
\]

Unweighted classes are closed under finite addition.  Combining the old bounds with (BB4)--(BB5) yields

\[
\boxed{
\operatorname{BaseBounds}(s,b^\sharp).
}
\tag{BB7}
\]

Thus the designated root may be incorporated into the exact source mean base without changing the abstract hypotheses of the source increment theorems.

## 5. Residual increment is still the old high-exponent object

Let `h_corr` be the small residual mean increment and suppose

\[
\operatorname{IncrementBounds}(s,H,h_{corr}),
\qquad H\ge\frac9{10}.
\]

The source theorems in `MeanIncrementBounds` depend on the base only through `BaseBounds`.  Since (BB7) supplies the same hypothesis for `b^sharp`, all of their displayed exponent conclusions remain unchanged.

In particular,

\[
\boxed{
\operatorname{radialRemainder}
\in
M_{H+9/10-2\kappa_s},
}
\tag{BB8}
\]

\[
\boxed{
\operatorname{thetaRemainder}
\in
M_{H+1-2\kappa_s},
}
\tag{BB9}
\]

and, for an admissible pressure increment,

\[
\boxed{
\operatorname{axialRemainder}
\in
M_{H+1-2\kappa_s}.
}
\tag{BB10}
\]

No exponent is reduced by the presence of the designated root.

## 6. Why the principal root self-interaction does not create a new base class

The root principal polarization is transverse to its radial phase covector. Therefore

\[
\Pi_{principal}\mathcal B(M_{des},M_{des})=0.
\]

The exact self-interaction comes only from the order-`epsilon` radial/curl remainder and slow coefficient variation.  These terms are already compatible with the positive source classes used in (BB8)--(BB10).

Thus absorbing `M_des` into `b^sharp` does not introduce an additional order-`M_{1/2}` mean source.

## 7. Orbit covariance remains a forcing, not part of the base

The beta-one/beta-two orbit is not absorbed into `BaseBounds`.  Its conjugate covariance remains on the right-hand side of the mean equation and belongs to the source class

\[
W_{1/2}\times W_{1/2}
\to M_{1-\kappa_s}
\]

up to the polynomial `O(S)` orbit count and the exponentially small off-center/action tails already audited.

Generated `rM`, `r\ne\pm1`, are residual mean-lattice coefficients and are exponentially below the designated root scale.

## 8. Consequence for the local source fixed point

At the exact source graph level the corrected decomposition is

\[
\boxed{
\text{base }b
\quad\longrightarrow\quad
b^\sharp=b+M_{des},
}

followed by the **same** high-exponent residual mean correction scheme as before.

Hence the designated beta-zero root introduces no new source-exponent obstruction.  The remaining obstruction is entirely in the whole-space realization:

1. reconstruct `b^sharp` on `R^3` with the Cauchy/curl root;
2. prove that exact whole-space pressure elimination/Leray and forward mean propagation preserve the source-class exponent ledger for this oscillatory base;
3. couple that mean solve to the growing beta-one/beta-two nonzero orbit.

The next theorem should therefore be a **whole-space Leray realization of source `BaseBounds` with one designated beta-zero root**, not a new local mean algebra theorem.
