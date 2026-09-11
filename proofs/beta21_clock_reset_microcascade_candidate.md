# Beta-(2,1) finite clock-reset microcascade candidate

**Status:** NEW REDUCED ENVELOPE CONSTRUCTION / COMPUTER-ASSISTED TRANSVERSE CANDIDATE. This note gives a finite low-genealogy quadratic character chain that regenerates the original beta-two parent phase at the end of one clock-reset interval. The reduced action ledger can be tuned to exact equality with the original parent envelope while the first `2+(-1)->1` relay resonance remains exact. This removes the previous purely kinematic objection that clock reset necessarily requires `Theta(M)` genealogy in every `(2,1)` design.

It does **not** prove the localized unforced Navier--Stokes supercell. The new interactions use beta values up to `3`; every required polarization projection, timing/order compatibility, non-designated action exclusion, and exact phase-adapted PDE correction must still be proved.

## 1. Geometry and first designated relay

Use a general beta pair

\[
\beta_P=2,\qquad \beta_C=1,
\]

with first-event reduced coordinates

\[
x_P=x,\qquad x_C=x+\delta.
\]

The difference child

\[
D=P-C
\]

has beta `1` and reduced coordinate

\[
\boxed{x_D=x-\delta.}
\tag{MC1}
\]

Require the same reduced envelope resonance as the first relay:

\[
\boxed{
I_2(x)+I_1(x+\delta)-I_1(x-\delta)=0.
}
\tag{MC2}
\]

Unlike v0.8, `delta` is not tied to `1/(2M)`. We now choose it to make a finite reset microcascade possible.

## 2. Exact finite character chain

Starting from the physically present characters `P`, `C`, `D=P-C`, consider the following quadratic chain near a late pulse offset `s`:

\[
\boxed{P+C^*=D}\qquad\text{(the original relay),}
\]

then

\[
\boxed{C+D=P},
\tag{MC3}
\]

which can reinforce the parent,

\[
\boxed{P+D=E},
\qquad \beta_E=3,
\tag{MC4}
\]

\[
\boxed{E-C=Q},
\qquad \beta_Q=2,
\tag{MC5}
\]

\[
\boxed{Q-D=H},
\qquad \beta_H=1,
\tag{MC6}
\]

and finally at the reset face

\[
\boxed{H+D=P_{\rm new}},
\qquad \beta_{P_{\rm new}}=2.
\tag{MC7}
\]

In the integer `(P,C)` character basis these are

\[
D=P-C,
\qquad
E=2P-C,
\qquad
Q=2P-2C=2D,
\qquad
H=P-3C=3D-P,
\qquad
P_{\rm new}=2P-4C=H+D.
\tag{MC8}
\]

Equivalently, up to complex conjugation, `P_new` is the fixed low-genealogy character `(1,-4)` found by the bounded beta search. No coefficient grows with a large design integer.

## 3. Reduced slopes of the chain

At a common offset `s`, the reduced slope of a character `aP+bC` with beta `2a+b` is

\[
\boxed{
x_{a,b}(s)=x+s+\frac{b}{2a+b}\,\delta.}
\tag{MC9}
\]

Hence the relevant slopes are

\[
\begin{aligned}
x_C(s)&=x+\delta+s,\\
x_D(s)&=x-\delta+s,\\
x_E(s)&=x-\frac13\delta+s,\\
x_Q(s)&=x-\delta+s,\\
x_H(s)&=x-3\delta+s.
\end{aligned}
\tag{MC10}
\]

Choose the reset face

\[
\boxed{T=2\delta.}
\tag{MC11}
\]

Then

\[
x_H(T)=x-\delta,
\qquad
x_D(T)=x+\delta,
\tag{MC12}
\]

and therefore the final sum has reduced slope

\[
\boxed{
x_{P_{\rm new}}(T)=x.}
\tag{MC13}
\]

So the **beta-two parent slope is exactly reset** after a finite offset `T=2delta`.

This is a physical quadratic regeneration statement, not merely a `GL(2,Z)` reindexing.

## 4. Action bookkeeping for a late microcascade

At an offset `s`, let

\[
A_C=I_1(x+\delta+s),
\qquad
A_D=I_1(x-\delta+s).
\tag{MC14}
\]

If the first feedback `C+D->P` is used to place the parent on the combined source action, the succeeding idealized quadratic chain has source actions

\[
\begin{aligned}
A_P^{\rm boost}&=A_C+A_D,\\
A_E&=A_P^{\rm boost}+A_D=A_C+2A_D,\\
A_Q&=A_E+A_C=2A_C+2A_D,\\
A_H&=A_Q+A_D=2A_C+3A_D.
\end{aligned}
\tag{MC15}
\]

After generating `H` at `s`, propagate it homogeneously to `T=2delta`. Its action becomes

\[
A_H(T)
=A_H
+I_1(x-\delta)-I_1(x-3\delta+s).
\tag{MC16}
\]

The old child `D` at `T` has natural action `I_1(x+delta)`. Thus the final regenerated beta-two parent has action

\[
\boxed{
\begin{aligned}
\mathcal A_{\rm reset}(x,\delta,s)
={}&3I_1(x+\delta+s)
+2I_1(x-\delta+s)\\
&-I_1(x-3\delta+s)
+I_1(x-\delta)
+I_1(x+\delta).
\end{aligned}
}
\tag{MC17}
\]

Exact action renewal requires

\[
\boxed{
\mathcal A_{\rm reset}(x,\delta,s)=I_2(x).
}
\tag{MC18}
\]

To make the late generation point robust, impose stationarity in `s`:

\[
\boxed{
3I_1'(x+\delta+s)
+2I_1'(x-\delta+s)
-I_1'(x-3\delta+s)=0.
}
\tag{MC19}
\]

Equations (MC2), (MC18), (MC19) are three scalar equations for `(x,delta,s)`.

## 5. Computer-assisted transverse solution

High-precision solution gives

\[
\boxed{x_*\approx0.7859855569295219140,}
\tag{MC20}
\]

\[
\boxed{\delta_*\approx0.07069967306663885738,}
\tag{MC21}
\]

\[
\boxed{s_*\approx0.14119460888766346057.}
\tag{MC22}
\]

The reset face is

\[
\boxed{T_*=2\delta_*\approx0.14139934613327771476,}
\tag{MC23}
\]

so the late microcascade point lies just before reset:

\[
\boxed{T_*-s_*\approx2.04737245614254\times10^{-4}>0.}
\tag{MC24}
\]

The Jacobian of `(MC2),(MC18),(MC19)` with respect to `(x,delta,s)` is numerically

\[
\begin{pmatrix}
-1.6518333885 & 1.3197888106 & 0\\
2.5185939835 & 1.3593380231 & 0\\
-11.7665926443 & -13.0050969799 & -11.7665926443
\end{pmatrix},
\tag{MC25}
\]

with

\[
\boxed{\det\approx65.5330033379\ne0.}
\tag{MC26}
\]

The second derivative of the reset action defect in `s` is

\[
\boxed{\partial_s^2(\mathcal A_{\rm reset}-I_2(x))\approx-11.7665926443<0.}
\tag{MC27}
\]

so `s_*` is a strict local maximum of the available reset action.

The companion script `experiments/beta21_clock_reset_microcascade.py` reproduces these values at high precision. A publication claim would require interval certification; the present status is computer-assisted reduced construction.

## 6. Action ledger at the solution

At `s=s_*`,

\[
I_1(x+\delta+s)\approx-6.74263\times10^{-6},
\]

\[
I_1(x-\delta+s)\approx-0.0310166810.
\]

The successive source actions are approximately

\[
\begin{aligned}
A_P^{\rm boost}&=-0.0310234236,\\
A_E&=-0.0620401047,\\
A_Q&=-0.0620468473,\\
A_H&=-0.0620535899.
\end{aligned}
\tag{MC28}
\]

Their natural envelope actions at the same location are more negative:

\[
\begin{aligned}
I_2(x+s)&\approx-0.342926,\\
I_3(x-\delta/3+s)&\approx-1.249061,\\
I_2(x-\delta+s)&\approx-0.197197,\\
I_1(x-3\delta+s)&\approx-0.123909.
\end{aligned}
\tag{MC29}
\]

Thus every promoted intermediate mode in this formal chain has positive action headroom at the reduced-envelope level.

After propagation to `T=2delta`, the final ledger gives

\[
\boxed{A_{P_{\rm new}}(T)=I_2(x)}
\tag{MC30}
\]

numerically to the working precision.

## 7. What was learned from the failed `(3,2)` attempt

The `(3,2)` construction in `beta32_commensurate_clock_reset_candidate.md` solves the kinematic clock commensurability elegantly, but its reset basis characters are not automatically populated. The present search instead asks for an explicit bounded quadratic genealogy and tunes the envelope geometry around that genealogy.

This changes the design principle:

\[
\boxed{
\text{first choose a finite physically generatable reset tree,}
\quad
\text{then solve its envelope resonance equations.}
}
\tag{MC31}
\]

rather than solving a lattice-basis reset first and hoping amplitude follows.

## 8. Remaining obligations

This candidate is promising but is not yet a relay theorem. The next mandatory checks are:

1. derive and sign the exact principal Leray/growing-polarization coefficient for every interaction (MC3)--(MC7); a single zero coefficient kills the chain;
2. prove that the proposed ordering near `s_*` can be separated into finitely many collars without losing the action equality by more than the available transversality correction;
3. redo the global lattice action filter with `E,Q,H` declared designated modes and show that no competing non-designated mode gains comparable action;
4. prove finite-`u_*` persistence for the full multi-equation resonance system using the source exact primitive `mathcal E_{beta,u}`;
5. only after those steps port the phase-adapted exact zero-residual contraction machinery.

If items 1--3 close, the project will have crossed an important conceptual boundary: a finite physical phase-amplitude reset supercell will exist at principal reduced level, rather than only an amplitude-renewal cell.