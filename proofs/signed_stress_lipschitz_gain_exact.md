# Exact signed-stress Lipschitz gain at fixed Sobolev order

**Status:** PROVED SOURCE-TRANSFER LEMMA AT FIXED DERIVATIVE ORDER.

This note removes the provisional `0.17` placeholder from the mean-contraction bookkeeping. It uses the exact exponent accounting in OpenAI Proposition 9.6, Step 2, together with the fact that the signed amplitude correction is linear in the prescribed stress and all remaining terms are bilinear or quadratic. At one fixed sufficiently high Sobolev order, the source size estimates therefore transfer to Lipschitz difference estimates with the same epsilon exponents.

The source parameters are

\[
\kappa_s=10^{-5},
\qquad
\sigma_j=\frac15+\frac j{10},
\qquad
B=\frac12+\sigma_j,
\qquad
C^*=1+\sigma_j=B+\frac12.
\tag{SS1}
\]

## 1. Exact covariance decomposition

Let `Sigma` be the auxiliary-mean stress target constructed from the current averaged tangential residual. The source signed-amplitude map produces a wave increment

\[
s=t_s+r_s,
\]

where `t_s` is the prescribed transverse amplitude and `r_s` is the curl/reconstruction remainder. With

\[
\mathcal B(a,b)=\langle\langle a\otimes b+b\otimes a\rangle_\theta\rangle_Y,
\]

Corollary 7.8 and Proposition 9.6 give the exact covariance change

\[
\boxed{
\langle\Delta W\rangle_Y
=
\mathcal B(w_0^{\rm tan},t_s)
+
\mathcal B(w-w_0^{\rm tan},t_s)
+
\mathcal B(w,r_s)
+
\langle\langle s\otimes s\rangle_\theta\rangle_Y.
}
\tag{SS2}
\]

The radial--tangential part of the first term equals the prescribed `Sigma` exactly and cancels the target averaged residual at principal order.

Thus only the last three terms contribute to the post-correction averaged residual.

## 2. Exact source exponents before divergence

The source records

\[
w-w_0^{\rm tan}\in W_{0.68}
\]

and the signed correction at the current cycle in the class needed to realize `Sigma`. Proposition 9.6, Step 2, gives the following exact lower exponents for the three remainders in (SS2):

\[
\boxed{
\mathcal B(w-w_0^{\rm tan},t_s)
\in M_{C^*+0.18-\kappa_s},
}
\tag{SS3}
\]

\[
\boxed{
\mathcal B(w,r_s)
\in M_{C^*+1/2-2\kappa_s},
}
\tag{SS4}
\]

\[
\boxed{
\langle\langle s\otimes s\rangle_\theta\rangle_Y
\in M_{C^*+\sigma_j-2\kappa_s}.
}
\tag{SS5}
\]

The radial divergence in the tangential mean equation costs one additional `kappa_s`. Therefore the three post-divergence gains above the baseline `C^*` are

\[
\boxed{
\delta_1=0.18-2\kappa_s,
\qquad
\delta_2=\frac12-3\kappa_s,
\qquad
\delta_3=\sigma_j-3\kappa_s.
}
\tag{SS6}
\]

The retained finite-moment term has gain at least `1-kappa_s` and is therefore not the bottleneck.

Since

\[
\sigma_j\ge\frac15,
\qquad
\kappa_s=10^{-5},
\]

we have

\[
\delta_1=0.17998,
\qquad
\delta_2=0.49997,
\qquad
\delta_3\ge0.19997.
\]

Hence the exact weakest displayed source gain is

\[
\boxed{
\delta_{\rm stress}
=\frac9{50}-2\kappa_s
=0.18-2\kappa_s.
}
\tag{SS7}
\]

The `0.17` appearing in the source proof is a deliberately rounded common lower bound; it is not the sharp exponent supplied by the displayed Step-2 remainder calculation.

## 3. Why the same exponent holds for differences

Fix one derivative order `m_0>=6` and one small ball of admissible mean/nonzero states. Let two states be denoted by

\[
X=(m,w),
\qquad
\widetilde X=(\widetilde m,\widetilde w).
\]

The stress target construction has the form

\[
\Sigma=\mathcal R_{\rm stress}(X),
\]

where the radial moment subtraction and fixed profile insertion are linear bounded maps at this fixed derivative order. The signed-amplitude map has the form

\[
\boxed{s=\mathcal L_{\rm as}\Sigma}
\tag{SS8}
\]

with `L_as` linear: the formula divides by the fixed strictly positive primary amplitude and then applies fixed cutoffs, physical rescaling, and curl reconstruction.

Therefore

\[
\delta s
=\mathcal L_{\rm as}\,\delta\Sigma.
\tag{SS9}
\]

Every remainder in (SS2) is bilinear or quadratic. For example,

\[
\begin{aligned}
&\mathcal B(w-w_0^{\rm tan},t_s)
-\mathcal B(\widetilde w-w_0^{\rm tan},\widetilde t_s)\\
&\quad=
\mathcal B(w-\widetilde w,t_s)
+
\mathcal B(\widetilde w-w_0^{\rm tan},t_s-\widetilde t_s),
\end{aligned}
\tag{SS10}
\]

and

\[
s\otimes s-\widetilde s\otimes\widetilde s
=(s-\widetilde s)\otimes s
+\widetilde s\otimes(s-\widetilde s).
\tag{SS11}
\]

At fixed `m_0`, `H^{m_0}` is an algebra, so the same product estimates used for size estimates give Lipschitz estimates on a fixed small ball. No extra derivative or epsilon loss is introduced by taking the difference.

Consequently the post-principal signed-stress remainder satisfies

\[
\boxed{
\|\delta\mathcal N_{\rm stress}\|_{H^{m_0}}
\le
C_{M,I,m_0}S_*^C
\varepsilon^{\delta_{\rm stress}}
\|X-\widetilde X\|_{\mathcal X^{m_0}},
}
\tag{SS12}
\]

with

\[
\boxed{
\delta_{\rm stress}=\frac9{50}-2\kappa_s>0.
}
\tag{SS13}
\]

Here `X^{m_0}` denotes the fixed product norm for the mean variables and the exact nonzero forward solution on the relay collar.

## 4. Composition with the mean-to-wave map

The branch already proves

\[
\|z(m)-z(\widetilde m)\|_X
\le C_{M,I}\|m-\widetilde m\|_Y.
\tag{SS14}
\]

Thus, after substituting the exact nonzero solution into (SS12),

\[
\boxed{
\|\mathcal N_{\rm stress}(m)-\mathcal N_{\rm stress}(\widetilde m)\|_{H^{m_0}}
\le
C_{M,I,m_0}S_*^C
\varepsilon^{9/50-2\kappa_s}
\|m-\widetilde m\|_{H^{m_0}}.
}
\tag{SS15}
\]

This is the signed-stress Lipschitz estimate needed in the final mean contraction.

## 5. Updated aggregate nonlinear factor

The provisional term `epsilon^0.17` in the earlier audits can therefore be replaced by

\[
\boxed{
\varepsilon^{9/50-2\kappa_s}.
}
\tag{SS16}
\]

The current aggregate mean nonlinear factor becomes

\[
\boxed{
\eta_{\rm nl,\ell}
\lesssim
C_MS_*^C
\left[
\varepsilon^{9/50-2\kappa_s}
+\varepsilon^{1/2-\kappa_s}
+\varepsilon^{1-2\kappa_s}
+\rho_\ell
\right].
}
\tag{SS17}
\]

Since `9/50-2kappa_s>0`, this tends to zero in the source parameter regime.

## 6. What is closed by this note

The signed-stress block no longer carries an unspecified decimal slack. Its exact weakest displayed source gain is

\[
\boxed{\frac9{50}-2\kappa_s.}
\]

At fixed Sobolev order the linear/bilinear structure of the correction upgrades the source size estimate to a Lipschitz difference estimate with the same exponent.

This closes the signed-stress proof obligation for the local contraction bookkeeping. It does not address the remaining whole-space pressure/localization issue.