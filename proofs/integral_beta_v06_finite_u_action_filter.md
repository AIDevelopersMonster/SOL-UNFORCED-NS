# v0.6 integral-beta relay: finite-u persistence and action filter

**Status:** PROVED MODEL THEOREM / PREFERRED PARAMETER CANDIDATE. This file improves the v0.5 integral-beta design by moving the decaying parent from `x_1=4/5` to `x_1=3/4`. The change preserves the exact arithmetic relation `2-1=1`, keeps the first feedback harmonic purely radial, and creates a fixed exponential action deficit for the first regenerated growing unit-beta sideband.

This is still an envelope/phase-lattice theorem. It does not yet prove the full localized unforced Navier–Stokes relay.

## 1. Parameters

Fix

\[
\boxed{
\beta_1=2,
\qquad
\beta_2=1,
\qquad
\beta_1-\beta_2=1,
\qquad
x_1=\frac34.
}
\tag{A1}
\]

For catalyst coordinate `y`, define the desired unit-beta child coordinate

\[
\boxed{x_c(y)=2x_1-y=\frac32-y.}
\tag{A2}
\]

The reduced envelope primitive is

\[
I_\beta(x)
=\log x+\frac23\log\beta-\frac{\beta^2x^3}{3}+\frac13,
\qquad
F_\beta=I_\beta'=\frac1x-\beta^2x^2.
\tag{A3}
\]

Define

\[
G(y)=I_2(3/4)+I_1(y)-I_1(3/2-y).
\tag{A4}
\]

## 2. Certified reduced resonance

For rational `y`, multiplying (A4) by three gives

\[
3G(y)=\log Z(y)+P(y),
\]

with

\[
Z(y)=4\left(\frac{(3/4)y}{3/2-y}\right)^3\in\mathbb Q_{>0}
\]

and

\[
P(y)=1-4(3/4)^3-y^3+(3/2-y)^3\in\mathbb Q.
\]

The exact atanh-series certificate in `experiments/integral_beta_v06_certificate.py` proves

\[
G\left(\frac{3927}{5000}\right)<0,
\qquad
G\left(\frac{1571}{2000}\right)>0.
\]

Therefore

\[
\boxed{
0.7854<y_0<0.7855.
}
\tag{A5}
\]

Numerically,

\[
\boxed{
y_0\approx0.7854873695884608,}
\]

\[
\boxed{x_{c,0}\approx0.7145126304115392.}
\]

Since both `y` and `x_c` are below one,

\[
G'(y)=F_1(y)+F_1(x_c(y))>0,
\]

so the root is unique and transverse.

The same exact certificate gives the wider endpoint margins

\[
\boxed{
G(19/25)<-39/1000,
\qquad
G(4/5)>11/500.
}
\tag{A6}

## 3. Two explicit finite-u envelope error bounds

Recall the exact envelope

\[
\mathcal E_{\beta,u}(x)
=
\operatorname{arsinh}(ux)
-
\operatorname{arsinh}(u x_{\beta,u})
-
\frac{\beta^2}{(1+u^2)^{3/2}}
\left[
 u(x-x_{\beta,u})
+
\frac{u^3}{3}(x^3-x_{\beta,u}^3)
\right].
\tag{A7}
\]

### Lemma 3.1: unit-beta interval

For

\[
\frac35\le x\le\frac45,
\qquad u\ge20,
\]

\[
\boxed{
|\mathcal E_{1,u}(x)-I_1(x)|
\le\frac{3}{2u^2}.
}
\tag{A8}
\]

For beta one the turning point is exactly one. Write

\[
r(z)=\operatorname{arsinh}z-\log(2z),
\qquad 0\le r(z)\le\frac1{4z^2}.
\]

The inverse-hyperbolic-sine error is at most

\[
\frac{1}{4u^2x^2}\le\frac{25}{36u^2}.
\]

The linear viscous term is at most `2/(5u^2)`, and the cubic coefficient error is at most

\[
\frac{1-x^3}{2u^2}
\le\frac{49}{125u^2}.
\]

Their sum is smaller than `3/(2u^2)`.

### Lemma 3.2: the fixed beta-two parent

For

\[
x=\frac34,
\qquad u\ge20,
\]

\[
\boxed{
|\mathcal E_{2,u}(3/4)-I_2(3/4)|
\le\frac4{u^2}.
}
\tag{A9}
\]

Indeed, with `a=2^{-2/3}` and `d=a^{-2}-1=2^{4/3}-1`,

\[
\frac35<a<\frac23,
\qquad 0<d<\frac85,
\]

and

\[
x_{2,u}=a\sqrt{1-d/u^2}>\frac{59}{100}.
\]

Using the same bound for `r(z)`, the complete `arsinh/log` contribution is less than `2/u^2`; the linear viscous term is less than `16/(25u^2)`; and the two cubic replacement errors sum to less than `61/(50u^2)`. Hence the total is less than `4/u^2`.

## 4. Exact finite-u resonance theorem

Define

\[
G_u(y)
=\mathcal E_{2,u}(3/4)
+\mathcal E_{1,u}(y)
-\mathcal E_{1,u}(3/2-y).
\tag{A10}
\]

On

\[
\frac{19}{25}\le y\le\frac45,
\]

both unit-beta arguments lie in `[3/5,4/5]`. Lemmas 3.1–3.2 give

\[
\boxed{
|G_u(y)-G(y)|\le\frac7{u^2}.
}
\tag{A11}
\]

For `u>=20`, `7/u^2<=7/400`. Combining (A6) and (A11) gives

\[
G_u(19/25)<0,
\qquad
G_u(4/5)>0.
\]

Moreover

\[
G_u'(y)
=H_{1,u}(y)+H_{1,u}(3/2-y)>0
\]

because both arguments are below the unit-beta turning point `x=1`.

Therefore:

### Finite-u v0.6 resonance theorem

For every fixed

\[
\boxed{u_*=u\ge20,}
\]

there is a unique exact resonance root

\[
\boxed{
\frac{19}{25}<y_u<\frac45.
}
\tag{A12}
\]

The beta-two parent is decaying because `x_{2,u}<2^{-2/3}<3/4`, while catalyst and child are growing because

\[
y_u<1,
\qquad
x_c(y_u)<1.
\]

Thus

\[
\boxed{
\text{decaying beta-2 parent}
+\text{ growing beta-1 catalyst}
\xrightarrow{\text{difference}}
\text{ growing beta-1 child}
}
\tag{A13}
\]

holds in the exact finite-u envelope model.

Representative roots are

\[
y_{20}\approx0.786166291392389,
\quad
y_{50}\approx0.785595530752873,
\quad
y_{100}\approx0.785514393236699,
\]

and converge to (A5).

## 5. First feedback harmonic remains purely radial

The child-minus-catalyst lattice index is

\[
r_0=(1,-2).
\]

Its tangential coefficient is

\[
T_{r_0}=2-2=0.
\]

Its radial coefficient is

\[
R_{r_0}/u
=2x_1-2y_u
=\frac32-2y_u.
\]

Because `y_u>19/25`, this never vanishes on the theorem bracket. Hence its inviscid growing term is exactly zero and

\[
\boxed{
\Gamma_{r_0}<0.
}
\tag{A14}
\]

For any fixed choice of `u_*>=20`, the corresponding forward inverse has a finite constant depending on `u_*` but not on the dyadic level. Thus it introduces no exponential `S_*` gain.

## 6. The first regenerated growing mode

Adding the radial step `r_0` to the desired child `(1,-1)` gives

\[
m_2=(2,-3).
\]

Its tangential coefficient is again one:

\[
T_{m_2}=4-3=1,
\]

and its unit-beta reduced coordinate is

\[
\boxed{
x_2(y)=4x_1-3y=3-3y.}
\tag{A15}
\]

On the exact resonance bracket,

\[
\frac35\le x_2(y)\le\frac{18}{25}<1,
\]

so this mode is locally on a **growing** unit-beta branch. Thus beta integrality does not make the entire correction lattice forward-stable.

The relevant question is instead whether the mode is seeded at its natural tail size.

## 7. Exact action deficit for `m_2`

Let

\[
A_u:=\mathcal E_{2,u}(3/4),
\qquad
B_u:=\mathcal E_{1,u}(y_u).
\]

The desired child satisfies the exact envelope resonance

\[
\mathcal E_{1,u}(x_c)=A_u+B_u.
\]

The radial feedback `r_0` is generated from child times catalyst, so its source action is `A_u+2B_u`. Its stable inverse changes only the prefactor, not the `S_*` exponential action. Therefore the first source capable of generating `m_2=child+r_0` has action

\[
2A_u+3B_u.
\]

Compare this with the natural unit-beta tail action at `x_2`:

\[
\boxed{
\Delta_{2,u}
:=2A_u+3B_u-\mathcal E_{1,u}(x_2(y_u)).
}
\tag{A16}
\]

In the reduced model set

\[
D_2(y)
=2I_2(3/4)+3I_1(y)-I_1(3-3y).
\]

On `[19/25,4/5]`, both `y` and `x_2` are below one, hence

\[
D_2'(y)=3F_1(y)+3F_1(x_2(y))>0.
\]

The exact rational logarithm certificate gives

\[
\boxed{D_2(4/5)<-\frac1{25}.}
\tag{A17}
\]

Therefore `D_2(y_u)<-1/25`. Applying (A8)–(A9) to the six envelope factors in (A16),

\[
|\Delta_{2,u}-D_2(y_u)|
\le
\frac{14}{u^2}
\le\frac7{200}.
\]

Consequently

\[
\boxed{
\Delta_{2,u}<-rac1{200}.
}
\tag{A18}

Thus `m_2` is growing, but it is seeded below its natural growing-tail scale by a fixed exponential action gap.

If

\[
\Lambda_*:=\frac{\lambda_0L_s}{u_*},
\]

then even after the maximum homogeneous amplification from its generation point to its unit-beta peak, the `m_2` contribution retains the factor

\[
\boxed{
\exp(-\Lambda_*/200).
}
\tag{A19}
\]

Since `L_s\asymp S_*` and `u_*` is fixed once for the construction, this is `e^{-cS_*}` and therefore flat relative to every algebraic power of the dyadic scale.

This is the first rigorous **action-subcritical feedback** result in the branch.

## 8. The whole in-window unit-beta feedback ladder

Repeated addition of the radial feedback step gives

\[
\boxed{
m_a=(a,1-2a)=e_2+a(1,-2),\qquad a\ge1.}
\tag{A20}
\]

Every `m_a` has tangential coefficient

\[
T_{m_a}=2a+(1-2a)=1.
\]

Its reduced unit-beta coordinate is

\[
\boxed{
x_a(y)=\frac32a+(1-2a)y.}
\tag{A21}
\]

The largest possible source action obtained from the base parent/catalyst tails is

\[
S_{a,u}=aA_u+(2a-1)B_u.
\tag{A22}
\]

From the exact rational inequalities

\[
I_2(3/4)<-\frac{27}{500},
\qquad
I_1(4/5)<-\frac3{50},
\qquad
I_1(1/2)>-\frac{81}{200},
\]

and (A8)–(A9), for `u>=20` we have

\[
A_u< -\frac{11}{250},
\qquad
B_u< -\frac9{160}.
\tag{A23}
\]

If a ladder mode lies in its standard unit-beta growing window

\[
\frac12\le |x_a(y_u)|\le1,
\]

then monotonicity of `E_{1,u}` on `[1/2,1]` and (A8) give

\[
\mathcal E_{1,u}(|x_a|)>-\frac{327}{800}.
\tag{A24}
\]

For every `a>=3`, (A22)–(A23) imply

\[
S_{a,u}
\le 3\left(-\frac{11}{250}\right)
+5\left(-\frac9{160}\right)
=-\frac{1653}{4000}.
\]

Combining with (A24),

\[
\boxed{
S_{a,u}-\mathcal E_{1,u}(|x_a|)
< -\frac9{2000},
\qquad a\ge3,
}
\tag{A25}
\]

whenever the mode is generated inside the standard growing window.

Together with the sharper `a=2` estimate (A18), this proves:

### In-window action filter

Apart from the deliberately resonant desired child `m_1`, every unit-beta member of the radial feedback ladder that is generated inside the standard growing window is exponentially **action-subcritical**. Its local positive growth rate does not by itself promote it to primary size.

## 9. Why v0.6 is preferable to v0.5

The previous v0.5 point `x_1=4/5` killed the first feedback inviscid term but placed `m_2=(2,-3)` at a supercritical reduced action mismatch. The new exact rational choice

\[
\boxed{x_1=3/4}
\]

moves the relay deeper into the parent/catalyst tails and changes the sign of this second-generation action balance.

The resulting hierarchy is now:

\[
\boxed{
\text{desired child: resonant action}
}
\]

\[
\boxed{
(1,-2):\ \text{purely radial stable correction}
}
\]

\[
\boxed{
(2,-3),(3,-5),\ldots:\ \text{growing if in-window, but exponentially action-subcritical}.
}
\]

This is a qualitatively cleaner zero-force correction architecture.

## 10. Remaining barrier

The theorem does not control lattice modes whose effective pulse coordinate lies outside the raw source window, nor does it prove that localized curl/cutoff corrections preserve the action gaps. The next local task is therefore:

1. source-audit the localized packet product to prove that no omitted term changes the action exponent;
2. classify **off-window** low lattice modes and show that they can be inverted without later re-entering as primary growing packets;
3. combine the action filter with the high-harmonic stable tail and exact sparse-support bookkeeping.
