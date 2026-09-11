# Characteristic fast-time inverse for the mean block

**Status:** PROVED LOCAL FORWARD INVERSE THEOREM. This removes the auxiliary-time small-divisor derivative loss from the preferred **forward input-output** formulation of the mean equations. It does not by itself close the radial compactification remainders from Lemma 8.2.

The key observation is that the divisor in source Lemma 8.6 appears only because the source freezes the slow time `T` and solves the cohomological equation

\[
 c_i N_i\phi=F
\]

on a whole torus. For a local autonomous relay we do not need a two-sided, fixed-`T` correction. We may solve along the actual normalized physical-time characteristics of

\[
\boxed{t_*= -\varepsilon\partial_T+c_iN_i.}
\tag{CT1}
\]

This is an initial-value problem, not a torus cohomology problem.

## 1. Characteristic strip

Fix one band/common-torus chart. The source normalization gives

\[
N_i=v_t\cdot\partial_y,
\qquad
c_i\asymp S_*^{-1},
\]

while `epsilon=Q^h` is constant on the chart.

Let `L>0` be a fixed normalized physical-time length, independent of the dyadic level, and set

\[
\boxed{
I_T=[T_0-\varepsilon L,T_0].
}
\tag{CT2}

For `0<=s<=L` define the characteristic map

\[
\boxed{
T(s)=T_0-\varepsilon s,
\qquad
y(s)=y_0+c_i s\,v_t.
}
\tag{CT3}

Then for every smooth coefficient `f`,

\[
\frac{d}{ds}f(T(s),y(s))
=(-\varepsilon\partial_T+c_iN_i)f
=t_*f.
\tag{CT4}

Thus `s` is exactly the normalized physical-time parameter for the chart operator `t_*`.

## 2. Exact causal inverse

Let `F=F(R,Z,T,y)` be smooth on the strip. Define

\[
\boxed{
(\mathcal J_iF)(R,Z,T,y)
=
-\frac1\varepsilon
\int_T^{T_0}
F\!\left(
R,Z,\tau,
 y+\frac{c_i}{\varepsilon}(T-\tau)v_t
\right)d\tau.
}
\tag{CT5}

Equivalently, in the characteristic coordinate

\[
s=\frac{T_0-T}{\varepsilon},
\qquad
\eta=y-c_i s v_t,
\]

one has simply

\[
\boxed{
\widetilde{\mathcal J_iF}(s,\eta)
=
-\int_0^s\widetilde F(\sigma,\eta)d\sigma.
}
\tag{CT6}

A direct differentiation gives

\[
\boxed{
t_*\mathcal J_iF=F,
\qquad
(\mathcal J_iF)|_{T=T_0}=0.
}
\tag{CT7}

Changing the orientation gives the analogous entrance-value inverse from the opposite end of the strip.

No Fourier division occurs anywhere in (CT5)–(CT7).

## 3. No small divisor and no torus derivative loss

Let `X_y` be any translation-invariant Banach norm on the torus, for example `C^m`, `H^m`, a Fourier `l^1` norm, or a Gevrey norm. Torus translation is an isometry in `X_y`, so

\[
\boxed{
\sup_{T\in I_T}
\|\mathcal J_iF(T)\|_{X_y}
\le
L\sup_{T\in I_T}\|F(T)\|_{X_y}.
}
\tag{CT8}

In particular the bound is independent of the Diophantine denominator `v_t\cdot k` and independent of `c_i^{-1}`.

This should be compared with the frozen-time source inverse, whose coefficient estimate contains

\[
\|(v_t\cdot\partial_y)^{-1}F\|_{C^m}
\lesssim
\|F\|_{C^{m+4}}.
\]

The forward characteristic inverse has no such loss.

## 4. Physical-jet norm

For exact iteration the right norm is not the source's coordinate derivative norm in `partial_T` separately. Define the local physical-jet seminorm

\[
\boxed{
\|f\|_{\mathfrak M^{m}_{\rm char}}
:=
\max_{a+b+c+d\le m}
\|\partial_R^a\partial_Z^b\partial_y^c t_*^d f\|_{L^\infty}.
}
\tag{CT9}

Here `partial_y^c` denotes arbitrary torus derivatives of total order `c`. On one fixed common chart these operators commute with `t_*` up to the already-controlled smooth chart coefficients; for the exact constant `c_i` representation they commute exactly.

From (CT7), for `d>=1`,

\[
t_*^d\mathcal J_iF=t_*^{d-1}F.
\]

The spatial and torus derivatives commute through (CT5). Therefore

\[
\boxed{
\|\mathcal J_iF\|_{\mathfrak M^{m}_{\rm char}}
\le
C_{m,L}
\|F\|_{\mathfrak M^{m}_{\rm char}}.
}
\tag{CT10}

No derivative index is shifted upward on the right-hand side.

For every fixed positive `epsilon`, the coordinate derivatives `(partial_T,partial_y)` are recovered from `(t_*,partial_y)` by

\[
\partial_T
=-\varepsilon^{-1}(t_*-c_iN_i),
\]

so the characteristic class still consists of ordinary smooth functions. The point is that the **uniform dyadic bookkeeping** follows the physical derivative `t_*`, rather than an artificial split into slow and fast pieces.

## 5. Haar mean and common-torus descent

If

\[
\langle F\rangle_y=0
\]

for every `(R,Z,T)`, then Haar invariance under translation and (CT5) give

\[
\boxed{
\langle\mathcal J_iF\rangle_y=0.
}
\tag{CT11}

Likewise, the torus translations in (CT5) commute with deck translations. Hence a coefficient descending to a common torus remains a common-torus coefficient after `mathcal J_i`.

The inverse is real-preserving and does not enlarge the support in `R` or `Z`. It does enlarge the slow-time support toward the chosen exit face, which is intentional in the forward relay architecture: the correction is carried as an outgoing state rather than forced to vanish at both temporal ends.

## 6. Mean zero-average update

Let

\[
E_\theta^\circ,
\qquad E_z^\circ
\]

be the zero-Haar-average tangential mean residuals. In the preferred forward formulation define the **desired** temporal correction by

\[
\boxed{
\Delta v_{\rm des}=-\mathcal J_iE_\theta^\circ,
\qquad
\gamma_{d,\rm des}=-\mathcal J_iE_z^\circ.
}
\tag{CT12}

Then

\[
\boxed{
 t_*\Delta v_{\rm des}=-E_\theta^\circ,
\qquad
 t_*\gamma_{d,\rm des}=-E_z^\circ
}
\tag{CT13}

exactly, with zero exit/entrance value according to orientation.

Thus the zero-average **temporal** mean correction no longer requires source Lemma 8.6 or any Gevrey/Nash--Moser device merely to invert `v_t\cdot partial_y`.

## 7. Relation to the source pulse coordinate

The bounded strip (CT2) is not an ad hoc tiny interval. Source equation (6.21) parameterizes the fast auxiliary trajectory by the same normalized physical-time variable: a change `s` produces a torus displacement `c_i s v_t`, while the slow coordinate changes by `epsilon s` under `t_*`.

Hence a fixed relay collar of normalized fast-time width `L` corresponds exactly to a slow-time width

\[
\boxed{\Delta T=\varepsilon L.}
\tag{CT14}

This explains why the causal inverse costs only `L`, not `epsilon^{-1}` and not `c_i^{-1}`.

## 8. What remains

The temporal small divisor is therefore **not a fundamental obstruction** once the local problem is formulated as an input-output evolution.

One source-specific issue remains in the compact mean machinery. The source realizes an axial desired increment by a compactly supported azimuthal potential and obtains

\[
\Delta\gamma
=\gamma_d-A_1\gamma_d.
\]

The remainder `A_1\gamma_d` is a radial compactification remainder. Source Lemma 8.2 proves it is flat by repeated inversion of the other torus direction `v_r\cdot partial_y`; that proof again loses derivatives at arbitrary repeated order.

Accordingly the corrected local frontier is now narrower:

\[
\boxed{
\textbf{exact treatment of the radial compactification remainder,}
}
\]

not the fast-time torus divisor.

There are two promising routes:

1. a Gevrey estimate making the radial remainder quantitatively super-flat rather than merely `C^infty`-flat;
2. an unforced-specific forward/Leray formulation that does not require every mean correction to be compactly supported in the radial variable.

The next note proves the first quantitative Gevrey estimate.
