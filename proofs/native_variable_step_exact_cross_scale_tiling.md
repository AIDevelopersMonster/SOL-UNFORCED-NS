# Native variable-step exact cross-scale tiling

**Status:** PROVED GLOBAL SCALE-SCHEDULING / EXACT-BRIDGE REDUCTION THEOREM, SUBJECT TO THE ALREADY-PROVED `O(S_*)` FINITE-CIRCUIT ZERO-RESIDUAL ESTIMATES. This theorem removes the unsupported fixed-ratio exact inter-scale bridge.

The previous fixed-ratio transfer theorem is useful for linear normalized shadowing, but a fixed ratio `q_{j+1}=vartheta q_j` produces a source-fast transport interval much longer than the `O(S_*)` exact-correction segments that have actually been proved. The correct autonomous schedule is instead to let the relative q-step shrink with the source parameter:

\[
\boxed{
q_{j+1}
=q_j\bigl(1-\Lambda\varepsilon_jS_j\bigr),
\qquad
\varepsilon_j=q_j^h.
}
\tag{NV1}

Then one complete corrected cell, including its cross-scale handoff to the next cell, has only `O(S_j)` length in the source fast coordinate. Thus the existing polynomial-loss exact zero-residual machinery applies without a new long-time inverse theorem.

## 1. Source fast/physical time relation

The source chart identity from `ActualPhaseDefect.slot_coordinates_temporal` gives the physical temporal direction in phase coordinates as

\[
e_V-\varepsilon e_T.
\]

Equivalently, up to the fixed sign convention,

\[
\boxed{dT=\varepsilon\,dV,}
\tag{NV2}

where `T` is the normalized physical time coordinate at fixed physical scale and `V` is the fast pulse coordinate.

The native pulse/slot length is polynomial:

\[
L_j\asymp S_j,
\]

with `S(n)=n^2` on the source dyadic hierarchy.

Therefore a physical normalized time displacement

\[
\Delta T=O(\varepsilon_jS_j)
\]

corresponds to only

\[
\boxed{\Delta V=O(S_j).}
\tag{NV3}

## 2. Why a fixed ratio was too long for the proved exact theorem

For a fixed shrink factor

\[
q_{j+1}=\vartheta q_j,
\qquad 1-\vartheta\asymp1,
\]

the normalized physical time change is `O(1)`. By (NV2), the corresponding fast interval is

\[
\Delta V\asymp\varepsilon_j^{-1},
\]

which is exponentially/larger-than-polynomial relative to `S_j` as `q_j->0`.

`two_collar_zero_residual_reduction.md` proves polynomial-loss control on transport intervals of size `O(S_j)`; it does not prove a uniform exact nonlinear inverse over `O(epsilon_j^{-1})` fast time.

Hence fixed-ratio **linear shadowing** must not be confused with an exact unforced inter-scale bridge.

## 3. Variable q-step

Choose a fixed design constant

\[
\Lambda>0
\]

and define

\[
\delta_j:=\Lambda\varepsilon_jS_j.
\]

Because

\[
\varepsilon_j=q_j^h
\]

decays exponentially in the native band while `S_j` grows only polynomially,

\[
\boxed{\varepsilon_jS_j\to0.}
\tag{NV4}

After increasing the starting level,

\[
0<\delta_j<\frac12.
\]

Define

\[
\boxed{
q_{j+1}=q_j(1-\delta_j).
}
\tag{NV5}

Thus

\[
q_j-q_{j+1}
=\Lambda q_j^{1+h}S_j.
\tag{NV6}

## 4. The scale sequence still reaches zero

The sequence is positive and strictly decreasing. Let

\[
q_j\downarrow q_\infty\ge0.
\]

If `q_infty>0`, then

\[
\varepsilon_j=q_j^h\ge q_\infty^h>0
\]

and `S_j>=1`, so

\[
\delta_j\ge\Lambda q_\infty^h>0.
\]

Then (NV5) would force a fixed relative decrease at every sufficiently late step, contradicting convergence to a positive limit.

Hence

\[
\boxed{q_j\to0.}
\tag{NV7}

The number of cells is therefore infinite even though the relative scale change per late cell tends to zero.

## 5. First-passage realization on the trapped spine

Use the exact trapped material spine and define `t_{j+1}` as the first time after `t_j` at which

\[
q(t_{j+1})=q_{j+1}.
\]

Existence follows from continuity and `q(t)->0`.

The trapped-spine speed estimate gives

\[
|\dot q|\le C_q.
\]

Therefore

\[
 t_{j+1}-t_j
\ge
\frac{q_j-q_{j+1}}{C_q}
=
\boxed{
\frac{\Lambda}{C_q}q_j^{1+h}S_j.
}
\tag{NV8}

No monotonicity assumption between first-passage times is required.

## 6. Fit one complete cell inside one scale step

The complete nine-lobe corrected cell, including all finite dirty reserve events, clean active gates, finite transport corridors and fixed support buffers, satisfies

\[
\Delta t_j^{cell}
\le
C_{cell}q_j^{1+h}S_j.
\tag{NV9}

Choose once and for all

\[
\boxed{
\Lambda>2C_qC_{cell}.
}
\tag{NV10}

Then (NV8)--(NV9) give

\[
\boxed{
\Delta t_j^{cell}
<\frac12(t_{j+1}-t_j)
}
\tag{NV11}

for every sufficiently high level.

Thus the whole exact cell can be placed between the two first-passage sections with positive temporal buffers. There is no separate macroscopic inter-cell gap that requires an unproved long exact bridge.

## 7. Fast-coordinate length of the entire step

Divide the relative scale change by epsilon:

\[
\frac{q_j-q_{j+1}}{q_j\varepsilon_j}
=
\Lambda S_j.
\]

By the source identity (NV2), the full physical/normalized interval from one scale section to the next therefore corresponds to

\[
\boxed{
\Delta V_j=O(\Lambda S_j).
}
\tag{NV12}

This is exactly the regime treated by the finite-collar zero-residual reduction:

- finite critical propagators have at most polynomial `S_j` loss;
- the stable complement has the uniform inverse/smoothing;
- mean Lipschitz factors carry positive powers of `epsilon_j`;
- every polynomial factor `S_j^C` is dominated by `epsilon_j^alpha` for fixed `alpha>0` at high levels.

Adding the fixed factor `Lambda` changes only design constants.

Hence the **whole scale step** can be included in one exact phase-adapted zero-residual solve, rather than concatenating a local exact cell with a merely linear inter-scale shadowing interval.

## 8. q-variation is source-small inside one step

From (NV5),

\[
\boxed{
\frac{q_j-q_{j+1}}{q_j}
=\Lambda\varepsilon_jS_j
=o(1).
}
\tag{NV13}

Therefore every q-normalized coefficient/frame/phase quantity changes by `o(1)` over one late step on the compact source cone. This variation belongs to the same slowly varying/source-small perturbation class already used to pass frozen gate ranks to finite positive-width exact gates.

In particular, the zero-step canonical beta-two/beta-one frame identification is perturbed by only `o(1)`; no fixed nontrivial two-channel WKB transfer coefficient is needed.

## 9. Exact handoff replaces fixed-ratio shadowing

One late stage is now treated as one single exact object:

\[
\boxed{
\text{incoming renewed lobe/Fourier state at }q_j
\xrightarrow{\text{one exact }O(S_j)\text{ zero-residual circuit}}
\text{renewed state at }q_{j+1}.
}
\tag{NV14}

The finite amplitude/phase controls retract the output to the canonical normalized renewal section, while the q/frame change across the step is only `o(1)` and therefore lies inside the same inverse-function neighborhoods.

Thus the previously open **exact inter-scale bridge** is not solved by extending the PDE inverse to fixed logarithmic length. It is eliminated by choosing the physically natural scale step on which the already-proved exact inverse applies.

## 10. Accumulation time

Since `q_j->0`, the first-passage times along the trapped spine satisfy

\[
t_j\uparrow1.
\]

For every `T<1`, only finitely many complete exact stages occur before `T`.

The infinite construction therefore has the correct finite-time accumulation geometry.

## 11. Revised global frontier

After the native variable-step replacement, the remaining global obligations are:

1. prove an **invariant small ball** for the accumulated stable/nonzero and mean correction state from one exact stage to the next;
2. use finite-stage consistency to define one smooth exact solution on every compact interval `[0,T]`, `T<1`;
3. prove finite total kinetic energy of the full designated + waste field (the reserve waste part is already summable);
4. prove that the renewed physical carrier/amplitude growth forces divergence of the desired regularity norm as `t up to1`.

A fixed-ratio exact bridge is no longer required.

No completed unforced Navier--Stokes blowup theorem is claimed here.
