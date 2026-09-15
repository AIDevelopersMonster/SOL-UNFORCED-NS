# Amplitude transversality for the corrected three-gate beta-(2,1) active cell

**Status:** PROVED FINITE-DIMENSIONAL AMPLITUDE-RENEWAL THEOREM CONDITIONAL ONLY ON PHYSICAL SUPPORT CONCATENATION OF THE THREE ALREADY-CLOSED LOCAL GATES. The corrected non-turning architecture now has exact local zero-residual theorems for

1. the entrance gate `P-C -> D`;
2. the strong-`H` gate producing `P_new` and cancelling old `C`;
3. the final three-state cleanup gate.

This note proves that, once those collars are realized in one causal support circuit, there is **no additional amplitude fixed-point obstruction**. The entrance controls prescribe the outgoing unit-beta amplitude `D_*`; the terminal controls prescribe the outgoing beta-two amplitude `P_*`. Treating `D_*` as one global complex cell parameter, the full four-coordinate handoff map

\[
(P_{out},D_{out},H_{out},M_{out})
\]

has a block-triangular Jacobian with nonzero determinant. Therefore the complete cell can return any nearby prescribed nonzero beta-two/beta-one amplitude pair, in particular the same pair used at its input after the character relabelling `(P_new,D)->(P,C)`.

The remaining local obstacle is geometric/support-theoretic: prove that the physically generated `D` and the surviving catalyst bank can be routed through the separated collars without an uncontrolled common overlap. This theorem deliberately does not assume that point silently.

## 1. Three exact local gates already available

At

\[
u=2.5,
\qquad
\delta=0.1375,
\qquad
x=0.7779445026067248271\ldots,
\]

the branch now contains:

### Entrance gate

`beta21_corrected_entrance_four_control_C1_closure.md` gives, for every prescribed `D_*` in a fixed nonzero compact neighborhood, a four-control exact solve with

\[
\boxed{(D,M,H,R_3)_{out}=(D_*,0,0,0).}
\tag{AT1}
\]

The catalyst `C` remains nonzero and the old parent is routed away from later collisions.

### Strong-`H` gate

`beta21_corrected_strong_H_nine_control_C1_closure.md` gives a nine-control exact solve with

\[
\boxed{
(C,M,P,H,2D+C,D+2C,2C-D,P_{new},3D+C)_{out}
=(0,0,0,0,0,0,0,P_H,0)
}
\tag{AT2}
\]

for a prescribed nonzero `P_H`, while the `D` channel stays in a fixed nonzero compact range.

### Terminal gate

`beta21_corrected_terminal_three_control_C1_closure.md` gives three same-character `P_new` controls with

\[
\boxed{(P_{new},H,M)_{out}=(P_*,0,0).}
\tag{AT3}
\]

Again the `D` channel remains nonzero.

All three maps are exact local zero-residual maps for sufficiently high dyadic levels, with `C^1` dependence on their finite parameters.

## 2. Promote the entrance output amplitude to a cell parameter

Let

\[
d\in\mathbb C
\]

denote the prescribed entrance output in (AT1). The entrance inverse-function theorem is uniform on a compact nonzero neighborhood, so the four entrance control amplitudes are `C^1` functions

\[
p^{ent}=p^{ent}(d;A_P^{in},A_C^{in})
\tag{AT4}
\]

and the exact entrance output satisfies

\[
D_{ent}=d.
\tag{AT5}
\]

The subsequent free/designated transport of the `D` channel between disjoint active collars is linear at principal order. Write its normalized transfer factors as

\[
g_{D,1},\qquad g_{D,2},
\]

for entrance-to-strong-`H` and strong-`H`-to-terminal transport. On every finite source-safe compact collar these factors are nonzero.

The exact mean/stable-complement corrections and the exact finite control solves perturb the `D` trace by `o(1)` in `C^1`. Therefore the final unit-beta amplitude has the form

\[
\boxed{
D_{out}(d,p^{term})
=g_D d+r_{D,\ell}(d,p^{term}),
\qquad
 g_D:=g_{D,1}g_{D,2}\ne0,
}
\tag{AT6}

with

\[
\boxed{
\|r_{D,\ell}\|_{C^1}=o(1).
}
\tag{AT7}

The terminal `P_new` controls may affect `D` only through the same lower-order exact correction mechanism; they do not provide an order-one direct `D` source because their principal character is beta two.

Hence

\[
\boxed{
\partial_dD_{out}=g_D+o(1),
}
\tag{AT8}

uniformly, and in particular this derivative is nonzero for all sufficiently high levels.

## 3. Terminal three-control transverse block

Let

\[
p=(p_1,p_2,p_3)\in\mathbb C^3
\]

be the terminal same-character `P_new` controls. The terminal theorem gives the exact exit map

\[
\mathcal T_\ell(d,p)
=(P_{out},H_{out},M_{out}).
\tag{AT9}

For fixed `d`,

\[
\boxed{
D_p\mathcal T_\ell
=J_{3,var}+o(1),
\qquad
\det J_{3,var}\ne0.
}
\tag{AT10}

Thus the three complex terminal controls remain locally onto the three complex coordinates `(P,H,M)`.

## 4. Full four-coordinate handoff Jacobian

Define the complete local amplitude-cleanup map

\[
\boxed{
\mathcal A_\ell(d,p)
=(D_{out},P_{out},H_{out},M_{out})
\in\mathbb C^4.
}
\tag{AT11}

Order the variables as `(d,p_1,p_2,p_3)` and outputs as `(D,P,H,M)`.

At principal level the Jacobian has block form

\[
D\mathcal A_0
=
\begin{pmatrix}
 g_D & 0\\
 * & J_{3,var}
\end{pmatrix}.
\tag{AT12}

The exact local solves perturb this matrix only by `o(1)` in the same normalized coordinates:

\[
\boxed{
D\mathcal A_\ell
=
\begin{pmatrix}
 g_D & 0\\
 * & J_{3,var}
\end{pmatrix}
+o(1).
}
\tag{AT13}

Therefore

\[
\boxed{
\det D\mathcal A_\ell
=g_D\det J_{3,var}+o(1).
}
\tag{AT14}

Since both principal factors are nonzero, there exists `ell_0` such that for every `ell>=ell_0`,

\[
\boxed{\det D\mathcal A_\ell\ne0.}
\tag{AT15}

## 5. Exact prescription of the outgoing pair

Let

\[
(A_2^*,A_1^*)\in(\mathbb C\setminus\{0\})^2
\]

be any target beta-two/beta-one pair in a sufficiently small fixed neighborhood of the principal cell output.

Apply the inverse-function theorem to (AT11). There exist unique nearby parameters

\[
\boxed{d_\ell=d_0+o(1),
\qquad
p_\ell=p_0+o(1)
}
\tag{AT16}

such that

\[
\boxed{
D_{out}=A_1^*,
\qquad
P_{out}=A_2^*,
\qquad
H_{out}=0,
\qquad
M_{out}=0.
}
\tag{AT17}

The entrance controls are then chosen as the exact `C^1` function `p^{ent}(d_ell;A_P^{in},A_C^{in})`, and the strong-`H` controls are chosen by their own exact inverse-function theorem on the resulting compact incoming neighborhood.

Thus the output amplitudes are not merely close to a renewal section: they can be prescribed exactly within the local active-cell neighborhood.

## 6. Exact amplitude renewal

Take the desired output pair equal to the chosen input normalized pair after the canonical character relabelling

\[
(P_{new},D)\mapsto(P,C).
\tag{AT18}

That is, if the input amplitudes are

\[
(A_P^{in},A_C^{in}),
\]

set

\[
A_2^*=A_P^{in},
\qquad
A_1^*=A_C^{in}.
\tag{AT19}

Then (AT17) gives

\[
\boxed{
(A_{P_{new}}^{out},A_D^{out})
=(A_P^{in},A_C^{in}),
}
\tag{AT20}

while every promoted terminal contaminant is exactly zero.

Since the corrected geometry already gives the slope return

\[
(z_{P_{new}},z_D)_T=(x,x+\delta),
\]

and the exact action identities give the corresponding natural output action levels, the **finite-dimensional state renewal problem is closed** once physical support concatenation is supplied.

No separate two-amplitude fixed-point theorem is required.

## 7. Phase reset

The two outgoing generators have linearly independent integer characters in the rank-two lattice. As in `exact_two_collar_renewal_state.md`, a torus translation gives two independent phase parameters. Therefore, after matching the exact amplitudes (AT20), the two complex arguments can also be reset to the chosen input reference phases.

Thus amplitude magnitudes and phases present no additional finite-dimensional obstruction.

## 8. What remains local

The corrected active cell is now closed in

- envelope/action geometry;
- principal polarization;
- finite critical rank;
- exact local zero-residual transfer for each of three collars;
- terminal cleanup;
- exact two-amplitude/phase renewal.

The single remaining **local-cell** obligation is:

\[
\boxed{
\textbf{physical support concatenation of the three collars.}
}
\tag{AT21}

Specifically, one must prove that the physically generated entrance child `D` and the surviving catalyst configuration can

1. leave the entrance overlap before uncontrolled downstream generation;
2. be transported to the strong-`H` collar;
3. realize exactly the required `C,D` overlap there;
4. leave that overlap with `C=0` and the new `(P_new,D)` bank;
5. enter the terminal collar without reintroducing an uncontrolled earlier parent overlap.

`translated_async_overlap.md` proves finite prescribed overlap geometry, but `support_gating_requires_generation_delays.md` shows that this is not by itself a theorem for a **generated** child. Therefore (AT21) must be proved separately and cannot be replaced by a label-routing assertion.

## 9. Programme consequence

Conditional on (AT21), the branch has an exact local autonomous beta-(2,1) renewal cell:

\[
\boxed{
(P,C)_{in}
\longmapsto
(P_{new},D)_{out}
\equiv(P,C)_{next},
}
\tag{AT22}

with exact slope, action, amplitude and phase reset and with every source-promoted contaminant controlled or action-subcritical.

This is a major reduction of the local problem. It is **not** a global cascade or an unforced Navier--Stokes blowup theorem: after support concatenation, cross-scale shadowing, infinite sparse placement, summability and initial-data recovery remain.
