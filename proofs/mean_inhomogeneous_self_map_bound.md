# Inhomogeneous mean defect and fixed-point ball invariance

**Status:** PROVED SOURCE-EXPONENT SELF-MAP ESTIMATE FOR THE GLOBAL TIME-FORWARD MEAN EQUATION.

This note supplies the last purely local Banach estimate left by `global_fixed_order_leray_oseen_propagator.md`: the value of the Duhamel map at the origin is source-small. Together with the already-proved Lipschitz constant `q_ell -> 0`, this gives a unique global angular-mean correction on one relay time collar in the fixed-order Sobolev realization.

The theorem concerns the local-in-time mean equation coupled to the already exact nonzero forward solution. It does not yet assert physical-scale inheritance or an infinite relay chain.

## 1. Mean source at zero correction

Set the new angular mean correction to zero and let

\[
z_0:=z(0)
\]

be the exact nonzero forward correction supplied by `nonzero_harmonic_forward_reduction.md`.

The mean inhomogeneous forcing consists of four source types:

1. the covariance of the designated primary nonzero waves;
2. covariance terms containing at least one supported nonzero correction `z_0`;
3. the already-supported stage-zero mean residual/base-cutoff terms;
4. post-principal signed-stress and transport reconstruction remainders.

The primary designated wave has source order

\[
\boxed{W_{1/2}.}
\tag{MI1}
\]

The source zero-harmonic product law is

\[
\boxed{
W_\alpha\times W_{\alpha'}
\longrightarrow
M_{\alpha+\alpha'-\kappa_s}.
}
\tag{MI2}
\]

Therefore the largest unavoidable raw primary covariance has mean order

\[
\boxed{
M_{1-\kappa_s}.
}
\tag{MI3}
\]

At one fixed Sobolev order this gives

\[
\boxed{
\|F_{\rm prim,\ell}\|_{H^{m_0}}
\le C_MS_*^C\varepsilon^{1-\kappa_s}.
}
\tag{MI4}
\]

No inverse epsilon factor is introduced by the whole-space Leray projector.

## 2. Terms containing the exact nonzero correction

The nonzero forward theorem gives, in the primary-wave normalized packet norm,

\[
\boxed{
\|z_0\|\le C_{M,I}\rho_\ell,
}
\tag{MI5}
\]

where

\[
\boxed{
\rho_\ell
\lesssim
S_*^C\varepsilon^{1/5}
+S_*^Ce^{-c_MS_*}.
}
\tag{MI6}
\]

Thus pairing `z_0` with a primary `W_{1/2}` wave produces an additional factor `rho_ell` relative to (MI4):

\[
\boxed{
\|F_{\rm prim-z,\ell}\|_{H^{m_0}}
\le
C_MS_*^C\varepsilon^{1-\kappa_s}\rho_\ell.
}
\tag{MI7}
\]

The quadratic `z_0-z_0` covariance is smaller still:

\[
\boxed{
\|F_{z-z,\ell}\|_{H^{m_0}}
\le
C_MS_*^C\varepsilon^{1-\kappa_s}\rho_\ell^2.
}
\tag{MI8}
\]

The precise packet normalization may shift both sides by the same fixed primary scale; the key point is unchanged: every term containing `z_0` is strictly smaller than the raw primary covariance.

## 3. Supported stage-zero mean residual

The source initialization records

\[
C_0^*=1.2.
\tag{MI9}
\]

Hence the supported stage-zero mean residual belongs to a strictly higher epsilon order than (MI3):

\[
\boxed{
\|F_{\rm supp,\ell}\|_{H^{m_0}}
\le C_MS_*^C\varepsilon^{6/5}.
}
\tag{MI10}
\]

The v0.8 action-subcritical pieces additionally carry `e^{-c_MS_*}` and are harmless here.

## 4. Signed-stress and transport remainders

The signed-stress principal covariance is chosen to cancel the prescribed averaged stress target. Its post-principal remainder has the exact gain established in `signed_stress_lipschitz_gain_exact.md`:

\[
\boxed{
\delta_{\rm stress}=\frac9{50}-2\kappa_s>0.
}
\tag{MI11}
\]

Applied to a target of order at least `M_{1-kappa_s}`, it therefore contributes

\[
\boxed{
\|F_{\rm stress-rem,\ell}\|_{H^{m_0}}
\le
C_MS_*^C
\varepsilon^{1-\kappa_s+9/50-2\kappa_s}.
}
\tag{MI12}
\]

The temporal/viscous reconstruction remainders gain at least `1-2kappa_s` relative to their input target and are smaller than (MI4) as well.

## 5. Aggregate inhomogeneous forcing

Combining (MI4), (MI7), (MI8), (MI10), and (MI12), the full projected mean source at zero satisfies

\[
\boxed{
\|F_{\rm in,\ell}\|_{L^\infty(I;H^{m_0})}
\le
C_MS_*^C\varepsilon^{1-\kappa_s}
\left[1+O(\rho_\ell)+O(\varepsilon^{\delta_*})\right]
}
\tag{MI13}
\]

for some fixed `delta_*>0`.

In particular, after increasing the frozen design-dependent constant,

\[
\boxed{
\|F_{\rm in,\ell}\|_{L^\infty H^{m_0}}
\le
C_MS_*^C\varepsilon^{1-\kappa_s}
=:a_\ell,
\qquad a_\ell\to0.
}
\tag{MI14}
\]

## 6. Duhamel value at the origin

Let `V_ws` be the global mean propagator from `global_fixed_order_leray_oseen_propagator.md`. Define the nonlinear mean map

\[
\boxed{
\mathcal T_\ell(m)(s)
:=
\int_{s_-}^{s}
\mathcal V_{\rm ws}(s,\tau)
\left[
F_{\rm in,\ell}(\tau)
+\mathcal F_{\rm nl,\ell}(m)(\tau)
\right]d\tau.
}
\tag{MI15}
\]

Then

\[
\boxed{
\|\mathcal T_\ell(0)\|_{C(I;H^{m_0})}
\le
K_{M,I,m_0}|I|a_\ell.
}
\tag{MI16}
\]

Set

\[
\boxed{
r_\ell:=2K_{M,I,m_0}|I|a_\ell.}
\tag{MI17}
\]

Then `r_ell -> 0` and

\[
\boxed{
\|\mathcal T_\ell(0)\|\le r_\ell/2.
}
\tag{MI18}
\]

## 7. Ball invariance and contraction

The global propagator theorem and nonlinear block audit give

\[
\boxed{
\|\mathcal T_\ell(m)-\mathcal T_\ell(\widetilde m)\|
\le q_\ell\|m-\widetilde m\|,
\qquad q_\ell\to0.
}
\tag{MI19}
\]

Choose `ell` sufficiently large that

\[
q_\ell\le\frac12.
\tag{MI20}
\]

For `\|m\|\le r_\ell`,

\[
\|\mathcal T_\ell(m)\|
\le
\|\mathcal T_\ell(0)\|+q_\ell\|m\|
\le
\frac{r_\ell}{2}+\frac{r_\ell}{2}
=r_\ell.
\tag{MI21}
\]

Thus `T_ell` maps the closed ball `B_{r_ell}` into itself and is a strict contraction there.

Banach's fixed-point theorem gives a unique

\[
\boxed{
m_\ell\in C(I;H^{m_0})
}
\tag{MI22}
\]

satisfying

\[
\boxed{
m_\ell=\mathcal T_\ell(m_\ell),
\qquad
\|m_\ell\|\le r_\ell
=O\!\left(S_*^C\varepsilon^{1-\kappa_s}\right).
}
\tag{MI23}
\]

## 8. Coupling back to the nonzero block

Set

\[
\boxed{z_\ell:=z(m_\ell).}
\tag{MI24}
\]

By the exact nonzero forward theorem, `z_ell` solves every nonzero angular harmonic equation on the local relay collar. By (MI22), `m_ell` solves the projected whole-space angular mean equation.

Therefore, **at the level of the reduced physical mean/nonzero system represented in the branch**, the local time-forward zero-residual fixed point is closed.

## 9. What this does not yet prove

This theorem does not prove:

- that the reconstructed whole-space mean tail lies in exactly the same source localization class assumed in every coefficient-level nonzero estimate, rather than merely being small in global `H^{m_0}`;
- that the local corrected state can be handed to the next smaller physical scale with the v0.8 action geometry unchanged;
- that pressure/velocity tails from infinitely many relays remain summable;
- an infinite autonomous relay chain;
- finite-time blowup for unforced 3D Navier--Stokes.

The first item is now the final **local reconstruction/interface audit** before promoting (MI22)-(MI24) to a publication-level exact local whole-space relay theorem.

## 10. Immediate frontier

The next task is to prove a core-locality lemma:

> If `m_ell` is the small global Sobolev mean fixed point above and the designated/nonzero packets are supported in a fixed core collar, then every mixed coefficient/product estimate used in `nonzero_harmonic_forward_reduction.md` depends only on the restriction of `m_ell` to that core, with constants controlled by the global `H^{m_0}` norm; no compact support of `m_ell` is required.

If this closes, the local theorem no longer has a pressure/localization mismatch. The remaining frontier becomes physical-scale inheritance.