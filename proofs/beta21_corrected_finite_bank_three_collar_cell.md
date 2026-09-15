# Corrected beta-(2,1) three-collar cell with a finite same-character support bank

**Status:** PROVED ONE-CELL SUPPORT/EXACT-ZERO-RESIDUAL CONCATENATION THEOREM WITH A FINITE PRELOADED SAME-CHARACTER CATALYST BANK, SUBJECT TO THE BRANCH-WIDE SOURCE-LINE AND NUMERICAL-CERTIFICATION CAVEATS. NOT A SELF-REPLICATING SUPPORT-BANK RENEWAL THEOREM. The corrected active gates can be placed in one causal physical-support circuit if the input catalyst character is represented by two support-separated copies carrying the same Fourier character and polarization:

\[
C^{ent},\qquad C^{H}.
\]

`C^{ent}` participates only in the entrance `P-C -> D` gate. The generated `D` harmonic is then transported on its carrier to the late strong-`H` collar, where it meets `C^H`. The strong-`H` active gate exactly removes `C^H` and all other promoted traces except `(P_new,D)`. Those two designated channels may then overlap until a late terminal gate adjacent to the reset face; the terminal gate exactly removes the only two promoted descendants `(H,M)`, after which the parent supports are separated.

This construction uses no new lattice generator: `C^{ent}` and `C^H` have the same lattice character. The source formalization explicitly keeps the label carrier independent of harmonic index, while the translated auxiliary-rectangle lemma permits a finite family of prescribed overlap supernodes. The finite extension of the already proved two-collar zero-residual reduction then yields one exact correction problem across the three collars and transport segments.

The theorem closes **one corrected active cell with a finite support bank**. It does not yet prove that the outgoing `D` packet regenerates the same two-copy catalyst support bank required by the next cell. That stronger support-bank renewal problem is the next autonomous-cascade frontier.

## 1. Numerical/collar geometry

Freeze

\[
u=2.5,
\qquad
\delta=0.1375,
\qquad
x=0.7779445026067248271\ldots.
\]

Let

\[
t_*=0.2251291169828679798\ldots,
\qquad
T=0.275.
\]

Choose the three active collars

\[
\boxed{I_{ent}=[0,0.001],}
\tag{FB1}
\]

\[
\boxed{I_H=[t_*-0.001,t_*+0.001],}
\tag{FB2}
\]

and, using `beta21_corrected_late_terminal_relocation.md`,

\[
\boxed{I_{term}=[T-0.003,T-0.001]=[0.272,0.274].}
\tag{FB3}
\]

These collars are pairwise disjoint with fixed positive normalized gaps.

The designated reduced slopes relevant to the transported `D` and the two active gates remain strictly inside the raw source pulse interval. In particular,

\[
z_D(0)=x-\delta=0.6404445\ldots,
\]

\[
z_D(t_*)=x-\delta+t_*=0.8655736\ldots,
\]

and

\[
z_D(T)=x+\delta=0.9154445\ldots.
\tag{FB4}
\]

Thus the generated unit-beta child never approaches a pulse endpoint during the finite cell.

## 2. Source support facts used

Two exact source-geometry facts are used.

### 2.1 Harmonic index does not change the label carrier

The formalized source file `NavierStokes/ActualInitialExcluded.lean` defines the original label's slow mask and Gaussian source rectangle on the common torus lift and states explicitly that **the harmonic index does not change this set**. Therefore correction/descendant harmonics attached to one label remain supported inside the same broad label carrier.

This is precisely what is needed to transport the entrance-generated `D` harmonic through the middle segment without inventing a new spatial-frequency generator.

### 2.2 Finite translated overlap supernodes

`translated_async_overlap.md` proves that a finite family of label rectangles can be assigned prescribed affine pulse coordinates at a common physical auxiliary point and that generic center choices preserve disjointness of distinct non-designated supernodes.

Consequently a finite number of copies of the **same Fourier character** can be placed at different auxiliary centers. Such copies enlarge the support-label bank but do not enlarge the rank-two Fourier lattice.

## 3. Catalyst bank

Represent the incoming catalyst character by two support labels

\[
\boxed{C^{ent},\ C^H}
\tag{FB5}
\]

with identical phase character, beta weight and principal polarization, but different auxiliary centers.

Their support geometry is chosen so that:

1. `C^{ent}` overlaps the incoming parent/control bank only on `I_ent`;
2. `C^{ent}` has no common support with the transported designated `D` after the entrance exit;
3. `C^H` is disjoint from the entrance supernode and from the transported `D` before `I_H`;
4. `C^H` overlaps `D` exactly on the designated strong-`H` supernode `I_H`;
5. after the strong-`H` exit the exact amplitude of `C^H` is zero, so it cannot participate in any later leading collision.

All these are finite support-incidence requirements. The translated-rectangle construction supplies the required center freedom after the three fixed collar widths are chosen sufficiently small.

No additional Fourier character is introduced because

\[
\operatorname{char}(C^{ent})
=
\operatorname{char}(C^H)
=C.
\tag{FB6}

## 4. Entrance active exit

On `I_ent`, use `beta21_corrected_entrance_four_control_C1_closure.md` with the catalyst copy `C^{ent}`. The exact gate gives

\[
\boxed{
(D,M,H,R_3)_{I_{ent},out}
=(D_*,0,0,0),
\qquad D_*\ne0.
}
\tag{FB7}

The old parent is not needed later and its support is routed away from all subsequent designated collisions.

The catalyst copy `C^{ent}` also leaves the designated support circuit at this point. Hence the passive-collar recursion obstruction cannot restart after the entrance exit: the exact forbidden traces are zero and the old entrance catalyst support is absent.

## 5. Middle transport of the generated child

The designated `D` harmonic is generated on the entrance carrier and then evolved forward through the middle segment

\[
J_1=[0.001,t_*-0.001].
\]

Because no designated catalyst support intersects it on the interior of `J_1`, the dangerous `C+D` collision algebra is absent there.

The full correction problem is nevertheless evolved, not reset by hand. The finite-stage source-localized action theorem and the exact nonzero/mean forward machinery imply polynomial envelope-renormalized transport bounds on a segment of length `O(S_*)`, exactly as in `two_collar_zero_residual_reduction.md`.

Thus the designated child arrives at the strong-`H` collar with a nonzero compact normalized amplitude, while all non-designated remainder terms remain in the action-subcritical/stable correction class.

## 6. Strong-`H` active exit

On `I_H`, the transported `D` meets only the late catalyst copy `C^H` among the leading beta-one catalyst labels.

Apply `beta21_corrected_strong_H_nine_control_C1_closure.md`. The exact output is

\[
\boxed{
(C^H,M,P,H,2D+C,D+2C,2C-D,P_{new},3D+C)_{out}
=(0,0,0,0,0,0,0,P_H,0),
}
\tag{FB8}

with `P_H != 0` and `D` retained nonzero.

Hence every source-promoted character above the target layer other than the designated pair `(P_new,D)` is zero at the strong-`H` exit.

This is exactly the active-exit mechanism missing in `passive_five_collar_recursion_obstruction.md`.

## 7. Post-strong-`H` designated interval

On

\[
J_2=[t_*+0.001,T-0.003]
\]

the designated pair `(P_new,D)` is allowed to coexist. The full propagated-action audit in `beta21_corrected_terminal_three_control_C1_closure.md` proves that the **only** new source-promoted characters above the renewed parent target are

\[
H=P_{new}-D,
\qquad
M=P_{new}-2D.
\tag{FB9}

Every other descendant has a fixed negative reset-face action gap.

Therefore this segment has a finite designated extension `(P_new,D,H,M)` and an infinite stable/action-subcritical complement. No uncontrolled infinite critical family is introduced by allowing this overlap.

## 8. Last-overlap terminal gate

Place the relocated terminal gate on `I_term`. By `beta21_corrected_late_terminal_relocation.md`, the exact output satisfies

\[
\boxed{
(P_{new},H,M)_{out}
=(P_*,0,0),
}
\tag{FB10}

with `D` retained nonzero.

Choose the support geometry so that `I_term` is the **last common support interval** of `P_new` and `D`. For

\[
T-0.001<t\le T
\]

their prescribed support labels are disjoint.

Hence after the exact exit condition (FB10), the quadratic sources for both `H` and `M` vanish identically on the final segment. They cannot be regenerated before the reset face.

The designated pair propagates homogeneously to `T`, where

\[
\boxed{
(z_{P_{new}},z_D)_T=(x,x+\delta).
}
\tag{FB11}

## 9. One exact correction problem across the finite circuit

The exact local gates are not patched as unrelated solutions. Treat the union

\[
I_{ent}\cup J_1\cup I_H\cup J_2\cup I_{term}\cup[T-0.001,T]
\]

as one forward phase-adapted correction problem with a finite designated state that changes only at the declared active collars.

The argument of `two_collar_zero_residual_reduction.md` extends verbatim to a fixed finite number of collars:

- every transport segment has at most `O(S_*)` normalized length;
- finite critical propagators have design-dependent bounded/polynomial envelope-normalized transfer;
- the infinite stable complement has the existing uniform inverse/smoothing;
- every omitted genealogy has either a fixed negative action gap or belongs to the stable complement;
- the mean return factors retain positive powers of `epsilon`;
- multiplying by any fixed power of `S_*` does not destroy these small factors;
- finite control parameter differentiation leaves all source exponents unchanged.

Thus the complete finite circuit has one unique exact nonzero/mean correction depending `C^1` on the finite gate controls.

The separate local Jacobians are block-causal because later controls do not affect earlier exit traces. Their diagonal blocks are precisely the already proved invertible entrance, strong-`H`, and terminal Jacobians. Therefore the full finite control Jacobian is block lower triangular with nonzero determinant.

Consequently the three local exact targets can be imposed simultaneously in one exact zero-residual cell.

## 10. Amplitude and phase return

Apply `beta21_corrected_active_cell_amplitude_transversality.md`. The entrance target amplitude and terminal controls can be chosen so that

\[
\boxed{
(A_{P_{new}}^{out},A_D^{out})
=(A_P^{in},A_C^{in})
}
\tag{FB12}

for any input pair in the fixed nonzero amplitude neighborhood.

The two torus phase parameters reset the two generator phases exactly.

Thus this finite-bank cell returns the complete **two-generator Fourier state**: beta weights, slopes, actions, complex amplitudes and phases.

## 11. What has and has not been closed

### Closed for one finite-bank cell

The corrected construction now has, in one exact zero-residual finite circuit:

1. source-matched entrance generation of `D`;
2. active cancellation of entrance shortcut descendants;
3. transport of the physically generated child to a late designated collision;
4. active strong-`H` generation of `P_new` and exact removal of the late catalyst;
5. finite post-strong-`H` promoted dynamics;
6. a last-overlap terminal cancellation gate;
7. exact slope/action/amplitude/phase return of the two generator characters.

### Not closed

The input support state used two same-character catalyst copies,

\[
C^{ent},\ C^H.
\]

The present theorem returns the **Fourier generator state**, but it does not prove that the outgoing unit-beta packet `D` automatically reproduces the same two-copy support-label microstructure needed to run the next cell without any preloaded auxiliary packet bank.

Therefore

\[
\boxed{
\text{Fourier-state renewal is proved for the finite-bank cell,}
}
\]

but

\[
\boxed{
\text{self-replicating support-bank renewal remains open.}
}
\tag{FB13}

Equivalently, an infinite construction may still use a finite prearranged same-character support bank at each scale, provided the later global sparse-placement and initial-data summability theorem proves that all such packets belong to one smooth finite-energy initial datum. What is not yet proved is a stricter Markovian statement in which each cell dynamically regenerates all support labels required by the next one.

## 12. New frontier

There are now two legitimate continuation routes:

1. **prearranged finite-bank global route:** keep a fixed finite number of same-character auxiliary support labels per scale and prove infinite sparse placement, correction summability and recovery of one smooth finite-energy initial datum;
2. **strict autonomous-bank route:** enlarge the local renewal state to include the finite support-lobe amplitudes/locations and prove that the outgoing generated packets reproduce that entire bank.

The first route is sufficient for an unforced globally prearranged solution if the global assembly closes; the second is a stronger self-replication theorem.

No infinite cascade or unforced Navier--Stokes blowup theorem is claimed here.
