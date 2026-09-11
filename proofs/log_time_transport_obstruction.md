# Fixed-log-step transport obstruction for the current source packet family

**Status:** PROVED SOURCE-DERIVED SCALING OBSTRUCTION. This note corrects the short-log near-identity assumption in `cross_scale_renewal_section_shadowing_reduction.md`. The normalized source packet evolution is bounded in the fast characteristic time of `t_*`, not in the logarithmic singular time `sigma=-log(1-t)`. In logarithmic time the generator carries an unavoidable factor `epsilon^{-1}`. Therefore a fixed positive log-step cannot be treated as a near-identity transport of one current source packet.

This does not rule out an infinite unforced cascade. It shows that any successful cascade must renew/relabel the phase state on the natural fast packet time, for which the logarithmic step tends to zero.

## 1. Exact fast-time characteristic

On one source band, `characteristic_fast_time_mean_inverse.md` gives

\[
t_*=-\varepsilon\partial_T+c_iN_i,
\qquad
T(s)=T_0-\varepsilon s,
\tag{LT1}
\]

where `s` is the exact characteristic parameter:

\[
\frac d{ds}=t_*.
\tag{LT2}
\]

Since

\[
\tau=1-t=QT
\]

on a fixed dyadic chart and

\[
\sigma=-\log\tau,
\]

we obtain the exact identity

\[
\boxed{
\frac{d\sigma}{ds}
=\frac{\varepsilon}{T(s)}.
}
\tag{LT3}
\]

Hence

\[
\boxed{
\frac{ds}{d\sigma}
=\frac{T(s)}{\varepsilon}.
}
\tag{LT4}
\]

On every compact source overlap/trapping set used by the relay, `T` is bounded above and below by positive constants. Thus fast time and log time differ by the large factor `epsilon^{-1}`.

## 2. Exact transformation of the normalized WKB generator

Let `a(s)` denote any finite normalized WKB/polarization coefficient block along the same characteristic, and write its source equation as

\[
\frac{da}{ds}=A_s(s)a.
\tag{LT5}
\]

The source pulse calculation, after freezing `M`, has bounded coefficients in this variable. In particular the growing-coordinate scalar rate for beta `beta` is

\[
\boxed{
a_{\rm net,\beta}(x;p)
=\lambda_0(p)
\left[
\frac1{\sqrt{1+u_*^2x^2}}
-\beta^2\frac{1+u_*^2x^2}{(1+u_*^2)^{3/2}}
\right]
}
\tag{LT6}
\]

up to the already-audited `O(S_*^{-1})` frame error. Here `u_*=M^2` is frozen and `p` stays in a compact strict-cone set, so `A_s` is uniformly bounded.

Reparameterizing (LT5) by `sigma` and using (LT4) gives

\[
\boxed{
\frac{da}{d\sigma}
=A_\sigma(\sigma)a,
\qquad
A_\sigma
=\frac{T}{\varepsilon}A_s.
}
\tag{LT7}
\]

Thus boundedness of `A_s` does **not** imply boundedness of `A_sigma`.

## 3. The divergence is genuine, not merely an upper-bound artifact

At the second v0.8 renewal event the regenerated beta-two channel lies strictly on the decaying side:

\[
x_R:=x_M+\theta_M^{\rm ren}
>x_{2,u_*}.
\tag{LT8}
\]

The inequality is strict by `v08_beta2_feedback_renewal.md`. Since the slow parameter set is compact and

\[
0<\lambda_-\le\lambda_0(p),
\]

there exists, after freezing `M`, a number `c_M>0` such that

\[
\boxed{
a_{\rm net,2}(x_R;p)\le-c_M<0}
\tag{LT9}
\]

uniformly in the admissible slow parameter `p`.

For sufficiently high levels the `O(S_*^{-1})` source-frame error is smaller than `c_M/2`. Therefore the actual fast-time generator has a beta-two direction whose scalar coefficient has magnitude at least `c_M/2` at the renewal section. By (LT7),

\[
\boxed{
\|A_\sigma\|
\ge
\frac{T_-c_M}{2\varepsilon}
\longrightarrow\infty.
}
\tag{LT10}
\]

Consequently the proposed bound

\[
\sup_\sigma\|A_\sigma(\sigma)\|<\infty
\]

from the amplitude-only short-log reduction is false for the current packet normalization.

## 4. A fixed logarithmic step is much longer than one packet

The translated source pulse coordinate satisfies

\[
x=\frac12+\frac{s-s_0}{L_s},
\qquad
L_s\asymp S_*.
\tag{LT11}
\]

The two designated events of the current cell are separated by

\[
\Delta s_{\rm cell}
=\theta_M^{\rm ren}L_s
\asymp S_*.
\tag{LT12}
\]

Using the exact characteristic law `T(s)=T_0-epsilon(s-s_0)`, the corresponding logarithmic change is

\[
\boxed{
\Delta\sigma_{\rm cell}
=
\log\frac{T_0}{T_0-\varepsilon\Delta s_{\rm cell}}
}
\tag{LT13}
\]

and, because `epsilon S_* -> 0`,

\[
\boxed{
\Delta\sigma_{\rm cell}
=
\frac{\varepsilon\theta_M^{\rm ren}L_s}{T_0}
+O(\varepsilon^2L_s^2)
\asymp\varepsilon S_*\to0.
}
\tag{LT14}
\]

By contrast, a fixed log step `delta>0` requires from (LT3)

\[
\Delta s
\asymp\frac{\delta}{\varepsilon},
\tag{LT15}
\]

which satisfies

\[
\frac{\Delta s}{L_s}
\asymp
\frac{\delta}{\varepsilon S_*}
\longrightarrow\infty.
\tag{LT16}
\]

Thus fixed-ratio q transport crosses asymptotically many source-pulse lengths. It is outside the local packet theorem and cannot be justified by a one-cell near-identity argument.

## 5. Correct scale descent is a vanishing-log-step descent

The source-compatible scale increment per full relay cell is therefore

\[
\boxed{
\delta_\ell
:=\Delta\sigma_{\rm cell}
\asymp\varepsilon_\ell S_{*,\ell},
\qquad
\delta_\ell\to0.
}
\tag{LT17}
\]

This does not prevent approach to the singular time. If an infinite sequence of exact cells can be concatenated, then `sigma_j` obeys a positive recurrence of the form

\[
\sigma_{j+1}-\sigma_j
\asymp
 e^{-h\sigma_j}\sigma_j^2
\tag{LT18}
\]

up to fixed overlap constants, because `epsilon=Q^h`, `Q asy tau asy e^{-sigma}`, and `S_*=ell^2 asy sigma^2` on the dyadic cover.

Such a positive recurrence cannot converge to a finite `sigma_infty`: if it did, the right side of (LT18) would remain bounded below by a positive constant. Hence, conditional on indefinite cell concatenation,

\[
\boxed{\sigma_j\to\infty,\qquad q_j\to0,\qquad t_j\to1.}
\tag{LT19}
\]

So a fixed shrink factor is not needed for finite-time accumulation.

## 6. Consequence

The correct cross-scale problem is no longer

\[
\widehat T(\sigma+\delta,\sigma)\approx I
\quad\text{for fixed }\delta>0.
\]

That statement is incompatible with the exact source time scaling.

The remaining problem is to renew the **complete phase-amplitude state** after each fast cell while the physical scale changes only by `O(epsilon S_*)` in logarithmic time. The next note shows that the present two-event cell renews beta values and amplitudes but does not renew the phase-slope coordinates, and then identifies an exact lattice-shear mechanism that could do so.