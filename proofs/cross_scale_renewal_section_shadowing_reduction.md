# Cross-scale renewal-section shadowing: reduction to one source transport estimate

**Status:** PROVED REDUCTION / ONE SOURCE-DERIVED TRANSPORT ESTIMATE REMAINS OPEN. The exact local two-collar renewal theorem now supplies, at every sufficiently high level and every admissible slow point, a compact nonzero renewal section. This note proves that no new nonlinear or amplitude fixed-point problem appears between levels. The remaining cross-scale issue is one uniform short-log-time estimate for the exact normalized physical propagator and transported phase covector along the trapped spine.

## 1. Exact renewal section

Let `P=K_slow` be the compact strict-cone profile set. From `exact_two_collar_renewal_state.md`, for every sufficiently high level `ell` and `p in P` there is an exact two-component normalized renewal state

\[
S_\ell(p)=(A_{2,\ell}(p),A_{1,\ell}(p))
\]

modulo the two independent torus phases, with

\[
\boxed{0<c_0\le |A_{j,\ell}(p)|\le C_0<\infty.}
\tag{SH1}
\]

Moreover `uniform_C1_two_collar_renewal_map.md` and the uniform implicit-function theorem give

\[
S_\ell(p)=S_0(p)+o(1)
\tag{SH2}
\]

uniformly in `p`, where `S_0(p)` is the continuous principal section determined by the coefficient field.

Thus the family of admissible exact incoming states is a compact section rather than one fixed vector.

## 2. Trapped spine and short logarithmic steps

Let `p(sigma)` denote the slow profile point along the exact trapped background characteristic from `profile_characteristic_trapped_spine.md`, with

\[
\sigma=-\log(1-t),
\qquad
q(\sigma)\asymp e^{-\sigma}.
\]

The profile ODE has a smooth bounded vector field on the compact trapping rectangle. Therefore there is a constant `L_P` such that

\[
\boxed{|p(\sigma+\delta)-p(\sigma)|\le L_P|\delta|}
\tag{SH3}
\]

for all sufficiently late times and every fixed small `delta`.

Choose a fixed shrink ratio

\[
\vartheta=e^{-\delta},\qquad 0<\delta\ll1.
\tag{SH4}
\]

Then consecutive relay profile points satisfy

\[
\boxed{|p_{j+1}-p_j|\le L_P\delta+o(1).}
\tag{SH5}
\]

The exact principal renewal section is continuous on `P`; on any finite atlas of the compact set it is uniformly continuous. Hence

\[
\boxed{|S_0(p_{j+1})-S_0(p_j)|\le \omega_S(L_P\delta)}
\tag{SH6}
\]

for a modulus of continuity `omega_S(r)->0`.

## 3. What the cross-scale propagator must do

Let

\[
\widehat T_j
:=\mathcal C_{q_{j+1}}T(q_{j+1},q_j)\mathcal C_{q_j}^{-1}
\]

be the exact normalized physical propagator for the designated two-channel state between relay cells, including the polarization transport but excluding the next local nonlinear renewal event.

The natural short-log-time target is

\[
\boxed{
\|\widehat T_j-I\|_{\mathcal L(E_{\rm des})}
\le C\delta+r_j,
\qquad r_j\to0,
}
\tag{SH7}
\]

on the finite designated packet block, uniformly along the trapped spine.

For the transported normalized phase covectors the analogous target is

\[
\boxed{
\|\widehat T_j^{\rm cov}-I\|
\le C\delta+r_j.
}
\tag{SH8}
\]

These are stronger and cleaner than the earlier abstract assertion that a fixed-ratio operator has some nonzero matrix coefficient. They express the fact that for `vartheta` sufficiently close to one, a bounded normalized generator has a near-identity evolution over logarithmic time `delta`.

## 4. Shadowing consequence of (SH7)--(SH8)

Assume (SH7)--(SH8). Starting with the exact renewal state `S_{ell_j}(p_j)`, transport it to the next level:

\[
\widetilde S_{j+1}:=\widehat T_jS_{\ell_j}(p_j).
\]

Then by (SH1), (SH7),

\[
\boxed{
|\widetilde S_{j+1}-S_{\ell_j}(p_j)|
\le C_1\delta+C_0r_j.
}
\tag{SH9}
\]

Together with (SH2) and (SH6),

\[
\boxed{
\operatorname{dist}
(\widetilde S_{j+1},S_{\ell_{j+1}}(p_{j+1}))
\le
C_1\delta+\omega_S(L_P\delta)+o_j(1).
}
\tag{SH10}
\]

Choose `delta` once and for all so small that the right side lies inside the fixed implicit-function neighborhood used to construct the exact next renewal state. Then, for all sufficiently high levels, the transported state is an admissible input for the next exact two-collar solve.

The two torus translation parameters reset its two phases exactly. The amplitude magnitudes need not be literally identical under free transport: the next local renewal solve is parameterized on an open neighborhood of the exact renewal section, and uniform transversality (`det=-2`) supplies the small correction back to the section.

Thus (SH7)--(SH8) imply a one-step shadowing map

\[
\boxed{
S_{\ell_j}(p_j)
\xrightarrow{\rm physical\ transport}
\text{neighborhood of }S_{\ell_{j+1}}(p_{j+1})
\xrightarrow{\rm exact\ renewal}
S_{\ell_{j+1}}(p_{j+1}).
}
\tag{SH11}

No product of scalar gains has to be bounded away from zero: each step is retracted to the uniformly transverse exact renewal section.

## 5. Physical amplitude and carrier scaling

The normalization `C_q` restores the intrinsic physical primary scale

\[
U_{\rm pkt}(q),\ \Omega_{\rm phys}(q)
\asymp q^{-(1+h)/2}.
\]

Therefore a normalized state remaining in the compact nonzero range (SH1) automatically has physical amplitude and carrier of size

\[
\boxed{q_j^{-(1+h)/2}}
\tag{SH12}
\]

at level `j`.

The cross-scale shadowing problem is therefore not an additional amplification problem. It is only preservation of the normalized compact renewal section.

## 6. Infinite geometric placement if one-step shadowing holds

With fixed `vartheta=e^{-delta}<1`, choose

\[
q_j=q_0\vartheta^j.
\tag{SH13}
\]

Then

\[
q_j\downarrow0
\]

geometrically. Since along the trapped spine `tau=q(1-eta^2)` with `1-eta^2` bounded above and below, the corresponding physical times satisfy

\[
1-t_j\asymp q_j.
\tag{SH14}
\]

Hence `t_juparrow1` and the available time gaps form a geometric sequence. The source pulse duration at level `q_j` is smaller than the scale gap by a positive `q_j^h` factor (up to powers of `S_*`), so sufficiently late cells can in principle be placed disjointly once the exact slow-box geometry is audited.

This observation does not yet constitute the global gluing theorem; it only shows that fixed-ratio shadowing is compatible with finite accumulation time.

## 7. Remaining source-derived estimate

The only new analytical statement required for one-step cross-scale shadowing is now:

### Short-log normalized transport theorem

For the exact normalized linearized Navier--Stokes/WKB system along the trapped spine, prove that its generator `A(sigma)` on the finite designated state/covector block is uniformly bounded on the compact trapping set,

\[
\boxed{\sup_{\sigma\ge\sigma_0}\|A(\sigma)\|\le C_A<\infty,}
\tag{SH15}
\]

with the source-small realization error tending to zero at high levels.

Then Duhamel/Gronwall gives immediately, for `0<=delta<=delta_0`,

\[
\boxed{
\|\widehat T(\sigma+\delta,\sigma)-I\|
\le e^{C_A\delta}-1+o(1)
\le C\delta+o(1),
}
\tag{SH16}
\]

and identically for the covector system. This is precisely (SH7)--(SH8).

The branch currently contains the normalized profile equations and bounded strict-cone coefficients needed to expect (SH15), but the exact cross-`q` generator has not yet been derived line-by-line from the pinned source variables. Therefore this note deliberately stops at the reduction and does not label cross-scale shadowing proved.

## 8. New frontier

The next research action is no longer to compute a mysterious fixed transfer coefficient. It is to derive the exact normalized generator along the trapped spine and prove the uniform bound (SH15). If that closes, one-step cross-scale renewal shadowing follows by the elementary near-identity estimate above.

After that the remaining global obligations are sparse-box placement, infinite tail summability, and recovery of one smooth finite-energy initial datum.