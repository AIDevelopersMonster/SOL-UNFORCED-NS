# Twelve-state PBH rank theorem for the unrouted second active gate

**Status:** PROVED LEADING-ACTION FROZEN FULL-SYMBOL CONTROLLABILITY THEOREM. In the unrouted second overlap, one same-character `C` control profile drives two leading minimal-action branches simultaneously:

\[
C_{ctrl}+D\to P_{fresh}\to E_{fresh},
\]

and

\[
D-C_{ctrl}\to M\to X_2\to\cdots\to X_{10}.
\]

At leading minimal-leaf action these two branches are dynamically decoupled except for their common scalar control. Each branch is individually controllable. Their frozen full-symbol spectra are disjoint at the finite-`u_*=4` working point. Therefore the combined twelve-state single-input pair is controllable by the PBH criterion. Twelve translated smooth `C` controls give a locally onto finite output map on

\[
(P,E,M,X_2,\ldots,X_{10}).
\]

Cross-branch genealogies that would couple the positive-`C` `P/E` branch into the negative-`C` root family require additional cancelling leaves and are strictly lower in action; they enter the exact transfer as an action-small perturbation.

## 1. Two leading branches from one parent control

Perturb the old catalyst `C` in the physically present `C,D` second overlap. The same control coefficient has two principal quadratic projections:

\[
C_{ctrl}+D\to P_{fresh}=C+D,
\tag{PB1}
\]

and

\[
D-C_{ctrl}\to M=D-C.
\tag{PB2}
\]

Both projections are nonzero at the working geometry. The first is the already-audited unit-beta sum projection; the second is the beta-zero difference projection from the mean-root audit.

The fresh sum branch then has

\[
P_{fresh}+D\to E_{fresh}=C+2D.
\tag{PB3}
\]

The root branch is the ten-state chain from `beta21_second_gate_unrouted_ten_control_root_rank.md`.

## 2. Leading-action state

Order the twelve leading states as

\[
Y=(P,E;M,X_2,X_3,\ldots,X_{10}).
\tag{PB4}
\]

After integrating-factor normalization only when convenient, the frozen full-symbol linearization around the nonzero reference genealogy may be split at leading minimal action as

\[
\boxed{
Y'=A_0Y+B_0q,
\qquad
A_0=A_{PE}\oplus A_R,
\qquad
B_0=b_{PE}\oplus b_R.
}
\tag{PB5}

The `2 x 2` block `A_PE` has the nonzero edge `P+D -> E`. The `10 x 10` block `A_R` has the nine nonzero subdiagonal edges of the root chain. The input vector has a nonzero component in the first state of each block because both (PB1) and (PB2) are nonzero.

Thus

\[
(A_{PE},b_{PE})
\]

and

\[
(A_R,b_R)
\]

are individually controllable.

## 3. Why leading cross-branch couplings are absent

The `P/E` branch has nonnegative `C` coefficient:

\[
P=C+D,
\qquad
E=C+2D.
\]

Every nontrivial root-sideband state after `M=D-C` has a negative `C` coefficient. To produce a root character from a `P` or `E` leaf one must introduce additional conjugate-`C` leaves to reverse that sign. Conversely, to produce `P` or `E` from a negative-`C` root leaf one must introduce additional positive `C` leaves.

Because

\[
A_C<0,
\]

every additional cancelling pair decreases the leaf action by a fixed positive amount. Hence such cross-branch genealogies are strictly below the minimal absolute-leaf action used for the leading normalized coordinates.

Therefore the leading action-normalized finite operator is block diagonal as in (PB5). Cross-branch terms carry a fixed exponential action deficit and are `o(1)` after leading-action normalization.

## 4. Frozen full-symbol rates

For a positive-beta state `(beta,z)`, use the exact normalized principal rate

\[
\Gamma_{\beta}(z)
=
\frac1{\sqrt{1+u_*^2z^2}}
-
\beta^2
\frac{1+u_*^2z^2}{(1+u_*^2)^{3/2}}.
\tag{PB6}
\]

At `u_*=4`, the fresh branch has approximately

\[
\boxed{
\lambda_P=-0.8171726595,
\qquad
\lambda_E=-1.8732463513.
}
\tag{PB7}
\]

The beta-zero root has purely viscous normalized principal rate

\[
\boxed{
\lambda_M
=-\frac{n_M^2}{(1+u_*^2)^{3/2}}
\approx-0.0281388477,
}
\tag{PB8}
\]

where

\[
n_M=u_*(z_D-z_C)=-1.4043968469\ldots.
\]

The nine positive-beta descendants in the sufficient root chain have the diagnostic rates

\[
\begin{array}{c|r}
X_2&0.3606888939\\
X_3&0.8137920726\\
X_4&0.7803181375\\
X_5&0.3419701239\\
X_6&0.7523006399\\
X_7&0.9419807595\\
X_8&0.7138540285\\
X_9&0.6498149187\\
X_{10}&0.8487652673
\end{array}
\tag{PB9}

All twelve rates are distinct. The smallest pairwise separation in this frozen list is approximately

\[
\boxed{
\delta_{spec}\approx1.871877\times10^{-2}>0.
}
\tag{PB10}

Thus

\[
\boxed{
\operatorname{spec}(A_{PE})
\cap
\operatorname{spec}(A_R)
=\varnothing.
}
\tag{PB11}

## 5. PBH direct-sum lemma

Let `(A_1,b_1)` and `(A_2,b_2)` be finite-dimensional single-input controllable pairs with disjoint spectra. Then

\[
(A_1\oplus A_2,b_1\oplus b_2)
\]

is controllable.

Indeed, if `w=(w_1,w_2)` is a left eigenvector of `A_1\oplus A_2` with eigenvalue `lambda`, disjoint spectra imply that exactly one component can be nonzero. Controllability of the corresponding block gives

\[
w\cdot(b_1\oplus b_2)\ne0.
\]

The PBH criterion therefore gives full controllability.

Applying this lemma to (PB5),

\[
\boxed{
(A_0,B_0)\text{ is controllable on }\mathbb C^{12}.
}
\tag{PB12}

## 6. Smooth translated controls

For a controllable finite constant-coefficient pair `(A_0,B_0)`, the twelve response functions generated by

\[
K(\tau)
=\int e^{A_0(v_+-s)}B_0q(s-\tau)ds
\tag{PB13}
\]

span the full state space as `tau` varies on any nontrivial interval, provided the profile has nonzero transform on the finite spectrum. Equivalently, the scalar functions are an exponential-polynomial Chebyshev family associated with the cyclic minimal polynomial of `A_0`.

Therefore there exist twelve distinct centers

\[
\tau_1,\ldots,\tau_{12}
\]

inside a sufficiently short fixed source collar for which

\[
\boxed{
\det J_{12,0}\ne0.
}
\tag{PB14}

Unlike the nilpotent special cases, the determinant is a generalized exponential/Vandermonde determinant rather than a pure polynomial Vandermonde.

## 7. Stability under the actual coefficient system

The spectral separation (PB10), nonzero edge margins, and nonzero control projections are fixed after the finite-`u` design is frozen. On a sufficiently short collar, slowly varying source coefficients perturb the response columns continuously.

Cross-branch minimal-action violations are absent by Section 3; all remaining cross-branch terms carry a fixed action deficit. Source frame and curl errors contribute `O(S_*^{-1})` plus positive epsilon powers.

Hence

\[
J_{12,des,\ell}
=J_{12,0}+o(1)
\tag{PB15}
\]

in the leading action-normalized finite coordinates, and for all sufficiently high levels

\[
\boxed{
|\det J_{12,des,\ell}|
\ge\frac12|\det J_{12,0}|>0.
}
\tag{PB16}

## 8. Finite target

A sufficient clean leading target is

\[
\boxed{
(P,E,M,X_2,\ldots,X_{10})_{out}
=(P_*,E_*,0,\ldots,0),
}
\tag{PB17}

or, if outgoing `P` is not needed,

\[
P_*=0,
\qquad E_*\ne0.
\]

The twelve-control map is locally onto, so either finite prescription is available at frozen leading level.

This resolves the previous `E`-transversality issue without requiring routed removal of the old catalyst.

## 9. New frontier

The unrouted second gate now has a full leading finite-dimensional control architecture. The remaining obligation is the exact action-normalized `C^1` zero-residual transfer for the twelve same-character parent controls and a positive-width audit preserving the tiny positive/negative gap around the new beta-three mode `10D-7C`.

No support-removal hypothesis is required in this architecture.
