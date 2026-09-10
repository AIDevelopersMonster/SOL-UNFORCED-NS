# Localized growing-projection stability for the corrected difference relay

**Status:** PROVED ABSTRACT STABILITY LEMMA / CONDITIONAL PDE APPLICATION. The functional estimate below is elementary and rigorous under the stated packet-class hypotheses. The remaining audit is to verify that the exact localized curl-generated packets used in the source construction satisfy those hypotheses with the required constants.

## 1. Principal margin

For the corrected v0.4 difference relay

\[
\beta_1=\frac{25}{16},\qquad
\beta_2=\frac9{16},\qquad
\beta_1-\beta_2=1,
\]

`difference_branch_projection.md` gives a principal child growing coefficient \(A_+^{(0)}\) which is uniformly separated from zero in a small neighborhood \(\mathcal U\) of the certified resonance:

\[
\boxed{|A_+^{(0)}|\ge c_*=0.38.}
\tag{S1}
\]

The precise numerical constant is not structurally important; what matters is a fixed positive margin independent of the dyadic level.

## 2. Packet decomposition

Let the two localized divergence-free parent packets have the form

\[
W_j=W_j^{(0)}+R_j,
\qquad j=1,2,
\]

where the principal pieces satisfy the primary coefficient scale

\[
W_j^{(0)}\in W^{1/2}
\]

and the curl/localization remainders satisfy

\[
R_j\in W^{1-\kappa_s},
\qquad 0<\kappa_s<\frac12.
\]

Assume one oscillatory derivative costs

\[
O(\varepsilon^{-1/2}S_*^C)
\]

and the phase-normal/Leray frame errors are

\[
O(S_*^{-1})
\]

uniformly in the designated relay collar.

These are the packet-class hypotheses that must be checked against the exact source formulas before the lemma is promoted from conditional application to a source-embedded PDE statement.

## 3. Expansion of the designated difference interaction

Write the desired difference-harmonic component of

\[
\mathcal N(W_1,W_2)
:=\mathbb P\big[(W_1\cdot\nabla)W_2+(W_2\cdot\nabla)W_1\big]
\]

as

\[
\mathcal N_-=
\mathcal N_-^{00}
+\mathcal N_-^{0R}
+\mathcal N_-^{R0}
+\mathcal N_-^{RR}.
\]

The principal-principal term has size

\[
\mathcal N_-^{00}
=O(\varepsilon^{1/2}S_*^C P_1P_2),
\]

because

\[
\varepsilon^{1/2}\varepsilon^{1/2}\varepsilon^{-1/2}
=\varepsilon^{1/2}.
\]

A term with one remainder obeys

\[
\mathcal N_-^{0R},\mathcal N_-^{R0}
=O(\varepsilon^{1-\kappa_s}S_*^C P_1P_2),
\tag{S2}
\]

since

\[
\varepsilon^{1/2}\varepsilon^{1-\kappa_s}\varepsilon^{-1/2}
=\varepsilon^{1-\kappa_s}.
\]

The remainder-remainder term is still smaller:

\[
\mathcal N_-^{RR}
=O(\varepsilon^{3/2-2\kappa_s}S_*^C P_1P_2).
\tag{S3}
\]

Therefore, relative to the principal source scale,

\[
\boxed{
\frac{|
\mathcal N_-^{0R}+
\mathcal N_-^{R0}+
\mathcal N_-^{RR}|}
{\varepsilon^{1/2}P_1P_2}
\le
C S_*^C\varepsilon^{1/2-\kappa_s}.
}
\tag{S4}
\]

Because \(\kappa_s<1/2\) and \(\varepsilon=Q^h\) decays exponentially in the dyadic level while \(S_*\) grows only polynomially, the right-hand side tends to zero.

## 4. Frame and Leray perturbations

Let \(\Pi_{+,0}\) denote the reference projection onto the child growing coordinate and \(\Pi_+\) the actual local one. Under the phase/frame hypothesis,

\[
\|\Pi_+-\Pi_{+,0}\|\le CS_*^{-1}.
\tag{S5}
\]

Thus the full normalized growing coefficient satisfies

\[
A_+
=A_+^{(0)}+E_{\rm loc},
\]

with

\[
\boxed{
|E_{\rm loc}|
\le C\left(S_*^{-1}+S_*^C\varepsilon^{1/2-\kappa_s}\right).
}
\tag{S6}
\]

Both terms tend to zero with the level.

## 5. Stability lemma

Choose \(\ell_0\) so large that for every \(\ell\ge\ell_0\),

\[
C\left(S_*^{-1}+S_*^C\varepsilon^{1/2-\kappa_s}\right)
\le\frac{c_*}{2}.
\tag{S7}
\]

Then (S1) and (S6) give

\[
\boxed{
|A_+|\ge\frac{c_*}{2}=0.19.
}
\tag{S8}
\]

Consequently the desired localized difference-harmonic source cannot be erased by curl remainders, localization errors, or the \(O(S_*^{-1})\) perturbation of the child frame, provided the exact packets satisfy the stated source-class bounds.

Restoring the physical coefficient scale gives the schematic lower bound

\[
\boxed{
|\Pi_+S_c|
\ge
c_{\rm loc}\,A_1A_2\Omega\,P_1P_2,
\qquad c_{\rm loc}>0,
}
\tag{S9}
\]

with a constant independent of the sufficiently large relay level.

## 6. Significance

This removes an important **stability** obstruction: the principal nonzero growing projection has enough margin to survive the known improved packet remainder classes.

It does **not** yet prove the full Controlled-Overlap Local Difference-Relay Lemma because three items remain:

1. line-by-line source audit that the exact curl-generated packets and phase/Leray corrections satisfy the hypotheses used above;
2. exact solution of the strongly damped sum branch and all feedback/cutoff residuals with zero forcing;
3. compatibility of the resulting local module with later physical-scale inheritance \(q_j\to q_{j+1}\).
