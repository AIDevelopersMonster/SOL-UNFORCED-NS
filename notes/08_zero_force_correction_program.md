# Note 08 — zero-force correction program after stable sum-sideband inversion

The corrected v0.4 relay has now passed one more local test: the unwanted sum harmonic

\[
\beta_+=17/8
\]

has an exact finite-`u_*` damping gap on the full resonance bracket, and its scalar moving-frame coefficient equation has a bounded forward inverse. See `proofs/sum_sideband_local_inverse.md`.

This changes the remaining local problem from

> can the unwanted sideband be damped?

into

> can all correction-generated terms be solved simultaneously with zero external force?

## Proposed correction map

Write the localized relay state schematically as

\[
W=W_1+W_2+W_c+Z,
\]

where `W_1,W_2` are the designated parents, `W_c` is the extracted desired child branch, and `Z` is the sum of all correction modes.

After subtracting the desired child source, write the remaining residual as

\[
\mathcal R(Z)=R_0+LZ+Q(Z)+C(Z),
\]

where:

- `R_0` contains the first unwanted sum sideband, cutoff defects and improved curl/localization errors;
- `L` is the linearized packet operator on the correction modes;
- `Q(Z)` contains correction-correction quadratic terms;
- `C(Z)` contains parent/catalyst/child interactions with corrections.

The zero-force problem is to solve

\[
\boxed{\mathcal R(Z)=0.}
\]

Equivalently, after inverting the stable/improved pieces of `L`,

\[
\boxed{Z=\mathcal T(Z).}
\]

## Desired contraction structure

The current estimates suggest three distinct small parameters:

1. the unwanted sum mode has a fixed stable inverse with no epsilon loss;
2. curl/localization remainders gain at least `epsilon^(1/2-kappa_s)` relative to the principal relay source;
3. feedback generated while the child is still a tail carries an extra Gaussian factor `exp(-c S_*)`.

The target norm should therefore weight correction components according to their mechanism rather than forcing all of them into one unweighted amplitude class.

A plausible schematic norm is

\[
\|Z\|_{\mathfrak X}
=
\sup_{\gamma}
\left(
\varepsilon^{-\alpha_\gamma}
S_*^{-C_\gamma}
P_\gamma^{-1}
\|Z_\gamma\|
\right),
\]

with separate exponents for stable sidebands, curl remainders and flat feedback modes.

The next theorem-level target is:

### Local nonlinear correction contraction

Find a ball `B_R` in a weighted correction space such that for all sufficiently large levels,

\[
\mathcal T(B_R)\subseteq B_R,
\]

and

\[
\|\mathcal T(Z)-\mathcal T(\widetilde Z)\|_{\mathfrak X}
\le\kappa\|Z-\widetilde Z\|_{\mathfrak X},
\qquad \kappa<1.
\]

If proved, Banach's fixed-point theorem would eliminate the local non-designated residual **exactly**, instead of exporting it into a smooth external force.

## Warning

The source forced construction does not need such a theorem because exponentially flat residuals may be absorbed into the prescribed smooth force. Therefore this contraction is genuinely new work; it cannot be cited as already contained in the source paper.

The first subproblem is to classify every correction-generated harmonic produced by `W_+^{corr}` and determine whether it lands in:

- a uniformly stable beta sector;
- an algebraically improved packet class;
- or a potentially resonant sector requiring a new cancellation.
