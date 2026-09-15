# Action-scale and support obstruction to the terminal homogeneous second-gate bank

**Status:** PROVED OBSTRUCTION TO THE PREVIOUS TERMINAL HOMOGENEOUS-CANCELLATION ARCHITECTURE INSIDE THE CURRENT FINITE-`u_*=4` RESET CELL. The five-coordinate principal map in `beta21_second_gate_terminal_homogeneous_cancellation_bank.md` is algebraically full rank, and `beta21_second_gate_five_control_C1_transfer.md` correctly states a conditional finite-parameter transfer. However two hypotheses required to realize that map are not satisfied by the current source geometry:

1. the four unwanted critical traces are exponentially **above** their own natural homogeneous pulse envelopes, so an `O(1)` source-native homogeneous pulse in the same character cannot cancel them;
2. the surviving unit-beta parent `D` cannot passively leave the terminal correction region before the reset face, because from the second collision to the reset face it moves toward its turning point rather than into a flat tail.

Hence the terminal direct-character bank is not an admissible closure mechanism for the present reset cell. The second active gate must use **source-matched controls generated at the parent/product action scale**, or the reset timing/support architecture must be redesigned.

## 1. Second-collision and reset times

At the finite-`u=4` cleanup point,

\[
\delta=0.17554960586942932598\ldots,
\qquad
T=2\delta=0.35109921173885865196\ldots.
\tag{TB1}
\]

Use the ordered working value

\[
t_2=0.218506242359214\ldots.
\tag{TB2}
\]

The reduced slopes at the second collision are

\[
z_D(t_2)=1-2\delta+t_2
=0.867407030620355348\ldots,
\tag{TB3}
\]

\[
z_P(t_2)=1-\delta+t_2
=1.042956636489784674\ldots.
\tag{TB4}
\]

For unit beta at `u=4`, the exact turning point is

\[
x_{1,4}=1.
\tag{TB5}
\]

Since

\[
z_D(T)=1-2\delta+T=1,
\tag{TB6}
\]

the reset face is exactly the `D` turning section.

## 2. `D` does not enter a removable tail before the reset

The exact unit-beta envelope satisfies

\[
\mathcal E_{1,4}(z_D(t_2))
=-0.02407863050407955\ldots,
\tag{TB7}
\]

and

\[
\mathcal E_{1,4}(z_D(T))=0.
\tag{TB8}
\]

On the entire interval

\[
t_2\le t\le T,
\]

the slope moves monotonically from `0.8674...` to the turning point `1`, so the envelope **increases** toward its maximum. Thus there is no post-collision subinterval before `T` on which the existing `D` packet becomes increasingly flat relative to its own pulse scale.

Consequently a cutoff that removes `D` before the terminal correction bank would have to transition while the packet is still at leading designated scale. Its cutoff derivative is not protected by an additional fixed action deficit. The exact correction solve would then face a leading `D`-scale residual rather than the `o(1)` perturbation assumed by the terminal-bank `C^1` transfer.

This directly contradicts the handoff hypothesis

\[
P,D\notin I_{corr,j}
\]

used in the terminal-bank reduction if all correction collars are required to lie inside the current reset interval before `T`.

The problem is especially structural because `D` is also the intended parent of the final reset edge

\[
H+D\to P_{new}
\]

at `T`.

## 3. `P` can decay, but that does not repair the bank

The beta-two packet is already on the decaying side at `t_2`. Its exact natural envelope at the second section is

\[
\mathcal E_{2,4}(z_P(t_2))
=-0.6931817871527722\ldots.
\tag{TB9}
\]

The derivative is approximately

\[
\partial_x\mathcal E_{2,4}(z_P(t_2))
=-3.26869\ldots,
\tag{TB10}
\]

so it acquires additional negative action rapidly to the right. For example at `z_P=1.10`, only `0.05704...` later in reduced drift,

\[
\mathcal E_{2,4}(1.10)
=-0.8935908038\ldots,
\tag{TB11}
\]

a further negative increment of about `-0.2004`.

Thus `P` is not the support bottleneck. The surviving `D` is.

## 4. Direct homogeneous controls have the wrong action scale

The full second-gate critical audit identifies the unwanted positive-defect characters

\[
H_1=2D-C,
\quad
H_2=3D-2C,
\quad
H_3=4D-3C,
\quad
H_4=7D-5C.
\tag{TB12}
\]

Their exact center leaf-action defects relative to their natural finite-`u=4` envelopes are

\[
\Delta_1\approx0.1547751844,
\]

\[
\Delta_2\approx0.7930137444,
\]

\[
\Delta_3\approx0.5737188319,
\]

\[
\Delta_4\approx0.3555923117.
\tag{TB13}
\]

On the source action scale

\[
\Lambda_\ell\asymp S_*,
\]

the generated unwanted trace in character `H_j` is therefore larger than an `O(1)` source-native homogeneous pulse on the natural `H_j` envelope by

\[
\boxed{
\exp(\Delta_j\Lambda_\ell).
}
\tag{TB14}
\]

To cancel such a trace by a direct homogeneous pulse in the same character would require a normalized control amplitude of size

\[
|p_j|\asymp\exp(\Delta_j\Lambda_\ell),
\tag{TB15}
\]

not an `O(1)` parameter in a fixed compact source-class neighborhood.

No fixed change of the source epsilon exponent repairs this: for every fixed `A`,

\[
\varepsilon^{-A}=\exp(O(\ell)),
\]

whereas

\[
\exp(\Delta_j\Lambda_\ell)=\exp(c_j\ell^2).
\]

Thus (TB15) exits the fixed source hierarchy.

## 5. Why waiting does not fix the action mismatch

Suppose an unwanted `H_j` trace and a homogeneous control in the same character are both propagated by the same principal linear mode. Homogeneous propagation adds the same envelope increment

\[
\mathcal E_j(t)-\mathcal E_j(t_2)
\]

to both action exponents. Therefore their action difference `Delta_j` is invariant under homogeneous transport.

Hence there is no later time at which an `O(1)` natural homogeneous pulse catches up with an already generated supercritical trace. The multiplicative factor in (TB14) persists until a nonlinear/source-matched cancellation acts.

## 6. Consequence for the previous five-control theorem

The algebraic statement

\[
D_pY_{out}^{principal}=I_5
\]

is correct after normalizing five hypothetical direct character controls to unit exit trace. But the normalization itself requires the forbidden exponentially large factors (TB15) for the four unwanted rows.

Accordingly `beta21_second_gate_five_control_C1_transfer.md` must be read strictly as a **conditional transfer theorem**. Its support/action hypotheses are not realized by the current finite-`u=4` reset architecture.

It does not close the second gate.

## 7. Sharp source-matched frontier

Any admissible leading cancellation of `H_1,...,H_4` must inherit their promoted leaf action from the original `P,D` collision genealogy rather than being injected on the smaller natural homogeneous envelopes.

Therefore the next control architecture must operate at or upstream of the promoted genealogy. Two promising equivalent formulations are:

1. translated internal `P/D` subpacket controls inside the second collision, with a finite critical exit map;
2. controls in a **subcritical ancestor character** whose interaction with the surviving `D` generates the dangerous modes at their correct promoted action.

The algebraic structure of the four critical characters reveals such an ancestor and is recorded separately in `beta21_second_gate_mean_root_factorization.md`.

No exact second gate is claimed here.
