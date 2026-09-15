# Exact four-control `C^1` closure of the corrected beta-(2,1) entrance gate

**Status:** PROVED EXACT LOCAL ZERO-RESIDUAL FOUR-CONTROL ENTRANCE GATE THEOREM AT THE CORRECTED NON-TURNING WORKING POINT, SUBJECT TO THE BRANCH-WIDE NUMERICAL-CERTIFICATION CAVEAT. The corrected entrance difference event

\[
P-C\to D
\]

is exactly source matched at

\[
u=2.5,
\qquad
\delta=0.1375,
\qquad
x=0.7779445026067248271\ldots.
\]

A future-action audit shows that, among all characters generated in a short entrance collar, the only unwanted classes capable of reaching the later strong-`H` section above its target action are

\[
H=2D-C,
\qquad
R_3=3D-2C.
\]

The beta-zero root

\[
M=D-C
\]

is already below that future target, but it must be cancelled locally because it is the mediator of the dangerous chain. Thus the sufficient entrance control block is only

\[
(D,M,H,R_3).
\]

Four translated same-character `P` subpackets drive the exact source-matched rooted chain

\[
P-C\to D,
\qquad
D-C\to M,
\qquad
M+D\to H,
\qquad
H+M\to R_3.
\]

Every mandatory principal coefficient is nonzero with a fixed positive margin. The action-normalized frozen system is a four-state weighted shift and is controllable. The existing parameter-dependent phase-adapted zero-residual machinery transfers this rank to the exact local PDE map. Therefore one may prescribe

\[
\boxed{
(D,M,H,R_3)_{out}=(D_*,0,0,0),
\qquad D_*\ne0,
}
\]

while retaining the nonzero catalyst `C`. The old parent `P` need not be cancelled: after support routing it is exponentially negligible by the strong-`H` section.

This closes the last individual local gate in the corrected three-gate architecture. The remaining local tasks are support/collar concatenation and exact amplitude-state renewal of the outgoing `(P_new,D)` pair.

## 1. Corrected entrance resonance

The exact envelope relation is

\[
\boxed{
\mathcal E_{2,u}(x)
+
\mathcal E_{1,u}(x+\delta)
=
\mathcal E_{1,u}(x-\delta).
}
\tag{E4-1}
\]

At the working point,

\[
A_P
=-0.14633880209035941292\ldots,
\]

\[
A_C
=-0.00855661308220016015\ldots,
\]

\[
A_D
=-0.15489541517255957307\ldots,
\tag{E4-2}
\]

so

\[
\boxed{A_P+A_C=A_D.}
\tag{E4-3}
\]

The reduced slopes are

\[
z_P=x,
\qquad
z_C=x+\delta,
\qquad
z_D=x-\delta,
\]

all strictly inside the source interval `(1/2,3/2)`.

## 2. Rooted entrance genealogy

Define

\[
M=D-C=P-2C,
\]

\[
H=M+D=2D-C=2P-3C,
\]

\[
R_3=H+M=3D-2C=3P-5C.
\tag{E4-4}
\]

The sufficient controlled state is

\[
\boxed{Y_{ent}=(D,M,H,R_3).}
\tag{E4-5}
\]

The selected leading genealogy is

\[
P-C\to D,
\tag{E4-6}
\]

\[
D-C\to M,
\tag{E4-7}
\]

\[
M+D\to H,
\tag{E4-8}
\]

\[
H+M\to R_3.
\tag{E4-9}
\]

Every step uses characters already present in the two-generator lattice; no new generator is introduced.

## 3. Principal polarization margins

The first edge is a positive-beta difference interaction `(2,1)->1`. The generic formula in `beta21_microcascade_polarization_audit.md` gives automatic nonvanishing because

\[
z_P-z_C=-\delta\ne0.
\]

At the entrance center,

\[
\boxed{
\kappa_{P-C\to D}
\approx-1.24742865925.
}
\tag{E4-10}

The second edge has beta-zero target. Its exact projected root source has norm

\[
\boxed{
\|b_{D-C\to M}\|
\approx4.02998592509.
}
\tag{E4-11}

Using the beta-zero wave-root formula from `beta21_second_gate_mean_root_polarization_audit.md`,

\[
\boxed{
\kappa_{M+D\to H}
\approx-7.09992543506,
}
\tag{E4-12}

and

\[
\boxed{
\kappa_{H+M\to R_3}
\approx-6.55989900671.
}
\tag{E4-13}

On the fixed collar

\[
\boxed{0\le t\le10^{-3},}
\tag{E4-14}

`experiments/beta21_corrected_entrance_four_state_audit.py` gives the conservative sampled bounds

\[
|\kappa_{P-C\to D}|>1.2472,
\]

\[
\|b_{D-C\to M}\|>4.0299,
\]

\[
|\kappa_{M+D\to H}|>7.0999,
\]

\[
|\kappa_{H+M\to R_3}|>6.5598.
\tag{E4-15}
\]

Thus the selected rooted chain stays uniformly away from every principal polarization zero.

## 4. Future-action audit to the strong-`H` section

The relevant question is not which descendants are momentarily present at `t=0`, but which entrance-generated descendants can still compete at

\[
t_*=0.2251291169828679798\ldots
\]

with the later strong-`H` target action

\[
A_*^{H}
=-0.08872289617738492231\ldots.
\tag{E4-16}
\]

Represent an entrance character as

\[
K=mP+nC,
\qquad
\beta_K=2m+n.
\]

The reachability audit starts from the real seeds `±P,±C`, combines only distinct signed characters at principal order, assigns source action as the sum of parent actions, and propagates each positive-beta child exactly from its generation section to `t_*`. For beta-zero children, ignoring viscous damping gives a conservative upper bound.

At the collar center the only conjugacy classes at or above `A_*^H` are

\[
\boxed{
C,\quad D=P-C,\quad H=2P-3C,\quad R_3=3P-5C.
}
\tag{E4-17}

The first omitted class is

\[
M=P-2C,
\]

with future-action gap approximately

\[
\boxed{
A_M^{upper}-A_*^{H}
\approx-7.4729\times10^{-2}.
}
\tag{E4-18}

On the whole entrance collar (E4-14), the same promoted list persists and the nearest omitted future-action gap remains larger than

\[
\boxed{
\gamma_{future}>7.47\times10^{-2}.
}
\tag{E4-19}

Thus every other entrance-generated character is exponentially negligible by the strong-`H` stage once the four displayed controlled coordinates are prescribed.

## 5. Why the old parent need not be an exit coordinate

The original beta-two parent `P` is not cancelled by the entrance gate. Instead it is support-routed away from the subsequent active collars.

Even under conservative homogeneous transport, its action at `t_*` is

\[
A_P^{tr}(t_*)
\approx-0.604914174965657,
\]

which is below the strong-`H` target by more than

\[
0.516.
\tag{E4-20}
\]

Hence the old parent has no leading action role at the next active stage. It need not consume a control coordinate in the entrance solve.

## 6. Frozen four-state controllability

Split the incoming beta-two parent into four localized same-character amplitude controls,

\[
\boxed{
P(p)=P_{base}+\sum_{j=1}^4p_jP_j,
\qquad p\in\mathbb C^4,
}
\tag{E4-21}
\]

with distinct translated centers inside the positive entrance collar.

Linearization of `P_j-C -> D` supplies a direct nonzero input into the `D` equation. At leading action order the chain (E4-6)--(E4-9) gives, after integrating-factor/action normalization,

\[
X'=A_4X+B_4q,
\qquad
X=(D,M,H,R_3),
\]

with

\[
B_4=b_0e_1,
\qquad b_0\ne0,
\]

and nonzero first-subdiagonal coefficients

\[
a_1,a_2,a_3\ne0.
\]

The action filtration removes every alternative route from the leading normalized operator: each such route needs an additional negative-action `C` or `P` leaf.

Therefore the frozen leading operator is a weighted shift up to its diagonal, and

\[
\boxed{
\det[B_4,A_4B_4,A_4^2B_4,A_4^3B_4]
=b_0^4a_1^3a_2^2a_3\ne0.
}
\tag{E4-22}
\]

Thus the four-state frozen entrance system is controllable.

## 7. Smooth translated `P` controls

For a controllable finite constant pair `(A_4,B_4)`, translated compact source profiles generate a full-rank response for four suitable distinct centers in every sufficiently short nontrivial interval. Choose fixed smooth profiles inside (E4-14) and write their principal response matrix as

\[
J_{4,0},
\qquad
\boxed{d_4:=|\det J_{4,0}|>0.}
\tag{E4-23}

The coefficient margins (E4-15) are uniform on the positive collar. Hence slow coefficient variation gives

\[
\boxed{
|\det J_{4,var}|\ge\frac34d_4>0
}
\tag{E4-24}
\]

after fixing sufficiently narrow profile supports and centers.

## 8. Internal realization and no new forcing

Every `P_j` in (E4-21) has the same phase and principal polarization as the physically present incoming parent `P`.

Therefore:

1. no new lattice generator is added;
2. same-phase `P_i,P_j` principal self-interactions vanish by incompressibility;
3. the difference interaction with the fixed catalyst `C` supplies the direct `D` source with the nonzero coefficient (E4-10);
4. the source coefficient classes are closed under the finite localized decomposition;
5. Lemma 7.7-type curl realization restores exact divergence freedom with lower-order remainder;
6. the parameters are internal approximate-field degrees of freedom, not external forcing.

This is the exact entrance analogue of `catalyst_subpacket_direct_P_realization.md`.

## 9. Exact parameter-dependent zero-residual solve

Choose a fixed compact control neighborhood `K_p`. Differentiation in one of the four finite amplitudes replaces one bounded parent coefficient by one bounded fixed profile and does not differentiate the high carrier phase.

Hence the estimates already proved in `six_control_C1_exact_first_gate_closure.md` apply with only a changed finite design constant:

\[
\|f_p\|+\|D_pf_p\|
\le
CS_*^A(\varepsilon^{1/5}+e^{-cS_*}),
\tag{E4-25}
\]

\[
\|F_{mean,p}\|+\|D_pF_{mean,p}\|
\le
CS_*^A\varepsilon^{1-\kappa_s}.
\tag{E4-26}
\]

The exact nonzero and mean maps remain uniform contractions for sufficiently high dyadic levels. Their fixed points are `C^1` in `p` and obey

\[
\boxed{
\|D_pz\|+\|D_pm\|=o(1).
}
\tag{E4-27}
\]

## 10. Exact entrance exit map

Define

\[
\mathcal G^{ent}_{\ell}(p)
=(D,M,H,R_3)_{out}.
\tag{E4-28}

The fixed future-action gap (E4-19), the positive-width principal rank, and the exact correction estimate imply

\[
\boxed{
D_p\mathcal G^{ent}_{\ell}
=J_{4,var}+o(1).
}
\tag{E4-29}

Therefore, for all sufficiently high levels,

\[
\boxed{
|\det D_p\mathcal G^{ent}_{\ell}|
\ge\frac12d_4>0.
}
\tag{E4-30}

At frozen principal level prescribe

\[
(D,M,H,R_3)
=(D_*,0,0,0),
\qquad D_*\ne0.
\tag{E4-31}

The quantitative inverse-function theorem gives a unique nearby exact control vector

\[
\boxed{p_\ell=p^0+o(1)}
\tag{E4-32}

such that

\[
\boxed{
\mathcal G^{ent}_{\ell}(p_\ell)
=(D_*,0,0,0).
}
\tag{E4-33}

The catalyst `C` remains in a fixed nonzero compact amplitude range; it is not an exit coordinate of the four-state solve. The old parent `P` is routed away after the entrance collar and is action-negligible at the next stage by Section 5.

## 11. Consequence

The corrected entrance event is now an exact local active gate:

\[
\boxed{
(P,C)_{in}
\longmapsto
(C,D)_{handoff},
}
\tag{E4-34}

with prescribed nonzero `D` amplitude and with the three mediator/danger coordinates

\[
M=H=R_3=0
\]

at the gate exit.

Combining this theorem with

- `beta21_corrected_strong_H_nine_control_C1_closure.md`, and
- `beta21_corrected_terminal_three_control_C1_closure.md`,

all three individual active collars of the corrected non-turning architecture are now locally closed.

The next theorem must concatenate them with explicit support routing and then solve the two-amplitude renewal condition for the complete local cell. No cross-scale infinite cascade or unforced Navier--Stokes blowup theorem is claimed. Publication-final use still requires outward-rounded interval certification of the numerical margins above.
