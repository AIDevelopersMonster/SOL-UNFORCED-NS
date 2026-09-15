# Mean-orbit harmonic split and covariance audit for the low-`u` boundary-layer cell

**Status:** PROVED HARMONIC-SECTOR / ACTION-WEIGHT REDUCTION; EXACT WHOLE-SPACE MEAN OPERATOR BOUND STILL OPEN.  This note continues the correction in `beta21_lowu_designated_mean_root_coupled_reduction.md` and places **all** beta-zero multiples of the reset root in the angular-mean lattice.

The principal root

\[
M=P-2C
\]

is extracted as the designated mean mode.  Every multiple `rM` also has beta zero and is therefore angularly invariant.  Differences of the beta-one or beta-two orbit packets generate such modes, but their physical source action is exponentially below the designated root.  The phase-adapted analytic lattice weight at `sigma_0=0.005` consumes only a tiny fraction of this gap.

Thus the only order-one beta-zero mean coordinate is the preloaded `M_des`; the remaining `rM` family is a small residual mean forcing.  No exact reset cell is claimed here.

## 1. Angular-mean classification

The source harmonic field has angular frequency `j k_p`, and its normalized angular integral keeps exactly the zero angular character.  In the beta-relay notation, beta is the tangential/angular coefficient.  Therefore

\[
\boxed{
\beta(K)=0
\Longrightarrow
K\text{ belongs to the angular-mean sector.}
}
\tag{MO1}
\]

For

\[
M=P-2C
\]

we have `beta(M)=0`, hence for every integer `r`,

\[
\boxed{
\beta(rM)=0.
}
\tag{MO2}
\]

Consequently the identities

\[
C_j-C_k=(j-k)M,
\]

\[
Q_n-Q_m=(n-m)M
\]

produce **mean-lattice coefficients**, not nonzero angular harmonics.

## 2. Designated versus residual beta-zero modes

The boundary-layer Poincare mechanism preloads one nonzero root amplitude in the `r=1` character.  Reality supplies its conjugate `r=-1`.  Define

\[
\boxed{
\mathcal M_{des}=\{\pm M\}.
}
\tag{MO3}
\]

Every other beta-zero multiple belongs to the residual phase-adapted mean lattice:

\[
\boxed{
\mathcal M_{res}
=\{rM:r\in\mathbb Z,\ r\ne\pm1\}.
}
\tag{MO4}
\]

The zero character `r=0` is the genuine nonoscillatory angular mean.  Nonzero `rM` are angularly invariant but retain an auxiliary/spatial reconstructed phase and are naturally represented by the coefficient mean space

\[
\mathfrak M_{\sigma,m_0}
=
\sum_{k\in\mathbb Z^2}
 e^{\sigma|k|_1}
 \|M_{\ell,k}m_k\|_{H^{m_0}}.
\]

This is exactly the setting of `phase_adapted_whole_space_leray_intertwining.md`.

## 3. Orbit index ranges

Use

\[
u=1.8,\qquad x=0.70,\qquad w=0.03,\qquad
\delta_S=\kappa/S,
\]

with

\[
\kappa=0.894049167184884\ldots.
\]

For catalyst modes the slope spacing is `2 delta_S`, so

\[
|j|\le \frac{wS}{2\kappa}+O(1).
\tag{MO5}
\]

Therefore a catalyst difference has

\[
|r|=|j-k|\le\frac{wS}{\kappa}+O(1).
\tag{MO6}
\]

For parent modes the slope spacing is `delta_S`, hence

\[
|n|\le \frac{wS}{\kappa}+O(1)
\tag{MO7}
\]

and

\[
|r|=|n-m|\le\frac{2wS}{\kappa}+O(1).
\tag{MO8}
\]

Since

\[
M=(1,-2)
\]

in the `(P,C)` lattice basis,

\[
\boxed{|rM|_1=3|r|.}
\tag{MO9}
\]

Thus the conservative mean-lattice index bounds are

\[
\boxed{
|rM|_1
\le C_{M,C}S+O(1),
\qquad
C_{M,C}:=\frac{3w}{\kappa}
\approx0.10067,
}
\tag{MO10}
\]

for catalyst differences and

\[
\boxed{
|rM|_1
\le C_{M,Q}S+O(1),
\qquad
C_{M,Q}:=\frac{6w}{\kappa}
\approx0.20134,
}
\tag{MO11}
\]

for parent differences.

## 4. Physical source-action gaps

At the center `z=x`, the natural beta-one and beta-two actions satisfy numerically

\[
2\mathcal E_1(x)\approx-0.17695,
\]

\[
2\mathcal E_2(x)\approx-0.23457.
\]

A difference interaction uses one mode and the conjugate of another, so its source action is the sum of the two physical input actions.  The bilateral large-deviation weights have maximum zero only at the orbit center and are nonpositive elsewhere.  Hence the center values give conservative ceilings for the entire truncated orbit:

\[
\boxed{
A_{C-\bar C}^{mean}\le-\gamma_{M,C},
\qquad
\gamma_{M,C}\approx0.1769,
}
\tag{MO12}
\]

and

\[
\boxed{
A_{Q-\bar Q}^{mean}\le-\gamma_{M,Q},
\qquad
\gamma_{M,Q}\approx0.2345.
}
\tag{MO13}
\]

These are fixed reduced-action deficits relative to the designated root scale.

The genuine zero auxiliary character `r=0` produced by exact conjugate pairs is governed by the ordinary source covariance estimate

\[
W_{1/2}\times W_{1/2}\to M_{1-\kappa_s};
\]

it is not promoted to the designated `M_{1/2}` scale.

## 5. Analytic mean-lattice budget

Fix the already selected

\[
\boxed{\sigma_0=0.005.}
\]

For catalyst-difference mean modes, the worst analytic exponent is

\[
\sigma_0 C_{M,C}
\approx5.04\times10^{-4}.
\]

For parent-difference modes,

\[
\sigma_0 C_{M,Q}
\approx1.01\times10^{-3}.
\]

Therefore

\[
\boxed{
\gamma_{M,C}-\sigma_0C_{M,C}>0.176,
}
\tag{MO14}
\]

and

\[
\boxed{
\gamma_{M,Q}-\sigma_0C_{M,Q}>0.233.
}
\tag{MO15}
\]

up to harmless `O(1/S)` endpoint corrections.

Thus the mean analytic weight is negligible compared with the physical action deficit of generated beta-zero modes.

## 6. Multiplicity and fixed derivative order

The orbit contains `O(S)` active characters at one point.  For a fixed output difference `r`, the number of pairs `(j,k)` with `j-k=r` is at most `O(S)`; summing over all output `r` gives at most `O(S^2)` crude pair count.

At every fixed derivative order `m`, character differentiation and physical source reconstruction contribute only fixed powers of `S`, by `PhysicalGraphBounds.norm_character_jet`, `PhysicalWaveSum` local finiteness and `LabelSumBounds.bilinear_jet_bound`.

Hence there is a fixed exponent `A_m` such that the generated residual mean coefficients obey schematically

\[
\boxed{
\|F_{rM}^{gen}\|_{\mathfrak M_{\sigma_0,m_0}}
\le
S^{A_m}
\left[
 e^{-0.176S}+e^{-0.233S}
\right]
+S^{A_m}\varepsilon^{1-\kappa_s}.
}
\tag{MO16}
\]

The last term includes the genuine conjugate-pair covariance and the lower-order source/curl/frame corrections.

## 7. Nearly neutral beta-zero damping

In the boundary-layer geometry the normalized viscous rate of `rM` has the form

\[
\lambda_{rM}
=-c_M\left(\frac rS\right)^2.
\tag{MO17}
\]

For `|r|=O(S)` this gives uniform damping.  For fixed nonzero `r`, any modewise damping inverse would cost at most

\[
O(S^2/r^2).
\tag{MO18}
\]

This possible polynomial loss is harmless against (MO14)--(MO15):

\[
\boxed{
S^A e^{-0.176S}\to0
}
\tag{MO19}
\]

for every fixed `A`.

The preferred exact implementation is the forward whole-space mean propagator rather than a static inverse, so no singular `r=0` inversion is required.  Equation (MO18) is only a conservative fallback estimate for nonzero residual beta-zero modes.

## 8. Principal designated root self-source

The designated `r=\pm1` root is treated separately.  Its frozen principal polarization is orthogonal to its radial phase vector, hence

\[
\Pi_{mean}\mathcal B(M_{des},M_{des})=0
\]

at principal carrier order, as proved in `beta21_lowu_designated_mean_root_coupled_reduction.md`.

Therefore the estimates above are not contaminated by an order-`M_{1/2}` root self-stress.

## 9. Consequence for the mean decomposition

The complete angular mean may be written

\[
\boxed{
M_{des}+m_{res},
}
\]

where `M_des` contains only the prescribed `r=\pm1` root pair and

\[
m_{res}\in\mathfrak M_{\sigma_0,m_0}
\]

contains:

1. the genuine zero auxiliary mode;
2. all generated `rM`, `r\ne\pm1`;
3. the old whole-space mean/pressure correction and inherited tail.

The new generated `rM` forcing is exponentially smaller than the already allowed source mean scale after analytic weighting.  Thus it does not require a second designated beta-zero bank.

## 10. Remaining operator theorem

The remaining mean problem is not an action-filter problem.  It is to prove that the whole-space phase-adapted Leray--Oseen propagator linearized about

\[
U_{base}+M_{des}
\]

obeys a fixed-order bound with constants uniform (or at worst harmlessly polynomial) in `S`, while retaining the existing positive epsilon exponents in the residual mean contraction.

The next target is therefore

\[
\boxed{
\text{a designated-mean-root whole-space Oseen propagator theorem.}
}
\]

No exact unforced reset cell is claimed before that propagator and its coupling to the growing nonzero orbit are proved.
