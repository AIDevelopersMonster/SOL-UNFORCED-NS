# Common characteristic Gevrey profile compatibility — corrected scope

**Status:** PROVED FOR THE FIXED PROFILE/NONRADIAL BLOCKS; DOES NOT REMOVE THE SAME-RADIUS RADIAL COMPACTIFICATION OBSTRUCTION.

This note records the part of the common-space program that survives the sharper radial audit in `radial_gevrey_radius_loss_and_same_space_obstruction.md`.

For every fixed `s>1`, all **finitely many fixed** local cutoffs and reserved bump profiles used by the frozen v0.8 relay may be chosen in one compactly supported Gevrey class. Finite sums, products, differentiation, translation, analytic coordinate changes, and finite-dimensional moment inversion preserve that class after finitely many preassigned radius losses.

In particular:

1. the five reserved profiles used by the Vandermonde moment map may be chosen Gevrey while preserving invertibility, since the exact finite moment matrix is an open perturbation of a Vandermonde matrix;
2. finite Gevrey partitions of unity may be used on the bounded local collar;
3. pressure/stress reconstruction maps that are ordinary fixed radial integral/differential operators are bounded between fixed Gevrey radii;
4. the temporal characteristic inverse `J_i` is bounded with no torus derivative loss;
5. the full nonzero forward propagator and the map `m -> z(m)` can be differentiated in the same finite characteristic/Gevrey calculus, because the coefficient family is fixed and the angular high-mode smoothing estimate is unchanged;
6. polynomial and bilinear source remainders inherit Lipschitz difference estimates from their size estimates on a fixed small ball.

What this note **does not** prove is that the compact radial cutoff operator `A_e` is a small map on one and the same unrestricted Gevrey radius. The corrected radial theorem shows that

\[
\|A_ef\|_{G^s_{L_2}}
\le C e^{-cM_r^{1/(2s)}}\|f\|_{G^s_{L_0}},
\qquad L_2<L_0,
\]

but also gives near-resonant test modes excluding a uniform same-radius `o(1)` norm.

Therefore the fixed-profile compatibility issue is **not** the current obstruction. The remaining obstruction is the two-sided compact radial boundary condition itself.

The preferred exact-closure route is now `radial_characteristic_forward_inverse.md`: replace the compact radial inverse by a one-sided characteristic inverse, retain a radial exit trace as part of the outgoing relay state, and prove the coupled temporal-radial forward theorem.

This file must not be cited as closing the full angular mean by a same-space compact-radial Banach contraction.