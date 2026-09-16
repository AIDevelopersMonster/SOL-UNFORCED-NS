# Source growing-coordinate normalization for the low-`u` root coupling

**Status:** PROVED COMMON PRINCIPAL GROWING-COORDINATE NORMALIZATION FOR BETA-ONE AND BETA-TWO SECTORS / FINITE-S FRAME PERTURBATIONS REMAIN LOWER-ORDER.  This note pins the normalization factor left open in `beta21_lowu_single_root_coupling_ratio.md`.

The question is whether the source primary-wave convention inserts a hidden sector-dependent scalar `chi_b` between the principal growing projection coefficient `A_b^+` and the coefficient used in the orbit shift equation.  At principal source-frame level it does not: both sectors use the same positive homogeneous seed and the same synthesis convention.  Thus

\[
\boxed{\chi_1=\chi_2=1}
\]

in the natural source growing coordinate.

No assertion is made that the full finite-`S` physical frame is literally identical in the two sectors; those smooth differences belong to the already-audited `O(S^{-1})`/source-small coefficient perturbation.

## 1. The common positive homogeneous seed

The source file `NavierStokes/PrimaryPulseBounds.lean` defines

\[
\texttt{positiveSeed}:=(1,0)
\]

in the two-dimensional moving-frame state and proves

\[
\|\texttt{positiveSeed}\|=1.
\]

The actual growing fundamental solution is initialized by

\[
\texttt{referenceP}(0)\,\texttt{positiveSeed}
\]

and `fundamental_eq_primary` identifies that constructed fundamental with the source primary solution.

The definition is label-independent.  In particular no beta-dependent scalar is inserted into the positive state coordinate.

## 2. Common synthesis of the physical growing vector

The same source file defines

\[
\texttt{synthesisColumn}(d,0)
\]

for the positive column by

\[
\boxed{
\operatorname{pack}
\left(
1,
-\rho K+\lambda_+N
\right),
}
\tag{SN1}

in source notation, where `rho`, the moving frame `(K,N)`, and the positive eigenvector/eigenvalue coefficient are supplied by the current label geometry.

The theorem `ambient_eq_synthesis` gives

\[
\boxed{
\texttt{ambient}(w)
=w_0\,\texttt{synthesisColumn}(d,0)
+w_1\,\texttt{synthesisColumn}(d,1).
}
\tag{SN2}

Thus the first state coordinate is literally the scalar coefficient of the positive physical column.

This is exactly the coordinate used by the branch polarization formula

\[
g(s)=e_r-sK+c_0\sqrt{1+s^2}N.
\]

The branch notation differs, but the normalization convention is the same: unit radial coefficient and the positive `N` eigenvector sign.

## 3. Physical covariance amplitude is an external scalar coefficient

The source `primaryCoefficient` is

\[
\boxed{
\texttt{PartitionedCovariance.amplitude}\times
\texttt{complexify}(v),
}
\tag{SN3}

where `v` is the physical synthesis vector.

Therefore the covariance construction chooses the scalar amount of a primary wave; it does not renormalize the positive synthesis column differently for beta one and beta two.

For a bilinear root-wave interaction, the incoming wave scalar amplitude factors linearly from the interaction.  The output growing projection `A_b^+` is the scalar coefficient relative to the target positive synthesis column.  Consequently the induced linear translation coefficient is

\[
\boxed{
a_b=\alpha_M A_b^+}
\tag{SN4}

up to the common time/action normalization already displayed explicitly in the low-`u` orbit theorem.

There is no additional principal sector factor.

## 4. Consequence for the low-`u` ratio equation

The general placeholder relation

\[
a_C=\alpha_M\chi_1A_1^+,
\qquad
 a_P=\alpha_M\chi_2A_2^+
\]

therefore has

\[
\boxed{\chi_1=\chi_2=1}
\tag{SN5}

in the source positive-coordinate normalization.

Hence the required principal ratio is exactly

\[
\frac{a_P}{a_C}
=\frac{A_2^+}{A_1^+}.
\]

The tuned boundary-layer polarization parameter from
`beta21_lowu_single_root_coupling_ratio.md` remains

\[
\boxed{
\tau_*
=-0.2087411867089201\ldots.
}
\tag{SN6}

No correction of `tau_*` by a hidden beta-sector normalization is required.

## 5. Finite-`S` frame variation

At finite `S`, the beta-one and beta-two labels have slightly different slopes and therefore slightly different actual `rho`, eigenvector and frame coefficients.  These differences are already part of the exact slope dependence in

\[
A_b^+(s,m;k,r)
\]

and the source/frame perturbation terms.

They are not independent constant normalizations.  On the central profile scale they enter the first derivative coefficients and the `O(h_S^2)` remainder of the profile normal form.

Thus they must be differentiated, not represented by arbitrary constants `chi_b`.

## 6. Consequence

The single-root principal compatibility chain is now closed:

\[
\boxed{
\text{one root amplitude}
+\text{ one transverse polarization parameter}
\Longrightarrow
(\lambda_C,\mu_P)
\text{ at the selected low-`u` dispersion point}.
}
\]

The next unresolved local theorem is no longer source amplitude normalization.  It is the exact discrete finite-`S` profile equation around the continuum operator

\[
\mathcal L_b=v_b\partial_y+B_by+C_b.
\]
