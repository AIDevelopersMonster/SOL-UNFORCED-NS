# STATUS

**Project:** SOL-UNFORCED-NS  
**Bootstrap:** v0.1  
**Date:** 2026-09-09

## Claim discipline

### Established inside this repository only after direct algebra/numerical checking

- The rational relay choice
  \[
  r=\frac{17}{12},
  \qquad
  h=2\log_2\!\frac{17}{12}-1
  \approx 0.005000681058366707
  \]
  satisfies \(0<h<1/100\).

- With
  \[
  \beta_1=\frac{93}{100},
  \qquad
  \beta_2=\frac{73}{150},
  \]
  we have
  \[
  \beta_1+\beta_2=\frac{17}{12},
  \qquad
  \beta_-=\beta_1-\beta_2=\frac{133}{300}.
  \]

- For the current reduced large-\(u_*\) model,
  \[
  F_\beta(x)=\frac1x-\beta^2x^2,
  \]
  the witness
  \[
  x_c=\frac{17}{32},
  \quad
  x_1\approx1.550891747,
  \quad
  x_2\approx-1.417243476
  \]
  gives
  \[
  F_{\beta_1}(x_1)<0,\qquad
  F_{\beta_2}(|x_2|)>0,\qquad
  F_1(x_c)>0.
  \]

- Under the current phase bookkeeping, the associated difference branch has
  \[
  x_-\approx4.80914545044
  \]
  and
  \[
  F_{\beta_-}(x_-)<0.
  \]

These calculations are reproducible with `experiments/relay_parameter_scan.py`.

## Source-derived statements that still require exact source-line/page audit before publication

- Physical carrier scaling inferred from the OpenAI forced Navier–Stokes normalization:
  \[
  \Omega_\ell\asymp Q^{-(1+h)/2}.
  \]

- The next-band ratio:
  \[
  \Omega_{\ell+1}/\Omega_\ell = 2^{(1+h)/2}.
  \]

- The principal reduced β-growth model:
  \[
  a_\beta(s)
  =
  \lambda_0
  \left[
  \frac{1}{\sqrt{1+s^2}}
  -
  \beta^2
  \frac{1+s^2}{(1+u_*^2)^{3/2}}
  \right].
  \]

- Wave-class power counting for the relay source and curl remainders.

These are working transcriptions/inferences from the cited papers and must be re-audited against the exact definitions before they are elevated to theorem statements.

## Not proved

- Existence of an exact unforced localized relay.
- Stability of the relay under physical localization.
- Preservation of all OpenAI correction-cycle estimates after controlled support overlap.
- Closure of all residual terms with \(R\equiv0\).
- Finite-time blowup for unforced 3D Navier–Stokes.

## GitHub threshold

Reached.

Reason: the project now contains independent mathematical objects, explicit parameters, competing barriers, a falsifiable local lemma, and reproducible computations.

## Publication threshold

Not reached.

Minimum desired threshold:

> A rigorous **Controlled-Overlap Local β-Relay Lemma** for localized divergence-free packets with a quantified growing projection and a strictly improved remainder class.
