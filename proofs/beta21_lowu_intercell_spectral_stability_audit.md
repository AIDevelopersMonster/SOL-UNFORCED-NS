# Spectral stability audit of the low-`u` bilateral reset

**Status:** PROVED LIMITING SPECTRAL INSTABILITY OF THE CANONICAL BILATERAL FIXED PROFILE / GLOBAL ASSEMBLY STRATEGY CORRECTED.  The exact finite-`S` local reset theorem gives one exact canonical cell, but an infinite chain cannot be justified merely by showing that the next incoming orbit profile is `o(1)` close to the canonical one.  The limiting bilateral Poincare operators possess transverse expanding spectral directions.

Therefore the global programme needs either:

1. an **exact invariant inter-cell profile/cocycle**, or
2. a genuine global shadowing/stable-manifold construction that controls the expanding directions.

A naive accumulation of small dyadic-boundary mismatch errors is not sufficient.

No claim about impossibility of a global cascade is made; this note only identifies the correct dynamical requirement.

## 1. Limiting catalyst Poincare operator

For the catalyst orbit, the limiting full-cell map is

\[
\boxed{\mathcal P_C=R^{-1}e^{\lambda_C R}.}
\tag{SA1}
\]

The canonical bilateral profile is a shift eigenprofile

\[
Rc=\rho_Cc
\]

with

\[
\boxed{\rho_C=0.3510126502440001\ldots}
\tag{SA2}
\]

and

\[
\boxed{\lambda_C=-2.982607649202283\ldots.}
\tag{SA3}
\]

The fixed-point relation is

\[
\boxed{e^{\lambda_C\rho_C}=\rho_C.}
\tag{SA4}
\]

## 2. Catalyst spectral multiplier

For a formal shift eigenvalue `zeta`,

\[
R f_\zeta=\zeta f_\zeta,
\]

the catalyst Poincare multiplier is

\[
\boxed{
m_C(\zeta)=\frac{e^{\lambda_C\zeta}}{\zeta}.}
\tag{SA5}
\]

On the natural spectral circle through the canonical eigenvalue, write

\[
\zeta=\rho_Ce^{i\phi}.
\]

Then

\[
\log|m_C(\zeta)|
=\lambda_C\rho_C\cos\phi-\log\rho_C.
\]

By (SA4),

\[
\lambda_C\rho_C=\log\rho_C.
\]

Therefore

\[
\boxed{
\log|m_C(\rho_Ce^{i\phi})|
=\log\rho_C(\cos\phi-1).
}
\tag{SA6}

Since

\[
0<\rho_C<1,
\qquad
\log\rho_C<0,
\]

we obtain

\[
\boxed{
|m_C(\rho_Ce^{i\phi})|>1
\quad\text{for every }\phi\not\equiv0\pmod{2\pi}.
}
\tag{SA7}

Thus the canonical catalyst eigenprofile is not transversely attracting on this spectral circle.

At the opposite point `phi=pi`,

\[
\log|m_C(-\rho_C)|=-2\log\rho_C,
\]

hence

\[
\boxed{
|m_C(-\rho_C)|=\rho_C^{-2}
\approx8.11623.
}
\tag{SA8}

The transverse expansion can therefore be large in one cell.

## 3. Limiting parent Poincare operator

For the parent orbit,

\[
\boxed{\mathcal P_P=R^{-2}e^{\mu_PR}.}
\tag{SA9}

The canonical shift eigenvalue is

\[
\boxed{
\rho_P
=-2.147691668824314
+1.235899139340218\,i,
}
\tag{SA10}

with

\[
\boxed{\mu_P=-0.845013757547658\ldots.}
\tag{SA11}

The fixed-point relation is

\[
\boxed{e^{\mu_P\rho_P}=\rho_P^2.}
\tag{SA12}

Numerically,

\[
\boxed{
\mu_P\rho_P
\approx
1.814829007127034
-1.044351775683794\,i.
}
\tag{SA13}

## 4. Parent spectral multiplier

For a shift spectral value `zeta`,

\[
\boxed{
m_P(\zeta)=\frac{e^{\mu_P\zeta}}{\zeta^2}.}
\tag{SA14}

Put

\[
\zeta=\rho_Pe^{i\phi}.
\]

Because `|zeta|=|rho_P|`,

\[
\log|m_P(\zeta)|
=
\Re(\mu_P\rho_Pe^{i\phi})
-2\log|\rho_P|.
\]

Taking absolute values in (SA12) gives

\[
2\log|\rho_P|=\Re(\mu_P\rho_P).
\]

Hence

\[
\boxed{
\log|m_P(\rho_Pe^{i\phi})|
=
\Re\bigl(\mu_P\rho_P(e^{i\phi}-1)\bigr).
}
\tag{SA15}

The maximum over `phi` is

\[
\boxed{
\max_\phi\log|m_P|
=|\mu_P\rho_P|-\Re(\mu_P\rho_P).
}
\tag{SA16}

Using (SA13),

\[
|\mu_P\rho_P|
\approx2.0938660311690405,
\]

so

\[
\boxed{
\max_\phi|m_P|
\approx1.32185628>1.
}
\tag{SA17}

There are therefore parent transverse expanding directions as well.

For comparison, the minimum modulus on the same circle is approximately

\[
\boxed{
\min_\phi|m_P|
\approx0.0200667,
}
\tag{SA18}

so the parent sector is strongly mixed stable/unstable rather than uniformly unstable.

## 5. Consequence for small inter-cell errors

Suppose one writes the incoming orbit at cell `j` as

\[
U_j=U_{can,j}+e_j.
\]

A bound of the form

\[
\|e_{j+1}\|
\le
C\|e_j\|+\delta_j,
\qquad
\delta_j\to0,
\]

with merely bounded `C>1`, is not enough to guarantee a globally bounded shadowing orbit.

The limiting catalyst calculation shows that the true transverse linearized factor can exceed eight on parts of the shift spectrum.  Thus even very small boundary-transfer errors may amplify rapidly if they possess components in the unstable spectral directions.

Therefore the statement

\[
\boxed{
\text{“dyadic resampling error tends to zero”}
}
\]

is insufficient by itself for an infinite cascade theorem.

## 6. What remains viable

The instability does **not** invalidate the exact local reset theorem.  It changes the global strategy.

Three routes remain mathematically viable.

### Route A: exact invariant cocycle

Construct a scale-dependent bilateral profile

\[
U_{inv}(q,S)
\]

such that exact gap transport followed by the exact local cell satisfies

\[
\boxed{
U_{inv,j+1}
=\mathcal F_j(U_{inv,j})
}
\tag{SA19}
\]

with no transverse mismatch.  This is the preferred route because it avoids backward specification of future corrections.

### Route B: nonautonomous stable manifold

Split the full inter-cell cocycle into stable, center and unstable spectral bundles and construct one forward orbit lying on the corresponding nonautonomous stable/center manifold.  This requires a genuine exponential-dichotomy theorem in the scale-dependent weighted sequence spaces.

Any use of this route must be audited against the backward-heat obstruction: the stable-manifold construction must not amount to storing exponentially large future high-frequency data in the initial state.

### Route C: exact profile-generating forward dynamics

Exploit the fact that the root shift semigroup itself generates new orbit indices forward.  Instead of resetting to a separately prescribed canonical truncated profile at every source level, construct one forward infinite-sequence state whose changing physical localization automatically supplies the needed newly visible orbit tails.

This would replace dyadic profile resampling by one global sequence-space evolution.

## 7. Corrected global frontier

The sharp next question is no longer simply

\[
\text{“is the dyadic profile mismatch }o(1)\text{?”}
\]

It is

\[
\boxed{
\text{does there exist an exact forward invariant low-`u` orbit profile across scale?}
}
\tag{SA20}

The preferred next theorem is therefore

`beta21_lowu_intercell_invariant_profile.md`.

It should first attack the principal shift cocycle, where the Poincare maps are explicit functions of `R`, before reintroducing the source-small PDE correction.

No global unforced Navier--Stokes claim is justified until this invariant-profile/shadowing problem is closed.
