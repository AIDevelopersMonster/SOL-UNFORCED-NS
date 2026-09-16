# `C^1` parameter transfer for the low-`u` coupled correction

**Status:** PROVED ASYMPTOTIC `C^1` SMALLNESS OF THE EXACT COUPLED PDE CORRECTION IN ACTION-NORMALIZED OUTPUT COORDINATES / FINAL FINITE-DIMENSIONAL RESET IFT IS THE NEXT STEP.

The coupled Banach theorem
`beta21_lowu_coupled_mean_nonzero_contraction.md`
produces, for frozen macroscopic parameters

\[
p=(\kappa,\theta,A_M),
\]

one exact local residual correction

\[
U_S(p):=(m_S(p),z_S(p)).
\]

The remaining question is whether the exact PDE correction can destroy the already proved principal finite-dimensional transversality.  This note proves that it cannot: in action-normalized outgoing coordinates the correction map and its first parameter derivative tend to zero.

No global cascade is claimed here.

## 1. Parameter neighborhood

Let

\[
p_*=(\kappa_*,\theta_*,A_{M,*})
\]

be the principal boundary-layer reset point from
`beta21_lowu_boundary_layer_bilateral_orbit_reset.md`.

Fix one sufficiently small compact neighborhood

\[
K_p\Subset\mathbb R^3
\]

on which:

1. the strict source/orbit core remains unchanged;
2. the weighted action margins stay positive;
3. the root Cauchy/curl construction remains transverse;
4. the designated shift propagators remain uniformly bounded;
5. the principal reset Jacobian remains a fixed positive distance from singularity.

All estimates below are uniform on `K_p`.

## 2. Parameter-dependent coupled map

Write the exact correction equation as

\[
\boxed{
U=\mathcal T_S(p;U),
\qquad U=(m,z).
}
\tag{C1}

The coupled theorem gives, in the weighted product norm `||.||_{*,S}`,

\[
\boxed{
\|D_U\mathcal T_S(p;U)\|
\le q_{*,S}<1/2
}
\tag{C2}

for all sufficiently large `S`, uniformly for `p in K_p` and `U` in the shrinking invariant ball.

Hence

\[
\boxed{
\|(I-D_U\mathcal T_S)^{-1}\|
\le\frac1{1-q_{*,S}}\le2.
}
\tag{C3}

## 3. `C^1` regularity of the building blocks

Every parameter dependence enters through a finite family of smooth normalized coefficients:

- boundary-layer spacing `delta_S=kappa/S`;
- parent phase angle `theta`;
- designated root amplitude `A_M`;
- corresponding finite shift coefficients and source frame data.

The earlier source audits prove that, at each fixed physical/source derivative order and fixed parameter-differentiation order, parameter differentiation costs only a fixed power of `S`:

\[
\boxed{
C_{m,1}^{param}(S)\le C_mS^{B_m}.
}
\tag{C4}

The root-augmented mean propagator satisfies the same polynomial parameter bound, and the weighted off-orbit/covariance estimates retain their positive action or epsilon factors under first parameter differentiation.

Therefore the complete coupled map is `C^1` on

\[
K_p\times B_{r_{*,S}}.
\]

## 4. Derivative of the inhomogeneous defect

Let

\[
R_{*,S}(p):=\|\mathcal T_S(p;0)\|_{*,S}.
\]

The coupled theorem gives

\[
R_{*,S}\to0.
\]

Every parameter derivative of an inhomogeneous source term costs at most one polynomial factor and preserves the source-small mechanism.  Hence for some fixed `B`,

\[
\boxed{
\|D_p\mathcal T_S(p;0)\|_{*,S}
\le
S^B R_{*,S}^{sharp},
}
\tag{C5}

where

\[
R_{*,S}^{sharp}
\le
S^A\varepsilon^{a_*}+S^Ae^{-cS}
\tag{C6}
\]

for one fixed

\[
\boxed{a_*>0.}
\]

Thus

\[
\boxed{S^BR_{*,S}^{sharp}\to0.}
\tag{C7}

## 5. Derivative on the shrinking ball

For `U` in the invariant ball,

\[
\|U\|_{*,S}\le2R_{*,S}.
\]

Differentiate all coefficient and bilinear terms in `p`.  A differentiated term either:

1. differentiates an inhomogeneous source and is controlled by (C5), or
2. differentiates a coefficient multiplying `U`, producing at most
   \[
   S^B\|U\|_{*,S},
   \]
3. differentiates one off-orbit/action-small block, preserving `e^{-cS}`, or
4. differentiates one covariance-return block, preserving a positive epsilon exponent.

Therefore

\[
\boxed{
\sup_{U\in B_{r_{*,S}}}
\|D_p\mathcal T_S(p;U)\|_{*,S}
\le
S^B\left(R_{*,S}^{sharp}+R_{*,S}\right)
=o(1).
}
\tag{C8}

## 6. Parameter derivative of the exact fixed point

Differentiate

\[
U_S(p)=\mathcal T_S(p;U_S(p)).
\]

Then

\[
\left(I-D_U\mathcal T_S\right)D_pU_S
=D_p\mathcal T_S.
\tag{C9}

Using (C3) and (C8),

\[
\boxed{
\|D_pU_S(p)\|_{*,S}
\le2
\|D_p\mathcal T_S(p;U_S(p))\|_{*,S}
=o(1).
}
\tag{C10}

Thus the exact coupled correction is `C^1` in the macroscopic reset parameters and its first derivative vanishes asymptotically in the product correction norm.

## 7. Outgoing finite-dimensional observables

Let

\[
\mathcal O_S^{out}(p;U)
\in\mathbb R^3
\]

be the three action-normalized reset observables:

1. the catalyst multiplier error;
2. the real part of the parent multiplier error;
3. the imaginary part of the parent multiplier error.

At `U=0`, these are the finite-`S` principal Poincare observables.

The output extraction map is a fixed finite trace/projection on the designated orbit plus source-normalized reconstruction.  Its fixed derivative order costs at most a polynomial power of `S`.  Therefore

\[
\boxed{
\|D_U\mathcal O_S^{out}\|
\le CS^{B_O}.
}
\tag{C11}

Since

\[
\|U_S\|_{*,S}
+\|D_pU_S\|_{*,S}
=o(S^{-B_O}),
\]

after absorbing the fixed polynomial into the positive source exponent, one obtains

\[
\boxed{
\mathcal O_S^{exact}(p)
:=\mathcal O_S^{out}(p;U_S(p))
=
\mathcal O_S^{principal}(p)+o(1)
}
\tag{C12}

and

\[
\boxed{
D_p\mathcal O_S^{exact}(p)
=
D_p\mathcal O_S^{principal}(p)+o(1)
}
\tag{C13}

uniformly on a sufficiently small fixed neighborhood of `p_*`.

## 8. Principal Jacobian

The principal catalyst scalar derivative is

\[
\boxed{
\lambda_C-\rho_C^{-1}
=-5.83150782219\ldots\ne0.
}
\tag{C14}

For the complex parent equation,

\[
\boxed{
\det D_{(\kappa,\theta)}
(\Re F_P,\Im F_P)
=1.2199224287\ldots\ne0.
}
\tag{C15}

The full three-real-variable principal Jacobian is block triangular to leading order, with one catalyst scalar block and the two-dimensional parent block.  Hence

\[
\boxed{
\det J_0\ne0.
}
\tag{C16}

## 9. Persistence of exact rank

By (C13),

\[
D_p\mathcal O_S^{exact}
=J_0+o(1)
\]

after the already proved finite-`S` `O(S^{-1})` principal correction is included.

Therefore there exists `S_0` such that for every `S>=S_0`,

\[
\boxed{
|\det D_p\mathcal O_S^{exact}|
\ge\frac12|\det J_0|>0.
}
\tag{C17}

Thus the exact Navier--Stokes correction cannot destroy the principal reset transversality.

## 10. Remaining step

The remaining local theorem is now purely finite-dimensional:

- use the exact finite-`S` principal approximate zero
  \[
  p_S^{principal}=p_*+O(S^{-1});
  \]
- use (C12) to show the exact PDE-corrected reset defect at that point is `o(1)`;
- use (C17) and the finite-dimensional implicit-function theorem to obtain one exact parameter triple
  \[
  p_S^{exact}
  \]
  with zero reset observable.

No infinite-dimensional PDE inversion remains in this final local step.

## 11. Consequence

The local low-`u` programme has now crossed the following threshold:

\[
\boxed{
\text{principal transverse reset}
+
\text{exact coupled PDE correction}
\Longrightarrow
\text{exact reset map remains transverse.}
}
\]

The next file should state and prove the exact finite-`S` local reset theorem.  Only after that theorem is established should the programme return to inter-cell assembly and the infinite cascade question.
