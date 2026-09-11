# Harmonic boundary replacement is bounded but not automatically small

**Status:** PROVED NEGATIVE LOCALIZATION LEMMA / SHARPENED WHOLE-SPACE FRONTIER.

This note corrects the optimistic possibility raised in `fixed_annulus_leray_oseen_propagator.md` that a fixed buffer separation by itself might force the harmonic difference between bounded-annulus and whole-space pressure to inherit the small factor `rho_ell`.

The correct statement is weaker and more useful: the harmonic corrector is bounded by the size of the boundary discrepancy, but geometric separation on a fixed normalized collar does not create an additional epsilon factor. Therefore the boundary replacement cannot be treated as a new `o(1)` nonlinear remainder unless the boundary data themselves are already `o(1)` for an independent reason.

## 1. Abstract comparison

Let

\[
\Omega_{\rm core}\Subset\Omega_{\rm buf}\Subset\Omega
\]

be fixed nested annular collars with positive normalized separation. Let `F` be supported in `Omega_buf`. Denote by

\[
\mathbb P_{\mathbb R^3}F=F-\nabla p_\infty
\]

the whole-space Leray projection and by

\[
\mathbb P_\Omega F=F-\nabla p_\Omega
\]

the bounded-annulus Hodge projection for the impermeable realization used in the fixed-annulus theorem.

Inside `Omega_core` both pressure potentials solve the same Poisson equation because the source divergence is the same. Hence

\[
\boxed{
h_F:=p_\Omega-p_\infty
}
\tag{HB1}
\]

satisfies

\[
\boxed{\Delta_*h_F=0\quad\text{in }\Omega_{\rm core}.}
\tag{HB2}
\]

Therefore

\[
\boxed{
\mathbb P_{\mathbb R^3}F
=\mathbb P_\Omega F+\nabla h_F
\quad\text{in }\Omega_{\rm core}.
}
\tag{HB3}
\]

## 2. Interior elliptic estimate

Standard interior elliptic regularity gives, for fixed `m>=0`,

\[
\boxed{
\|\nabla h_F\|_{H^m(\Omega_{\rm core})}
\le
C_{m,\Omega_{\rm core},\Omega_{\rm buf}}
\|h_F\|_{H^{m+1}(\Omega_{\rm buf})}.
}
\tag{HB4}
\]

Equivalently one may estimate the core field by boundary traces on a separating surface `Gamma`:

\[
\boxed{
\|\nabla h_F\|_{H^m(\Omega_{\rm core})}
\le
C_m
\left(
\|h_F\|_{H^{m+1/2}(\Gamma)}
+
\|\partial_nh_F\|_{H^{m-1/2}(\Gamma)}
\right).
}
\tag{HB5}
\]

The constant depends on the fixed separation but carries no small dyadic parameter.

Thus buffer separation gives smoothing/boundedness, not asymptotic smallness.

## 3. Why fixed separation cannot create an epsilon gain

Take a nontrivial harmonic function on a fixed annulus, for example a low axial/spatial harmonic mode whose boundary trace has unit size. Its value and gradient on a smaller fixed core remain a fixed nonzero fraction of the boundary size. There is no parameter tending to zero in this geometry.

Consequently no estimate of the form

\[
\boxed{
\|\nabla h_F\|_{H^m(\Omega_{\rm core})}
\le
\eta_\ell
\|\text{boundary discrepancy}\|,
\qquad
\eta_\ell\to0,
}
\tag{HB6}
\]

can follow from fixed collar separation alone.

The only possible sources of smallness are therefore:

1. the boundary discrepancy itself is already small because the forcing that creates it belongs to an `o(1)` source class;
2. the physical separation grows with the dyadic scale in a way that yields an actual decaying multipole factor;
3. low spatial moments of the forcing vanish, causing cancellation in the whole-space Newtonian tail;
4. the whole-space Leray operator is incorporated directly into the full linear propagator instead of being treated as a perturbative corrector.

## 4. Multipole interpretation

For compactly supported forcing in physical space, the whole-space pressure is determined by

\[
-\Delta p_\infty=\partial_i\partial_j T_{ij}
\]

for the relevant stress tensor `T`. Far from the source, the leading tail is governed by the lowest nonvanishing moments of `T`.

Therefore the correct quantity to audit is not the distance from the artificial annular wall by itself, but the first nonzero multipole of the actual relay stress/mean source.

If the monopole/dipole-type moments vanish because of divergence structure or source symmetries, one may gain powers of the support-to-observation ratio. If they do not vanish, the pressure tail can be the same algebraic order as the source amplitude.

This converts the boundary-replacement problem into a finite moment/cancellation problem.

## 5. Consequence for the nonlinear contraction

The signed-stress and mean/nonzero nonlinear source blocks are now known to carry positive factors:

\[
\varepsilon^{9/50-2\kappa_s},
\qquad
\varepsilon^{1/2-\kappa_s},
\qquad
\varepsilon^{1-2\kappa_s},
\qquad
\rho_\ell.
\]

If the whole-space pressure correction is generated only by these nonlinear residuals, boundedness of the global Leray operator is sufficient: no additional small factor is required, because the input is already `o(1)`.

The dangerous case is an `O(1)` linear/background boundary discrepancy. Such a term cannot be pushed into the nonlinear contraction and must be absorbed into the exact whole-space linear propagator.

Hence the local architecture should now be split as follows:

\[
\boxed{
\text{all }O(1)\text{ whole-space pressure effects}\to\text{linear operator},
}
\tag{HB7}
\]

\[
\boxed{
\text{all source-small whole-space pressure effects}\to\text{nonlinear Duhamel map}.
}
\tag{HB8}
\]

## 6. Corrected frontier

The previous target

\[
\text{prove harmonic boundary corrector is automatically }O(\rho_\ell)
\]

is false without an independent smallness or moment hypothesis.

The correct next theorem is instead:

> Construct the mean equation directly with the whole-space Leray/Hodge operator, prove its bounded action on the fixed-order packet/Sobolev space used by the relay, and show that every nonlinear pressure contribution inherits the already-proved small factor of its source.

A secondary, potentially stronger route is to compute the low multipoles of the actual relay stress and prove extra decay/cancellation. That may become important for physical-scale inheritance, but it is not required merely to preserve the local contraction if the whole-space projector is bounded.
