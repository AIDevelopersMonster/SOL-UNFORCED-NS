# Finite critical block and uniform stable complement for v0.8

**Status:** PROVED PRINCIPAL/FULL-SYMBOL REDUCTION LEMMA at one frozen v0.8 design, using the already-audited `O(S_*^{-1})` frame perturbation and lattice nondegeneracy. This theorem does not solve the finite compact-support compatibility equations. It proves that the genuinely infinite part of the harmonic lattice is uniformly forward-stable and has a stage-uniform inverse.

## 1. Freeze one admissible v0.8 design

Choose once and for all a sufficiently large integer `M` from `integral_beta_v08_large_u_halfstep_family.md` and freeze

\[
u_*=M^2,
\qquad
\beta_1=2,
\qquad
\beta_2=1,
\]

with one exact relay root `x_M`. Let

\[
y_M=\left(1+\frac1{2M}\right)x_M.
\]

For a lattice index

\[
\nu=(a,b)\in\mathbb Z^2,
\]

put

\[
T_\nu=2a+b,
\qquad
N_\nu=(2M+1)T_\nu-2a.
\tag{C1}
\]

At the relay center the signed reduced slope is

\[
\xi_\nu(0)
=\frac{x_M N_\nu}{2M T_\nu}
\qquad(T_\nu\ne0).
\tag{C2}
\]

Along a translated common auxiliary trajectory every lattice slope has the same additive drift,

\[
\boxed{
\xi_\nu(\theta)=\xi_\nu(0)+\theta,
}
\tag{C3}
\]

as proved in `source_localized_action_preservation.md`.

Fix a compact drift interval

\[
J=[\theta_-,\theta_+]
\tag{C4}
\]

containing the whole region on which the local correction and its relay-compatible cutoff are allowed to live. The interval is fixed after the v0.8 design is frozen and is independent of the dyadic level `ell`.

## 2. Exact principal net-rate function

For `T_\nu != 0`, the normalized principal growing-coordinate rate is

\[
\boxed{
\Gamma_\nu(\theta)
=
\frac{1}{\sqrt{1+u_*^2\xi_\nu(\theta)^2}}
-
T_\nu^2
\frac{1+u_*^2\xi_\nu(\theta)^2}
{(1+u_*^2)^{3/2}}.
}
\tag{C5}

This is the beta-envelope rate with

\[
\beta=|T_\nu|.
\]

For `T_\nu=0`, the inviscid growing contribution vanishes identically. The mode has a nonzero radial normal for every nonzero lattice index, because

\[
T_\nu=0
\Longrightarrow
b=-2a,
\qquad
N_\nu=-2a\ne0,
\]

and hence is purely viscously damped.

## 3. Only finitely many lattice modes can be critical

Define the principal critical set

\[
\boxed{
\mathcal C_M
:=
\{\nu\ne0:\sup_{\theta\in J}\Gamma_\nu(\theta)\ge0\}.
}
\tag{C6}

We claim that `C_M` is finite.

Suppose first that `T_\nu !=0` and `Gamma_\nu(theta)>=0` at some `theta in J`. Multiplying (C5) by the positive factor `sqrt(1+u_*^2 xi^2)` gives

\[
T_\nu^2
\big(1+u_*^2\xi_\nu(\theta)^2\big)^{3/2}
\le
(1+u_*^2)^{3/2}.
\]

Therefore

\[
\boxed{
|T_\nu|
\le
K_M:=(1+u_*^2)^{3/4},
}
\tag{C7}
\]

and

\[
|\xi_\nu(\theta)|
\le
\frac{\sqrt{1+u_*^2}}{u_*}
<\sqrt2.
\tag{C8}
\]

Let

\[
J_*:=\max(|\theta_-|,|\theta_+|).
\]

Then by (C3),

\[
|\xi_\nu(0)|
\le\sqrt2+J_*.
\]

Using (C2),

\[
\boxed{
|N_\nu|
\le
\frac{2M}{x_M}
(\sqrt2+J_*)|T_\nu|.
}
\tag{C9}
\]

Equations (C7) and (C9) leave only finitely many integer pairs `(T,N)`, hence only finitely many lattice indices by the inverse arithmetic

\[
a=\frac{(2M+1)T-N}{2},
\qquad
b=N-2MT.
\]

The `T=0` modes are strictly viscous and do not enter `C_M`. Thus

\[
\boxed{|\mathcal C_M|<\infty.}
\tag{C10}

A very coarse explicit count follows immediately from (C7)–(C9); its size may be large as a function of `M`, but `M` is frozen before the dyadic limit and only finiteness is needed here.

## 4. Uniform gap on the infinite stable complement

Let

\[
\mathcal S_M
=(\mathbb Z^2\setminus\{0\})\setminus\mathcal C_M.
\]

For each fixed `nu in S_M`, compactness of `J` gives

\[
\sup_{\theta\in J}\Gamma_\nu(\theta)<0.
\]

We need a gap uniform in the **infinite** set `S_M`.

If `|T_\nu| -> infinity`, then from (C5)

\[
\sup_{\theta\in J}\Gamma_\nu(\theta)
\le
1-
\frac{T_\nu^2}{(1+u_*^2)^{3/2}}
\longrightarrow-\infty.
\tag{C11}
\]

If `|T_\nu|` stays bounded while `|N_\nu| -> infinity`, then (C2)–(C3) imply

\[
\inf_{\theta\in J}|\xi_\nu(\theta)|\to\infty,
\]

and the negative viscous term in (C5) again tends uniformly to `-infinity`.

Consequently, for any fixed number (say `-1`) only finitely many indices satisfy

\[
\sup_J\Gamma_\nu>-1.
\]

Removing the finite critical set from this finite remainder leaves a strictly negative minimum. Hence there exists

\[
\boxed{\gamma_M>0}
\tag{C12}
\]

such that

\[
\boxed{
\Gamma_\nu(\theta)
\le-\gamma_M
\qquad
(\nu\in\mathcal S_M,\ \theta\in J).
}
\tag{C13}

Thus the entire infinite complement is uniformly forward-stable at principal level.

## 5. Quadratic high-mode damping and smoothing

The stronger lattice estimate from `harmonic_lattice_separation.md` gives, after freezing the v0.8 design and allowing the fixed drift interval `J`, constants `c_M,C_M>0` such that the principal normal obeys

\[
|n_\nu^{(0)}|
\ge c_M|\nu|_1-C_M.
\tag{C14}

The inviscid projected symbol is homogeneous of degree zero in the phase normal and is uniformly bounded on the frozen background compact set. The viscous term is quadratic in `|n_\nu|`. Therefore there exist constants `R_M,c'_M>0` such that

\[
\boxed{
\Gamma_\nu(\theta)
\le-c'_M|\nu|_1^2
\qquad
(|\nu|_1\ge R_M,\ \theta\in J).
}
\tag{C15}

At coefficient level, variation of constants on such modes yields the high-mode inverse estimate

\[
\boxed{
\|G_\nu f_\nu\|_{\rm packet}
\le
\frac{C_M}{1+|\nu|_1^2}
\|f_\nu\|_{\rm packet}.
}
\tag{C16}

For the finitely many stable low modes in `S_M`, (C13) gives a uniform bound after enlarging `C_M`. Hence (C16) may be taken for **all** `nu in S_M` with a larger design-dependent constant.

## 6. Stability under the actual source frame errors

The source phase and moving-frame audit gives `O(S_*^{-1})` perturbations. The lattice-normal perturbation is linear in `(a,b)`, while the reference lower bound is also linear in lattice size; therefore the relative normal error is uniformly `O(S_*^{-1})` across the lattice, as already noted in `harmonic_lattice_separation.md`.

Choose the dyadic threshold `ell_0(M)` so large that every frame/symbol perturbation is at most `gamma_M/2` on the finitely many low stable modes. For high modes, the quadratic viscous gap (C15) dominates the same perturbation automatically.

Thus the **actual localized coefficient system** has a stage-uniform forward inverse on the stable complement satisfying

\[
\boxed{
\|\mathcal G_{S,M}f\|_{\ell^1_\sigma(\rm packet)}
\le C_M
\|f\|_{\ell^1_\sigma(\rm packet)}
}
\tag{C17}

for every exponential lattice weight

\[
w_\sigma(\nu)=e^{\sigma|\nu|_1},
\qquad \sigma\ge0,
\]

and, modewise, retaining the high-frequency smoothing (C16).

No constant in (C17) depends on correction stage or on a finite harmonic truncation. It depends on the frozen relay design `M`, the compact drift interval `J`, and the fixed packet seminorm order.

## 7. Analytic lattice convolution is not the obstruction

For

\[
\|z\|_\sigma
=\sum_{\nu\in\mathbb Z^2}
 e^{\sigma|\nu|_1}\|z_\nu\|_{\rm packet},
\]

the exponential weight is submultiplicative:

\[
e^{\sigma|\nu+\mu|_1}
\le
 e^{\sigma|\nu|_1}e^{\sigma|\mu|_1}.
\]

Therefore ordinary coefficient convolution satisfies

\[
\boxed{
\|z*w\|_\sigma
\le
\|z\|_\sigma\|w\|_\sigma.
}
\tag{C18}

The source-localized product theorem already shows that designated products introduce only algebraic packet factors and preserve the action weight. Together with the high-mode smoothing (C16), this means there is no **combinatorial explosion** coming merely from the infinite number of lattice sites.

What still has to be checked for a full Banach fixed point is the exact uniform harmonic dependence of every differentiated quadratic packet symbol. The expected Navier–Stokes divergence structure plus the source incompressibility gain leaves at most one output-carrier factor, which would be absorbed by the two-power smoothing in (C16), but that last uniform symbol statement has not yet been promoted to a theorem in this repository.

## 8. Main consequence

The stage-uniform infinite-lattice problem splits as

\[
\boxed{
\ell^1_\sigma(\mathbb Z^2)
=
\mathfrak X_{\rm crit}
\oplus
\mathfrak X_{\rm stable},
\qquad
\dim\mathfrak X_{\rm crit}<\infty,
}
\tag{C19}

where:

- `X_stable` has a full stage-uniform right inverse with quadratic high-mode smoothing;
- `X_crit` contains every mode that can be neutral or growing anywhere in the allowed correction interval and is **finite-dimensional** for the frozen design.

Thus exact zero-force closure no longer requires solving infinitely many independent endpoint compatibility conditions. All possible Fredholm/compact-support obstructions are confined to one finite critical block.

The remaining local tasks are now precisely:

1. prove the uniform one-output-carrier bound for the full localized quadratic symbol in the analytic lattice norm;
2. solve the finite-dimensional compact-support compatibility map on `X_crit` (multi-collar transversality or an equivalent internal control mechanism);
3. combine the finite solve with (C17) and the v0.8 action gap to obtain the nonlinear fixed point.
