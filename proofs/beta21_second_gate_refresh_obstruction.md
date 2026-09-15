# Second-gate transported-`P` refresh obstruction

**Status:** PROVED EXACT-ENVELOPE / PRINCIPAL OBSTRUCTION TO A COMMON `(C,D,P)` SECOND COLLAR. The immediate sibling `P+C -> F` is not the sharpest obstruction when the old catalyst `C` remains in the second `P+D -> E` overlap. The stronger problem is that the old pair `C,D` regenerates the beta-two parent `P` at the second collar with an action **strictly above** the transported `P` action used by the ordered reset ledger. This refreshed `P` then regenerates `E` at the same larger exponential scale. Hence the original finite-`u=4` reset ledger cannot survive an uncontrolled common triple overlap.

A viable second stage must therefore do one of two things:

1. route/delay the old `C` packet so that it is absent from the second `P-D` collision window; or
2. include the refreshed `P` contribution itself in a leading active cancellation system.

The first route is the cleaner branch pursued next.

## 1. Exact second-collar data

Use the finite-`u=4` ordered point

\[
u_*=4,
\qquad
\delta=0.17554960586942932598\ldots,
\]

\[
s=0.213506242359214\ldots,
\qquad
\eta=0.005,
\qquad
t_2=s+\eta.
\]

At the second collision time,

\[
\begin{aligned}
z_C&=1+t_2
=1.218506242359214\ldots,\\
z_D&=1-2\delta+t_2
=0.867407030620355\ldots,\\
z_P&=1-\delta+t_2
=1.042956636489785\ldots.
\end{aligned}
\tag{SR1}
\]

The exact finite-`u` envelope values are

\[
\boxed{
A_C:=\mathcal E_{1,4}(z_C)
=-0.06603621737409447\ldots,
}
\tag{SR2}
\]

\[
\boxed{
A_D:=\mathcal E_{1,4}(z_D)
=-0.02407863050407955\ldots.
}
\tag{SR3}
\]

The transported beta-two packet from the first collision has action

\[
\boxed{
A_P^{tr}
=-0.10519727146343909\ldots.
}
\tag{SR4}
\]

## 2. The old parents regenerate `P`

If `C` and `D` are both physically present in the second overlap, their quadratic sum branch again has character

\[
C+D=P.
\]

Its source action at the second collar is

\[
\boxed{
A_P^{fresh}=A_C+A_D
=-0.09011484787817402\ldots.
}
\tag{SR5}

Therefore

\[
\boxed{
A_P^{fresh}-A_P^{tr}
=0.01508242358526506\ldots>0.
}
\tag{SR6}

On the source action scale `Lambda_ell ~ c S_*`, the fresh contribution exceeds the transported one by

\[
\exp\{0.0150824\ldots\,\Lambda_\ell\}.
\tag{SR7}
\]

No fixed power of `epsilon` or polynomial factor in `S_*` can compensate this at high dyadic level.

## 3. The refresh coefficient is genuinely nonzero

For the unit-beta sum interaction, the exact principal source-frame formula evaluated at `(z_C,z_D)` gives

\[
\boxed{
\kappa_{CD\to P}(t_2)
=0.4469186474144234\ldots\ne0.
}
\tag{SR8}

Thus (SR5) is not a formal character possibility. The refreshed `P` is physically generated at principal order. Source-frame and curl errors are lower order and cannot erase the fixed coefficient margin.

## 4. The intended second-generation action is also shifted

The ordered ledger uses the transported parent and defines

\[
A_E^{ledger}=A_P^{tr}+A_D.
\]

Numerically,

\[
\boxed{
A_E^{ledger}
=-0.12927590196751864\ldots.
}
\tag{SR9}

But the freshly regenerated `P` immediately combines with `D` to produce the same beta-three character

\[
E=P+D=C+2D
\]

at action

\[
\boxed{
A_E^{fresh}
=A_C+2A_D
=-0.11419347838225356\ldots.
}
\tag{SR10}

Hence

\[
\boxed{
A_E^{fresh}-A_E^{ledger}
=0.01508242358526508\ldots>0.
}
\tag{SR11}

The same exponential advantage propagates directly into the intended output channel. Therefore one cannot regard the common triple overlap as merely adding a smaller sibling correction to an otherwise unchanged reset ledger.

## 5. Consequence for the sibling `F`

The previously isolated branch

\[
P+C\to F=2C+D
\]

is still genuinely nonzero and promoted relative to its own natural beta-three envelope. However its absolute source action using the transported `P` is

\[
A_F=A_P^{tr}+A_C
=-0.17123348883753356\ldots,
\]

which is below the ledger `E` action by a fixed amount.

Thus the primary obstruction to the common triple overlap is not `F` itself but the **leading refresh of `P` and `E`** in (SR6), (SR11).

This corrects the architectural emphasis of `beta21_second_gate_immediate_sibling_obstruction.md`: that note remains valid as a nonzero sibling calculation, but the refresh obstruction is stronger.

## 6. Required redesign

The old finite-`u` ordered action reset was solved under the assumption that the `P` entering the second event is the packet transported from the first event. Equations (SR6)--(SR11) show that this assumption fails if `C,D` re-overlap there.

Therefore a clean continuation of the original reset geometry requires

\[
\boxed{
C_{old}\notin \operatorname{supp}_{overlap}(P,D)
\quad\text{during the second collision window.}
}
\tag{SR12}

The old catalyst may be reintroduced later by a separately delayed same-character subpacket for the intended third and fourth events; this adds no lattice generator. The exact support/handoff realization is a separate architectural obligation.

If (SR12) is not imposed, the second gate must actively cancel the refreshed `P` at leading scale and the entire action-reset system must be solved with that cancellation included.

## 7. New clean second-gate model

Under the delayed-`C` routing condition (SR12), the only leading designated parents in the second collision are

\[
P,\qquad D.
\]

Their quadratic interaction has two first-generation branches:

\[
P+D\to E
\]

and

\[
P-D\to \widetilde C.
\]

The difference child `\widetilde C` has the old catalyst character but is newly generated inside the second collar. It therefore cannot be removed by support routing and must be included in the second active-gate audit.

This two-input routed problem is the next theorem layer.
