# Coupled phase-adapted local zero-residual theorem

**Status:** PROVED LOCAL WHOLE-SPACE ZERO-RESIDUAL FIXED POINT ON ONE FROZEN RELAY COLLAR, IN THE PHASE-ADAPTED COEFFICIENT REALIZATION. THIS IS NOT YET AN INFINITE RELAY / BLOWUP THEOREM.

This note combines the exact nonzero forward map, the quantitative mean sensitivity estimate, the exact signed-stress Lipschitz gain, the whole-space Leray--Oseen estimate, and `phase_adapted_whole_space_leray_intertwining.md` into one Banach fixed point on a single frozen relay collar.

The remaining post-local issue is physical-scale inheritance: whether the noncompact whole-space mean/pressure tail produced by one exact relay lies in an outgoing class that can be passed to the next relay scale and summed across an infinite cascade.

## 1. Phase-adapted mean space

For auxiliary index `k in Z^2`, let

\[
M_{\ell,k}f=e^{i\theta_{\ell,k}}f,
\qquad
\theta_{\ell,k}=2\pi k\cdot\Phi_\ell.
\]

At one fixed integer `m_0>=6`, define

\[
\boxed{
\|m\|_{\mathfrak M_{\sigma,m_0}}
:=\sum_{k\in\mathbb Z^2}
 e^{\sigma|k|_1}
 \|M_{\ell,k}m_k\|_{H^{m_0}(\mathbb R^3)}.
}
\tag{CL1}
\]

By `phase_adapted_whole_space_leray_intertwining.md`, the induced coefficient Leray projector obeys

\[
\boxed{
\|\mathbb P_{\rm coeff,\ell}m\|_{\mathfrak M_{\sigma,m_0}}
\le \|m\|_{\mathfrak M_{\sigma,m_0}},
}
\tag{CL2}
\]

and physical reconstruction exactly intertwines the projectors.

The phase-addition identity also gives the Banach algebra estimate

\[
\boxed{
\|fg\|_{\mathfrak M_{\sigma,m_0}}
\le C_{m_0}
\|f\|_{\mathfrak M_{\sigma,m_0}}
\|g\|_{\mathfrak M_{\sigma,m_0}}.
}
\tag{CL3}
\]

Thus no WKB or low-frequency split is needed in the coupled mean equation.

## 2. Exact coefficient form of physical differentiation

On the `k`th mode,

\[
M_{\ell,k}^{-1}\partial_j M_{\ell,k}
=\partial_j+i\partial_j\theta_{\ell,k},
\tag{CL4}
\]

and similarly for the physical-time derivative,

\[
\boxed{
M_{\ell,k}^{-1}\partial_s M_{\ell,k}
=\partial_s+i\partial_s\theta_{\ell,k}.
}
\tag{CL5}
\]

Consequently the complete physical Navier--Stokes operator, including transport, viscosity, pressure projection, and time dependence of the phases, has an exact coefficient representation obtained by conjugation mode by mode. There is no unrecorded derivative of the oscillatory phase: every such term is one of the characteristic coefficient derivatives already used by the source packet calculus.

For finite auxiliary Fourier sums,

\[
\boxed{
\mathcal N_{\rm phys}(\mathcal R_\ell U)
=\mathcal R_\ell\mathcal N_{\rm coeff,\ell}(U),
}
\tag{CL6}
\]

where `N_phys` denotes the projected Navier--Stokes residual. By the weighted `l^1` convergence and fixed-order product estimates, (CL6) extends to the completion of the coefficient space.

## 3. Nonzero block conditional on the mean

Let `X` denote the nonzero-harmonic packet space of `nonzero_harmonic_forward_reduction.md`. For every mean input in a sufficiently small ball of `mathfrak M_{sigma,m0}`, the exact forward nonzero problem has a unique solution

\[
\boxed{z=z(m)}
\tag{CL7}
\]

with

\[
\boxed{
\|z(m)\|_X\le C_{M,I}\rho_\ell,
}
\tag{CL8}
\]

and

\[
\boxed{
\|z(m)-z(\widetilde m)\|_X
\le C_{M,I}\|m-\widetilde m\|_{\mathfrak M_{\sigma,m_0}}.
}
\tag{CL9}
\]

The local core use of the global mean is legitimate because every designated/nonzero packet is supported in a fixed compact relay core. A fixed cutoff equal to one near that core leaves all mixed terms with the packet unchanged and is bounded in the phase-adapted fixed-order norm.

## 4. Mean equation after substituting the exact nonzero solve

Substitute (CL7) into the exact angular-mean equation and eliminate pressure with the coefficient Leray projector. Let

\[
\mathcal V_{\rm mean}(s,\tau)
\]

be the phase-adapted conjugate of the whole-space Leray--Oseen propagator. The physical estimate and exact conjugation give

\[
\boxed{
\|\mathcal V_{\rm mean}(s,\tau)f\|_{\mathfrak M_{\sigma,m_0}}
\le K_{M,I,m_0}\|f\|_{\mathfrak M_{\sigma,m_0}}.
}
\tag{CL10}
\]

Define

\[
\boxed{
\mathcal T_\ell(m)(s)
=\int_{s_-}^{s}
\mathcal V_{\rm mean}(s,\tau)
\left[
F_{\rm in,\ell}
+\mathcal F_{\rm nl,\ell}(m,z(m))
\right](\tau)d\tau.
}
\tag{CL11}
\]

The inhomogeneous forcing estimate is

\[
\boxed{
\|F_{\rm in,\ell}\|_{L^\infty\mathfrak M_{\sigma,m_0}}
\le C_MS_*^C\varepsilon^{1-\kappa_s}.
}
\tag{CL12}
\]

The weighted coefficient norm causes no additional epsilon loss: the fixed designated modes contribute finite lattice weight, while the nonzero correction is already controlled in an exponentially weighted lattice norm.

## 5. Exact Lipschitz small factor

There are four relevant nonlinear difference classes.

The signed-stress block now has the exact gain

\[
\boxed{
\varepsilon^{9/50-2\kappa_s}.
}
\tag{CL13}
\]

The mean-to-wave-to-covariance return has gain

\[
\boxed{
\varepsilon^{1/2-\kappa_s}+\rho_\ell.
}
\tag{CL14}
\]

The temporal/viscous reconstruction remainders gain at least

\[
\boxed{
\varepsilon^{1-2\kappa_s},
}
\tag{CL15}
\]

and the purely quadratic mean difference contributes `O(r_ell)` on a ball of radius `r_ell`.

Therefore

\[
\boxed{
\|\mathcal T_\ell(m)-\mathcal T_\ell(\widetilde m)\|
\le q_\ell
\|m-\widetilde m\|,
}
\tag{CL16}
\]

where

\[
\boxed{
q_\ell
\le C_{M,I,m_0}S_*^C
\left[
\varepsilon^{9/50-2\kappa_s}
+\varepsilon^{1/2-\kappa_s}
+\varepsilon^{1-2\kappa_s}
+\rho_\ell
+r_\ell
\right].
}
\tag{CL17}
\]

Since `kappa_s=10^{-5}` and

\[
\rho_\ell\lesssim S_*^C\varepsilon^{1/5}+S_*^Ce^{-c_MS_*},
\]

we have

\[
\boxed{q_\ell\to0.}
\tag{CL18}
\]

## 6. Self-map radius

From (CL10)--(CL12),

\[
\|\mathcal T_\ell(0)\|
\le K_{M,I,m_0}|I|C_MS_*^C\varepsilon^{1-\kappa_s}.
\tag{CL19}
\]

Choose

\[
\boxed{
r_\ell
=2K_{M,I,m_0}|I|C_MS_*^C\varepsilon^{1-\kappa_s}.
}
\tag{CL20}
\]

Then `r_ell -> 0`. For all sufficiently large `ell`, (CL18) gives `q_ell<=1/2`, and hence

\[
\|\mathcal T_\ell(m)\|
\le \frac12r_\ell+\frac12r_\ell=r_\ell
\tag{CL21}
\]

on the closed ball `B_{r_ell}`.

Banach's theorem therefore gives a unique

\[
\boxed{
m_\ell\in B_{r_ell}\subset C(I;\mathfrak M_{\sigma,m_0})
}
\tag{CL22}
\]

with

\[
\boxed{
m_\ell=\mathcal T_\ell(m_\ell),
\qquad
\|m_\ell\|
=O(S_*^C\varepsilon^{1-\kappa_s}).
}
\tag{CL23}
\]

Set

\[
\boxed{z_\ell=z(m_\ell).}
\tag{CL24}
\]

## 7. Exact local residual statement

The nonzero theorem makes every nonzero angular harmonic of the coefficient residual vanish. The fixed point (CL22) makes the angular-mean coefficient residual vanish. Therefore

\[
\boxed{
\mathcal N_{\rm coeff,\ell}(U_{\rm relay}+m_\ell+z_\ell)=0
}
\tag{CL25}
\]

on the frozen relay time collar.

By the exact reconstruction identity (CL6),

\[
\boxed{
\mathcal N_{\rm phys}
\left(
\mathcal R_\ell(U_{\rm relay}+m_\ell+z_\ell)
\right)=0
}
\tag{CL26}
\]

as a physical whole-space projected Navier--Stokes equation on that time collar, with pressure recovered by the whole-space elliptic projector.

Thus the **single-relay local zero-force closure is complete in the phase-adapted realization**.

## 8. What this theorem does not claim

Equation (CL26) is a local-in-time, one-relay statement. It does not prove that infinitely many such relays can be nested while preserving all hypotheses. In particular it does not yet prove:

1. that the whole-space mean/pressure tail from relay `ell` is in the admissible incoming class at relay `ell+1`;
2. that the tails from infinitely many relays are summable in the physical norm needed away from the singular time;
3. that the v0.8 action gap and designated projection survive the inherited low-frequency background from all previous relays;
4. that a global smooth finite-energy initial datum is obtained;
5. finite-time blowup for the unforced three-dimensional Navier--Stokes equations.

Those are physical-scale inheritance/global assembly obligations.

## 9. Publication threshold

This theorem crosses a **local-method publication threshold**: the branch now contains a coherent exact one-relay zero-force closure theorem, including the pressure/nonzero/mean interface, after correcting two failed radial pressure routes.

It does **not** cross the threshold for a paper claiming the Millennium problem or an unforced blowup theorem. A defensible first paper may now be prepared around the local theorem and the pressure-architecture correction, provided the proof is independently line-audited against the exact source chart definitions and every source-dependent estimate is pinned to exact equation/proposition references.

The main research frontier is now

\[
\boxed{\textbf{physical-scale inheritance of the whole-space mean/pressure tail.}}
\]
