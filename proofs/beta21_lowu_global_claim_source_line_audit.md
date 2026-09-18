# Global-claim source-line audit: Gate 2 monodromy correction

**Status:** SOURCE-LINE AUDIT IN PROGRESS. A critical unsourced step has been found in Gate 2. The current Gate 2--3 global chain is conditional until a buffer-inclusive / within-stage characteristic-monodromy theorem is proved.

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

## 3. The Gate 2 discrepancy

The theorem file

**beta21_lowu_gate2_natural_rebase_characteristic_invariance.md**

proves only

\[
\boxed{\text{pure scale/reference rebase is neutral}.}
\]

Its final section explicitly says that genuine normalized within-stage dynamics still requires analysis and names the missing target

**beta21_lowu_gate2_within_stage_characteristic_monodromy.md**.

No such theorem file exists in the branch.

The later file

**beta21_lowu_gate2_characteristic_connection_audit.md**

asserts

\[
\boxed{
\operatorname{Herm}\mathcal A_c^{(0)}=0
}
\tag{SL1}
\]

and then

\[
\boxed{
\|\operatorname{Herm}\mathcal A_{c,S}\|
\le
CS^B(\varepsilon^{a_*}+e^{-cS}).
}
\tag{SL2}
\]

The cited ingredients are skew moving-frame kinematics, eigenRate subtraction, pure-rebase neutrality, and source-small Gate 1 correction derivatives.

Those ingredients do not yet compute the full exact connection

\[
\mathcal A_{c,S}
=
[D_\Xi(\mathfrak C\circ\mathscr S)]^{-1}
\mathfrak C
\left(
\mathcal X_{S,p}(\mathscr S)
-
\partial_\sigma\mathscr S
\right).
\]

In particular they do not explicitly account for the complete entrance/exit buffer evolution and the real component induced after projection to the exact characteristic basis.

Therefore the bounded characteristic fundamental matrix used later in Gate 2 is not yet source-line justified.

\[
\boxed{\text{CRITICAL CONDITIONAL STEP.}}
\]

---

## 4. Why an unabsorbed \(O(S^{-1})\) per-cell factor matters

The source-slot bridge proves one low-\(u\) cell has \(O(1)\) source fast length and finite-\(S\) moving-frame/modal errors may integrate to

\[
O(S^{-1})
\]

on such an interval.

Since

\[
S_j\asymp(\log j)^2,
\]

an unabsorbed real multiplier

\[
1+c/S_j+o(S_j^{-1})
\]

cannot be treated as summable forcing:

\[
\sum_jS_j^{-1}
=
\infty.
\]

It must either

1. be absorbed into an exact frozen one-step monodromy;
2. be shown to be a connection rate multiplied by \(\Delta\sigma_j\); or
3. be proved skew / modulus-neutral by an exact identity.

The current chain has not yet established one of these alternatives for the complete buffer-inclusive transport.

---

## 5. Conservative repair

### Buffer-inclusive exact frozen section

Let

\[
\mathcal B^{in}_{S,p}(b),
\qquad
\mathcal B^{out}_{S,p}(b)
\]

be normalized unforced buffer flow maps of fast length \(b>0\), and define

\[
\boxed{
\mathscr P^{ext}_{S,p}
=
\mathcal B^{out}_{S,p}(b)
\circ
\mathscr P^{Gate1}_{S,p}
\circ
\mathcal B^{in}_{S,p}(b).
}
\tag{SL3}
\]

Choose \(b>0\) sufficiently small but fixed.

At \(b=0\), Gate 1 has an exact full-state fixed family and a transverse finite-dimensional solve. Smooth dependence of the physical buffer flow gives

\[
\mathcal B(b)=I+O(b)
\]

in the normalized fixed-order chart.

The natural target is therefore a buffer-inclusive exact family

\[
\boxed{
\mathscr P^{ext}_{S,p}
\mathscr S^{ext}_{S,b}(p,\Xi)
=
\mathscr S^{ext}_{S,b}(p,\Xi).
}
\tag{SL4}
\]

If this is proved, every frozen buffer multiplier is part of the exact local monodromy rather than a Gate 2 error.

### Slow characteristic connection

After (SL4), Gate 2 compares extended frozen sections at nearby slow points.

It is sufficient to prove

\[
\boxed{
\|\operatorname{Herm}\mathcal A_{c,S}\|
\le
C/S
+
CS^B(\varepsilon^{a_*}+e^{-cS}).
}
\tag{SL5}
\]

The stronger old estimate (SL2) is unnecessary.

Along the trapped spine,

\[
S(\sigma)\asymp\sigma^2,
\]

so

\[
\boxed{
\int_{\sigma_0}^{\infty}\frac{d\sigma}{S(\sigma)}
<\infty.
}
\tag{SL6}
\]

Equivalently,

\[
\sum_j\frac{\Delta\sigma_j}{S_j}
\asymp
\sum_j\frac1{j(\log j)^2}
<\infty.
\tag{SL7}
\]

Thus an \(O(S^{-1})\) **connection rate** is harmless even though an \(O(S^{-1})\) per-cell multiplier is not.

---

## 6. Corrected status

Until (SL4)--(SL5) are proved,

\[
\boxed{
\text{Gate 2 nonlinear invariant cocycle is CONDITIONAL.}
}
\]

Consequently the downstream Gate 3 construction is also conditional.

The safe status is

\[
\boxed{\text{Gate 1: strong branch theorem;}}
\]

\[
\boxed{\text{Gate 2: one monodromy repair remains;}}
\]

\[
\boxed{\text{Gate 3: downstream, not globally promotable.}}
\]

This supersedes earlier conversation-level statements that Gate 2 or Gate 3 was unconditionally closed.

---

## 7. Next targets and kill criterion

The next theorem targets are

1. **beta21_lowu_gate1_buffer_inclusive_exact_section.md**;
2. **beta21_lowu_gate2_within_stage_characteristic_monodromy.md**.

If the buffer-inclusive fixed family cannot be continued for any positive fixed buffer length, or if the slow connection has a nonintegrable positive Hermitian rate, the global infinite-cascade line must be frozen at Gate 1.

No final unforced singularity or Clay-prize claim is made here.
