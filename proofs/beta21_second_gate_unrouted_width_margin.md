# Quantitative width margin for the unrouted second active gate

**Status:** COMPUTER-ASSISTED EXACT-ENVELOPE WIDTH CERTIFICATE / FINITE CONTINUITY REDUCTION. At the finite-`u_*=4` second-overlap working point, the six positive-defect unwanted characters from `beta21_second_gate_unrouted_full_critical_audit.md` remain the only action-supercritical naturally critical outputs on the forward normalized collar

\[
\boxed{0\le t\le5\times10^{-4}.}
\]

The weakest controlled positive mode `10D-7C` remains strictly positive throughout this collar, while the closest uncontrolled mode `8D-6C` retains a substantial negative margin. No omitted lattice site can enter the natural critical window on this collar.

A publication-final certificate should replace sampled high-precision derivative suprema by interval arithmetic; the analytic reduction is finite and explicit.

## 1. Drifting parents

At the second section put

\[
z_C(0)=1.218506242359214\ldots,
\qquad
z_D(0)=0.867407030620355\ldots.
\tag{UW1}
\]

Over a forward offset `t`,

\[
z_C(t)=z_C(0)+t,
\qquad
z_D(t)=z_D(0)+t.
\tag{UW2}
\]

For

\[
K_{m,n}=mD+nC,
\qquad B=m+n>0,
\]

the reduced slope is

\[
\boxed{
\xi_{B,m}(t)
=\frac{mz_D(t)+(B-m)z_C(t)}B
=\xi_{B,m}(0)+t.
}
\tag{UW3}

The maximal absolute-leaf action is

\[
\boxed{
S_{B,m}(t)
=|m|\mathcal E_{1,4}(z_D(t))
+|B-m|\mathcal E_{1,4}(z_C(t)).
}
\tag{UW4}

Define

\[
\boxed{
\Delta_{B,m}(t)
=S_{B,m}(t)-\mathcal E_{B,4}(|\xi_{B,m}(t)|).
}
\tag{UW5}

## 2. Exact derivative formula

Use

\[
\partial_x\mathcal E_{\beta,4}(x)
=
\frac4{\sqrt{1+16x^2}}
-
\frac{\beta^2}{17^{3/2}}
(4+64x^2).
\tag{UW6}

Away from a zero of `xi`,

\[
\boxed{
\begin{aligned}
\Delta'_{B,m}(t)
={}&|m|\mathcal E'_{1,4}(z_D(t))
+|B-m|\mathcal E'_{1,4}(z_C(t))\\
&-\operatorname{sgn}(\xi_{B,m}(t))
\mathcal E'_{B,4}(|\xi_{B,m}(t)|).
\end{aligned}}
\tag{UW7}

Thus every width claim reduces to finitely many explicit one-variable inequalities.

## 3. Weakest controlled positive mode

The smallest positive center defect is the beta-three character

\[
\boxed{10D-7C}
\tag{UW8}
\]

with

\[
\Delta(0)
=0.00278376364225984025\ldots.
\tag{UW9}
\]

High-precision exact-envelope evaluation gives

\[
\boxed{
\Delta(5\times10^{-4})
\approx0.000768375003>0.
}
\tag{UW10}

Thus this mode remains in the controlled supercritical set throughout the chosen collar.

It crosses zero only later; no argument depends on continuing the gate beyond the certified width.

## 4. Closest uncontrolled mode

The closest negative center defect is

\[
\boxed{8D-6C}
\tag{UW11}
\]

with signed beta two and

\[
\Delta(0)
=-0.01706970932492087079\ldots.
\tag{UW12}

At the right edge of the chosen collar,

\[
\boxed{
\Delta(5\times10^{-4})
\approx-0.0160176311612<0.
}
\tag{UW13}

A direct finite derivative sweep over the complete 50-mode center-critical set gives a conservative bound below `3.71` for the largest absolute derivative on this interval. The mean-value estimate is therefore consistent with the explicit endpoint margins.

Every other uncontrolled center-critical mode remains more negative.

## 5. No omitted mode enters the critical set

For a mode outside the center naturally-critical set to enter under forward drift, it must start below the negative turning boundary and satisfy

\[
\xi_{B,m}(0)+t=-x_{B,4}.
\]

The nearest omitted lattice site is

\[
(B,m,n)=(7,27,-20),
\]

whose crossing time is

\[
\boxed{
t_{cross}\approx0.00593684811.}
\tag{UW14}

The next crossing is later than `0.0075`.

Therefore

\[
5\times10^{-4}
<\frac1{10}t_{cross},
\]

and no omitted positive-beta lattice site enters the naturally growing/neutral window on the certified gate collar.

All `|B|>=9` modes remain uniformly principal-decaying because no real beta turning point exists at `u=4`.

## 6. Uniform margin

A conservative working certificate is therefore

\[
\boxed{
\begin{aligned}
&\Delta_{danger}(t)>7\times10^{-4}
&&\text{for the weakest controlled dangerous mode},\\
&\Delta_{uncontrolled}(t)<-1.5\times10^{-2}
&&\text{for every uncontrolled center-critical mode},
\end{aligned}}
\tag{UW15}

for

\[
0\le t\le5\times10^{-4}.
\]

The numerical constants are deliberately rounded inward.

## 7. Consequence

The unrouted second-gate finite control theorem has a genuine nonzero action-safe width. Combining this width with the short-collar full-symbol rank threshold, define

\[
\boxed{
w_2
=\min(5\times10^{-4},w_{rank,12})>0.}
\tag{UW16}

On `w_2`:

1. the twelve-state leading response remains full rank;
2. all six dangerous modes stay inside the controlled block;
3. every uncontrolled naturally critical mode has a fixed negative action gap;
4. no new lattice site enters the critical set.

This is the width input required for the exact twelve-parameter `C^1` transfer.
