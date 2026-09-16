# Analytic-tail symbol invertibility for the low-`u` core+tail reset

**Status:** PROVED LIMITING ANALYTIC-TAIL SPECTRAL SEPARATION / FINITE-`S` VARIABLE-COEFFICIENT TAIL PERTURBATION STILL OPEN.

The compact-primary-bank obstruction shows that an exact local reset cannot be a nonzero finitely supported fixed vector.  The corrected state must be

\[
U_S=U_{core,S}+z_{tail,S},
\]

with `z_tail,S` in the completed analytic correction lattice.

The spectral instability audit, however, shows expanding directions in the tangent-Gaussian bilateral profile space.  This note proves that those central-profile unstable directions do **not** automatically obstruct the analytic tail equation.  At the fixed analytic radius

\[
\boxed{\sigma_0=0.005,}
\]

the spectrum of the unit orbit shift lies in a narrow annulus around the unit circle, while the characteristic zeros of both limiting reset operators are separated from that annulus.

Thus the limiting tail operators

\[
I-\mathcal P_C,
\qquad
I-\mathcal P_P
\]

are invertible in the weighted Wiener/analytic lattice.  The remaining task is to prove that the exact finite-`S` variable-coefficient tail operator is a sufficiently controlled perturbation after the tangent-Gaussian core has been split off.

No exact finite-`S` core+tail fixed point is claimed here.

## 1. Weighted bilateral shift

The orbit increment is the beta-zero character

\[
M=(1,-2),
\qquad |M|_1=3.
\]

On an analytic coefficient sequence `a=(a_j)_{j in Z}` use

\[
\boxed{
\|a\|_{\mathcal A_\sigma}
:=\sum_{j\in\mathbb Z}e^{3\sigma|j|}|a_j|.
}
\tag{AT1}
\]

Let

\[
(Ra)_j=a_{j-1}.
\]

Then

\[
\|R\|\le e^{3\sigma},
\qquad
\|R^{-1}\|\le e^{3\sigma}.
\]

The Gelfand spectrum of the bilateral shift on the corresponding Beurling/Wiener algebra is the annulus

\[
\boxed{
\mathfrak A_\sigma
=\{\zeta\in\mathbb C:
 e^{-3\sigma}\le|\zeta|\le e^{3\sigma}\}.
}
\tag{AT2}
\]

At `sigma=sigma_0=0.005`,

\[
\boxed{
0.98511<|\zeta|<1.01512
}
\tag{AT3}
\]

throughout the annulus.

## 2. Limiting catalyst tail symbol

The catalyst Poincare operator is

\[
\mathcal P_C=R^{-1}e^{\lambda_CR},
\]

with

\[
\lambda_C=-2.982607649202283\ldots.
\]

Hence the fixed-equation symbol is

\[
\boxed{
F_C(\zeta)
:=1-\frac{e^{\lambda_C\zeta}}{\zeta}.
}
\tag{AT4}
\]

A zero satisfies

\[
e^{\lambda_C\zeta}=\zeta.
\tag{AT5}
\]

Write

\[
\zeta=x+iy,
\qquad r=|\zeta|.
\]

Taking absolute values in (AT5) gives

\[
\lambda_Cx=\log r.
\tag{AT6}
\]

On the annulus (AT3),

\[
|\log r|\le3\sigma_0=0.015,
\]

so

\[
\boxed{|x|<0.006.}
\tag{AT7}
\]

Because `r>0.98511`, this implies

\[
\boxed{|y|>0.985.}
\tag{AT8}
\]

Thus the principal argument of `zeta` lies within a very small neighborhood of `+pi/2` when `y>0` and of `-pi/2` when `y<0`; for the coarse bounds above it is enough to use

\[
1.56<|\arg\zeta|<1.59.
\tag{AT9}
\]

Taking arguments in (AT5),

\[
\lambda_Cy
=\arg\zeta+2\pi n,
\qquad n\in\mathbb Z.
\tag{AT10}
\]

But (AT8) and the annulus upper radius give

\[
2.93<|\lambda_Cy|<3.04.
\tag{AT11}
\]

For `y>0`, the left side of (AT10) is negative, whereas the possible right sides nearest that interval are approximately

\[
\arg\zeta-2\pi\in(-4.73,-4.69)
\]

and

\[
\arg\zeta\in(1.56,1.59).
\]

Neither intersects `(-3.04,-2.93)`.  The case `y<0` is the conjugate argument.

Therefore

\[
\boxed{F_C(\zeta)\ne0
\quad\text{for every }\zeta\in\mathfrak A_{\sigma_0}.}
\tag{AT12}
\]

Equivalently, none of the catalyst fixed-profile characteristic roots lies in the analytic-tail shift spectrum.

For orientation only, the exact roots may also be written

\[
\zeta_k=-\frac{W_k(-\lambda_C)}{\lambda_C},
\]

where `W_k` is a Lambert branch.  The canonical positive profile root is

\[
\rho_C=0.351012650244\ldots,
\]

well inside the inner radius of (AT3); the next conjugate pair has modulus about `1.555`, well outside the outer radius.  These numerical values are not needed for the elementary exclusion proof above.

## 3. Limiting parent tail symbol

The parent Poincare operator is

\[
\mathcal P_P=R^{-2}e^{\mu_PR},
\]

with

\[
\mu_P=-0.845013757547658\ldots.
\]

The fixed-equation symbol is

\[
\boxed{
F_P(\zeta)
:=1-\frac{e^{\mu_P\zeta}}{\zeta^2}.
}
\tag{AT13}
\]

A zero obeys

\[
e^{\mu_P\zeta}=\zeta^2.
\tag{AT14}
\]

Taking moduli gives

\[
\mu_Px=2\log r.
\tag{AT15}
\]

Hence on (AT3)

\[
\boxed{|x|<0.036.}
\tag{AT16}
\]

and therefore again

\[
\boxed{|y|>0.984.}
\tag{AT17}
\]

The argument remains close to `+-pi/2`; a safe coarse bound is

\[
1.53<|\arg\zeta|<1.61.
\tag{AT18}
\]

Taking arguments in (AT14),

\[
\mu_Py
=2\arg\zeta+2\pi n.
\tag{AT19}
\]

From (AT17) and the annulus upper radius,

\[
0.83<|\mu_Py|<0.86.
\tag{AT20}
\]

For `y>0`, the left side of (AT19) is negative.  The nearest possible right-side intervals are near

\[
2\arg\zeta\in(3.06,3.22)
\]

and, after subtracting `2pi`, near

\[
(-3.23,-3.06).
\]

Neither intersects `(-0.86,-0.83)`.  The lower-half-plane case is conjugate.

Thus

\[
\boxed{F_P(\zeta)\ne0
\quad\text{for every }\zeta\in\mathfrak A_{\sigma_0}.}
\tag{AT21}
\]

For orientation, the exact roots can be parameterized by

\[
\zeta=\frac{W_k(\pm a)}a,
\qquad
a=-\mu_P/2>0.
\]

The smallest positive root is about `0.73351`, while the canonical complex parent pair has modulus about `2.47791`; both are separated from (AT3).

## 4. Wiener invertibility

The symbols `F_C` and `F_P` are analytic on a neighborhood of the compact annulus `A_{sigma_0}` and are nonzero there by (AT12) and (AT21).

The weighted Wiener lemma therefore gives

\[
\boxed{
(I-\mathcal P_C)^{-1}
:\mathcal A_{\sigma_0}\to\mathcal A_{\sigma_0},
}
\tag{AT22}
\]

and

\[
\boxed{
(I-\mathcal P_P)^{-1}
:\mathcal A_{\sigma_0}\to\mathcal A_{\sigma_0},
}
\tag{AT23}
\]

with finite operator norms depending only on the fixed low-`u` limiting coefficients and `sigma_0`, not on `S`.

A dense numerical diagnostic gives a large safety margin: the minimum of `|F_C|` on (AT3) is approximately `0.946`, and that of `|F_P|` is approximately `0.552`.  Publication use of these decimal lower bounds should be outward-rounded/interval-certified; only strict nonvanishing is used in (AT22)--(AT23).

## 5. Why this does not contradict the rough-spectrum instability

The spectral audit studies the tangent-Gaussian bilateral profile space whose natural spectral circles pass through

\[
\rho_C=0.351\ldots
\]

and

\[
\rho_P=-2.14769\ldots+1.23590\ldots i.
\]

Those circles contain expanding Poincare directions.

The analytic correction tail uses a **different Banach geometry**: after the central profile and its geometric/large-deviation weights have been factored out, the residual orbit shift has spectrum in the narrow annulus (AT3) around the unit circle.

The characteristic fixed-profile roots are outside that annulus.  Hence

\[
\boxed{
\text{central tangent-profile instability}
\not\Rightarrow
\text{analytic-tail noninvertibility}.
}
\tag{AT24}
\]

This is precisely the spectral separation required by the corrected Lyapunov--Schmidt architecture.

## 6. Limiting Lyapunov--Schmidt consequence

Let `d_tail` be the boundary defect created by cutting the central tangent-Gaussian profile to the source-supported primary bank.  The compact-orbit obstruction audit gives

\[
\|d_{tail}\|_{\mathcal A_{\sigma_0}}
\le S^Ae^{-cS}
\]

at the source boundary scale.

At limiting constant-coefficient tail level, (AT22)--(AT23) give unique solutions

\[
z_C=(I-\mathcal P_C)^{-1}d_C,
\qquad
z_P=(I-\mathcal P_P)^{-1}d_P,
\]

with

\[
\boxed{
\|z_C\|+\|z_P\|
\le C S^Ae^{-cS}.
}
\tag{AT25}
\]

Thus there is no limiting spectral-size obstruction to completing the compact central bank by an exponentially small analytic tail.

## 7. Exact finite-`S` theorem still required

The remaining theorem is the variable-coefficient analogue of (AT22)--(AT25).  It must combine:

1. the tangent-Gaussian finite-`S` central normal form;
2. the source-supported compact-bank boundary defect;
3. the exact analytic tail correction operator;
4. the already proved coupled mean/nonzero zero-residual contraction;
5. `C^1` dependence on the macroscopic reset parameters.

The preferred target is

\[
\boxed{
\|\mathcal P_{tail,S}-\mathcal P_{tail}^{(0)}\|
\le o(1)
}
\tag{AT26}
\]

in the tail analytic norm **after** the tangent-Gaussian core is removed.  Then (AT22)--(AT23) and a Neumann argument give the exact finite-`S` tail inverse.

If (AT26) is too strong globally in the tail index, it is enough to prove a block version: a finite boundary layer is handled by the discrete Volterra profile equation, while the far analytic tail is treated by (AT22)--(AT23) plus the stable/full-symbol complement propagator.

No exact full-state finite-`S` reset is claimed until this last perturbation theorem is closed.
