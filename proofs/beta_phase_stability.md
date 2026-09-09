# β-phase stability for the OpenAI pulse equation

**Status:** DERIVED WORKING PROPOSITION. This is not yet publication-final; every estimate should be rechecked line-by-line against the pinned source version before promotion to theorem status.

Primary source: OpenAI, *Finite Time Blowup for Navier–Stokes*, equations (7.2)–(7.11), Proposition 7.2, and Lemma 7.7.

## 1. β-scaled phase family

Fix a compact interval

\[
0<\beta_-\le \beta\le \beta_+<\infty.
\]

In the phase construction of (7.2)–(7.4), replace the unrounded tangential wave-number vector by

\[
(\widetilde p_\beta/R_0,p_{z,\beta})
=
\beta B_s
\left(
K-\frac{\sigma u_*g_0}{L_s|g_0|^2}
\right),
\]

and replace

\[
x_0=\frac{\sigma B_su_*}{2}
\]

by

\[
x_{0,\beta}=\frac{\sigma\beta B_su_*}{2}.
\]

As in the source construction, choose \(kp_\beta\) to be a nearest nonzero integer to \(k\widetilde p_\beta\), while leaving \(p_{z,\beta}\) unrounded. Define

\[
\Phi_\beta
=
p_\beta\theta+p_{z,\beta}Z/\varepsilon
+x_{0,\beta}R
-v(p_\beta F+p_{z,\beta}G).
\]

Let

\[
n_\beta:=\nabla_*\Phi_\beta.
\]

## 2. Phase-normal estimate

The proof of Lemma 7.1 is linear in the unrounded frequency data. Because \(\beta\) stays in a fixed compact subset of \((0,\infty)\), the same rounding and slow-box estimates give

\[
\boxed{
|n_\beta-\beta B_s(s(v),K)|+|n_\beta'|
\le \frac{C_{\beta_-,\beta_+}}{S_*}.
}
\]

The phase-transport defect remains

\[
\boxed{
E_{\mathrm{ik},\beta}
=(t_*+bD_r+F\partial_\theta+GD_z)\Phi_\beta
=O(\varepsilon S_*^C)
}
\]

in every fixed coefficient derivative.

The only new point is uniformity in \(\beta\), which follows from the compact lower/upper bounds on \(\beta\).

## 3. Inviscid projected operator is scale-invariant

The source formula (7.6) is

\[
A_\Phi
=-K+
\frac{n_\Phi\big(n_\Phi^TK-(n_\Phi')^T\big)}{|n_\Phi|^2}.
\]

Under exact scaling

\[
(n_\Phi,n_\Phi')\mapsto(\beta n_\Phi,\beta n_\Phi'),
\]

the second term is unchanged. Therefore the reference inviscid projected operator is homogeneous of degree zero in the phase-normal scale.

Consequently the same moving-plane frame calculation gives

\[
\boxed{
B_\ell(A_{\Phi_\beta}B-B')
=
\operatorname{diag}(\lambda,-\lambda)+E_\beta,
\qquad
|E_\beta|\le C/S_*.
}
\]

The reference growth rate \(\lambda(v)\) is unchanged to leading order by \(\beta\).

## 4. Viscous term acquires β²

For harmonic \(m\), the leading viscous damping is

\[
m^2d_\beta,
\qquad
d_\beta=\varepsilon k^2|n_\beta|^2.
\]

Hence

\[
\boxed{
d_\beta
=
\beta^2d_{\rm ref}+O(S_*^{-1}),
\qquad
d_{\rm ref}=\varepsilon k^2B_s^2(1+s^2).
}
\]

Thus the growing coordinate has principal net exponent

\[
\boxed{
a_{\rm net,\beta}(s)
=
\frac{\lambda_0}{\sqrt{1+s^2}}
-
\beta^2\frac{\lambda_0(1+s^2)}{(1+u_*^2)^{3/2}}.
}
\]

(The displayed normalization uses the source choice of \(B_s\).)

## 5. Exact turning point

The unique positive zero of the principal net exponent is

\[
\boxed{
y_\beta
=
\sqrt{(1+u_*^2)\beta^{-4/3}-1}.
}
\]

Indeed

\[
(1+y_\beta^2)^{3/2}
=(1+u_*^2)^{3/2}\beta^{-2}.
\]

For fixed \(\beta\),

\[
\frac{y_\beta}{u_*}\to\beta^{-2/3}
\qquad (u_*\to\infty).
\]

This recovers the reduced model

\[
F_\beta(x)=\frac1x-\beta^2x^2,
\qquad s=u_*x.
\]

## 6. β-dependent recentering

The source proof obtains Gaussian decay by centering the envelope at the unique zero of \(a_{\rm net}\). For \(\beta=1\), this is the midpoint \(|s|=u_*\).

For general \(\beta\), if \(y_\beta\) lies a fixed positive fraction away from the raw pulse endpoints, define \(v_\beta\) by

\[
|s(v_\beta)|=y_\beta
\]

and define

\[
P_\beta(v)
=
\exp\left(
\int_{v_\beta}^{v}a_{\rm net,\beta}(s(w))\,dw
\right).
\]

The derivative of \(a_{\rm net,\beta}(|s(v)|)\) remains negative and comparable to \(-L_s^{-1}\) on any fixed compact β-range for which the turning point stays inside the raw interval. Therefore the same two integrations used in (7.16) give

\[
\boxed{
 e^{-C(v-v_\beta)^2/L_s}
\le P_\beta(v)
\le e^{-c(v-v_\beta)^2/L_s}.
}
\]

This is important for the relay project: different β-packets need not reach their maximal amplitude at the same pulse coordinate.

## 7. What this does and does not establish

This derivation removes one concern: changing the carrier magnitude by a fixed β does not destroy the shear eigendirections; it changes the leading damping by β² and shifts the pulse turning point.

It does **not** yet prove that two differently centered β-packets can be made to overlap in a way that produces an admissible child phase. That is the next proof obligation.
