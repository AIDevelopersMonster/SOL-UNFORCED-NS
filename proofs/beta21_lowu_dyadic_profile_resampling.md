# Dyadic profile resampling for the low-`u` bilateral orbit

**Status:** PROVED SUMMABLE CANONICAL-PROFILE CHANGE AFTER TANGENT REMOVAL AND `j/sqrt(S)` RESCALING / EXACT NONLINEAR INTER-CELL SHADOWING STILL OPEN.

The raw large-deviation sequence spaces at source lengths

\[
S_n=n^2,
\qquad
S_{n+1}=(n+1)^2
\]

cannot be compared by the same-index map: tail weights may differ by `exp(O(sqrt(S)))`.  However the **canonical physical orbit profile** is concentrated on the much smaller index window

\[
|j|=O(\sqrt S),
\]

and, after removing the geometric shift eigenfactor and rescaling

\[
y=\frac{j}{\sqrt S},
\]

it has a fixed Gaussian limit.

The first finite-`S` correction is of order `S^{-1/2}`.  Because `S_n=n^2`, its change between neighboring source levels is

\[
\frac1n-\frac1{n+1}=O(n^{-2}),
\]

which is summable.  This gives the correct dyadic boundary norm for global shadowing.

The theorem concerns canonical profile geometry.  It does not yet prove that the exact nonlinear gap/cell cocycle maps one resampled profile to the next.

## 1. Orbit slope grids

At the exact finite-`S` low-`u` reset point let

\[
\kappa_S=\kappa_*+O(S^{-1}).
\]

The catalyst orbit slope spacing is twice the boundary-layer separation and the parent spacing is one separation.  Thus, after choosing the index origin at the profile center,

\[
\boxed{
z_{C,j}(S)=x+d_{C,S}\frac jS,\qquad d_{C,S}=2\kappa_S,}
\tag{DR1}
\]

\[
\boxed{
z_{Q,j}(S)=x+d_{Q,S}\frac jS,\qquad d_{Q,S}=\kappa_S.}
\tag{DR2}
\]

The harmless integer centering offsets produced by the exact finite-`S` lattice choice change `j` by `O(1)` and therefore contribute only `O(S^{-1/2})` translation in the profile coordinate below.  They may be absorbed into the canonical phase/translation normalization; for clarity the centered formulas (DR1)--(DR2) are used throughout.

## 2. Large-deviation actions have a nondegenerate quadratic maximum

For `b=1,2`, recall

\[
H_b(z)=\mathcal E_b(z)-\mathcal E_b(x)+(x-z)g_b,
\qquad
g_b=u\Gamma_b(x).
\]

The branch already proves

\[
H_b(x)=0,
\qquad
H_b'(z)=u\bigl(\Gamma_b(z)-\Gamma_b(x)\bigr).
\]

Hence

\[
\boxed{H_b'(x)=0.}
\tag{DR3}
\]

Since `Gamma_b` is strictly decreasing on the positive strict core,

\[
\boxed{
H_b''(x)=u\Gamma_b'(x)<0.
}
\tag{DR4}
\]

Thus `x` is a strict nondegenerate maximum of each physical orbit action.

Fix a smaller compact core around `x`.  Smoothness gives constants

\[
a_b>0,\qquad C_b<\infty
\]

such that

\[
\boxed{
H_b(x+s)
=-a_bs^2+b_bs^3+O(s^4)
}
\tag{DR5}
\]

and

\[
H_b(x+s)\le-\frac{a_b}{2}s^2
\tag{DR6}
\]

on that core after shrinking it if necessary.

## 3. Tangent/geometric normalization

Let the exact finite-`S` canonical shift ratios be

\[
\rho_{C,S},\qquad \rho_{P,S},
\]

with

\[
\rho_{C,S}=\rho_C+O(S^{-1}),
\qquad
\rho_{P,S}=\rho_P+O(S^{-1})
\tag{DR7}
\]

by the finite-`S` exact reset theorem and its `C^1` parameter transfer.

Write canonical orbit coefficients schematically as

\[
c_{S,j}=c_{S,0}\rho_{C,S}^{\,j},
\qquad
q_{S,j}=q_{S,0}\rho_{P,S}^{\,j}
\tag{DR8}
\]

inside the principal bilateral core, with the exact finite-`S` action-normalized correction absorbed into the `O(S^{-1})` profile terms below.

Define tangent-normalized sequences

\[
\boxed{
\widetilde c_{S,j}:=\rho_{C,S}^{-j}c_{S,j}/c_{S,0},
\qquad
\widetilde q_{S,j}:=\rho_{P,S}^{-j}q_{S,j}/q_{S,0}.
}
\tag{DR9}

At limiting principal level both are the constant sequence `1`.  All physical bilateral localization is then carried by the action weights `H_1,H_2` rather than by an exponentially growing/decaying raw geometric coefficient.

This is the correct normalization for comparing different source lengths.

## 4. Central profile coordinate

Put

\[
\boxed{y=\frac j{\sqrt S}.}
\tag{DR10}

For sector `b` with spacing coefficient `d_{b,S}`, equations (DR1)--(DR2) give

\[
z_{b,j}(S)-x
=d_{b,S}\frac y{\sqrt S}.
\tag{DR11}

Taylor expansion (DR5) yields

\[
\begin{aligned}
S H_b(z_{b,j}(S))
&=-a_bd_{b,*}^2y^2
+\frac{b_bd_{b,*}^3y^3}{\sqrt S}
+O\!\left(\frac{1+|y|^4}{S}\right),
\end{aligned}
\tag{DR12}

uniformly for `|y|` in every fixed compact set.  Here

\[
d_{C,*}=2\kappa_*,
\qquad
d_{Q,*}=\kappa_*.
\]

The `O(S^{-1})` drift of `kappa_S` changes the quadratic coefficient only by `O(S^{-1})`; it does not create another `S^{-1/2}` term.

## 5. Gaussian limiting profiles

Define

\[
\boxed{
G_b(y):=\exp(-a_bd_{b,*}^2y^2).
}
\tag{DR13}

and

\[
\boxed{
G_{b,1}(y):=
 b_bd_{b,*}^3y^3G_b(y).
}
\tag{DR14}

Exponentiating (DR12) gives, on compact `y`-sets,

\[
\boxed{
\exp\{S H_b(z_{b,j}(S))\}
=G_b(y)
+S^{-1/2}G_{b,1}(y)
+O\!\left(S^{-1}(1+|y|^8)G_b(y)^{1/2}\right).
}
\tag{DR15}

The precise polynomial degree in the remainder is irrelevant; any fixed sufficiently large power works after shrinking the quadratic constant in the Gaussian majorant.

Thus the canonical physical orbit has a fixed Gaussian continuum limit after tangent removal.

## 6. Uniform Gaussian tails

From (DR6), for all central indices inside the strict core,

\[
\exp\{S H_b(z_{b,j}(S))\}
\le
\exp(-c_bj^2/S)
\tag{DR16}
\]

for one `c_b>0` independent of `S`.

Consequently, for every `N`, choose `L_N` sufficiently large.  Then the profile contribution of

\[
|j|\ge L_N\sqrt{S\log S}
\]

is bounded by

\[
\boxed{CS^{-N}}
\tag{DR17}
\]

in every fixed polynomially weighted `ell^2` profile norm.

The much farther fixed-core boundary `|z-x|=w` already has the stronger estimate

\[
S^Ae^{-c_{bd}S}.
\tag{DR18}
\]

Hence all profile comparison may be reduced to a slowly growing central `y` window.

## 7. A common continuum profile space

Let

\[
h_S:=S^{-1/2}.
\]

For a tangent-normalized sequence `a_j`, define `I_S a` to be its piecewise-linear interpolation on the mesh

\[
y_j=jh_S.
\]

Use one fixed Gaussian Sobolev profile norm, for example

\[
\boxed{
\|f\|_{\mathcal H_b^2}^2
:=\sum_{r=0}^2
\int_{\mathbb R}
(1+y^2)^2
|\partial_y^rf(y)|^2
G_b(y)\,dy.
}
\tag{DR19}

The Gaussian may be weakened slightly without changing the theorem.

For every fixed smooth Gaussian-polynomial profile, piecewise-linear interpolation has the standard second-order approximation error

\[
\boxed{
\|I_S(f|_{h_S\mathbb Z})-f\|_{\mathcal H_b^1}
\le C_fh_S^2
=CS^{-1}.
}
\tag{DR20}

The core truncation changes this only by the super-polynomial/exponential tails (DR17)--(DR18).

## 8. Canonical profile expansion in the common space

Let `F_{b,S}` be the interpolated tangent-normalized physical canonical profile for sector `b`.  Equations (DR15), (DR17), and (DR20) give

\[
\boxed{
F_{b,S}
=G_b
+S^{-1/2}G_{b,1}
+R_{b,S},
}
\tag{DR21}

with

\[
\boxed{
\|R_{b,S}\|_{\mathcal H_b^1}
\le CS^{-1}+CS^{-N}+CS^Ae^{-cS}.
}
\tag{DR22}

After fixing `N>=2`, this is simply

\[
\boxed{
\|R_{b,S}\|_{\mathcal H_b^1}\le CS^{-1}.
}
\tag{DR23}

The finite-`S` exact PDE correction is super-polynomially small in `S^{-1}` and is absorbed into (DR23).

## 9. Neighboring dyadic levels

Now set

\[
S_n=n^2.
\]

Then

\[
S_n^{-1/2}=\frac1n.
\]

Equation (DR21) becomes

\[
F_{b,n}
=G_b+\frac1nG_{b,1}+R_{b,n},
\qquad
\|R_{b,n}\|\le Cn^{-2}.
\tag{DR24}

Therefore

\[
\begin{aligned}
F_{b,n+1}-F_{b,n}
&=\left(\frac1{n+1}-\frac1n\right)G_{b,1}
+R_{b,n+1}-R_{b,n}.
\end{aligned}
\]

Hence

\[
\boxed{
\|F_{b,n+1}-F_{b,n}\|_{\mathcal H_b^1}
\le \frac{C}{n^2}.
}
\tag{DR25}

In particular

\[
\boxed{
\sum_{n\ge n_0}
\|F_{b,n+1}-F_{b,n}\|_{\mathcal H_b^1}
<\infty.
}
\tag{DR26}

This is the summable dyadic profile-resampling estimate sought in
`beta21_lowu_intercell_orbit_transfer_reduction.md`.

## 10. Interpretation in the original lattice

The continuum embedding automatically performs the correct physical-slope reindexing.  An old index `j` corresponds to profile coordinate

\[
y=j/\sqrt{S_n}.
\]

At the next level the same continuum point is sampled near

\[
j'\approx y\sqrt{S_{n+1}}.
\]

Thus

\[
j'\approx j\sqrt{S_{n+1}/S_n},
\]

which is precisely the slope-matched rather than same-index comparison required by the previous reduction.

The reindexing is a **comparison of canonical profiles**, not an assertion that the physical Fourier character `j` is literally relabelled to `j'` by the source chart change.  The exact physical inter-cell evolution must still be shown to shadow this canonical profile comparison.

## 11. Relation to the spectral-instability audit

`beta21_lowu_intercell_spectral_stability_audit.md` proves that arbitrary lattice-rough perturbations can be strongly amplified by the limiting Poincare operators.

That theorem does not contradict (DR25).  The dyadic canonical-profile defect lies in the smooth low-lattice-frequency sector represented by the continuum `y` variable.  High-frequency alternating perturbations such as the catalyst spectral point `zeta=-rho_C`, which experiences amplification about `8.1`, are not generated by the smooth resampling operation above.

Therefore the global shadowing theorem must preserve **profile regularity** in addition to small norm.  A raw `ell^2` perturbation theorem is insufficient.

## 12. Remaining dynamical theorem

The canonical profile change itself is now summable.  The unresolved step is dynamical:

> Show that exact physical gap transport plus one exact local reset maps the smooth tangent-Gaussian profile sector into itself, and that the induced profile error satisfies a summable recurrence after the three macroscopic reset parameters are modulated.

Equivalently, construct a scale-dependent profile cocycle on

\[
\mathcal H_C^1\oplus\mathcal H_P^1
\]

whose canonical sequence (DR24) is shadowed by an exact forward solution.

The preferred next file is

`beta21_lowu_smooth_profile_shadowing_reduction.md`.

Only after that dynamical shadowing theorem should the programme attempt the final single-initial-datum / finite-time accumulation argument.
