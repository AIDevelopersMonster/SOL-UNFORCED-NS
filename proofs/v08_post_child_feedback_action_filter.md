# v0.8 post-child feedback action filter on the full renewal interval

**Status:** PROVED PRINCIPAL/EXACT-ENVELOPE ACTION THEOREM. This closes a gap in the two-event renewal picture: after the first difference event the surviving unit-beta catalyst and unit-beta child generate a new lattice, and the old first-event action theorem did not by itself prove that this enlarged genealogy remains subcritical all the way to the beta-two renewal point.

The theorem below proves that every non-designated principal-growing descendant of the surviving pair retains a fixed negative action margin on the whole interval from the first event to the renewal event. The only deliberately extracted new channel is the beta-two sum response. Stable/decaying descendants are handled by the forward pulse inverse and are not required to satisfy a growing-action inequality.

## 1. Surviving pair after the first event

Freeze the v0.8 design

\[
u_*=M^2,\qquad \delta_M=\frac1{2M},\qquad
x_M\to a_*:=2^{-2/3},
\]

and write

\[
y_M=(1+\delta_M)x_M,\qquad
c_M=(1-\delta_M)x_M.
\tag{FA1}
\]

After the first difference event the relevant surviving nonzero waves are

\[
B=e_2\quad(\beta=1,\ x=y_M+\theta),
\]

and

\[
C=e_1-e_2\quad(\beta=1,\ x=c_M+\theta).
\]

Here

\[
0\le\theta\le\theta_M^{\rm ren},
\qquad
\theta_M^{\rm ren}\to\theta_*\approx0.1742136425
\tag{FA2}
\]

is the exact renewal interval from `v08_beta2_feedback_renewal.md`.

For integers `(m,n)`, a genealogy containing `m` signed copies of `C` and `n` signed copies of `B` has total beta integer

\[
\boxed{T=m+n}
\tag{FA3}
\]

and signed radial coefficient

\[
\boxed{
r_{m,n}(\theta)
=m(c_M+\theta)+n(y_M+\theta)
=T(x_M+\theta)+\frac{x_M}{2M}(n-m).
}
\tag{FA4}
\]

For `T!=0` put

\[
\boxed{
\xi_{m,n}(\theta)=\left|\frac{r_{m,n}(\theta)}T\right|.
}
\tag{FA5}
\]

The exact source action carried by the two homogeneous unit-beta inputs is

\[
\boxed{
S_{m,n}(\theta)
=|m|\mathcal E_{1,M^2}(c_M+\theta)
+|n|\mathcal E_{1,M^2}(y_M+\theta).
}
\tag{FA6}
\]

The target homogeneous action is

\[
\mathcal E_{|T|,M^2}(\xi_{m,n}(\theta)).
\]

## 2. Uniform negative action of each surviving generator

The whole interval (FA2) stays a fixed positive distance below the unit-beta turning point. Indeed

\[
y_M+\theta_M^{\rm ren},\ c_M+\theta_M^{\rm ren}\to z_*\approx0.8041741675<1.
\]

By the `C^1` convergence

\[
\mathcal E_{1,M^2}(x)=I_1(x)+O(M^{-4})
\]

on compact positive intervals, there are `M_0` and a fixed number `b_fb>0` such that for every `M>=M_0`, every `theta` in (FA2),

\[
\boxed{
\mathcal E_{1,M^2}(c_M+\theta)\le-b_{\rm fb},
\qquad
\mathcal E_{1,M^2}(y_M+\theta)\le-b_{\rm fb}.
}
\tag{FA7}
\]

Consequently

\[
\boxed{
S_{m,n}(\theta)\le-b_{\rm fb}(|m|+|n|).
}
\tag{FA8}
\]

## 3. Exact zero-beta descendants are viscous

If `T=0`, then `n=-m`, and (FA4) becomes

\[
r_{m,-m}=m(c_M-y_M)=-\frac{mx_M}{M}.
\tag{FA9}
\]

For every nonzero genealogy this is nonzero. Thus the tangential beta cancels but the phase normal does not: the mode is purely viscously damped at principal level. It is not a principal-growing obstruction.

## 4. Main theorem

Exclude the two surviving designated unit-beta modes and their conjugates,

\[
(m,n)=(1,0),(0,1),(-1,0),(0,-1).
\tag{FA10}
\]

Then there exist constants

\[
M_1<\infty,\qquad \delta_{\rm fb}>0
\]

such that for every `M>=M_1`, every `theta in [0,theta_M^ren]`, and every non-designated **principal-growing** mode with `T!=0`,

\[
\boxed{
S_{m,n}(\theta)
-\mathcal E_{|T|,M^2}(\xi_{m,n}(\theta))
\le-\delta_{\rm fb}.
}
\tag{FA11}
\]

### Proof

Assume otherwise. Then there are `M_j->infinity`, points `theta_j` in the renewal intervals, and non-designated principal-growing pairs `(m_j,n_j)` for which the left side of (FA11) tends to zero from above or from arbitrarily small negative values.

Let

\[
N_j:=|m_j|+|n_j|.
\]

For every exact principal-growing beta-envelope, the lower bound already proved in the v0.8 half-step theorem gives

\[
\mathcal E_{|T_j|,M_j^2}(\xi_j)>-\log(3M_j^2).
\tag{FA12}
\]

Together with (FA8), near-failure of (FA11) forces

\[
\boxed{N_j=O(\log M_j).}
\tag{FA13}
\]

After a subsequence, `theta_j->theta_infty in [0,theta_*]`. Since `|T_j|<=N_j` and every nonzero integer `T_j` has `|T_j|>=1`, (FA4) and (FA13) imply, whenever `|T_j|` stays fixed,

\[
\frac{r_{m_j,n_j}(\theta_j)}{T_j}
=x_{M_j}+\theta_j
+O\left(\frac{\log M_j}{M_j}\right)
\to z_\infty:=a_*+\theta_\infty.
\tag{FA14}
\]

If `|T_j|->infinity`, the exact growing condition implies the turning point tends to zero, while (FA14) is replaced by the even easier estimate that a growing mode must have a large cancellation in (FA4). Such a cancellation requires `N_j` comparable to `M_j|T_j|`, contradicting (FA13). Hence, after another subsequence, `|T_j|=T_0` is fixed.

If `T_0>=3`, the limiting turning point obeys

\[
T_0^{-2/3}<2^{-2/3}=a_*\le z_\infty,
\]

contradicting the principal-growing condition.

If `T_0=2` and `theta_infty>0`, the same contradiction holds because `z_infty>a_*`, whereas the beta-two turning point tends to `a_*`. If `T_0=2` and `theta_infty=0`, the target action tends to `I_2(a_*)=0`, while `N_j>=2` and (FA7) give a strictly negative source action. Thus the deficit cannot tend to zero.

It remains to consider `T_0=1`. Parity gives

\[
N_j\equiv1\pmod2.
\]

The excluded designated modes are exactly the cases `N_j=1`. Hence every non-designated sequence has eventually

\[
N_j\ge3.
\]

Passing to a subsequence with fixed `(m,n)` if `N_j` is bounded, or using (FA8) if it is unbounded, the only possible near-zero case is bounded `N_j`. Then exact-envelope convergence and (FA14) give

\[
S_{m,n}-\mathcal E_{1,M_j^2}(\xi)
\to(N_j-1)I_1(z_\infty).
\tag{FA15}
\]

But `z_infty<=z_*<1`, so

\[
I_1(z_\infty)\le I_1(z_*)<0,
\]

and `N_j-1>=2`. The limit in (FA15) is therefore uniformly negative, contradiction.

All cases contradict failure of a fixed gap. This proves (FA11). `square`

## 5. Consequence for the long feedback interval

The long interval of length

\[
\theta_M^{\rm ren}L_s\asymp S_*
\]

does **not** create a new family of uncontrolled growing harmonics after the child becomes an independent designated wave.

Every non-designated mode belongs to one of two classes:

1. principal-growing, but with the fixed action deficit (FA11), hence carrying `exp(-c_M S_*)` after maximal homogeneous amplification;
2. principal-stable/decaying, hence eligible for the source forward pulse inverse and the quadratic high-mode stable inverse.

The beta-two channel `B+C=e_1` is deliberately removed from this remainder analysis and treated as the renewal output in `v08_beta2_feedback_renewal.md`.

Thus the new child genealogy does not invalidate the v0.8 action architecture on the feedback segment.