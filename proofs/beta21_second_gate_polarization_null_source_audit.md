# Source audit of the second-gate polarization-null candidate

**Status:** SOURCE-REALIZATION GAP IDENTIFIED. The principal algebraic cancellation in `beta21_second_gate_polarization_null_candidate.md` is correct, but the currently pinned source pulse machinery does not by itself supply the required order-one mixed growing/decaying polarization as a localized same-character control. Therefore the polarization-null mechanism is **not** promoted to an exact gate theorem.

## 1. What the algebraic candidate needs

The candidate requires, at the routed second collision, a beta-two `P` control with principal polarization

\[
p_P(\lambda_*)=g_P+\lambda_* d_P,
\qquad
\lambda_*\approx-1.83986275014345,
\]

for which

\[
A_-^+(\lambda_*)=0,
\qquad
A_+^+(\lambda_*)\approx-1.24674061852109\ne0.
\]

Thus the unwanted `P-D -> C_new` growing source vanishes while the desired `P+D -> E` growing source survives.

The issue is not this principal algebra. The issue is whether such an order-one mixed polarization is available **inside the audited source classes** without paying a leading residual or an exponentially large incoming amplitude.

## 2. What the pinned homogeneous pulse lemma actually provides

The pinned OpenAI source, Lemma 7.4, constructs a particular homogeneous `m=1` pulse in the diagonal growing/decaying coordinates by specifying a nonzero growing datum and zero decaying datum. In the source notation this is the homogeneous pulse used later to realize covariance columns; its physical polarization is asymptotic to the distinguished growing vector

\[
e_r-sK+c_0\sqrt{1+s^2}N
\]

up to `O(S_*^{-1})` frame error.

Therefore the source lemma directly certifies the growing pulse required throughout the existing branch. It does **not** state a localized source-class theorem for arbitrary order-one combinations

\[
z_+g+z_-d
\]

with both `z_+,z_-` freely prescribed at an interior collision point.

Linear ODE existence for arbitrary transverse initial data is of course formal, but the branch needs more than existence: it needs the same support, envelope, smooth-zero-extension and source-small residual properties.

## 3. Why a hand-cut local mixed pulse is not enough

One cannot simply multiply an arbitrary mixed homogeneous solution by a compact time profile supported in the second collar. The derivative of that profile enters the pulse equation at the same carrier character. Unless the transition lies where the homogeneous amplitude is exponentially small or is itself generated through the source inverse, this can be an order-one residual.

An order-one residual would invalidate the perturbative statement

\[
D_p\mathcal G_\ell=J_{principal}+o(1)
\]

used by the first-gate `C^1` transfer.

Thus the algebraic mixed polarization cannot be inserted by fiat.

## 4. Transporting a decaying component is also nontrivial

A second idea is to prescribe the decaying component at an earlier collar and transport it homogeneously to the second collision. But the two diagonal coordinates have opposite inviscid shear exponents. Over a fixed positive normalized displacement, their relative size changes exponentially on the source action scale `Lambda_ell ~ c S_*`.

To retain an order-one ratio

\[
z_-/z_+\sim\lambda_*
\]

at the second collision would generally require exponentially reweighted incoming data. Such a datum is outside the current fixed normalized source-amplitude bookkeeping unless a separate resonance theorem compensates the decaying action.

No such compensation theorem is presently available.

## 5. Conservative conclusion

The polarization-null candidate remains valuable because it identifies a real algebraic direction in which the second gate could simplify. But the current rigorous status is

\[
\boxed{
\text{principal cancellation exists}
\quad\not\Rightarrow\quad
\text{source-admissible local control exists}.}
\]

Therefore it must not be used to discard the full critical lattice set in `beta21_second_gate_full_critical_audit.md`.

## 6. Source-native route retained

The conservative continuation is to use only control packets already justified by the source architecture:

1. homogeneous growing pulses of existing/specified characters;
2. translated auxiliary supports/centers;
3. curl-generated exact divergence-free realization;
4. finite source-wave sums;
5. exact zero-residual correction after the principal finite-dimensional map is proved.

A particularly clean alternative is to introduce direct same-character homogeneous controls for the finitely many critical output coordinates, rather than trying to create all control authority indirectly through one `P-D` source channel. At frozen principal level this gives a diagonally dominant finite exit map; nonlinear cross-couplings are then a finite perturbation to be audited on a sufficiently short collar.

The next theorem should therefore construct a **direct-character source-native control bank** for

\[
E,\quad 2D-C,\quad3D-2C,\quad4D-3C,\quad7D-5C
\]

(and any additional bookkeeping traces required by the chosen collar realization), then prove its finite exit Jacobian remains invertible after the designated interactions are restored.

No exact second active gate is claimed yet.
