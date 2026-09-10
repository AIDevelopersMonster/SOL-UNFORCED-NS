# v0.8 critical block cardinality: the compact-support route is large

**Status:** PROVED PRINCIPAL LATTICE COUNTING THEOREM. This theorem does not create a new obstruction to the v0.8 relay. It quantifies the price of insisting that every critical correction vanish at both ends of a self-contained finite collar.

The conclusion is that the potentially nondecaying scalar block is finite for each frozen design, as proved previously, but its size grows like `Theta(M^5)` along the large-`u_*` half-step family. This makes a literal one-compatibility-condition-per-mode multicollar implementation mathematically possible but architecturally unattractive.

## 1. Exact critical inequality

Fix the v0.8 family

\[
u_*=M^2,
\qquad
\beta_1=2,
\qquad
\beta_2=1,
\]

with exact relay root `x_M` from `integral_beta_v08_large_u_halfstep_family.md`. For a lattice index `(a,b)`, set

\[
T=2a+b,
\qquad
N=(2M+1)T-2a.
\]

At the relay center, for `T!=0`, the effective reduced slope is

\[
\xi_{T,N}
=\frac{x_MN}{2MT}.
\tag{K1}
\]

The exact beta-`|T|` turning coordinate is

\[
x_{|T|,M^2}
=
\sqrt{
|T|^{-4/3}
+
\frac{|T|^{-4/3}-1}{M^4}
}.
\tag{K2}
\]

A principal growing or neutral mode must satisfy

\[
|\xi_{T,N}|
\le x_{|T|,M^2}.
\]

Equivalently,

\[
\boxed{
|N|
\le
B_M(T)
:=
\frac{2M|T|}{x_M}
 x_{|T|,M^2}.
}
\tag{K3}

The turning point exists only when

\[
|T|
\le
K_M:=(1+M^4)^{3/4}.
\tag{K4}

Admissible integer pairs satisfy the parity condition

\[
N\equiv T\pmod2.
\tag{K5}

The `T=0` block is purely viscous and is not counted as critical.

## 2. Upper bound `O(M^5)`

The v0.8 theorem gives

\[
x_M\to2^{-2/3}.
\]

Hence, for all sufficiently large `M`,

\[
\frac12<x_M<1.
\tag{K6}

From (K2),

\[
x_{|T|,M^2}
\le |T|^{-2/3}.
\]

Therefore

\[
B_M(T)
\le4M|T|^{1/3}.
\tag{K7}

Also, for large `M`,

\[
K_M<2M^3.
\tag{K8}

For fixed positive `T`, the number of integers `N` satisfying (K3) and the parity constraint is at most

\[
B_M(T)+2
\le4MT^{1/3}+2.
\]

The negative-`T` block is its conjugate copy. Consequently

\[
\begin{aligned}
|\mathcal C_M|
&\le
2\sum_{1\le T<2M^3}
(4MT^{1/3}+2)\\
&\le C M^5
\end{aligned}
\tag{K9}

for an absolute constant `C` and all sufficiently large `M`.

## 3. Lower bound `Omega(M^5)`

Consider positive integers in the slab

\[
\frac{M^3}{16}
\le T\le
\frac{M^3}{8}.
\tag{K10}

For such `T`,

\[
T^{-4/3}
\ge16M^{-4}.
\]

Using (K2),

\[
\begin{aligned}
x_{T,M^2}^2
&=T^{-4/3}(1+M^{-4})-M^{-4}\\
&\ge T^{-4/3}-M^{-4}\\
&\ge\frac{15}{16}T^{-4/3}.
\end{aligned}
\]

Hence

\[
x_{T,M^2}
\ge\frac{\sqrt{15}}4T^{-2/3}.
\tag{K11}

For large `M`, `x_M<1`, so (K3) gives

\[
B_M(T)
\ge
\frac{\sqrt{15}}2 M T^{1/3}.
\tag{K12}

On the slab (K10),

\[
T^{1/3}\ge\frac{M}{16^{1/3}},
\]

and therefore every such `T` admits at least

\[
c_1M^2
\]

parity-compatible critical values of `N`, for a fixed `c_1>0` and all sufficiently large `M`.

The slab itself contains at least

\[
c_2M^3
\]

positive values of `T`. Thus

\[
|\mathcal C_M|
\ge cM^5.
\tag{K13}

Combining with (K9),

\[
\boxed{
|\mathcal C_M|=\Theta(M^5).
}
\tag{K14}

## 4. Numerical scale

The exact count is design-dependent through `x_M`, but the scaling is already visible at modest values. A direct enumeration of the center inequality gives approximately

\[
|\mathcal C_5|\approx7.9\times10^3,
\]

\[
|\mathcal C_{10}|\approx2.66\times10^5,
\]

\[
|\mathcal C_{20}|\approx8.88\times10^6.
\]

These numbers are diagnostics, not used in the proof.

## 5. Consequence for exact compact temporal support

`multicollar_finite_critical_transversality.md` remains mathematically valid: for every frozen `M` the critical block is finite, so finitely many compatibility moments can in principle be controlled.

However, (K14) shows that along the large-`u_*` family the naive implementation may require on the order of `M^5` scalar critical directions before reality/polarization multiplicities are even included.

Therefore **exact two-sided temporal compact support of every correction is an unnecessarily expensive local design requirement**.

The natural alternative is to formulate the relay as a forward input-output map on a bounded characteristic collar:

- prescribe the incoming correction at the entrance;
- solve the exact correction equation forward;
- allow the small correction to leave the relay collar as part of the outgoing state;
- use the v0.8 action filter to keep every non-designated outgoing component subcritical.

A forward initial-value problem imposes no Fredholm compatibility moment. The next theorem implements this route in the analytic lattice packet space.
