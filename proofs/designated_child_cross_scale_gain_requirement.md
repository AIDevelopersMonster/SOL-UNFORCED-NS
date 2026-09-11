# Exact cross-scale gain required of the designated child

**Status:** PROVED NECESSARY SCALE LAW / DYNAMICAL GAIN STILL OPEN.

This note isolates the remaining physical-scale inheritance problem after `previous_relay_mean_tail_subcriticality.md`. The whole-space mean/pressure tail is source-small and subcritical at the next scale. The unresolved issue is whether the **designated nonzero child packet** generated at physical level `q_j` arrives at `q_{j+1}<q_j` with the amplitude and carrier normalization required to serve as a next-scale primary packet.

## 1. Physical size of one primary packet

The source physical base velocity scale is

\[
U_{\rm base}(q)\asymp q^{-A},
\qquad
A=\frac12+h.
\tag{CG1}
\]

A primary packet has coefficient order

\[
W_{1/2},
\]

so its normalized amplitude is `epsilon^{1/2}` with

\[
\varepsilon(q)=q^h.
\tag{CG2}
\]

Therefore its physical velocity amplitude is

\[
\boxed{
U_{\rm pkt}(q)
\asymp
q^{-A}\varepsilon(q)^{1/2}
=q^{-1/2-h/2}.
}
\tag{CG3}
\]

By `chart_invariant_carrier_scale.md`, the intrinsic physical carrier satisfies

\[
\boxed{
\Omega_{\rm phys}(q)
\asymp q^{-(1+h)/2}.
}
\tag{CG4}
\]

But

\[
\frac{1+h}{2}=\frac12+\frac h2.
\]

Hence the primary packet velocity amplitude and the intrinsic carrier have the **same q exponent**:

\[
\boxed{
U_{\rm pkt}(q)\asymp \Omega_{\rm phys}(q)
}
\tag{CG5}
\]

up to the frozen profile/design constants.

This identity is not an assumption; it follows directly from the source `W_{1/2}` amplitude normalization and the corrected physical carrier law.

## 2. Required gain between two physical levels

Let

\[
q_{j+1}=\vartheta q_j,
\qquad 0<\vartheta<1.
\tag{CG6}
\]

For a packet at `q_j` to become a correctly normalized primary packet at `q_{j+1}`, its physical amplitude must grow by

\[
\frac{U_{\rm pkt}(q_{j+1})}{U_{\rm pkt}(q_j)}
=\vartheta^{-(1+h)/2}.
\tag{CG7}
\]

The required physical carrier changes by exactly the same factor:

\[
\frac{\Omega_{\rm phys}(q_{j+1})}{\Omega_{\rm phys}(q_j)}
=\vartheta^{-(1+h)/2}.
\tag{CG8}
\]

Therefore a successful cross-scale relay must satisfy the paired inheritance law

\[
\boxed{
\frac{U_{c,j+1}}{U_{c,j}}
\sim
\frac{\Omega_{c,j+1}}{\Omega_{c,j}}
\sim
\vartheta^{-(1+h)/2}.
}
\tag{CG9}
\]

This is much sharper than the vague statement that the child must merely be amplified.

## 3. Why changing dyadic chart does not supply the gain

`chart_invariant_carrier_scale.md` proves that, at a fixed physical point, changing dyadic chart label leaves the physical carrier unchanged. Therefore the factor in (CG9) cannot be produced by passing from one overlapping chart to another.

It must arise from genuine evolution to a smaller physical `q`.

Thus any cross-band argument based on a chart-scale ratio alone is invalid.

## 4. Dimensionless packet amplitude at the next level

Suppose the child leaves relay `j` with the correct local primary normalization

\[
U_{c,j}\asymp q_j^{-1/2-h/2}.
\tag{CG10}
\]

If it were transported to `q_{j+1}` with **no physical amplitude growth**, then relative to the required next primary amplitude it would have size

\[
\frac{U_{c,j}}{U_{\rm pkt}(q_{j+1})}
=\vartheta^{(1+h)/2}<1.
\tag{CG11}
\]

After `n` such passive transfers the normalized amplitude would decay like

\[
\vartheta^{n(1+h)/2}.
\tag{CG12}
\]

Hence passive transport cannot sustain an autonomous cascade.

The transport interval between relay levels must provide exactly the missing amplification in (CG9), modulo a uniformly bounded nonzero transfer coefficient.

## 5. Necessary transfer theorem

Let `T_{j->j+1}` denote the physical linearized transport/evolution operator carrying the designated child from the exit of relay `j` to the entrance of relay `j+1` before the next nonlinear interaction is activated.

The needed theorem has the form

\[
\boxed{
T_{j\to j+1}W_{c,j}
=
\mathfrak g_j W_{p,j+1}+R_{j+1},
}
\tag{CG13}
\]

where `W_{p,j+1}` is a correctly normalized primary packet at the next physical level, and

\[
\boxed{
0<c_*\le |\mathfrak g_j|\le C_*<\infty
}
\tag{CG14}
\]

uniformly in `j`, while

\[
\boxed{
\|R_{j+1}\|\le o(1)\|W_{p,j+1}\|.
}
\tag{CG15}
\]

In physical units, (CG13)--(CG14) are equivalent to saying that the transport produces the scale gain (CG9) automatically through the q-dependent background dynamics.

## 6. Phase/orientation obligations

Amplitude alone is insufficient. The transported child must also enter the next relay with:

1. the correct unit-beta phase normalization;
2. phase normal within the open cone required by the source packet construction;
3. the correct growing/decaying frame orientation for the next designated interaction;
4. packet width compatible with the next `S_*`-scale source envelope;
5. transverse localization compatible with a fresh sparse supernode;
6. an error remainder lying in the already-admissible `rho_{j+1}` or another strictly smaller class.

The strict action-gap and projection-margin lemmas imply that sufficiently small perturbations of these data are allowed. What is missing is a theorem showing that the **background transport map actually lands inside that open admissible set**.

## 7. New conceptual simplification

Because of (CG5), the amplitude and frequency renormalizations are not two independent requirements. Both demand the same physical q-gain

\[
\boxed{q^{-(1+h)/2}.}
\]

Thus the cross-scale problem reduces to one dynamical renormalization statement:

> does the designated child evolve along the intended background characteristic so that its WKB amplitude and its physical wave covector acquire the same q-scaling already built into the source primary packet family?

If yes, the child automatically has the correct leading physical amplitude-to-carrier ratio at the next level.

## 8. What remains open

This note proves the exact required scale law but not the dynamical transport law producing it.

The sharp next target is therefore:

\[
\boxed{
\textbf{q-transport renormalization theorem for the designated unit-beta child.}
}
\]

One must derive it directly from the source background characteristic/WKB equations, not from dyadic chart relabeling.