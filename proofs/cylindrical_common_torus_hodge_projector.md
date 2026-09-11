# Cylindrical/common-torus Hodge projector after radial phase straightening

**Status:** PROVED LOCAL PROJECTOR THEOREM ON A FIXED ANNULAR COLLAR WITH IMPERMEABLE RADIAL BOUNDARY.

This note closes the first analytic obligation left by `elliptic_leray_mean_forward_reduction.md` in the natural local boundary realization. The key observation is that the apparently large radial phase derivative in the source geometry is a pure gauge: on a fixed annular collar it is removed exactly by a torus translation depending on `R`. After that conjugation the meridional Hodge problem is the ordinary axisymmetric Hodge problem, with the auxiliary torus acting only as a parameter. No Diophantine denominator occurs.

Throughout, the collar is

\[
\Omega=\{R_0<R<R_1\}\times\mathbb T_Z\times\mathbb T_y^2,
\qquad R_0>0,
\]

with fixed `R_0,R_1` independent of the dyadic level. The physical angular mean has already been taken, so the velocity unknown is

\[
m=(\beta,v,\gamma).
\]

The swirl component `v` is automatically orthogonal to the meridional divergence constraint and is therefore left unchanged by the meridional Hodge projector.

## 1. Source radial derivative is an exact gauge transform

On the common torus chart the radial derivative has the form

\[
\boxed{
D_r=\partial_R+a_\ell(R)L_r,
\qquad
L_r=v_r\cdot\partial_y,
}
\tag{HP1}
\]

with

\[
a_\ell(R)=M_r d_rR^{d_r-1}.
\]

Let

\[
\Phi_\ell(R)=\int_{R_0}^R a_\ell(s)\,ds.
\tag{HP2}
\]

Define the `R`-dependent torus translation

\[
\boxed{
(\mathcal U_\ell f)(R,Z,y)
:=f(R,Z,y+\Phi_\ell(R)v_r).
}
\tag{HP3}
\]

Because torus translation is an isometry in every translation-invariant Sobolev, analytic, or Gevrey norm in `y`, `U_ell` and `U_ell^{-1}` have norm one in the torus variables.

A direct calculation gives

\[
\boxed{
D_r=\mathcal U_\ell^{-1}\partial_R\mathcal U_\ell.
}
\tag{HP4}
\]

Thus the large phase parameter `M_r` is absent from the conjugated radial derivative.

The source axial derivative on this mean patch is

\[
D_z=\varepsilon\partial_Z,
\tag{HP5}
\]

which commutes with `U_ell`.

## 2. Divergence and streamfunction

The mean divergence constraint is

\[
\boxed{
(D_r+R^{-1})\beta+D_z\gamma=0.
}
\tag{HP6}
\]

After conjugation,

\[
\tilde\beta=\mathcal U_\ell\beta,
\qquad
\tilde\gamma=\mathcal U_\ell\gamma,
\]

it becomes

\[
\boxed{
(\partial_R+R^{-1})\tilde\beta
+\varepsilon\partial_Z\tilde\gamma=0.
}
\tag{HP7}
\]

Every sufficiently regular meridional field satisfying (HP7) and zero radial normal trace

\[
\tilde\beta|_{R=R_0,R_1}=0
\tag{HP8}
\]

may be represented by a streamfunction `Psi` with Dirichlet radial boundary condition:

\[
\boxed{
\tilde\beta=-\varepsilon\partial_Z\Psi,
\qquad
\tilde\gamma=(\partial_R+R^{-1})\Psi,
\qquad
\Psi|_{R=R_0,R_1}=0.
}
\tag{HP9}
\]

The condition `Psi=0` on a radial face implies `tilde beta=0` there because the boundary value vanishes identically as a function of `Z,y`.

## 3. Meridional vorticity operator

Define the azimuthal meridional vorticity

\[
\omega
:=D_z\beta-D_r\gamma.
\tag{HP10}
\]

In straightened variables,

\[
\tilde\omega
=\varepsilon\partial_Z\tilde\beta-\partial_R\tilde\gamma.
\]

Substituting (HP9) gives

\[
\boxed{
\tilde\omega=-\mathcal E_\varepsilon\Psi,
}
\tag{HP11}
\]

where

\[
\boxed{
\mathcal E_\varepsilon
:=
-\partial_R(\partial_R+R^{-1})
-\varepsilon^2\partial_Z^2.
}
\tag{HP12}
\]

Equivalently,

\[
\mathcal E_\varepsilon\Psi
=-\partial_R^2\Psi-R^{-1}\partial_R\Psi+R^{-2}\Psi
-\varepsilon^2\partial_Z^2\Psi.
\tag{HP13}
\]

This is the standard positive axisymmetric order-one Bessel/Stokes streamfunction operator on an annulus.

## 4. Coercivity has no torus small divisor

Use the cylindrical measure `R dR dZ dy`. Integration by parts with the Dirichlet boundary condition gives

\[
\boxed{
\langle \mathcal E_\varepsilon\Psi,\Psi\rangle
=
\|\partial_R\Psi\|_{L^2_R}^2
+\|R^{-1}\Psi\|_{L^2_R}^2
+\varepsilon^2\|\partial_Z\Psi\|_{L^2_R}^2.
}
\tag{HP14}
\]

Since `R_0>0` and the radial interval is fixed, Poincare gives

\[
\boxed{
\|\Psi\|_{H^1_{R,\varepsilon Z}}
\le C_I\|\mathcal E_\varepsilon\Psi\|_{H^{-1}_{R,\varepsilon Z}}.
}
\tag{HP15}
\]

Most importantly, the auxiliary torus frequency `k in Z^2` does not enter the coercivity constant at all after the gauge transform. In the original variables the same statement is therefore uniform in both `k` and the radial phase parameter `M_r`.

This removes the two candidate pathologies that appeared in the previous radial attempts:

- there is no division by `v_r dot k`;
- there is no radial Cauchy factor `exp(c epsilon |xi| Delta R)`.

The Hodge problem is a two-sided spatial elliptic boundary-value problem, not a one-sided spatial evolution.

## 5. Scalar Neumann formulation of the projector

For a general meridional field `F=(F_r,F_z)`, define `phi` by

\[
\boxed{
-\mathcal L_\varepsilon\phi
:=
-\left[(\partial_R+R^{-1})\partial_R
+\varepsilon^2\partial_Z^2\right]\phi
=\operatorname{div}_\varepsilon F
}
\tag{HP16}
\]

with the standard normal-trace Neumann condition

\[
\partial_R\phi|_{R=R_0,R_1}=F_r|_{R=R_0,R_1},
\tag{HP17}
\]

and zero weighted spatial mean fixing the additive constant. Then

\[
\boxed{
\mathbb P_{\rm cyl}F
:=F-\nabla_\varepsilon\phi,
\qquad
\nabla_\varepsilon=(\partial_R,\varepsilon\partial_Z),
}
\tag{HP18}
\]

satisfies

\[
\operatorname{div}_\varepsilon\mathbb P_{\rm cyl}F=0,
\qquad
(\mathbb P_{\rm cyl}F)_r|_{\partial I}=0.
\tag{HP19}
\]

The standard compatibility condition for the Neumann problem is exactly the divergence theorem and therefore holds identically for (HP16)-(HP17).

Define the common-torus projector by conjugation:

\[
\boxed{
\mathbb P_*
:=\mathcal U_\ell^{-1}\mathbb P_{\rm cyl}\mathcal U_\ell
}
\tag{HP20}
\]

on the meridional pair and let it act as the identity on the swirl component.

Then

\[
\boxed{
\operatorname{div}_*\mathbb P_*F=0,
\qquad
\mathbb P_*\nabla_*p=0
}
\tag{HP21}
\]

for gradients satisfying the same boundary realization.

## 6. Same-radius torus Gevrey boundedness

Let the characteristic Gevrey norm use a Fourier weight

\[
e^{\lambda |k|^{1/s}}
\]

in the auxiliary torus variables and a finite fixed collection of normalized spatial derivatives in `(R,epsilon Z)`. Because `P_cyl` acts independently on each auxiliary torus mode after straightening and its elliptic constants are independent of `k`,

\[
\boxed{
\|\mathbb P_{\rm cyl}F\|_{Y_{s,\lambda}}
\le C_{I,m}\|F\|_{Y_{s,\lambda}}.
}
\tag{HP22}
\]

The conjugating map `U_ell` is a translation in `y`; if radial derivatives are measured through the characteristic derivative `D_r`, (HP4) shows that the same norm is preserved exactly under the conjugation. Hence

\[
\boxed{
\|\mathbb P_*F\|_{Y_{s,\lambda}}
\le C_{I,m}\|F\|_{Y_{s,\lambda}},
}
\tag{HP23}
\]

with a constant independent of

\[
\ell,\quad M_r,\quad k.
\]

No Gevrey radius loss is required for the projector itself.

## 7. What the theorem does and does not solve

This note proves the precise projector statement requested in (EL10) of `elliptic_leray_mean_forward_reduction.md`, **for the impermeable radial boundary realization**.

It does not claim that this boundary realization is already compatible with the final global relay inheritance. In particular, the local theorem may carry tangential velocity/stress traces across the radial faces, but the normal meridional component is fixed to zero at the artificial radial boundary.

Thus the remaining local question is no longer Hodge boundedness. It is whether the full projected Oseen/Stokes mean operator, with the source base coefficients and designated-wave linearization, generates a dyadic-uniform forward propagator in the same characteristic Gevrey norm.

## 8. Immediate consequence

The first item in the pressure-repair frontier is closed:

\[
\boxed{
\mathbb P_*:Y_{s,\lambda}\to Y_{s,\lambda}
\text{ is bounded uniformly after exact radial phase straightening.}
}
\tag{HP24}
\]

The next target is the variable-coefficient projected evolution

\[
t_*m=\mathbb P_*\left[\varepsilon\Delta_*m+\mathcal B_0m\right]+F,
\tag{HP25}
\]

where `B_0` contains the frozen base transport and zeroth-order swirl/geometry couplings. The required theorem is a uniform energy/Gevrey estimate for (HP25) on the fixed temporal collar.
