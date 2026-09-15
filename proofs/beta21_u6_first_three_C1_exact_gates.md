# First three exact active beta-(2,1) gates at the supercritical working point `u_*=6`

**Status:** PROVED WORKING-RESEARCH `C^1` LOCAL ZERO-RESIDUAL GATE PACKAGE, CONDITIONAL ON THE RECORDED COMPUTER-ASSISTED FINITE ENVELOPE/RATE CERTIFICATES AND THE SAME SOURCE-PROFILE AUDIT USED BY THE `u=4` GATES. The exact source-safe moderate-`u` theorem applies to every fixed `u_0>0`, hence in particular to `u_*=6` on a sufficiently short fixed source-safe slab.

At `u=6` the finite dangerous blocks are larger than at `u=4` but remain organized by the single beta-zero root

\[
M=D-C.
\]

The first three active gates can therefore be re-instantiated with control counts

\[
\boxed{7,\quad13,\quad14}
\]

for gates one, two and three respectively. The third gate begins immediately at the second-gate exit and uses the same generic-entrance-amplitude transversality mechanism as at `u=4`.

No fourth/final gate or complete reset-cell theorem is claimed in this note.

## 1. Fixed supercritical design

Use

\[
\boxed{u_*=6,}
\]

with

\[
\delta=0.1686974699091436\ldots,
\qquad
x=1-\delta=0.8313025300908564\ldots,
\]

\[
T=2\delta=0.3373949398182873\ldots.
\tag{G6-1}
\]

The local source-cone theorem permits every fixed finite `u_0>0` on a sufficiently short nondegenerate edge collar, so `u=6` is source-admissible locally. The active-gate proof uses one such fixed source-safe slab.

For the concrete second-section audit use

\[
\boxed{t_2=0.209667379954882\ldots.}
\tag{G6-2}
\]

The exact strong-`H` final renewal root lies at

\[
t_{renew}=0.336494599305936\ldots,
\]

leaving the positive face margin

\[
T-t_{renew}\approx9.00\times10^{-4}.
\]

## 2. Gate one: seven-state finite block

At the first local section,

\[
z_C=1,
\qquad z_D=1-2\delta.
\]

The full naturally-critical audit contains 108 positive-beta characters, but exactly five unwanted modes have positive defect:

\[
2D-C,
\quad3D-2C,
\quad4D-3C,
\quad5D-3C,
\quad6D-4C.
\tag{G6-3}
\]

With

\[
M=D-C,
\]

a sufficient root chain is

\[
\boxed{
M
\to D+M
\to D+2M
\to D+3M
\to2D+3M
\to2D+4M.
}
\tag{G6-4}
\]

All five mandatory principal couplings are nonzero; representative coefficients are

\[
-27.21,\ -24.71,\ -3.73,\ +13.13,\ -32.43.
\tag{G6-5}
\]

Append the desired sum coordinate

\[
P=C+D.
\]

The single-state `P` branch and six-state root branch are individually controllable from the same-character `C` source and have disjoint frozen spectra. The smallest diagnostic rate separation is approximately

\[
1.34\times10^{-2}>0.
\]

Therefore the common-input PBH direct-sum lemma gives a controllable seven-state frozen pair.

Choose seven distinct smooth `C`-profile centers in a sufficiently short fixed collar. Their frozen response matrix satisfies

\[
\boxed{\det J_{7,0}\ne0.}
\tag{G6-6}

The closest uncontrolled naturally-critical mode has a large negative defect (about `-0.225`), so a fixed collar width `w_1=1e-4` easily preserves the classification.

The exact parameter-dependent nonzero/stable solve and residual mean contraction are the same analytic mechanisms as in the first `u=4` gate. In the leading action normalization,

\[
D_p\widehat{\mathcal G}_{1,\ell}
=J_{7,0}+o(1).
\tag{G6-7}

Hence, for all sufficiently high levels, seven smooth controls impose exactly

\[
\boxed{
P_{out}=P_*\ne0,
\qquad
M_{out}=\text{all five root descendants}_{out}=0.
}
\tag{G6-8}

This closes gate one at `u=6`.

## 3. Gate two: thirteen-state finite block

At the concrete second section (G6-2), the full audit contains 109 naturally-critical positive-beta characters. Exactly nine unwanted modes have positive defect:

\[
2D-C,
3D-2C,
4D-3C,
5D-4C,
6D-4C,
7D-5C,
8D-6C,
10D-7C,
11D-8C.
\tag{G6-9}

They lie in the eleven-state sufficient root chain

\[
\boxed{
\begin{aligned}
M
&\to D+M
\to D+2M
\to D+3M
\to D+4M\\
&\to2D+4M
\to2D+5M
\to2D+6M\\
&\to3D+6M
\to3D+7M
\to3D+8M.
\end{aligned}
}
\tag{G6-10}

All mandatory frozen couplings are nonzero. The mean-wave coefficients are approximately

\[
-27.14,\ -40.51,\ -11.02,\ -5.29,\ -48.44,\ -19.56,\ -15.76,\ -66.26,\ -48.08,
\]

and the two wave-wave `+D` edges are approximately

\[
+22.15,\quad+14.40.
\tag{G6-11}

Append the refreshed designated branch

\[
P=C+D,
\qquad E=C+2D.
\]

The resulting thirteen-state frozen pair splits at leading minimal action into a two-state `P/E` branch and the eleven-state root branch, driven by the same scalar `C` source. Each branch is controllable. Their spectra are disjoint; the smallest pairwise frozen separation in the complete sufficient block is about

\[
2.15\times10^{-2}>0.
\]

Thus

\[
\boxed{(A_{13},B_{13})\text{ is controllable}.}
\tag{G6-12}

Thirteen smooth translated `C` profiles give a response matrix

\[
\boxed{\det J_{13,0}\ne0.}
\tag{G6-13}

The closest uncontrolled negative defect is approximately

\[
-0.00554359,
\]

and direct exact-envelope evaluation shows that a short width `w_2=1e-4` preserves (indeed slightly improves) this margin.

The exact action-normalized `C^1` transfer therefore gives, for sufficiently high levels,

\[
\boxed{
P_{out}=0,
\qquad
E_{out}=E_*\ne0,
}
\tag{G6-14}

with all eleven root coordinates zero at the exit and every uncontrolled naturally-critical mode below a fixed negative action gap.

The amplitude `E_*` may be prescribed in a fixed admissible nonzero neighborhood.

## 4. Gate three: append terminal `Q`

Start gate three **immediately** at the exact gate-two exit section. Thus

\[
P=0,
\qquad E=E_*\ne0,
\qquad
M=\text{root chain}=0
\tag{G6-15}

at its entrance, while `C,D` remain present.

Append

\[
Q=2D.
\]

The terminal source contains the two nonzero leading channels

\[
E-C\to Q,
\qquad
X_2+C\to Q.
\]

At `u=6` the frozen coefficients are approximately

\[
\boxed{
\kappa_{E-C\to Q}\approx-6.40734,
\qquad
\kappa_{X_2+C\to Q}\approx+3.01735.
}
\tag{G6-16}

The `Q` full-symbol rate is approximately

\[
\lambda_Q\approx-0.316912,
\]

and its distance to the nearest upstream diagnostic rate is about

\[
\boxed{0.236>0.}
\tag{G6-17}

Thus `lambda_Q` is well outside the upstream spectrum.

## 5. Generic entrance-amplitude transversality at `u=6`

The thirteen-state upstream pair from gate two is controllable. Appending terminal `Q` produces the PBH scalar

\[
\Theta_Q(E_*)
=b_Q(E_*)
-c_Q^T(\lambda_QI-A_{13})^{-1}B_{13}.
\tag{G6-18}

Because `E=E_*` is already nonzero at the immediate entrance, differentiating

\[
E-C_{ctrl}\to Q
\]

provides a direct terminal input

\[
b_Q(E_*)=b_{Q,0}+\alpha_QE_*,
\qquad
\alpha_Q\ne0
\]

by (G6-16). The upstream leading pair is independent of the numerical entrance value `E_*`. Hence

\[
\boxed{
\Theta_Q(E_*)
=\Theta_{Q,0}+\alpha_QE_*
}
\tag{G6-19}

is affine and nonconstant.

There is therefore at most one forbidden complex value (or a proper real algebraic exceptional set in the doubled-real formulation). Choose the gate-two target outside it. Then the full fourteen-state frozen third-gate pair is controllable.

Fourteen translated smooth `C` controls may be chosen so that

\[
\boxed{\det J_{14,0}\ne0.}
\tag{G6-20}

## 6. Exact third-gate transfer

Normalize the promoted terminal `Q` on its source-matched absolute-leaf action scale. Extract the complete fourteen-state finite block, including the beta-zero root, and leave the remaining infinite lattice in the stage-uniform stable complement.

The same parameter-dependent contraction estimates give

\[
D_p\widehat{\mathcal G}_{3,\ell}
=J_{14,0}+o(1).
\tag{G6-21}

Thus the exact inverse/implicit-function theorem gives fourteen controls with

\[
\boxed{
P_{out}=0,
\qquad
E_{out}=0,
\qquad
Q_{out}=Q_*\ne0,
}
\tag{G6-22}

and all eleven root coordinates zero at the third-gate exit.

This closes gate three at `u=6`.

## 7. What is now closed at `u=6`

At working-research level we have the exact local chain

\[
\boxed{
(C,D)
\stackrel{G_1}{\longmapsto}(C,D,P_*)
\stackrel{G_2}{\longmapsto}(C,D,E_*)
\stackrel{G_3}{\longmapsto}(C,D,Q_*),
}
\tag{G6-23}

with finite exact cancellation of the complete audited dangerous root family at each exit section.

The next event must **not** use the weaker nominal `Q-C -> H` action as its leading scale. The fourth-gate obstruction proves that the unavoidable root-generated

\[
H=2D-C
\]

appears at the stronger action `A_C+2A_D`. The supercritical `u=6` design was chosen precisely because accepting that strong `H` opens the causal final renewal root (G6-1).

The next proof layer is therefore an exact fourth active gate that prescribes the strong root-scale `H` while cancelling the rest of the enlarged root family, followed by the final `H+D -> P_new` renewal event at `t_renew`.

No complete reset-cell theorem is claimed yet.
