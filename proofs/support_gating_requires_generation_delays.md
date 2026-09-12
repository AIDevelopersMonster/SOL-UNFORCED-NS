# Passive support gating is insufficient for the beta-(2,1) cleanup cell

**Status:** PROVED PRINCIPAL/EXACT-ENVELOPE OBSTRUCTION TO A SINGLE-OVERLAP-COLLAR ROUTING IMPLEMENTATION. The moderate-`u_*` cleanup architecture cannot be made safe merely by declaring that only the intended channels are propagated from one cell to the next. If the full late genealogy is allowed to coexist in one common overlap region, the Navier--Stokes quadratic nonlinearity immediately generates the downstream chain inside that same collar. In particular a premature beta-one `H` mode is produced with positive reset-face action and therefore cannot be discarded by any fixed algebraic/epsilon smallness.

This does **not** rule out a support-gated circuit with genuinely separated generation windows. It proves that generation-time localization must be part of the construction: the intended chain must be realized as a directed sequence of narrow overlap collars, not as one static supernode containing all input/output supports.

The numerical certificate is `experiments/beta21_premature_H_leakage.py`.

## 1. Finite-`u` cleanup gauge

Work on the exact finite-`u` turning-point cleanup branch of `beta21_finite_u_cleanup_window.md`:

\[
x+\delta=1,
\tag{SG1}
\]

and

\[
\boxed{
\mathcal E_{2,u}(x)=\mathcal E_{1,u}(1-2\delta).
}
\tag{SG2}
\]

Thus at the first relay section the surviving unit-beta phases have slopes

\[
\boxed{
z_C=1,
\qquad
z_D=1-2\delta.
}
\tag{SG3}
\]

The reset face is

\[
T=2\delta.
\tag{SG4}
\]

At that face the designated renewed catalyst `D` reaches its turning point:

\[
z_D(T)=1.
\tag{SG5}
\]

## 2. The late character chain can collapse into the first overlap collar

The intended ordered genealogy is

\[
C+D\to P,
\]

\[
P+D\to E,
\]

\[
E-C\to Q,
\]

\[
Q-C\to H,
\]

\[
H+D\to P_{new}.
\tag{SG6}
\]

If all newly generated harmonics remain supported in the same common auxiliary overlap collar, then the first four interactions in (SG6) are not forced to wait for the later designed microtimes. The quadratic equation recursively feeds each newly created output into the next interaction at the same physical location.

At the common first section the character identities are

\[
P=C+D,
\qquad
E=P+D=C+2D,
\]

\[
Q=E-C=2D,
\qquad
\boxed{H=Q-C=2D-C.}
\tag{SG7}
\]

The signed beta of `H` is one. Its first-section reduced slope is therefore

\[
\boxed{
z_H(0)=2z_D-z_C=1-4\delta.
}
\tag{SG8}
\]

Since all beta-one phases acquire the same additive reduced drift, at the reset face

\[
\boxed{
z_H(T)=z_H(0)+2\delta=1-2\delta=z_D(0).}
\tag{SG9}
\]

So the premature `H` does not leave the growing window: it lands exactly at the original child slope by the reset time.

## 3. Premature `H` action

Let

\[
A:=\mathcal E_{1,u}(1-2\delta).
\tag{SG10}
\]

By the relay resonance (SG2),

\[
A=\mathcal E_{2,u}(x)<0.
\tag{SG11}
\]

The immediate chain in (SG7) gives, at the first section,

\[
A_P=A_C+A_D=0+A=A,
\]

\[
A_E=A_P+A_D=2A,
\]

\[
A_Q=A_E+A_C=2A,
\]

and hence

\[
\boxed{A_H(0)=A_Q+A_C=2A.}
\tag{SG12}
\]

Equivalently, if one counts the direct monomial genealogy, `H=2D-C` is cubic and carries the same exponent because `A_C=0` at the turning point.

Homogeneous propagation of `H` from slope `1-4delta` to slope `1-2delta` adds

\[
\mathcal E_{1,u}(1-2\delta)-\mathcal E_{1,u}(1-4\delta).
\]

Therefore

\[
\boxed{
A_H^{early}(T)
=3A-\mathcal E_{1,u}(1-4\delta).
}
\tag{SG13}
\]

The companion script evaluates this exact finite-`u` expression.

## 4. The leakage is exponentially supercritical

On the entire computed cleanup branch where the nontrivial root exists and the spent-catalyst cleanup is negative, `A_H^{early}(T)` is positive. Representative values are

\[
\begin{array}{c|c|c}
u & \delta & A_H^{early}(T)\\ \hline
1.62 & 0.2450002 & 0.15160\\
1.80 & 0.2279475 & 0.17304\\
2.00 & 0.2147614 & 0.18896\\
2.50 & 0.1954355 & 0.21148\\
3.00 & 0.1853395 & 0.22298\\
3.50 & 0.1793745 & 0.22972\\
4.00 & 0.1755496 & 0.23404\\
4.50 & 0.1729477 & 0.23698\\
4.90 & 0.1714214 & 0.23871
\end{array}
\tag{SG14}
\]

For the source-safe working point `u=4`,

\[
\boxed{
A_H^{early}(T)\approx0.2340425089>0.
}
\tag{SG15}
\]

The intended renewed beta-two parent has

\[
\mathcal E_{2,4}(x)
\approx-0.1713153639.
\tag{SG16}
\]

Thus the premature beta-one leakage sits above the intended parent by

\[
\boxed{
A_H^{early}(T)-\mathcal E_{2,4}(x)
\approx0.4053578728.
}
\tag{SG17}
\]

On the source action scale `Lambda_ell~L_s/u_*~cS_*`, this corresponds to an exponential factor

\[
\exp(cS_*)
\]

relative to the intended packet normalization.

Any fixed polynomial or fixed positive power of `epsilon` coming from the fact that `H` first appears at higher nonlinear order is only

\[
\exp(-O(\ell)),
\]

whereas the action advantage is

\[
\exp(+c\ell^2).
\]

Therefore fixed-order nonlinear smallness **cannot** suppress this premature `H` at high dyadic levels.

## 5. The required edges are genuinely nonzero

This is not an artifact of a vanishing quadratic coefficient. At `u=4` and the cleanup geometry, the principal growing projections for the collapsed chain are nonzero:

\[
C+D\to P:\quad 0.5472\ldots,
\]

\[
P+D\to E:\quad 0.8959\ldots,
\]

\[
E-C\to Q:\quad -4.6347\ldots,
\]

\[
Q-C\to H:\quad -8.4223\ldots.
\tag{SG18}
\]

Hence the quadratic algebra does populate the entire premature path at principal level.

The source-frame `O(S_*^{-1})` perturbations cannot remove these fixed nonzero margins for sufficiently large level.

## 6. Why static auxiliary support separation does not repair this

`translated_async_overlap.md` proves that one may prescribe a finite family of translated rectangles and keep distinct supernodes disjoint. That lemma is sufficient for deciding **which independent input labels meet**.

It does not provide a mechanism that makes a nonlinear output disappear from the physical region in which it was generated. Once `P` is created on the common support of `C` and `D`, the PDE solution contains `P` there; therefore `P` can immediately interact with `D`. The same statement then applies recursively to `E` and `Q`.

Consequently a single static supernode containing `C` and `D` cannot implement the intended causal graph merely by assigning different future output centers after the fact.

The source's finite-color separation is a separation of **prescribed label supports**. It is not a projection that deletes correction harmonics generated by the nonlinear equation.

## 7. Necessary redesign: generation-delayed routing

A viable support-gated cell must impose a stronger architecture.

There must be genuinely separated physical/auxiliary overlap windows

\[
\mathcal C_1,\mathcal C_2,\mathcal C_3,\mathcal C_4,\mathcal C_5
\]

such that, schematically,

\[
C\cap D\ne\varnothing\quad\text{only on }\mathcal C_1,
\]

then the transported `P` meets `D` on `C_2` but is separated from the catalyst configuration that would prematurely form the later descendants, and so on.

The crucial requirement is not merely

\[
\text{different collar centers},
\]

but

\[
\boxed{
\text{the output of event }j
\text{ must be transported into event }j+1
\text{ only after leaving the support geometry that would realize event }j+2.
}
\tag{SG19}
\]

In other words the interaction graph must be **causal in physical support**, not just causal in an action ledger.

## 8. Consequence for the research frontier

The following route is now ruled out:

\[
\boxed{
\text{one common finite supernode}
+\text{post hoc output selection}
+\text{cleanup at the reset face}.
}
\tag{SG20}
\]

The cleanup theorem remains useful, because it suppresses the spent old catalyst once a correctly routed cell reaches its reset section. But cleanup cannot substitute for generation-time gating.

The next precise problem is therefore:

\[
\boxed{
\textbf{construct a moving/translated five-collar support circuit}
}
\]

inside the source auxiliary-torus geometry and prove that each desired mode is present at its next collar while every non-designated growing combination that would shortcut the chain has zero overlap there (or is already action-subcritical).

Only after that support circuit is proved should the multi-collar zero-residual fixed point be revisited for the `u=4` cleanup cell.
