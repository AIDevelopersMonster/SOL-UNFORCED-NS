# One-sided radial pressure closure has an axial-frequency Cauchy instability

**Status:** PROVED MODEL OBSTRUCTION / CORRECTION TO THE ONE-SIDED PRESSURE ROUTE.

This note tests the one-sided radial pressure reconstruction from `one_sided_radial_mean_reorganization.md` after coupling it back to incompressibility and the axial mean equation. The first-order radial inverses themselves are bounded. The coupled pressure/divergence system is not: prescribing pressure and meridional potential data on one radial face creates an elliptic Cauchy problem whose resolvent grows exponentially in the axial Fourier frequency.

The conclusion is specific. The algebraic identities in the one-sided radial notes remain valid, but they do **not** furnish a dyadic-uniform bounded mean propagator on Sobolev or compactly supported Gevrey-`s>1` spaces. Pressure must instead be eliminated by a spatial elliptic/Hodge-Leray solve, or one must impose a genuine two-sided elliptic boundary-value problem.

## 1. Principal subsystem sufficient to test boundedness

It is enough to inspect a simplified linear subsystem of the exact mean equations. Set the fixed base and nonlinear source terms to zero, suppress the auxiliary-torus dependence, and retain only incompressibility, pressure, and the axial coupling. This is a legitimate test because failure of boundedness in this invariant subsystem rules out a uniform bound for the larger one-sided system.

Write

\[
D_z=\varepsilon\partial_Z
\]

and use the meridional potential

\[
\boxed{
\beta=-D_z\Psi,
\qquad
\gamma=(\partial_R+R^{-1})\Psi.
}
\tag{PC1}
\]

Let

\[
\boxed{u:=t_*\Psi.}
\tag{PC2}
\]

Ignoring only commutators that vanish in the constant-coefficient test subsystem, the radial pressure equation and the axial momentum equation become

\[
\boxed{
\partial_R p=D_z u,
}
\tag{PC3}
\]

\[
\boxed{
(\partial_R+R^{-1})u+D_zp=0.
}
\tag{PC4}
\]

The proposed one-sided pressure route prescribes an entrance value, for example

\[
\boxed{p(R_0,\cdot)=0}
\tag{PC5}
\]

on an annulus `R in [R_0,R_1]`, `R_0>0`.

## 2. Axial Fourier mode

Take one axial Fourier mode

\[
e^{i\xi Z}
\]

and set

\[
a:=\varepsilon|\xi|.
\]

After a harmless phase rotation of the pressure, define a real variable `q` so that (PC3)-(PC4) become

\[
\boxed{
 u'=a q-\frac{u}{R},
\qquad
 q'=a u.
}
\tag{PC6}
\]

The entrance pressure condition is

\[
q(R_0)=0.
\tag{PC7}
\]

Eliminating `q` gives

\[
\boxed{
 u''+\frac1R u'-\left(a^2+\frac1{R^2}\right)u=0.
}
\tag{PC8}
\]

This is the modified Bessel equation of order one.

## 3. Exact growing branch

The general solution of (PC8) is

\[
\boxed{
 u(R)=A I_1(aR)+B K_1(aR),
}
\tag{PC9}
\]

and, using the standard derivative identities,

\[
\boxed{
 q(R)=A I_0(aR)-B K_0(aR).
}
\tag{PC10}
\]

Condition (PC7) forces

\[
\boxed{
B=A\frac{I_0(aR_0)}{K_0(aR_0)}.
}
\tag{PC11}
\]

Normalize the entrance potential-time trace by

\[
 u(R_0)=u_0\ne0.
\tag{PC12}
\]

Then

\[
A=
\frac{u_0}
{I_1(aR_0)+I_0(aR_0)K_1(aR_0)/K_0(aR_0)}.
\tag{PC13}
\]

For large `a`, the standard asymptotics

\[
I_\nu(x)\sim \frac{e^x}{\sqrt{2\pi x}},
\qquad
K_\nu(x)\sim \sqrt{\frac{\pi}{2x}}e^{-x}
\]

show that the coefficient of the growing `I_1` branch is nonzero and

\[
\boxed{
|u(R_1)|
\ge
c(R_0,R_1)|u_0|
\exp\bigl(a(R_1-R_0)\bigr)
}
\tag{PC14}
\]

for all sufficiently large `a`, up to an inessential polynomial factor in `a` that can be absorbed by reducing the exponential constant.

Equivalently, for some `c_1,c_2>0`,

\[
\boxed{
\|(u,q)(R_1)\|
\ge c_1e^{c_2\varepsilon|\xi|(R_1-R_0)}
\|(u,q)(R_0)\|.
}
\tag{PC15}
\]

Thus the radial Cauchy propagator is exponentially unstable in axial frequency.

## 4. The same obstruction in the pressure mass operator

The same calculation can be written in the operator notation of `full_linear_mean_propagator_reduction.md`.

Let `K_0` solve `partial_R p=f` from the entrance face and `K_1` solve `(partial_R+1/R)u=f` from the entrance face. Eliminating `p` gives a mass-type equation

\[
\boxed{
\mathcal M_\xi u
=
\left(I-a^2K_1K_0\right)u=f.
}
\tag{PC16}
\]

The previous estimate

\[
\|\mathcal M_\ell-I\|\lesssim\varepsilon^2
\]

cannot hold as an operator estimate on a space containing arbitrary axial frequencies, because

\[
a^2=\varepsilon^2|\xi|^2
\]

is unbounded as `|xi| -> infinity` for every fixed positive `epsilon`.

More strongly, (PC14) shows that the inverse Cauchy resolvent itself has exponential high-frequency growth.

The source rule that `D_z=epsilon partial_Z` gains one **source exponent** is a finite-stage coefficient bookkeeping statement. It does not imply that `D_z` is a small bounded operator on one fixed Sobolev or Gevrey space.

## 5. Failure in Sobolev and Gevrey spaces

### 5.1 Sobolev

For every finite `m`, multiplication of an axial Fourier mode by

\[
e^{c\varepsilon|\xi|\Delta R}
\]

beats the polynomial Sobolev weight `(1+|xi|)^m`. Hence the one-sided coupled pressure propagator is not bounded

\[
H^m\to H^m
\]

uniformly in axial frequency.

### 5.2 Gevrey `s>1`

A Gevrey-`s` Fourier weight has subexponential form

\[
\exp(L|\xi|^{1/s}).
\]

Even allowing a fixed radius loss `L_0>L_1`, the available decay

\[
\exp(-(L_0-L_1)|\xi|^{1/s})
\]

cannot dominate

\[
\exp(c\varepsilon|\xi|\Delta R)
\]

as `|xi| -> infinity` when `s>1`.

Therefore

\[
\boxed{
\text{the coupled one-sided pressure solve is not bounded between any two fixed positive-radius Gevrey-}s>1\text{ spaces.}
}
\tag{PC17}
\]

### 5.3 Analytic class

For `s=1`, an analytic radius loss larger than `c epsilon Delta R` can in principle absorb the Cauchy growth. But nontrivial compactly supported analytic profiles do not exist, and the present relay architecture was explicitly using compactly supported Gevrey profiles. This is not a repair of the current route.

## 6. Why the radial torus Diophantine issue is irrelevant here

The instability above occurs in the auxiliary Haar mode

\[
k_y=0.
\]

Thus `D_r=partial_R` in the test subsystem. No factor `v_r dot k`, no near-resonant torus mode, and no radial phase parameter `M_r` is needed.

This obstruction is therefore distinct from the same-radius compactification obstruction proved in `radial_gevrey_radius_loss_and_same_space_obstruction.md`.

The earlier radial obstruction came from forcing two-sided compact support through a phase-following primitive. The present obstruction comes from treating an elliptic pressure/divergence problem as a one-sided radial Cauchy evolution.

## 7. Consequence for the local architecture

The following statements remain valid:

- the scalar first-order inverse of `(D_r+e/R)` with one prescribed radial trace is bounded in characteristic norms;
- the algebraic identities in `one_sided_radial_mean_reorganization.md` are correct as identities;
- the principal swirl derivative cancellation is correct and zeroth order.

What fails is the inference that these scalar one-sided inverses can be coupled through pressure and incompressibility to produce a bounded full mean propagator.

Hence the proposed local map

\[
(m_{in},z_{in},r_{in})\mapsto(m_{out},z_{out},r_{out})
\]

cannot be justified by one-sided radial pressure propagation in the current smooth/Gevrey framework.

## 8. Correct repair: pressure is elliptic, time is forward

The natural repair is to keep the successful **forward physical-time** formulation but restore the spatially elliptic nature of pressure.

Two mathematically legitimate routes remain.

1. **Elliptic boundary-value route.** On a fixed spatial collar, solve the pressure/Hodge problem with compatible two-sided spatial boundary conditions. High axial frequencies are then controlled elliptically rather than propagated as radial Cauchy data.
2. **Leray/Stokes-Oseen route.** Eliminate pressure by the spatial Leray projector and solve the divergence-free mean equation forward in physical time. Pressure is recovered elliptically after the velocity is known.

The second route is developed in `elliptic_leray_mean_forward_reduction.md`.

## 9. Corrected frontier

The local obstruction is no longer a mysterious derivative loss. It is now explicit:

\[
\boxed{
\textbf{one-sided radial propagation is compatible with scalar transport inverses, but not with the coupled elliptic pressure constraint.}
}
\]

The next theorem must therefore prove a bounded **time-forward, space-elliptic** linear mean propagator and then reinsert the already-audited nonlinear small factors.
