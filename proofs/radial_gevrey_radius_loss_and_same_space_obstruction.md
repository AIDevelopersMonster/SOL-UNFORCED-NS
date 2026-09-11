# Radial Gevrey radius loss and the same-space compactification obstruction

**Status:** PROVED LOCAL FUNCTIONAL-ANALYTIC OBSTRUCTION / CORRECTED GE VREY ESTIMATE.

This note audits the radial compactification operator from OpenAI Section 8.2 in the exact functional setting needed by the unforced program. It has two conclusions.

1. A compactly supported Gevrey source gives a quantitatively tiny cutoff remainder **after a fixed loss of Gevrey radius**.
2. On an unrestricted one-radius Gevrey space, the radial cutoff operator is **not** an `o(1)` operator as the radial phase parameter grows. Near-resonant torus modes prevent such a bound.

Therefore the earlier idea that the radial compactification remainder can simply be inserted as one more small block in a single fixed-radius Banach contraction is not justified. The radial block must either be handled on a scale of Gevrey spaces or removed by an input-output reformulation that does not require two-sided radial compact support.

Throughout, the symbol `M_r` denotes the **radial phase parameter** from source equation (6.6), not the frozen integer relay-design parameter `M` used elsewhere in the v0.8 beta family.

## 1. Source operator in straightened radial coordinates

On one common torus, source Section 8.2 introduces

\[
D_r=\partial_R+M_r d_rR^{d_r-1}L_r,
\qquad
L_r=v_r\cdot\partial_y,
\]

with

\[
\boxed{
M_r\asymp \varepsilon^{-\kappa_s}S_*^{-\rho_g}.
}
\tag{RG1}
\]

After the change of variable

\[
U=R^{d_r},
\]

the full-line phase-following integral appearing in the compact primitive has the model form

\[
\boxed{
(J_{M_r}F)(U,y)
=
\int_{\mathbb R}
F(U+u,y+M_ruv_r)\,du.
}
\tag{RG2}
\]

The actual cutoff remainder `A_e`, `e in {0,1,2}`, differs from a fixed compactly supported multiplier times `J_{M_r}` only by bounded radial weights and the fixed change between `R` and `U` on the active shell.

The source Diophantine estimate is

\[
\boxed{
|v_r\cdot k|\ge \frac{c_0}{1+|k|},
\qquad k\in\mathbb Z^2\setminus\{0\}.
}
\tag{RG3}
\]

## 2. Exact Fourier sampling formula

Write

\[
F(U,y)=\sum_{k\in\mathbb Z^2}F_k(U)e^{2\pi i k\cdot y}
\]

and use the Fourier convention

\[
\widehat F_k(\xi)=\int_{\mathbb R}F_k(U)e^{-2\pi i\xi U}\,dU.
\]

A change of variable in (RG2) gives, for every torus mode,

\[
\boxed{
(J_{M_r}F)_k(U)
=
e^{-2\pi iM_r(v_r\cdot k)U}
\widehat F_k\!\left(-M_r(v_r\cdot k)\right).
}
\tag{RG4}
\]

This formula is the sharp form of the repeated integration-by-parts argument in source Lemma 8.2.

If the weighted radial Haar moment vanishes, then the `k=0` term of the relevant full-line integral vanishes exactly. Hence only `k != 0` enters the compactification remainder.

## 3. Joint Gevrey Fourier decay

Fix `s>1`. On a compact radial interval, use a standard joint Gevrey norm whose Fourier characterization implies

\[
\boxed{
|\widehat F_k(\xi)|
\le
C\|F\|_{G^s_{L_0}}
\exp\!\left[-L_0\bigl(|k|+|\xi|\bigr)^{1/s}\right]
}
\tag{RG5}
\]

for some radius `L_0>0`. Equivalent product weights such as
`exp[-L_0(|k|^{1/s}+|xi|^{1/s})]` give the same conclusion below.

Let

\[
0<L_2<L_1<L_0.
\]

Insert (RG4) into (RG5). In the weaker radius `L_1`, the sampled mode carries the factor

\[
\exp\!\left[-(L_0-L_1)
\bigl(|k|+M_r|v_r\cdot k|\bigr)^{1/s}\right].
\]

By (RG3),

\[
|k|+M_r|v_r\cdot k|
\ge
|k|+\frac{c_0M_r}{1+|k|}
\ge c_1\sqrt{M_r}
\]

for all `k != 0` and all sufficiently large `M_r`. Therefore

\[
\boxed{
|k|+M_r|v_r\cdot k|
\ge c_1M_r^{1/2}.
}
\tag{RG6}
\]

Consequently

\[
\boxed{
\|J_{M_r}F\|_{G^s_{L_1}}
\le
C_{L_0,L_1,s}
\exp\!\left[-c(L_0-L_1)M_r^{1/(2s)}\right]
\|F\|_{G^s_{L_0}}.
}
\tag{RG7}
\]

Multiplication by the fixed Gevrey cutoff derivative, the powers `R^{+/-e}`, and the fixed `R <-> U` coordinate change are bounded after one further fixed radius margin. Thus the actual source cutoff operators satisfy

\[
\boxed{
\|A_ef\|_{G^s_{L_2}}
\le
C
\exp\!\left[-cM_r^{1/(2s)}\right]
\|f\|_{G^s_{L_0}},
\qquad e=0,1,2,
}
\tag{RG8}
\]

provided the corresponding weighted Haar moment vanishes.

Using (RG1), this is

\[
\boxed{
\|A_ef\|_{G^s_{L_2}}
\le
C\exp\!\left[
-c\varepsilon^{-\kappa_s/(2s)}
S_*^{-\rho_g/(2s)}
\right]
\|f\|_{G^s_{L_0}}.
}
\tag{RG9}
\]

This is a correct quantitative form of the source's `C^infty` flatness mechanism, but it is explicitly a **radius-losing** estimate.

## 4. Why the same-radius estimate is false

The loss of radius in (RG8) is not a technical artifact.

The source direction `v_r` is quadratic irrational. In the coordinates used to prove (6.7),

\[
v_r\cdot k=(k_1+k_2)-\sqrt2\,k_2.
\]

The continued-fraction convergents of `sqrt(2)` have bounded successive denominator ratios. Hence for every sufficiently large `M_r` one can choose a nonzero integer vector `k=k(M_r)` with

\[
\boxed{
|k|\asymp M_r,
\qquad
|v_r\cdot k|\lesssim |k|^{-1},
\qquad
M_r|v_r\cdot k|\lesssim 1.
}
\tag{RG10}
\]

Choose a fixed compactly supported Gevrey bump `psi(U)` and modulate it by a bounded radial frequency so that its Fourier transform is nonzero at the sampled value `-M_r(v_r dot k)`. Set

\[
F_{M_r}(U,y)
=a_{M_r}\psi_{M_r}(U)e^{2\pi i k\cdot y},
\]

where `a_{M_r}` normalizes the same-radius Gevrey norm to one.

Because `k != 0`, the Haar mean is zero and hence the weighted moment hypothesis required for the cutoff remainder is automatically satisfied. By (RG4) and (RG10), the sampled Fourier coefficient is bounded below by a fixed multiple of `|a_{M_r}|`. On any subinterval where the fixed cutoff derivative is nonzero, the resulting `A_eF_{M_r}` has the same torus frequency and a comparable normalized Gevrey size.

Thus there exists `c_*>0` and a sequence of admissible large radial parameters such that

\[
\boxed{
\|A_eF_{M_r}\|_{G^s_L}
\ge c_*\|F_{M_r}\|_{G^s_L}.
}
\tag{RG11}
\]

In particular, there is no estimate of the form

\[
\|A_ef\|_{G^s_L}
\le \eta(M_r)\|f\|_{G^s_L},
\qquad \eta(M_r)\to0,
\]

on the unrestricted one-radius Gevrey space.

This is the radial analogue of a small-divisor obstruction, although it appears here as a failure of same-radius smallness rather than as an explicit unbounded Fourier divisor.

## 5. Correction to the previous finite-iteration argument

The earlier note `gevrey_radial_compactification_remainder.md` tried to infer a fixed positive-radius stretched-exponential tail directly from a schematic estimate

\[
\|A_1f\|_{C^m}\le C^{m+1}\varepsilon^\delta\|f\|_{C^{m+r}}.
\]

That inference omitted the dependence of the Gevrey operator constant on the radius margin and therefore did not prove a same-space small operator.

What is valid is the radius-budget statement (RG8). For a **finite** number of radial compactification corrections one may choose radii

\[
L_0>L_1>\cdots>L_N>L_\infty>0
\]

and apply (RG8) at each step. If the gaps are distributed so that the multiplier constants remain controlled, one obtains a quantitatively super-algebraic finite tail. This is useful as a preconditioning step.

It does **not** imply convergence of the infinite Neumann series in one fixed positive-radius Gevrey space, because (RG11) rules out the required same-space `o(1)` operator norm.

## 6. Consequence for the exact mean theorem

The compact radial block cannot be assigned a small factor `eta_l=o(1)` in the same unrestricted Gevrey norm merely from Gevrey regularity.

Therefore a one-space contraction theorem for the full compactly supported mean map must do one of the following:

1. exploit an additional spectral restriction on the actual nonlinear range that excludes the near-resonant test family (RG10);
2. use a genuine scale-of-spaces argument with controlled Gevrey-radius loss;
3. replace the two-sided compact radial inverse by a one-sided radial input-output inverse and carry the nonzero radial exit trace as part of the outgoing state.

The third route is developed separately in `proofs/radial_characteristic_forward_inverse.md`.

## 7. Research conclusion

The radial issue is now sharply separated from the rest of the mean block:

\[
\boxed{
\text{Gevrey regularity makes }A_e\text{ tiny only across a radius gap,}
\quad
\text{not in one fixed radius.}
}
\]

Hence the local zero-force program has not failed, but the previous claim that the remaining mean theorem is a plain one-space Gevrey Banach contraction was too strong. The remaining obstruction is specifically the compact radial boundary condition, not the fast-time inverse and not the finite five-dimensional moment map.
