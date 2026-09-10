# v0.8 large-`u_*` half-step family

**Status:** PROVED ASYMPTOTIC ENVELOPE/LATTICE THEOREM. This closes the model-level objection that the v0.7 tuned resonance occurred only near one moderate value `u_*≈49.36`. The theorem constructs exact finite-`u_*` relay resonances along a sequence `u_*=M^2 -> infinity` and proves a uniform principal action filter for the complete two-generator lattice, apart from the deliberately resonant catalyst/child modes.

This is **not** yet the localized Navier–Stokes relay theorem. Source-level curl/cutoff/transport/Leray estimates and exact zero-force correction remain separate obligations.

## 1. Half-step family

Let

\[
a_*:=2^{-2/3}.
\]

For an integer `M>=1`, set

\[
\delta_M:=\frac1{2M},
\qquad
u_M:=M^2.
\]

Use the integral-beta pair

\[
\boxed{\beta_1=2,\qquad \beta_2=1.}
\tag{H1}
\]

For a first-parent coordinate `x`, prescribe

\[
\boxed{
y=(1+\delta_M)x,
\qquad
x_c=(1-\delta_M)x.}
\tag{H2}
\]

Then

\[
2x-y=x_c,
\]

so the difference harmonic is exactly a unit-beta child.

Define the exact finite-`u` resonance function

\[
\boxed{
G_M(x)
:=
\mathcal E_{2,\nu_M}(x)
+
\mathcal E_{1,\nu_M}((1+\delta_M)x)
-
\mathcal E_{1,\nu_M}((1-\delta_M)x).
}
\tag{H3}

Here `mathcal E` is the exact envelope primitive from `beta_phase_stability.md`.

## 2. Existence of exact resonances with `u_* -> infinity`

Let the reduced companion be

\[
G_M^\infty(x)
:=
I_2(x)
+
I_1((1+\delta_M)x)
-
I_1((1-\delta_M)x).
\tag{H4}
\]

The source-envelope expansion gives, uniformly on every fixed compact interval in `x>0`,

\[
\mathcal E_{\beta,u}(x)=I_\beta(x)+O(u^{-2})
\]

for fixed `beta=1,2`. Since `nu_M=M^2`,

\[
\boxed{
G_M(x)-G_M^\infty(x)=O(M^{-4}).
}
\tag{H5}

At `x=a_*`,

\[
I_2(a_*)=0.
\]

Because `a_*<1` and `I_1'(x)=1/x-x^2>0` on `(0,1)`, the mean-value theorem gives, for all sufficiently large `M`,

\[
I_1((1+\delta_M)a_*)
-
I_1((1-\delta_M)a_*)
\ge \frac{c_0}{M}
\tag{H6}
\]

for some fixed `c_0>0`. Hence (H5) implies

\[
\boxed{G_M(a_*)>0}
\tag{H7}
\]

for large `M`.

Now fix any sufficiently small `eta>0` with `a_*+eta<1`. Since `a_*` is the unique maximum point of `I_2`,

\[
I_2(a_*+\eta)<0.
\]

The unit-beta difference in (H4) tends to zero as `M -> infinity`, and (H5) also tends to zero. Therefore

\[
\boxed{G_M(a_*+\eta)<0}
\tag{H8}
\]

for all sufficiently large `M`.

By continuity, for each sufficiently large `M` there is at least one

\[
\boxed{x_M\in(a_*,a_*+\eta)}
\tag{H9}
\]

such that

\[
\boxed{G_M(x_M)=0.}
\tag{H10}
\]

Because `eta` can be taken arbitrarily small in the preceding argument, one may select the roots so that

\[
\boxed{x_M\to a_*}
\tag{H11}
\]

as `M -> infinity`.

Set

\[
y_M=(1+\delta_M)x_M,
\qquad
x_{c,M}=(1-\delta_M)x_M.
\]

Then

\[
y_M\to a_*,
\qquad
x_{c,M}\to a_*.
\tag{H12}
\]

Since the exact beta-two turning point satisfies

\[
x_{2,\nu_M}<2^{-2/3}=a_*<x_M,
\]

the first parent is decaying. For large `M`, both `y_M` and `x_{c,M}` are below the unit-beta turning point `1`, so catalyst and child are growing.

Thus the exact finite-`u_*` family has

\[
\boxed{
\text{decaying beta-2 parent}
+\text{ growing beta-1 catalyst}
\longrightarrow
\text{ growing beta-1 child}
}
\tag{H13}
\]

with

\[
\boxed{u_*=\nu_M=M^2\to\infty.}
\tag{H14}

This removes the finite upper-range concern of v0.7: any fixed source cone threshold for `u_*` can be exceeded by taking `M` large enough.

## 3. Exact half-step lattice arithmetic

For a lattice index `(a,b) in Z^2`, let

\[
T:=2a+b.
\tag{H15}
\]

At the relay point the reduced radial coefficient is

\[
r_{a,b}=2ax_M+b y_M.
\]

Using (H2),

\[
r_{a,b}
=x_M\left(T+\frac{b}{2M}\right).
\]

Define

\[
\boxed{N:=(2M+1)T-2a.}
\tag{H16}
\]

Then

\[
\boxed{
r_{a,b}=\frac{x_M}{2M}N.}
\tag{H17}
\]

Conversely,

\[
a=\frac{(2M+1)T-N}{2},
\qquad
b=N-2MT,
\tag{H18}
\]

and admissibility is exactly

\[
N\equiv T\pmod2.
\]

For the unit-beta ladder `T=1`,

\[
N=2M+1-2a.
\]

Thus zero lies exactly halfway between the two neighboring integer ladder sites `a=M` and `a=M+1`:

\[
r_{M,1-2M}=\frac{x_M}{2M},
\qquad
r_{M+1,-1-2M}=-\frac{x_M}{2M}.
\tag{H19}
\]

The half-step small-divisor protection therefore survives while `M` grows.

## 4. Base actions

Define

\[
A_M:=\mathcal E_{2,\nu_M}(x_M),
\qquad
B_M:=\mathcal E_{1,\nu_M}(y_M).
\tag{H20}
\]

The exact resonance says

\[
\mathcal E_{1,\nu_M}(x_{c,M})=A_M+B_M.
\tag{H21}
\]

Because the first parent lies on the decaying side of its beta-two turning point,

\[
A_M<0.
\]

By (H11)–(H12) and the finite-`u` convergence,

\[
\boxed{A_M\to0,}
\tag{H22}
\]

while

\[
\boxed{B_M\to B_*:=I_1(a_*)<0.}
\tag{H23}
\]

Fix

\[
b_*:=-\frac12B_*>0.
\]

Then for all sufficiently large `M`,

\[
\boxed{B_M\le-b_*.}
\tag{H24}
\]

Any monomial in the two real parent packets with net lattice index `(a,b)` contains at least `|a|` factors of parent 1 and at least `|b|` factors of the catalyst. Since both actions are nonpositive, its largest possible source action is therefore

\[
\boxed{S_M(a,b)=|a|A_M+|b|B_M.}
\tag{H25}
\]

Additional cancelling factors only make the action more negative.

## 5. A universal lower bound for a growing natural action

Consider any lattice mode with

\[
\beta=|T|\ge1
\]

whose positive turning point exists. On its growing side the envelope is increasing from zero slope to the turning point, so

\[
\mathcal E_{\beta,\nu_M}(x)
\ge
\mathcal E_{\beta,\nu_M}(0).
\]

Writing `z=nu_M x_{beta,nu_M}`, the exact zero-slope formula has the form

\[
\mathcal E_{\beta,\nu_M}(0)
=-\operatorname{arsinh}z+\text{positive term}.
\]

For `beta>=1`, `0<=z<=nu_M`. Therefore

\[
\mathcal E_{\beta,\nu_M}(0)
>-\operatorname{arsinh}(\nu_M)
>-\log(3\nu_M).
\]

Since `nu_M=M^2`, every growing mode satisfies

\[
\boxed{
\mathcal E_{|T|,\nu_M}(x)>-\log(3M^2).
}
\tag{H26}

This logarithmic lower bound is the reason for choosing a half-step denominator `M` that grows while `u_*=M^2`: the action cost of a deep lattice cancellation is linear in `M`, whereas the deepest possible natural growing action is only logarithmic in `M`.

## 6. Global asymptotic action filter

For `T != 0`, define the effective positive reduced slope

\[
\boxed{
\xi_M(a,b)
:=\left|\frac{r_{a,b}}{T}\right|
=x_M\left|1+\frac{b}{2MT}\right|.
}
\tag{H27}

A mode is called **principal-growing** if its exact net beta-envelope rate at this point is positive. Equivalently,

\[
\xi_M(a,b)<x_{|T|,\nu_M}.
\]

The catalyst `(0,1)` and desired child `(1,-1)` are deliberately resonant and are excluded from the non-designated set, together with their conjugates.

### Theorem 6.1 — uniform action deficit

There exist constants

\[
M_0<\infty,
\qquad
\delta_*>0
\]

such that for every `M>=M_0` and every non-designated principal-growing lattice mode `(a,b)`,

\[
\boxed{
S_M(a,b)
-
\mathcal E_{|T|,\nu_M}(\xi_M(a,b))
\le-\delta_*.
}
\tag{H28}

In particular, after maximal homogeneous amplification from the relay point to that mode's natural peak, every non-designated growing harmonic retains a fixed exponential action deficit.

### Proof

Assume the conclusion is false. Then there are `M_j -> infinity` and non-designated growing indices `(a_j,b_j)` such that

\[
D_j
:=S_{M_j}(a_j,b_j)
-
\mathcal E_{|T_j|,\nu_{M_j}}(\xi_{M_j})
\to0
\]

from above or from arbitrarily small negative values.

By (H26), for large `j`,

\[
S_{M_j}(a_j,b_j)
> -\log(3M_j^2)-1.
\]

But (H24) and `A_M<=0` give

\[
S_M(a,b)\le-b_*|b|.
\]

Hence

\[
\boxed{|b_j|=O(\log M_j).}
\tag{H29}

Therefore

\[
\frac{b_j}{2M_jT_j}\to0
\]

uniformly whenever `T_j !=0`, because `|T_j|>=1`. By (H11),

\[
\boxed{\xi_{M_j}(a_j,b_j)\to a_*}
\tag{H30}

unless the sequence is eventually excluded by the growing condition first.

If `|T_j|>=3` along a subsequence, then

\[
x_{|T_j|,\nu_{M_j}}
<|T_j|^{-2/3}
\le3^{-2/3}
<a_*.
\]

This contradicts (H30) and the growing inequality for large `j`. Thus eventually

\[
|T_j|\le2.
\]

#### Case `|T_j|=2`

Parity forces `b_j` even. If `b_j=0`, the mode is the designated beta-two parent or its conjugate, which is in fact decaying and is not in the non-designated growing set.

If `b_j !=0`, then `|b_j|>=2`, so

\[
S_{M_j}(a_j,b_j)\le-2b_*.
\]

Meanwhile (H30), `nu_M -> infinity`, and `a_*=2^{-2/3}` imply

\[
\mathcal E_{2,\nu_{M_j}}(\xi_{M_j})\to I_2(a_*)=0.
\]

Hence `D_j<=-2b_*+o(1)`, contradicting `D_j->0`.

#### Case `|T_j|=1`

Now the natural action converges, by (H30), to

\[
I_1(a_*)=B_*.
\]

If `|b_j| -> infinity`, then (H24) gives `S_{M_j}->-infinity`, again impossible. Therefore, after passing to a subsequence, `(T_j,b_j)` is constant. Then `a_j=(T_j-b_j)/2` is also constant. Using (H22)–(H23),

\[
S_{M_j}(a_j,b_j)\to |b_j|B_*.
\]

Thus

\[
D_j\to(|b_j|-1)B_*.
\]

Because `B_*<0`, this can fail to be strictly negative only when `|b_j|<=1`. Parity for `|T|=1` forces `|b_j|=1`, and the four possibilities are exactly the catalyst/child pair and their conjugates:

\[
(0,1),\quad(1,-1),\quad(0,-1),\quad(-1,1).
\]

These were excluded as designated modes. Contradiction.

#### Case `T_j=0`

For completeness, a nonzero `T=0` mode has `b=-2a` and

\[
r=2a(x_M-y_M)\neq0.
\]

Its inviscid growing contribution vanishes exactly, so it is purely viscously damped and never belongs to the principal-growing set.

All cases contradict the assumed failure. Therefore some fixed `delta_*>0` and `M_0` exist, proving (H28). ∎

## 7. Exponential consequence at dyadic level

Let

\[
\Lambda_M:=\frac{\lambda_0L_s}{\nu_M}.
\]

For one fixed sufficiently large design integer `M`, both `M` and `u_*=M^2` are fixed constants as the dyadic level `ell -> infinity`, while

\[
L_s\asymp S_*=\ell^2.
\]

Hence Theorem 6.1 gives, for every non-designated growing lattice mode, the post-amplification factor

\[
\boxed{
\exp(-\delta_*\Lambda_M)
=
\exp\!\left(-c_M S_*\right),
\qquad c_M>0.
}
\tag{H31}

This is flat relative to every algebraic power of the dyadic scale.

The point is subtle but crucial: `M` is taken large **once**, to exceed any source admissibility threshold, and is then frozen. The exponential flatness is in the dyadic level, not in the design parameter `M`.

## 8. Research consequence

The v0.7 concern

\[
\text{“the tuned resonance may occur below the source-required }u_*\text{”}
\]

is removed at the principal model level.

There is an unbounded family of exact finite-`u_*` resonances with

\[
\boxed{u_*=M^2\to\infty}
\]

and a complete two-generator lattice action filter:

\[
\boxed{
\text{designated catalyst/child are resonant;}
\quad
T=0\text{ modes are viscously stable;}
\quad
\text{every other growing harmonic is action-subcritical.}
}
\tag{H32}

The next barrier is therefore no longer the off-window lattice or the size of `u_*`. It is the **source-localized preservation theorem**: prove that curl generation, slow cutoffs, transport defects, Leray/frame perturbations, and the stable/unstable correction inverses change only algebraic/polynomial prefactors and do not alter the action exponents used in (H25)–(H31).
