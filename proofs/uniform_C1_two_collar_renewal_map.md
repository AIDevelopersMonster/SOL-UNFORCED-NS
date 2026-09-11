# Uniform `C^1` control of the exact two-collar renewal map

**Status:** PROVED PARAMETER-DEPENDENT FIXED-POINT THEOREM IN THE BRANCH'S PHASE-ADAPTED REALIZATION. This upgrades the schematic estimate in `two_collar_zero_residual_reduction.md` to a uniform `C^1` statement on a fixed compact amplitude neighborhood and a compact slow-parameter set. It uses only the already established forward nonzero solve, mean contraction, action-filter bounds, and the source-normalized coefficient theorem.

This is still subject to the branch-wide publication caveat: the phase-adapted packet norms and every source-dependent coefficient class must be independently line-audited against the pinned source before a publication-final theorem is claimed.

## 1. Parameters and the small quantity

Fix the v0.8 design integer `M` and let

\[
P:=K_{\rm slow}
\]

be the compact strict-cone slow set from `source_normalized_two_event_coefficients.md`.

Let

\[
A=(A_2,A_1)\in\mathbb C^2
\]

be the finite designated incoming amplitudes. By the uniform coefficient bounds, the principal renewal section lies in one compact positive annulus. Choose once and for all a compact amplitude set

\[
K_A\Subset(\mathbb C\setminus\{0\})^2
\tag{C1-1}
\]

containing a fixed neighborhood of every principal renewal state over `p in P`.

Put

\[
\delta_0:=\frac9{50}-2\kappa_s>0
\]

and define a conservative total source error

\[
\boxed{
\Delta_\ell
:=C_M\left[
S_*^{-1}
+S_*^{C_M}\varepsilon^{\delta_0}
+S_*^{C_M}\varepsilon^{1/5}
+S_*^{C_M}e^{-c_MS_*}
\right].
}
\tag{C1-2}
\]

Since `epsilon=Q^h` decays exponentially in the dyadic level while `S_*=ell^2`,

\[
\boxed{\Delta_\ell\to0.}
\tag{C1-3}
\]

The `S_*^{-1}` term records the source moving-frame/phase error; the positive epsilon powers cover the signed-stress, nonzero, mean and reconstruction remainders.

## 2. Exact correction equation conditional on designated amplitudes

Let

\[
Z=(z,m)
\]

collect the non-designated nonzero-harmonic correction and the angular mean correction on the full two-collar cell. The forward nonzero theorem and the phase-adapted mean theorem give a Banach space `X_cell` in which the exact correction equation can be written

\[
\boxed{
Z=\Phi_{\ell,p}(A,Z).
}
\tag{C1-4}
\]

The principal designated outputs are **not** included in `Phi`; they are extracted into the finite map `mathscr R_{0,p}`. Thus every term remaining in `Phi` contains at least one of the following source-small structures:

- a frame/phase discrepancy `O(S_*^{-1})`;
- the exact signed-stress gain `epsilon^(9/50-2 kappa_s)`;
- the supported nonzero defect `rho_ell=O(S_*^C epsilon^(1/5)+S_*^C e^{-cS_*})`;
- a mean correction of size `O(S_*^C epsilon^(1-kappa_s))`;
- a curl/reconstruction remainder with a positive source exponent;
- a non-designated action deficit `e^{-c_MS_*}`.

Because the Navier--Stokes nonlinearity is polynomial of degree two in the finite amplitudes, differentiating once with respect to `A` only lowers a finite polynomial degree and **does not change any epsilon/action exponent**. Since `A` ranges over the fixed compact set `K_A`, the same small factor is uniform after one amplitude derivative.

Consequently the established block estimates imply

\[
\boxed{
\sup_{p\in P,\,A\in K_A}
\|\Phi_{\ell,p}(A,0)\|_{X_{\rm cell}}
\le C\Delta_\ell,
}
\tag{C1-5}
\]

and

\[
\boxed{
\sup_{p,A}
\|D_A\Phi_{\ell,p}(A,0)\|
\le C\Delta_\ell.
}
\tag{C1-6}
\]

On the correction ball of radius `C Delta_ell`, the differentiated mean/nonzero return estimates give

\[
\boxed{
q_\ell
:=
\sup_{p,A,Z}
\|D_Z\Phi_{\ell,p}(A,Z)\|
\longrightarrow0.
}
\tag{C1-7}
\]

uniformly. Increase the starting level so that

\[
q_\ell\le\frac12.
\tag{C1-8}
\]

The source coefficient maps and the exact forward propagators depend smoothly on the finite amplitudes, so `Phi` is `C^1` in `(A,Z)` on this fixed compact parameter set.

## 3. Uniform parameter-dependent contraction

For each `(ell,p,A)`, Banach's theorem gives a unique fixed point

\[
\boxed{
Z_{\ell,p}(A)=\Phi_{\ell,p}(A,Z_{\ell,p}(A)).
}
\tag{C1-9}
\]

and, by (C1-5), (C1-8),

\[
\boxed{
\|Z_{\ell,p}(A)\|
\le2C\Delta_\ell.
}
\tag{C1-10}
\]

Differentiate (C1-9) with respect to `A`:

\[
\left(I-D_Z\Phi\right)D_AZ
=D_A\Phi.
\tag{C1-11}
\]

The inverse exists and

\[
\left\|(I-D_Z\Phi)^{-1}\right\|
\le\frac1{1-q_\ell}\le2.
\tag{C1-12}
\]

Using (C1-6) and the fact that evaluating `D_A Phi` at `Z=O(Delta_ell)` changes the bound only by the already-small correction radius,

\[
\boxed{
\sup_{p\in P,\,A\in K_A}
\|D_AZ_{\ell,p}(A)\|
\le C'\Delta_\ell.
}
\tag{C1-13}
\]

Thus

\[
\boxed{
\|Z_{\ell,p}\|_{C^1(K_A;X_{\rm cell})}
\le C'\Delta_\ell
}
\tag{C1-14}
\]

uniformly in `p`.

The same argument applies to slow parameters on a slightly smaller compact set because source coefficients are smooth there; only uniformity in `p`, not a small `p`-derivative, is needed below.

## 4. The exact outgoing designated map

Let

\[
\mathscr R_{\ell,p}(A)
\]

be the exact outgoing two-component designated amplitude after solving the complete zero-residual correction on the cell.

Split it as

\[
\boxed{
\mathscr R_{\ell,p}(A)
=
\mathscr R_{0,p}(A)
+E^{\rm dir}_{\ell,p}(A)
+H_{\ell,p}(A,Z_{\ell,p}(A)).
}
\tag{C1-15}
\]

Here:

- `mathscr R_{0,p}` is the source-normalized principal two-event map built from `kappa_1^0(p),kappa_2^0(p)`;
- `E_dir` contains the direct phase/frame/curl/localization error in the two designated projections;
- `H` contains all contributions involving the exact nonzero/mean correction.

`source_normalized_two_event_coefficients.md` gives

\[
\boxed{
\|E^{\rm dir}_{\ell,p}\|_{C^1(K_A)}
\le C\Delta_\ell.
}
\tag{C1-16}
\]

The exact quadratic output functional is bounded in `C^1` on the fixed compact amplitude/correction neighborhood, hence

\[
\|H(A,Z)\|\le C\|Z\|,
\tag{C1-17}
\]

and

\[
\|D_AH(A,Z)\|
\le C\|Z\|+C\|D_AZ\|.
\tag{C1-18}
\]

Using (C1-10), (C1-13),

\[
\boxed{
\sup_{p\in P}
\|H_{\ell,p}(\cdot,Z_{\ell,p}(\cdot))\|_{C^1(K_A)}
\le C\Delta_\ell.
}
\tag{C1-19}
\]

Combining (C1-15)--(C1-19) yields the desired theorem:

\[
\boxed{
\sup_{p\in P}
\|\mathscr R_{\ell,p}-\mathscr R_{0,p}\|_{C^1(K_A)}
\le C\Delta_\ell
\longrightarrow0.
}
\tag{C1-20}
\]

## 5. Uniformity over the principal renewal section

Write

\[
a(p)=|\kappa_1^0(p)|,
\qquad
b(p)=|\kappa_2^0(p)|.
\]

The source-normalized coefficient theorem gives

\[
0<a_-\le a(p)\le a_+,
\qquad
0<b_-\le b(p)\le b_+.
\tag{C1-21}
\]

Hence the principal magnitude section

\[
\boxed{
s_0(p)
=
\left(a(p)^{-1},[a(p)b(p)]^{-1/2}\right)
}
\tag{C1-22}
\]

lies in a compact subset of the positive quadrant. The set `K_A` can therefore be chosen once, independently of `ell` and `p`, with a fixed positive distance from the coordinate axes.

This justifies taking moduli and phase coordinates smoothly in the next implicit-function step.

## 6. Consequence

The schematic claim

\[
\mathscr R_{\ell,p}=\mathscr R_{0,p}+o_{C^1}(1)
\]

is now a theorem in the branch's exact phase-adapted local realization, with an explicit conservative error scale (C1-2).

Therefore the remaining local renewal problem is purely finite-dimensional: apply a uniform implicit-function theorem to the transverse principal fixed-magnitude section. That step is carried out separately in `exact_two_collar_renewal_state.md`.