# Corrected entrance rank from four unit-beta `C` controls

**Status:** PROVED PRINCIPAL/FROZEN RANK REPLACEMENT THEOREM; EXACT `C^1` PERSISTENCE FOLLOWS BY THE SAME FINITE-PARAMETER ARGUMENT AS THE EXISTING ENTRANCE THEOREM. The four same-character beta-two `P` controls used in `beta21_corrected_entrance_four_control_C1_closure.md` are not structurally necessary. The corrected entrance block can instead be driven by four localized copies of the already-present unit-beta catalyst character `C`.

This replacement matters globally: together with `beta21_corrected_terminal_three_D_control_rank.md`, **every finite active control in the corrected cell may be taken on the single unit-beta character that is already forward-renewed by the catalyst-bank mechanism.**

The theorem below is a rank theorem plus source-class realization. The exact zero-residual persistence is the same parameter-differentiation step already proved for the original four-control entrance gate; no new PDE inverse is introduced.

## 1. Corrected entrance block

At

\[
u=2.5,
\qquad
\delta=0.1375,
\qquad
x=0.7779445026067248271\ldots,
\]

use the entrance genealogy

\[
P-C\to D,
\qquad
D-C\to M,
\qquad
M+D\to H,
\qquad
H+M\to R_3,
\]

where

\[
M=D-C,
\qquad
H=2D-C,
\qquad
R_3=3D-2C.
\]

The controlled output is

\[
X=(D,M,H,R_3).
\]

The already audited principal margins at the collar center are

\[
|\kappa_{P-C\to D}|\approx1.24743,
\]

\[
\|b_{D-C\to M}\|\approx4.02999,
\]

\[
|\kappa_{M+D\to H}|\approx7.09993,
\]

\[
|\kappa_{H+M\to R_3}|\approx6.55990,
\]

and the same positive margins persist on the fixed entrance collar

\[
0\le t\le10^{-3}.
\]

## 2. Replace the beta-two control by a catalyst control

Perturb the physically present catalyst by one localized same-character profile,

\[
C\mapsto C+p\,C_{ctrl}.
\]

Linearization of the first difference event gives the direct source

\[
P-C_{ctrl}\to D.
\]

Because the difference coefficient is nonzero, the action-normalized control vector has a nonzero first coordinate:

\[
\boxed{
B=b_0e_D+b_1e_M+b_2e_H+b_3e_{R_3},
\qquad b_0\ne0.
}
\tag{EC1}
\]

The lower components are allowed. They collect simultaneous shorter responses of the same catalyst perturbation against already-present/generated fields. No vanishing assumption on `b_1,b_2,b_3` is needed.

## 3. Integrating-factor triangular form

Use the same action/integrating-factor normalization as in the existing entrance theorem. The frozen leading operator is lower triangular with the homogeneous diagonal removed and with nonzero first subdiagonal

\[
A_{M,D}=c_1\ne0,
\qquad
A_{H,M}=c_2\ne0,
\qquad
A_{R_3,H}=c_3\ne0.
\tag{EC2}
\]

Entries farther below the first subdiagonal are unrestricted.

This is exactly the algebraic setting already proved in `beta21_second_gate_unrouted_ten_control_root_rank.md`: a control vector may have arbitrary lower components as long as its first pivot is nonzero.

For completeness, after successive elimination of the already-created pivot rows, the first new component of `A^kB` is

\[
b_0c_1\cdots c_k.
\]

Therefore

\[
\boxed{
\det[B,AB,A^2B,A^3B]
=b_0^4c_1^3c_2^2c_3\ne0.
}
\tag{EC3}

The direct lower responses of `C_{ctrl}` cannot cancel this pivot determinant.

## 4. Four translated `C` profiles

Choose one fixed smooth compact profile `q` of nonzero mass and four distinct translated centers inside the entrance collar. The usual moment/Vandermonde argument then gives a principal response matrix `J_{4,C}` with

\[
\boxed{
\det J_{4,C}
\propto
b_0^4c_1^3c_2^2c_3
\prod_{i<j}(\tau_j-\tau_i)
\ne0.
}
\tag{EC4}

For equal spacing the determinant has the same `Delta^6` law as the original four-control gate.

Because all edge coefficients stay uniformly separated from zero on the positive-width collar, slow coefficient variation preserves this rank.

## 5. Source realization

Every control profile has exactly the same beta-one lattice character, oscillatory phase and principal polarization as the existing catalyst `C`.

Hence:

1. no new lattice generator is introduced;
2. same-phase control-control principal self-interactions vanish by incompressibility;
3. finite smooth profile multiplication preserves the source wave classes;
4. curl reconstruction restores exact divergence freedom with only the already-audited lower-order remainder;
5. finite parameter differentiation changes only the fixed design constants.

Thus the replacement controls lie in the same admissible source classes as the `C` controls already used in the unrouted root and strong-`H` theorems.

## 6. Exact `C^1` persistence

Let

\[
\mathcal G^{ent,C}_\ell(p)
=(D,M,H,R_3)_{out},
\qquad p\in\mathbb C^4.
\]

The parameter-dependent nonzero/mean contraction estimates used in `beta21_corrected_entrance_four_control_C1_closure.md` depend only on:

- a fixed finite source-admissible profile family;
- bounded parameter derivatives;
- the positive future-action gap;
- a nonzero finite principal determinant.

All four properties hold for the present `C` family. Hence

\[
D_p\mathcal G^{ent,C}_\ell
=J_{4,C}+o(1)
\]

and for all sufficiently high levels the exact Jacobian remains invertible.

Consequently one may prescribe

\[
\boxed{
(D,M,H,R_3)_{out}
=(D_*,0,0,0),
\qquad D_*\ne0,
}
\tag{EC5}

using four localized unit-beta catalyst controls.

The base catalyst channel is retained in the same nonzero compact amplitude neighborhood as in the original entrance architecture; the localized control profiles are supported inside the entrance collar and need not introduce a new persistent beta-two control bank.

## 7. Global significance

The corrected entrance no longer requires independently renewed beta-two `P`-profile controls. Its finite control character is the same unit-beta character that becomes the outgoing `D` character after renewal.

Thus, after the terminal replacement theorem below, the complete control-character set reduces to

\[
\boxed{\{\beta=1\}\text{ only}.}
\]

This does not yet prove renewal of the full **profile shapes**. It removes the mixed-character profile-state obstruction and reduces the remaining autonomous support/profile question to a finite bank carried entirely by the self-renewing unit-beta sector.
