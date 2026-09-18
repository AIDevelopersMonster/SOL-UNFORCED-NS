# Gate 1 adversarial re-audit

**Status:** GATE 1 IS NOT CLOSED. THE CURRENT BRANCH CONTAINS SEVERAL STRONG REDUCTIONS AND PARTIAL THEOREMS, BUT THE FILES CLAIMING AN EXACT FINITE-S CORE+TAIL RESET DEPEND ON MULTIPLE UNPROVED OR INCOMPATIBLY-STATED INPUTS. THIS NOTE SUPERSEDES ALL EARLIER "GATE 1 CLOSED" STATUS LINES UNTIL THE OBLIGATIONS BELOW ARE REPAIRED.

The safe current project state is

\[
\boxed{
\text{Gate 1: conditional / not closed;}
\quad
\text{Gate 2: downstream conditional;}
\quad
\text{Gate 3: downstream conditional.}
}
\]

No global singularity or Clay-prize claim is made.

---

# A. Missing finite-S tangent normal-form theorem

The file beta21_lowu_exact_discrete_central_profile.md assumes

\[
\mathcal P_{b,S}^{tan}
=
I+h_S\mathcal L_b+h_S^2\mathcal K_{b,S},
\qquad
h_S=S^{-1/2},
\]

with

\[
\sup_S
\|\mathcal K_{b,S}\|_{X_b^{m+2}\to X_b^m}
<\infty.
\]

But the branch has no theorem file proving this operator expansion.

The existing beta21_lowu_profile_normal_form_coefficients.md proves only the leading coefficients \(v_b,B_b,C_b\) and Gaussian admissibility. Its own frontier explicitly lists as open:

- derive the full \(O(h_S^2)\) remainder in a Gaussian profile norm;
- solve the exact discrete finite-S profile equation.

Therefore the exact discrete-profile theorem currently assumes its main input.

\[
\boxed{\text{A: OPEN.}}
\]

---

# B. The current discrete-profile Neumann argument loses one derivative

Even granting the missing expansion, the current proof has a scale-of-spaces mismatch.

It states

\[
\mathcal K_{b,S}:X_b^{m+2}\to X_b^m,
\]

and

\[
G_b:X_b^m\to X_b^{m+1}.
\]

Hence

\[
G_b\mathcal K_{b,S}:
X_b^{m+2}\to X_b^{m+1},
\]

which loses one derivative relative to the input.

The proof then treats

\[
I+h_SG_b\mathcal K_{b,S}
\]

as a bounded perturbation of the identity on one Banach space and applies a Neumann series. That is not justified with the displayed mapping properties.

A repair needs one of:

1. a semiclassical graph norm in which \(h_SG_b\mathcal K_{b,S}\) is genuinely bounded on the same space;
2. a tame/Nash--Moser scale argument;
3. a stronger remainder theorem \(\mathcal K_{b,S}:X^{m+1}\to X^m\) together with a one-derivative-gaining \(G_b\);
4. a direct discrete Volterra construction avoiding the Neumann operator on a derivative-losing scale.

Until one such repair is written, the exact central profile theorem is not valid.

\[
\boxed{\text{B: OPEN.}}
\]

---

# C. Volterra inverse / solvability space is not pinned correctly

The discrete-profile proof defines

\[
X_{b,0}^m
=
\ker\ell_b
\]

and then writes

\[
G_b:X_{b,0}^m\to X_{b,0}^{m+1}.
\]

But the right-hand side

\[
\mathcal K_{b,S}(\phi_b+w)
\]

is not proved to belong to \(\ker\ell_b\).

Fixing the normalization of the solution removes the one-dimensional kernel. It does not automatically impose a solvability condition on the forcing.

The correct theorem must determine whether

\[
\mathcal L_b
=
v_b\partial_y+B_by+C_b
\]

on the chosen physical Gaussian graph space has one-dimensional kernel and zero cokernel, in which case one can define

\[
G_b:X_b^m\to X_{b,0}^{m+1}
\]

on the entire forcing space, or whether a nontrivial cokernel exists and a genuine Lyapunov--Schmidt scalar condition is required.

The current proof does not establish this Fredholm statement.

\[
\boxed{\text{C: OPEN.}}
\]

---

# D. Exact core+tail theorem promotes reductions to proved operator estimates

The file beta21_lowu_exact_finiteS_core_tail_local_reset.md lists as proved inputs several earlier layers that themselves still state open operator obligations.

For example, beta21_lowu_designated_orbit_complement_propagator_reduction.md ends with the target

\[
\|B_S\|+\|C_S\|
\le
S^Ae^{-c_*S}
\]

and explicitly says the actual curl/Leray source-level estimate remained open at that stage.

A later file, beta21_lowu_uniform_source_bilinear_packet_bound.md, does provide a source-uniform fixed-order bilinear estimate and closes much of that port. However its own final caveat says the abstract norm \(X_m\) has not yet been identified with one explicitly named common norm with all derivative offsets and polynomial powers recorded.

For a scalar action-gap estimate this may be bookkeeping.

For the three-block Banach map

\[
T\oplus m\oplus z
\]

it is not automatically bookkeeping: every block map must be bounded between the exact spaces used by the fixed-point theorem, with compatible derivative orders.

Thus the exact core+tail theorem needs a single common-norm operator ledger, not just exponent signs.

\[
\boxed{\text{D: OPEN AT OPERATOR-NORM COMPATIBILITY LEVEL.}}
\]

---

# E. Derivative-loss compatibility of the Banach map is not yet written

The source-uniform bilinear theorem gives schematically

\[
X_{m+c}\times X_{m+1+c}
\to
X_m.
\]

The nonzero forward propagator does provide one parabolic derivative of smoothing:

\[
\mathfrak A_{\sigma,0}
\to
\mathfrak A_{\sigma,1}
\]

with the integrable kernel

\[
1+(t-s)^{-1/2}.
\]

This is enough for the original nonzero block at one derivative loss.

But Gate 1 later combines tail, angular mean, nonzero complement, parameter differentiation, and curl/reconstruction offsets.

The current three-block contraction theorem does not state one derivative-index ledger proving that every nonlinear leg returns to the same product space after all fixed offsets \(c\).

In particular, the proof cannot simply call all finite derivative losses "polynomial in S": derivative loss and polynomial coefficient growth are different issues.

A correct Gate 1 theorem must choose explicit integers

\[
m_T,m_M,m_Z
\]

and prove every arrow

\[
T\to m,\quad
T\to z,\quad
m\to T,\quad
m\to z,\quad
z\to T,\quad
z\to m
\]

maps the selected spaces to themselves after the available smoothing.

\[
\boxed{\text{E: OPEN.}}
\]

---

# F. The old two-block weighted-norm proof contained an algebraic gap; this one is repaired

The earlier mean/nonzero contraction chose

\[
\tau_S=\sqrt{b_S/c_S}
\]

and estimated \(\tau_S\) from upper bounds on \(b_S,c_S\).

That is invalid without a lower bound on \(c_S\).

This has now been repaired in beta21_lowu_coupled_mean_nonzero_contraction.md by choosing explicit positive majorants

\[
b_S\le\bar b_S,\qquad
c_S\le\bar c_S
\]

and setting

\[
\tau_S=\sqrt{\bar b_S/\bar c_S}.
\]

Then

\[
\tau_Sc_S
\le
\sqrt{\bar b_S\bar c_S},
\qquad
b_S/\tau_S
\le
\sqrt{\bar b_S\bar c_S},
\]

so the contraction estimate follows from proved upper bounds only.

\[
\boxed{\text{F: REPAIRED.}}
\]

Commit:

\[
\texttt{2d622eadd98f590140dc45b36eb35fa83fb49ac0}.
\]

---

# G. The three-block Perron-weight argument still needs quantitative weight control

The core+tail theorem writes a nonnegative Lipschitz matrix

\[
L_S=
\begin{pmatrix}
q_T&a_{Tm}&a_{Tz}\\
a_{mT}&q_m&b\\
a_{zT}&c&q_z
\end{pmatrix}
\]

and argues that every directed cycle product tends to zero, hence

\[
\rho(L_S)\to0.
\]

Even if this spectral-radius statement is correct, the proof then chooses a positive Perron weight vector \(w_S\) and defines the product norm from it.

To close the fixed point and \(C^1\) transfer, one must also control the condition number of those weights.

If, for example,

\[
w_T/w_m
\]

or

\[
w_z/w_T
\]

grows faster than the source-small forcing decays, then

\[
\rho(L_S)<1
\]

alone does not imply the inhomogeneous radius or parameter derivative is small in the same weighted norm.

The two-block repair shows the right method: choose weights from explicit majorants, not from an abstract Perron eigenvector, and prove all weighted entries and the weighted forcing quantitatively small.

No such explicit three-block majorant-weight construction is currently written.

\[
\boxed{\text{G: OPEN.}}
\]

---

# H. Cross-label overlap changes a structural hypothesis of the pinned source

This is the most serious source-compatibility issue found in the second audit.

The pinned OpenAI construction proves and uses pairwise disjoint label support in structural theorems, not merely in one local product estimate.

Examples include:

- ActualCarrierGeometry.labelCarrier_disjoint;
- ActualInitialization pairwise support disjointness;
- ActualCycleResidualBounds.extraction_regular, whose hypotheses explicitly include disjoint supports;
- SignedCovariance.finite_product_diagonal, which uses padded-slot disjointness;
- WaveInteractionBounds.product_curl_zero on disjoint supports.

The low-u relay deliberately introduces a supernode in which selected labels overlap.

The branch file translated_async_overlap.md proves only that the overlap geometry is possible.

The branch file source_localized_action_preservation.md correctly observes that the local Leibniz estimate survives if one retains a cross-label product instead of setting it to zero.

But this does not automatically show that every downstream source theorem whose proof uses pairwise disjointness remains valid under the supernode modification.

Therefore Gate 1 needs a new explicit theorem of one of two forms.

### Option H1: independent overlapped residual decomposition

Rebuild the exact local harmonic/residual decomposition for one finite supernode directly, without using any source theorem whose hypotheses include label disjointness.

Then use only source theorems that are pointwise/local and remain valid for each individual wave.

### Option H2: supernode quotient/relabel theorem

Package the selected overlapping family as one new composite label and prove that all source regularity, reconstruction and residual theorems apply to that composite object while outer labels remain disjoint.

At present neither theorem is written.

Thus the statement

> "the only change from the source product calculus is that the selected cross-label product is retained rather than zero"

is too strong.

\[
\boxed{\text{H: OPEN AND HIGH PRIORITY.}}
\]

---

# I. Numerical action margins are not yet theorem certificates

Several decisive Gate 1 margins are recorded as results of "dense optimization", including

\[
C+C\to Q:
\qquad
\Delta_{\max}\le-0.05925018\ldots,
\]

and

\[
Q-C\to C:
\qquad
\Delta_{\max}\le-0.11675015\ldots.
\]

These are excellent numerical diagnostics, but the branch does not yet contain an interval-arithmetic or analytic monotonicity certificate proving the inequalities on the full compact core.

Likewise some transversality values are floating evaluations.

For a proof that depends on an exponential factor

\[
e^{-cS}
\]

with fixed \(c>0\), strict negativity must be certified, not merely sampled densely.

\[
\boxed{\text{I: OPEN CERTIFICATION TASK.}}
\]

---

# J. Exact finite-dimensional reset observables are underspecified

The older local reset theorem uses three real observables:

1. catalyst multiplier;
2. real parent multiplier;
3. imaginary parent multiplier.

The later core+tail theorem introduces additionally

- the root polarization parameter \(\tau\);
- central profile normalizations;
- a secondary parent Gaussian resonant gauge.

It states that after "one harmless normalization/gauge choice" the finite-dimensional ledger has matching dimensions and a nonsingular principal Jacobian.

That is not yet a complete Lyapunov--Schmidt theorem.

One must explicitly list all finite coordinates, all normalization constraints, all actual reset equations, which coordinates are free characteristic data, which coordinates are solved, and the exact square Jacobian whose determinant/minimal singular value is bounded away from zero.

Otherwise it is possible to accidentally consume a characteristic degree of freedom twice or miss a solvability condition from C.

\[
\boxed{\text{J: OPEN.}}
\]

---

# K. Revised Gate 1 architecture

A defensible proof order is now:

## Gate 1A — overlapped supernode exact algebra

Prove an exact residual decomposition for the deliberately overlapping finite label family, independent of source disjointness theorems.

## Gate 1B — exact normalized finite-S designated generator

Define the exact tangent/action-normalized one-cell operator and prove the expansion

\[
\mathcal P_{b,S}^{tan}
=
I+h_S\mathcal L_b+h_S^2\mathcal K_{b,S}
\]

in a precisely named Gaussian graph norm.

## Gate 1C — tame/discrete central profile theorem

Repair derivative loss and the Fredholm/Volterra domain issue; prove exact discrete profiles.

## Gate 1D — certified action margins

Replace dense scans by outward-rounded interval or analytic certificates.

## Gate 1E — common derivative-index operator ledger

Choose exact tail/mean/nonzero spaces and prove every block arrow is a self-map after available smoothing.

## Gate 1F — explicit three-block weighted contraction

Use majorant-derived weights, not an abstract Perron vector, and prove both contraction and forcing smallness in the same norm.

## Gate 1G — finite-dimensional Lyapunov--Schmidt ledger

Write the complete square finite-dimensional system and prove uniform transversality.

Only then may one state

\[
\boxed{\text{Gate 1 closed.}}
\]

---

# L. Current strongest safe claim

The branch currently supports a substantial collection of local reductions:

- viable low-u principal beta-(2,1) orbit geometry;
- one-root principal coupling compatibility;
- exact beta-zero root Cauchy/curl realization;
- root-augmented whole-space Oseen reduction;
- nonzero forward smoothing;
- weighted off-orbit and covariance reductions;
- source-uniform local bilinear estimates;
- polynomial tail-parametrix reduction with isolated secondary resonance;
- finite-dimensional principal transversality;
- repaired two-block mean/nonzero majorant contraction.

But the exact finite-S full-state reset theorem is not yet proved because obligations A--E, G--J remain.

The next mathematical priority is H + A/B/C, not Gate 2.

No downstream theorem should be strengthened before those are repaired.
