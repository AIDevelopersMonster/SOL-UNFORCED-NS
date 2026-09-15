# Turning-face zero-cost promoted-ladder obstruction

**Status:** PROVED PRINCIPAL / ACTION OBSTRUCTION TO ANY FINITE TERMINAL CONTROL BLOCK AT THE EXACT UNIT-BETA TURNING FACE. This corrects the previous `u=6` frontier note: the old catalyst `C` is not the only isolated terminal contaminant. If the surviving unit-beta channel `D` reaches its exact turning point with nonzero amplitude, then every additional `D` leaf costs zero action. A nonzero old `C` therefore seeds an infinite sum ladder

\[
W_k:=C+kD,\qquad k=0,1,2,\ldots,
\]

whose every fixed rung has the same action as `C`. The mandatory principal edges

\[
W_k+D\to W_{k+1}
\]

are strictly nonzero for every `k`. Hence, whenever `A_C>A_{P_{new}}`, infinitely many fixed lattice characters are promoted above the intended renewed parent. No finite-dimensional terminal Vandermonde/PBH block can remove this obstruction.

The correct redesign is to abandon the old passive-cleanup gauge `x+delta=1` and renew on a non-turning section with `A_D<0`, or else introduce a genuinely infinite-dimensional/support-separation mechanism. The next note develops the non-turning route.

## 1. Turning-face data

In the old finite-`u` cleanup gauge,

\[
x+\delta=1,
\qquad
T=2\delta.
\]

The surviving unit-beta channel has

\[
z_D(T)=x-\delta+T=x+\delta=1.
\]

Therefore

\[
\boxed{A_D(T)=\mathcal E_{1,u}(1)=0.}
\tag{ZL1}
\]

At the `u=6` active redesign point recorded in `beta21_u6_fourth_gate_strong_H_reset_handoff.md`,

\[
A_C(T)-A_{P_{new}}(T)
\approx 5.22782435\times10^{-4}>0.
\tag{ZL2}
\]

Thus old `C` is exponentially above the desired renewed beta-two parent on the source action scale.

## 2. Infinite one-`C` sum ladder

Define

\[
\boxed{W_k=C+kD.}
\tag{ZL3}
\]

Its signed beta is

\[
\beta_k=k+1>0.
\]

Since leaf actions add in absolute genealogy bookkeeping and `A_D(T)=0`,

\[
\boxed{
A_{W_k}(T)=A_C(T)+kA_D(T)=A_C(T)
}
\tag{ZL4}
\]

for every fixed `k>=0`.

Hence every rung has the same exponential action advantage over `P_new`:

\[
\boxed{
A_{W_k}(T)-A_{P_{new}}(T)
=A_C(T)-A_{P_{new}}(T)>0.
}
\tag{ZL5}
\]

This statement does not rely on whether `W_k` lies in its own natural growing window. For large `k` the homogeneous beta-`k+1` mode is strongly viscous, but the quadratic source generated inside the terminal overlap still enters at the leaf action (ZL4). A stable inverse may contribute algebraic/high-mode smoothing; it cannot change the fixed source action exponent.

## 3. Every mandatory edge is nonzero

At the turning face write

\[
z_D=1,
\qquad
z_C=1+a,
\qquad a>0.
\]

Then

\[
z_{W_k}
=\frac{z_C+kz_D}{k+1}
=1+\frac{a}{k+1}>1=z_D.
\tag{ZL6}
\]

Use actual source slopes

\[
s_1=u z_{W_k},\qquad s_2=u z_D,
\]

and beta weights

\[
b_1=k+1,\qquad b_2=1.
\]

For two growing reference polarizations

\[
g(s)=e_r-sK+c_0\sqrt{1+s^2}\,N,
\]

the principal sum vector is, up to the common oscillatory scalar,

\[
B_+
=(s_1-s_2)\bigl(b_1g(s_1)-b_2g(s_2)\bigr).
\tag{ZL7}
\]

The target beta is `b=b_1+b_2=k+2` and the target slope is

\[
s_t=\frac{b_1s_1+b_2s_2}{b_1+b_2}>0.
\]

Projecting to the child divergence-free plane and resolving into growing/decaying references gives the growing coefficient

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

Every factor in (ZL8) has a fixed strict sign:

- `s_1-s_2>0` by (ZL6);
- `b_1-b_2=k>=0`;
- `-b_1s_1+b_2s_2<0`, so the first numerator is strictly positive;
- `b_1 sqrt(1+s_1^2)-b_2 sqrt(1+s_2^2)>0` for `k>=1`; for `k=0` it is still positive because `s_1>s_2`.

Therefore

\[
\boxed{\kappa_k^+>0\qquad\text{for every }k\ge0.}
\tag{ZL9}
\]

Thus the entire ladder is physically populated at principal order; it is not a lattice-arithmetic overcount.

## 4. Why Duhamel order does not rescue a finite block

The `k`th rung first appears at finite nonlinear/Duhamel order and therefore carries a finite coefficient depending on the fixed terminal-collar width. For each **fixed** `k`, this coefficient is independent of the dyadic action scale `Lambda_ell`.

But (ZL5) produces the ratio

\[
\exp\{[A_C-A_{P_{new}}]\Lambda_\ell\}
\]

against the desired renewed parent. Since the bracket is fixed positive, this tends to infinity faster than any fixed algebraic source factor and overwhelms the finite Duhamel coefficient for every fixed `k`.

Hence there are infinitely many individually promoted fixed lattice characters at high levels.

## 5. Consequence

The old conclusion

\[
\text{`only terminal old-}C\text{ cancellation remains'}
\]

is too optimistic at an exact turning boundary. Even a perfect scalar cancellation attempt must act in a neighborhood in which `C` and a zero-action-cost `D` coexist, and that neighborhood carries the infinite promoted ladder above.

Therefore:

\[
\boxed{
\text{exact turning-face renewal}
+ A_D=0
+ A_C>A_{P_{new}}
\Longrightarrow
\text{no finite terminal critical block.}
}
\tag{ZL10}
\]

This does **not** rule out active beta-(2,1) renewal. It rules out the special turning-point gauge as the final handoff architecture.

## 6. Correct next route

The relay resonance itself does not require `x+delta=1`. If one drops that obsolete passive-cleanup condition and keeps only

\[
\mathcal E_{2,u}(x)
=\mathcal E_{1,u}(x+\delta)
+\mathcal E_{1,u}(x-\delta),
\]

then an exact phase-slope reset can be performed on a **non-turning** section where

\[
\mathcal E_{1,u}(x+\delta)<0.
\]

Every additional `D` leaf then costs a fixed negative action, restoring finiteness of every promoted lattice block. More generally the beta-preserving shear family `U_n` yields higher-order clock-resetting generator pairs. A concrete source-window-compatible candidate with passive disposal of old `C` is developed in the next theorem layer.
