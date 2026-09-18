# Low-`u` beta-(2,1) boundary-layer bilateral orbit reset

**Status:** SUPERSEDED IN ITS ONE-SIDED ROOT-SHIFT FORM. THE REAL CAUCHY ROOT CONTAINS BOTH `+M` AND `-M` CHARACTERS, SO THE PRINCIPAL GENERATOR MUST CONTAIN BOTH `R` AND `R^{-1}`. SEE `beta21_lowu_real_root_bidirectional_principal_reset.md`. THE ORBIT ALGEBRA, ACTION FUNCTIONS, AND LOW-`u` STABILITY ANALYSIS REMAIN USEFUL; THE OLD DISPERSION FORMULAS AND NUMBERS MUST NOT BE CITED AS THE CURRENT PRINCIPAL RESET. This note replaces the temporally controlled corrected cell by a genuinely Cauchy-realizable physical Fourier orbit state. The preferred working point is

\[
\boxed{u=1.8,\qquad x=0.70.}
\]

The cell uses the reset-invariant beta-zero character

\[
M=P-2C
\]

and the full bilateral orbits

\[
C_j=C+jM,
\qquad
Q_n=P+nM.
\]

The reset transvection acts by index translation. In the boundary-layer scaling

\[
\boxed{\delta_S=\kappa/S,}
\]

the only order-one principal interactions on a fixed orbit core are the beta-zero translations by `M`. All non-`M` beta-one/beta-two feedback has a fixed negative action gap, while beta-three and higher sectors are full-symbol stable at the selected low `u`.

The resulting limiting Poincare problem has explicit bilateral shift eigenprofiles. A concrete fixed point is found with a nonzero transversality determinant. Exact finite-`S` principal tuning follows by the implicit-function theorem with

\[
\kappa_S=\kappa_*+O(S^{-1}),
\qquad
\theta_S=\theta_*+O(S^{-1}).
\]

The unresolved theorem is the passage from this principal orbit problem, whose critical block has `O(S)` characters, to one exact phase-adapted zero-residual Navier--Stokes solve with uniform constants.

No global unforced blowup theorem is claimed.

## 1. Why the low-`u` regime is necessary

At the earlier `u=2.5` boundary-layer candidate, two neighboring beta-two parent phases produced a beta-four sum branch with positive action defect. The principal coefficient was only polynomially small in `delta`, which cannot beat a fixed positive action advantage on the `S` scale.

At `u=1.8`, however,

\[
(1+u^2)\,3^{-4/3}-1<0,
\qquad
(1+u^2)\,4^{-4/3}-1<0.
\]

Hence beta-three and beta-four have no real turning points in the source model. Their normalized full-symbol rates are uniformly negative on the compact positive slope region used below.

The parent beta-two and catalyst beta-one branches retain real turning structure, so the desired two-sector orbit dynamics remains available while the dangerous high-beta growing sectors are removed.

## 2. Actual source support and orbit core

The source Gaussian slot cutoff is supported in normalized slot coordinate

\[
\theta\in[1/6,5/6].
\]

The affine pulse coordinate used throughout this branch is

\[
z=\frac12+\theta.
\]

Thus the existing Gaussian-supported source class lies inside

\[
\boxed{z\in[2/3,4/3].}
\]

Choose

\[
\boxed{x=0.70}
\]

and the strict orbit core

\[
\boxed{|z-x|\le w,\qquad w=0.03.}
\]

Therefore

\[
0.67\le z\le0.73
\]

with a positive margin from both source endpoints.

## 3. Reset shear and physical orbit state

For beta-(2,1),

\[
R(P)=3P-4C,
\qquad
R(C)=P-C.
\]

With

\[
M=P-2C
\]

one has the exact shear identity

\[
\boxed{R(K)=K+\beta(K)M.}
\]

Hence

\[
R(M)=M.
\]

Define the bilateral orbit characters

\[
C_j=C+jM,
\qquad j\in\mathbb Z,
\]

and

\[
Q_n=P+nM,
\qquad n\in\mathbb Z.
\]

Then

\[
R(C_j)=C_{j+1},
\qquad
R(Q_n)=Q_{n+2}.
\]

Thus after relabelling to the next cell, the catalyst orbit shifts by one index and the parent orbit by two indices.

This is a physical Fourier Cauchy state. No future temporal control parameters are introduced.

## 4. Boundary-layer scaling

Let `S` be the large source length parameter and set

\[
\boxed{\delta_S=\kappa/S.}
\]

The reduced slope of an orbit mode changes by `O(1/S)` per lattice index. On the stretched cell clock

\[
\tau=St,
\]

the full reset interval has finite length

\[
0\le\tau\le2\kappa.
\]

The reset characters remain exactly integral; only their physical slope separation tends to zero.

This scaling has three simultaneous advantages:

1. action differences of order `delta` become finite `O(1)` weights after multiplication by `S`;
2. the Duhamel interaction interval remains finite in the stretched clock;
3. a dangerous near-zero unit-beta lattice character requires index depth `Theta(S)`, removing the earlier bounded-depth small-divisor obstruction.

## 5. Limiting rates

Use

\[
\Gamma_b(z)
=\frac1{\sqrt{1+u^2z^2}}
-b^2\frac{1+u^2z^2}{(1+u^2)^{3/2}}.
\]

At the working point define

\[
g_1=u\Gamma_1(x),
\qquad
g_2=u\Gamma_2(x).
\]

Numerically,

\[
\boxed{g_1=0.5855008057784036\ldots,}
\]

\[
\boxed{g_2=-1.0149492185320377\ldots.}
\]

Thus the beta-one orbit is on the favorable side of its turning point while the beta-two orbit has already crossed to negative local rate. The bilateral coefficient weights below compensate this drift at the Poincare level.

## 6. Limiting `M`-translation equations

At principal order the beta-zero root `M` translates orbit index. After the action/tangent normalization the beta-one and beta-two orbit vectors satisfy constant-coefficient shift equations of the form

\[
\partial_\tau c=a_C R c,
\qquad
\partial_\tau q=a_P R q,
\]

where `R` is the unit index shift. It is convenient to absorb the cell length `2kappa` into the full-cell semigroup parameters

\[
\lambda_C=2\kappa a_C,
\qquad
\mu_P=2\kappa a_P.
\]

Then one cell produces

\[
c_{out}=e^{\lambda_C R}c_{in},
\]

\[
q_{out}=e^{\mu_P R}q_{in}.
\]

The reset relabelling shifts the catalyst orbit back by one and the parent orbit back by two. Hence the limiting Poincare maps are

\[
\boxed{\mathcal P_C=R^{-1}e^{\lambda_C R},}
\]

\[
\boxed{\mathcal P_P=R^{-2}e^{\mu_P R}.}
\]

## 7. Bilateral eigenprofiles

Seek geometric shift eigenprofiles

\[
Rc=\rho_C c,
\qquad
Rq=\rho_P q.
\]

The fixed-point equations are

\[
\boxed{\frac{e^{\lambda_C\rho_C}}{\rho_C}=1,}
\tag{BL1}
\]

\[
\boxed{\frac{e^{\mu_P\rho_P}}{\rho_P^2}=1.}
\tag{BL2}
\]

The physical large-deviation balance fixes the moduli

\[
|\rho_C|=e^{-2\kappa g_1},
\]

\[
|\rho_P|=e^{-\kappa g_2}.
\]

Take `rho_C>0` and write

\[
\rho_P=e^{-\kappa g_2}e^{i\theta}.
\]

The two real parent fixed-point equations reduce to

\[
\boxed{\cos\theta=\frac{g_2}{2g_1},}
\tag{BL3}
\]

and on the first positive phase branch

\[
\boxed{
\kappa
=\frac{2\pi-2\theta}
{4g_1\sin\theta}.
}
\tag{BL4}

At the selected working point,

\[
\boxed{\theta=2.619416765747896\ldots,}
\]

\[
\boxed{\kappa_*=0.894049167184884\ldots.}
\]

Therefore

\[
\boxed{\rho_C=0.3510126502440001\ldots,}
\]

\[
\boxed{
\rho_P
=-2.147691668824314
+1.235899139340218\,i.
}
\]

The full-cell semigroup coefficients are

\[
\boxed{\lambda_C=-2.982607649202283\ldots,}
\]

\[
\boxed{\mu_P=-0.845013757547658\ldots.}
\]

Direct substitution gives

\[
\frac{e^{\lambda_C\rho_C}}{\rho_C}=1,
\qquad
\frac{e^{\mu_P\rho_P}}{\rho_P^2}=1
\]

up to floating evaluation error.

## 8. Physical bilateral localization

For `b=1,2`, define

\[
\Phi_b(z)
=\mathcal E_b(z)+(x-z)g_b,
\qquad
H_b(z)=\Phi_b(z)-\mathcal E_b(x).
\]

Then

\[
H_b'(z)
=u\bigl(\Gamma_b(z)-\Gamma_b(x)\bigr).
\]

For positive `z`, each `Gamma_b` is strictly decreasing. Hence

\[
\boxed{H_b(z)\le0}
\]

with equality only at `z=x`.

Thus the geometric growth of the normalized bilateral Fourier coefficients is exactly dominated by the physical envelope away from the center. The actual field is localized on both orbit tails.

At the chosen core boundary,

\[
H_1(0.67)\approx-8.61\times10^{-4},
\]

\[
H_1(0.73)\approx-8.63\times10^{-4},
\]

\[
H_2(0.67)\approx-2.106\times10^{-3},
\]

\[
H_2(0.73)\approx-2.143\times10^{-3}.
\]

Therefore truncating the formal bilateral eigenprofile to `|z-x|<=0.03` produces an exponentially small physical boundary tail `e^{-cS}`.

## 9. Principal nonlinear closure on the core

The exact orbit algebra contains

\[
C_j+C_k=Q_{j+k-1},
\]

\[
Q_n-C_j=C_{n-j+1},
\]

\[
C_j-C_k=(j-k)M.
\]

Dense optimization of the physical large-deviation action on the full core gives the fixed negative margins

\[
\boxed{
\max_{core}
\bigl[\Phi_1(z_1)+\Phi_1(z_2)-\Phi_2((z_1+z_2)/2)\bigr]
\le-0.05925018225\ldots,
}
\tag{BL5}
\]

for beta-one sum feedback, and

\[
\boxed{
\max_{core}
\bigl[\Phi_2(z_Q)+\Phi_1(z_C)-\Phi_1(2z_Q-z_C)\bigr]
\le-0.11675015251\ldots
}
\tag{BL6}
\]

whenever the target slope remains in the core.

Thus all non-`M` beta-one/beta-two feedback is exponentially smaller than the designated orbit state by a fixed factor `e^{-gamma S}`.

The beta-zero harmonics produced by differences of equal-beta orbit packets are also exponentially small compared with the preloaded invariant `M` channel. At the center,

\[
2\mathcal E_1(x)\approx-0.17695,
\]

\[
2\mathcal E_2(x)\approx-0.23457.
\]

Finally, beta-three and beta-four have no real turning branches at `u=1.8`, so mixed higher-beta sectors lie in the uniformly stable full-symbol complement rather than a competing growing action layer.

Therefore the **only order-one principal critical dynamics on the core is the `M`-translation shift** used in Sections 6--7.

## 10. Finite-`S` verification

The companion script

`experiments/beta21_lowu_boundary_layer_audit.py`

records the limiting constants and a representative exact finite-`u` finite-`S` quadrature audit with

\[
\delta_S=\kappa_*/S.
\]

After tuning the normalized beta-zero prefactor so the catalyst multiplier is matched, the parent multiplier error behaves as

\[
\begin{array}{c|c}
S&|\mathcal P_P-1|\\ \hline
50&5.038\times10^{-2}\\
100&2.631\times10^{-2}\\
200&1.346\times10^{-2}\\
500&5.463\times10^{-3}\\
1000&2.745\times10^{-3}\\
2000&1.376\times10^{-3}\\
5000&5.511\times10^{-4}\\
10000&2.757\times10^{-4}.
\end{array}
\]

Thus the exact principal finite-`S` map approaches the limiting fixed point at the expected `O(S^{-1})` rate. The catalyst multiplier error in the same audit is `O(S^{-2})` after its scalar prefactor tuning.

## 11. Transversality and exact finite-`S` principal tuning

The catalyst scalar dispersion derivative is

\[
\frac{d}{d\rho}
\log\!\left(\frac{e^{\lambda_C\rho}}{\rho}\right)
=\lambda_C-\rho^{-1}.
\]

At the working point,

\[
\boxed{
\lambda_C-\rho_C^{-1}
=-5.83150782219\ldots\ne0.
}
\tag{BL7}

For the complex parent equation define

\[
F_P(\kappa,\theta)
=\frac{\exp(\mu(\kappa)\rho(\kappa,\theta))}
{\rho(\kappa,\theta)^2}.
\]

At the fixed point,

\[
\partial_\kappa F_P
\approx-1.1681144773\,i,
\]

\[
\partial_\theta F_P
\approx1.0443517758-0.1851709930\,i.
\]

Therefore

\[
\boxed{
\det D_{(\kappa,\theta)}
(\Re F_P,\Im F_P)
\approx1.2199224287\ne0.
}
\tag{BL8}

The finite-`S` principal map differs from the limiting map by `O(S^{-1})` on the fixed compact core. Hence the finite-dimensional implicit-function theorem gives parameters

\[
\boxed{
\kappa_S=\kappa_*+O(S^{-1}),
\qquad
\theta_S=\theta_*+O(S^{-1})
}
\tag{BL9}
\]

for which the parent principal multiplier is **exactly** one. Independently, the nonzero catalyst derivative (BL7) permits tuning its physical beta-zero amplitude/prefactor to impose the catalyst principal multiplier exactly.

Thus the observed finite-`S` convergence is transverse and can be upgraded to an exact finite-`S` principal renewal statement, not merely an asymptotic coincidence.

## 12. The growing-block issue

The orbit core contains index width

\[
N_S\asymp\frac{wS}{\kappa_*}.
\]

Hence the designated principal block has `O(S)` Fourier characters. This is qualitatively different from the fixed 3-, 9-, or 44-state blocks studied earlier in the branch.

Nevertheless its **physical** total size is small: every beta-one/beta-two orbit packet on the core carries a fixed negative center action, while the number of packets grows only linearly. Thus factors of `O(S)` are dominated by the exponential action weights.

The exact next theorem must place the orbit coefficients in a weighted sequence space adapted to `H_1,H_2`, solve the `M`-shift semigroup exactly, and prove that:

1. the `O(S)` counting constants remain only polynomial;
2. the fixed gaps (BL5)--(BL6) beat those polynomial losses;
3. the beta-three-plus stable complement retains a uniform inverse;
4. mean and curl corrections remain uniformly contractive;
5. boundary truncation contributes only `e^{-cS}`;
6. finite-`S` `O(S^{-1})` coefficient variation preserves the transverse fixed point.

Until this growing-block zero-residual theorem is proved, this note is a **principal autonomous Cauchy reset reduction**, not an exact unforced Navier--Stokes cascade cell.

## 13. Research consequence

The low-`u` boundary-layer route removes every defect that forced the earlier active-control architecture:

- no future temporal control profiles;
- no delayed passive-lobe collision assumption;
- no old-catalyst exact cancellation gate;
- no fixed-shear beta-zero parent obstruction;
- no beta-four growing shortcut at the selected `u`;
- no bounded-depth small-divisor witness.

The remaining barrier is now functional-analytic rather than algebraic:

\[
\boxed{
\textbf{uniform exact PDE closure for an }O(S)\textbf{-dimensional weighted orbit block.}
}
\]

That is the next target.
