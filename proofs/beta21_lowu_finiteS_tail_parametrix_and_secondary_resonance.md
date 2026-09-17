# Finite-`S` analytic-tail parametrix and the secondary parent resonance

**Status:** PROVED PRINCIPAL FINITE-`S` TAIL RIGHT-INVERSE REDUCTION WITH AT MOST POLYNOMIAL LOSS / FULL PDE-COUPLED CORE+TAIL FIXED POINT STILL OPEN.

This note repairs an over-strong target left in
`beta21_lowu_analytic_tail_symbol_invertibility.md`.
It is **not** necessary, and in the parent sector is in fact false, to require a single uniform estimate

\[
\mathcal P_{tail,S}=\mathcal P_{tail}^{(0)}+o(1)
\]

on the entire bilateral tail lattice.

The correct finite-`S` architecture is local in reduced slope:

1. a central neutral strip around `x=0.70`, where the frozen reset symbols are uniformly elliptic on a slightly enlarged analytic annulus;
2. ordinary elliptic tail windows away from isolated frozen resonances;
3. one **secondary parent resonant window** near
   \[
   z_0=1.0664069\ldots,
   \]
   where the parent root-shift coefficient crosses zero;
4. a first-order Volterra/Gaussian normal form in that resonant window whose right inverse loses only `O(sqrt(S))`;
5. source/action-small forcing, so any fixed polynomial inverse loss is harmless.

Thus the finite-`S` tail problem has a polynomially bounded right inverse after one harmless resonant gauge is fixed.  No exact full-state reset is claimed until this tail solve is coupled to the exact central discrete profile and the nonlinear PDE correction.

## 1. Limiting slope-dependent root couplings

Let

\[
u=1.8,\qquad x=0.70,
\qquad \kappa_*=0.894049167184884\ldots,
\]

and let

\[
\tau_*=-0.2087411867089201\ldots,
\qquad
L_x=\sqrt{1+x^2}.
\]

The exact principal polarization calculation in
`beta21_lowu_single_root_coupling_ratio.md`
gives, uniformly on compact slope intervals,

\[
A_b^+(s,m_S;k_S,r)
=
 m_Sr\,F_b(s)+O(m_S^2),
\]

where

\[
\boxed{
F_b(s)
:=\frac{b\tau_*}{L_x}
+\frac1{2\sqrt{1+s^2}}.
}
\tag{TP1}
\]

After the common root amplitude is normalized at `s=x`, the limiting full-cell shift strengths are therefore

\[
\boxed{
\Lambda_C(s)
:=\lambda_C\frac{F_1(s)}{F_1(x)},
}
\tag{TP2}
\]

\[
\boxed{
\Lambda_P(s)
:=\mu_P\frac{F_2(s)}{F_2(x)},
}
\tag{TP3}
\]

with

\[
\lambda_C=-2.982607649202283\ldots,
\qquad
\mu_P=-0.845013757547658\ldots.
\]

The exact finite-`S` source-frame coefficients differ from (TP2)--(TP3) by `O(S^{-1})` in fixed `C^1` slope norms after the already proved tuning

\[
\tau_S=\tau_*+O(S^{-1}),
\qquad
\kappa_S=\kappa_*+O(S^{-1}).
\]

## 2. Uniform ellipticity on the central strict strip

Use the strict physical orbit strip

\[
\boxed{|s-x|\le w,\qquad w=0.03.}
\tag{TP4}
\]

On this strip direct evaluation of (TP2)--(TP3) gives the safe ranges

\[
\boxed{
-3.055<\Lambda_C(s)<-2.910,
}
\tag{TP5}
\]

\[
\boxed{
-0.918<\Lambda_P(s)<-0.772.
}
\tag{TP6}
\]

The publication tail norm uses `sigma_0=0.005`.  For the local parametrix reserve the larger radius

\[
\boxed{\sigma_1=0.01.}
\tag{TP7}
\]

Its shift annulus is

\[
\mathfrak A_{\sigma_1}
=\{e^{-0.03}\le|\zeta|\le e^{0.03}\}.
\]

### Catalyst

A frozen catalyst zero would satisfy

\[
e^{\Lambda_C(s)\zeta}=\zeta.
\tag{TP8}
\]

Write `zeta=X+iY`, `r=|zeta|`.  Taking moduli gives

\[
\Lambda_C(s)X=\log r.
\]

From (TP5) and `|log r|<=0.03`,

\[
|X|<0.011.
\]

Since `r>=e^{-0.03}>0.970`,

\[
|Y|>0.969.
\]

Hence

\[
2.82<|\Lambda_C(s)Y|<3.15.
\]

But `arg(zeta)` lies near `+/- pi/2`.  The values

\[
\arg\zeta+2\pi k
\]

nearest the negative interval `(-3.15,-2.82)` lie near `+pi/2` or `-3pi/2`, neither of which intersects it.  Thus (TP8) has no solution on `A_{sigma_1}`.

### Parent

A frozen parent zero would satisfy

\[
e^{\Lambda_P(s)\zeta}=\zeta^2.
\tag{TP9}
\]

The modulus equation is

\[
\Lambda_P(s)X=2\log r.
\]

Using (TP6),

\[
|X|<0.078,
\qquad
|Y|>0.967.
\]

Therefore

\[
0.74<|\Lambda_P(s)Y|<0.95.
\]

On the other hand

\[
2\arg\zeta+2\pi k
\]

nearest the corresponding signed interval has modulus about `pi`, not below one.  Hence (TP9) also has no solution.

Consequently the frozen symbols

\[
F_{C,s}(\zeta)
:=1-\frac{e^{\Lambda_C(s)\zeta}}\zeta,
\]

\[
F_{P,s}(\zeta)
:=1-\frac{e^{\Lambda_P(s)\zeta}}{\zeta^2}
\]

are uniformly nonzero for

\[
|s-x|\le0.03,
\qquad
\zeta\in\mathfrak A_{\sigma_1}.
\tag{TP10}
\]

By compactness and the weighted Wiener lemma, their inverses have uniformly bounded `A_{sigma_0}` convolution norms and uniformly bounded first convolution moments.  The radius reserve `sigma_1-sigma_0>0` is what supplies the first-moment bound.

A dense numerical diagnostic gives much larger margins than needed: at `sigma_0=0.005` the observed minima are about `0.94` in the catalyst sector and `0.52` in the parent sector.  These decimal margins are diagnostic only; the nonvanishing argument above is the proof used here.

## 3. Slowly varying finite-`S` windows

In sector `b`, one lattice step changes reduced slope by

\[
\Delta s_b=\frac{d_b}{S}+O(S^{-2}),
\]

where

\[
d_C=2\kappa_*,
\qquad
d_P=\kappa_*.
\]

Cover the strict strip by windows of length

\[
\boxed{L_S=\lfloor\sqrt S\rfloor.}
\tag{TP11}
\]

Let `chi_q` be a discrete partition of unity with bounded overlap and

\[
|\chi_q(j+1)-\chi_q(j)|\le C/L_S.
\tag{TP12}
\]

On one window centered at `j_q`, coefficient variation is

\[
\boxed{
|\Lambda_{b,S}(j)-\Lambda_{b,S}(j_q)|
\le C\frac{L_S}{S}+O(S^{-1})
=O(S^{-1/2}).
}
\tag{TP13}
\]

The principal generator is a diagonal coefficient times the one-step shift.  Its exponential has factorially decaying shift coefficients.  Therefore its commutator with a slowly varying cutoff obeys

\[
\boxed{
\|[\mathcal P_{b,S},\chi_q]\|_{\mathcal A_{\sigma_0}}
\le C/L_S
=O(S^{-1/2}).
}
\tag{TP14}
\]

Indeed each `R^k` term costs at most `k/L_S`, while

\[
\sum_{k\ge0}\frac{C^k}{k!}k<\infty.
\]

Let `G_{b,q}` denote the frozen Wiener inverse at the central slope of the window.  The patched parametrix

\[
\boxed{
Q_{b,S}^{neu}
:=\sum_q\chi_q G_{b,q}\chi_q
}
\tag{TP15}
\]

satisfies

\[
\boxed{
(I-\mathcal P_{b,S})Q_{b,S}^{neu}
=I+E_{b,S}^{neu},
\qquad
\|E_{b,S}^{neu}\|
\le CS^{-1/2}+o(1).
}
\tag{TP16}
\]

The number of windows does not multiply the error because the partition has bounded overlap and the analytic norm is `ell^1`-based.

Thus for sufficiently large `S`, the neutral-strip tail operator has a uniform inverse.

## 4. The parent has a second frozen resonance away from the central strip

The catalyst coupling `F_1(s)` stays positive on the source-supported positive-slope interval, so no analogous zero-crossing appears there.

For the parent,

\[
F_2(s)=\frac{2\tau_*}{L_x}
+\frac1{2\sqrt{1+s^2}}.
\]

It has one positive zero because `tau_*<0`.  Solving explicitly,

\[
\boxed{
\sqrt{1+z_0^2}
=-\frac{L_x}{4\tau_*},
}
\tag{TP17}
\]

hence

\[
\boxed{
z_0=1.0664069295\ldots.}
\tag{TP18}
\]

At this point

\[
\Lambda_P(z_0)=0.
\]

The frozen parent symbol becomes

\[
1-\zeta^{-2},
\]

which vanishes at

\[
\zeta=+1,\qquad\zeta=-1.
\]

Therefore a single global uniform Wiener inverse on the full parent tail is impossible.  This is a genuine correction to the simpler limiting-tail picture.

## 5. Transversality of the secondary resonance

Since

\[
F_2'(s)
=-\frac{s}{2(1+s^2)^{3/2}},
\]

we have

\[
\boxed{
\Lambda_P'(z_0)
=\mu_P\frac{F_2'(z_0)}{F_2(x)}
=2.13318\ldots>0.
}
\tag{TP19}
\]

Thus the zero-crossing is transverse.

Let `j_0(S)` be the parent index whose slope is nearest `z_0` and set

\[
\boxed{
y=(j-j_0)/\sqrt S.}
\tag{TP20}
\]

Then

\[
\Lambda_{P,S}(j)
=S^{-1/2}a_0y+O(S^{-1}(1+y^2)),
\]

where

\[
\boxed{
a_0=\kappa_*\Lambda_P'(z_0)
=1.90717\ldots>0.}
\tag{TP21}
\]

## 6. Local normal forms at `zeta=+1` and `zeta=-1`

### The `+1` branch

For a slowly varying envelope

\[
q_j=f(y),
\]

we have

\[
R=e^{-S^{-1/2}\partial_y}+O(S^{-1}),
\]

and hence

\[
I-R^{-2}e^{\Lambda_{P,S}R}
=
-S^{-1/2}
\left(2\partial_y+a_0y\right)
+O(S^{-1})
\tag{TP22}
\]

in fixed Gaussian graph norms.

The leading operator

\[
\boxed{L_+:=2\partial_y+a_0y}
\tag{TP23}
\]

has the Gaussian kernel

\[
\boxed{
f_+(y)=e^{-a_0y^2/4}.}
\tag{TP24}
\]

It is nevertheless **surjective** on the natural Gaussian growth/decay scale: a right inverse is obtained by variation of constants.  Its kernel is one-dimensional and is fixed by one normalization condition, for example by requiring zero coefficient along `f_+`.

After this gauge choice the local right inverse has norm `O(1)` for `L_+`, hence

\[
\boxed{
\|(I-\mathcal P_{P,S})^{-1}_{res,+}\|
\le C\sqrt S.
}
\tag{TP25}
\]

for the original finite-`S` operator.

### The `-1` branch

Write

\[
q_j=(-1)^jf(y).
\]

Then

\[
R=-e^{-S^{-1/2}\partial_y}+O(S^{-1}),
\]

and the leading local operator is

\[
\boxed{L_-:=2\partial_y-a_0y.}
\tag{TP26}
\]

Its formal homogeneous solution grows like

\[
e^{+a_0y^2/4}
\]

and is excluded from the decaying resonant tail space.  Hence the `-1` branch is injective there and has a direct Volterra inverse.  The same finite-`S` scaling gives at worst another `O(sqrt(S))` bound.

Thus the secondary parent resonance creates one harmless Gaussian gauge mode but no solvability obstruction.

## 7. Physical action makes the secondary block exponentially negligible

The parent physical action has its unique maximum at `s=x`; explicitly

\[
H_2'(s)=u(\Gamma_2(s)-\Gamma_2(x)),
\qquad
H_2(x)=0,
\]

and `Gamma_2` is strictly decreasing on the positive slope interval.  Since

\[
z_0\ne x,
\]

we have the strict structural inequality

\[
\boxed{H_2(z_0)<0.}
\tag{TP27}
\]

Hence there are constants `delta_0,c_res>0` such that

\[
H_2(s)\le-c_{res}
\qquad
(|s-z_0|\le\delta_0).
\tag{TP28}
\]

A numerical diagnostic gives

\[
H_2(z_0)\approx-0.351686,
\]

so the available physical margin is very large.  The precise decimal is not needed.

Therefore any source-generated forcing entering the secondary resonant window has size

\[
\boxed{
S^Ae^{-c_{res}S}
}
\tag{TP29}
\]

up to the already audited analytic lattice price.  Multiplication by the worst resonant inverse loss `sqrt(S)` still gives

\[
\boxed{
S^{A+1/2}e^{-c_{res}S}\to0.
}
\tag{TP30}
\]

Thus the secondary resonance is dynamically harmless at the correction scale.

## 8. Ordinary far-tail windows

Remove fixed small neighborhoods of

\[
x
\quad\text{and}\quad
z_0
\]

from the parent slope line, and remove only the central neighborhood of `x` from the catalyst line.  On every remaining compact source-relevant slope set the corresponding frozen reset symbol is nonzero on `A_{sigma_1}`.

The same `L_S=sqrt(S)` partition-of-unity construction as in section 3 gives local Wiener parametrices with errors

\[
O(S^{-1/2})+o(1).
\]

Outside source-relevant compact slope sets, the existing full-symbol/stable-sector propagator estimates apply; these modes belong to the ordinary analytic correction complement rather than to the low-`u` critical orbit geometry.

Combining the ordinary windows with the two parent resonant model inverses yields a global principal tail right inverse

\[
\boxed{
\mathcal G_{tail,S}
}
\tag{TP31}
\]

with a fixed polynomial bound

\[
\boxed{
\|\mathcal G_{tail,S}\|
\le C S^{1/2}
}
\tag{TP32}
\]

(after harmless enlargement of the power if fixed source/curl derivative losses are included).

The `+1` resonant Gaussian gauge is fixed once and for all in the definition of `X_tail,S`; equivalently it may be carried as one extra finite-dimensional Lyapunov--Schmidt coordinate.

## 9. Consequence for the core+tail boundary defect

The compact-orbit obstruction theorem gives a boundary/handoff defect

\[
\|d_{bd,S}\|_{tail}
\le S^Ae^{-cS}.
\]

The tail parametrix therefore produces

\[
\boxed{
\|z_{tail,S}\|_{tail}
\le
CS^{A+1/2}e^{-cS}
}
\tag{TP33}
\]

at principal finite-`S` level, plus the already existing source-small PDE correction terms.

Because every source-small term has the form

\[
S^B\varepsilon^a,
\qquad a>0,
\]

and `S` grows only polynomially in the source hierarchy, the additional fixed power from (TP32) does not change any small-exponent sign.

## 10. Updated Gate 1 status

The finite-`S` tail problem is therefore **not** blocked by the rough bilateral spectral instability and is **not** blocked by the secondary parent resonance.

The remaining local obstruction is now concentrated in the central tangent-Gaussian core:

\[
\boxed{
\text{prove an exact discrete finite-}S\text{ central profile, then couple it to }\mathcal G_{tail,S}.
}
\tag{TP34}

Once that central profile theorem is available, the existing coupled zero-residual/C1 machinery can be re-run with the polynomial tail inverse loss absorbed into the source-small factors.

No exact full-state finite-`S` reset is claimed in this note.
