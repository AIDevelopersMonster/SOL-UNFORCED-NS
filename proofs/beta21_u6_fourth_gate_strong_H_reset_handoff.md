# `u_*=6` fourth strong-`H` gate and final-renewal handoff

**Status:** PROVED WORKING-RESEARCH FOURTH-GATE REDUCTION / STRONG-`H` RENEWAL HANDOFF. At the supercritical working point `u_*=6`, the fourth active gate should prescribe the leading root-generated

\[
H=2D-C
\]

directly as the nonzero `X_2` coordinate of the already controllable `P/E + root` block. The weaker nominal `Q-C -> H` contribution is exponentially subleading on this normalization and belongs to the correction layer.

The retained promoted `Q` from gate three becomes strongly action-subcritical by the reset face and need not be included in the fourth leading finite block. The strong `H` then feeds the final edge

\[
H+D\to P_{new}=3D-C
\]

at the causal renewal time from `beta21_strong_H_active_renewal_bifurcation.md`.

The only remaining leading boundary-state obstruction identified in this note is the old catalyst `C`: at `u=6` it arrives at the reset face slightly **above** the renewed beta-two parent by the positive cleanup defect `+5.23e-4`. Thus a final terminal `C` cancellation/cleanup gate is required before claiming a clean renewed pair `(P_new,D)`.

No complete reset-cell theorem is claimed yet.

## 1. Entrance from the exact third gate

The `u=6` first-three-gate package gives the exact third exit state

\[
\boxed{
P=E=0,
\qquad
Q=Q_*\ne0,
\qquad
M=X_2=\cdots=X_{11}=0,
}
\tag{FH1}

with the physical unit-beta parents `C,D` retained.

Here the sufficient root chain is

\[
M,
D+M,
D+2M,
D+3M,
D+4M,
2D+4M,
2D+5M,
2D+6M,
3D+6M,
3D+7M,
3D+8M.
\]

The desired fourth output is

\[
\boxed{H:=2D-C=D+M=X_2.}
\tag{FH2}

## 2. Leading fourth-gate scale

The unavoidable root genealogy

\[
D-C\to M,
\qquad
D+M\to H
\]

has leading action

\[
\boxed{A_H^{root}=A_C+2A_D.}
\tag{FH3}

The old nominal path through the promoted third output,

\[
Q-C\to H,
\]

has action

\[
A_H^{Q-C}=3A_C+2A_D.
\]

Their difference is

\[
A_H^{root}-A_H^{Q-C}=-2A_C>0.
\]

At the concrete second/third section `A_C≈-0.06377`, so the root contribution is above the nominal `Q-C` path by roughly `0.1275` action units. The inequality persists on the short gate collars.

Thus `Q-C -> H` is exponentially small in the leading root normalization and does not alter the frozen fourth-gate rank.

## 3. Fourth-gate controllability is already contained in gate two

At `u=6`, the thirteen-state pair

\[
(P,E,M,X_2,\ldots,X_{11})
\]

is controllable by the second-gate PBH/root-chain theorem. Gate four uses the **same finite pair** but changes the target.

Instead of setting every root coordinate to zero, prescribe

\[
\boxed{
(P,E,M,X_2,X_3,\ldots,X_{11})_{out}
=(0,0,0,H_*,0,\ldots,0),
\qquad H_*\ne0.
}
\tag{FH4}

Since the frozen response matrix is already invertible, this change of target requires no new rank theorem.

The same action-normalized parameter-dependent contraction argument gives an exact `C^1` zero-residual gate for all sufficiently high levels. Hence gate four may be closed with thirteen smooth parent controls, leaving a prescribed nonzero strong root-scale `H` and cancelling the rest of the leading finite block.

## 4. The residual `Q` is harmless at the reset face

The gate-three promoted `Q=2D` begins at action

\[
A_Q^{prom}=2A_C+2A_D.
\]

At the concrete `u=6` second-section geometry this is approximately

\[
A_Q^{prom}\approx-0.1745844154.
\tag{FH5}

Propagate the beta-two `Q` packet homogeneously to the reset face `T=2delta`. Since its reduced slope is the same as `D`, it reaches slope `1` at `T`. Exact finite-`u=6` propagation gives

\[
\boxed{
A_Q(T)\approx-0.4840579285.
}
\tag{FH6}

The renewed beta-two parent target is

\[
\boxed{
A_{P_{new}}(T)
=\mathcal E_{2,6}(x)
=-0.1671552311\ldots.
}
\tag{FH7}

Therefore

\[
\boxed{
A_Q(T)-A_{P_{new}}(T)
\approx-0.3169026975<0.
}
\tag{FH8}

The old `Q` is exponentially below the renewed parent by a very large fixed action gap. It cannot contaminate the next cell at leading order.

## 5. Strong-`H` final renewal

The exact strong-`H` renewal equation at `u=6` has the causal root

\[
\boxed{
t_{renew}\approx0.336494599305936,}
\tag{FH9}

with

\[
\boxed{T-t_{renew}\approx9.0034\times10^{-4}>0.}
\tag{FH10}

At this event the leading fourth output `H` interacts with the surviving `D`:

\[
\boxed{H+D\to P_{new}=3D-C.}
\tag{FH11}

By construction of the scalar renewal root, homogeneous beta-two propagation from the generation section to the reset face gives exactly

\[
\boxed{
A_{P_{new}}(T)=\mathcal E_{2,6}(x).
}
\tag{FH12}

The surviving `D` reaches its unit-beta turning point at the same face,

\[
A_D(T)=0.
\]

Thus the desired renewed pair `(P_new,D)` is action-matched at the reset face.

## 6. The remaining old-`C` boundary problem

At `u=6`, the old catalyst reaches the reset face with action

\[
\boxed{
A_C(T)
=\mathcal E_{1,6}(1+2\delta)
\approx-0.1666324486.
}
\tag{FH13}

Comparing with (FH7),

\[
\boxed{
A_C(T)-A_{P_{new}}(T)
\approx+5.22782435\times10^{-4}>0.
}
\tag{FH14}

This is exactly the positive spent-catalyst cleanup defect at `u=6`.

Therefore old `C` is not action-discardable: on the source action scale it is exponentially larger than `P_new` by the fixed amount (FH14), although the numerical action difference is small.

This is now the **sole identified leading boundary-state contamination** in the strong-`H` active-renewal design. `Q` is strongly subcritical, the cancelled root family is zero at the fourth gate exit, and all uncontrolled finite modes retain negative action gaps.

## 7. Why terminal `C` cancellation is plausible but not yet proved

Unlike the previously rejected direct homogeneous cancellation of supercritical sidebands, the old `C` itself lies on its **own natural unit-beta envelope**. Therefore a source-native homogeneous packet in the same `C` character can have the correct action scale with only an `O(1)` normalized amplitude; no forbidden factor `exp(+cS_*)` is required.

This removes the earlier action-mismatch obstruction.

However a late `C` cancellation pulse can still interact with the surviving `D` and the newly generated `P_new` while it is being inserted. Those products occur at leading or near-leading action and must be included in a finite terminal cleanup block. One cannot simply subtract `C` by hand.

Thus the final local frontier is

\[
\boxed{
\textbf{terminal source-native cancellation of old }C
\textbf{ with finite sideband control.}
}
\tag{FH15}

If that gate closes while preserving `(P_new,D)` and cancelling every newly generated critical sideband, the `u=6` beta-(2,1) active reset cell will be locally complete.
