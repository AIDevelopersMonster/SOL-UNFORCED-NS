# Global-claim source-line audit: Gate 2 monodromy correction

**Status:** SOURCE-LINE AUDIT IN PROGRESS. THE PREVIOUS GATE 2 CHARACTERISTIC-MONODROMY GAP HAS BEEN REPAIRED BY `beta21_lowu_gate2_shrinking_buffer_schedule.md` AND `beta21_lowu_gate2_within_stage_characteristic_monodromy.md`, AND THE NONLINEAR COCYCLE HAS BEEN RERUN AGAINST THOSE INPUTS. GATE 2 IS RESTORED AT THE BRANCH-THEOREM LEVEL. A FINAL GLOBAL SINGULARITY CLAIM REMAINS WITHHELD UNTIL THE REMAINING DERIVED GATE 1 / GATE 3 LAYERS ARE SOURCE-LINE AUDITED.

Pinned source:

\[
\texttt{openai/NavierStokesAndEuler@f9e8bc5b38b6e212696e8a30e3e91517af887bbd}.
\]

No final unforced singularity or Clay-prize claim is permitted while this item remains open.

---

## 1. Source-exact inputs that pass

### Physical phase

The pinned PhaseCalculus source gives

\[
\Phi
=
p\theta+\frac{p_z}{\varepsilon}Z+x_0R-v[pF+p_zG]
\]

and the exact phase normal. This is sufficient for the exact beta-zero root-phase pinning.

\[
\boxed{\text{SOURCE-EXACT.}}
\]

### Natural physical rebase

The pinned PhysicalParticularWave / ActualReferenceRebase source proves the exact velocity scale factor

\[
Q^{A(h)}/Q_r^{A(h)}
\]

with no additional scalar. After the standard \(Q^{-A(h)}\) normalization, pure band/reference rebase is exactly amplitude-neutral.

\[
\boxed{\text{SOURCE-EXACT.}}
\]

### Moving source frame

PrimaryODE.FrameData.Kinematics proves exact skew orthonormal-frame derivatives and exact eigenvector-rate bookkeeping in the source primary ODE.

\[
\boxed{\text{SOURCE-EXACT FOR THE SOURCE PRIMARY ODE.}}
\]

Important: this does not itself prove a sign for the later low-\(u\) Gate 2 characteristic connection.

### Whole-space residual reconstruction

The pinned graph-to-physical residual identities and the branch phase-adapted Leray intertwining give a whole-space physical projected Navier--Stokes equation on each exact relay time collar.

\[
\boxed{\text{SOURCE-EXACT + DERIVED CONJUGATION.}}
\]

---

## 2. Standard external PDE dependency

The fixed-fast buffer map uses ordinary local wellposedness and smooth dependence for smooth divergence-free 3D Navier--Stokes data over a finite interval.

This must receive an explicit standard PDE citation in any global paper.

\[
\boxed{\text{STANDARD EXTERNAL PDE DEPENDENCY.}}
\]

---

## 3. Gate 2 discrepancy and repair

The first source-line pass found a real logical gap.

The theorem

**beta21_lowu_gate2_natural_rebase_characteristic_invariance.md**

proved only that pure source scale/reference rebase is neutral after natural normalization.  It explicitly left within-stage normalized characteristic dynamics open.

A later audit had asserted a source-small Hermitian connection without computing the complete buffer-inclusive exact characteristic transport.

That stronger source estimate is now discarded.

### Repair A: shrinking buffers

The theorem

**beta21_lowu_gate2_shrinking_buffer_schedule.md**

replaces fixed fast buffers by

\[
b_j=\varepsilon_j^2.
\]

They remain positive and fit inside the same constant-fast allocation, while

\[
\sum_j b_j<\infty.
\]

Standard short-time smooth dependence gives a summable \(C^1\) perturbation of the identity for the entire normalized buffer flow.  Thus no sign or leading coefficient of the source modal errors is needed on the extra buffers.

### Repair B: exact frozen active-cell tangent monodromy

Gate 1 supplies an exact characteristic family

\[
\mathscr P_{S,p}\mathscr S_S(p,\Xi)
=
\mathscr S_S(p,\Xi).
\]

Differentiate in \(\Xi\):

\[
D_U\mathscr P_{S,p}\,
D_\Xi\mathscr S_S
=
D_\Xi\mathscr S_S.
\]

Therefore

\[
\boxed{
D_U\mathscr P_{S,p}|_{E_{S,p}}=I
}
\]

on the exact characteristic tangent bundle.

All finite-\(S\) modal/frame/curl/tail effects inside the frozen active cell are already included in this identity.

### Repair C: orthonormal/Kato slow connection

Let

\[
B_S(p)=D_\Xi\mathscr S_S(p,\Xi_*),
\qquad
G_S(p)=B_S(p)^*B_S(p),
\]

and define the orthonormal characteristic frame

\[
\mathcal E_S(p)
=
B_S(p)G_S(p)^{-1/2}.
\]

Then

\[
\mathcal E_S^*\mathcal E_S=I,
\]

so along the trapped-spine slow path

\[
\mathcal A_S
=
\mathcal E_S^*
\partial_\sigma\mathcal E_S
\]

satisfies

\[
\boxed{
\mathcal A_S^*+\mathcal A_S=0
}
\]

exactly.

Thus the first-order slow characteristic transport is norm-neutral by finite-dimensional Hilbert geometry, not by an unproved source sign condition.

The discrete overlap map satisfies

\[
T_j^{char}
=
I-\Delta\sigma_j\mathcal A_j
+
O((\Delta\sigma_j)^2),
\]

hence

\[
(T_j^{char})^*T_j^{char}
=
I+O((\Delta\sigma_j)^2).
\]

Since

\[
\sum_j(\Delta\sigma_j)^2<\infty,
\]

the characteristic fundamental matrix and inverse remain uniformly bounded.

### Repair D: nonlinear cocycle rerun

The file

**beta21_lowu_gate2_nonlinear_invariant_cocycle.md**

has been updated so that its center propagation uses the repaired orthonormal/Kato connection and shrinking buffers.  It no longer cites the unsupported source-small Hermitian connection estimate.

### Verdict

\[
\boxed{
\text{GATE 2 MONODROMY GAP: REPAIRED AT THE BRANCH-THEOREM LEVEL.}
}
\]

The standard local Navier--Stokes flow theorem remains an external cited dependency for the shrinking buffers.

---

## 4. Corrected Gate 2 source-line classification

The decisive Gate 2 inputs are now classified as follows.

1. Pure source scale/reference rebase neutrality:
   \[
   \boxed{\text{SOURCE-EXACT.}}
   \]

2. Exact Gate 1 characteristic fixed-family identity:
   \[
   \boxed{\text{DERIVED GATE 1 THEOREM.}}
   \]

3. Frozen tangent monodromy identity obtained by differentiating that exact family:
   \[
   \boxed{\text{EXACT CONSEQUENCE OF THE DERIVED GATE 1 THEOREM.}}
   \]

4. Orthonormal/Kato connection skew-Hermiticity:
   \[
   \boxed{\text{STANDARD FINITE-DIMENSIONAL HILBERT-BUNDLE IDENTITY.}}
   \]

5. \(C^2\) section Taylor remainder:
   \[
   \boxed{\text{DERIVED BRANCH THEOREM.}}
   \]

6. Shrinking buffer flow:
   \[
   \boxed{\text{STANDARD LOCAL PDE FLOW + SUMMABLE DESIGN CHOICE.}}
   \]

7. Hyperbolic analytic complement / Lyapunov--Perron solve:
   \[
   \boxed{\text{DERIVED BRANCH THEOREM.}}
   \]

At this source-line granularity there is no longer a missing Gate 2 within-stage monodromy hypothesis.

---

## 5. Updated safe project status

After the repair,

\[
\boxed{
\text{Gate 1: strong derived branch theorem;}
}
\]

\[
\boxed{
\text{Gate 2: restored / closed at branch-theorem level;}
}
\]

\[
\boxed{
\text{Gate 3: internally closed at branch-theorem level, but global promotion still withheld.}
}
\]

Why is the global claim still withheld?

Because Gate 1, the hyperbolic Gate 2 complement, and the physical Gate 3 lower-bound/Gram lemmas are substantial **derived** results.  The present source-line audit has classified their dependencies but has not yet independently replayed every estimate from the pinned source and standard PDE inputs.

The next audit phase is therefore theorem-by-theorem proof replay, beginning with the Gate 1 normal form / tail / exact gluing chain and then the Gate 3 physical lower-bound chain.

## 6. Next source-line audit targets

The next work is not another global theorem.  It is a conservative proof replay of the two deepest derived blocks:

1. **Gate 1 replay**
   - finite-\(S\) tangent normal form;
   - exact discrete central profile;
   - analytic-tail parametrix;
   - coupled full-state gluing and finite-dimensional IFT.

2. **Gate 3 replay**
   - center-point physical \(H^1\) lower bound;
   - catalyst Gram coercivity;
   - tail/correction upper bounds in the same physical norm.

Any nonabsorbable loss or unproved compactness/invertibility assumption found in that replay downgrades the global chain immediately.

No final unforced singularity or Clay-prize claim is made here.
