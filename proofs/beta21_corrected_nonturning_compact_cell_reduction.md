# Corrected non-turning beta-(2,1) compact-cell reduction

**Status:** EXACT-ENVELOPE CANDIDATE + FINITE SOURCE-ACTION REDUCTION. NOT YET A FULL CONTROLLABILITY OR EXACT `C^1` RESET-CELL THEOREM. This note uses the corrected first-relay resonance

\[
\mathcal E_{2,u}(x)+\mathcal E_{1,u}(x+\delta)
=\mathcal E_{1,u}(x-\delta)
\]

and identifies a compact non-turning `n=1` design whose strong-`H` renewal has a large causal margin, whose surviving unit-beta channel has strictly negative action at the handoff, and whose full source-promoted terminal lattice is finite. A simple reachability filter reduces the crude terminal upper bound further by enforcing principal same-phase self-interaction zero.

The remaining theorem obligation is finite-dimensional controllability of the reachable promoted graph. No complete autonomous reset cell is claimed here.

## 1. Corrected working point

Choose

\[
\boxed{u=2.5,\qquad \delta=0.1375.}
\tag{NC1}
\]

Solving the corrected exact relay resonance gives

\[
\boxed{
x
=0.77794450260672482712680064619405\ldots.}
\tag{NC2}
\]

Thus the initial slope coordinates are

\[
z_P=x,
\qquad
z_C=x+\delta
=0.9154445026067248271\ldots,
\]

\[
z_D=x-\delta
=0.6404445026067248271\ldots.
\tag{NC3}
\]

All three lie strictly inside the source auxiliary interval `(1/2,3/2)`.

The exact finite-`u` resonance is

\[
\boxed{
\mathcal E_{2,2.5}(x)
+\mathcal E_{1,2.5}(x+\delta)
-\mathcal E_{1,2.5}(x-\delta)=0.
}
\tag{NC4}
\]

Numerically,

\[
A_P=-0.14633880209035941292\ldots,
\]

\[
A_C=-0.00855661308220016015\ldots,
\]

\[
A_D=-0.15489541517255957307\ldots.
\tag{NC5}
\]

So `P-C -> D` is exactly source matched.

## 2. Strong-`H` renewal and exact slope reset

Use

\[
M=D-C,
\qquad
H=D+M=2D-C,
\qquad
P_{new}=H+D=3D-C=2D+M.
\tag{NC6}
\]

The exact strong-`H` parent-renewal equation is

\[
\boxed{
3\mathcal E_{1,u}(x-\delta+t)
+\mathcal E_{1,u}(x+\delta+t)
-\mathcal E_{2,u}(x-2\delta+t)
=0.
}
\tag{NC7}
\]

At the working point it has the causal root

\[
\boxed{
t_*
=0.22512911698286797975123849107983\ldots.}
\tag{NC8}
\]

The clock-reset section is

\[
\boxed{T=2\delta=0.275.}
\tag{NC9}
\]

Hence

\[
\boxed{T-t_*=0.04987088301713202025\ldots>0.}
\tag{NC10}
\]

The renewed beta-two packet is generated at reduced slope

\[
\boxed{
z_{P_{new}}(t_*)
=x-2\delta+t_*
=0.72807361958959280688\ldots,}
\tag{NC11}
\]

comfortably inside the source window.

At the final section,

\[
z_D(T)=x+\delta,
\qquad
z_{P_{new}}(T)=x.
\tag{NC12}
\]

Thus the outgoing pair `(P_new,D)` returns exactly to the input beta-two/beta-one slope coordinates `(x,x+delta)`.

## 3. The turning-face obstruction is absent

At the handoff,

\[
\boxed{
A_D(T)
=\mathcal E_{1,2.5}(x+\delta)
=-0.00855661308220016015\ldots<0.
}
\tag{NC13}
\]

Therefore every extra surviving `D` leaf costs a fixed negative source action. The zero-cost ladder mechanism of `beta21_turning_face_zero_cost_ladder_obstruction.md` is absent.

The spent old catalyst has

\[
z_C^{old}(T)=x+3\delta
=1.1904445026067248271\ldots
\]

and

\[
\boxed{
A_C^{old}(T)
=-0.04406251619706007055\ldots.
}
\tag{NC14}
\]

It is still larger than the renewed beta-two target action, so it cannot simply be discarded. It must be included in the terminal active control problem.

## 4. Natural-growing audit stays small

At the input, renewal and boundary sections, the naturally growing/neutral positive-defect block remains small. A representative exact-envelope enumeration gives only a handful of positive rows, all organized by the beta-zero root direction `M=D-C`.

This is useful but **not sufficient** for the handoff theorem, because a stable character forced at a source action above `A_P` remains exponentially relevant even when its homogeneous symbol is stable.

Accordingly the final audit must use source action, not only the natural-envelope defect.

## 5. Full source-action promoted set is finite

At the boundary define

\[
A_C^T=A_C^{old}(T),
\qquad
A_D^T=A_D(T),
\qquad
A_*:=A_{P_{new}}(T)=\mathcal E_{2,2.5}(x).
\]

For a character

\[
K_{m,n}=mD+nC,
\]

the maximal absolute-leaf action is

\[
\boxed{
S_{m,n}=|m|A_D^T+|n|A_C^T.
}
\tag{NC15}
\]

Since both coefficients are strictly negative, the condition

\[
S_{m,n}\ge A_*
\tag{NC16}
\]

leaves only finitely many integer pairs `(m,n)`.

Thus the terminal source-promoted lattice is finite even before polarization/reachability reduction.

For the nearby scan-optimized non-turning family, the smallest crude conjugacy-class counts occur in this same moderate-`u` region. The exact candidate (NC1) is retained because it combines source-window margin, a substantial causal renewal margin, and a manageable finite graph.

## 6. Same-phase self-zero reachability refinement

The crude bound (NC15) pretends, for example, that a pure `kD` harmonic can be built at action `kA_D`. But principal incompressibility gives

\[
D+D\to2D=0
\]

for identical same-phase packets, and similarly for repeated direct same-phase self-interactions.

A first reachability refinement therefore starts from the real seed characters

\[
\pm C,\quad\pm D,
\]

and iterates quadratic sums only between **distinct signed characters**, keeping a child only if the accumulated source action remains at least `A_*`.

This simple dynamic programme is implemented in

`experiments/beta21_corrected_nonturning_scan.py`.

It removes the most obvious pure-self-interaction overcount. The surviving promoted graph is still finite and lies in a narrow strip of small catalyst multiplicity rather than filling a two-dimensional lattice.

This dynamic programme is conservative: it does not yet test every actual Leray polarization coefficient. Hence it is a finite **upper graph for the true reachable promoted block**, not a proof that every retained edge is populated.

## 7. Structural form of the terminal graph

Two principal families are unavoidable whenever old `C` coexists with `D`:

### Sum ladder

\[
C
\to C+D
\to C+2D
\to\cdots.
\tag{NC17}
\]

### Difference/root ladder

\[
C
\to M=D-C
\to D+M
\to D+2M
\to\cdots.
\tag{NC18}
\]

Additional finite merger branches arise when these two families interact. Because every additional `C` or `D` leaf carries a fixed negative action, the merger depth above `A_*` is finite.

This is the correct terminal active-control object. It replaces the false idea that only the scalar old-`C` coordinate had to be cancelled.

## 8. What is closed and what remains

Closed here:

1. corrected non-turning exact first resonance;
2. exact strong-`H` renewal root;
3. exact phase-slope return `(P_new,D) -> (x,x+delta)`;
4. strict negative surviving-`D` action, eliminating the infinite zero-cost ladder;
5. finiteness of the **full source-action promoted** terminal lattice;
6. a reproducible reachability upper graph after same-phase self-zero filtering.

Not yet closed:

\[
\boxed{
\textbf{finite-dimensional controllability of the full reachable terminal graph.}
}
\tag{NC19}
\]

The next theorem must either:

- prove PBH/structural controllability of the finite sum/root/merger graph using translated same-character parent controls; or
- find a further support/action reduction that removes the merger branches before the final control solve.

Only after that rank theorem should the exact action-normalized `C^1` zero-residual transfer be repeated.

No full reset-cell or unforced Navier--Stokes blowup theorem is claimed.
