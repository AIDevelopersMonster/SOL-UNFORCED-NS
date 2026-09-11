# Previous-relay whole-space mean/pressure tail is subcritical at the next physical scale

**Status:** PROVED CONDITIONAL SCALE-TRANSFER LEMMA UNDER A FIXED PHYSICAL SHRINK FACTOR. This note addresses only the inherited whole-space mean/pressure correction from an already-closed single relay. It does **not** prove that the designated child packet itself has the correct amplitude/phase normalization to seed the next relay.

The governing input from `coupled_phase_adapted_local_zero_residual_theorem.md` is the local mean size

\[
\boxed{
\|m_j\|\lesssim C_M S_j^C\varepsilon_j^{1-\kappa_s}
}
\tag{PT1}
\]

at relay scale `q_j`, with

\[
\varepsilon_j\asymp q_j^h,
\qquad
0<\kappa_s\ll1.
\tag{PT2}
\]

The source/base velocity scale is

\[
\boxed{
U_{\rm base}(q)\asymp q^{-A},
\qquad A=\frac12+h.
}
\tag{PT3}
\]

The intrinsic physical carrier is, by `chart_invariant_carrier_scale.md`,

\[
\boxed{
\Omega_{\rm phys}(q)\asymp q^{-(1+h)/2}.
}
\tag{PT4}
\]

## 1. Fix the physical scale map

Let the next relay be placed at

\[
\boxed{q_{j+1}=\vartheta q_j,\qquad 0<\vartheta<1,}
\tag{PT5}
\]

with `vartheta` independent of `j`. This is a genuine change of physical location/scale, not a change of dyadic chart label at the same point.

The next base amplitude is therefore larger by

\[
\frac{U_{\rm base}(q_{j+1})}{U_{\rm base}(q_j)}
=\vartheta^{-A}.
\tag{PT6}
\]

Meanwhile the next intrinsic carrier is larger by

\[
\frac{\Omega_{\rm phys}(q_{j+1})}{\Omega_{\rm phys}(q_j)}
=\vartheta^{-(1+h)/2}.
\tag{PT7}
\]

## 2. Convert the old mean correction to physical amplitude

The normalized local theorem measures `m_j` relative to the relay chart at `q_j`. Restoring the source velocity prefactor `q_j^{-A}`, the inherited physical mean correction obeys schematically

\[
\boxed{
|m_j^{\rm phys}|
\lesssim
q_j^{-A}S_j^C q_j^{h(1-\kappa_s)}.
}
\tag{PT8}
\]

Thus

\[
|m_j^{\rm phys}|
\lesssim
S_j^C q_j^{-1/2-h\kappa_s}.
\tag{PT9}
\]

This estimate uses only the local fixed-point size and the standard physical velocity normalization; the whole-space Leray projector introduces no extra inverse power because it is order zero in the fixed Sobolev realization.

## 3. Compare with the next relay base

Normalize the inherited old mean by the **next** relay base scale:

\[
\mathfrak r_{j\to j+1}
:=
\frac{|m_j^{\rm phys}|}{U_{\rm base}(q_{j+1})}.
\tag{PT10}
\]

Using (PT3), (PT5), and (PT9),

\[
\begin{aligned}
\mathfrak r_{j\to j+1}
&\lesssim
S_j^C
q_j^{-1/2-h\kappa_s}
(\vartheta q_j)^{1/2+h}\\
&=
S_j^C\vartheta^{1/2+h}
q_j^{h(1-\kappa_s)}.
\end{aligned}
\]

Hence

\[
\boxed{
\mathfrak r_{j\to j+1}
\lesssim
S_j^C\vartheta^{1/2+h}\varepsilon_j^{1-\kappa_s}
\to0.
}
\tag{PT11}
\]

So the previous-relay mean correction is asymptotically negligible compared with the base amplitude at the next smaller physical scale.

The crucial point is that the `epsilon^{1-kappa_s}` gain survives the change of physical normalization. There is no adverse pressure factor.

## 4. Derivatives measured on the next carrier scale

The action geometry depends not only on velocity amplitude but also on derivatives of inherited background fields. A derivative at the next relay carrier scale is naturally normalized by `Omega_phys(q_{j+1})`.

For the old mean tail itself, fixed-order whole-space Sobolev control gives local `W^{r,infty}` bounds for every fixed `r` below the chosen Sobolev order. Since the old mean is generated at frequencies no worse than the old relay/pressure scale, the conservative derivative comparison carries one old carrier factor per derivative. Therefore for fixed `r`,

\[
\frac{|\nabla^r m_j^{\rm phys}|}
{U_{\rm base}(q_{j+1})\Omega_{\rm phys}(q_{j+1})^r}
\lesssim
S_j^C\varepsilon_j^{1-\kappa_s}
\vartheta^{1/2+h}
\left(
\frac{\Omega_{\rm phys}(q_j)}
{\Omega_{\rm phys}(q_{j+1})}
\right)^r.
\tag{PT12}
\]

Using (PT7),

\[
\boxed{
\frac{|\nabla^r m_j^{\rm phys}|}
{U_{\rm base}(q_{j+1})\Omega_{\rm phys}(q_{j+1})^r}
\lesssim
S_j^C\varepsilon_j^{1-\kappa_s}
\vartheta^{1/2+h+r(1+h)/2}.
}
\tag{PT13}
\]

For every fixed `r`, this tends to zero with `j`.

Thus the inherited mean is subcritical not only in amplitude but in every fixed finite normalized derivative needed by the local relay theorem.

## 5. Pressure tail

The physical pressure-gradient correction is

\[
\nabla p_j=(I-\mathbb P)F_j.
\]

By `whole_space_leray_fixed_order_bound.md`,

\[
\boxed{
\|\nabla p_j\|_{H^m}
\le\|F_j\|_{H^m}.
}
\tag{PT14}
\]

Hence the pressure gradient inherits the same source-small factors as the mean forcing. In particular there is no loss capable of cancelling `epsilon_j^{1-kappa_s}`.

For the next relay, the pressure contribution enters only through its induced velocity/background correction and through fixed-order local derivatives. Those are controlled by the same argument as (PT11)--(PT13).

Therefore the noncompact nature of pressure is **not**, by itself, a cross-scale obstruction.

## 6. Sum over all earlier relays

Suppose

\[
q_j=q_0\vartheta^j.
\tag{PT15}
\]

Then

\[
\varepsilon_j^{1-\kappa_s}
=q_0^{h(1-\kappa_s)}
\vartheta^{jh(1-\kappa_s)}.
\tag{PT16}
\]

The source polynomial factor `S_j^C` grows only polynomially in the level. Consequently

\[
\boxed{
\sum_{j\ge0}S_j^C\varepsilon_j^{1-\kappa_s}<\infty.
}
\tag{PT17}
\]

More relevantly, at relay `n` the cumulative dimensionless inherited mean from all earlier relays is bounded by a convolution of a polynomial sequence with the geometric factor in (PT16). For a fixed scale ratio `vartheta`, the tail from relays sufficiently far behind is summable, while the finitely many nearest predecessors are individually `o(1)` at large `n` by (PT11).

Thus, after choosing a sufficiently large starting level,

\[
\boxed{
\|B_{<n}^{\rm inherited}\|_{C^r_{\rm normalized}(q_n)}=o(1)
}
\tag{PT18}
\]

for every fixed finite `r` required by the relay stability theorem.

This is exactly the form needed to preserve strict open conditions such as:

- the v0.8 action gap `delta_*>0`;
- the designated growing projection margin;
- finite critical-block transversality;
- the fixed coefficient cone conditions.

Because these conditions are strict, an `o(1)` perturbation preserves them from some level onward.

## 7. What is actually closed

Under the physical scale law `q_{j+1}=vartheta q_j` and the existing single-relay estimate,

\[
\boxed{
\text{previous mean/pressure tail}
\longrightarrow
\text{admissible small background at the next relay}
}
\tag{PT19}
\]

at every fixed derivative order.

Moreover the accumulated tails of all sufficiently old relays are summable in these normalized local seminorms.

So the whole-space pressure tail is **not the current scale-inheritance bottleneck**.

## 8. Remaining bottleneck: designated child transport

This lemma does not prove that the designated child generated near `q_j` becomes the correctly normalized parent/catalyst datum at `q_{j+1}`.

The intrinsic carrier changes by the factor

\[
\vartheta^{-(1+h)/2},
\]

while the source velocity normalization changes by

\[
\vartheta^{-A}.
\]

A genuine cascade therefore requires a theorem for the **transport/amplification law of the designated child between distinct physical q-levels**, including phase orientation, beta normalization, packet width, and amplitude.

That is now the sharp cross-scale frontier.