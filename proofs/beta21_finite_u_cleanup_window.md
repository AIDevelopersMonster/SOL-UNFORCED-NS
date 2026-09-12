# Exact finite-`u_*` cleanup window for the beta-(2,1) reset architecture

**Status:** EXACT-SOURCE ENVELOPE / COMPUTER-ASSISTED DESIGN WINDOW. The large-`u_*` ordered beta-(2,1) reset candidate suffers a full-lattice action-filter obstruction because both old unit-beta channels remain available after reset. This note identifies a different finite-`u_*` design regime in which the surviving child is placed exactly at its beta-one turning point and the **spent old catalyst lies strictly below the renewed beta-two parent** at the reset face.

This does not yet prove a support-gated autonomous cell. It isolates a concrete parameter window in the exact source envelope where one of the two old input channels can be exponentially discarded after one reset, while the renewed pair remains available. The remaining tasks are to embed the ordered collision circuit into the auxiliary-support geometry and to verify that no unwanted sibling output is routed into the next cell.

Primary source input: the exact finite-`u_*` envelope `mathcal E_{beta,u}` from `beta_phase_stability.md`, derived from the source pulse equations (7.2)--(7.11).

## 1. Turning-point gauge

Impose

\[
\boxed{x+\delta=1.}
\tag{CU1}
\]

Thus the beta-one catalyst coordinate at the first-event section is exactly its source turning point. Since

\[
\mathcal E_{1,u}(1)=0
\]

for every finite `u`, the first exact relay resonance

\[
\mathcal E_{2,u}(x)
+\mathcal E_{1,u}(x+\delta)
=\mathcal E_{1,u}(x-\delta)
\]

reduces to

\[
\boxed{
\mathcal E_{2,u}(1-\delta)
=
\mathcal E_{1,u}(1-2\delta).
}
\tag{CU2}
\]

For each tested `u` in the range below there is a unique root near the reduced large-`u` value `delta≈0.1633`.

Set

\[
\boxed{x_u:=1-\delta_u.}
\tag{CU3}
\]

## 2. Reset face and the spent-catalyst coordinate

Keep the same kinematic reset face

\[
\boxed{T=2\delta_u.}
\tag{CU4}
\]

The renewed pair is

\[
(P_{new},D)
\]

with reset coordinates

\[
\boxed{x_{P_{new}}(T)=x_u,\qquad x_D(T)=x_u+\delta_u=1.}
\tag{CU5}
\]

The **old** catalyst `C`, if allowed to continue to the reset face, has coordinate

\[
\boxed{x_C(T)=x_u+3\delta_u=1+2\delta_u.}
\tag{CU6}
\]

Define the cleanup defect

\[
\boxed{
\Delta_{clean}(u)
:=
\mathcal E_{1,u}(x_u+3\delta_u)
-
\mathcal E_{2,u}(x_u).
}
\tag{CU7}
\]

If

\[
\Delta_{clean}(u)<0,
\]

then the spent old catalyst is exponentially below the renewed beta-two parent on the source action scale `Lambda~L_s/u`.

## 3. Exact finite-`u` computation

The companion script

`experiments/beta21_finite_u_cleanup_window.py`

solves (CU2) using the exact finite-`u` source primitive. Representative values are

\[
\begin{array}{c|c|c|c}
u & \delta_u & x_u & \Delta_{clean}(u)\\ \hline
2 & 0.2147613876 & 0.7852386124 & -0.0108674473\\
3 & 0.1853394591 & 0.8146605409 & -0.0031500616\\
4 & 0.1755496059 & 0.8244503941 & -0.0009299185\\
4.5 & 0.1729477209 & 0.8270522791 & -0.0003685222\\
4.9 & 0.1714213828 & 0.8285786172 & -0.0000447672\\
5 & 0.1710965815 & 0.8289034185 & +0.0000235958\\
7 & 0.1672574710 & 0.8327425290 & +0.0008175294\\
10 & 0.1652320608 & 0.8347679392 & +0.0012259189
\end{array}
\tag{CU8}
\]

The sign changes once. Numerically,

\[
\boxed{u_{crit}\approx4.96475611525.}
\tag{CU9}
\]

Hence, throughout the computed interval

\[
\boxed{2\le u<u_{crit},}
\tag{CU10}
\]

we have exact-source cleanup

\[
\boxed{\Delta_{clean}(u)<0.}
\tag{CU11}
\]

while for larger `u` the spent catalyst again sits slightly above the renewed beta-two parent.

The large-`u` limit is therefore the wrong regime for this particular cleanup mechanism.

## 4. Concrete exact-source working point `u=4`

Choose

\[
\boxed{u_*=4.}
\tag{CU12}
\]

Then

\[
\boxed{
\delta\approx0.1755496058694293,
\qquad
x\approx0.8244503941305708.
}
\tag{CU13}
\]

The exact first relay resonance holds:

\[
\mathcal E_{2,4}(x)
+
\mathcal E_{1,4}(1)
-
\mathcal E_{1,4}(x-\delta)=0.
\]

At the reset face

\[
T=2\delta\approx0.3510992117388586,
\]

the renewed child lies exactly at its turning point,

\[
\boxed{x_D(T)=1,\qquad \mathcal E_{1,4}(1)=0,}
\tag{CU14}
\]

whereas the renewed parent has

\[
\boxed{
\mathcal E_{2,4}(x)
\approx-0.171315363856206.
}
\tag{CU15}
\]

The spent old catalyst has

\[
 x_C(T)=x+3\delta\approx1.351099211738859
\]

and

\[
\boxed{
\mathcal E_{1,4}(x_C(T))
\approx-0.172245282371120.
}
\tag{CU16}
\]

Thus

\[
\boxed{
\Delta_{clean}(4)
\approx-9.29918514914\times10^{-4}<0.
}
\tag{CU17}
\]

This is small but fixed after `u=4` is frozen. Since the source action is multiplied by a factor comparable to `L_s/u`, the ratio between spent catalyst and renewed parent is

\[
\boxed{
\exp\{-c_{clean}L_s\}
}
\tag{CU18}
\]

for some fixed `c_clean>0` depending only on the frozen design.

Therefore polynomial `S_*` losses cannot restore the spent catalyst at sufficiently high levels.

## 5. Reset-action equation still has a causal solution

Using the same bounded reset genealogy

\[
C+D\to P,
\quad
P+D\to E,
\quad
E-C\to Q,
\quad
Q-C\to H,
\quad
H+D\to P_{new},
\]

and replacing every reduced primitive by the **exact** `mathcal E_{beta,4}`, the simultaneous reset-action equation has a causal root

\[
\boxed{s_{sim}\approx0.250238056806416.}
\tag{CU19}
\]

Since

\[
T-s_{sim}\approx0.1008611549>0,
\]

the reset occurs strictly before the face.

More importantly, the simultaneous collision is not required. Taking an ordered spacing

\[
\boxed{\eta=0.005}
\tag{CU20}
\]

and event times

\[
t_1=s,\quad t_2=s+\eta,\quad t_3=s+2\eta,\quad t_4=s+3\eta,
\]

the exact finite-`u` ordered action equation has the root

\[
\boxed{s_{ord}\approx0.213506242359214.}
\tag{CU21}
\]

The final causal margin is then

\[
\boxed{
T-t_4
\approx0.12259296938>0.
}
\tag{CU22}
\]

and the final parent-action residual is zero to the working numerical precision.

Thus the cleanup condition is compatible with a widely separated causal microcollar chain; it is not produced by squeezing all collisions into one tiny interval.

## 6. Polarization margins remain nonzero at `u=4`

At the ordered point (CU20)--(CU21), the exact principal source-frame coefficients have the approximate values

\[
\begin{array}{c|r}
P+C^*\to D & -2.7745\\
C+D\to P & +0.4488\\
P+D\to E & +0.8590\\
E-C\to Q & -4.4442\\
Q-C\to H & -7.3452\\
H+D\to P_{new} & +0.5472
\end{array}
\tag{CU23}
\]

so no mandatory edge is near a principal Leray cancellation.

## 7. What this fixes -- and what it does not

The full-lattice witness `7D-6C` from `beta21_action_filter_obstruction.md` is fatal only if the same old `C,D` bank remains available indefinitely and every algebraically possible genealogy can continue into later cells.

The finite-`u` cleanup window provides a route to break that assumption:

\[
\boxed{
\text{old }C
\quad\hbox{is exponentially below}\quad
P_{new}
\text{ at the reset face},
}
\tag{CU24}
\]

while the surviving `D` is exactly at its beta-one turning point and becomes the intended next catalyst.

This is **not yet** enough to declare `7D-6C` harmless inside the same cell. A support-gated construction is still needed so that unwanted descendants generated in one microcollar are not geometrically routed into later designated collars or the next cell.

The corrected target is therefore no longer a global all-lattice action filter. It is a finite **directed collision graph** with three properties:

1. every designated edge has the nonzero coefficients already audited;
2. every non-designated sibling output either leaves the routed support graph or carries a fixed exponential tail before it can re-enter;
3. at the cell boundary only the renewed pair `(P_new,D)` is retained at leading order, while the old catalyst is exponentially subleading.

## 8. Source-cone caveat

The source Section 7 construction permits choosing `u_*` sufficiently large after the background stress cone has been fixed, but the branch has so far used the large-`u_*` regime rather than proving that the specific moderate value

\[
u_*=4
\]

satisfies every quantitative cone margin required by the pinned source realization.

Therefore (CU12) is currently an **exact-envelope design point**, not yet a source-certified packet theorem.

The next mandatory audit is to compare the exact cone inequality used in the pinned OpenAI Section 7 packet construction with the cleanup window

\[
2\le u<u_{crit}\approx4.96475611525.
\]

If the source cone admits one `u` in this interval, the cleanup mechanism survives source certification. If it requires `u>u_{crit}`, this specific turning-point cleanup mechanism is ruled out and the project must return to support routing or a different phase bank.
