# Coupled angular-mean Gevrey contraction — RETRACTED DRAFT

**Status:** RETRACTED / DO NOT CITE AS A PROVED LOCAL CLOSURE THEOREM.

This file was written before the sharper radial audit in
`proofs/radial_gevrey_radius_loss_and_same_space_obstruction.md`.
That audit proves that the compact radial cutoff operator is stretched-exponentially small only **across a fixed Gevrey-radius gap**, while an unrestricted same-radius estimate

\[
\|A_ef\|_{G^s_L}\le\eta(M_r)\|f\|_{G^s_L},\qquad \eta(M_r)\to0,
\]

is false because of near-resonant torus modes.

Accordingly, the Banach contraction previously asserted here by treating the compact radial remainder as an `o(1)` operator on one fixed Gevrey space was premature.

The pieces of the former argument that remain valid are now separated into current files:

- `proofs/nonzero_mean_sensitivity.md` — quantitative mean/nonzero sensitivity;
- `proofs/mean_nonlinear_block_small_factor_audit.md` and `proofs/coupled_mean_block_small_factor_audit.md` — non-radial small factors;
- `proofs/radial_gevrey_radius_loss_and_same_space_obstruction.md` — the corrected compact radial estimate and obstruction;
- `proofs/radial_characteristic_forward_inverse.md` — exact one-sided radial inverse without derivative loss.

The current target is a **coupled temporal-radial characteristic input-output theorem** in which the compact radial boundary condition is removed and radial exit traces are carried as part of the outgoing state.

No exact local zero-force theorem is claimed by this file.