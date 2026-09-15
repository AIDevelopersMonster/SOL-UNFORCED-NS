# Correction: the full control-profile renewal map is not yet canonically defined

**Status:** CLAIM-DISCIPLINE CORRECTION / SHARP FRONTIER RESET. The reduction `control_profile_bank_finite_state_reduction.md` correctly observed that only finitely many localized profile parameters occur in one corrected cell. However Sections CP3--CP8 implicitly treated those local gate parameters as if the exact PDE cell already supplied canonical **output profile coordinates** of the same type. The existing gate theorems do not yet provide such output coordinates.

They provide finite maps

\[
p\longmapsto \text{scalar exit traces},
\]

not a canonical map

\[
\text{incoming localized profile vector}
\longmapsto
\text{outgoing localized profile vector}.
\]

Therefore the abstract full-profile map `F_ell` / `R_ell` in that note should be regarded as a **target construction**, not as an already-defined theorem object.

This correction does not reopen the scalar gate ranks, catalyst-carrier renewal, or two-channel Fourier renewal. It only prevents a premature fixed-point argument on coordinates that have not yet been physically defined at the cell output.

## 1. What the exact gate theorems actually define

The corrected entrance theorem uses four localized control amplitudes and proves local surjectivity of

\[
\mathcal G^{ent}_\ell(p)
=(D,M,H,R_3)_{out}.
\]

The strong-`H` theorem uses nine localized amplitudes and proves local surjectivity of

\[
\mathcal G^H_\ell(p)
=(C,M,P,H,2D+C,D+2C,2C-D,P_{new},3D+C)_{out}.
\]

The terminal theorem uses three localized amplitudes and proves local surjectivity of

\[
\mathcal G^{term}_\ell(p)
=(P_{new},H,M)_{out}.
\]

In each case the `p_j` are **input coordinates used to achieve an exit target**. The theorem does not define an outgoing family `p'_j` whose shapes and centers are canonically the renewed controls of the next cell.

Hence a fixed-point equation

\[
\mathscr R_0(p)=p
\]

is not meaningful until those outgoing coordinates are defined by physical observables.

## 2. New unit-beta control simplification

Two replacement theorems remove the mixed-character part of this problem:

- `beta21_corrected_entrance_four_C_control_rank.md` replaces the four entrance beta-two controls by four unit-beta `C` controls;
- `beta21_corrected_terminal_three_D_control_rank.md` replaces the three terminal beta-two controls by three unit-beta `D` controls.

The strong-`H` gate already uses unit-beta `C` controls.

Therefore every finite active control in the corrected cell may now be chosen in the **single unit-beta character sector**:

\[
\boxed{
\text{entrance: }C,
\qquad
\text{strong-H: }C,
\qquad
\text{terminal: }D\sim C_{next}.
}
\tag{CM1}
\]

This is a genuine structural strengthening: no autonomous renewal theorem for a separate beta-two control-profile bank is needed.

## 3. Correct state object: physical unit-beta lobes

The next profile state must be defined by **physical outgoing observables**, not by reusing the names of the local control parameters.

A natural candidate is a finite family of support-separated unit-beta lobes

\[
\boxed{
\mathcal L
=(L_1,\ldots,L_N),
}
\tag{CM2}
\]

where each `L_j` is a physical unit-beta packet with

1. a prescribed support label/center class;
2. a normalized complex amplitude/phase observable;
3. a fixed source-cone/polarization margin;
4. enough finite profile moments to ensure the translated-profile control ranks used by the three gates.

The renewal problem is then to prove that one cell produces an outgoing lobe family

\[
\mathcal L_{out}
\]

which again belongs to the same admissible finite lobe class and has the same cardinality.

Only after this physical lobe map is defined may one ask for a fixed point, fixed ray, invariant compact set, or infinite orbit.

## 4. Why literal lobe renewal is preferable

A lobe output can be read directly from the PDE field by support localization and projection onto the designated unit-beta harmonic. It is therefore a genuine observable.

By contrast, a local Jacobian parameter is a coordinate on the chosen approximate-field family; without an explicit output-identification theorem it is not a renewed physical state variable.

Thus the corrected logical order is

\[
\boxed{
\text{gate controls}
\to
\text{physical output lobes}
\to
\text{lobe renewal map}
\to
\text{autonomous iteration}.
}
\tag{CM3}

## 5. Reserve-lane observation

A second simplification is available. Not every lobe-generation lane must satisfy the full exact active-exit cancellation conditions. Exact cancellation is required only for packets that will participate in a later designated overlap on the singular relay spine.

A reserve child may be generated forward by a source-matched collision and routed into a support corridor disjoint from all future designated supernodes. Its finite side products remain part of the exact global solution but need not be included in the next relay state, provided their global norm is summable and they never re-enter the relay support circuit.

This suggests a finite lobe-bank renewal architecture with:

- a small number of **clean active lanes** governed by the exact gate theorems;
- additional **dirty reserve lanes** used only to replenish the unit-beta lobe bank;
- geometric routing of their side products away from the trapped relay spine.

The next quantitative obligation is the norm/summability theorem for the routed-away reserve waste.

## 6. Revised frontier

The sharp next tasks are now:

1. prove a physical-energy/smooth-norm summability bound for finitely many routed-away reserve descendants per scale;
2. define a fixed finite unit-beta lobe class by explicit physical observables;
3. prove that the doubled/finite entrance architecture produces enough outgoing unit-beta lobes to restore that class with no cardinality growth;
4. only then define the full lobe renewal map and study its autonomous infinite iteration.

No fixed point of a full profile map is currently claimed.
