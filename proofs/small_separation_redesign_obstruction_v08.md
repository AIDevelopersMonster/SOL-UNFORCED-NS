# No `O(1/M)` renewal delay in the current v0.8 `(2,1)` large-`u_*` family

**Status:** PROVED ASYMPTOTIC OBSTRUCTION. The clock-reset theorem suggests redesigning the relay so that the second event occurs only `O(1/M)` after the first, because then a bounded-degree lattice descendant could in principle compensate the offset. This note proves that the present v0.8 family cannot be tuned that way while retaining its current `(beta_2,beta_1)=(2,1)` and large-`u_*` asymptotics.

Thus the next redesign must change more than the location of the second collar inside the existing family.

## 1. Source action

For `beta>0` and `u>0`, write

\[
\mathcal E_{\beta,u}(x)
\]

for the exact principal source action normalized to vanish at its turning point

\[
x_{\beta,u}
=\sqrt{\beta^{-4/3}+\frac{\beta^{-4/3}-1}{u^2}}.
\tag{SR1}
\]

For beta `1`, this gives exactly

\[
\boxed{x_{1,u}=1.}
\tag{SR2}
\]

The derivative is

\[
\boxed{
\partial_x\mathcal E_{\beta,u}(x)
=
\frac{u}{\sqrt{1+u^2x^2}}
-
\frac{\beta^2u(1+u^2x^2)}{(1+u^2)^{3/2}}.
}
\tag{SR3}
\]

For `beta=1` and `0<x<1`, the first term is strictly larger than the second, so

\[
\partial_x\mathcal E_{1,u}(x)>0.
\tag{SR4}
\]

Since `E_{1,u}(1)=0`, it follows that

\[
\boxed{
\mathcal E_{1,u}(x)<0
\quad(0<x<1).
}
\tag{SR5}
\]

## 2. First v0.8 event

The current family fixes

\[
u_*=M^2,
\qquad
\beta_P=2,
\qquad
\beta_C=1,
\]

and

\[
y_M=x_M+d_M,
\qquad
c_M=x_M-d_M,
\qquad
d_M=\frac{x_M}{2M}.
\tag{SR6}
\]

The first designated difference event is selected by

\[
\boxed{
\mathcal E_{2,M^2}(x_M)
+
\mathcal E_{1,M^2}(y_M)
-
\mathcal E_{1,M^2}(c_M)
=0.
}
\tag{SR7}
\]

Because `d_M=O(M^{-1})`, the last two terms differ by `O(M^{-1})` on compact subintervals. Therefore

\[
\mathcal E_{2,M^2}(x_M)=O(M^{-1}).
\tag{SR8}
\]

The already established v0.8 root theorem gives the sharper limit

\[
\boxed{x_M\to x_{2,\infty}=2^{-2/3}.}
\tag{SR9}
\]

## 3. Hypothetical short renewal delay

Suppose one tried to tune the second event so that

\[
\theta_M=O(M^{-1}).
\tag{SR10}
\]

The second event would require the beta-one pair to regenerate beta two, hence the principal action equality

\[
\boxed{
\mathcal E_{1,M^2}(y_M+\theta_M)
+
\mathcal E_{1,M^2}(c_M+\theta_M)
-
\mathcal E_{2,M^2}(x_M+\theta_M)
=0.
}
\tag{SR11}
\]

Under (SR9)--(SR10),

\[
y_M+\theta_M\to2^{-2/3},
\qquad
c_M+\theta_M\to2^{-2/3},
\qquad
x_M+\theta_M\to2^{-2/3}.
\tag{SR12}
\]

The beta-two action at its limiting turning point tends to zero:

\[
\mathcal E_{2,M^2}(x_M+\theta_M)\to0.
\tag{SR13}
\]

For beta one, the large-`u` limit at a fixed `0<x<1` exists and is

\[
\mathcal E_{1,\infty}(x)
=
\log x-\frac{x^3-1}{3}.
\tag{SR14}
\]

At

\[
x_2:=2^{-2/3}<1,
\]

(SR5) and direct substitution give

\[
\boxed{
\mathcal E_{1,\infty}(x_2)
=
-\frac23\log2+\frac14
<0.
}
\tag{SR15}
\]

Indeed `2 log 2/3 > 1/4`.

Taking the limit in the left side of (SR11) therefore gives

\[
\boxed{
2\mathcal E_{1,\infty}(2^{-2/3})
=
-\frac43\log2+\frac12
<0,
}
\tag{SR16}
\]

not zero. This contradicts (SR11).

Hence

\[
\boxed{
\theta_M\neq O(M^{-1})
}
\tag{SR17}
\]

for any renewal root in the present v0.8 large-`u_*` family.

## 4. In fact the delay stays macroscopic

The previously derived limiting renewal equation is

\[
H_\infty(z)
=
\log z-\frac23\log2+\frac23z^3+\frac13,
\tag{SR18}
\]

with

\[
H_\infty'(z)=\frac1z+2z^2>0.
\tag{SR19}
\]

It has a unique root

\[
z_*\approx0.8041741675.
\]

Since the first event tends to

\[
x_2=2^{-2/3}\approx0.6299605249,
\]

the actual renewal delay satisfies

\[
\boxed{
\theta_M^{\rm ren}\to
\theta_*:=z_*-2^{-2/3}
\approx0.1742136425>0.
}
\tag{SR20}
\]

Thus the delay is genuinely `Theta(1)` in reduced pulse coordinate.

## 5. Combination with the clock-reset theorem

`clock_reset_requires_high_genealogy.md` proves that a unit-beta descendant capable of compensating a delay `theta` needs an original catalyst coefficient

\[
b=-\frac{2M\theta}{x_M}.
\tag{SR21}
\]

Using (SR20),

\[
\boxed{
\frac{|b|}{M}
\to
\frac{2\theta_*}{2^{-2/3}}
\approx0.55309.
}
\tag{SR22}
\]

Therefore the macroscopic renewal delay and the `Theta(M)` genealogical clock-reset cost are two sides of the same obstruction.

## 6. Consequence for redesign

Merely sliding the second collar inside the current `(2,1)`, `u_*=M^2` v0.8 family cannot produce a source-compatible `O(1/M)` renewal interval.

A low-genealogy clock-closing redesign must alter at least one structural ingredient:

- the beta pair / harmonic arithmetic;
- the large-`u_*` scaling law;
- or the number/type of independent incoming phase banks.

The next economical search is therefore a generalized two-event resonance family with variable integer beta pair `(p,q)` and a required renewal delay comparable to the intrinsic lattice spacing, rather than another modification of the already exhausted `(2,1)` half-step family.