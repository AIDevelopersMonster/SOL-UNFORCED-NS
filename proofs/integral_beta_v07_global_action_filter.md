# v0.7 rational half-step relay: global principal action filter

**Status:** PROVED PRINCIPAL ENVELOPE/LATTICE THEOREM, conditional only on the certified scalar resonance parameter described in Section 2. The existence sign check is reproducible by interval arithmetic in `experiments/integral_beta_v07_interval_certificate.py`. This is not yet a localized Navier–Stokes relay theorem.

The point of v0.7 is to attack the **off-window low lattice modes** left open by v0.6. Instead of treating only the unit-beta radial-feedback ladder, the arithmetic is chosen so that the complete two-generator harmonic lattice can be classified.

## 1. Rational half-step geometry

Take

\[
\boxed{
\beta_1=2,
\qquad
\beta_2=1,
\qquad
x_1=\frac{29}{40}.
}
\tag{G1}
\]

Choose the catalyst and desired child coordinates by

\[
\boxed{
y=\frac{37}{36}x_1=\frac{1073}{1440},
\qquad
x_c=\frac{35}{36}x_1=\frac{203}{288}.}
\tag{G2}
\]

Then

\[
2x_1-y=x_c,
\]

so the desired difference harmonic is again a unit-beta child.

The first radial feedback step has coordinate difference

\[
2(x_1-y)=-\frac{29}{720}.
\]

For the unit-beta ladder `m_a=(a,1-2a)`,

\[
x_a
=2ax_1+(1-2a)y
=\frac{1073-58a}{1440}.
\tag{G3}
\]

Hence zero lies **exactly halfway between** the two integer indices `a=18` and `a=19`:

\[
x_{18}=\frac{29}{1440},
\qquad
x_{19}=-\frac{29}{1440}.
\tag{G4}
\]

Thus the near-tangential accident seen in v0.6 is replaced by an exact arithmetic gap.

## 2. Exact finite-u resonance at a tuned `u_*`

Let `E_{beta,u}(x)` denote the exact normalized envelope primitive from `beta_phase_stability.md`. Define

\[
\boxed{
R(u)
=
\mathcal E_{2,u}\!\left(\frac{29}{40}\right)
+
\mathcal E_{1,u}\!\left(\frac{1073}{1440}\right)
-
\mathcal E_{1,u}\!\left(\frac{203}{288}\right).
}
\tag{G5}
\]

Direct outward interval evaluation gives

\[
R(20)
< -6.99\times10^{-4}<0,
\]

and

\[
R(100)
> 1.03\times10^{-4}>0.
\]

The interval enclosures are printed by `experiments/integral_beta_v07_interval_certificate.py`. By continuity there exists at least one

\[
\boxed{u_\dagger\in(20,100)}
\tag{G6}
\]

such that

\[
\boxed{
\mathcal E_{2,u_\dagger}(x_1)
+
\mathcal E_{1,u_\dagger}(y)
=
\mathcal E_{1,u_\dagger}(x_c).
}
\tag{G7}
\]

Numerically the root is

\[
\boxed{u_\dagger\approx49.35646602870114.}
\tag{G8}
\]

No uniqueness in `u` is needed below; every root in `(20,100)` obeys the same action estimates.

At any such root the beta-two parent is decaying because

\[
x_{2,u}<2^{-2/3}<\frac{63}{100}<x_1,
\]

while catalyst and child are growing because

\[
y<1,
\qquad x_c<1,
\]

and the unit-beta turning point is exactly one.

## 3. Exact arithmetic of the whole phase lattice

Let `(a,b) in Z^2` denote the phase

\[
a\Phi_1+b\Phi_2.
\]

Its tangential coefficient is the integer

\[
\boxed{T=2a+b.}
\tag{G9}
\]

Its reduced radial coefficient is

\[
r=2ax_1+by.
\]

Introduce

\[
\boxed{N=37T-2a.}
\tag{G10}
\]

Then exact arithmetic gives

\[
\boxed{
r=\frac{29}{1440}N.}
\tag{G11}
\]

Conversely,

\[
a=\frac{37T-N}{2},
\qquad
b=N-36T,
\tag{G12}
\]

so admissible pairs `(T,N)` satisfy

\[
N\equiv T\pmod2.
\]

Thus the reference normal lattice has the particularly simple form

\[
\boxed{
(u r,T)
=
\left(
\frac{29u}{1440}N,\ T
\right),
\qquad N\equiv T\pmod2.
}
\tag{G13}
\]

This converts the off-window problem into integer arithmetic.

## 4. Source action bound

At the tuned root set

\[
A:=\mathcal E_{2,u_\dagger}(x_1),
\qquad
B:=\mathcal E_{1,u_\dagger}(y).
\]

Both are negative. Any monomial assembled from the two real parent packets and producing lattice index `(a,b)` contains at least `|a|` parent-1 factors and `|b|` catalyst factors. Extra cancelling factors only make the envelope smaller. Therefore the **largest possible source action** at that lattice index is

\[
\boxed{
S_{a,b}=|a|A+|b|B.
}
\tag{G14}

The following uniform bounds hold for every `20<=u<=100`:

\[
\boxed{A<-\frac{33}{1000},
\qquad
B<-\frac{12}{125}.}
\tag{G15}

### Bound for `A`

For `u>=20`, with

\[
c_u=(1+u^{-2})^{-3/2}\ge\frac{797}{800},
\]

the beta-two derivative satisfies

\[
H_{2,u}(x)
\le
\frac1x-\frac{797}{200}x^2.
\]

Also `x_{2,u}<2^{-2/3}<63/100`. Hence

\[
A
\le
\int_{63/100}^{29/40}
\left(\frac1x-\frac{797}{200}x^2\right)dx
< -\frac{33}{1000}.
\]

The final strict inequality follows from the alternating upper bound for `log(1+19/126)`; using the first three terms already gives the rational upper value `-0.033485...`.

### Bound for `B`

For unit beta and `x in [y,1]`,

\[
H_{1,u}(x)
\ge
\frac1x-x^2
-
\frac1{u^2}
\left(1+\frac1{2x^3}\right).
\]

Since `u>=20`, integration from `y` to one and the positive series for `-log(1-z)`, `z=1-y=367/1440`, give

\[
-B=\int_y^1H_{1,u}(x)dx
>0.096024...>\frac{12}{125}.
\]

This proves (G15).

## 5. Universal lower bound for every growing natural envelope

Let `beta>=1` and suppose its positive turning point exists. Put

\[
z_{\beta,u}=u x_{\beta,u}
=\sqrt{(1+u^2)\beta^{-4/3}-1}.
\]

At zero slope,

\[
\mathcal E_{\beta,u}(0)
=\psi(z_{\beta,u}),
\]

where

\[
\psi(z)
=-\operatorname{arsinh}z
+
\frac{z+z^3/3}{(1+z^2)^{3/2}}.
\tag{G16}
\]

A direct differentiation gives

\[
\boxed{
\psi'(z)
=-\frac{3z^2+z^4}{(1+z^2)^{5/2}}<0
\qquad(z>0).
}
\tag{G17}
\]

Since `beta>=1`, `z_{beta,u}<=u`. Therefore

\[
\mathcal E_{\beta,u}(0)
\ge
\mathcal E_{1,u}(0).
\]

The exact envelope is increasing from zero slope to the growing turning point, so every point on a growing branch satisfies

\[
\mathcal E_{\beta,u}(x)
\ge
\mathcal E_{1,u}(0).
\]

For `u<=100`, monotonicity of `psi` gives

\[
\mathcal E_{1,u}(0)
\ge\psi(100)>-5.
\tag{G18}
\]

For the last estimate, `arsinh(100)<log 201<16/3`, while `(u+u^3/3)/(1+u^2)^{3/2}>1/3` for `u>=1`.

Thus

\[
\boxed{
\text{every growing lattice mode at }u_\dagger\text{ has natural action}>-5.}
\tag{G19}

## 6. All modes with `|T|>=4` are automatically action-subcritical

By conjugation it suffices to take `T>0`. A growing mode has

\[
x=\frac{29|N|}{1440T}<T^{-2/3},
\]

hence

\[
|N|<\frac{1440}{29}T^{1/3}.
\tag{G20}
\]

For `T>=4`,

\[
T^{1/3}<\frac25T,
\]

so

\[
|N|<\frac{576}{29}T<36T.
\]

Therefore `a>0` and `b<0`. Using (G12) and (G15),

\[
\begin{aligned}
S_{a,b}
&<
-\frac{33}{2000}(37T-N)
-\frac{12}{125}(36T-N)\\
&=
-\frac{8133}{2000}T
+\frac9{80}N.
\end{aligned}
\]

Using (G20) and `T^{1/3}<2T/5`,

\[
S_{a,b}
<
-\frac{106257}{58000}T.
\]

Thus for every `T>=4`,

\[
\boxed{S_{a,b}<-7.3<-5.}
\tag{G21}
\]

Together with (G19), every growing mode with `|T|>=4` is strictly action-subcritical.

If the turning point does not exist, the mode is already viscously stable and needs no action comparison.

## 7. The finite low block `T=1,2,3`

The remaining growing modes are finite. The key simplification is concavity:

\[
\partial_x^2\mathcal E_{\beta,u}(x)
=
-\frac{u^3x}{(1+u^2x^2)^{3/2}}
-
\frac{2\beta^2u^3x}{(1+u^2)^{3/2}}
<0
\tag{G22}
\]

for `x>0`.

Hence, on every interval where the signs of `a,b,N` are fixed,

\[
S_{a,b}-\mathcal E_{T,u}\!\left(\frac{29|N|}{1440T}\right)
\]

is a convex function of the continuous variable `N`. Its maximum on each such interval occurs at an endpoint.

### `T=1`

Growing implies `|N|<=49` and `N` is odd. The two primary resonances are

\[
N=37 \quad\text{(catalyst)},
\qquad
N=35 \quad\text{(desired child)}.
\]

After removing them, convexity reduces all other growing modes to the six endpoint checks

\[
N=1,33,-1,-49,39,49.
\]

They are strictly subcritical using (G15) and the elementary unit-beta bound

\[
\mathcal E_{1,u}(x)
\ge
\log x+\frac{797}{2400}(1-x^3),
\qquad 0<x\le1.
\tag{G23}
\]

Useful coarse consequences are

\[
\mathcal E_{1,u}(x)>-0.191\quad(x\ge13/20),
\]

\[
\mathcal E_{1,u}(x)>-3.7\quad(x\ge1/50),
\]

and

\[
\mathcal E_{1,u}(x)>-0.1\quad(x\ge3/4).
\]

For example the nearest nonprimary descendant `N=33`, namely `(a,b)=(2,-3)`, satisfies

\[
S_{2,-3}< -0.354,
\qquad
\mathcal E_{1,u}(33\cdot29/1440)>-0.191,
\]

so

\[
\boxed{
S_{2,-3}-\mathcal E_{1,u}(33\cdot29/1440)<-0.163.
}
\tag{G24}
\]

The other five endpoint margins are larger.

### `T=2`

Growing implies `|N|<=62`, with `N` even. Here `a>0,b<0` throughout. Convexity reduces the block to

\[
N=-62,0,62.
\]

The pure tangential mode `N=0` has `(a,b)=(37,-72)`, so (G15) gives `S<-8.1<-5`. At `N=62`,

\[
(a,b)=(6,-10),
\qquad
x=\frac{899}{1440}.
\]

If it is growing, its turning point is below `63/100`; since `H<=1/x` on the growing side,

\[
\mathcal E_{2,u}(x)
> -\log\frac{63/100}{x}
> -\frac1{20}.
\]

But `S<-1.158`, hence this endpoint is strongly subcritical. The negative endpoint has still smaller source action.

### `T=3`

Growing implies `|N|<=71`, with `N` odd. Convexity reduces the block to

\[
N=-71,-1,1,71.
\]

The three endpoints other than `N=71` already have source action below `-5`. For `N=71`,

\[
(a,b)=(20,-37),
\qquad
x=\frac{2059}{4320}>\frac{19}{40}.
\]

The beta-three turning point is below `1/2`, hence

\[
\mathcal E_{3,u}(x)
> -\log\frac{1/2}{x}
> -\frac1{19},
\]

whereas `S<-4.212`. Thus this endpoint is also strongly subcritical.

## 8. Global principal action-filter theorem

Combine Sections 5–7.

### Theorem

At any tuned resonance `u_dagger in (20,100)` satisfying (G7), every nonzero harmonic-lattice mode generated inside the bounded relay supernode falls into exactly one of the following classes:

1. the deliberate catalyst `(0,1)` or its conjugate;
2. the deliberate desired child `(1,-1)` or its conjugate, for which the envelope action is exactly resonant;
3. a mode whose principal net rate is nonpositive;
4. a growing mode whose maximal source action is strictly below its natural growing envelope action.

Moreover, every class-4 mode has a uniform action deficit

\[
\boxed{
S_{a,b}
-
\mathcal E_{|T|,u_\dagger}
\left(\frac{29|N|}{1440|T|}\right)
< -0.15.
}
\tag{G25}
\]

The conservative constant `0.15` is set by the nearest `T=1,N=33` descendant; all other endpoint estimates above are stronger.

Thus, if

\[
\Lambda_*=\frac{\lambda_0L_s}{u_\dagger},
\]

then after maximal homogeneous amplification to its natural peak, every non-designated growing harmonic retains at least the factor

\[
\boxed{
\exp(-0.15\Lambda_*)=e^{-cS_*}.
}
\tag{G26}

This includes the previously open **off-window** growing modes with effective `|x|<1/2`.

## 9. What this closes and what it does not

This closes the off-window low-mode problem at the **principal finite-u envelope/lattice level** for the tuned v0.7 geometry. The important point is that local positive growth no longer implies danger: every non-designated growing lattice mode is born with a larger negative action than the maximum growth it can subsequently recover.

It does **not** yet prove exact zero-force closure because:

1. the source construction chooses `u_*` only by a strict cone-margin requirement; the repository has not yet proved that the particular root `u_dagger≈49.36` exceeds that profile-dependent threshold;
2. the exact localized curl/cutoff/transport/Leray calculus must preserve the action count (G14) without introducing a new exponential factor;
3. exponentially subcritical modes must still be solved **exactly**, not discarded;
4. interactions after the bounded relay supernode and physical-scale inheritance remain separate global problems.

The next design question is whether the rational half-step construction can be made into a family whose tuned resonance occurs at arbitrarily large admissible `u_*` while retaining a global lattice action gap.
