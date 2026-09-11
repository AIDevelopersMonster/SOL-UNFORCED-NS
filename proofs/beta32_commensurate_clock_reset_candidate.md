# Beta-(3,2,1) commensurate clock-reset relay candidate

**Status:** NEW REDUCED-MODEL CONSTRUCTION / EXACT FINITE-`u_*` PERSISTENCE REDUCTION. A reproducible high-precision sign/Jacobian certificate identifies a reduced two-event resonance whose event separation is exactly the *minimal integer clock-reset distance* of the `(3,2)` phase lattice. Because the exact source envelope converges in `C^1` to the reduced envelope for the fixed beta set `{1,2,3}`, the nondegenerate reduced root persists for all sufficiently large finite `u_*` once the reduced root is interval-certified. The full localized Navier--Stokes relay is **not** proved here: principal polarization, the new action filter, and physical promotion of the reset characters remain open.

The important advance over v0.8 is structural. The old `(2,1)` cell required a clock-reset character whose genealogy depth grew like `Theta(M)`. The present `(3,2)` geometry makes the reset arithmetic finite and level-independent.

## 1. Reduced source envelope

Use the source-derived large-`u_*` primitive

\[
I_\beta(x)
=\log(x\beta^{2/3})
-\frac{\beta^2}{3}(x^3-\beta^{-2}),
\qquad
I_\beta'(x)=\frac1x-\beta^2x^2.
\tag{B32-1}
\]

Take the phase beta triangle

\[
\boxed{p=3,\qquad q=2,\qquad r=p-q=1.}
\tag{B32-2}
\]

Let the first-event reduced coordinates be

\[
x_P=x,\qquad x_C=x+\delta.
\]

Exact phase locking of the difference child `D=P-C` requires

\[
r x_D=p x_P-q x_C,
\]

hence

\[
\boxed{x_D=x-2\delta.}
\tag{B32-3}
\]

## 2. First and second resonance equations

The first difference event

\[
P+C^*\longrightarrow D
\]

has the reduced envelope equation

\[
\boxed{
F_1(x,\delta)
:=I_3(x)+I_2(x+\delta)-I_1(x-2\delta)=0.
}
\tag{B32-4}
\]

After a common pulse drift `theta`, the feedback event

\[
C+D\longrightarrow P
\]

has mismatch

\[
I_2(x+\delta+\theta)
+I_1(x-2\delta+\theta)
-I_3(x+\theta).
\tag{B32-5}
\]

The lattice calculation below shows that the **minimal nontrivial exact reset** of the `(3,2)` generator pair occurs when

\[
\boxed{\theta=6\delta.}
\tag{B32-6}
\]

Imposing this from the outset gives the second equation

\[
\boxed{
F_2(x,\delta)
:=I_2(x+7\delta)
+I_1(x+4\delta)
-I_3(x+6\delta)=0.
}
\tag{B32-7}
\]

Thus clock commensurability and the two event resonances reduce to two scalar equations in `(x,delta)`.

## 3. High-precision reduced root

The system (B32-4), (B32-7) has the numerical root

\[
\boxed{
 x_*\approx0.6496821163284529427446342426,
}
\tag{B32-8}
\]

\[
\boxed{
 \delta_*\approx0.0001541755117697605484905616362.
}
\tag{B32-9}
\]

Therefore

\[
\boxed{
\theta_*=6\delta_*
\approx0.000925053070618563290943369817.
}
\tag{B32-10}
\]

The relevant coordinates are all strictly inside the source pulse interval `(1/2,3/2)`:

\[
\begin{aligned}
x_P&\approx0.6496821163,\\
x_C&\approx0.6498362918,\\
x_D&\approx0.6493737653,
\end{aligned}
\]

and at the second event

\[
\begin{aligned}
x_P+\theta_*&\approx0.6506071694,\\
x_C+\theta_*&\approx0.6507613449,\\
x_D+\theta_*&\approx0.6502988184.
\end{aligned}
\tag{B32-11}
\]

The residuals are below `10^-40` in the companion high-precision script.

## 4. Transversality of the reduced root

At the root, differentiation of (B32-4), (B32-7) gives numerically

\[
D(F_1,F_2)
\approx
\begin{pmatrix}
-3.5281259834&2.0862180724\\
3.2301477902&16.9938549803
\end{pmatrix}.
\tag{B32-12}
\]

Hence

\[
\boxed{
\det D(F_1,F_2)(x_*,\delta_*)
\approx-66.6952540099\ne0.
}
\tag{B32-13}
\]

A small rectangle around (B32-8)--(B32-9) also exhibits the Poincare--Miranda sign pattern: taking

\[
|x-x_*|\le10^{-5},
\qquad
|\delta-\delta_*|\le5\cdot10^{-6},
\tag{B32-14}
\]

high-precision evaluation gives `F_1>0` on the left `x` face and `F_1<0` on the right `x` face, while `F_2<0` on the lower `delta` face and `F_2>0` on the upper `delta` face. The smallest displayed face margins are about `2.0e-5`.

For publication this numerical certificate should be rerun with outward-rounded interval arithmetic. The repository script records the values needed for that audit. Until then we call (B32-8)--(B32-13) a **computer-assisted reduced root**, not a publication-final analytic theorem.

## 5. General minimal clock-reset arithmetic

The commensurability `theta=6 delta` is not guessed. It is the minimal integer reset distance for a primitive `(p,q)` beta pair.

Let `p>q>0`, `r=p-q`, and assume `gcd(p,q)=1`. At a first event use

\[
x_P=x,
\qquad
x_C=x+\delta,
\qquad
x_D=x-\frac qr\delta.
\tag{B32-15}
\]

At a later common offset `theta`, the post-event basis is `(P,D)` with beta vector `(p,r)`. Seek an integer unimodular matrix

\[
U=\begin{pmatrix}a&b\\c&d\end{pmatrix}
\]

such that it maps both the beta vector and the beta-weighted radial vector to a reset `(P,C)` input geometry:

\[
U\binom p r=\binom p q,
\tag{B32-16}
\]

\[
U\binom{p(x+\theta)}{r(x+\theta)-q\delta}
=\binom{px}{q(x+\delta)}.
\tag{B32-17}
\]

The first row of (B32-16) has the general form

\[
a=1+rk,
\qquad
b=-pk,
\tag{B32-18}
\]

and (B32-17) then forces

\[
\theta=-kq\delta.
\tag{B32-19}
\]

The second row has the general form

\[
c=1+rm,
\qquad
d=-1-pm,
\tag{B32-20}
\]

and its radial equation forces

\[
\theta=-mp\delta.
\tag{B32-21}
\]

For positive `theta`, the smallest simultaneous integer solution therefore satisfies

\[
\boxed{
\frac\theta\delta=\operatorname{lcm}(p,q)=pq
}
\tag{B32-22}
\]

for a primitive pair.

For `(p,q)=(3,2)`, this gives exactly

\[
\boxed{\theta=6\delta.}
\]

Thus the reduced root above is synchronized with the **minimal possible integer phase reset**, not with an arbitrarily chosen separation.

## 6. Exact reset matrix for `(3,2)`

At the minimal reset, solving (B32-16)--(B32-17) gives

\[
\boxed{
U_{32}
=\begin{pmatrix}
-2&9\\
-1&5
\end{pmatrix},
\qquad
\det U_{32}=-1.
}
\tag{B32-23}
\]

Therefore, from the post basis `(P,D)`, define

\[
\boxed{
P_{\rm new}=-2P+9D,
\qquad
C_{\rm new}=-P+5D.
}
\tag{B32-24}
\]

Because `D=P-C`, equivalently

\[
P_{\rm new}=7P-9C,
\qquad
C_{\rm new}=4P-5C.
\tag{B32-25}
\]

Their beta labels are exactly

\[
\beta(P_{\rm new})=3,
\qquad
\beta(C_{\rm new})=2,
\]

and, when `theta=6 delta`, their reduced radial coordinates are **exactly** the original first-event values

\[
\boxed{x_{P_{\rm new}}=x,\qquad x_{C_{\rm new}}=x+\delta.}
\tag{B32-26}
\]

Thus the phase lattice itself admits a finite, exact, level-independent clock reset.

## 7. Exact finite-`u_*` persistence

For the fixed beta set `{1,2,3}`, `beta_phase_stability.md` proves

\[
\mathcal E_{\beta,u}(x)=I_\beta(x)+O(u^{-2})
\]

in `C^1` on compact positive `x` intervals.

Replace `I_beta` by the exact source primitive `mathcal E_{beta,u}` in (B32-4), (B32-7), while retaining the exact arithmetic constraint `theta=6 delta`. Since the reduced Jacobian is transverse by (B32-13), the implicit-function theorem gives, once the reduced root is interval-certified, a unique exact finite-`u` branch

\[
\boxed{(x_u,\delta_u)\to(x_*,\delta_*)}
\tag{B32-27}
\]

for all sufficiently large `u`.

A diagnostic solve at `u=100` gives

\[
x_{100}\approx0.6496346318463,
\qquad
\delta_{100}\approx0.0001541549170,
\tag{B32-28}
\]

again with `theta_100=6 delta_100` imposed exactly.

The important point is that finite-`u` persistence uses a fixed finite beta set, so the existing source `C^1` convergence applies directly; no growing-beta uniformity is being assumed.

## 8. What this actually fixes

For v0.8 `(2,1)`, the renewal separation is asymptotically `0.174...` while the integer slope lattice spacing is `O(1/M)`. Hence a reset needs genealogy depth `Theta(M)`.

For the new `(3,2)` reduced design,

\[
\boxed{\theta_*/\delta_*=6}
\tag{B32-29}
\]

and the reset matrix (B32-23) has fixed coefficients. Therefore the **diverging genealogy-depth obstruction is removed at the kinematic/envelope level**.

This is a genuine step toward an autonomous cascade: the clock-reset problem has changed from an asymptotically deep lattice problem to a fixed finite-dimensional supercell problem.

## 9. What remains open

Three major tasks remain before this candidate can replace v0.8:

1. derive the principal quadratic polarization coefficients for `3+(-2)->1` and `2+1->3` and prove nonvanishing with margins;
2. redo the complete action-filter theorem for the `(3,2)` lattice, including the deliberately promoted reset characters in (B32-24);
3. construct a finite sequence of exact quadratic events that gives the reset characters **order-one designated amplitudes**. A unimodular relabelling alone does not create physical Fourier amplitude on those characters.

Only after these close should the phase-adapted zero-residual and two-collar `C^1` machinery be ported from v0.8 to the new supercell.