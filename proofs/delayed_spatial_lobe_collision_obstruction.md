# Obstruction to delayed `O(1)` collisions from separated Cauchy lobes

**Status:** MECHANISM OBSTRUCTION / REPAIR FILTER. This note rules out the naive repair proposed after `active_gate_temporal_control_cauchy_obstruction.md`: one cannot simply replace future temporal control bumps by spatially disjoint incoming homogeneous lobes and expect the common background transport to bring them into an order-one collision later.

At leading geometric-optics order all phases and envelopes are transported by the same material background flow. A smooth material flow is a diffeomorphism and preserves disjointness of advected supports. Viscosity destroys exact compact support, but on one source-native relay stage the diffusive leakage across a fixed fraction of the packet width is exponentially small in `1/(epsilon S)` and therefore cannot supply the order-one control columns used by the active-gate rank arguments.

The correct autonomous repair must encode its finite control degrees in an already-overlapping physical Cauchy state (for example an extended finite Fourier/amplitude state), not in delayed collisions of initially separated passive lobes.

## 1. Common material transport

The source eikonal equation for every oscillatory phase is

\[
D_t\Phi
=(\partial_t+U_B\cdot\nabla)\Phi=0
\]

up to the already-audited source-small correction terms.

Let

\[
\mathfrak F_{t,s}:x\mapsto X(t;s,x)
\]

be the material flow of the smooth realized background on one preterminal stage. For every fixed `t<1`, standard ODE uniqueness gives a diffeomorphism on the relevant compact source annulus.

Hence if two leading packet envelopes have disjoint supports at the physical Cauchy time `s`,

\[
K_1\cap K_2=\varnothing,
\]

their inviscid transported supports satisfy

\[
\boxed{
\mathfrak F_{t,s}(K_1)
\cap
\mathfrak F_{t,s}(K_2)
=\varnothing.
}
\tag{DL1}

Thus common advection alone cannot create a new collision between initially separated lobes.

## 2. Source-native stage duration

On the preferred `sigma` schedule,

\[
\Delta t_j
\asymp
q_j^{1+h}S_j.
\tag{DL2}

A fixed normalized source lobe has physical radial width

\[
w_{r,j}\asymp q_j^{1/2}
\tag{DL3}

and axial width

\[
w_{z,j}\asymp q_j^D,
\qquad D=\frac12-h.
\tag{DL4}

Consider two material tubes separated by a fixed fraction of the radial packet width,

\[
d_j\ge c_0q_j^{1/2}.
\tag{DL5}

## 3. Diffusive leakage is super-small

The heat kernel tail across distance `d_j` over time `Delta t_j` carries the Gaussian factor

\[
\exp\left(-\frac{c d_j^2}{\Delta t_j}\right).
\]

Using (DL2)--(DL5),

\[
\frac{d_j^2}{\Delta t_j}
\gtrsim
\frac{q_j}{q_j^{1+h}S_j}
=
\frac1{\varepsilon_jS_j},
\qquad
\varepsilon_j=q_j^h.
\]

Therefore

\[
\boxed{
\text{radial leakage}
\lesssim
\exp\left[-\frac{c}{\varepsilon_jS_j}\right].
}
\tag{DL6}

Since

\[
\varepsilon_jS_j\to0,
\]

this is smaller than every fixed power of `epsilon_j` and every inverse polynomial in `S_j`.

The axial width gives an even stronger ratio:

\[
\frac{q_j^{2D}}{q_j^{1+h}S_j}
=
\frac{q_j^{-3h}}{S_j},
\]

which also diverges strongly.

Thus viscosity cannot turn two support-separated incoming lobes into an order-one overlap during one late relay stage.

## 4. Homogeneous pulse survival does not change the support conclusion

`PrimaryODE.homogeneous_forward_bound` proves a genuine nonzero-harmonic homogeneous forward propagator from an arbitrary earlier slot time. In the growing branch the amplitude may survive/grow according to the prescribed envelope, with only a fixed multiplicative propagator loss on an `O(S)` interval.

This is important for Cauchy realizability of an **already present** packet, but it does not make disjoint material supports intersect. The homogeneous modal growth acts on the packet amplitude carried inside its tube; it does not supply a distinct group velocity that would move one lobe across another.

Hence homogeneous growing pulses solve the amplitude-survival problem but not delayed support collision.

## 5. Consequence for the proposed translated-lobe repair

The static geometric statement `translated_async_overlap.md` proves that spacetime slot rectangles can be placed so that different labels overlap at prescribed future supernodes. In the forced/source construction those rectangles are legitimate spacetime-localized source packets.

For an autonomous unforced Cauchy construction, however, a future spacetime rectangle must itself arise from the earlier physical field. Equations (DL1)--(DL6) show that initially separated passive lobes transported by the common background cannot create the required new order-one overlaps merely by waiting.

Therefore the implication

\[
\boxed{
\text{static future overlap geometry}
\not\Rightarrow
\text{Cauchy-realizable delayed collision}
}
\tag{DL7}

must be respected.

## 6. Correct next state object

The remaining finite control freedom must be encoded in degrees of freedom already present in the overlapping Cauchy state. A canonical choice is the finite vector of physical Fourier/promoted amplitudes itself.

For example, instead of enforcing

\[
(M,H,R_3)_{out}=0
\]

by future time-localized controls, treat

\[
(M,H,R_3)_{in}
\]

as genuine Cauchy coordinates and include their propagated values in the complete one-cell map.

More generally collect every source-promoted physical character required by the corrected cell into a finite state

\[
\boxed{
Y=(A_{K_1},\ldots,A_{K_N}).
}
\tag{DL8}

The exact cell defines a genuine Poincare map

\[
\boxed{
Y_{out}=\mathcal P_\ell(Y_{in})
}
\tag{DL9}

because these coordinates are restrictions/projections of the physical field on Cauchy sections, not future profile knobs.

The autonomous renewal problem becomes a finite invariant-graph/fixed-point problem for (DL9), coupled to the already-proved stable infinite complement.

## 7. New frontier

Construct the principal frozen map `P_0` on the smallest sufficient physical Fourier state and test:

1. whether its secondary block has an invariant graph over the two designated generator amplitudes `(P,C)`;
2. equivalently, whether `I-D_Y P_0` is invertible in the secondary coordinates at a candidate renewed state;
3. whether the resulting physical state remains inside the existing source-action/polarization admissible region;
4. whether the exact `C^1` correction perturbs this finite physical Poincare map by `o(1)`.

This route uses only genuine incoming Cauchy amplitudes and therefore removes the temporal-control autonomy defect if the finite fixed-point problem closes.

No autonomous reset theorem is claimed yet.
