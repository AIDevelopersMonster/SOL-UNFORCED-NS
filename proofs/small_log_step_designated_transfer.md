# Small-log-step designated transfer theorem

**Status:** PROVED ABSTRACT/NORMALIZED TRANSFER THEOREM UNDER THE SOURCE-SMOOTH COEFFICIENT HYPOTHESIS. This closes the nonvanishing transfer coefficient in `q_transport_renormalization_reduction.md` for a fixed physical shrink factor sufficiently close to one. A separate geometric packing/separation audit is still required before declaring an infinite relay chain.

The point is that one need not compute a special long-range WKB transfer coefficient. Because the outgoing designated child and the next incoming primary are both **unit-beta** packets in the same normalized source frame, the cross-scale transfer coefficient equals one at zero logarithmic separation. Continuous dependence of the normalized linearized flow then gives a quantitative nonzero margin for every sufficiently small fixed logarithmic q-step.

## 1. Logarithmic q variable

Let

\[
\tau:=\log(q_j/q),
\qquad q\in[q_{j+1},q_j],
\]

so that for

\[
q_{j+1}=\vartheta q_j
\]

the transfer interval has fixed length

\[
\boxed{L_\vartheta:=\log(1/\vartheta)>0.}
\tag{ST1}
\]

After the q-normalization of `q_transport_renormalization_reduction.md`, the designated polarization block obeys a finite-dimensional equation

\[
\boxed{
\partial_\tau a=A_0(\tau)a+E_j(\tau)a,
}
\tag{ST2}
\]

where the frozen normalized profile generator is bounded on the compact admissible cone,

\[
\boxed{
\|A_0(\tau)\|\le C_M,
}
\tag{ST3}
\]

and source-small perturbations satisfy

\[
\boxed{
\sup_\tau\|E_j(\tau)\|\le \eta_j,
\qquad \eta_j\to0.
}
\tag{ST4}
\]

The same form follows for the normalized phase-covector equation obtained from

\[
D_t\nabla\Phi=-(\nabla U_0)^T\nabla\Phi.
\]

## 2. Near-identity estimate

Let `U_j(tau,0)` be the fundamental matrix of (ST2). Duhamel's formula gives

\[
U_j(\tau,0)-I
=\int_0^\tau (A_0(s)+E_j(s))U_j(s,0)\,ds.
\]

Gronwall yields

\[
\|U_j(s,0)\|
\le \exp[(C_M+\eta_j)s].
\]

Therefore

\[
\boxed{
\|U_j(L_\vartheta,0)-I\|
\le
\exp[(C_M+\eta_j)L_\vartheta]-1.
}
\tag{ST5}
\]

This bound is uniform in the physical scale index `j` once the frozen design is fixed.

## 3. Canonical identification of child and next primary

The v0.8 difference relay produces a **unit-beta child**. The next relay also uses a unit-beta designated input packet before its new interaction is activated. Under the source normalized frame at zero q-separation, these are the same normalized polarization datum. Denote it by a unit vector

\[
\boxed{e_* .}
\tag{ST6}
\]

Thus the zero-step transfer coefficient is exactly

\[
\boxed{
\langle e_*^*,Ie_*\rangle=1.
}
\tag{ST7}
\]

For the finite step define

\[
\boxed{
g_{j,\vartheta}
:=\langle e_*^*,U_j(L_\vartheta,0)e_*\rangle.
}
\tag{ST8}
\]

Then (ST5) gives

\[
\boxed{
|g_{j,\vartheta}-1|
\le
\exp[(C_M+\eta_j)L_\vartheta]-1.
}
\tag{ST9}
\]

## 4. Quantitative nonvanishing

Choose once and for all `vartheta_*<1` sufficiently close to one that

\[
\boxed{
e^{2C_M\log(1/\vartheta_*)}-1<\frac14.}
\tag{ST10}
\]

For every fixed

\[
\vartheta\in(\vartheta_*,1)
\]

and all sufficiently high relay levels, `eta_j<=C_M`, so (ST9) implies

\[
\boxed{
|g_{j,\vartheta}-1|<\frac14,
\qquad
|g_{j,\vartheta}|>\frac34.
}
\tag{ST11}
\]

Hence the designated transfer coefficient is uniformly bounded away from zero:

\[
\boxed{
\frac34<|g_{j,\vartheta}|<\frac54
}
\tag{ST12}
\]

after increasing the starting level if necessary.

This proves the coefficient nondegeneracy condition that remained open in `q_transport_renormalization_reduction.md`.

## 5. Transverse leakage is small

Let `Pi_*` be the normalized projection onto the next primary direction. Then

\[
\Pi_*^\perp U_j(L_\vartheta,0)e_*
=\Pi_*^\perp(U_j-I)e_*.
\]

Thus

\[
\boxed{
\|\Pi_*^\perp U_j(L_\vartheta,0)e_*\|
\le e^{(C_M+\eta_j)L_\vartheta}-1.
}
\tag{ST13}
\]

By choosing `vartheta` still closer to one if required, this can be made smaller than any preassigned strict cone/transversality margin of the frozen relay design. The transverse component therefore belongs to the stable/admissible perturbation block.

## 6. Phase cone persistence

Let `n_*(tau)` be the normalized phase covector transported by the corresponding normalized eikonal linear equation. On the frozen compact source cone its generator is bounded by a constant `C_{phase,M}`. The same argument gives

\[
\boxed{
|n_*(L_\vartheta)-n_*(0)|
\le C'_M L_\vartheta
}
\tag{ST14}
\]

for sufficiently small `L_vartheta` (with source-small corrections absorbed into `C'_M`).

The admissible phase/beta region used by the relay construction is open and the unit-beta datum lies strictly inside it. Let `d_cone>0` be its distance to the complement in normalized phase coordinates. Choose `vartheta` so that

\[
C'_M L_\vartheta<\frac12d_{\rm cone}.
\tag{ST15}
\]

Then every transported child remains in the admissible next-primary phase cone uniformly at all sufficiently high levels.

## 7. Restoring physical amplitude and carrier

By `q_transport_renormalization_reduction.md`, restoring physical units between `q_j` and `q_{j+1}=vartheta q_j` contributes the exact common q-weight

\[
\vartheta^{-\gamma},
\qquad
\gamma=\frac{1+h}{2},
\]

to both primary packet amplitude and physical carrier.

Combining this with (ST12),

\[
\boxed{
T_{j\to j+1}W_{c,j}
=\mathfrak g_j W_{p,j+1}+R_{j+1},
\qquad
\frac34<|\mathfrak g_j|<\frac54,
}
\tag{ST16}
\]

in normalized next-scale units, while the transverse normalized remainder is bounded by

\[
\boxed{
\|R_{j+1}\|_{\rm norm}
\le C_M\log(1/\vartheta)+o_j(1).
}
\tag{ST17}
\]

For a fixed sufficiently near-one `vartheta`, this lies inside the strict stable/cone margins.

## 8. Infinite frequency growth is not lost by taking a small step

Choosing `vartheta` close to one does not destroy the cascade scaling. If

\[
q_j=q_0\vartheta^j,
\]

then

\[
q_j\to0
\]

and therefore

\[
\boxed{
\Omega_{\rm phys}(q_j)
\asymp q_j^{-\gamma}
=q_0^{-\gamma}\vartheta^{-j\gamma}\to\infty.
}
\tag{ST18}
\]

Likewise the correctly normalized primary packet amplitude grows geometrically. A near-one shrink ratio merely increases the number of relay stages needed for a prescribed total scale change; it does not change the asymptotic direction.

## 9. What this theorem closes

Under the standard source-smooth normalized coefficient hypothesis already used throughout the fixed-order packet calculus, there exists a nonempty interval

\[
\boxed{
\vartheta\in(\vartheta_*,1)
}
\]

for which the designated unit-beta child is transported to the next unit-beta primary sector with a uniformly nonzero order-one coefficient, while polarization and phase leakage remain within the frozen strict margins.

Thus the previous bottleneck

\[
\boxed{g_\vartheta^{(0)}\ne0}
\]

is closed without a special resonance computation: it follows from near-identity transfer over a sufficiently small fixed logarithmic q-step.

## 10. Remaining global obstruction

This does **not** yet prove an infinite autonomous Navier--Stokes relay chain. The next obligation is geometric and combinatorial rather than WKB-amplitude based:

> Can infinitely many exact local relay collars with a fixed near-one scale ratio be placed along the intended q-characteristic so that their nonlinear interaction windows are separated/controlled, their source supernodes remain admissible, and the sum of all local corrections gives smooth finite-energy data before the accumulation time?

That **relay-collar packing and global assembly theorem** is now the sharp frontier.
