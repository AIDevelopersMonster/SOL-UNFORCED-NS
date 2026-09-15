# `u_*=6` active-reset redesign audit for the beta-(2,1) cell

**Status:** COMPUTER-ASSISTED EXACT-ENVELOPE / FROZEN PRINCIPAL DESIGN AUDIT. The strong-`H` renewal bifurcation suggests moving the active reset cell above the old passive-cleanup threshold. This note audits the concrete candidate

\[
\boxed{u_*=6.}
\]

The conclusion is encouraging but not yet a full reset theorem:

1. the exact turning-point resonance has a unique working root `delta≈0.16869747`;
2. the strong-`H` final renewal has a causal root with margin about `9.0e-4` before the reset face;
3. the first active gate has only five positive-defect unwanted modes, all in one beta-zero root family;
4. the second active section has nine positive-defect unwanted modes, again all in that same root family;
5. a single eleven-state root chain spans the second dangerous block;
6. every mandatory frozen principal edge in that chain is nonzero by a large margin;
7. the relevant full-symbol rates remain pairwise separated.

Thus crossing the passive-cleanup threshold enlarges the finite control blocks but does not destroy their root-family architecture.

The first three exact `C^1` gate theorems proved at `u=4` still require re-instantiation at `u=6`; this note supplies the finite algebra/action data needed for that transfer.

## 1. Exact turning-point data

Solve

\[
\mathcal E_{2,6}(1-\delta)
=\mathcal E_{1,6}(1-2\delta).
\]

The exact-envelope root is

\[
\boxed{
\delta_6
=0.1686974699091436\ldots,
}
\tag{U6A1}
\]

so

\[
\boxed{
x_6=0.8313025300908564\ldots,}
\tag{U6A2}
\]

and

\[
\boxed{
T_6=2\delta_6
=0.3373949398182873\ldots.
}
\tag{U6A3}

The old passive cleanup defect is positive at this working point:

\[
\Delta_{clean}(6)
\approx+5.22782435\times10^{-4}.
\]

This is no longer treated as a failure because the active architecture retains and controls the old parents instead of discarding `C` passively.

## 2. Strong-`H` final renewal root

The strong-root final equation

\[
F_6(t)
=\mathcal E_{1,6}(1+t)
+3\mathcal E_{1,6}(1-2\delta_6+t)
-\mathcal E_{2,6}(1-3\delta_6+t)
=0
\]

has the causal root

\[
\boxed{
t_{renew}\approx0.336494599305936.}
\tag{U6A4}

Hence

\[
\boxed{
T_6-t_{renew}
\approx9.00340512\times10^{-4}>0.
}
\tag{U6A5}

This is almost an order of magnitude larger than the conservative `1e-4` active-collar widths used in the local gate audits.

## 3. Candidate early timing

For comparison with the old ordered ledger, retaining the nominal spacing

\[
\eta=0.005
\]

gives the exact ordered-action root

\[
\boxed{
s_{ord,6}\approx0.204667379954882,}
\tag{U6A6}

so the old second-event location would be

\[
\boxed{
t_{2,6}=s_{ord,6}+0.005
\approx0.209667379954882.}
\tag{U6A7}

This timing is used only as a concrete second-section audit point. The final active redesign is not required to preserve the old four-event ledger.

## 4. First-section full critical audit

At the first local section use

\[
z_C=1,
\qquad
z_D=1-2\delta_6.
\]

Then

\[
A_C=0,
\qquad
A_D=-0.167155231065458\ldots.
\]

At `u=6`, positive-beta turning points exist up to beta `15`. The exact enumeration contains

\[
\boxed{108}
\]

naturally-critical positive-beta characters before conjugate identification.

Despite that larger natural set, only **five** unwanted modes have positive absolute-leaf defect:

\[
\boxed{
2D-C,
\quad3D-2C,
\quad4D-3C,
\quad5D-3C,
\quad6D-4C.
}
\tag{U6A8}

Their defects are approximately

\[
\begin{array}{c|r}
2D-C&+0.4089480095\\
3D-2C&+1.5710247927\\
4D-3C&+0.0131762481\\
5D-3C&+0.0016071234\\
6D-4C&+0.5787445241
\end{array}
\tag{U6A9}

The closest uncontrolled negative mode is already separated by about

\[
-0.2254.
\]

Thus the first-section finite block has a comfortable uncontrolled margin.

## 5. First-section root factorization

Set

\[
M=D-C.
\]

Then the five positive-defect modes become

\[
D+M,
\quad D+2M,
\quad D+3M,
\quad2D+3M,
\quad2D+4M.
\tag{U6A10}

A sufficient six-state root chain is

\[
\boxed{
M
\to D+M
\to D+2M
\to D+3M
\to2D+3M
\to2D+4M.
}
\tag{U6A11}

The mandatory frozen principal coefficients at `u=6` are approximately

\[
\begin{array}{c|r}
D+M&-27.2107\\
(D+M)+M&-24.7052\\
(D+2M)+M&-3.73066\\
(D+3M)+D&+13.1333\\
(2D+3M)+M&-32.4342
\end{array}
\tag{U6A12}

and are all fixed distances from zero.

Appending the desired first output

\[
P=C+D
\]

gives a seven-state sufficient first-gate block. Its diagnostic full-symbol rates are pairwise distinct; the smallest separation is approximately

\[
\boxed{1.34\times10^{-2}>0.}
\tag{U6A13}

Thus the same common-input PBH/direct-sum architecture used at `u=4` has a nondegenerate `u=6` analogue, now with a six-state root branch.

## 6. Second-section full critical audit

At the concrete second point (U6A7),

\[
z_C=1.209667379954882\ldots,
\]

\[
z_D=0.872272440136595\ldots,
\]

with natural actions

\[
\boxed{
A_C=-0.0637690500348631\ldots,
}
\tag{U6A14}

\[
\boxed{
A_D=-0.0235231576803986\ldots.
}
\tag{U6A15}

The naturally-critical enumeration contains

\[
\boxed{109}
\]

positive-beta characters. Exactly **nine** unwanted characters have positive leaf-action defect:

\[
\boxed{
2D-C,
\quad3D-2C,
\quad4D-3C,
\quad5D-4C,
\quad6D-4C,
\quad7D-5C,
\quad8D-6C,
\quad10D-7C,
\quad11D-8C.
}
\tag{U6A16}

The defects are approximately

\[
\begin{array}{c|r}
5D-4C&+0.04554\\
10D-7C&+0.19941\\
2D-C&+0.21498\\
6D-4C&+0.28185\\
8D-6C&+0.33785\\
11D-8C&+0.42288\\
3D-2C&+0.94856\\
7D-5C&+1.00115\\
4D-3C&+1.10122
\end{array}
\tag{U6A17}

The closest uncontrolled negative mode is

\[
4D? \text{ no: } (B,m,n)=(4,14,-10)=14D-10C
\]

with defect approximately

\[
\boxed{-0.00554359.}
\tag{U6A18}

Although narrower than at `u=4`, this is still a fixed nonzero margin. A short fixed active collar such as `1e-4` moves the margin farther negative in the direct exact-envelope check.

## 7. Eleven-state second-gate root chain

All nine positive-defect modes in (U6A16) lie in the single family generated by `M=D-C`.

A sufficient chain is

\[
\boxed{
\begin{aligned}
M
&\to D+M
\to D+2M
\to D+3M
\to D+4M\\
&\to2D+4M
\to2D+5M
\to2D+6M\\
&\to3D+6M
\to3D+7M
\to3D+8M.
\end{aligned}
}
\tag{U6A19}

The dangerous modes occur among these chain states; intermediate states are retained for triangular controllability.

The mandatory mean-wave coefficients at the frozen second geometry are approximately

\[
-27.1390,
-40.5123,
-11.0206,
-5.28645,
-48.4402,
-19.5585,
-15.7555,
-66.2631,
-48.0767,
\]

and the two required wave-wave `+D` edges are approximately

\[
+22.1518,
\qquad
+14.4040.
\tag{U6A20}

Every mandatory edge is therefore nonzero with a large margin.

## 8. Full-symbol separation at the second section

Append the refreshed designated branch

\[
P=C+D,
\qquad E=C+2D.
\]

The diagnostic rates are

\[
\lambda_P\approx-0.5530033,
\qquad
\lambda_E\approx-1.2691056,
\qquad
\lambda_M\approx-0.0182086,
\]

with root descendant rates approximately

\[
0.2473,
0.6343,
0.7583,
0.2888,
0.6022,
0.9671,
0.7356,
0.5488,
0.8404,
0.9456.
\]

The smallest pairwise separation in this sufficient thirteen-state block is approximately

\[
\boxed{2.15\times10^{-2}>0.}
\tag{U6A21}

Thus the common-input exponential/PBH response remains nondegenerate after extending the root chain.

## 9. Programme consequence

The supercritical candidate `u=6` simultaneously exhibits

- a causal strong-`H` final renewal root;
- finite first/second positive-defect blocks;
- one common beta-zero root organization;
- nonzero mandatory polarization coefficients;
- nonzero full-symbol spectral separations.

This makes `u=6` a substantially better candidate for the **full active reset cell** than the old passive-cleanup point `u=4`.

The next mandatory steps are now sharply defined:

1. promote the seven-state first-gate frozen rank to an exact `C^1` gate at `u=6`;
2. promote the thirteen-state second-gate frozen rank to an exact `C^1` gate at `u=6`;
3. repeat the immediate third-gate terminal-`Q` generic-transversality argument at `u=6`;
4. build the fourth strong-root-`H` gate rather than the weaker nominal `Q-C` gate;
5. concatenate to the final renewal time (U6A4).

No full reset-cell theorem is claimed in this audit.
