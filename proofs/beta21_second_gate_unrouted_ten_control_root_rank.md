# Ten-control triangular rank theorem for the unrouted second-gate mean-root family

**Status:** PROVED FROZEN PRINCIPAL ROOT-BLOCK RANK THEOREM. Keeping the old `C,D` pair in the second overlap enlarges the dangerous sideband family but leaves it finite. All six positive-defect characters lie on one ten-state chain generated from the beta-zero root `M=D-C`. The mandatory principal couplings along that chain are nonzero. Therefore ten translated parent-control profiles with a nonzero direct `M` component give full rank on the complete sufficient root block.

This theorem controls the dangerous/root coordinates. It deliberately does **not** yet prescribe the desired `E` amplitude; `E`-transversality after root cancellation is the remaining finite-dimensional issue before an exact unrouted second-gate theorem.

## 1. Ten-state sufficient root chain

Define

\[
X_1=M=D-C,
\tag{UR1}
\]

\[
X_2=D+M=2D-C,
\tag{UR2}
\]

\[
X_3=D+2M=3D-2C,
\tag{UR3}
\]

\[
X_4=D+3M=4D-3C,
\tag{UR4}
\]

\[
X_5=D+4M=5D-4C,
\tag{UR5}
\]

\[
X_6=2D+4M=6D-4C,
\tag{UR6}
\]

\[
X_7=2D+5M=7D-5C,
\tag{UR7}
\]

\[
X_8=2D+6M=8D-6C,
\tag{UR8}
\]

\[
X_9=3D+6M=9D-6C,
\tag{UR9}
\]

\[
X_{10}=3D+7M=10D-7C.
\tag{UR10}
\]

The positive-defect modes from the full unrouted audit are

\[
X_2,X_3,X_4,X_6,X_7,X_{10}.
\]

The intermediate states `X_1,X_5,X_8,X_9` are included to make the control genealogy triangular.

## 2. Mandatory edge sequence

The directed chain is

\[
X_1+D\to X_2,
\tag{UR11}
\]

\[
X_j+M\to X_{j+1},
\qquad j=2,3,4,
\tag{UR12}
\]

\[
X_5+D\to X_6,
\tag{UR13}
\]

\[
X_j+M\to X_{j+1},
\qquad j=6,7,
\tag{UR14}
\]

\[
X_8+D\to X_9,
\tag{UR15}
\]

and

\[
X_9+M\to X_{10}.
\tag{UR16}
\]

All actions along this chain are the minimal absolute-leaf actions of the displayed characters because `M=D-C` itself is generated at the minimal two-leaf action `A_C+A_D`.

## 3. Principal nonvanishing

The first six mandatory coefficients through `X_7` are the same beta-zero mean-wave / one wave-wave coefficients audited in `beta21_second_gate_mean_root_polarization_audit.md`.

At the finite-`u=4` second-overlap geometry the additional three edges have principal growing coefficients

\[
\boxed{
\kappa_{X_7+M\to X_8}
\approx-14.2725436647,
}
\tag{UR17}

\[
\boxed{
\kappa_{X_8+D\to X_9}
\approx+5.3025260157,
}
\tag{UR18}

and

\[
\boxed{
\kappa_{X_9+M\to X_{10}}
\approx-35.3434809182.
}
\tag{UR19}

Hence every first-subdiagonal coupling of the ten-state chain is separated from zero at frozen principal level.

## 4. Parent-control input has a nonzero root component

Perturb the physically present old catalyst `C` by a smooth same-character control profile `q`. Its interaction with the surviving `D` has two leading branches:

\[
C_{ctrl}+D\to P_{fresh}
\]

and

\[
D-C_{ctrl}\to M.
\]

The beta-zero difference projection is nonzero. Therefore, after phase/action normalization, the control vector entering the root-chain linearization has the form

\[
\boxed{
B=b_0e_1+\sum_{j=2}^{10}b_je_j,
\qquad b_0\ne0.
}
\tag{UR20}

The lower components account for direct/shorter responses caused by the simultaneous sum branch and by other already-present base fields. Their values are irrelevant for the pivot argument below.

## 5. Lower-triangular linearization

Linearize the full finite root genealogy around its nonzero reference trajectory, after integrating-factor normalization of diagonal homogeneous transport. In the ordered basis `(X_1,...,X_10)`, the frozen system is

\[
X'=AX+Bq,
\tag{UR21}
\]

where `A` is lower triangular and

\[
\boxed{
A_{j+1,j}=c_j\ne0,
\qquad j=1,\ldots,9.
}
\tag{UR22}
\]

Entries farther below the first subdiagonal are unrestricted.

## 6. Controllability determinant

The Krylov matrix

\[
\mathcal C_{10}
=[B,AB,\ldots,A^9B]
\tag{UR23}
\]

is lower triangular in its pivot structure. The first new component of `A^kB` occurs in row `k+1` and equals

\[
\boxed{
b_0c_1c_2\cdots c_k.}
\tag{UR24}
\]

Hence

\[
\boxed{
\det\mathcal C_{10}
=b_0^{10}
 c_1^9c_2^8c_3^7c_4^6c_5^5c_6^4c_7^3c_8^2c_9
\ne0.
}
\tag{UR25}

Crucially, the simultaneous direct `P` response of a `C` perturbation only modifies the lower entries `b_j`; it cannot remove the nonzero pivot `b_0` and therefore cannot destroy this determinant.

## 7. Ten translated smooth controls

Choose one fixed smooth profile `q` with nonzero mass `mu_0`, and ten distinct translated centers `tau_j`. Let

\[
L_j=v_+-\tau_j.
\]

Exactly as in the previous smooth-profile control theorems, the exit kernel has a degree-nine finite expansion in `L`. The moment transform is lower triangular with diagonal `mu_0`.

Thus the ten-control exit matrix obeys

\[
\boxed{
\det J_{10}
=
\frac{
 b_0^{10}c_1^9c_2^8c_3^7c_4^6c_5^5c_6^4c_7^3c_8^2c_9
}{1!2!3!4!5!6!7!8!9!}
\mu_0^{10}
\prod_{1\le i<j\le10}(L_j-L_i).
}
\tag{UR26}

For equal spacing `L_j=L_0+(j-1)Delta`,

\[
\boxed{
\det J_{10}
=b_0^{10}c_1^9c_2^8c_3^7c_4^6c_5^5c_6^4c_7^3c_8^2c_9
\mu_0^{10}\Delta^{45}.
}
\tag{UR27}

Therefore the frozen root-block response is full rank.

## 8. Beta-zero stable transport

`X_1=M` is a `T=0` viscous mode. Its fixed full-symbol stable propagator may be absorbed by an integrating factor exactly as in `beta21_second_gate_beta_zero_fullsymbol_rank_bridge.md`. This changes the common source profile and column weights but not the nonzero pivot structure. On a sufficiently short fixed collar the full-symbol root matrix remains a continuous invertible perturbation of (UR26).

## 9. Source realization

Unlike the routed root controls, no exponential down-scaling is required. The old `C` packet and `D` packet are both physically present at their natural second-overlap actions. A bounded smooth `O(1)` perturbation of the `C` coefficient therefore changes the `D-C -> M` source at exactly the uncontrolled root action

\[
A_C+A_D.
\]

Finite sums of same-character `C` control profiles remain in the source wave class, add no lattice generator, and have vanishing same-phase principal self-interaction. Curl reconstruction supplies exact divergence-free physical controls with lower-order remainders.

Thus the ten controls are source-matched internal design parameters, not external forcing.

## 10. What is now closed and what remains

The complete six-mode positive-defect obstruction of the unrouted second overlap has been reduced to a ten-dimensional triangular root block, and that root block has a full-rank internal parent-control response.

What remains is one finite-dimensional transversality issue:

\[
\boxed{
\textbf{after solving }X_{1,out}=\cdots=X_{10,out}=0,
\textbf{ prove that the desired refreshed }E\textbf{ output is nonzero (or add one extra independent control to prescribe it).}
}
\tag{UR28}

Only after this `E`-transversality and the usual action-normalized `C^1` exact transfer should the unrouted second active gate be declared closed.
