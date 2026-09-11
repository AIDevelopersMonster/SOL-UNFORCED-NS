# v0.8 beta-two renewal from the catalyst--child feedback pair

**Status:** PROVED PRINCIPAL TWO-EVENT RENEWAL THEOREM FOR THE CURRENT v0.8 ENVELOPE MODEL; FINITE-`M` RESONANCE PERSISTS EXACTLY. This removes the purely algebraic missing-beta-two obstruction of `v08_state_renewal_obstruction.md`. It does **not** yet prove that infinitely many two-event cells can be embedded into one exact unforced solution.

The key observation is that the mode arithmetic already contains the missing channel:

\[
\boxed{e_2+(e_1-e_2)=e_1.}
\tag{BR1}
\]

Thus the old unit-beta catalyst and the newly generated unit-beta child can interact again, at a later pulse coordinate, to regenerate the beta-two parent. The first relay event and this renewal event occur at different locations along the same source pulse.

## 1. First event: current v0.8 difference relay

Freeze a sufficiently large design integer `M`, put

\[
u_*=M^2,
\qquad
\delta_M=\frac1{2M},
\qquad
\beta_1=2,
\qquad
\beta_2=1,
\tag{BR2}
\]

and let `x_M` be the exact finite-`u_*` resonance root from `integral_beta_v08_large_u_halfstep_family.md`. Define

\[
 y_M=(1+\delta_M)x_M,
\qquad
 x_{c,M}=(1-\delta_M)x_M.
\tag{BR3}
\]

Then

\[
2x_M-y_M=x_{c,M},
\qquad
y_M+x_{c,M}=2x_M.
\tag{BR4}
\]

The first event has the exact envelope identity

\[
\boxed{
\mathcal E_{2,M^2}(x_M)
+\mathcal E_{1,M^2}(y_M)
=\mathcal E_{1,M^2}(x_{c,M}).
}
\tag{BR5}
\]

It generates the unit-beta child `d=e_1-e_2` with a nonzero growing projection; `v08_designated_projection_nonvanishing.md` gives the current-design bound

\[
|A_+^{(1)}|\ge\frac{3M}{16}.
\tag{BR6}
\]

## 2. Common pulse drift preserves the feedback phase identity

Across one translated supernode the three reduced pulse coordinates drift with the same increment

\[
\theta=\frac{v-v_0}{L_s}.
\tag{BR7}
\]

Hence

\[
 x_1(\theta)=x_M+\theta,
\quad
 x_2(\theta)=y_M+\theta,
\quad
 x_c(\theta)=x_{c,M}+\theta.
\tag{BR8}
\]

By (BR4), for every `theta`,

\[
\boxed{
 x_2(\theta)+x_c(\theta)=2x_1(\theta).
}
\tag{BR9}
\]

This is exactly the phase-slope relation needed for the **sum** interaction of the two unit-beta modes `e_2` and `d` to regenerate the beta-two mode `e_1`.

Thus phase locking does not have to be retuned at the second event.

## 3. Renewal mismatch function

Define

\[
\boxed{
H_M(\theta)
:=
\mathcal E_{1,M^2}(y_M+\theta)
+\mathcal E_{1,M^2}(x_{c,M}+\theta)
-\mathcal E_{2,M^2}(x_M+\theta).
}
\tag{BR10}
\]

A zero of `H_M` is an exact envelope resonance for

\[
\boxed{
\text{unit-beta catalyst}
+\text{unit-beta child}
\longrightarrow
\text{beta-two regenerated parent}.
}
\tag{BR11}
\]

The half-step theorem gives

\[
x_M,y_M,x_{c,M}\to a_*:=2^{-2/3}.
\tag{BR12}
\]

The exact source envelope converges in `C^1` on compact positive `x`-intervals:

\[
\mathcal E_{\beta,M^2}(x)=I_\beta(x)+O(M^{-4}).
\tag{BR13}
\]

Therefore `H_M` converges uniformly on compact `theta` intervals to

\[
\boxed{
H_\infty(\theta)
=2I_1(a_*+\theta)-I_2(a_*+\theta).
}
\tag{BR14}
\]

Put `z=a_*+theta`. Using

\[
I_\beta(z)
=\log(z\beta^{2/3})-
\frac{\beta^2z^3}{3}+\frac13,
\]

we obtain the explicit formula

\[
\boxed{
H_\infty
=\log z-\frac23\log2+\frac23z^3+\frac13.
}
\tag{BR15}
\]

Its derivative is

\[
\boxed{
\frac{dH_\infty}{dz}=\frac1z+2z^2>0.
}
\tag{BR16}
\]

Hence `H_infty` has at most one positive zero.

Direct evaluation gives

\[
H_\infty(0.79)<-0.035,
\qquad
H_\infty(0.82)>0.040.
\tag{BR17}
\]

Therefore there is a unique

\[
\boxed{
z_*\in(0.79,0.82)}
\tag{BR18}
\]

with `H_infty(z_*)=0`. Numerically,

\[
\boxed{
z_*\approx0.8041741674845713.}
\tag{BR19}
\]

Since

\[
a_*=2^{-2/3}\approx0.6299605249474366,
\]

the limiting pulse separation is

\[
\boxed{
\theta_*:=z_*-a_*
\approx0.1742136425371347.
}
\tag{BR20}
\]

## 4. Exact finite-`M` renewal resonance

Choose the fixed bracket

\[
\theta\in[0.16,0.19].
\tag{BR21}
\]

By (BR17), the limiting mismatch has strict opposite signs at the two endpoints. Uniform convergence (BR13)--(BR14) therefore implies that, for all sufficiently large frozen `M`,

\[
H_M(0.16)<0,
\qquad
H_M(0.19)>0.
\tag{BR22}
\]

By continuity there exists

\[
\boxed{
\theta_M^{\rm ren}\in(0.16,0.19)
}
\tag{BR23}
\]

such that

\[
\boxed{
H_M(\theta_M^{\rm ren})=0.
}
\tag{BR24}
\]

Moreover every convergent subsequence of such roots must approach the unique limiting root, hence

\[
\boxed{
\theta_M^{\rm ren}\to\theta_*.
}
\tag{BR25}
\]

The second exact interaction window is separated from the first by

\[
\boxed{
\Delta v_M
=\theta_M^{\rm ren}L_s
\asymp0.174\,L_s.
}
\tag{BR26}
\]

Thus it is an `O(S_*)` separation inside the full source pulse, not a bounded-collar perturbation of the first event.

## 5. Growth/decay orientation at the renewal event

For the reduced limiting envelopes, the unit-beta turning point is

\[
z_{1,*}=1,
\]

while the beta-two turning point is

\[
z_{2,*}=2^{-2/3}=a_*\approx0.62996.
\]

At the renewal root

\[
z_*\approx0.80417,
\]

so

\[
\boxed{
z_*<1}
\tag{BR27}
\]

and both unit-beta inputs lie on their growing side, whereas

\[
\boxed{
z_*>2^{-2/3}}
\tag{BR28}
\]

puts the beta-two output on its decaying side.

The inequalities are strict. By finite-`M` convergence, for every sufficiently large frozen `M` the exact finite-`u_*` renewal event has the same orientation:

\[
\boxed{
\text{growing beta-1}
+\text{growing beta-1}
\longrightarrow
\text{decaying beta-2}.
}
\tag{BR29}
\]

This is exactly the complementary channel needed by the first relay, whose beta-two input is deliberately on the decaying side.

## 6. Principal polarization of the regenerated beta-two mode

Let the two unit-beta input slopes at the renewal event be

\[
s_2=u(y_M+\theta),
\qquad
s_c=u(x_{c,M}+\theta),
\tag{BR30}
\]

and set

\[
s_1=\frac{s_2+s_c}{2}=u(x_M+\theta).
\tag{BR31}
\]

Their normals sum to the beta-two target

\[
(s_2e_r+K)+(s_ce_r+K)
=2(s_1e_r+K).
\tag{BR32}
\]

Write the source growing polarization as

\[
g(s)=e_r-sK+c_0\sqrt{1+s^2}\,N,
\qquad c_0<0.
\]

Put

\[
\Delta:=s_2-s_c>0.
\tag{BR33}
\]

The principal sum-interaction vector is, up to the common scalar factor,

\[
B_{\rm ren}
=(g(s_2)\cdot k_c)g(s_c)
+(g(s_c)\cdot k_2)g(s_2).
\]

Since

\[
g(s_2)\cdot k_c=s_c-s_2=-\Delta,
\qquad
g(s_c)\cdot k_2=s_2-s_c=\Delta,
\]

we get

\[
B_{\rm ren}
=\Delta\bigl(g(s_2)-g(s_c)\bigr).
\tag{BR34}
\]

Let

\[
h_1=e_r-s_1K
\]

be the transverse basis vector for the beta-two target plane. Leray projection of `K` onto that plane is

\[
P_1K=-\frac{s_1}{1+s_1^2}h_1.
\tag{BR35}
\]

Therefore the `h_1` coefficient of the projected renewal source is

\[
\boxed{
H_{\rm pol}
=\frac{\Delta^2s_1}{1+s_1^2}>0.
}
\tag{BR36}
\]

The `N` coefficient has the same sign contribution to the target growing coordinate because

\[
\Delta>0,
\qquad
\sqrt{1+s_2^2}-\sqrt{1+s_c^2}>0,
\qquad c_0<0.
\]

Hence, if `A_+^{(2)}` is the regenerated beta-two growing-coordinate coefficient,

\[
\boxed{
A_+^{(2)}\ge\frac12H_{\rm pol}.
}
\tag{BR37}
\]

But the half-step geometry gives

\[
\Delta=u(y_M-x_{c,M})
=\frac{ux_M}{M}
=Mx_M,
\tag{BR38}
\]

independently of `theta`, while

\[
s_1=M^2(x_M+\theta).
\]

At the renewal event `x_M+theta` stays in a fixed compact subset of `(0,infty)`. For sufficiently large `M`, using `x_M>=1/2` and `x_M+theta>=1/2`,

\[
\frac{s_1^2}{1+s_1^2}\ge\frac12.
\]

Thus

\[
H_{\rm pol}
=\frac{M^2x_M^2s_1}{1+s_1^2}
=\frac{x_M^2}{x_M+\theta}
\frac{s_1^2}{1+s_1^2}
\ge c_{\rm ren}>0
\tag{BR39}
\]

for a fixed constant `c_ren` independent of the relay level and, after freezing a sufficiently large design `M`, independent of the physical scale.

Consequently

\[
\boxed{
A_+^{(2)}\ge c_{\rm ren}/2>0.
}
\tag{BR40}
\]

There is no principal polarization cancellation in the beta-two renewal channel.

## 7. Two-event state renewal cell

At principal envelope/polarization level we therefore have the finite cell

\[
\boxed{
(\beta=2,\beta=1)
\xrightarrow[\theta=0]{\rm difference}
\beta=1\ \text{child},
}
\tag{BR41}
\]

followed at the later exact resonance by

\[
\boxed{
(\beta=1\ \text{catalyst},\beta=1\ \text{child})
\xrightarrow[\theta=\theta_M^{\rm ren}]{\rm sum}
\beta=2\ \text{regenerated parent}.
}
\tag{BR42}
\]

Thus the current v0.8 lattice does contain both output beta channels needed for a repeated relay:

\[
\boxed{
\beta=1\ \text{surviving/generated child},
\qquad
\beta=2\ \text{regenerated parent}.
}
\tag{BR43}
\]

This removes the algebraic missing-channel obstruction identified in `v08_state_renewal_obstruction.md`.

## 8. What remains open

The result is not yet an infinite autonomous cascade theorem. The remaining obligations have become more precise:

1. extend the exact zero-residual local solve from one bounded interaction collar to the **two separated collars** `theta=0` and `theta=theta_M^ren` plus the transport interval between them;
2. prove that the beta-one child survives the second event with an order-one outgoing normalized amplitude while the beta-two regenerated mode has the exact normalization required by the next cell;
3. control all new non-designated harmonics produced by the second designated interaction in the existing weighted lattice norm;
4. transport the two-output state to the next physical `q` level and reset it into the admissible two-input geometry without an accumulating amplitude defect;
5. only then prove infinite packing/global summability.

The sharp next target is therefore a **two-collar exact zero-residual renewal theorem**, not a generic packing theorem.