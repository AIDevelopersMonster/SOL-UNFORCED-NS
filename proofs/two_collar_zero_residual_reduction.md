# Two-collar exact zero-residual reduction

**Status:** PROVED REDUCTION THEOREM. The two separated designated interaction collars plus the `O(S_*)` transport segment between them can be treated as one exact correction problem without introducing a new infinite-dimensional instability. What remains is a finite-dimensional designated amplitude-renewal map and the already-identified source-chart audit. This note does **not** claim that the renewal map is the identity or that an infinite autonomous cascade is closed.

## 1. Geometry of one renewal cell

Freeze one sufficiently large v0.8 design integer `M`. Let the first designated collar be centered at

\[
\theta=0,
\]

and the beta-two renewal collar at

\[
\theta=\theta_M^{\rm ren}\in(0.16,0.19).
\]

Choose fixed normalized half-width `delta_c>0` small enough that

\[
I_1=[-\delta_c,\delta_c],
\qquad
I_2=[\theta_M^{\rm ren}-\delta_c,\theta_M^{\rm ren}+\delta_c]
\]

are disjoint and lie inside the common translated source rectangles. In the source pulse variable `v`, these have bounded physical widths after the local collar rescaling, while their centers are separated by

\[
\Delta v_M=\theta_M^{\rm ren}L_s\asymp S_*.
\]

Let

\[
J=[\delta_c,\theta_M^{\rm ren}-\delta_c]
\]

be the middle transport segment.

## 2. Designated and remainder splitting

Write the coefficient state as

\[
U=U_{\rm des}+Z,
\]

where `U_des` contains only the finite designated channels required by the two-event cell:

- beta-two parent `P_2`;
- unit-beta catalyst `C_1`;
- unit-beta first-event child `D_1`;
- beta-two renewal output `R_2`.

All other nonzero harmonics, including sum/difference sidebands of the second event and every descendant of them, are included in `Z_nz`. The angular mean correction is `m`.

Thus

\[
Z=(Z_{nz},m).
\]

The nonzero lattice is still the same two-generator integer lattice; adding the child as a named designated channel does not create a third independent frequency generator because

\[
D_1=P_2-C_1.
\]

Likewise the renewal output satisfies

\[
R_2=C_1+D_1=P_2.
\]

Hence no increase of lattice rank occurs in the two-event cell.

## 3. Middle-segment nonzero control

`v08_post_child_feedback_action_filter.md` proves on the full interval from the first event to the renewal event that every non-designated principal-growing descendant of the surviving pair has a fixed negative action deficit

\[
S_\nu-\mathcal E_\nu\le-\delta_{fb}<0.
\]

Therefore, after factoring out the exact homogeneous source envelope of each mode, every principal-growing non-designated mode carries

\[
O(S_*^C e^{-c_MS_*}).
\]

Every principal-decaying mode lies in the stable complement of `finite_critical_block_uniform_stable_inverse.md`, with quadratic high-mode damping. The analytic convolution theorem `analytic_quadratic_symbol_bound.md` then gives a bounded nonlinear stable-complement map.

Consequently the long middle segment `J` does **not** produce an `exp(+cS_*)` loss in the renormalized packet norm. Its non-designated input-output operator satisfies

\[
\boxed{
\|\mathcal V_J^{\rm rem}f\|_{\mathfrak A_\sigma}
\le C_M S_*^{C_M}\|f\|_{\mathfrak A_\sigma}
}
\tag{TC1}
\]

with polynomial loss only, and any forcing carrying a positive epsilon power or fixed action deficit remains small as `ell->infinity`.

The estimate is in the source envelope-renormalized packet norm; it is **not** an unweighted physical Sobolev propagator bound across an interval of length `O(S_*)`.

## 4. Mean block across the full cell

The whole-space mean equation is forward in physical time after Leray elimination. Its nonlinear Lipschitz factors are

\[
\varepsilon^{9/50-2\kappa_s},
\qquad
\varepsilon^{1/2-\kappa_s},
\qquad
\varepsilon^{1-2\kappa_s},
\qquad
\rho_\ell.
\]

The only new issue in passing from one collar to the two-collar cell is the larger normalized interval. A polynomial factor in `S_*` multiplying any of these quantities is harmless because

\[
S_*^C\varepsilon^\delta\to0
\]

for every fixed `delta>0` in the source hierarchy.

Thus, after increasing the starting level if necessary, the same Banach ball argument used in `coupled_phase_adapted_local_zero_residual_theorem.md` gives a unique mean correction **conditional on the finite designated amplitudes** throughout `I_1 union J union I_2`:

\[
\boxed{
m=m(A_{des}),
\qquad
\|m\|\le C_M S_*^C\varepsilon^{1-\kappa_s}.}
\tag{TC2}
\]

Likewise the nonzero remainder is uniquely determined:

\[
\boxed{
Z_{nz}=Z_{nz}(A_{des}),
\qquad
\|Z_{nz}\|\le C_M\bigl(S_*^C\varepsilon^{1/5}+S_*^Ce^{-c_MS_*}\bigr).}
\tag{TC3}
\]

The dependence on the finite designated amplitude vector is locally Lipschitz.

## 5. Finite designated amplitude map

Let

\[
A_{in}=(A_2,A_1)
\]

be the normalized amplitudes of the beta-two parent and unit-beta catalyst entering the first collar. Solving the exact remainder and mean equations conditional on `A_in`, then passing through the first collar, middle transport, and renewal collar, defines a finite-dimensional outgoing map

\[
\boxed{
\mathscr R_\ell:\mathbb C^2\to\mathbb C^2,
\qquad
A_{out}=\mathscr R_\ell(A_{in}).}
\tag{TC4}
\]

The two components of `A_out` are:

1. the surviving/generated unit-beta channel;
2. the regenerated beta-two channel.

The principal calculations `v08_designated_projection_nonvanishing.md` and `v08_beta2_feedback_renewal.md` imply that the two relevant quadratic coefficients are nonzero. Therefore the Jacobian of the *principal truncated* renewal map is not identically zero.

All exact correction terms perturb the map by

\[
\boxed{
\mathscr R_\ell
=\mathscr R_0+\mathcal E_\ell,
\qquad
\|\mathcal E_\ell\|_{C^1(K)}
\le C_{M,K}S_*^C\varepsilon^{\delta_*}
}
\tag{TC5}
\]

on each fixed compact amplitude set `K`, for some positive source exponent `delta_*`. Here `mathscr R_0` is the finite principal two-event amplitude map.

Thus the full exact PDE cell has been reduced to the finite problem of finding an amplitude normalization/fixed ray for `mathscr R_0` that persists under the `C^1`-small perturbation (TC5).

## 6. What has been eliminated

The following are **not** additional obstructions for the two-collar cell:

- growth of the number of independent lattice generators;
- infinitely many new unstable harmonics on the middle segment;
- whole-space pressure nonlocality;
- an `O(S_*)` exponential loss for non-designated packet modes in the envelope-renormalized norm;
- the angular mean as a separate unsolved PDE block.

They are absorbed by the existing lattice, action, Leray and mean fixed-point machinery.

## 7. Sharp remaining finite problem

The next theorem is now finite-dimensional:

\[
\boxed{
\textbf{principal two-event amplitude renewal fixed-ray theorem.}
}
\]

One must compute the leading map

\[
\mathscr R_0(A_2,A_1)
\]

including the exact normalization of both designated quadratic projections and the linear homogeneous transport between the two collars, then prove the existence of a nonzero vector `A_*` and scalar `lambda_*!=0` such that

\[
\boxed{
\mathscr R_0(A_*)=\lambda_* A_*.
}
\tag{TC6}
\]

For an autonomous scale-repeatable cell one further needs the normalized magnitude of `lambda_*` to be compensable by the fixed q-step transport, ideally `|lambda_*|=1` after using one available amplitude/phase parameter.

This finite amplitude recurrence is the current bottleneck. Until it is solved, an infinite exact unforced relay chain is not proved.