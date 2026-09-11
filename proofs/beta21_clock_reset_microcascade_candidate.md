# Beta-(2,1) finite clock-reset microcascade candidate

**Status:** CORRECTED REDUCED ENVELOPE CONSTRUCTION / PRINCIPAL POLARIZATION AUDIT PASSED. The computer-assisted transverse root is unchanged, but the event genealogy and signed-beta bookkeeping are corrected here. The correct late chain is

\[
C+D\to P,\qquad
P+D\to E,\qquad
E-C\to Q,\qquad
Q-C\to H,\qquad
H+D\to P_{\rm new}.
\]

The previous draft accidentally wrote `Q-D -> H` and consequently displayed two wrong character identities. The numerical action equations, the slope `x_H=x-3delta+s`, and the reset-action formula were already those of the **correct** `Q-C -> H` chain, so the transverse root below does not change.

This note still does **not** prove the localized unforced Navier--Stokes supercell. Timing separation, the promoted-mode action filter, exact finite-`u_*` persistence, and the phase-adapted PDE correction remain open.

## 1. Geometry and first relay

Take

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

has signed beta `1` and reduced coordinate

\[
\boxed{x_D=x-\delta.}
\tag{MC1}
\]

The first reduced envelope resonance is

\[
\boxed{
I_2(x)+I_1(x+\delta)-I_1(x-\delta)=0.
}
\tag{MC2}
\]

## 2. Correct finite character chain

Starting from the physically present characters `P`, `C`, and `D=P-C`, use near a late pulse offset `s`

\[
\boxed{C+D=P},
\tag{MC3}
\]

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
\boxed{Q-C=H},
\qquad \beta_H=1,
\tag{MC6}
\]

and finally at the reset face

\[
\boxed{H+D=P_{\rm new}},
\qquad \beta_{P_{\rm new}}=2.
\tag{MC7}
\]

In the integer `(P,C)` character basis,

\[
\boxed{
\begin{aligned}
D&=P-C,\\
E&=2P-C,\\
Q&=2P-2C=2D,\\
H&=2P-3C=3D-P,\\
P_{\rm new}&=3P-4C=H+D=4D-P.
\end{aligned}}
\tag{MC8}
\]

The signed-beta functional is

\[
\beta(aP+bC)=2a+b.
\tag{MC9}
\]

Therefore

\[
\beta(D,E,Q,H,P_{\rm new})=(1,3,2,1,2)
\]

exactly. In particular the reset parent is `(3,-4)`, **not** `(2,-4)`.

This correction is essential: `2P-4C` would have signed beta zero and could not be the regenerated beta-two parent.

## 3. Reduced slopes

At common offset `s`, any character `aP+bC` with nonzero signed beta `B=2a+b` has reduced slope

\[
\boxed{
x_{a,b}(s)=x+s+\frac{b}{B}\delta.}
\tag{MC10}
\]

Hence

\[
\begin{aligned}
x_C(s)&=x+\delta+s,\\
x_D(s)&=x-\delta+s,\\
x_P(s)&=x+s,\\
x_E(s)&=x-\frac13\delta+s,\\
x_Q(s)&=x-\delta+s,\\
x_H(s)&=x-3\delta+s.
\end{aligned}
\tag{MC11}
\]

Choose the reset face

\[
\boxed{T=2\delta.}
\tag{MC12}
\]

Then

\[
x_H(T)=x-\delta,
\qquad
x_D(T)=x+\delta,
\]

and the beta-one sum `H+D` has reduced slope

\[
\boxed{x_{P_{\rm new}}(T)=x.}
\tag{MC13}
\]

Moreover the surviving child `D` itself has

\[
\boxed{x_D(T)=x+\delta,}
\tag{MC14}
\]

so at the level of signed beta and reduced slopes the pair

\[
(P_{\rm new},D)
\]

exactly reproduces the original input geometry `(P,C)`.

Thus the candidate is a true **two-channel kinematic reset**, not merely a parent reset.

## 4. Correct action bookkeeping

At offset `s`, put

\[
A_C=I_1(x+\delta+s),
\qquad
A_D=I_1(x-\delta+s).
\tag{MC15}
\]

The corrected chain gives

\[
\begin{aligned}
A_P^{\rm boost}&=A_C+A_D,\\
A_E&=A_P^{\rm boost}+A_D=A_C+2A_D,\\
A_Q&=A_E+A_C=2A_C+2A_D,\\
A_H&=A_Q+A_C=3A_C+2A_D.
\end{aligned}
\tag{MC16}
\]

This is exactly the coefficient pattern that was used in the original numerical solve.

Propagate `H` from `s` to `T=2delta`:

\[
A_H(T)
=A_H
+I_1(x-\delta)-I_1(x-3\delta+s).
\tag{MC17}
\]

At `T`, the old child `D` has natural action `I_1(x+delta)`. Therefore

\[
\boxed{
\begin{aligned}
\mathcal A_{\rm reset}(x,\delta,s)
={}&3I_1(x+\delta+s)
+2I_1(x-\delta+s)\\
&-I_1(x-3\delta+s)
+I_1(x-\delta)
+I_1(x+\delta).
\end{aligned}}
\tag{MC18}
\]

Exact parent-action renewal requires

\[
\boxed{
\mathcal A_{\rm reset}(x,\delta,s)=I_2(x).
}
\tag{MC19}
\]

For robustness, impose stationarity in the late generation offset:

\[
\boxed{
3I_1'(x+\delta+s)
+2I_1'(x-\delta+s)
-I_1'(x-3\delta+s)=0.
}
\tag{MC20}
\]

Together with (MC2), these are three scalar equations for `(x,delta,s)`.

## 5. Computer-assisted transverse solution

High-precision solution gives

\[
\boxed{x_*\approx0.7859855569295219140,}
\tag{MC21}
\]

\[
\boxed{\delta_*\approx0.07069967306663885738,}
\tag{MC22}
\]

\[
\boxed{s_*\approx0.14119460888766346057.}
\tag{MC23}
\]

The reset face is

\[
\boxed{T_*=2\delta_*\approx0.14139934613327771476,}
\tag{MC24}
\]

so

\[
\boxed{T_*-s_*\approx2.04737245614254\times10^{-4}>0.}
\tag{MC25}
\]

The Jacobian of `(MC2),(MC19),(MC20)` with respect to `(x,delta,s)` is numerically

\[
\begin{pmatrix}
-1.6518333885 & 1.3197888106 & 0\\
2.5185939835 & 1.3593380231 & 0\\
-11.7665926443 & -13.0050969799 & -11.7665926443
\end{pmatrix},
\]

with

\[
\boxed{\det\approx65.5330033379\ne0.}
\tag{MC26}
\]

and

\[
\boxed{
\partial_s^2(\mathcal A_{\rm reset}-I_2(x))
\approx-11.7665926443<0.
}
\tag{MC27}
\]

Thus the reduced solution is strongly transverse and `s_*` is a strict local maximum of the reset action.

The companion script `experiments/beta21_clock_reset_microcascade.py` reproduces these values. Publication use still requires interval certification.

## 6. Action headroom

At `s=s_*`, approximately

\[
I_1(x+\delta+s)\approx-6.74263\times10^{-6},
\]

\[
I_1(x-\delta+s)\approx-0.0310166810.
\]

Hence

\[
\begin{aligned}
A_P^{\rm boost}&\approx-0.0310234236,\\
A_E&\approx-0.0620401047,\\
A_Q&\approx-0.0620468473,\\
A_H&\approx-0.0620535899.
\end{aligned}
\tag{MC28}
\]

The corresponding natural envelope actions are more negative:

\[
\begin{aligned}
I_2(x+s)&\approx-0.342926,\\
I_3(x-\delta/3+s)&\approx-1.249061,\\
I_2(x-\delta+s)&\approx-0.197197,\\
I_1(x-3\delta+s)&\approx-0.123909.
\end{aligned}
\tag{MC29}
\]

Thus the promoted modes have positive reduced action headroom.

At the reset face the ledger gives

\[
\boxed{A_{P_{\rm new}}(T)=I_2(x)}
\tag{MC30}
\]

by construction.

## 7. Principal polarization audit

The exact source-frame audit is recorded separately in `beta21_microcascade_polarization_audit.md`. Its conclusion is that, after the genealogy correction above, **every mandatory quadratic edge has a nonzero growing-polarization coefficient**:

\[
P+C^*\to D,
\quad
C+D\to P,
\quad
P+D\to E,
\quad
E-C\to Q,
\quad
Q-C\to H,
\quad
H+D\to P_{\rm new}.
\tag{MC31}
\]

The signs are fixed by the source geometry, and no edge is a collinear self-interaction. A direct diagnostic at `u_*=100` gives substantial margins for all five late edges.

Therefore the candidate survives the mandatory principal-polarization test.

## 8. Remaining obligations

The frontier is now narrower:

1. separate the late chain into finitely many ordered micro-collars inside the very small interval `T_*-s_*`, and use the transverse `(x,delta,s)` freedom to preserve the exact action conditions;
2. redo the global lattice action filter with `P,E,Q,H,P_new` declared designated/promoted channels and exclude every competing non-designated mode;
3. prove exact finite-`u_*` persistence for the full ordered-collar system with the exact source primitive `mathcal E_{beta,u}`;
4. port the phase-adapted zero-residual `C^1` contraction to the resulting finite supercell;
5. only then return to infinite cell concatenation and global summability.

The candidate is therefore still pre-publication, but it has crossed the previous polarization barrier: the finite reset genealogy is now algebraically correct and every required principal quadratic coupling is nonzero.