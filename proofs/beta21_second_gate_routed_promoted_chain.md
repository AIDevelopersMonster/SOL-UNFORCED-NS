# Routed second-gate promoted chain at finite `u_*=4`

**Status:** COMPUTER-ASSISTED EXACT-ENVELOPE ENUMERATION / FINITE PROMOTED CHAIN IDENTIFIED. After imposing the clean routing condition that the old catalyst `C_old` is absent from the second `P-D` overlap, the intended second event

\[
P+D\to E
\]

still has an unavoidable difference branch

\[
P-D\to C_{new}.
\]

The new unit-beta child is itself strongly promoted relative to its natural envelope. While it is present inside the collision collar it can combine repeatedly with the surviving unit-beta `D`, producing the chain

\[
C_{new}
\to P_2
\to E_2
\to G_4
\to G_5
\to G_6
\to G_7
\to G_8,
\]

where

\[
G_\beta=C+(\beta-1)D.
\]

Every beta `2,...,8` member is promoted above its exact finite-`u` natural envelope. At beta `9` the real turning point ceases to exist, so the chain enters the uniformly forward-stable high-beta sector. Thus the routed second-gate obstruction is **finite**, but it is not a two-row `(E,C_new)` problem.

This note identifies the finite chain and the required next control architecture. It does not yet prove the final second-gate response rank.

## 1. Routed second-collar inputs

Assume the old catalyst has been support-delayed away from the second collision:

\[
C_{old}\notin I_2.
\tag{SGR1}
\]

The leading input packets are therefore

\[
P,\qquad D.
\tag{SGR2}
\]

At the finite-`u=4` ordered working point,

\[
z_D=0.867407030620355\ldots,
\qquad
z_P=1.042956636489785\ldots,
\tag{SGR3}
\]

with actions

\[
A_D=-0.02407863050407955\ldots,
\tag{SGR4}
\]

\[
A_P=-0.10519727146343909\ldots.
\tag{SGR5}
\]

The intended sum output has

\[
E=P+D,
\qquad
A_E=A_P+A_D
=-0.12927590196751864\ldots.
\tag{SGR6}
\]

## 2. Unavoidable difference child

The same pair has the difference character

\[
\boxed{C_{new}=P-D=C.}
\tag{SGR7}
\]

The exact principal difference-interaction coefficient is

\[
\boxed{
\kappa_{P-D\to C_{new}}
=1.7193870146980885\ldots\ne0.
}
\tag{SGR8}
\]

The generated action is the same source-product action

\[
\boxed{
A_{C_{new}}=A_P+A_D
=-0.12927590196751864\ldots.
}
\tag{SGR9}
\]

Its character slope is exactly the old catalyst slope

\[
z_{C_{new}}=2z_P-z_D
=1.218506242359214\ldots.
\tag{SGR10}
\]

The natural unit-beta envelope there is

\[
\mathcal E_{1,4}(z_{C_{new}})
=-0.06603621737409447\ldots.
\tag{SGR11}
\]

Hence

\[
\boxed{
A_{C_{new}}-
\mathcal E_{1,4}(z_{C_{new}})
=-0.06323968459342416\ldots.
}
\tag{SGR12}
\]

Thus `C_new` is below the unit-beta natural envelope in absolute action. Nevertheless it is a leading first-generation trace produced at exactly the same source order as the desired `E`, so it cannot simply be ignored when constructing a clean output gate. In particular, while present inside the collar it generates promoted higher-beta descendants.

## 3. Repeated `D` attachment chain

Define

\[
G_\beta:=C_{new}+(\beta-1)D,
\qquad \beta\ge1.
\tag{SGR13}
\]

Thus

\[
G_1=C_{new},
\quad
G_2=P_2,
\quad
G_3=E_2,
\tag{SGR14}
\]

and for `beta>=4` these are new characters.

The source-product action is

\[
\boxed{
A_{G_\beta}
=A_{C_{new}}+(\beta-1)A_D.
}
\tag{SGR15}
\]

The beta-normalized slope is

\[
\boxed{
z_{G_\beta}
=
\frac{z_{C_{new}}+(\beta-1)z_D}{\beta}.
}
\tag{SGR16}
\]

## 4. Exact finite-u enumeration

Using the exact envelope `E_{beta,4}`, one obtains

\[
\begin{array}{c|c|c|c|c}
\beta & z_{G_\beta} & A_{G_\beta}
&\mathcal E_{\beta,4}(z_{G_\beta})
&A_G-\mathcal E\\ \hline
1&1.21850624&-0.12927590&-0.06603622&-0.06323968\\
2&1.04295664&-0.15335453&-0.69318179&+0.53982725\\
3&0.98444010&-0.17743316&-1.91174963&+1.73431647\\
4&0.95518183&-0.20151179&-3.68029024&+3.47877845\\
5&0.93762687&-0.22559042&-5.98330628&+5.75771586\\
6&0.92592357&-0.24966905&-8.81560863&+8.56593958\\
7&0.91756406&-0.27374768&-12.17806389&+11.90431620\\
8&0.91129443&-0.29782632&-16.07939907&+15.78157275
\end{array}
\tag{SGR17}
\]

Thus

\[
\boxed{
G_2,G_3,G_4,G_5,G_6,G_7,G_8
}
\tag{SGR18}
\]

are all promoted above their exact natural envelopes.

The growth of the positive defect is not a numerical accident: the source action loses only the fixed amount `|A_D|~0.0241` per attached `D`, while the beta-viscous natural envelope becomes rapidly more negative.

## 5. Why the chain is finite-critical

At `u=4`, the exact beta turning point is

\[
x_{\beta,4}
=\frac14\sqrt{17\beta^{-4/3}-1}.
\tag{SGR19}
\]

It exists only for

\[
\beta\le8.
\]

For

\[
\boxed{\beta\ge9}
\tag{SGR20}
\]

the radicand is negative. Hence the principal growing coordinate has strictly negative net rate for every slope: there is no growing/neutral beta-9 turning point at all.

Therefore the repeated-`D` promoted chain meets the uniformly stable high-beta sector after the finite list (SGR18). The infinite tail does not create infinitely many finite-dimensional compatibility equations; it belongs to the stable-complement solve.

## 6. Character collisions with the designated channels

The first members of the chain are not all new independent Fourier characters:

\[
G_1=C,
\qquad
G_2=P,
\qquad
G_3=E.
\tag{SGR21}
\]

Thus generation inside the second collar produces **renewal contributions** to existing characters before creating genuinely new rows at beta four and above.

This is important for the finite control map:

- `G_2` perturbs the transported `P` amplitude;
- `G_3` perturbs the desired `E` amplitude;
- `G_4,...,G_8` are genuinely new promoted shortcut coordinates.

A correct second-gate map must therefore be formulated in terms of total exit amplitudes, not genealogical labels.

## 7. Sufficient clean second-gate output block

If the outgoing transported `P` is support-terminated immediately after the second collar and does not enter later overlaps, it need not be prescribed as an independent renewal coordinate. A sufficient clean finite output block is then

\[
\boxed{
\mathcal Y_2
=(E,C_{new},G_4,G_5,G_6,G_7,G_8).
}
\tag{SGR22}
\]

with target

\[
\boxed{
(E,C_{new},G_4,G_5,G_6,G_7,G_8)_{out}
=(E_*,0,0,0,0,0,0).
}
\tag{SGR23}
\]

This gives **seven complex output conditions** in the clean routed formulation.

If one also insists on prescribing the total beta-two `P` exit amplitude, the sufficient block becomes eight-dimensional. The seven-row route is preferred because `P` has no later designated role once the second event has completed; its support can be ended at the handoff.

## 8. Control-rank warning

The second gate is not an immediate copy of the first six-state direct-source Vandermonde. A perturbation of the `P-D` collision directly excites both the sum child `E` and the difference child `C_new` at the same source order. The later rows `G_4,...,G_8` are then generated through repeated attachment of `D`.

Therefore the correct frozen response matrix has a two-branch first layer followed by a one-sided triangular tail. Its rank must be proved explicitly; it cannot be inferred from the first-gate consecutive-degree Vandermonde theorem.

A promising route is to use translated control profiles. The homogeneous beta-three and beta-one exit kernels have distinct logarithmic rates at the working point:

\[
\partial_z\mathcal E_{3,4}(z_E)
\approx-7.4929854050,
\]

\[
\partial_z\mathcal E_{1,4}(z_C)
\approx-0.6088316901,
\tag{SGR24}
\]

so time translation already separates the direct `E` and `C_new` rows. Downstream repeated-`D` integrations add higher Volterra orders for `G_4,...,G_8`.

This suggests a seven-control generalized exponential/Vandermonde system rather than a singular same-order source matrix.

## 9. Next frontier

The second-gate problem is now finite:

\[
\boxed{
\textbf{prove full rank for a seven-control translated-profile response map on }
(E,C_{new},G_4,\ldots,G_8).
}
\tag{SGR25}
\]

After rank, the same finite-parameter `C^1` zero-residual transfer used for the first gate can be repeated. Separately, the handoff architecture must provide delayed same-character copies of `C` and `D` for the later `E-C`, `Q-C`, and `H+D` events without reintroducing the refresh obstruction.

No full reset-cell or unforced Navier--Stokes blowup theorem is claimed here.
