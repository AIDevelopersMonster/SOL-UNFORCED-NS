# q-transport renormalization: exact reduction to a scale-stationary transfer coefficient

**Status:** PROVED REDUCTION THEOREM / ONE DYNAMICAL MATRIX COEFFICIENT REMAINS OPEN.

This note attacks the frontier isolated in `designated_child_cross_scale_gain_requirement.md`. It does not assume that a dyadic chart change creates physical amplification; that possibility was already ruled out by `chart_invariant_carrier_scale.md`. Instead we separate the forced q-scaling from the genuinely dynamical part of the child transport.

The conclusion is useful because it shows that the cross-scale problem is not an infinite sequence of unrelated estimates. For a fixed physical shrink factor

\[
q_{j+1}=\vartheta q_j,\qquad 0<\vartheta<1,
\]

all scale dependence can be removed by the source normalization. What remains is one fixed normalized transfer operator on one compact q-ratio interval. The cascade closes if and only if one finite-dimensional designated matrix coefficient of that operator is bounded away from zero, with the transverse complement controlled.

## 1. Primary q-weight

The physical primary packet velocity and carrier have the common q-weight

\[
\boxed{
\gamma:=\frac{1+h}{2},
\qquad
U_{\rm pkt}(q)\asymp q^{-\gamma},
\qquad
\Omega_{\rm phys}(q)\asymp q^{-\gamma}.
}
\tag{QR1}
\]

This is exactly `designated_child_cross_scale_gain_requirement.md`, equations (CG3)--(CG5).

Let `C_q` denote the complete source normalization that maps a physical packet near level `q` to its normalized packet coefficient. It contains the q-dependent velocity prefactor, spatial chart scaling, phase normalization, and the fixed moving frame. We only use the two identities forced by the source normalization:

\[
\boxed{
\mathcal C_q(q^{-\gamma}W_q^{\rm phys})=O(1),
}
\tag{QR2}
\]

and the same normalization sends a physical covector of size `q^{-gamma}` to an order-one normalized covector. Equivalently, `C_q^{-1}` restores the common factor `q^{-gamma}` in both amplitude and carrier.

## 2. Physical and normalized transport operators

Let

\[
T(q_1,q_0)
\]

be the exact physical linearized propagator carrying the designated child along the background from level `q_0` to level `q_1<q_0`, before the next nonlinear relay interaction.

Define the normalized propagator by conjugation:

\[
\boxed{
\widehat T(q_1,q_0)
:=\mathcal C_{q_1}\,T(q_1,q_0)\,\mathcal C_{q_0}^{-1}.
}
\tag{QR3}
\]

This identity is exact by definition. Hence

\[
\boxed{
T(q_1,q_0)
=\mathcal C_{q_1}^{-1}
\widehat T(q_1,q_0)
\mathcal C_{q_0}.
}
\tag{QR4}
\]

All explicit q-power amplification required by the next primary normalization is carried by `C_{q_1}^{-1}`. Therefore the physical gain

\[
(q_1/q_0)^{-\gamma}
\]

is automatic **provided the normalized designated component of `widehat T` stays order one and nonzero**.

This identifies precisely what must be proved dynamically.

## 3. Fixed-ratio scale stationarity

The source background is written in q-normalized profile variables; the local packet equations are likewise expressed through dimensionless variables such as

\[
X=\frac{r^2}{2q}
\]

and normalized shear/frame data. Consequently, once a fixed profile point/cone and frozen relay design are chosen, the coefficients of the normalized linearized transport between `q` and `vartheta q` depend on q only through source-small correction terms.

Abstract this source statement as

\[
\boxed{
\widehat T(\vartheta q,q)
=\widehat T_\vartheta^{(0)}+E_q,
\qquad
\|E_q\|\le C S(q)^C\varepsilon(q)^\delta,
}
\tag{QR5}
\]

for some `delta>0`, in the finite packet seminorm required for the designated block. The branch's source coefficient calculus already has exactly this form for fixed finite derivative order: q-dependence beyond the normalized profile is polynomial times a positive power of epsilon.

Thus

\[
\boxed{
\|E_q\|\to0\quad(q\to0).
}
\tag{QR6}
\]

The leading normalized cross-scale map is therefore a **single fixed operator** `widehat T_vartheta^(0)`.

This is a reduction, not yet an evaluation of that operator.

## 4. Designated two-dimensional WKB block

Let `e_c` denote the outgoing normalized child direction at the end of relay `j`, and let `e_p` denote the normalized incoming primary direction required at relay `j+1`. Both belong to the fixed two-dimensional WKB polarization block of the moving frame.

Define the designated transfer coefficient

\[
\boxed{
g_\vartheta^{(0)}
:=\langle e_p^*,\widehat T_\vartheta^{(0)}e_c\rangle.
}
\tag{QR7}
\]

Let `Pi_p` be the projection onto the next primary direction and `Pi_p^perp=I-Pi_p`. Then

\[
\widehat T_\vartheta^{(0)}e_c
=g_\vartheta^{(0)}e_p+r_\vartheta^{(0)},
\qquad
r_\vartheta^{(0)}:=\Pi_p^\perp\widehat T_\vartheta^{(0)}e_c.
\tag{QR8}
\]

The desired inheritance theorem is therefore equivalent to two fixed normalized statements:

\[
\boxed{|g_\vartheta^{(0)}|>0}
\tag{QR9}
\]

and

\[
\boxed{r_\vartheta^{(0)}\text{ lies in the admissible stable/transverse input class}.}
\tag{QR10}
\]

No new scale-dependent gain estimate is required after these are proved.

## 5. Perturbative persistence at high relay level

Suppose

\[
|g_\vartheta^{(0)}|\ge2c_*>0.
\tag{QR11}
\]

By (QR5)--(QR6), for sufficiently small q,

\[
\left|
\langle e_p^*,E_qe_c\rangle
\right|\le c_*.
\]

Hence the exact normalized coefficient obeys

\[
\boxed{
|g_j|
:=
|\langle e_p^*,\widehat T(\vartheta q_j,q_j)e_c\rangle|
\ge c_*.
}
\tag{QR12}
\]

Similarly, any strict open cone/stable-complement condition satisfied by `r_vartheta^(0)` persists under `E_q=o(1)`.

Restoring physical units with (QR4),

\[
\boxed{
T(q_{j+1},q_j)W_{c,j}
=
\vartheta^{-\gamma}g_j W_{p,j+1}^{\rm unit}
+R_{j+1}^{\rm phys},
}
\tag{QR13}
\]

where `W_{p,j+1}^{unit}` denotes the normalized unit primary profile restored at scale `q_{j+1}`. Since the standard physical primary itself has amplitude `q_{j+1}^{-gamma}`, this is exactly the gain law required in (CG9), modulo the bounded nonzero coefficient `g_j`.

## 6. Carrier inheritance is the same normalized statement

Let `n_c` be the normalized child phase covector. Under the exact eikonal transport,

\[
D_t\Phi=0,
\]

its physical gradient satisfies

\[
\boxed{
D_t(\nabla\Phi)=-(\nabla U_0)^T\nabla\Phi.
}
\tag{QR14}
\]

After conjugation by the source q-normalization, the normalized covector obeys a dimensionless first-order linear ODE on the same fixed q-ratio interval. Thus its cross-scale propagation is also governed by a fixed normalized transfer matrix plus source-small perturbations.

Consequently the required physical carrier factor `vartheta^{-gamma}` again comes from restoring units at `q_{j+1}`; the genuine dynamical obligation is only that the normalized covector stays in the admissible unit-beta cone and does not collapse to zero.

This confirms the conceptual simplification noted in `designated_child_cross_scale_gain_requirement.md`: amplitude and carrier inheritance are not independent scale-gain problems.

## 7. Exact remaining finite problem

The infinite cascade inheritance problem has now been reduced to the following fixed calculation for one chosen `vartheta` and frozen relay design:

1. integrate/solve the normalized two-dimensional WKB polarization equation from the outgoing child section to the next incoming primary section;
2. compute

\[
g_\vartheta^{(0)}
=\langle e_p^*,\widehat T_\vartheta^{(0)}e_c\rangle;
\]

3. prove `g_vartheta^(0) != 0` with a quantitative margin;
4. verify that the normalized transported phase covector stays in the admissible beta/phase cone;
5. place the transverse remainder in the already-stable nonzero block.

If these five fixed normalized conditions hold, the branch's existing perturbation margins and previous-relay tail estimates promote them uniformly to every sufficiently high physical scale.

## 8. What is and is not proved

Proved here:

\[
\boxed{
\text{cross-scale q-power gain}
\iff
\text{nondegenerate normalized fixed-ratio transfer}.
}
\tag{QR15}
\]

More precisely, the apparent need to manufacture a fresh factor `vartheta^{-(1+h)/2}` dynamically is misleading after exact normalization: that factor is the difference between the physical units at `q_j` and `q_{j+1}`. The dynamics only has to preserve a nonzero order-one normalized child component while transporting it into the next admissible cone.

Not proved here:

\[
\boxed{g_\vartheta^{(0)}\ne0.}
\]

That is now the sharp bottleneck. It is a finite normalized WKB transfer calculation, not a scale-asymptotic or pressure-tail problem.
