# Physical-scale inheritance update v0.5

**Branch:** `research/physical-scale-inheritance-v0.1`  
**Date:** 2026-09-11

## New theorem-level closure

`proofs/source_normalized_two_event_coefficients.md` closes the source-normalized coefficient audit for both designated events in the correct uniform form.

After freezing one admissible v0.8 design `M`, define

\[
rho(p):=\sqrt{\varepsilon_\ell}\,k_\ell B_{s,\ell}(p).
\]

Using the exact source normalization of `B_s`,

\[
\boxed{
rho(p)=\frac{\sqrt{\lambda_0(p)}}{(1+M^4)^{3/4}},
}
\]

so the apparently dangerous physical-scale factor is exactly independent of the dyadic level `ell`.

For the first event `2-1->1`, the full leading normalized coefficient has the form

\[
\kappa_1^0(p)
=\varsigma_1\,rho(p)\,Gamma_1(M)
\int \omega_1(\xi)e^{\mu_1(p)\xi}\,d\xi,
\]

with

\[
|Gamma_1(M)|\ge 3M/16.
\]

For the second event `1+1->2`,

\[
\kappa_2^0(p)
=\varsigma_2\,rho(p)\,Gamma_2(M)
\int \omega_2(\xi)e^{\mu_2(p)\xi}\,d\xi,
\]

with `Gamma_2(M)` uniformly positive for the frozen design.

Taking fixed nonnegative nonzero overlap profiles `omega_1,omega_2`, both integrals are strictly positive. On every compact strict-cone slow set,

\[
\boxed{
0<c_{i,M}\le|\kappa_i^0(p)|\le C_{i,M}<\infty,
\qquad i=1,2.
}
\]

The actual localized coefficients satisfy

\[
\boxed{
\kappa_{i,\ell}^{loc}(p)
=\kappa_i^0(p)+o_\ell(1)
}
\]

uniformly, because the source frame/phase error is `O(S_*^{-1})`, while curl and transport/base remainders carry positive epsilon powers.

## Important correction to v0.4 status

The previous update stated the remaining target as convergence to two universal numbers

\[
\kappa_{i,\ell}\to\kappa_i^*\ne0.
\]

That statement was unnecessarily strong. Along the trapped material spine the slow profile point is known to remain in a compact strict-cone set, but is not yet known to converge to a single point. Therefore one should not assert a universal scalar limit without an additional slow-profile convergence theorem.

The correct result is stronger for the construction and weaker logically:

\[
\boxed{
\kappa_{i,\ell}(p_\ell)
=\kappa_i^0(p_\ell)+o(1),
\qquad
\inf_{p\in K_{slow}}|\kappa_i^0(p)|>0.
}
\]

Thus designated coefficient degeneration cannot occur anywhere along the admissible trapped spine.

## Uniform principal renewal transversality

For

\[
a(p)=|\kappa_1^0(p)|,
\qquad
b(p)=|\kappa_2^0(p)|,
\]

the principal magnitude map has the positive fixed state

\[
x_*(p)=a(p)^{-1},
\qquad
y_*(p)=[a(p)b(p)]^{-1/2}.
\]

A direct calculation improves the earlier generic nonzero determinant to

\[
\boxed{
\det D F_p(x_*(p),y_*(p))=-2.
}
\]

This determinant is exactly independent of `p`, `a` and `b`. Therefore the principal two-event renewal section has a **uniform transversality margin** along the entire slow compact set.

## New sharp frontier

The coefficient audit is no longer the bottleneck. The next theorem-level target is the uniform parameter-dependent exact map estimate

\[
\boxed{
\mathscr R_{\ell,p}
=\mathscr R_{0,p}+o_{C^1}(1)
}
\]

on one fixed compact neighborhood of the principal fixed-state section, uniformly for `p in K_slow`.

If this is established, the determinant `-2` gives a uniform implicit-function theorem and therefore an **exact nonzero two-collar renewal state** for every sufficiently high physical level.

Only after that should the argument move to global shadowing of these exact local renewal states under physical cross-`q` transport and infinite accumulation toward `t=1`.

## Publication status

The local one-collar zero-residual method remains a publication candidate pending the already identified line audit against exact source packet norms and v0.8 designated persistence.

The global/autonomous result is still **below publication threshold**. The major remaining steps are:

1. uniform `C^1` exact two-collar renewal theorem;
2. cross-`q` shadowing of the two-component renewal section;
3. infinite-cell global assembly and summability;
4. construction of one global smooth finite-energy unforced solution;
5. proof of actual finite-time singularity.

No unforced Navier--Stokes blowup theorem is claimed at this stage.