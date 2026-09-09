# β-phase stability for the OpenAI pulse equation

**Status:** DERIVED WORKING PROPOSITION. This is not yet publication-final; every estimate should be rechecked line-by-line against the pinned source version before promotion to theorem status.

Primary source: OpenAI, *Finite Time Blowup for Navier–Stokes*, equations (7.2)–(7.11), Proposition 7.2, Lemma 7.4, Lemma 7.7, Proposition 9.1.

## 1. β-scaled phase family

Fix a compact interval

\[
0<\beta_-\le \beta\le \beta_+<\infty.
\]

In the phase construction (7.2)–(7.4), replace the unrounded frequency data and initial radial phase slope by their β-scaled versions. After the same angular rounding step, write the resulting phase as \(\Phi_\beta\) and

\[
n_\beta:=\nabla_*\Phi_\beta.
\]

Because the phase formulas are linear in the unrounded frequency data, the source proof of Lemma 7.1 gives, uniformly for β in the fixed compact interval,

\[
\boxed{
|n_\beta-\beta B_s(s(v),K)|+|n_\beta'|
\le \frac{C_{\beta_-,\beta_+}}{S_*}.
}
\]

The transport defect likewise remains

\[
\boxed{
E_{\mathrm{ik},\beta}
=(t_*+bD_r+F\partial_\theta+GD_z)\Phi_\beta
=O(\varepsilon S_*^C)
}
\]

in every fixed coefficient derivative.

## 2. Inviscid projected operator is scale-invariant

The source projected operator (7.6) is

\[
A_\Phi
=-K+
\frac{n_\Phi\big(n_\Phi^TK-(n_\Phi')^T\big)}{|n_\Phi|^2}.
\]

Under exact scaling

\[
(n_\Phi,n_\Phi')\mapsto(\beta n_\Phi,\beta n_\Phi'),
\]

the fraction is unchanged. Thus the reference inviscid projected operator is homogeneous of degree zero in the phase-normal scale. The same moving-frame calculation therefore gives

\[
\boxed{
B_\ell(A_{\Phi_\beta}B-B')
=
\operatorname{diag}(\lambda,-\lambda)+E_\beta,
\qquad
|E_\beta|\le C/S_*.
}
\]

The reference shear growth rate remains

\[
\lambda(s)=\frac{\lambda_0}{\sqrt{1+s^2}}
\]

at principal order.

## 3. Viscous term acquires β²

For harmonic \(m\), the leading damping is

\[
m^2d_\beta,
\qquad
d_\beta=\varepsilon k^2|n_\beta|^2.
\]

Using the source normalization of \(B_s\),

\[
\boxed{
d_\beta
=
\beta^2d_{\rm ref}+O(S_*^{-1}),
\qquad
d_{\rm ref}
=
\frac{\lambda_0(1+s^2)}{(1+u_*^2)^{3/2}}.
}
\]

Hence the principal growing-coordinate exponent is

\[
\boxed{
a_{\rm net,\beta}(s)
=
\lambda_0
\left[
\frac{1}{\sqrt{1+s^2}}
-
\beta^2\frac{1+s^2}{(1+u_*^2)^{3/2}}
\right].
}
\tag{B1}
\]

## 4. Exact turning point

The unique positive zero of (B1) is

\[
\boxed{
y_\beta
=
\sqrt{(1+u_*^2)\beta^{-4/3}-1}.
}
\tag{B2}
\]

Indeed

\[
(1+y_\beta^2)^{3/2}
=(1+u_*^2)^{3/2}\beta^{-2}.
\]

For fixed β,

\[
\frac{y_\beta}{u_*}\to\beta^{-2/3}
\qquad(u_*\to\infty).
\]

Since the source construction permits choosing \(u_*\) larger once the strict cone margin is fixed, the large-\(u_*\) regime is a legitimate design regime rather than a formal limit only.

## 5. Exact β-envelope primitive

On a sign-fixed pulse rectangle, the source coordinate satisfies

\[
|s(v)|=u_*
\left(\frac12+\frac{v}{L_s}\right),
\qquad
0\le v\le L_s,
\]

so

\[
\frac{d|s|}{dv}=\frac{u_*}{L_s}.
\]

Let

\[
x=\frac{|s|}{u_*},
\qquad
x_{\beta,u_*}=\frac{y_\beta}{u_*}.
\]

Center the β-envelope at the exact turning point and define

\[
P_\beta(v)
=
\exp\left(
\int_{v_\beta}^{v}a_{\rm net,\beta}(s(w))\,dw
\right).
\]

Then

\[
\log P_\beta(v)
=
\frac{\lambda_0L_s}{u_*}
\mathcal E_{\beta,u_*}(x),
\]

where the exact normalized primitive is

\[
\boxed{
\begin{aligned}
\mathcal E_{\beta,u}(x)
={}&
\operatorname{arsinh}(ux)
-
\operatorname{arsinh}(u x_{\beta,u})\\
&-
\frac{\beta^2}{(1+u^2)^{3/2}}
\left[
 u(x-x_{\beta,u})
+
\frac{u^3}{3}
(x^3-x_{\beta,u}^3)
\right].
\end{aligned}
}
\tag{B3}
\]

By construction

\[
\mathcal E_{\beta,u}(x_{\beta,u})=0,
\qquad
\mathcal E_{\beta,u}(x)\le0
\]

throughout the pulse interval.

## 6. Correct reduced large-\(u_*\) envelope

Uniformly on compact subsets of \(x\in(0,\infty)\) and β in a fixed compact subset of \((0,\infty)\),

\[
x_{\beta,u}
=
\beta^{-2/3}+O(u^{-2}),
\]

and

\[
\boxed{
\mathcal E_{\beta,u}(x)
=
I_\beta(x)+O(u^{-2}),
}
\tag{B4}
\]

with the correct reduced primitive

\[
\boxed{
I_\beta(x)
=
\log\!\big(x\beta^{2/3}\big)
-
\frac{\beta^2}{3}
\big(x^3-\beta^{-2}\big).
}
\tag{B5}
\]

Its derivative is exactly

\[
\boxed{
I_\beta'(x)
=
F_\beta(x)
:=
\frac1x-\beta^2x^2.
}
\tag{B6}
\]

**Correction of earlier notes.** An earlier working quantity multiplied \(I_\beta\) by an extra factor \(\beta^{2/3}\). That quantity is not the common-\(L_s\) envelope primitive coming from (B1) and (7.2). Any witness based on that extra factor is deprecated.

The expansion (B4) follows from

\[
\operatorname{arsinh}(ux)
=
\log(2ux)+O(u^{-2})
\]

uniformly for \(x\ge c>0\), together with

\[
x_{\beta,u}=\beta^{-2/3}+O(u^{-2})
\]

and

\[
(1+u^2)^{-3/2}=u^{-3}(1+O(u^{-2})).
\]

The same argument gives \(C^1\) convergence on such compact sets.

## 7. Gaussian localization survives β-scaling

If the turning point remains a fixed positive fraction away from the raw endpoints \(x=1/2,3/2\), then the derivative of \(a_{\rm net,\beta}(|s(v)|)\) remains negative and comparable to \(-L_s^{-1}\). Repeating the two integrations used in source equation (7.16) yields

\[
\boxed{
 e^{-C(v-v_\beta)^2/L_s}
\le P_\beta(v)
\le e^{-c(v-v_\beta)^2/L_s}.
}
\]

Thus β-packets may be centered at different pulse coordinates while retaining the same Gaussian-type tail mechanism.

## 8. What is established here

This derivation supports the following working conclusion:

- fixed β-rescaling preserves the principal shear eigendirections;
- damping changes by β²;
- the exact turning point is (B2);
- the exact normalized envelope is (B3);
- the correct large-\(u_*\) reduced primitive is (B5), with \(C^1\) error \(O(u_*^{-2})\).

It does **not** yet prove an interacting two-parent relay. The next steps are to construct a transverse reduced envelope resonance using (B5), prove persistence for finite large \(u_*\) using (B3), and then embed it into the localized curl-generated packet classes.
