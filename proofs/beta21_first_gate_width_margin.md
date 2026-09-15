# Quantitative nonzero-width margin for the first beta-(2,1) active gate

**Status:** COMPUTER-ASSISTED EXACT-ENVELOPE WIDTH CERTIFICATE / ANALYTIC MEAN-VALUE REDUCTION. For the exact finite-`u_*=4` cleanup point, after placing the supercritical characters `H=2D-C` and `R_3=3D-2C` (and the sufficient triangular intermediates) in the controlled block, the remaining center-critical modes retain a strict negative action defect on the forward normalized collar

\[
\boxed{0\le t\le10^{-3}.}
\]

The closest uncontrolled mode is `(B,m,n)=(2,6,-4)`. Its center defect is approximately `-0.0176368841`; at `t=10^-3` it is still approximately `-0.00799750168`. Thus the active gate can have a fixed nonzero normalized width. The present certificate uses high-precision evaluation of the exact finite-`u` formulas. A publication-final version should replace the numerical derivative suprema by interval arithmetic.

## 1. Exact drifting characters

Keep

\[
u=4,
\qquad
\delta=0.1755496058694293259805486194\ldots
\tag{GW1}
\]

from the exact cleanup resonance.

Over a forward normalized gate offset `t`, the two unit-beta input slopes are

\[
z_D(t)=1-2\delta+t,
\qquad
z_C(t)=1+t.
\tag{GW2}

For

\[
K_{m,n}=mD+nC,
\qquad B=m+n>0,
\]

the normalized beta-`B` slope is

\[
\boxed{
\xi_{B,m}(t)
=1-\frac{2m\delta}{B}+t.
}
\tag{GW3}

The maximal leaf-product action at time `t` is

\[
\boxed{
S_{B,m}(t)
=|m|\mathcal E_{1,4}(z_D(t))
+|B-m|\mathcal E_{1,4}(z_C(t)).
}
\tag{GW4}

Define

\[
\boxed{
\Delta_{B,m}(t)
=S_{B,m}(t)
-\mathcal E_{B,4}(|\xi_{B,m}(t)|).
}
\tag{GW5}

Only the finite center-critical set from `beta21_first_gate_full_critical_audit.md` needs to be checked.

## 2. Exact derivative formula

From the finite-`u` envelope primitive,

\[
\boxed{
\partial_x\mathcal E_{\beta,u}(x)
=
\frac{u}{\sqrt{1+u^2x^2}}
-
\frac{\beta^2}{(1+u^2)^{3/2}}
\left(u+u^3x^2\right).
}
\tag{GW6}

Away from a zero of `xi`, differentiation gives

\[
\boxed{
\begin{aligned}
\Delta_{B,m}'(t)
={}&|m|\mathcal E'_{1,4}(z_D(t))
+|B-m|\mathcal E'_{1,4}(z_C(t))\\
&-\operatorname{sgn}(\xi_{B,m}(t))
\mathcal E'_{B,4}(|\xi_{B,m}(t)|).
\end{aligned}}
\tag{GW7}

At a zero of `xi`, the defect is continuous and one-sided derivatives are given by the same formula with the appropriate sign.

Thus a finite interval certificate can be reduced to finitely many explicit one-variable derivative bounds.

## 3. The closest uncontrolled mode

After removing the designated inputs and the controlled dangerous characters, the smallest negative center margin occurs at

\[
\boxed{(B,m,n)=(2,6,-4).}
\tag{GW8}

Its center defect is

\[
\boxed{
\Delta_{2,6}(0)
=-0.01763688412078495434615649119\ldots.
}
\tag{GW9}

High-precision evaluation of (GW7) on

\[
0\le t\le10^{-3}
\]

gives

\[
\boxed{
\sup|\Delta_{2,6}'(t)|
<9.653.
}
\tag{GW10}

Hence the mean-value estimate already gives

\[
\Delta_{2,6}(t)
\le
-0.0176368841+9.653\,t.
\tag{GW11}

In particular at `t<=10^-3`,

\[
\boxed{
\Delta_{2,6}(t)<-0.00798.
}
\tag{GW12}

Direct exact-envelope evaluation at the right endpoint gives

\[
\boxed{
\Delta_{2,6}(10^{-3})
=-0.007997501684831825228\ldots.
}
\tag{GW13}

The corresponding linear mean-value crossing scale is

\[
\frac{0.0176368841}{9.653}
\approx1.827\times10^{-3},
\tag{GW14}

so the chosen width `10^-3` has a nontrivial safety factor.

## 4. Remaining finite critical modes

The same exact derivative check was performed for every uncontrolled member of the 51-mode positive-beta center-critical set. The next closest margins on `0<=t<=10^-3` are approximately

\[
\begin{array}{c|c}
(B,m,n)&\sup_{[0,10^{-3}]}\Delta_{B,m}\\ \hline
(2,5,-3)&-0.0866287993\\
(1,4,-3)&-0.161161459\\
(2,4,-2)&-0.383987094\\
(3,8,-5)&-0.712407568\\
(2,7,-5)&-0.733634707
\end{array}
\tag{GW15}

All other uncontrolled center-critical characters have still more negative defects.

Therefore there is a uniform finite-set margin

\[
\boxed{
\Delta_{B,m}(t)\le-\gamma_{gate},
\qquad
\gamma_{gate}>7.9\times10^{-3},
}
\tag{GW16}

for every uncontrolled center-critical mode and every

\[
0\le t\le10^{-3}.
\]

For a conservative quoted value one may take

\[
\boxed{\gamma_{gate}=7\times10^{-3}.}
\tag{GW17}

## 5. Modes outside the center-critical set

The center-critical enumeration contains every mode whose principal rate is nonnegative at `t=0`. Because the lattice turning inequalities have a positive finite separation from their nearest omitted sites after removing the exact designated turning-point input `C`, continuity gives a smaller neighborhood of `t=0` on which no omitted low mode enters the growing region.

At `u=4`, all `|B|>=9` modes are strictly principal-decaying for every slope, since the beta turning point no longer exists. Thus high-beta modes cannot enter the critical set under the small drift.

The exact minimum low-mode turning-boundary separation should be interval-certified together with (GW10) in the publication audit. Numerically the chosen width `10^-3` is far below the first relevant boundary crossing.

## 6. Consequence for the gate construction

Combining this note with

- `beta21_first_gate_full_critical_audit.md`,
- `six_control_smooth_gate_vandermonde.md`,
- `catalyst_subpacket_direct_P_realization.md`, and
- the parameter-dependent local zero-residual theorem,

we obtain the following source/principal package:

\[
\boxed{
\begin{gathered}
\text{finite full first-gate critical block},\\
\text{six-control full-rank smooth response},\\
\text{internal catalyst-subpacket realization},\\
\text{fixed nonzero gate width},\\
\text{uniform negative action gap for every uncontrolled critical mode}.
\end{gathered}}
\tag{GW18}

The remaining first-gate obligation is now the exact `C^1` transfer of the six-control source packet map at this chosen finite width, including the controlled rows `P_new,R_3`. Structurally this is the same parameter-differentiated Volterra/Banach argument already proved for the four-control block, but it should be recorded explicitly before declaring the first active gate complete.
