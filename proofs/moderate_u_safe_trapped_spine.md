# A trapped background spine inside a source-safe moderate-`u_*` region

**Status:** PROVED SOURCE-DERIVED EXISTENCE THEOREM AFTER REFINING THE ALLOWED PROFILE PARAMETER CHOICES. There exists a choice of the finite parameters in the OpenAI leading-profile construction for which one fixed compact rectangle in the active annulus simultaneously has

1. the exact Section 7 cone inequality for `u_*=4` with a fixed margin;
2. opposite signs of the similarity radial velocity coefficient `W` on its two radial faces;
3. opposite signs of the similarity axial coefficient `H_c` on its two axial faces.

Consequently the rectangle contains a leading stationary point `W=H_c=0`, and the realized background `u_B` has an exact late-time material characteristic trapped in the same `u_*=4`-safe rectangle. This closes the geometric safe-set barrier isolated in `localized_moderate_u_source_window.md`.

This theorem does **not** yet construct the unforced oscillatory relay on that spine. The remaining barrier is the support-gated finite supercell/PDE renewal itself.

Primary source: OpenAI, *Finite Time Blowup for Navier--Stokes*, Proposition 4.10, Lemma 4.5, Theorem 4.6, Proposition B.5 and (B.29)--(B.31), Corollary B.10, Proposition A.4 and (A.24)--(A.27), Lemma C.1, Proposition C.2, Proposition C.3, and Proposition 5.5.

## 1. The phase-cone quantity

For the final leading profile write

\[
\mathcal R(X,\eta)
:=
\left|
 c_0\frac{T_0\cdot K}{T_0\cdot N}
\right|
=
\sqrt{\frac{v_s-2}{2}}
\left|
\frac{n_z-t_sn_\theta}{n_\theta+t_sn_z}
\right|,
\tag{MS1}
\]

with `n=T_0/|T_0|`. A fixed Section 7 value `u_0>0` is admissible wherever

\[
\mathcal R<\vartheta(u_0),
\qquad
\vartheta(u_0)=\frac{u_0}{\sqrt{1+u_0^2}}.
\tag{MS2}
\]

For the cleanup design

\[
\boxed{
u_0=4,
\qquad
\vartheta_4:=\frac4{\sqrt{17}}\approx0.9701425.
}
\tag{MS3}
\]

We now strengthen the source parameter choices so that one whole radial corridor joining a negative-`W` face to a positive-`W` face satisfies

\[
\boxed{\mathcal R\le r_4<\vartheta_4}
\tag{MS4}
\]

for one fixed `r_4`.

## 2. A negative-`W` left face with arbitrarily small cone ratio

At the stress activation edge `X=X_a`, Proposition B.5 gives the exact flat factorization

\[
T_0=e_aB_0,
\qquad
B_0(0,\eta)=F p_{s,r}\ne0,
\tag{MS5}
\]

and the limiting stress direction is parallel to the limiting shear. Hence

\[
\mathcal R(X_a,\eta)=0
\]

uniformly in `eta`.

More quantitatively, the source estimates (B.29) give on the first activation collar, in the logarithmic coordinate

\[
y=\log(X/X_a),
\]

\[
P_c-v_s\ge c e_a,
\qquad
J_c=O(ye_a),
\tag{MS6}
\]

and the proof explicitly notes that the ratio of the quadratic cone numerator to `(P_c-v_s)^2` is `O(y^2)`. Therefore, after shrinking the allowed activation width `t_1>0`, one can arrange

\[
\boxed{
\sup_{0\le y\le t_1,\ |\eta|\le1}\mathcal R(X,\eta)
<\frac14.
}
\tag{MS7}
\]

This is compatible with the source parameter hierarchy: Proposition 4.10 chooses `t_1` after the earlier finite axis parameters and after the amplitude normalization has been fixed.

On the same collar, the analytic-axis calculation gives

\[
W=W_*+\Lambda^{-1}B,
\qquad
-W_*>2.8.
\tag{MS8}
\]

After the already allowed choice of sufficiently large `Lambda`, shrink the collar once more if necessary and choose a radial point

\[
\boxed{X_L\in(X_a,X_ae^{t_1})}
\tag{MS9}
\]

such that uniformly in `eta`,

\[
\boxed{W(X_L,\eta)\le-c_L<0}
\tag{MS10}
\]

and (MS7) holds on a full neighborhood of `X_L`.

## 3. A positive-`W` right face in the intermediate power-law region

The outer reference construction first drives the axial profile to zero. At the transition into the intermediate power-law interval, the source writes

\[
A_X(U)=\bar k\eta,
\]

and the final eleven zero-`U` units of the preceding stage give

\[
L\bar k<\frac12.
\]

Hence source (A.5) gives

\[
\boxed{W=1-L\bar k\ge\frac12}
\tag{MS11}
\]

on the next transition. On the following constant-slope interval `\bar k` decays exponentially, so the same positive sign persists. Also

\[
\boxed{U=0}
\tag{MS12}
\]

throughout the intermediate power-law interval.

Choose

\[
\boxed{X_R}
\tag{MS13}
\]

inside this interval, before the first reserved correction patch of (A.9), so that a fixed radial neighborhood of `X_R` obeys

\[
\boxed{W(X_R,\eta)\ge c_R>0}
\tag{MS14}
\]

uniformly in `eta`.

We also need this right neighborhood to be `u_*=4` safe. Here the source has

\[
b_s=0,
\qquad
v_s=a=2+O(\lambda),
\tag{MS15}
\]

and writes

\[
w=\frac{N_s}{EQ_s}.
\]

The explicit estimate (A.27) is

\[
\boxed{
\sqrt\lambda\,|w|
\le
C_{\rm pre}\sqrt\lambda(1+y)e^{\lambda y/2}
=o(1)
}
\tag{MS16}
\]

uniformly over the entire intermediate power-law interval

\[
0\le y\le60\log(1/\lambda).
\]

When `b_s=0`, `t_s=0`, `v_s=a`, and source (4.23) gives

\[
\frac{n_z}{n_\theta}
=
\frac{J_c}{P_c-a}.
\tag{MS17}
\]

The large-radius step in Proposition A.4 makes `p_{s,1}=P_c` arbitrarily large on this fixed logarithmic interval. Since `J_c=p_{s,1}w` when `b_s=0`, first choose `lambda` small and then the permitted large radial scale `X_R^{\rm source}` large enough that

\[
\boxed{
\mathcal R<\frac12
}
\tag{MS18}
\]

on the transition into, and on the initial portion of, the intermediate power-law interval containing our chosen `X_R`.

The order of these choices is exactly the source order: `lambda` is fixed before the final large radial scale/amplitude normalization.

## 4. Strengthening the Appendix C modulation corridor

Let

\[
I=[X_-,X_+]
\]

be the radial modulation interval of Appendix C. The source allows `X_-` to start inside the first admissible inner collar and `X_+` to end in the intermediate power-law interval before its first reserved patch. Choose them so that

\[
X_-<X_L<X_R<X_+
\]

with the endpoint neighborhoods contained in the quantitative safe neighborhoods constructed above.

The input joined profile has the following radial regimes between these neighborhoods.

- After the first inner activation transition, Proposition B.5 continues the inner profile with `v_s<1` through the remaining joining segment.
- The reference outer profile has `v_s\le2` through the inner reference and axial transition.
- Only on the transition into the intermediate power-law interval does `v_s` rise slightly above `2`, by `O(lambda)`; that entire region has the explicit safe estimate (MS18).

Lemma C.1 introduces a cutoff `zeta_L(v_s)`. Wherever

\[
v_s\le2+\delta_L/8,
\]

the loop uses the fixed scalar

\[
v_*=2+\delta_L/2.
\]

For the variance-active states the exact quadratic-cone identity gives

\[
\boxed{
\mathcal R_{\rm loop}^2<\frac12,
\qquad
\mathcal R_{\rm loop}<\frac1{\sqrt2}.
}
\tag{MS19}
\]

This is the estimate established in `localized_moderate_u_source_window.md` from source (C.8)--(C.10).

Where the cutoff vanishes, the loop equals the original shear. On our chosen `I`, those portions are contained either in the quantitatively safe first inner collar or in the quantitatively safe `O(lambda)` intermediate-power transition described by (MS7) and (MS18). Therefore the complete ideal loop on `I` satisfies a fixed bound

\[
\boxed{
\mathcal R_{\rm loop}\le r_*<\vartheta_4.
}
\tag{MS20}
\]

The gap is fixed because

\[
\max\left\{\frac14,\frac1{\sqrt2},\frac12\right\}
=\frac1{\sqrt2}
<\frac4{\sqrt{17}}.
\]

Proposition C.2 realizes the loop at a finite radial frequency `N`. Its exact shears differ from the loop values by `O(N^{-1})`, while `p_s` differs by `O(N^{-1})`; see (C.13)--(C.16). Since (MS20) is a strict compact inequality, choose the permitted finite `N` sufficiently large to preserve, for the **actual final profile** on `I`,

\[
\boxed{
\mathcal R(X,\eta)\le r_4<\frac4{\sqrt{17}}
\qquad
(X,\eta)\in I\times[-1,1].
}
\tag{MS21}
\]

The antiderivatives in (C.11) vanish identically on the radial boundary neighborhoods of `I`, so the modulation does not change the profiles at our sign faces. The later five-moment restoration is supported in the first reserved patch, strictly to the right of `X_+`; with the common axis pressure datum it does not alter the already constructed corridor.

Thus the final source profile contains the compact rectangle

\[
\boxed{
\mathcal Q_4=[X_L,X_R]\times[-1,1]
}
\tag{MS22}
\]

on which the exact leading Section 7 cone condition holds uniformly for `u_*=4`.

## 5. A stationary point inside the `u_*=4` safe rectangle

Recall

\[
H_c=D\eta+(1-\eta^2)U.
\tag{MS23}
\]

At the axial faces,

\[
\boxed{
H_c(X,-1)=-D<0,
\qquad
H_c(X,1)=D>0
}
\tag{MS24}
\]

for every `X`, independently of the profile details.

On the radial faces, (MS10) and (MS14) give

\[
\boxed{
W(X_L,\eta)<0,
\qquad
W(X_R,\eta)>0
}
\tag{MS25}
\]

uniformly for `|eta|<=1`.

Therefore the continuous map

\[
(X,\eta)\longmapsto(W(X,\eta),H_c(X,\eta))
\]

satisfies the Poincare--Miranda sign conditions on `Q_4`. Hence there exists

\[
\boxed{
(X_4,\eta_4)\in(X_L,X_R)\times(-1,1)
}
\tag{MS26}
\]

such that

\[
\boxed{
W(X_4,\eta_4)=0,
\qquad
H_c(X_4,\eta_4)=0.
}
\tag{MS27}
\]

By (MS21), this stationary point lies in a region where the exact source phase cone permits

\[
\boxed{u_*=4.}
\tag{MS28}
\]

Thus the previously separate facts

- `u_*=4` is source-safe somewhere, and
- a stationary profile point exists somewhere,

can be made true **at the same profile location** within one allowed source construction.

## 6. Exact realized-background spine remains in the same safe set

For the realized background `u_B`, Proposition 5.5 gives the normalized material-coordinate system

\[
\frac{dX}{d\sigma}
=\frac dL\left(XW+R_X\right),
\qquad
\frac{d\eta}{d\sigma}
=\frac dL\left(H_c+R_\eta\right),
\tag{MS29}
\]

with

\[
|R_X|+|R_\eta|\le Ce^{-2h\sigma}
\tag{MS30}
\]

on compact profile rectangles bounded away from `eta=+-1`, where

\[
\sigma=-\log(1-t).
\]

By continuity of (MS24), choose one fixed `delta_eta>0` so small that on

\[
\eta_-=-1+\delta_\eta,
\qquad
\eta_+=1-\delta_\eta,
\]

we retain uniform strict signs

\[
H_c(X,\eta_-)\le-c_\eta<0,
\qquad
H_c(X,\eta_+)\ge c_\eta>0
\tag{MS31}
\]

for `X_L<=X<=X_R`.

Set

\[
\boxed{
\mathcal Q_4'
=[X_L,X_R]\times[\eta_-,\eta_+].
}
\tag{MS32}
\]

For all sufficiently large `sigma`, (MS29)--(MS31) and the strict radial signs imply that the forward profile vector field points outward on all four faces of `Q_4'`:

\[
\dot X<0\text{ at }X=X_L,
\qquad
\dot X>0\text{ at }X=X_R,
\]

\[
\dot\eta<0\text{ at }\eta=\eta_-,
\qquad
\dot\eta>0\text{ at }\eta=\eta_+.
\tag{MS33}
\]

Hence the reverse-time field points strictly inward. Applying exactly the compact backward-shooting argument of `profile_characteristic_trapped_spine.md` gives an exact material characteristic of `u_B` satisfying

\[
\boxed{
(X(\sigma),\eta(\sigma))\in\mathcal Q_4'
\quad\text{for every sufficiently large }\sigma.
}
\tag{MS34}
\]

Since `Q_4'` is a compact subset of the `u_*=4` safe corridor and `eta` stays away from the endpoints,

\[
q(\sigma)=\frac{e^{-\sigma}}{1-\eta(\sigma)^2}
\asymp e^{-\sigma}\to0.
\tag{MS35}
\]

Thus there is an **exact physical background spine approaching the singular point while remaining forever inside one fixed moderate-`u` source-safe similarity region**.

The fixed margin in (MS21) also absorbs the `O(q^{2h})` background/frame corrections used at sufficiently high dyadic levels. Therefore the same frozen packet value `u_*=4` can be used uniformly along all sufficiently late relay stages placed on this spine, at the level of the source phase-cone inequalities.

## 7. Combination with the finite-`u` cleanup supercell

`beta21_finite_u_cleanup_window.md` proves that the exact source envelope at `u_*=4` admits the beta-(2,1) turning-point cleanup design, including

\[
\Delta_{\rm clean}(4)<0,
\]

and a causal ordered reset branch. The present theorem places the background relay spine in a region where **the same numerical value `u_*=4` is source-admissible at every sufficiently late scale**.

Consequently the following compatibility package is now closed at the source/principal geometric level:

\[
\boxed{
\begin{gathered}
\text{exact finite-}u_*=4\text{ relay/reset/cleanup envelope},\\
\text{nonzero principal collision polarizations},\\
\text{causal ordered microcollars},\\
\text{exact Section 7 cone admissibility on a fixed active rectangle},\\
\text{exact realized-background material spine trapped in that rectangle}.
\end{gathered}}
\tag{MS36}
\]

This removes the previous concern that the relay could be source-safe only at isolated locations that a physical characteristic could not revisit.

## 8. New frontier

The dominant unresolved issue is now **not** the background geometry and not the moderate-`u` source cone. It is the nonlinear support/routing architecture of the wave state.

The next theorem must show that a finite support-gated supercell can be embedded along the trapped spine so that

\[
(P,C)\longmapsto(P_{\rm new},D)
\]

with the exact finite-`u=4` amplitude/phase reset, while

- the spent old catalyst `C` is exponentially discarded;
- dangerous high-genealogy modes such as `7D-6C` never acquire a common propagated support leading into the next cell;
- all unintended sibling outputs are either support-separated or enter a forward-stable correction class;
- the local phase-adapted zero-residual contraction remains uniform over repeated cells.

Until that support-gated PDE theorem is proved, the global autonomous unforced cascade and finite-time blowup remain open.