# Quantitative mean-to-nonzero sensitivity on the forward relay

**Status:** PROVED ABSTRACTLY FROM THE EXISTING FORWARD PROPAGATOR, WITH SOURCE-EXPONENT IDENTIFICATION RECORDED SEPARATELY.

This note strengthens the qualitative statement in `nonzero_harmonic_forward_reduction.md` that the exact nonzero solution `z=z(m)` is locally Lipschitz in the angular mean input. The purpose is to isolate exactly where smallness does, and does not, enter the coupled mean fixed point.

The forward nonzero equation is

\[
\partial_v z
=\mathcal L_m(v)z+f_m+\mathcal B(z,z),
\qquad
\mathcal L_m:=\mathcal D+\mathcal K_m,
\tag{S1}
\]

on a fixed bounded relay collar `I=[v_-,v_+]`. For all mean inputs in one sufficiently small ball, the already-proved Volterra argument gives a full propagator `V_m(v,w)` satisfying

\[
\|V_m(v,w)g\|_{\mathfrak A_{\sigma,0}}
\le K_M\|g\|_{\mathfrak A_{\sigma,0}},
\tag{S2}
\]

and

\[
\|V_m(v,w)g\|_{\mathfrak A_{\sigma,1}}
\le K_M(1+(v-w)^{-1/2})
\|g\|_{\mathfrak A_{\sigma,0}}.
\tag{S3}
\]

The constants are uniform over that mean ball after the v0.8 design and collar are frozen.

## 1. Difference equation

Let

\[
z=z(m),
\qquad
\tilde z=z(\tilde m),
\qquad
\delta z=z-\tilde z,
\qquad
\delta m=m-\tilde m.
\]

Subtract the two exact equations. Using the equation linearized about `z(m)` as the reference evolution gives

\[
\partial_v\delta z
=
\bigl(\mathcal L_m+\mathcal B(z,\cdot)+\mathcal B(\cdot,\tilde z)\bigr)\delta z
+
(\mathcal K_m-\mathcal K_{\tilde m})\tilde z
+
(f_m-f_{\tilde m}).
\tag{S4}
\]

The quadratic perturbation of the propagator is harmless because

\[
\|z\|+\|\tilde z\|\le C\rho_\ell=o(1).
\]

Therefore the same integrable smoothing kernel yields, for sufficiently large dyadic level,

\[
\boxed{
\|\delta z\|_{C(I;\mathfrak A_{\sigma,1})}
\le
C_{M,I}
\left(
\|(\mathcal K_m-\mathcal K_{\tilde m})\tilde z\|_{L^\infty\mathfrak A_{\sigma,0}}
+
\|f_m-f_{\tilde m}\|_{L^\infty\mathfrak A_{\sigma,0}}
\right).
}
\tag{S5}
\]

## 2. Mean coefficients enter linearly and with one carrier derivative

The mean perturbation changes only the smooth coefficient fields in the Navier--Stokes linearization. In the source packet calculus, one output carrier derivative is the worst derivative loss. Thus for the chosen characteristic mean norm `Y` one has

\[
\boxed{
\|(\mathcal K_m-\mathcal K_{\tilde m})q\|_{\mathfrak A_{\sigma,0}}
\le
C_M\|m-\tilde m\|_Y
\|q\|_{\mathfrak A_{\sigma,1}}.
}
\tag{S6}
\]

The supported defect depends smoothly on the same mean coefficients, hence

\[
\boxed{
\|f_m-f_{\tilde m}\|_{\mathfrak A_{\sigma,0}}
\le
C_M a_\ell\|m-\tilde m\|_Y,
}
\tag{S7}
\]

where `a_ell` is the size of the source coefficient multiplying the mean variation. For the conservative stage-zero local state, `a_ell` is no worse than the algebraically small supported defect scale already recorded in the branch, and hence may be absorbed into `rho_ell`.

Using `\|\tilde z\|<=C\rho_ell` in (S6), (S5) gives

\[
\boxed{
\|z(m)-z(\tilde m)\|_{C(I;\mathfrak A_{\sigma,1})}
\le
C_{M,I}\rho_\ell
\|m-\tilde m\|_Y.
}
\tag{S8}
\]

Thus the correction part `z(m)` itself has a genuinely small mean sensitivity. This is stronger than bare local Lipschitz continuity.

## 3. Primary-wave covariance feedback

The full angular-mean covariance is not built only from the small correction `z`. It also contains the designated primary waves `w_{\rm pr}`, whose source amplitude is of order `W_{1/2}`. Hence the first variation of the covariance contains

\[
\delta W
=
\left\langle
w_{\rm pr}\otimes\delta z
+
\delta z\otimes w_{\rm pr}
\right\rangle_\theta
+
\left\langle
z\otimes\delta z
+
\delta z\otimes\tilde z
\right\rangle_\theta.
\tag{S9}
\]

The source product calculus (Lemma 9.2 in the OpenAI construction) records schematically

\[
W_\alpha\times W_{\alpha'}
\longrightarrow
M_{\alpha+\alpha'-\kappa_s}.
\tag{S10}
\]

Consequently the primary-wave part of (S9) gains the positive exponent

\[
\boxed{\varepsilon^{1/2-\kappa_s}}
\tag{S11}
\]

relative to the mean variation, while the correction--correction part gains at least one factor `rho_ell`.

Therefore, after the bounded pressure/stress/moment reconstructions are applied, the covariance-mediated mean feedback satisfies the schematic quantitative estimate

\[
\boxed{
\|\delta\mathcal W_{\rm mean}\|_Y
\le
C_MS_*^C
\left(
\varepsilon^{1/2-\kappa_s}
+ho_\ell
\right)
\|m-\tilde m\|_Y.
}
\tag{S12}
\]

The factor `S_*^C` records only the fixed polynomial source bookkeeping. Since `epsilon` decays exponentially in the dyadic level and `S_*=ell^2`, this factor still tends to zero provided `1/2-kappa_s>0`, as in the source parameter regime.

## 4. Interpretation

There are two distinct Lipschitz statements and they should not be conflated:

1. the **small correction solution** obeys the direct bound (S8), with factor `rho_ell`;
2. the **mean covariance feedback through the designated primary wave** is larger, and is controlled by the source exponent gain `epsilon^(1/2-kappa_s)` in (S12).

The second quantity is the one that belongs in the final coupled mean contraction constant.

## 5. Remaining coupling work

This note does not by itself close the angular mean equation. It supplies the nonzero-harmonic contribution to that closure. The complete contraction must also include:

- the nonlinear five-dimensional moment recomputation gain `epsilon^(0.9-2kappa_s)`;
- the signed stress correction remainder, whose conservative source gain is recorded separately in the coupled block audit;
- the one-shot Fourier--Gevrey radial tail from `gevrey_radial_compactification_remainder.md`;
- bounded characteristic integration by `J_i`.

Once those blocks are assembled in one common characteristic Gevrey norm, no separate Nash--Moser mechanism is required for the local mean solve.