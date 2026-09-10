# Source-localized preservation of the v0.8 action gap

**Status:** PROVED FINITE-STAGE TRANSFER THEOREM under the designated-overlap modification already isolated in `translated_async_overlap.md`. The proof is a line-by-line transfer of the OpenAI coefficient calculus to the v0.8 relay supernode. It proves that localization, curl generation, common-torus pullback, the pulse inverse, and the displayed linear residual operators introduce only algebraic/polynomial losses and therefore cannot erase a fixed `e^{-c S_*}` action deficit.

It does **not** yet prove the infinite zero-force correction fixed point. The remaining issue is a stage-uniform weighted inverse on the full harmonic lattice, including exact treatment of all compact-support compatibility conditions.

Primary source: OpenAI, *Finite Time Blowup for Navier–Stokes*, Definition 6.5, Proposition 6.6, Lemma 6.2, Proposition 7.2, Lemma 7.7, equation (7.40), Proposition 9.1, and Lemma 9.2.

## 1. Fix one v0.8 design

Choose once and for all an integer `M>=M_0` from `integral_beta_v08_large_u_halfstep_family.md`, freeze

\[
u_*=M^2,
\qquad
\beta_1=2,
\qquad
\beta_2=1,
\]

and choose one exact finite-`u_*` resonance root `x_M`. Put

\[
y_M=\left(1+\frac1{2M}\right)x_M,
\qquad
x_{c,M}=\left(1-\frac1{2M}\right)x_M.
\]

The v0.8 theorem supplies a fixed number

\[
\delta_*>0
\]

such that every non-designated principal-growing lattice mode has center action deficit at least `delta_*`.

At dyadic level `ell`, let

\[
L_s\asymp S_*=\ell^2,
\qquad
\Lambda_\ell:=\frac{\lambda_0L_s}{u_*}.
\]

Since `M` and `u_*` are now frozen, `Lambda_ell` is comparable to `S_*`.

## 2. Bounded-`v` relay collar and synchronized coordinate drift

Use the translated auxiliary rectangles from `translated_async_overlap.md` to place the two parents and the desired child at their prescribed local coordinates at one common point. Around that point take a collar

\[
\boxed{
\mathcal C_{L_0}:=\{|v-v_0|\le L_0\}
}
\tag{P1}
\]

with `L_0` fixed independently of `ell`.

The source pulse coordinate is affine and satisfies

\[
x=\frac12+\frac{v}{L_s}.
\]

All translated labels have the same derivative `dx/dv=1/L_s`; the translations change only their centers. Therefore throughout the common collar

\[
\boxed{
 x_1(v)=x_M+\theta(v),
\quad
 x_2(v)=y_M+\theta(v),
\quad
 x_c(v)=x_{c,M}+\theta(v),
}
\tag{P2}

where

\[
\boxed{
|\theta(v)|\le\frac{L_0}{L_s}=O(S_*^{-1}).
}
\tag{P3}

For a lattice phase `a Phi_1+b Phi_2`, write

\[
T=2a+b.
\]

If `T!=0`, its signed effective reduced slope is

\[
\xi_{a,b}(v)
=\frac{2a x_1(v)+b x_2(v)}{T}.
\]

Using `T=2a+b` and (P2),

\[
\boxed{
\xi_{a,b}(v)=\xi_{a,b}(v_0)+\theta(v).
}
\tag{P4}

This exact covariance is useful: **every nonzero-tangential lattice slope drifts by the same `O(S_*^{-1})` amount**, independently of `(a,b)`.

For `T=0`, the inviscid growing contribution vanishes and the mode is handled as a viscous mode rather than by a pulse-envelope comparison.

## 3. Direct coefficient-product rule inside a designated supernode

The source Definition 6.5 gives, for a wave coefficient of order `epsilon^alpha`,

\[
|D^I a_j|
\le
C_I\varepsilon^{\alpha_j}S_*^{C_I}
\sqrt\zeta\,\delta^{-C_I}P_j(v).
\tag{P5}

In the published construction distinct labels have disjoint auxiliary supports, so Proposition 6.6 sets their products to zero. Our relay supernode deliberately replaces this one separation relation for a prescribed finite family of labels.

On the common-torus overlap, however, the **estimate itself** follows directly from (P5): Leibniz' rule gives

\[
\boxed{
|D^I(a_1a_2)|
\le
C_I\varepsilon^{\alpha_1+\alpha_2}S_*^{C_I}
\zeta\,\delta^{-C_I}P_1P_2.
}
\tag{P6}

No inverse envelope is introduced. Lemma 6.2 supplies uniformly bounded derivative factors under common-torus pullback and introduces no new dyadic band. Hence a finite product of designated overlapping coefficients has the schematic bound

\[
\boxed{
|D^I F|
\le
C_I\varepsilon^\alpha S_*^{C_I}
\zeta^{\rho_I}\delta^{-C_I}
P_1^{n_1}P_2^{n_2}.
}
\tag{P7}

The only change from the source product calculus is that the selected cross-label product is retained rather than set equal to zero.

## 4. Genealogical action

A monomial generated from the two real parents and carrying net lattice index `(a,b)` contains at least

\[
n_1\ge|a|,
\qquad
n_2\ge|b|.
\tag{P8}

Define its source action at the relay center by

\[
\mathscr A_{n_1,n_2}
=n_1A_M+n_2B_M,
\]

where

\[
A_M=\mathcal E_{2,u_*}(x_M)<0,
\qquad
B_M=\mathcal E_{1,u_*}(y_M)<0.
\]

Extra cancelling parent/conjugate factors only make this action more negative.

For a non-designated principal-growing output mode `(a,b)`, let

\[
\mathscr E_{a,b}(v)
=
\mathcal E_{|T|,u_*}(|\xi_{a,b}(v)|).
\]

At the collar center, the v0.8 global action theorem gives

\[
\boxed{
\mathscr A_{n_1,n_2}
-
\mathscr E_{a,b}(v_0)
\le-\delta_*.
}
\tag{P9}

## 5. Uniform persistence of the action gap across the collar

The set of all genealogies is infinite, so one cannot justify (P9) throughout the collar by a finite-mode continuity statement alone. We split the argument into high degree and bounded degree.

Because `A_M<0` and `B_M<0`, continuity gives a fixed neighborhood `|theta|<=theta_0` and a number `c_M>0` such that

\[
\mathcal E_{2,u_*}(x_M+\theta)\le-c_M,
\qquad
\mathcal E_{1,u_*}(y_M+\theta)\le-c_M
\tag{P10}
\]

for `|theta|<=theta_0`.

Every principal-growing natural envelope is bounded below by a finite constant depending only on the frozen `u_*`; for example the zero-slope estimate from the v0.8 proof gives

\[
\mathscr E_{a,b}(v)>-C_M,
\qquad
C_M:=\log(3u_*)+1.
\tag{P11}

Hence whenever

\[
n_1+n_2\ge N_M:=\left\lceil\frac{C_M+2\delta_*}{c_M}\right\rceil,
\]

(P10)–(P11) imply

\[
\mathscr A_{n_1,n_2}(v)-\mathscr E_{a,b}(v)
\le-2\delta_*.
\tag{P12}

Only finitely many genealogies have degree `<N_M`. For this finite set, (P9), the exact common drift (P4), and continuity of the exact finite-`u_*` envelopes give a number `theta_1>0` such that

\[
\mathscr A_{n_1,n_2}(v)-\mathscr E_{a,b}(v)
\le-\frac{\delta_*}{2}
\tag{P13}
\]

whenever `|theta|<=theta_1`.

Take

\[
theta_*:=\min(theta_0,theta_1).
\]

Since `L_0/L_s -> 0`, there is `ell_0` such that the bounded collar (P1) obeys `|theta|<=theta_*` for every `ell>=ell_0`.

Therefore we have the uniform collar estimate

\[
\boxed{
P_1(v)^{n_1}P_2(v)^{n_2}
\le
\exp\!\left(-\frac{\delta_*}{2}\Lambda_\ell\right)
P_{a,b}(v)
}
\tag{P14}

for **every non-designated principal-growing genealogy**, all `v` in the relay collar, and all sufficiently large dyadic levels.

This is the key transfer from a pointwise action theorem to a localized packet estimate.

## 6. Curl generation cannot erase (P14)

The source Lemma 7.7 states that if `t_m in W^alpha`, then its curl potential and remainder satisfy

\[
C_m\in W^{\alpha+1/2},
\qquad
r_m\in W^{\alpha+1/2-\kappa_s},
\]

and the full curl-generated velocity is exactly divergence free.

Crucially, the definition of `W^alpha` retains the **same pointwise envelope `P(v)`**; the curl step changes only the epsilon exponent and polynomial coefficient bounds.

Thus applying the curl construction to a coefficient carrying the extra factor

\[
\exp\!\left(-\frac{\delta_*}{2}\Lambda_\ell\right)
\]

preserves that factor. The curl remainder even gains the algebraic exponent `1/2-kappa_s`.

## 7. Amplitude inversion cannot erase (P14)

Proposition 7.2 proves the forward propagator estimate

\[
\|V_m(v,w)\|
\le C\frac{P(v)}{P(w)}
\tag{P15}
\]

and consequently maps a source bounded by `epsilon^alpha S_*^C P(w)` to a response bounded by the **same envelope `P(v)`**, with only an additional polynomial factor from integration and differentiated coefficients.

Therefore, if an action-subcritical source obeys

\[
|f(v)|
\le
C\varepsilon^\alpha S_*^C
\exp\!\left(-\frac{\delta_*}{2}\Lambda_\ell\right)
P_{a,b}(v),
\]

then the pulse inverse gives

\[
\boxed{
|t(v)|
\le
C\varepsilon^\alpha S_*^{C'}
\exp\!\left(-\frac{\delta_*}{2}\Lambda_\ell\right)
P_{a,b}(v).
}
\tag{P16}

There is no factor `exp(+c S_*)`.

The source states Proposition 7.2 for a fixed finite harmonic family. Thus (P16) is a rigorous **finite-stage** statement. A uniform infinite-lattice norm is addressed in Section 12 below as the next unresolved step.

## 8. Linear residual terms preserve the action factor

Proposition 9.1 expands the exact linearized residual after the pulse inverse and curl construction. Relative to a source exponent `alpha`, every displayed non-cutoff term gains at least

\[
\frac12-3\kappa_s>0
\]

in the epsilon exponent. The phase-transport defect contributes only polynomial `S_*` factors.

Hence, if the input carries the flat action factor in (P16), every supported non-cutoff linear residual carries the same factor, multiplied only by

\[
\varepsilon^\rho S_*^C
\]

for a fixed exponent `rho` at that finite step.

Likewise Lemma 9.2 shows that the apparent carrier half-power in wave-wave transport is removed by exact incompressibility; the remaining class loss is algebraic (`kappa_s`), not exponential in `S_*`.

Thus the source-localized PDE operators occurring in the finite correction calculus do not create an exponential gain capable of cancelling (P14).

## 9. A relay-compatible temporal cutoff

The stock source cutoff (6.16) is centered on the original standard pulse and is not adapted to the v0.8 relay location near `x≈2^{-2/3}`. It should **not** be imported unchanged.

The proof of the source cutoff identity (7.40), however, uses only:

1. a smooth cutoff compactly supported inside the raw pulse interval;
2. a plateau containing the region where the pulse is used;
3. transitions located where the relevant Gaussian envelope is exponentially small;
4. derivative bounds obtained by rescaling a fixed cutoff.

For one frozen v0.8 design, the beta-two turning point is strictly above `x=1/2` and the unit-beta turning point is `x=1`. The relay coordinates stay a fixed positive distance from the raw endpoints `1/2,3/2`. We may therefore choose smooth label-dependent cutoffs with plateau containing the bounded relay collar and with transition regions a fixed positive `x`-distance from each relevant turning point and from the raw endpoints.

On each transition region the Gaussian estimate gives

\[
P(v)\le C e^{-c_ML_s}
\le C e^{-c_MS_*}.
\tag{P17}

The derivatives of a cutoff rescaled on an `x`-interval contribute only powers of `L_s^{-1}`; even a bounded-`v` local cutoff contributes at worst fixed/polynomial factors. In either case (7.40) becomes

\[
(1-\psi)f+\psi't,
\]

with the same exponential action/tail factor.

Thus the shifted cutoff required by v0.8 creates no positive exponential loss. This is a **derived extension of the source cutoff argument**, not a statement that the published fixed cutoff itself already contains the v0.8 relay point.

## 10. Physical derivatives preserve flatness

At any fixed finite correction depth and fixed physical derivative order, the source conversion from normalized to physical variables contributes a fixed power of `Q^{-1}` and polynomial powers of `S_*`. The wave calculus may also contribute a fixed power `epsilon^{-D}`.

For the action-subcritical factor in (P14),

\[
\exp\!\left(-\frac{\delta_*}{2}\Lambda_\ell\right)
\le e^{-c_MS_*}
=e^{-c_M\ell^2}.
\]

Since

\[
Q=2^{-\ell},
\qquad
\varepsilon=Q^h,
\]

we have for every fixed `A,B,C`

\[
Q^{-A}\varepsilon^{-B}S_*^C e^{-c_MS_*}
=
\exp\big(-c_M\ell^2+O(\ell)+O(\log\ell)\big)
\to0.
\tag{P18}

Indeed it beats every prescribed positive power of `q` after increasing `ell_0`.

Therefore the action gap is invariant under all **fixed finite compositions** of the source-localized operations audited above.

## 11. Finite-stage source-localized action-preservation theorem

Fix one sufficiently large v0.8 design integer `M`, then freeze `u_*=M^2`. There exist a fixed bounded relay collar, a sufficiently large dyadic threshold `ell_0`, and a constant `c_M>0` such that the following holds for every `ell>=ell_0`.

For every non-designated principal-growing lattice genealogy generated inside the relay supernode, the exact localized coefficient obtained by any fixed finite composition of

- designated coefficient products;
- common-torus pullback;
- normalized coefficient derivatives from Proposition 6.6;
- curl generation from Lemma 7.7;
- the pulse inverse from Proposition 7.2;
- supported linear-residual operations from Proposition 9.1;
- wave-wave transport using the incompressibility gain of Lemma 9.2;
- relay-compatible smooth temporal cutoffs;

retains a factor

\[
\boxed{e^{-c_MS_*}.}
\tag{P19}

No audited operation produces `e^{+cS_*}`. In particular, the v0.8 principal global action filter survives passage from ideal envelope monomials to the **finite-stage localized curl-generated coefficient calculus**.

## 12. The new remaining local barrier: stage-uniform lattice closure

The source paper only needs each correction stage to contain a finite harmonic set, and its differentiated inverse estimates are stated stage-by-stage. Its construction is allowed to leave additive flat residuals that become part of the external force.

The unforced program needs more. We must correct the flat descendants **exactly**, which naturally leads to an infinite harmonic correction problem.

The remaining local question is therefore not whether one localized operation destroys the v0.8 action deficit; this theorem rules that out. The new question is whether all stages can be closed in one weighted lattice norm with constants uniform in harmonic index and correction depth.

A natural next space is an analytic convolution algebra such as

\[
\|z\|_{\sigma}
=
\sum_{(a,b)\in\mathbb Z^2}
 e^{\sigma(|a|+|b|)}
\|z_{a,b}\|_{\rm packet},
\tag{P20}

possibly augmented by the action weight from (P14). The submultiplicative identity

\[
e^{\sigma|\nu+\mu|_1}
\le
 e^{\sigma|\nu|_1}e^{\sigma|\mu|_1}
\]

makes quadratic lattice convolution bounded. What remains to prove is a **uniform full-symbol right inverse** in that norm, together with the finite compact-support compatibility block.

That is now the sharp local zero-force target.
