# Active collision gate: finite-control reduction for the beta-(2,1) reset cell

**Status:** PROVED FINITE-DIMENSIONAL REDUCTION / SOURCE-SPECIFIC RANK STILL OPEN. The passive five-collar obstruction in `passive_five_collar_recursion_obstruction.md` shows that a useful collision gate must actively cancel forbidden downstream exit traces. This note proves the finite-dimensional control architecture needed for such a gate and identifies the minimal control count for the first explicit shortcut block.

The theorem is exact as a finite-dimensional reduction under the stated kernel-independence and packet-realizability hypotheses. It does **not** yet prove that the exact OpenAI source packet family realizes a full-rank four-control matrix for the beta-(2,1) gate.

## 1. The first active gate problem

Consider one collision collar intended to realize only

\[
C+D\longrightarrow P.
\tag{AG1}
\]

The local Duhamel analysis proves that, without active cancellation, the same open overlap also creates the shortcut chain

\[
P+D\to E,
\qquad
E-C\to Q,
\qquad
Q-C\to H.
\tag{AG2}
\]

For the first explicit gate, declare

\[
\mathcal F_1:=\{E,Q,H\}
\tag{AG3}
\]

as the forbidden principal exit block. Let

\[
P_{\rm out},\quad E_{\rm out},\quad Q_{\rm out},\quad H_{\rm out}
\in\mathbb C
\]

be the corresponding phase-normalized outgoing growing coefficients at the collar exit.

The desired gate condition is

\[
\boxed{
P_{\rm out}=P_*\ne0,
\qquad
E_{\rm out}=Q_{\rm out}=H_{\rm out}=0.
}
\tag{AG4}
\]

All non-designated modes outside the finite critical exit block are assigned to the stable complement and are to be slaved by the existing analytic/Leray contraction.

## 2. Independent localized controls

Introduce `r` complex control amplitudes

\[
p=(p_1,\ldots,p_r)\in\mathbb C^r
\tag{AG5}
\]

attached to independently localized source-admissible packet perturbations inside the collision collar. At the abstract level each control may be a narrow curl-generated packet or a finite linear combination of source packet types. What matters for the reduction is that the controls are independently tunable complex amplitudes and depend smoothly on their collar-center parameter.

Let

\[
\mathcal G_\ell(p)
:=
\begin{pmatrix}
P_{\rm out}(p)\\
E_{\rm out}(p)\\
Q_{\rm out}(p)\\
H_{\rm out}(p)
\end{pmatrix}
\in\mathbb C^4
\tag{AG6}
\]

be the exact phase-adapted outgoing map after the stable nonzero complement and angular mean have been solved conditionally on the finite controls.

The target vector is

\[
y_*=(P_*,0,0,0)^T.
\tag{AG7}
\]

## 3. Minimal control count

### Proposition 3.1

For a generic local gate imposing one prescribed nonzero complex designated output and `N` independent complex forbidden-trace equations, fewer than `N+1` independent complex controls cannot give a locally onto control map.

### Proof

The linearized target space has complex dimension `N+1`. The derivative of a map from `C^r` has rank at most `r`. Therefore local surjectivity requires

\[
r\ge N+1.
\tag{AG8}
\]

For the explicit block `F_1={E,Q,H}`, `N=3`, hence

\[
\boxed{r\ge4.}
\tag{AG9}
\]

Thus **four complex controls are generically minimal** for the first active beta-(2,1) genealogy gate. ∎

This count concerns only the displayed principal shortcut block. If the exact finite critical exit set contains `N_{crit}>3` independent forbidden complex coordinates, the generic lower bound becomes

\[
\boxed{r\ge1+N_{crit}.}
\tag{AG10}
\]

## 4. Point-control kernel matrix

Let the collision interval be

\[
I=(v_-,v_+).
\]

For a unit point-like control inserted at time `tau in I`, define the four principal linear response kernels

\[
K_P(\tau),\quad K_E(\tau),\quad K_Q(\tau),\quad K_H(\tau).
\tag{AG11}
\]

Here `K_P(tau)` is the exit response in the desired `P` channel and the remaining three kernels are the induced first variations of the forbidden exit traces after propagation through the triangular linearization about the chosen collision-gate background.

For four point controls at distinct centers

\[
\tau_1,\tau_2,\tau_3,\tau_4\in I,
\]

the principal control Jacobian is

\[
\boxed{
J_0=
\begin{pmatrix}
K_P(\tau_1)&K_P(\tau_2)&K_P(\tau_3)&K_P(\tau_4)\\
K_E(\tau_1)&K_E(\tau_2)&K_E(\tau_3)&K_E(\tau_4)\\
K_Q(\tau_1)&K_Q(\tau_2)&K_Q(\tau_3)&K_Q(\tau_4)\\
K_H(\tau_1)&K_H(\tau_2)&K_H(\tau_3)&K_H(\tau_4)
\end{pmatrix}.
}
\tag{AG12}
\]

The exact analogue of the sampling lemma in `multicollar_finite_critical_transversality.md` gives:

### Proposition 4.1

If

\[
K_P,K_E,K_Q,K_H
\tag{AG13}
\]

are linearly independent continuous functions on `I`, then there exist four distinct centers `tau_j` such that

\[
\boxed{\det J_0\ne0.}
\tag{AG14}
\]

### Proof

It is the `N=4` sampling lemma. Linear independence of four continuous functions implies the existence of four sampling points with nonsingular evaluation matrix. Distinctness follows automatically because coinciding points give identical columns and zero determinant. ∎

Hence the whole active-gate rank question is reduced to the concrete source-specific kernel independence in (AG13).

## 5. Smooth narrow controls preserve rank

Fix a unit-integral bump `psi in C_c^infty((-1,1))` and replace the point control at `tau_j` by

\[
q_{j,\delta}(v)
=\delta^{-1}\psi\!\left(\frac{v-\tau_j}{\delta}\right).
\tag{AG15}
\]

Let `J_delta` be the resulting principal response matrix. By continuity of the four kernels,

\[
J_\delta\longrightarrow J_0
\qquad(\delta\to0).
\tag{AG16}
\]

Therefore, whenever (AG14) holds, there exists `delta_0>0` such that

\[
\boxed{
0<\delta<\delta_0
\Longrightarrow
\det J_\delta\ne0.
}
\tag{AG17}
\]

Thus the control-rank mechanism is compatible with smooth localization; no literal impulse source is required by the finite-dimensional argument.

## 6. Nonlinear gate equation

Let `p_0` be a principal control vector satisfying

\[
\mathcal G_0(p_0)=y_*.
\tag{AG18}
\]

Assume

\[
D_p\mathcal G_0(p_0)=J_0
\tag{AG19}
\]

is invertible. Write the exact high-level map as

\[
\mathcal G_\ell(p)
=\mathcal G_0(p)+\mathcal E_\ell(p).
\tag{AG20}
\]

The previously proved source-localization, nonzero-harmonic forward solve, whole-space mean solve, and fixed-order Leray estimates give the required architecture for a `C^1` perturbation estimate of the form

\[
\boxed{
\|\mathcal E_\ell\|_{C^1(B(p_0,r))}
\le C S_*^A\varepsilon^{\delta_*}
+CS_*^Ae^{-cS_*}
=o(1),
}
\tag{AG21}
\]

provided the chosen controls are realized by packet perturbations lying in the same audited source classes. Equation (AG21) is the exact source-specific estimate that must still be checked for the new control family; it is not silently asserted here for arbitrary controls.

If (AG21) is verified, then for sufficiently high level

\[
D_p\mathcal G_\ell
\]

remains invertible and the finite-dimensional implicit-function theorem yields a unique nearby exact control vector

\[
\boxed{p_\ell=p_0+o(1)}
\tag{AG22}
\]

such that

\[
\boxed{
\mathcal G_\ell(p_\ell)=y_*.
}
\tag{AG23}
\]

This is precisely the desired exact forbidden-trace cancellation at one collar exit.

## 7. Stable complement does not change the control count

Let the full coefficient state split as

\[
U=U_{crit}+Z,
\tag{AG24}
\]

where `U_crit` consists of the finite designated/forbidden exit block and `Z` contains the infinite stable nonzero lattice together with the angular mean correction.

The existing local zero-residual and two-collar reduction results give a unique conditional solution

\[
\boxed{Z=Z(p)}
\tag{AG25}
\]

with locally Lipschitz, and in the publication norm `C^1`, dependence on the finite control vector, once the new controls remain in the audited packet class.

Substituting (AG25) into the four exit functionals merely changes `mathcal G_ell`; it does not add infinitely many independent control equations. Therefore the active-gate problem remains a finite-dimensional Lyapunov--Schmidt problem:

\[
\boxed{
\text{finite exit-trace solve}
+\text{unique stable-complement contraction}.
}
\tag{AG26}
\]

## 8. Why the four-control block is the correct first test

The explicit passive-collar leakage is generated by the rooted chain

\[
C+D\to P\to E\to Q\to H.
\tag{AG27}
\]

Therefore `(E,Q,H)` is the first finite block that must be killed before the desired `P` is transported into the next reset event.

If one can prove (AG13) for this four-row response system and realize the four controls exactly, then the most immediate genealogy shortcut isolated in `passive_five_collar_recursion_obstruction.md` is removed at the collar exit.

This still does not prove that **all** dangerous low modes vanish. The next audit must enumerate the full finite principal exit block generated during the collision collar. If additional growing/neutral coordinates occur, enlarge the row family and add one complex control per additional independent complex constraint.

## 9. Concrete source-specific obligations

The active-gate route is now reduced to four explicit tasks.

1. **Enumerate the finite gate-critical exit block.** Start with `E,Q,H` and add every other growing/neutral descendant that is not already uniformly action-subcritical on the collar.
2. **Derive the actual response kernels.** Compute `K_j(tau)` from the exact principal source propagators, Leray projections, and the chosen packet-control types.
3. **Prove kernel independence with a quantitative determinant margin.** Nonvanishing alone is enough for the abstract theorem, but publication robustness requires a fixed normalized lower bound before `O(S_*^{-1})` packet/frame errors.
4. **Realize the controls in the exact source class and prove (AG21).** The packet perturbations must remain curl-generated/divergence-free, obey the source wave-class bounds, preserve the `u_*=4` phase-cone margin, and not spoil the trapped-spine placement.

Only after these close should the one-collar gate be repeated five times along the ordered reset genealogy.

## 10. Research consequence

The new architecture is no longer

\[
\text{five passive translated overlaps}.
\]

It is

\[
\boxed{
\text{finite active gate}
\times
\text{ordered reset genealogy}
\times
\text{stable-complement contraction}.
}
\tag{AG28}
\]

For the first explicit shortcut block the control budget is now fixed:

\[
\boxed{
1\ \text{desired complex output}
+3\ \text{forbidden complex traces}
=4\ \text{complex controls, generically minimal}.
}
\tag{AG29}
\]

The decisive next mathematical question is therefore not how many passive collars to draw, but whether the exact beta-(2,1) source response kernels for these four exit coordinates are linearly independent and quantitatively transverse.

Until that source-specific rank theorem is proved, the active gate remains a rigorous reduction rather than a completed Navier--Stokes relay cell, and no infinite autonomous cascade or blowup theorem is claimed.
