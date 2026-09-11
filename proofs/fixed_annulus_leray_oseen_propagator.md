# Fixed-annulus Leray--Oseen mean propagator

**Status:** PROVED FOR THE FIXED IMPERMEABLE ANNULUS MODEL; NOT YET A WHOLE-SPACE LOCALIZATION THEOREM.

This note combines `cylindrical_common_torus_hodge_projector.md` with the exact principal swirl cancellation to close the linear mean propagator on a fixed annular spatial domain. It also records the remaining geometric issue honestly: a bounded-domain Leray projector is not automatically the same object as the pressure field of the whole-space Navier--Stokes relay.

The correct conclusion is therefore two-layered:

1. the feared linear analytic instability is absent in the fixed-annulus Hodge realization;
2. the remaining question is now **whole-space localization / boundary replacement**, not boundedness of the mean propagator itself.

## 1. Functional setting

Let

\[
\Omega=\{R_0<R<R_1\}\times\mathbb T_Z\times\mathbb T_y^2,
\qquad R_0>0,
\]

with radial phase straightened by the unitary torus translation `U_ell` from `cylindrical_common_torus_hodge_projector.md`.

Choose one fixed integer

\[
m_0>\frac{4}{2}+2,
\]

so that the normalized spatial/auxiliary Sobolev space `H^{m_0}` is an algebra and controls the first derivatives needed by the quadratic mean terms. The precise value is immaterial; one may take `m_0>=6`.

The use of a **fixed finite Sobolev order** is deliberate. Once the compact radial Gevrey Neumann mechanism has been abandoned, exact local contraction does not require an infinite hierarchy of physical-space derivatives. The source exponent bookkeeping may be applied at this one fixed order, with constants depending on `m_0` but not on the dyadic level.

Let

\[
\mathcal H_\sigma^{m_0}
=\{m\in H^{m_0}(\Omega):\operatorname{div}_*m=0,
\ m_r|_{R_0,R_1}=0\}.
\tag{LO1}
\]

The common-torus Hodge theorem gives

\[
\boxed{
\|\mathbb P_*F\|_{H^{m_0}}
\le C_{I,m_0}\|F\|_{H^{m_0}},
}
\tag{LO2}
\]

uniformly in the dyadic level and radial phase parameter.

## 2. Linear projected operator

Write the projected linear mean equation in normalized physical time `s` as

\[
\boxed{
\partial_s m
=\mathbb P_*\left[
\varepsilon\Delta_*m
-(U_0\cdot\nabla_*)m
-(m\cdot\nabla_*)U_0
+\mathcal C_{\rm cyl}m
\right]+F.
}
\tag{LO3}
\]

Here `U_0=(b,V,G)` is the frozen source base on the mean patch, and `C_cyl` contains the cylindrical lower-order terms.

By `principal_swirl_mean_cancellation.md`, the apparently first-order non-small `V` coupling reduces exactly to zeroth order after the divergence-free constraint is imposed. Thus every truly first-order coefficient in (LO3) is either an ordinary fixed base transport coefficient or belongs to a source-small correction.

## 3. L2 energy estimate

Because `P_*` is the orthogonal Hodge projection in the weighted cylindrical `L^2` realization and `m` is divergence free,

\[
\langle \mathbb P_*F,m\rangle=\langle F,m\rangle.
\tag{LO4}
\]

The viscous term satisfies, with the fixed impermeable/slip realization,

\[
\boxed{
\langle\Delta_*m,m\rangle
\le-c_I\|\nabla_*m\|_{L^2}^2+C_I\|m\|_{L^2}^2,
}
\tag{LO5}
\]

where the harmless lower-order cylindrical contribution is absorbed into `C_I`.

For the base transport,

\[
\left|
\langle (U_0\cdot\nabla_*)m,m\rangle
\right|
\le C\|\operatorname{div}_*U_0\|_{L^\infty}\|m\|_2^2
+\text{boundary flux}.
\tag{LO6}
\]

On the fixed mean patch the base is divergence free. Choose the annular faces in the fixed buffer where its normal component vanishes, or impose the corresponding impermeable realization. Then the boundary flux is zero.

The stretching and cylindrical terms obey

\[
\left|
\langle(m\cdot\nabla_*)U_0,m\rangle
\right|
+
|\langle\mathcal C_{\rm cyl}m,m\rangle|
\le C_{M,I}\|m\|_2^2.
\tag{LO7}
\]

Hence

\[
\boxed{
\frac12\frac d{ds}\|m\|_2^2
+c_I\varepsilon\|\nabla_*m\|_2^2
\le C_{M,I}\|m\|_2^2+\|F\|_2\|m\|_2.
}
\tag{LO8}
\]

No frequency-dependent positive growth appears.

## 4. Fixed-order derivative estimate

Apply normalized characteristic derivatives of total order at most `m_0`. Radial derivatives are taken through the straightened `D_r` graph, so the large phase coefficient never appears as a commutator loss.

At derivative order `|alpha|<=m_0`, write

\[
D^\alpha[(U_0\cdot\nabla_*)m]
=(U_0\cdot\nabla_*)D^\alpha m
+[D^\alpha,U_0\cdot\nabla_*]m.
\]

The first term has the same skew/flux structure as in (LO6). Since `m_0` is fixed and the frozen coefficient family has bounded source seminorms,

\[
\boxed{
\|[D^\alpha,U_0\cdot\nabla_*]m\|_2
\le C_{M,I,m_0}S_*^C\|m\|_{H^{m_0}}.
}
\tag{LO9}
\]

The power `S_*^C` is polynomial and fixed at this derivative level. The same estimate applies to the stretching, cylindrical, and Hodge commutator terms. The projected viscosity is dissipative at top order up to lower-order fixed coefficient terms.

Therefore

\[
\boxed{
\frac d{ds}\|m\|_{H^{m_0}}^2
+c\varepsilon\|m\|_{H^{m_0+1}}^2
\le C_{M,I,m_0}S_*^C\|m\|_{H^{m_0}}^2
+C\|F\|_{H^{m_0}}^2.
}
\tag{LO10}
\]

At first sight the polynomial `S_*^C` in the exponential of Gronwall would be undesirable. However the only source coefficients whose fixed derivatives grow polynomially with `S_*` are attached to the already normalized source scaling. Splitting the operator into the frozen `O(1)` base part and source-small coefficient remainder gives

\[
\mathcal L_{\rm mean}=\mathcal L_0+\mathcal R_\ell,
\qquad
\|\mathcal R_\ell\|_{H^{m_0}\to H^{m_0-1}}
\le S_*^C\varepsilon^{\delta_R}.
\tag{LO11}
\]

Because `S_*=ell^2` while `epsilon` is exponentially small in `ell`,

\[
S_*^C\varepsilon^{\delta_R}=o(1).
\tag{LO12}
\]

The genuinely `O(1)` coefficient family is fixed after the relay design is frozen and contributes only `C_{M,I,m_0}`. Thus for sufficiently large `ell`,

\[
\boxed{
\frac d{ds}\|m\|_{H^{m_0}}^2
+c\varepsilon\|m\|_{H^{m_0+1}}^2
\le C_{M,I,m_0}\|m\|_{H^{m_0}}^2
+C\|F\|_{H^{m_0}}^2.
}
\tag{LO13}
\]

## 5. Uniform forward propagator

On the fixed normalized temporal collar `s in [s_-,s_+]`, Gronwall gives

\[
\boxed{
\|\mathcal V_{\rm mean}(s,s_0)f\|_{H^{m_0}}
\le K_{M,I,m_0}\|f\|_{H^{m_0}},
}
\tag{LO14}
\]

where

\[
\boxed{
K_{M,I,m_0}<\infty
}
\]

is independent of the dyadic level, auxiliary torus frequency, axial frequency, and harmonic truncation.

This closes the linear bounded-propagator obligation **for the fixed-annulus Hodge problem**.

## 6. Nonlinear consequence on the fixed annulus

At fixed `m_0>=6`, `H^{m_0}` is an algebra, so polynomial mean nonlinearities satisfy ordinary difference estimates. Combining this with `nonzero_mean_sensitivity.md` gives the same source-small return factors as before:

\[
\boxed{
\eta_{\rm nl,\ell}
\lesssim C_MS_*^C
\left[
\varepsilon^{0.17}
+\varepsilon^{1/2-\kappa_s}
+\varepsilon^{1-2\kappa_s}
+\rho_\ell
\right]
\to0.
}
\tag{LO15}
\]

Hence, **as a bounded-domain PDE problem**, the Duhamel map is contractive for sufficiently large `ell` once the signed-stress size estimate is upgraded to the corresponding difference estimate at this fixed derivative order.

This is stronger than the previous Gevrey formulation in one important respect: no same-radius Gevrey closure is needed for the local mean fixed point after the compact radial inverse has been removed.

## 7. Why this is not yet the whole-space relay theorem

The original unforced Navier--Stokes problem is not posed on an annulus with an artificial impermeable wall. A bounded-domain Hodge projector enforces a boundary condition through a harmonic pressure correction. The whole-space pressure is instead determined by the global Newtonian/Hodge operator.

Therefore one must not identify

\[
\mathbb P_{*,\Omega}
\]

with the whole-space Leray projector merely because the designed source is concentrated inside `Omega`.

In particular, even if a nonlinear residual is compactly supported, the whole-space pressure gradient and Leray correction generally have spatial tails. These tails can cross the artificial radial faces and invalidate the impermeable bounded-domain model.

Thus exact local closure on the annulus is not by itself exact zero residual for a field extended to all of physical space.

## 8. New sharp frontier: boundary replacement

The remaining geometric problem is to compare the bounded-annulus Hodge solve with the actual whole-space pressure solve.

There are two viable routes.

### Route A: whole-space weighted Leray theorem

Work directly with the global physical-space projector

\[
\mathbb P_{\mathbb R^3}=I-\nabla\Delta^{-1}\operatorname{div}
\]

in a weighted Sobolev/packet norm. Prove that the pressure tail generated by one relay remains in the admissible small outgoing error class and does not destroy the action filter or the next-scale geometry.

### Route B: harmonic boundary corrector

Write

\[
\boxed{
\mathbb P_{\mathbb R^3}F
=\mathbb P_{\Omega}F+\nabla h_F
}
\tag{LO16}
\]

inside a smaller core collar, where `h_F` is harmonic there because both projectors solve the same divergence equation away from the artificial boundary discrepancy. Then estimate `nabla h_F` in the core from the separation between the relay support and the artificial radial faces.

If the support lies a fixed normalized distance from the faces and the boundary data are already source-small, elliptic interior estimates may place this harmonic corrector in the same `rho_ell`/positive-exponent error class.

Route B is the more local next attack.

## 9. Research conclusion

The pressure problem has now split cleanly:

\[
\boxed{
\text{linear mean propagator on a fixed annulus: CLOSED;}
}
\]

\[
\boxed{
\text{replacement of the artificial Hodge boundary by whole-space pressure: OPEN.}
}
\]

This is the correct frontier before any claim of an exact local whole-space zero-force relay.
