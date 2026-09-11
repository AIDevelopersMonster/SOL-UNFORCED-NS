# Full linear mean propagator: reduction after radial forwardization

**Status:** PARTIAL THEOREM / SHARPENED LINEAR OBLIGATION.

This note attacks the last local mechanism left after `one_sided_radial_mean_reorganization.md`. The purpose is to isolate all `O(1)` terms of the angular-mean equations into one linear forward system and to show that the pressure coupling does not create a new small-divisor problem.

The remaining unproved item after this note is a uniform characteristic energy/Volterra estimate for the resulting two-component linear system.

## 1. Exact source linearization

Use the source mean variables

\[
m=(\beta,v,\gamma)
\]

and linearize Proposition 8.1 at the frozen slow base `(b,V,G)`, retaining the exact nonzero field only in the nonlinear/source remainder.

The linear radial source is

\[
\boxed{
 g_r^{\rm lin}
=-t_*\beta
-(D_r+1/R)(2b\beta)
-D_z(b\gamma+G\beta)
+\frac{2V}{R}v
+\varepsilon(\Delta_0-R^{-2})\beta.
}
\tag{L1}
\]

The linear tangential residuals are

\[
\boxed{
E_\theta^{\rm lin}
=t_*v
+(D_r+2/R)(bv+\beta V)
+D_z(Gv+V\gamma)
-\varepsilon(\Delta_0-R^{-2})v,
}
\tag{L2}
\]

and

\[
\boxed{
E_z^{\rm lin}
=t_*\gamma
+(D_r+1/R)(b\gamma+\beta G)
+D_z(2G\gamma+p_m)
-\varepsilon\Delta_0\gamma.
}
\tag{L3}
\]

All quadratic mean products, wave covariances, supported residuals, and post-principal stress errors are assigned to the nonlinear forcing.

On the reserved source mean patch used by the finite correction system one has `G=0`; keeping `G` in the formulas above is harmless and makes the operator definition chart-independent.

## 2. Eliminate incompressibility by a meridional potential

Because

\[
(D_r+1/R)\beta+D_z\gamma=0,
\]

write

\[
\boxed{
\beta=-D_z\Psi,
\qquad
\gamma=(D_r+1/R)\Psi.
}
\tag{L4}
\]

The source vector-potential realization already uses this identity. The one-sided radial formulation merely allows `Psi` to have an outgoing radial trace instead of forcing it to vanish at both radial faces.

Thus the independent mean variables are reduced to

\[
\boxed{X=(v,\Psi).}
\tag{L5}
\]

## 3. One-sided pressure reconstruction and the apparent time-derivative feedback

Set

\[
p_m=\mathcal K_{r,0}g_r,
\]

with the exact one-sided inverse from `radial_characteristic_forward_inverse.md`.

The only potentially dangerous term is the pressure response to `-t_*\beta`. By (L4),

\[
-t_*\beta=D_zt_*\Psi+[D_z,t_*]\Psi.
\tag{L6}
\]

Ignoring the already-controlled lower-order commutator for the moment, the corresponding pressure contribution is

\[
p_m^{(t)}=\mathcal K_{r,0}D_zt_*\Psi.
\tag{L7}
\]

Substitution into the axial equation produces

\[
D_zp_m^{(t)}
=D_z\mathcal K_{r,0}D_zt_*\Psi.
\tag{L8}
\]

Apply `\mathcal K_{r,1}` to the axial equation so that the leading term `t_*\gamma=(D_r+1/R)t_*\Psi` becomes `t_*\Psi` plus the entrance trace. The coefficient of `t_*\Psi` is therefore

\[
\boxed{
\mathcal M_\ell
:=I+\mathcal K_{r,1}D_z\mathcal K_{r,0}D_z
+\mathcal C_{\rm comm},
}
\tag{L9}
\]

where `C_comm` collects fixed lower-order characteristic commutators.

This is the exact place where pressure enters the time derivative of the meridional potential.

## 4. The pressure mass operator is a perturbation of the identity

In the source normalized calculus, every axial derivative gains one positive power of `epsilon`; Section 9 records axial flux gain `+1`. The one-sided radial inverses are `O(1)` in characteristic norms. Hence, on the fixed collar,

\[
\boxed{
\|\mathcal K_{r,1}D_z\mathcal K_{r,0}D_z\|
\le C_MS_*^C\varepsilon^2.
}
\tag{L10}
\]

The commutator terms contain at least one slow/axial derivative of a fixed chart coefficient and obey the same type of positive source gain. Therefore

\[
\boxed{
\|\mathcal M_\ell-I\|
\le C_MS_*^C\varepsilon^{\delta_M},
\qquad \delta_M>0.
}
\tag{L11}
\]

For sufficiently large dyadic level,

\[
\|\mathcal M_\ell-I\|<1/2,
\]

so

\[
\boxed{
\mathcal M_\ell^{-1}
=\sum_{n=0}^\infty(-1)^n(\mathcal M_\ell-I)^n,
\qquad
\|\mathcal M_\ell^{-1}\|\le2.
}
\tag{L12}
\]

Thus pressure does **not** create an `O(1)` implicit obstruction in the temporal forward equation.

## 5. The genuine O(1) linear coupling

After applying `M_ell^{-1}`, all remaining terms linear in `(v,Psi)` split into two classes.

### 5.1 Small linear terms

Every term containing `b`, an axial derivative, viscosity, or a chart commutator carries a positive source gain. These may be left in the perturbative part if desired.

### 5.2 Principal swirl coupling

The terms involving the base swirl `V` need not be small:

\[
\boxed{
(D_r+2/R)(V\beta)+D_z(V\gamma)
}
\tag{L13}
\]

in the `v` equation and

\[
\boxed{
\mathcal K_{r,0}\left(\frac{2V}{R}v\right)
}
\tag{L14}
\]

inside the pressure contribution to the `Psi` equation.

These two terms form the true `O(1)` linear mean interaction. They must be absorbed into the full mean propagator exactly, just as the designated mixed operator `K` was absorbed in the nonzero-harmonic forward theorem.

## 6. Abstract two-component forward system

The exact linear mean system can therefore be written

\[
\boxed{
 t_*X
=\mathcal A_\ell X+F,
\qquad X=(v,\Psi),
}
\tag{L15}
\]

where

\[
\mathcal A_\ell
=\mathcal A_V+\mathcal A_{\rm small},
\tag{L16}
\]

`A_V` contains the principal swirl terms (L13)--(L14), and

\[
\boxed{
\|\mathcal A_{\rm small}\|
\le C_MS_*^C\varepsilon^{\delta_A}
}
\tag{L17}
\]

for some fixed `delta_A>0` in the source parameter range.

The principal operator `A_V` contains only fixed smooth coefficients on the frozen mean patch, one radial characteristic derivative in the meridional potential component, and bounded one-sided radial Volterra operators.

No large factor `M_r` or small divisor appears when the norm is built from the radial characteristic derivative rather than from `partial_R` and `partial_y` separately.

## 7. Correct graph norm

Use a graph norm that controls one radial characteristic derivative of `Psi`:

\[
\boxed{
\|X\|_{\mathfrak X^m}
:=
\|v\|_{\mathfrak R^m_{\rm char}}
+\|\Psi\|_{\mathfrak R^m_{\rm char}}
+\|\mathcal T_r\Psi\|_{\mathfrak R^m_{\rm char}}.
}
\tag{L18}
\]

In this norm the explicit swirl operator satisfies the formal bound

\[
\boxed{
\|\mathcal A_VX\|_{\mathfrak X^m_{-1}}
\le C_M\|X\|_{\mathfrak X^m},
}
\tag{L19}
\]

where the target graph space places the time derivative at one lower graph level, exactly as in a first-order transport system.

The remaining task is to close the corresponding energy/Volterra estimate without losing one graph level at each iteration.

## 8. Two viable closures of the linear estimate

There are now only two plausible linear mechanisms.

### Route I: characteristic energy estimate

Treat the `D_r` part of (L13) as part of the principal radial transport and derive an `H^m`/Gevrey energy inequality along `t_*` and `T_r`. Because the base coefficient `V` is fixed and smooth, the expected estimate is

\[
\frac{d}{ds}\|X(s)\|_{\mathfrak X^m}
\le C_M\|X(s)\|_{\mathfrak X^m}+\|F(s)\|_{\mathfrak X^m},
\tag{L20}
\]

which would give

\[
\boxed{
\|\mathcal V_{\rm mean}(s,s_0)\|
\le e^{C_M|s-s_0|}.
}
\tag{L21}
\]

on the fixed collar, uniformly in the dyadic level.

### Route II: two-variable Volterra formulation

Use both one-sided characteristic inverses explicitly. Because `K_r` is Volterra in the radial entrance variable and `J_i` is Volterra in normalized physical time, the coupled system can be written as a two-variable Volterra equation. Iterated kernels are ordered in both entrance variables and acquire factorial denominators. This can yield bounded resolvent even when the principal swirl coupling is not small.

Route II is structurally closest to the already successful nonzero-harmonic argument.

## 9. What has been proved in this note

The following points are now closed:

1. the full `O(1)` linear mean terms have been explicitly separated from the nonlinear small blocks;
2. incompressibility reduces the independent meridional unknowns to one potential `Psi`;
3. the pressure dependence on `t_*Psi` produces the mass operator (L9), not a new small divisor;
4. that mass operator is invertible for large dyadic level because its nontrivial part contains two axially small derivatives;
5. the only remaining non-small linear mechanism is the fixed smooth swirl coupling `A_V`;
6. the radial phase parameter `M_r` disappears from the operator bound in characteristic coordinates.

## 10. Remaining proof obligation

The local frontier is now the single estimate

\[
\boxed{
\|\mathcal V_{\rm mean}(s,s_0)\|_{\mathfrak X^m\to\mathfrak X^m}
\le C_{M,I}
}
\tag{L22}
\]

for the full linear two-component mean system on the bounded temporal-radial characteristic collar, with `C_{M,I}` independent of the dyadic level.

Once (L22) is proved, the nonlinear block audit gives an `o(1)` Lipschitz constant and the final local Banach contraction follows.

This note does **not** yet claim (L22).