# Passive five-collar recursion obstruction for the beta-(2,1) reset cell

**Status:** PROVED PRINCIPAL/LOCAL-DUHAMEL OBSTRUCTION TO A PURELY PASSIVE FIVE-COLLAR ROUTING THEOREM. The moving/translated-collar repair proposed after `support_gating_requires_generation_delays.md` is not sufficient if each collision collar is only a passive open overlap of its two input packets. In an open overlap the Navier--Stokes quadratic nonlinearity does not wait for the next designated collar: newly generated output is immediately available for further quadratic interaction with the inputs that are still present.

The conclusion is deliberately scoped. It does **not** rule out a multi-collar reset cell with active exit cancellation, additional control packets, a genuinely independent phase bank, or another mechanism that annihilates forbidden exit traces. It proves that translations and support declarations alone cannot supply the missing genealogy gate.

## 1. Working reset genealogy

Use the corrected beta-(2,1) character chain

\[
C+D\to P,
\qquad
P+D\to E,
\qquad
E-C\to Q,
\qquad
Q-C\to H,
\qquad
H+D\to P_{\rm new},
\tag{PF1}
\]

with

\[
D=P-C,
\qquad
E=C+2D,
\qquad
Q=2D,
\qquad
H=2D-C,
\qquad
P_{\rm new}=H+D.
\tag{PF2}
\]

The ordered reduced construction in `beta21_ordered_microcollar_unfolding.md` proves that the desired events can be assigned distinct times

\[
t_1<t_2<t_3<t_4<T
\tag{PF3}
\]

while preserving the exact reduced reset equations. The later obstruction `support_gating_requires_generation_delays.md` proves that allowing the entire late genealogy to coexist in one common overlap collar creates a premature `H` with supercritical reset-face action.

The question here is sharper: can one repair that failure merely by replacing the common supernode by five passive translated collision collars?

## 2. Local collision collar and projected principal equations

Consider the first late collision collar, intended only to realize

\[
C+D\to P.
\tag{PF4}
\]

Let `tau` be a local forward coordinate measured from an entrance section on which the newly generated downstream components are zero. On a nonempty open subcollar suppose the incoming `C` and `D` packet amplitudes are nonzero. Write their entrance values as

\[
C(0)=c\ne0,
\qquad
D(0)=d\ne0.
\tag{PF5}
\]

Project the quadratic equation onto the principal growing components of the characters in (PF1). The rooted chain contains the triangular subsystem

\[
\partial_\tau P
=\kappa_1 CD+\mathcal R_P,
\tag{PF6}
\]

\[
\partial_\tau E
=\kappa_2 PD+\mathcal R_E,
\tag{PF7}
\]

\[
\partial_\tau Q
=\kappa_3 E\overline C+\mathcal R_Q,
\tag{PF8}
\]

\[
\partial_\tau H
=\kappa_4 Q\overline C+\mathcal R_H.
\tag{PF9}
\]

Here the bar denotes the conjugate phase used by a difference interaction. The remainders collect the other projected branches, slow coefficient variation, and higher corrections; they do not alter the fact that the displayed rooted Duhamel tree is present whenever the corresponding four principal interaction coefficients are nonzero.

For the `u_*=4` cleanup geometry those coefficients were evaluated in `support_gating_requires_generation_delays.md` and are all separated from zero:

\[
\kappa_1\approx0.5472,
\quad
\kappa_2\approx0.8959,
\quad
\kappa_3\approx-4.6347,
\quad
\kappa_4\approx-8.4223.
\tag{PF10}
\]

Thus the rooted tree from `C,D` to `H` is not killed by the principal Leray/polarization algebra.

## 3. Iterated Duhamel term inside one open collar

Freeze the entrance amplitudes in the leading Taylor coefficient,

\[
C(\tau)=c+O(\tau),
\qquad
D(\tau)=d+O(\tau).
\tag{PF11}
\]

The displayed triangular tree contributes successively

\[
P(\tau)
=\kappa_1cd\,\tau+O(\tau^2),
\tag{PF12}
\]

\[
E(\tau)
=\frac{\kappa_1\kappa_2}{2}
cd^2\,\tau^2+O(\tau^3),
\tag{PF13}
\]

\[
Q(\tau)
=\frac{\kappa_1\kappa_2\kappa_3}{6}
|c|^2d^2\,\tau^3+O(\tau^4),
\tag{PF14}
\]

and

\[
\boxed{
H(\tau)
\supset
\frac{\kappa_1\kappa_2\kappa_3\kappa_4}{24}
|c|^2\overline c\,d^2\,\tau^4.
}
\tag{PF15}
\]

The symbol `\supset` is intentional: (PF15) isolates one explicit rooted-tree contribution in the full Duhamel expansion. At the working geometry its coefficient is nonzero by (PF10). Therefore passive support overlap does not make the forbidden `H` contribution identically zero.

This is the local version of the collapsed genealogy found in `support_gating_requires_generation_delays.md`. The important point is causal: generation of `P` at an interior point of the overlap does not move `P` to the next collar before the PDE can use it. On every later instant of the same open overlap, `P` is already part of the solution and can interact with `D`; the same statement then applies recursively to `E` and `Q`.

## 4. Why translating the later collars does not remove the term

Suppose one declares five disjoint future event collars

\[
\mathcal C_1,\dots,\mathcal C_5
\tag{PF16}
\]

and arranges by the auxiliary-torus translation lemma that the intended operands meet at their designated centers. Such translations determine where the **prescribed incoming packet supports** meet. They do not project the solution after a collision.

Inside `C_1`, the generated support satisfies schematically

\[
\operatorname{supp}P
\subset
\operatorname{supp}C\cap\operatorname{supp}D.
\tag{PF17}
\]

Consequently, on the interior portion where generation occurs,

\[
\operatorname{supp}P\cap\operatorname{supp}D\ne\varnothing.
\tag{PF18}
\]

The generated `E` is then supported in the same collision region, and because `C` is also present there, the difference descendants `Q` and `H` have nonempty local generation support as well. Moving `C_2,...,C_5` cannot retroactively erase this already generated contribution.

Using separate future copies of the same character does not change this argument. A copy of `C` used to create `P` remains an admissible quadratic partner for descendants created while that copy is still nonzero. The PDE sees fields, not the intended routing labels.

Hence

\[
\boxed{
\text{passive translated support geometry alone does not implement a one-edge collision gate.}
}
\tag{PF19}
\]

## 5. The obstruction survives algebraic shrinking of the collar

One might try to make `C_1` very narrow. If its normalized width is `omega_ell`, the explicit tree (PF15) pays four time integrations and hence an additional factor of order

\[
\omega_\ell^4
\tag{PF20}
\]

relative to the fixed incoming amplitudes, before the usual source normalization factors.

The premature-`H` audit at `u=4` gives a positive reset-face action advantage of fixed size: the early `H` has

\[
A_H^{\rm early}(T)\approx0.2340425089,
\tag{PF21}
\]

whereas the intended renewed beta-two parent has

\[
\mathcal E_{2,4}(x)\approx-0.1713153639.
\tag{PF22}
\]

Thus the action advantage is approximately

\[
0.4053578728>0.
\tag{PF23}
\]

on the source action scale. As already proved in `support_gating_requires_generation_delays.md`, this produces an `exp(cS_*)` advantage, while every fixed polynomial loss and every fixed positive power of the source `epsilon` contributes only `exp(-O(ell))`.

Therefore any collar-width strategy whose extra smallness is only algebraic in `S_*` and/or a fixed power of `epsilon` cannot repair the leakage asymptotically. An exponentially shrinking collision window is a different architecture and would require a new localization/derivative audit; it is not supplied by the existing translated-rectangle theorem.

## 6. Polarization zeros cannot by themselves gate every stage

A tempting active repair is to tune the next unwanted interaction coefficient to zero. The principal audit gives an important asymmetry.

For a difference interaction with positive slopes and unequal inputs, formula (PA6) of `beta21_microcascade_polarization_audit.md` has a strictly positive bracket, so

\[
\boxed{
s_1\ne s_2
\Longrightarrow
A_-^+\ne0.
}
\tag{PF24}
\]

The edges

\[
E-C\to Q,
\qquad
Q-C\to H
\tag{PF25}
\]

are consecutive difference interactions and the working reset requires unequal slopes. Hence, once an `E-C` collar produces `Q` while the same `C` copy is still present, the next difference edge `Q-C->H` has no principal polarization-zero gate available in this positive-slope geometry.

Sum edges can in principle have a cancellation in their growing coefficient, so a polarization zero may still be useful at selected stages. But it cannot furnish a complete passive/one-parameter genealogy breaker for the whole reset chain.

## 7. What a viable multi-collar theorem must add

The five-collar program therefore needs an **active exit condition**. At least one of the following additional mechanisms must be proved:

1. **collar-exit cancellation:** add localized control packets and impose that the forbidden generated traces vanish at the collar exit while the designated output remains nonzero;
2. **independent phase bank:** route the desired output into a genuinely new packet bank whose local collision algebra does not retain the old catalyst needed for the shortcut genealogy;
3. **new interaction geometry:** replace the beta-(2,1) chain by a geometry with a structural zero or stable gap on every immediate shortcut edge;
4. **non-algebraically thin gate:** introduce a level-dependent localization mechanism strong enough to beat the positive action advantage and separately prove that the resulting derivative costs remain source-admissible.

The existing abstract theorem `multicollar_finite_critical_transversality.md` suggests a concrete version of option 1: treat the designated output together with a finite list of forbidden exit traces as a finite-dimensional control map, then prove the actual source-specific sampling/kernel matrix has full rank. That rank statement is **not yet proved** for the beta-(2,1) reset cell.

## 8. New sharp frontier

The old frontier

\[
\text{construct five translated collision collars}
\]

is therefore replaced by the stronger and more precise target

\[
\boxed{
\textbf{construct one actively gated collision collar with exact forbidden-trace cancellation.}
}
\tag{PF26}
\]

A successful one-collar gate must prove, in the exact phase-adapted source variables, that

\[
(C,D)_{\rm in}
\longmapsto
P_{\rm out}\ne0,
\qquad
(E,Q,H,\ldots)_{\rm out}=0
\tag{PF27}
\]

for the finite principal critical set (with the stable complement slaved by the existing contraction), and that the Jacobian with respect to the chosen localized controls is uniformly invertible at sufficiently high levels.

Only after such a gate is available should it be concatenated into the ordered five-event reset circuit and the multi-collar zero-residual fixed point be revisited.

## 9. Consequence for the global claim

The current branch still proves a single-relay exact local closure candidate and substantial source/principal inheritance geometry, but it does **not** prove an autonomous infinite relay chain or finite-time blowup for unforced 3D Navier--Stokes. The newly isolated obstruction is narrower than before: the missing object is no longer merely a translated support layout, but an exact finite-dimensional **genealogy-breaking exit map** compatible with the Navier--Stokes correction problem.
