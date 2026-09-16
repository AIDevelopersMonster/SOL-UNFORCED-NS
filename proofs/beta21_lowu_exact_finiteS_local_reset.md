# Exact finite-`S` local reset theorem for the low-`u` boundary-layer cell

**Status:** PROVED EXACT LOCAL FINITE-`S` RESET THEOREM WITH ZERO RESIDUAL ON ONE RELAY COLLAR / GLOBAL INTER-CELL ASSEMBLY AND INFINITE CASCADE STILL OPEN.

This theorem combines the principal bilateral-orbit reset, the exact coupled mean/nonzero correction, and the `C^1` persistence of the finite-dimensional reset Jacobian.

For every sufficiently large source level, there exists a parameter triple

\[
p_S^{exact}=(\kappa_S,\theta_S,A_{M,S})
\]

near the principal boundary-layer point such that:

1. the complete unforced local Navier--Stokes residual vanishes on the relay collar;
2. the outgoing beta-one catalyst orbit is exactly reset after relabelling;
3. the outgoing beta-two parent orbit is exactly reset after relabelling;
4. the designated beta-zero mean root is carried consistently as incoming/outgoing Cauchy state;
5. all non-designated mean and nonzero harmonics are contained in the unique small coupled correction.

This closes the **one-cell local reset problem**.  It does not construct an infinite sequence of cells, a single global smooth initial datum realizing infinitely many resets, or a Navier--Stokes blowup solution.

## 1. Principal finite-`S` reset

`beta21_lowu_boundary_layer_bilateral_orbit_reset.md` proves the limiting reset point

\[
\boxed{
u=1.8,\qquad x=0.70,}
\]

with

\[
\boxed{
\kappa_*=0.894049167184884\ldots,
\qquad
\theta_*=2.619416765747896\ldots.
}
\]

The principal finite-`S` Poincare map differs from the limiting map by `O(S^{-1})`.  Its transversality gives one principal exact reset parameter triple

\[
\boxed{
p_S^{prin}=p_*+O(S^{-1})}
\tag{LR1}
\]

for which the finite-`S` **principal** catalyst and parent multipliers are exactly one.

The beta-zero amplitude component of `p` is tuned through the nonzero catalyst scalar derivative.

## 2. Principal Jacobian

Let

\[
\mathcal O_S^{prin}(p)\in\mathbb R^3
\]

be the three real principal reset observables:

1. catalyst multiplier error;
2. real parent multiplier error;
3. imaginary parent multiplier error.

At the limiting point the catalyst derivative is

\[
\boxed{
\lambda_C-\rho_C^{-1}
=-5.83150782219\ldots\ne0,
}
\tag{LR2}

and the parent block satisfies

\[
\boxed{
\det D_{(\kappa,\theta)}
(\Re F_P,\Im F_P)
=1.2199224287\ldots\ne0.
}
\tag{LR3}

Hence the full three-real-variable limiting Jacobian

\[
J_0:=D_p\mathcal O_0^{prin}(p_*)
\]

is invertible.

For sufficiently large `S`, the principal finite-`S` Jacobian remains invertible uniformly:

\[
\boxed{
\|(D_p\mathcal O_S^{prin})^{-1}\|
\le C_J.
}
\tag{LR4}

## 3. Exact PDE correction at fixed parameters

For each `p` in a fixed small neighborhood of `p_*`, the coupled theorem

`beta21_lowu_coupled_mean_nonzero_contraction.md`

produces a unique correction

\[
U_S(p)=(m_S(p),z_S(p))
\]

such that the residual mean and nonzero equations vanish simultaneously.

The correction radius satisfies

\[
\boxed{
\|U_S(p)\|_{*,S}
\le R_S,
\qquad R_S\to0.
}
\tag{LR5}

The source hierarchy gives the more explicit form

\[
R_S
\le
S^A\varepsilon^{a_*}
+S^Ae^{-cS}
\tag{LR6}
\]

for one fixed `a_*>0`.

Since the source length grows only polynomially in the band index whereas `epsilon=Q^h` decreases exponentially, one has for every fixed `N`

\[
\boxed{S^NR_S\to0.}
\tag{LR7}

Thus the exact PDE correction is super-polynomially small in `S^{-1}` along the source hierarchy.

## 4. Exact reset observable

Define the exact PDE-corrected reset map

\[
\boxed{
\mathcal O_S^{exact}(p)
:=
\mathcal O_S^{out}(p;U_S(p)).
}
\tag{LR8}

where `O_out` extracts the action-normalized outgoing catalyst and parent reset errors after the full reconstructed field is solved.

`beta21_lowu_coupled_C1_parameter_transfer.md` proves

\[
\boxed{
\mathcal O_S^{exact}(p)
=
\mathcal O_S^{prin}(p)+r_S(p),
}
\tag{LR9}

with

\[
\boxed{
\|r_S\|_{C^1(K_p)}\to0.
}
\tag{LR10}

In fact, after fixed polynomial trace/output losses,

\[
\|r_S\|_{C^1}
\le
S^BR_S
\tag{LR11}
\]

for one fixed `B`, so by (LR7)

\[
\boxed{
\|r_S\|_{C^1}=o(S^{-N})
}
\tag{LR12}
\]

for every fixed `N`.

## 5. Persistence of invertibility

At `p_S^{prin}`,

\[
\mathcal O_S^{prin}(p_S^{prin})=0.
\]

By (LR10),

\[
\boxed{
\mathcal O_S^{exact}(p_S^{prin})
=r_S(p_S^{prin})=o(1).
}
\tag{LR13}

Also

\[
D_p\mathcal O_S^{exact}
=
D_p\mathcal O_S^{prin}+D_pr_S.
\]

For sufficiently large `S`, (LR4) and (LR10) imply

\[
\boxed{
\|(D_p\mathcal O_S^{exact})^{-1}\|
\le2C_J
}
\tag{LR14}

throughout a fixed small neighborhood of `p_S^{prin}`.

Thus the exact corrected reset map remains uniformly transverse.

## 6. Finite-dimensional correction

Apply the quantitative inverse/implicit-function theorem to

\[
\mathcal O_S^{exact}:
\mathbb R^3\to\mathbb R^3
\]

at `p_S^{prin}`.

There exists a unique nearby parameter triple

\[
\boxed{p_S^{exact}}
\tag{LR15}

such that

\[
\boxed{
\mathcal O_S^{exact}(p_S^{exact})=0.
}
\tag{LR16}

Moreover

\[
\|p_S^{exact}-p_S^{prin}\|
\le
C\|r_S(p_S^{prin})\|.
\tag{LR17}

Hence

\[
\boxed{
p_S^{exact}=p_S^{prin}+o(S^{-N})}
\tag{LR18}
\]

for every fixed `N` permitted by the frozen source bookkeeping, and in particular

\[
\boxed{
p_S^{exact}=p_*+O(S^{-1}).}
\tag{LR19}

Thus

\[
\boxed{
\kappa_S=\kappa_*+O(S^{-1}),
\qquad
\theta_S=\theta_*+O(S^{-1}),
}
\tag{LR20}

with the beta-zero root amplitude receiving only a source-small exact correction from its principal tuned value.

## 7. Exact zero residual

For `p=p_S^{exact}`, let

\[
U_S^{exact}
:=
U_{base}
+M_{des}(p)
+U_{orb,S}(p)
+m_S(p)
+z_S(p).
\tag{LR21}

By the coupled fixed-point theorem and exact physical reconstruction,

\[
\boxed{
\mathcal N_{NS}
\bigl(U_S^{exact}\bigr)=0
}
\tag{LR22}

on the complete local relay collar.

There is no external forcing.  The designated root and orbit are incoming state data; the residual corrections are forward internal solutions of the unforced equations.

## 8. Exact orbit reset

Equation (LR16) means exactly that the corrected outgoing designated orbit equals the next canonical incoming orbit after reset relabelling.

For the catalyst family,

\[
\boxed{
C_{out,j}
\equiv C_{in,j+1}
}
\tag{LR23}

in the canonical next-cell labeling.

For the parent family,

\[
\boxed{
Q_{out,n}
\equiv Q_{in,n+2}
}
\tag{LR24}

with exact amplitude/phase normalization prescribed by the Poincare coordinates.

Equivalently, the outgoing designated state is exactly the reset image of the incoming designated state.

## 9. Beta-zero root handoff

The root character satisfies

\[
R(M)=M.
\]

The Cauchy-realized root is part of the designated mean state and is propagated by the exact root-augmented mean equation.  Its normalized amplitude parameter is included in `p_S^{exact}`.

Therefore the outgoing root coordinate is exactly the one required by the next canonical cell after the same relabelling and normalization.

No future-time root field is prearranged; the root is present in the incoming Cauchy state and carried forward.

## 10. Residual harmonics

All non-designated modes belong to the unique small coupled correction.

The nonzero correction obeys

\[
\|z_S\|
\le
S^A\varepsilon^{1/5}
+S^Ae^{-cS},
\]

up to the fixed product-space normalization.

The residual mean correction obeys

\[
\|m_S\|
\le
S^A\varepsilon^{1-\kappa_s}
+S^Ae^{-cS},
\]

with generated nonzero `rM` tails exponentially smaller.

Thus the exact reset does not require a growing bank of uncontrolled correction modes.

## 11. Local theorem closed

The following statement is now established within the theorem chain of this branch:

\[
\boxed{
\begin{minipage}{0.88\linewidth}
For every sufficiently large source level there exists one genuinely Cauchy-realizable, unforced, exact local Navier--Stokes solution on the low-`u` relay collar whose designated beta-one/beta-two bilateral orbit and beta-zero mean root return exactly to the canonical reset state after one cell.
\end{minipage}
}
\tag{LR25}

This is the first theorem in the low-`u` boundary-layer route where the **principal reset and the infinite-dimensional exact PDE correction are simultaneously closed**.

## 12. What this theorem does not prove

It does **not** prove:

1. that infinitely many such cells can be embedded into one global solution;
2. that the cell-to-cell physical support geometry remains compatible indefinitely;
3. that one smooth finite-energy initial datum generates the entire infinite chain;
4. convergence of the infinite correction sum;
5. persistence of a blowup observable in the global limit;
6. finite-time singularity of unforced Navier--Stokes.

Those are separate global assembly obligations.

## 13. Next frontier

The local low-`u` reset branch has crossed its local publication threshold mathematically, but before publication it still needs the standing numerical/source audit:

- outward-rounded interval certification of the quoted numerical margins;
- explicit source line/theorem citations for the uniform packet bounds;
- notation and numbering audit;
- conservative claim wording.

For the research programme, the next mathematical task is **inter-cell assembly**:

1. combine the exact local reset with the near-one cross-scale transfer;
2. place finitely many near-one cells inside each dyadic source slab;
3. use the exact catalyst/root/orbit reset as the cell handoff;
4. prove convergence of the infinite forward correction sequence to one smooth finite-energy initial datum;
5. only then test whether the intended physical blowup observable survives the exact limit.

No global claim should be made before those steps are closed.
