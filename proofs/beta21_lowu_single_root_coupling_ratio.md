# Single-root shift-coupling ratio for the low-`u` bilateral orbit

**Status:** PROVED PRINCIPAL SOURCE-FRAME COMPATIBILITY BY BOUNDARY-LAYER POLARIZATION TUNING / EXACT SOURCE AMPLITUDE-CONVENTION FACTOR STILL TO BE PINNED.  This note closes a logical gap in `beta21_lowu_boundary_layer_bilateral_orbit_reset.md`: the two limiting shift coefficients `a_C,a_P` cannot be chosen independently because both are produced by one physical beta-zero Cauchy root `M=P-2C`.

The principal Leray/polarization calculation shows that a fixed nonzero `K` component would force the beta-two/beta-one coupling ratio to tend to `2`, which is incompatible with the ratio required by the previously selected dispersion point.  However the Cauchy root is not a generated root and its transverse polarization is a design variable.  Choosing an `S`-dependent polarization that approaches the pure `N` direction with `K/N=O(S^{-1})` yields a one-parameter limiting coupling ratio.  The required ratio is attained transversely.

Thus there is **no principal single-root ratio obstruction**.  The old fixed generated-root polarization must not be imposed on the low-`u` Cauchy architecture.

No full finite-`S` profile theorem or global cascade is claimed here.

## 1. Generic beta-zero root polarization

Work in the frozen principal frame used by the existing polarization audits.  A positive-beta growing wave of signed beta `b>0` and reduced slope `s` has polarization

\[
\boxed{
g(s)=e_r-sK+c_0\sqrt{1+s^2}\,N,\qquad c_0<0.}
\tag{RC1}

The beta-zero root phase is radial.  Therefore every transverse root polarization has the form

\[
\boxed{
b_M=kK+c_0rN.}
\tag{RC2}

Here `k,r` are real design coefficients.  An overall common scalar is immaterial for the coupling ratio and is later absorbed into the root amplitude.

Let the radial source-normalized phase increment of the root be `m`.  Then addition of `M` preserves beta and moves the wave slope to

\[
\boxed{s_t=s+\frac mb.}
\tag{RC3}

This is exactly the geometry used in `beta21_second_gate_mean_root_polarization_audit.md`.

## 2. Exact principal symmetrized convective vector

The principal symmetrized interaction is

\[
Q=(g(s)\cdot me_r)b_M+(b_M\cdot b(se_r+K))g(s).
\tag{RC4}

Since

\[
g(s)\cdot e_r=1,
\qquad
b_M\cdot(se_r+K)=k,
\]

we obtain

\[
\boxed{
Q=mb_M+bk\,g(s).
}
\tag{RC5}

Its components in the frame `(e_r,K,N)` are

\[
Q_r=bk,
\]

\[
Q_K=mk-bks,
\]

\[
Q_N=c_0\left(mr+bk\sqrt{1+s^2}\right).
\tag{RC6}

## 3. Exact growing projection at the target slope

At the target slope define

\[
h_t=e_r-s_tK.
\]

After Leray projection to the target plane, the coefficient along `h_t` is

\[
\boxed{
A_h
=
\frac{bk-s_t(mk-bks)}{1+s_t^2}.
}
\tag{RC7}

The `N` coefficient divided by the `N` coefficient of the target growing polarization

\[
g(s_t)=h_t+c_0\sqrt{1+s_t^2}\,N
\]

is

\[
\boxed{
A_N
=
\frac{mr+bk\sqrt{1+s^2}}
{\sqrt{1+s_t^2}}.
}
\tag{RC8}

The growing and decaying polarizations are the symmetric/antisymmetric combinations of these two plane directions.  Hence the target growing coefficient is

\[
\boxed{
A_b^+(s,m;k,r)
=
\frac12\left(A_h+A_N\right).
}
\tag{RC9}

Equations (RC7)--(RC9) generalize equations (MP11)--(MP13) of the older generated-root audit.  Substituting its special polarization `k=-S`, `r=R_M` reproduces that formula exactly.

The source polarization constant `c_0` cancels from (RC9).

## 4. What a fixed root polarization would do

Fix `s=x` and let `m->0`.  If `k` tends to a nonzero constant, then

\[
A_h=bk+O(m),
\qquad
A_N=bk+O(m),
\]

and therefore

\[
\boxed{
A_b^+=bk+O(m).
}
\tag{RC10}

Thus

\[
\boxed{
\frac{A_2^+}{A_1^+}\to2.
}
\tag{RC11}

The low-`u` dispersion point instead requires, in the current source-frame amplitude convention,

\[
\boxed{
R_*:=\frac{\mu_P}{\lambda_C}
=
\frac{0.845013757547658\ldots}{2.982607649202283\ldots}
=0.2833137498905236\ldots.
}
\tag{RC12}

Therefore the previously written low-`u` theorem cannot use an `S`-independent generic transverse polarization with nonzero `K` component.

## 5. Boundary-layer polarization ansatz

The root slope increment itself is boundary-layer small:

\[
\boxed{m_S=2\delta_S=\frac{2\kappa_S}{S}.}
\tag{RC13}

Choose a fixed nonzero `r` and set

\[
\boxed{
k_S
=
\frac{m_Sr}{\sqrt{1+x^2}}\tau_S.}
\tag{RC14}

Thus

\[
\frac{k_S}{r}=O(S^{-1}),
\]

so the root polarization approaches the pure `N` direction.  This remains transverse to the radial beta-zero phase normal for every `S`.

Put

\[
L_x:=\sqrt{1+x^2}.
\]

Substitute (RC14) into (RC7)--(RC9) with `s=x`.  Since

\[
s_t=x+\frac{m_S}{b},
\]

a direct first-order expansion gives

\[
\boxed{
A_b^+
=
\frac{m_Sr}{2L_x}
\left(1+2b\tau_S\right)
+O(m_S^2r),
}
\tag{RC15}

uniformly for `tau_S` in a fixed compact set.

## 6. Limiting beta-two/beta-one ratio

For beta one (`C` orbit) and beta two (`P` orbit), (RC15) gives

\[
A_1^+
=
\frac{m_Sr}{2L_x}(1+2\tau_S)+O(m_S^2r),
\]

\[
A_2^+
=
\frac{m_Sr}{2L_x}(1+4\tau_S)+O(m_S^2r).
\tag{RC16}

Hence, provided `1+2tau !=0`,

\[
\boxed{
\frac{A_2^+}{A_1^+}
\to
\mathfrak R(\tau)
:=
\frac{1+4\tau}{1+2\tau}.
}
\tag{RC17}

The derivative is

\[
\boxed{
\mathfrak R'(\tau)
=
\frac{2}{(1+2\tau)^2}\ne0.
}
\tag{RC18}

Thus the limiting coupling ratio is a transverse one-real-parameter function of the boundary-layer root polarization.

## 7. Required polarization at the selected dispersion point

Solve

\[
\mathfrak R(\tau_*)=R_*.
\]

The exact algebraic solution is

\[
\boxed{
\tau_*
=
\frac{1-R_*}{2(R_*-2)}.
}
\tag{RC19}

Numerically,

\[
\boxed{
\tau_*=-0.2087411867089201\ldots.
}
\tag{RC20}

At this value,

\[
1+2\tau_*
\approx0.58251762658>0,
\]

\[
1+4\tau_*
\approx0.16503525316>0.
\tag{RC21}

Thus both catalyst and parent principal shift couplings are nonzero and have the same sign.  One common scalar root amplitude can then choose the common sign and absolute catalyst strength; the polarization parameter fixes the parent/catalyst ratio.

In particular a negative common amplitude produces the negative pair required by the current

\[
\lambda_C<0,
\qquad
\mu_P<0.
\]

## 8. Finite-`S` persistence of the ratio

Define the exact principal ratio, in the same source-frame growing coefficient convention, by

\[
\mathfrak R_S(\tau)
:=
\frac{A_2^+(x,m_S;k_S(\tau),r)}
{A_1^+(x,m_S;k_S(\tau),r)}.
\tag{RC22}

Equations (RC15)--(RC18) imply

\[
\mathfrak R_S(\tau)
=
\mathfrak R(\tau)+O(m_S)
\]

in `C^1` on a sufficiently small compact neighborhood of `tau_*`.

Since

\[
\mathfrak R'(\tau_*)\ne0,
\]

the one-dimensional implicit-function theorem gives, for all sufficiently large `S`, a unique

\[
\boxed{
\tau_S=\tau_*+O(m_S)
=\tau_*+O(S^{-1})
}
\tag{RC23}

such that

\[
\boxed{
\mathfrak R_S(\tau_S)=R_*.
}
\tag{RC24}

Thus the physical single-root ratio is not merely asymptotically close: at principal finite-`S` source-frame level it can be tuned exactly by the root polarization.

## 9. Common amplitude and semigroup strengths

After `tau_S` is selected, the catalyst coupling `A_1^+` is nonzero.  Let `alpha_M` denote the scalar amplitude multiplying the Cauchy root.  Both shift coefficients depend linearly on it:

\[
a_C=\alpha_M\chi_1(S)A_1^+,
\]

\[
a_P=\alpha_M\chi_2(S)A_2^+.
\tag{RC25}

In the source-frame growing-coordinate convention used in (RC9), the polarization projection itself has `chi_1=chi_2=1`.  Any additional fixed sector-dependent normalization introduced later by the exact source packet amplitude convention must be inserted explicitly here; it cannot be silently absorbed into two independent coefficients.

If the exact source realization gives constants/functions `chi_b(S)` with finite nonzero limits, then the ratio equation becomes

\[
\frac{\chi_2(S)}{\chi_1(S)}\mathfrak R_S(\tau_S)=R_*.
\tag{RC26}

Because `mathfrak R'(tau_*) !=0`, this equation remains locally solvable except at the isolated pole `1+2tau=0`.  Thus a fixed finite sector normalization does not recreate a structural ratio obstruction; it only shifts the required polarization value.

Finally choose `alpha_M` so that

\[
2\kappa_S a_C=\lambda_C
\tag{RC27}
\]

(or its finite-`S` corrected target).  Equation (RC24)/(RC26) then gives the required parent strength simultaneously.

## 10. Cauchy realizability of the tuned polarization

The curl construction in
`beta21_lowu_designated_mean_root_cauchy_curl_realization.md`
uses only:

1. a nonzero beta-zero phase covector `Xi_M`;
2. a smooth polarization transverse to `Xi_M`;
3. a scalar root amplitude;
4. a compact source-admissible cutoff.

The tuned polarization

\[
\boxed{
b_{M,S}
=
\frac{m_Sr\tau_S}{L_x}K+c_0rN
}
\tag{RC28}

satisfies all four requirements.  Its `K` coefficient tends to zero while its `N` coefficient remains nonzero.  Therefore all normalized curl and semiclassical jet estimates remain uniform; indeed the `K` part is smaller than in the fixed-polarization construction.

Thus the tuned root is honest incoming divergence-free Cauchy data and introduces no future-time control.

## 11. Correction to the low-`u` theorem chain

The limiting coefficients `lambda_C,mu_P` in
`beta21_lowu_boundary_layer_bilateral_orbit_reset.md`
must not be interpreted as two independently free interaction constants.

The correct principal parameter count is:

- one root scalar amplitude `alpha_M` fixes the common absolute shift strength;
- one transverse polarization parameter `tau` fixes the beta-two/beta-one ratio;
- the boundary-layer spacing/phase parameters continue to enforce the dispersion/reset conditions.

Therefore the low-`u` limiting fixed point remains **parameter-count compatible with one physical beta-zero root**.

## 12. Remaining exact obligation

Before publication, pin the exact source amplitude convention in (RC25):

1. identify the source packet coefficient coordinate corresponding to the growing projection (RC9);
2. compute the finite nonzero sector normalization ratio `chi_2/chi_1` if it is not exactly one;
3. replace (RC20) by the corrected root of (RC26) if necessary;
4. differentiate the exact tuned coupling with respect to slope to obtain the profile-normal-form coefficients `B_C,B_P` required by `beta21_lowu_finiteS_designated_profile_obligation.md`.

The important structural conclusion is already proved:

\[
\boxed{
\text{one physical Cauchy root can supply both low-`u` shift sectors;}
\quad
\text{no single-root ratio obstruction remains.}
}
