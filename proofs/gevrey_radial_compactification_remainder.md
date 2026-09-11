# One-shot Fourier--Gevrey control of the radial compactification remainder

**Status:** PROVED CONDITIONAL ESTIMATE / CORRECTION OF THE PREVIOUS DRAFT.

This note replaces the earlier decreasing-radius iteration argument for the radial cutoff remainder. The previous route from a fixed-loss estimate

\[
\|A_1 f\|_{C^m}\le C^{m+1}\varepsilon^\delta\|f\|_{C^{m+r}}
\]

to an `N(epsilon)->infinity` Gevrey iteration did not justify preservation of a positive limiting radius: the one-step constant depends on the radius loss, and that dependence cannot be iterated indefinitely without additional quantitative control.

The repaired argument uses the exact source representation from Section 8.2 of the OpenAI construction and obtains a **one-shot** stretched-exponential estimate by Fourier sampling along the rapidly shifted radial characteristic.

The theorem below is conditional only on an explicit profile regularity requirement: the coefficient to which the radial operator is applied, and the fixed cutoff multiplying the remainder, must belong to one common compactly supported Gevrey class of order `s>1`. This Gevrey profile-compatibility requirement must still be audited for the complete coupled relay construction.

## 1. Notation and the source identity

There are two unrelated quantities denoted `M` in the wider project. To avoid collision with the frozen v0.8 relay-design integer, this note writes

\[
\boxed{M_{\rm rad}}
\]

for the large radial phase-transport parameter called `M` in source equations (8.5)--(8.10).

On one common auxiliary torus, after the source change of radial variable

\[
U=R^{d_r},
\]

Lemma 8.2 writes the full-line radial integral in the form

\[
\boxed{
(J_{M_{\rm rad}}F)(U,y)
=\int_{\mathbb R}
F(U+u,y+M_{\rm rad}u v_r)\,du .
}
\tag{RG1}
\]

The compactification remainder is, up to fixed analytic radial weights,

\[
\boxed{
A_e f
=R^{-e}(\partial_R\chi_m)
J_{M_{\rm rad}}(R^e f),
\qquad e\in\{0,1,2\}.
}
\tag{RG2}
\]

The source moment condition implies that the auxiliary Haar mode `k=0` of the full-line integral vanishes. Thus only `k\ne0` must be estimated.

The radial torus direction satisfies the source Diophantine inequality (6.7)

\[
\boxed{
|v_r\cdot k|
\ge \frac{c_0}{1+|k|},
\qquad k\in\mathbb Z^2\setminus\{0\}.
}
\tag{RG3}
\]

Finally, the source scaling in the proof of Lemma 8.2 gives

\[
\boxed{
M_{\rm rad}^{-1}
\le C\varepsilon^{\kappa_s}S_*^{\rho_g}.
}
\tag{RG4}
\]

## 2. Gevrey input class

Fix `s>1`. On a fixed compact `U`-interval and the auxiliary torus, use any standard Gevrey norm equivalent to

\[
\boxed{
\|F\|_{G^s_\lambda}
=
\sum_{a\ge0}\sum_{\beta\in\mathbb N^2}
\frac{\lambda^{a+|\beta|}}
{(a!)^s(\beta!)^s}
\|\partial_U^a\partial_y^\beta F\|_{L^\infty}.
}
\tag{RG5}
\]

For compactly supported `G^s_\lambda` data, the radial Fourier transform of each torus coefficient obeys the standard Gevrey decay estimate

\[
\boxed{
|\widehat F_k(\xi)|
\le C\|F\|_{G^s_\lambda}
\exp\{-c\lambda_0(|k|^{1/s}+|\xi|^{1/s})\},
}
\tag{RG6}
\]

for some `lambda_0>0` depending only on the chosen equivalent norm and fixed support interval.

The same estimate holds after any fixed finite collection of slow or characteristic derivatives, provided those derivatives are included in the norm. They play no role in the fast radial Fourier argument and are suppressed below.

## 3. Exact Fourier sampling formula

Write

\[
F(U,y)=\sum_{k\in\mathbb Z^2}F_k(U)e^{2\pi i k\cdot y}.
\]

For `k\ne0`, (RG1) gives

\[
\begin{aligned}
(J_{M_{\rm rad}}F)_k(U)
&=
\int_{\mathbb R}F_k(U+u)
 e^{2\pi iM_{\rm rad}u(v_r\cdot k)}\,du\\
&=
e^{-2\pi iM_{\rm rad}U(v_r\cdot k)}
\widehat F_k\!\left(-2\pi M_{\rm rad}(v_r\cdot k)\right).
\end{aligned}
\tag{RG7}
\]

Thus the radial operator does not merely admit arbitrary-order integration by parts. It **samples the radial Fourier transform at the frequency**

\[
\boxed{
\xi_k=-2\pi M_{\rm rad}(v_r\cdot k).
}
\tag{RG8}
\]

## 4. The sampled frequency cannot be simultaneously small with the torus frequency

Set `x=|k|>=1`. By (RG3),

\[
|\xi_k|
\ge c\frac{M_{\rm rad}}{1+x}.
\]

Hence

\[
x^{1/s}+|\xi_k|^{1/s}
\ge
c_s\left(
x^{1/s}
+
\left(\frac{M_{\rm rad}}{1+x}\right)^{1/s}
\right).
\]

If `x>=sqrt(M_rad)`, the first term is at least `M_rad^{1/(2s)}`. If `x<sqrt(M_rad)`, the second term is at least a fixed multiple of `M_rad^{1/(2s)}`. Therefore

\[
\boxed{
|k|^{1/s}+|\xi_k|^{1/s}
\ge c_sM_{\rm rad}^{1/(2s)}.
}
\tag{RG9}
\]

This is the key point. A torus mode that is close to radial resonance must have large `|k|`; a low torus mode is sampled at a large radial Fourier frequency. Gevrey decay controls both regimes simultaneously.

## 5. Gevrey derivatives of the full-line integral

Differentiating (RG7) gives factors

\[
|\xi_k|^a|k|^{|\beta|}
\]

for `a` radial and `beta` torus derivatives. Use the elementary Gevrey absorption inequality

\[
\boxed{
x^n e^{-\theta x^{1/s}}
\le C_{s,\theta}^{n+1}(n!)^s,
\qquad x\ge0,
}
\tag{RG10}
\]

and reserve a fixed fraction of the exponential decay in (RG6) for each of:

1. radial derivatives;
2. torus derivatives;
3. summation over `k`;
4. the uniform `M_rad` gain from (RG9).

Consequently there exist fixed radii `0<lambda'<lambda` and constants `C,c>0`, independent of the dyadic level, such that

\[
\boxed{
\|J_{M_{\rm rad}}F\|_{G^s_{\lambda'}}
\le
C\exp\{-cM_{\rm rad}^{1/(2s)}\}
\|F\|_{G^s_\lambda},
}
\tag{RG11}
\]

whenever the Haar-zero moment removes the `k=0` contribution.

The loss from `lambda` to `lambda'` is **one fixed loss**, not a loss repeated `N(epsilon)` times.

## 6. The compactification remainder

The changes between `R` and `U=R^{d_r}` take place on a fixed compact shell bounded away from `R=0`; the coordinate map and the weights `R^{\pm e}` are analytic there. Choose the fixed cutoff `chi_m` in a compactly supported Gevrey-`s` class. Multiplication by `partial_R chi_m` and the analytic radial weights is bounded from a slightly larger radius to a fixed smaller radius.

Therefore (RG2) and (RG11) give

\[
\boxed{
\|A_e f\|_{G^s_{\lambda_*}}
\le
C\exp\{-cM_{\rm rad}^{1/(2s)}\}
\|f\|_{G^s_\lambda},
\qquad e\in\{0,1,2\}.
}
\tag{RG12}
\]

For the axial mean reconstruction,

\[
\Delta\gamma=\gamma_d-A_1\gamma_d,
\]

so the entire radial compactification error satisfies the one-step bound

\[
\boxed{
\|A_1\gamma_d\|_{G^s_{\lambda_*}}
\le
\tau_{\rm rad,\ell}
\|\gamma_d\|_{G^s_\lambda},
\qquad
\tau_{\rm rad,\ell}
:=C e^{-cM_{\rm rad}^{1/(2s)}}.
}
\tag{RG13}
\]

No radial-remainder iteration is required.

## 7. Dyadic smallness

By (RG4),

\[
M_{\rm rad}
\ge c\varepsilon^{-\kappa_s}S_*^{-\rho_g}.
\]

Hence

\[
\boxed{
\tau_{\rm rad,\ell}
\le
C\exp\!\left[
-c\varepsilon^{-\kappa_s/(2s)}
S_*^{-\rho_g/(2s)}
\right].
}
\tag{RG14}
\]

Since in the source dyadic bookkeeping `epsilon=Q^h`, `Q=2^{-ell}`, and `S_*=ell^2`, the exponent in (RG14) tends to `+infinity`; therefore

\[
\boxed{\tau_{\rm rad,\ell}=o(1).}
\tag{RG15}
\]

In fact it beats every fixed algebraic power of `epsilon` after allowing fixed polynomial powers of `S_*`.

## 8. What is proved and what remains

**Proved in this note, under the explicit Gevrey-input hypothesis:**

- the source full-line radial integral has the exact Fourier sampling formula (RG7);
- the Diophantine radial direction forces the sampled pair `(k,xi_k)` away from the joint low-frequency region by (RG9);
- one fixed Gevrey-radius loss gives the direct stretched-exponential estimate (RG12);
- the radial cutoff remainder is therefore a single small block with factor `tau_rad,ell=o(1)` and does not require an infinite or epsilon-dependent Gevrey iteration.

**Not yet proved here:**

- that every fixed cutoff/profile and every coefficient entering the complete coupled mean/nonzero forward map belongs to one common Gevrey-`s` class with radii compatible with the finite losses above;
- the complete one-space coupled mean contraction.

Those are now separated cleanly from the radial small-divisor mechanism. The old `N(epsilon)` decreasing-radius argument should not be used in a publication proof.