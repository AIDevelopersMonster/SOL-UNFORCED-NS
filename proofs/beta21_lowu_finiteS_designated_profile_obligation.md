# Finite-`S` designated orbit profile obligation for the low-`u` reset

**Status:** CORRECTION / MISSING THEOREM IDENTIFIED.  The current branch proves the limiting bilateral geometric fixed profile, the exact coupled PDE correction around a prescribed designated orbit, and three macroscopic finite-`S` reset observables.  It does **not yet contain a proof that the complete variable-coefficient finite-`S` `O(S)` designated orbit is an exact fixed vector of the one-cell Poincare map**.

Accordingly, `beta21_lowu_exact_finiteS_local_reset.md` must presently be read as conditional on the full-profile theorem isolated here.  Its zero-residual coupled correction theorem remains valid for the prescribed designated principal state; what is not yet justified is the inference from three scalar multiplier equations to exact equality of every designated orbit coordinate at the reset face.

This note derives the correct boundary-layer profile equation and reduces the missing `O(S)` fixed-vector problem to a one-dimensional continuum profile problem plus a discrete convergence theorem.

No global cascade claim is made.

## 1. Why three scalar reset observables are not enough

The limiting principal orbit equations are shift invariant:

\[
\mathcal P_C^{(0)}=R^{-1}e^{\lambda_CR},
\qquad
\mathcal P_P^{(0)}=R^{-2}e^{\mu_PR}.
\]

Therefore geometric shift eigenvectors

\[
Rc=\rho_Cc,
\qquad
Rq=\rho_Pq
\]

reduce the fixed-vector condition to the scalar dispersion equations

\[
\frac{e^{\lambda_C\rho_C}}{\rho_C}=1,
\qquad
\frac{e^{\mu_P\rho_P}}{\rho_P^2}=1.
\tag{FP1}
\]

At finite `S`, however, the exact normalized pulse/viscous rates depend on the orbit slope

\[
z_j=x+O(j/S).
\]

Thus the finite-`S` designated generator contains variable coefficients across the orbit core.  In general

\[
[\mathcal P_{b,S},R]\ne0.
\tag{FP2}
\]

Consequently a geometric limiting vector is not automatically an exact finite-`S` eigenvector.

The current numerical audit records scalar multiplier convergence and the current exact-reset theorem tunes three real observables.  Those facts do not imply

\[
\boxed{\mathcal P_{b,S}U_{b,S}=U_{b,S}}
\tag{FP3}
\]

in all `O(S)` designated coordinates.

## 2. The perturbation is singular at the profile level

The designated block has width

\[
N_S\asymp S.
\]

For a translation-invariant truncated shift, spectral separation near the fixed geometric mode is at best of order

\[
N_S^{-1}=O(S^{-1}).
\]

The finite-`S` coefficient variation is also recorded at order

\[
O(S^{-1})
\]

per one lattice step in the boundary-layer expansion.

Therefore a naive finite-dimensional eigenvector perturbation estimate of the form

\[
\|\mathcal P_{b,S}-\mathcal P_b^{(0)}\|=O(S^{-1})
\]

does not yield a uniform inverse on the complement of the limiting eigenvector.  The perturbation and spectral gap occur at the same scale.

The missing theorem is a singular boundary-layer profile problem, not a routine matrix perturbation.

## 3. Natural central scaling

Physical large-deviation localization gives

\[
H_b(x)=H_b'(x)=0,
\qquad
H_b''(x)<0.
\]

Hence physically relevant designated mass is concentrated at

\[
|j|=O(\sqrt S).
\]

Introduce

\[
\boxed{h_S:=S^{-1/2},\qquad y=jh_S.}
\tag{FP4}
\]

The orbit slope then has the form

\[
z_j=x+d_bh_Sy+O(S^{-1}),
\tag{FP5}
\]

where at the limiting working point

\[
d_C=2\kappa_*,
\qquad
d_P=\kappa_*.
\]

This is the same profile scaling used in
`beta21_lowu_dyadic_profile_resampling.md`.

## 4. Remove the limiting geometric factor

Write the catalyst and parent sequences as

\[
c_j=\rho_C^{\,j}f_C(y),
\qquad
q_j=\rho_P^{\,j}f_P(y).
\tag{FP6}
\]

Choose the shift convention so that on such profiles

\[
R=\rho_b e^{h_S\partial_y}
\tag{FP7}
\]

up to the harmless orientation choice `h_S -> -h_S`.

The limiting fixed relation ensures

\[
\mathcal P_b^{(0)}(\rho_b^j)=\rho_b^j.
\]

Thus the tangent-normalized profile `f_b` is the correct finite-`S` unknown.

## 5. Shift contribution to the profile normal form

For the catalyst,

\[
\mathcal P_C^{(0)}(R)=R^{-1}e^{\lambda_CR}.
\]

Using (FP7),

\[
\log\mathcal P_C^{(0)}
=
\lambda_C\rho_C e^{h_S\partial_y}
-\log\rho_C-h_S\partial_y.
\]

Since

\[
\lambda_C\rho_C=\log\rho_C,
\]

the zeroth-order term vanishes and

\[
\boxed{
\log\mathcal P_C^{(0)}
=h_Sv_C\partial_y+O(h_S^2\partial_y^2),
}
\tag{FP8}

with

\[
\boxed{
v_C:=\lambda_C\rho_C-1
=\log\rho_C-1
\ne0.
}
\tag{FP9}

Numerically,

\[
v_C\approx-2.0469330156.
\]

For the parent,

\[
\mathcal P_P^{(0)}(R)=R^{-2}e^{\mu_PR},
\]

and similarly

\[
\boxed{
\log\mathcal P_P^{(0)}
=h_Sv_P\partial_y+O(h_S^2\partial_y^2),
}
\tag{FP10}

where

\[
\boxed{
v_P:=\mu_P\rho_P-2\ne0.}
\tag{FP11}

At the working point,

\[
\mu_P\rho_P
\approx1.8148290071-1.0443517757i,
\]

so

\[
\boxed{
v_P\approx-0.1851709929-1.0443517757i.}
\tag{FP12}

Thus both profile equations have a nondegenerate first-order transport term.

## 6. Finite-`S` coefficient variation

The exact normalized generator coefficients are smooth functions of reduced slope.  With (FP5), Taylor expansion gives

\[
A_b(z_j)
=A_b(x)
+h_Sd_bA_b'(x)y
+O\bigl(h_S^2(1+y^2)\bigr).
\tag{FP13}

After the constant part is incorporated in the limiting dispersion relation, the first finite-`S` contribution to the one-cell map is therefore multiplication by an affine function of `y`:

\[
\boxed{
h_S(B_by+C_b).}
\tag{FP14}

The coefficients `B_b,C_b` are explicit finite combinations of first derivatives of the exact source pulse/viscous/root-shift coefficients at the working point and derivatives of the finite-`S` reset parameters.

They have **not yet been computed in the branch**.  Computing them from the actual finite-`S` designated generator is the next concrete step.

## 7. Leading continuum fixed-profile equation

Combining (FP8)--(FP14), the tangent-normalized finite-`S` fixed-vector equation has the formal expansion

\[
\boxed{
\mathcal P_{b,S}^{tan}
=I+h_S\mathcal L_b+O(h_S^2),
}
\tag{FP15}

with

\[
\boxed{
\mathcal L_b
=v_b\partial_y+B_by+C_b.
}
\tag{FP16}

Therefore the leading continuum profile must satisfy

\[
\boxed{
\mathcal L_bf_b=0.
}
\tag{FP17}

Because `v_b != 0`, this equation is explicitly solvable:

\[
\boxed{
f_b(y)
=A_b^{prof}
\exp\left(
-\frac{B_b}{2v_b}y^2
-\frac{C_b}{v_b}y
\right).
}
\tag{FP18}

Thus the missing `O(S)` eigenvector problem reduces at leading order to a Gaussian/shifted-Gaussian profile, not a dense matrix inversion.

## 8. Localization criterion

The physical designated profile must lie in the existing large-deviation weighted sequence space.  The continuum profile (FP18) is admissible if its Gaussian exponent is compatible with the physical action confinement.

A sufficient condition is

\[
\boxed{
\Re\left(\frac{B_b}{v_b}\right)>-2a_bd_b^2,
}
\tag{FP19}

where

\[
H_b(x+s)=-a_bs^2+O(s^3),
\qquad a_b>0.
\]

A stronger and cleaner target is

\[
\boxed{
\Re(B_b/v_b)>0,
}
\tag{FP20}

which makes the coefficient profile itself Gaussian-decaying before the physical action weight is applied.

The exact sign must be computed; it must not be assumed from the already-known concavity of `H_b`.

## 9. Required discrete theorem

Once `B_b,C_b` are known and the continuum profile is admissible, the publication-level finite-`S` theorem must prove the existence of exact discrete profiles

\[
f_{b,S}
\]

such that

\[
\boxed{
\mathcal P_{b,S}^{tan}f_{b,S}=f_{b,S}
}
\tag{FP21}

and

\[
\boxed{
f_{b,S}\to f_b}
\tag{FP22}
\]

in a Gaussian profile norm under the interpolation `y=j/sqrt(S)`.

Because the leading operator (FP16) is first order with `v_b != 0`, the natural proof is a discrete Volterra/transport argument in `y`, not a uniform inverse of the full `O(S)` matrix.

Boundary data are supplied in the exponentially small action tails, so the choice of one normalization constant `A_b^{prof}` fixes the interior profile.

## 10. Coupling to the exact PDE correction

The coupled mean/nonzero contraction theorem remains useful once (FP21) is established.  It solves all **non-designated** mean and nonzero harmonics around the exact designated profile.

Its correction radius is source-small:

\[
R_S\le S^A\varepsilon^{a_*}+S^Ae^{-cS}.
\]

Therefore the PDE correction perturbs the designated profile equation only by a source-small term.  The exact discrete profile theorem should be proved first at principal level and then upgraded by the same `C^1` contraction/IFT mechanism already used for the macroscopic parameters.

## 11. Correction to the present theorem chain

Until (FP21) is proved, the following statement in
`beta21_lowu_exact_finiteS_local_reset.md`

> “the outgoing beta-one/beta-two bilateral orbit is exactly reset in every designated coordinate”

is not yet justified by the current scalar-observable argument.

The valid current conclusion is narrower:

\[
\boxed{
\text{exact zero residual around the prescribed finite-`S` designated state}
\,+\,
\text{exact macroscopic scalar reset observables}.
}
\tag{FP23}

The full exact local reset theorem is restored once the finite-`S` designated profile equation (FP21) is closed.

## 12. Next attack

The next calculation is now sharply local:

1. write the exact finite-`S` catalyst and parent designated principal generators on the orbit core;
2. expand their coefficients at
   \[
   z=x+d_bj/S;
   \]
3. compute `B_C,C_C,B_P,C_P` in (FP14);
4. test the Gaussian admissibility condition (FP19);
5. construct the exact discrete fixed profiles by a first-order difference/Volterra scheme;
6. reinsert the source-small coupled PDE correction.

This obligation precedes any further global inter-cell assembly theorem.
