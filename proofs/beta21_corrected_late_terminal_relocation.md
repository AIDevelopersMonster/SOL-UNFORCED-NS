# Late relocation of the corrected three-state terminal gate

**Status:** PROVED POSITIVE-WIDTH RELOCATION OF THE EXACT THREE-CONTROL TERMINAL GATE TO A COLLAR ADJACENT TO THE RESET FACE, SUBJECT TO THE SAME NUMERICAL-CERTIFICATION CAVEAT AS THE ORIGINAL TERMINAL THEOREM. The exact three-state terminal theorem in `beta21_corrected_terminal_three_control_C1_closure.md` was first placed shortly after the strong-`H` section. For support concatenation it is better to postpone that gate until the end of the post-strong-`H` interval, so that the common `(P_new,D)` overlap can terminate immediately after exact cancellation of its promoted descendants.

Take

\[
T=2\delta=0.275,
\qquad
\boxed{t_{term}:=T-0.002=0.273}
\]

and the fixed collar

\[
\boxed{I_{term}:=[T-0.003,T-0.001]=[0.272,0.274].}
\]

On this collar the complete source-promoted block remains `(P_new,H,M)`, and the two mandatory chain couplings remain uniformly separated from zero. Therefore the same three-control exact `C^1` inverse-function theorem applies at the relocated collar.

The benefit is geometric: after the right endpoint `T-0.001`, the supports of `P_new` and `D` may be separated. Since `H=M=0` exactly at that exit and the parent supports no longer overlap afterwards, no new terminal contaminant is generated before the reset face.

## 1. The promoted-set audit is interval-global

The propagated-action classification used in `beta21_corrected_terminal_three_control_C1_closure.md` was not local to the original early terminal center. It maximized the action of every descendant over the entire interval

\[
 t_*<s<T.
\]

That audit proved that the only new descendants above the renewed beta-two target are

\[
H=P_{new}-D,
\qquad
M=P_{new}-2D.
\]

The nearest omitted sum child `P_new+D` has fixed negative reset-face gap

\[
\Delta_{sum}
\approx-8.5566\times10^{-3},
\]

and regenerated old catalyst `3D-P_new` is still lower.

Hence moving the cancellation collar anywhere inside `(t_*,T)` does not change the finite promoted state.

## 2. Late source geometry

At a time `s`,

\[
z_D(s)=x-\delta+s,
\qquad
z_P(s)=x-2\delta+s.
\]

On `I_term`, both lie strictly inside the source interval. The difference child

\[
z_H(s)=2z_P(s)-z_D(s)
\]

also stays positive and source-admissible.

At the center `s=0.273`,

\[
z_D\approx0.9134445026,
\]

\[
z_P\approx0.7759445026,
\]

\[
z_H\approx0.6384445026.
\]

Thus the late collar stays away from every raw source endpoint.

## 3. Difference-edge margin

The mandatory positive-beta difference interaction is

\[
P_{new}-D\to H.
\]

Using the exact principal formula from `beta21_microcascade_polarization_audit.md`, at the late center

\[
\boxed{
\kappa_{P-D\to H}
\approx-1.2477527210.
}
\]

At the two endpoints one obtains approximately

\[
-1.2479147363,
\qquad
-1.2475906948.
\]

Therefore throughout `I_term`,

\[
\boxed{
|\kappa_{P-D\to H}|>1.2475.
}
\tag{LT1}
\]

## 4. Beta-zero root margin

The next mandatory edge is

\[
H-D\to M,
\qquad \beta(M)=0.
\]

The exact projected beta-zero source norm from the root formula is approximately

\[
4.0208877243
\]

at the center. At the endpoints it is approximately

\[
4.0163397733,
\qquad
4.0254364424.
\]

Hence

\[
\boxed{
\|b_{H-D\to M}\|>4.016
}
\tag{LT2}
\]

throughout the relocated collar.

## 5. Frozen rank is unchanged

Order the state as

\[
X=(P_{new},H,M).
\]

As before, same-character `P_new` controls enter the first coordinate directly. Let `a` be the nonzero linearized `P_new -> H` coefficient and `b` the nonzero `H -> M` coefficient, including the fixed nonzero `D` base amplitude.

For the complete frozen in-block operator,

\[
\det[B,AB,A^2B]=a^2b\ne0.
\]

The bounds (LT1)--(LT2) give a fixed positive rank margin after the design is frozen. Slow coefficient variation on a sufficiently narrow positive collar preserves the determinant.

## 6. Exact `C^1` transfer

The source packet classes, finite parameter derivatives, exact nonzero solve and exact mean solve are identical to those in the original terminal theorem. Only the fixed center of the three control profiles has changed.

Therefore the exact exit map

\[
\mathcal G^{term,late}_\ell(p)
=(P_{new},H,M)_{out}
\]

satisfies

\[
D_p\mathcal G^{term,late}_\ell
=J_{3,late}+o(1),
\qquad
\det J_{3,late}\ne0,
\]

and for every sufficiently high level there is an exact control vector with

\[
\boxed{
(P_{new},H,M)_{out}=(P_*,0,0).
}
\tag{LT3}

The designated `D` channel stays nonzero.

## 7. Support-exit advantage

Choose the common `P_new,D` overlap so that its last active intersection is exactly the late terminal collar and the two parent supports are disjoint for

\[
T-0.001<t\le T.
\]

At the right endpoint of the gate, (LT3) gives

\[
H=M=0.
\]

After that endpoint the quadratic products requiring simultaneous `P_new,D` support vanish identically. Hence neither `H` nor `M` can be regenerated on the final free segment.

The two designated parents then propagate homogeneously to `T`, where their slopes are exactly

\[
(z_{P_{new}},z_D)=(x,x+\delta).
\]

Thus the late relocation converts the terminal gate into a genuine **last-overlap exit gate**, which is the form required for the support-circuit theorem.

## 8. Scope

This theorem does not by itself construct the earlier entrance-to-strong-`H` support handoff. It only removes the post-terminal regeneration problem. The remaining support issue is now concentrated in transporting the entrance-generated `D` to a later overlap with the catalyst configuration without retaining an uncontrolled common `C,D` support between the two active collars.
