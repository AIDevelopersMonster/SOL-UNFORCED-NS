# Two-channel small-log cross-scale transfer for the corrected beta-(2,1) cell

**Status:** PROVED NORMALIZED TWO-CHANNEL TRANSFER THEOREM UNDER THE SAME SOURCE-SMOOTH COEFFICIENT HYPOTHESIS AS `small_log_step_designated_transfer.md`. For the corrected active cell the outgoing and next incoming designated states have the same beta-two/beta-one normalized frame. Therefore the zero-log-step transfer is the identity on the entire two-dimensional designated block, not merely on one scalar child direction. A sufficiently small fixed logarithmic scale step keeps the full `2 x 2` normalized transfer uniformly close to the identity and hence invertible.

Combined with the exact local amplitude transversality of `beta21_corrected_active_cell_amplitude_transversality.md`, this closes the cross-scale **Fourier-state** shadowing problem for the prearranged finite-bank route. It does not reproduce the auxiliary support-label bank; those labels are assumed prearranged independently at each scale in this route.

## 1. Canonical outgoing and incoming frame

At the reset face of the corrected cell,

\[
(z_{P_{new}},z_D)=(x,x+\delta),
\]

with beta weights

\[
(2,1).
\]

After the canonical character relabelling

\[
(P_{new},D)\mapsto(P,C),
\]

the next cell uses exactly the same normalized beta/slope frame.

Let

\[
E_{des}=\operatorname{span}\{e_2,e_1\}
\]

be this fixed complex two-dimensional normalized designated block, where `e_2` and `e_1` denote the beta-two and beta-one source-frame packet directions, including their principal polarizations.

At zero logarithmic q-separation the canonical identification is exact:

\[
\boxed{\widehat T(0)|_{E_{des}}=I_{E_{des}}.}
\tag{2C1}

## 2. Logarithmic transport equation

Put

\[
\sigma=\log(q_j/q),
\qquad
q_{j+1}=\vartheta q_j,
\qquad
L_\vartheta=\log(1/\vartheta).
\]

Under the source normalization used in `q_transport_renormalization_reduction.md` and `small_log_step_designated_transfer.md`, the finite designated state obeys

\[
\partial_\sigma a
=A(\sigma)a,
\]

with

\[
A(\sigma)=A_0(\sigma)+E_j(\sigma).
\]

On the compact strict source cone, the source-smooth coefficient hypothesis gives

\[
\boxed{
\|A_0(\sigma)\|\le C_A,
\qquad
\sup_\sigma\|E_j(\sigma)\|\le\eta_j,
\qquad
\eta_j\to0.
}
\tag{2C2}

The same statement holds for the normalized two-generator phase-covector block.

## 3. Near-identity estimate on the whole designated block

Let `U_j(s,0)` be the fundamental matrix. Duhamel plus Gronwall gives

\[
\boxed{
\|U_j(L_\vartheta,0)-I\|
\le
\exp[(C_A+\eta_j)L_\vartheta]-1.
}
\tag{2C3}

Choose once and for all `vartheta_*<1` sufficiently close to one that

\[
\exp[2C_A\log(1/\vartheta_*)]-1<\frac14.
\tag{2C4}

Then for every fixed

\[
\vartheta\in(\vartheta_*,1)
\]

and every sufficiently high relay level,

\[
\boxed{
\|G_j-I_2\|<\frac14,
\qquad
G_j:=\Pi_{des}U_j(L_\vartheta,0)|_{E_{des}}.
}
\tag{2C5}

The transverse component obeys the same small bound:

\[
\boxed{
\|\Pi_{des}^\perp U_j(L_\vartheta,0)|_{E_{des}}\|<\frac14.
}
\tag{2C6}

After choosing the step smaller if required, the right side in (2C6) lies inside the strict stable/cone margin used by the local cell.

## 4. Uniform invertibility

From (2C5),

\[
G_j=I_2+K_j,
\qquad
\|K_j\|<\frac14.
\]

Hence the Neumann series gives

\[
\boxed{
G_j^{-1}
=\sum_{m=0}^\infty(-K_j)^m,
}
\tag{2C7}

and

\[
\boxed{
\|G_j^{-1}\|\le\frac4{3}.
}
\tag{2C8}

In particular every singular value of `G_j` lies in the interval

\[
\boxed{
\frac34< s_k(G_j)<\frac54,
\qquad k=1,2.
}
\tag{2C9}

Thus neither designated channel can collapse under one fixed small logarithmic scale step, and no accidental scalar cancellation can destroy the two-channel state.

## 5. Phase-covector persistence

The two phase covectors satisfy the normalized eikonal transport equation

\[
\partial_\sigma n
=A_{cov}(\sigma)n
\]

with a uniformly bounded generator on the compact source cone.

Therefore

\[
\|U^{cov}_j(L_\vartheta,0)-I\|
\le C L_\vartheta+o_j(1).
\tag{2C10}

The corrected beta-two/beta-one phase pair lies strictly inside its admissible cone. Choose `vartheta` so close to one that (2C10) is smaller than half the cone distance. Then both transported phase covectors remain admissible uniformly at high levels.

## 6. Exact next-cell correction by the active amplitude map

Let

\[
A_j^{out}\in\mathbb C^2
\]

be the exact corrected cell output. Cross-scale transport gives

\[
\widetilde A_{j+1}
=G_j A_j^{out}+r_j,
\]

where the projected stable/transverse leakage is inside the small correction class.

Because `G_j` is uniformly close to the identity, the transported pair lies in the same fixed compact nonzero amplitude neighborhood used by the exact local gate theorems whenever the canonical renewal state does.

The next corrected active cell is not a rigid fixed map: `beta21_corrected_active_cell_amplitude_transversality.md` proves local surjectivity of the finite amplitude controls. Hence the next cell can accept the transported pair and choose its internal controls so that its output is retracted exactly to the canonical pair.

Thus there is a one-step map

\[
\boxed{
A_j^{ren}
\xrightarrow{\text{normalized physical transport}}
\widetilde A_{j+1}
\xrightarrow{\text{exact active cell}}
A_{j+1}^{ren},
}
\tag{2C11}

with all amplitudes remaining in one fixed compact nonzero range.

## 7. Physical q-scaling

Restoring physical units contributes the same exact source normalization factor as in the one-channel theorem:

\[
\gamma=\frac{1+h}{2},
\qquad
U_{pkt}(q),\Omega_{phys}(q)\asymp q^{-\gamma}.
\]

For

\[
q_{j+1}=\vartheta q_j,
\]

one step multiplies the physical unit scale by

\[
\vartheta^{-\gamma}.
\]

The matrix `G_j` contributes only a uniformly bounded nonzero normalized change. Thus repeated corrected cells retain the intended geometric physical carrier growth.

## 8. Fixed-ratio infinite sequence

Choose one

\[
\vartheta\in(\vartheta_*,1)
\]

and set

\[
q_j=q_0\vartheta^j.
\]

Then

\[
q_j\downarrow0,
\qquad
\Omega_{phys}(q_j)\asymp q_0^{-\gamma}\vartheta^{-j\gamma}\to\infty.
\]

The small step does not stop the scale cascade; it only increases the number of local cells per fixed logarithmic scale change.

## 9. Scope for the finite-bank route

The theorem closes cross-scale transport of the **two Fourier generators** and their phase covectors. In the prearranged finite-bank route, the auxiliary same-character support labels required by the next cell are placed independently at that scale as part of the global initial packet bank. Therefore they do not have to be dynamically cloned by the two-channel transfer.

What remains for that route is now geometric/global rather than finite-dimensional:

1. sparse placement of the countably many finite-bank cells and their active collars;
2. summability of every designated/control/correction packet over all scales;
3. recovery of one smooth finite-energy initial datum;
4. proof that the exact infinite assembly remains zero residual and reaches the intended finite accumulation time.

The stronger strict-autonomous-bank route remains open because it asks the outgoing packet to reproduce the auxiliary support-label microstructure itself.

No global unforced Navier--Stokes blowup theorem is claimed here.
