# Turning-face zero-cost promoted-ladder obstruction

**Status:** PROVED PRINCIPAL / ACTION OBSTRUCTION TO ANY FINITE TERMINAL CONTROL BLOCK AT THE EXACT UNIT-BETA TURNING FACE. **Correction:** an earlier version misstated the general non-turning first-relay resonance in the final route paragraph. The correct resonance is

\[
\mathcal E_{2,u}(x)
+\mathcal E_{1,u}(x+\delta)
-\mathcal E_{1,u}(x-\delta)=0.
\]

The turning-face obstruction itself is unchanged because the old gauge has `x+delta=1` and hence `E_{1,u}(x+delta)=0`.

## 1. Turning-face data

In the old finite-`u` cleanup gauge,

\[
x+\delta=1,
\qquad
T=2\delta.
\]

The surviving unit-beta channel has

\[
z_D(T)=x-\delta+T=x+\delta=1,
\]

so

\[
\boxed{A_D(T)=\mathcal E_{1,u}(1)=0.}
\tag{ZL1}
\]

At the `u=6` active redesign point recorded in `beta21_u6_fourth_gate_strong_H_reset_handoff.md`,

\[
A_C(T)-A_{P_{new}}(T)
\approx5.22782435\times10^{-4}>0.
\tag{ZL2}
\]

Thus old `C` is exponentially above the desired renewed beta-two parent.

## 2. Infinite one-`C` sum ladder

Define

\[
\boxed{W_k=C+kD,\qquad k=0,1,2,\ldots.}
\tag{ZL3}
\]

Its signed beta is `k+1`. Since `A_D(T)=0`, absolute-leaf action bookkeeping gives

\[
\boxed{A_{W_k}(T)=A_C(T)}
\tag{ZL4}
\]

for every fixed `k`. Hence

\[
\boxed{
A_{W_k}(T)-A_{P_{new}}(T)
=A_C(T)-A_{P_{new}}(T)>0.
}
\tag{ZL5}
\]

Large-beta homogeneous stability supplies algebraic/high-mode smoothing but does not change this fixed source action exponent.

## 3. Every mandatory ladder edge is nonzero

At the turning face write

\[
z_D=1,
\qquad z_C=1+a,
\qquad a>0.
\]

Then

\[
z_{W_k}
=1+\frac{a}{k+1}>1=z_D.
\tag{ZL6}
\]

Use actual source slopes

\[
s_1=uz_{W_k},\qquad s_2=uz_D
\]

and beta weights

\[
b_1=k+1,\qquad b_2=1.
\]

For growing reference polarization

\[
g(s)=e_r-sK+c_0\sqrt{1+s^2}\,N,
\]

the principal sum vector for `W_k+D -> W_{k+1}` is proportional to

\[
B_+
=(s_1-s_2)\bigl(b_1g(s_1)-b_2g(s_2)\bigr).
\tag{ZL7}
\]

The child slope is

\[
s_t=\frac{b_1s_1+b_2s_2}{b_1+b_2}.
\]

Resolving the Leray projection into the child growing reference gives

\[
\kappa_k^+
=\frac{s_1-s_2}{2}
\left[
\frac{(b_1-b_2)-s_t(-b_1s_1+b_2s_2)}{1+s_t^2}
+
\frac{b_1\sqrt{1+s_1^2}-b_2\sqrt{1+s_2^2}}
{\sqrt{1+s_t^2}}
\right].
\tag{ZL8}
\]

Here `s_1-s_2>0`; the first bracketed numerator is strictly positive; and the second is strictly positive. Therefore

\[
\boxed{\kappa_k^+>0\qquad(k\ge0).}
\tag{ZL9}
\]

Thus every fixed rung is genuinely populated at principal order.

## 4. Finite Duhamel order does not rescue a finite block

For each fixed `k`, the `k`th rung carries only finite algebraic/Duhamel factors independent of the dyadic action scale. The ratio to the desired parent contains

\[
\exp\{[A_C-A_{P_{new}}]\Lambda_\ell\},
\]

which diverges because the bracket is fixed positive. Hence infinitely many individually fixed characters are promoted at high levels.

Therefore

\[
\boxed{
\text{exact turning-face renewal}
+A_D=0
+A_C>A_{P_{new}}
\Longrightarrow
\text{no finite terminal critical block.}
}
\tag{ZL10}
\]

## 5. Correct non-turning frontier

The relay resonance does **not** require `x+delta=1`. Its correct finite-`u` form is

\[
\boxed{
\mathcal E_{2,u}(x)
+\mathcal E_{1,u}(x+\delta)
=\mathcal E_{1,u}(x-\delta).
}
\tag{ZL11}
\]

At a non-turning renewal section with

\[
\mathcal E_{1,u}(x+\delta)<0,
\]

every additional surviving unit-beta leaf costs a fixed negative action, so the zero-cost argument above disappears and the promoted terminal block is finite.

The beta-preserving shear family may still be used to formulate higher-order target characters, but every non-turning numerical candidate must be solved using (ZL11). The previously recorded candidate values obtained from the incorrect plus-plus equation are retracted in `beta21_higher_order_clock_reset_family.md`.
