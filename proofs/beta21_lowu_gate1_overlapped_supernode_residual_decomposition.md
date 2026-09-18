# Gate 1A: exact residual algebra for one deliberately overlapped supernode

**Status:** PROVED ALGEBRAIC / SOURCE-COMPATIBILITY REDUCTION FOR A FINITE OVERLAPPED SUPERNODE.  THE PROOF DOES NOT USE THE PINNED SOURCE THEOREMS WHOSE HYPOTHESES REQUIRE PAIRWISE DISJOINT LABEL SUPPORT.  IT REPLACES THEM BY A DIRECT EXPANSION OF THE PHYSICAL NAVIER--STOKES RESIDUAL AND LOCAL SOURCE JET ESTIMATES.  OPERATOR-NORM, NORMAL-FORM, AND FIXED-POINT CLOSURE REMAIN SEPARATE GATE 1 OBLIGATIONS.

Pinned source:

\[
\texttt{openai/NavierStokesAndEuler@f9e8bc5b38b6e212696e8a30e3e91517af887bbd}.
\]

This theorem repairs the structural source-compatibility issue isolated as item H in

\[
\texttt{beta21_lowu_gate1_adversarial_reaudit.md}.
\]

The low-\(u\) relay intentionally allows a finite family of selected labels to overlap on one common physical/source collar.  Therefore one must **not** use source results whose assumptions include pairwise label disjointness, such as the standard extraction-regular decomposition for the original disjoint label architecture.

Instead we treat the complete finite overlapped family as one physical supernode field and expand its viscosity-one Navier--Stokes residual directly.

No exact reset theorem is claimed here.

---

## 1. Finite physical supernode

Let \(F\) be the finite set of internal supernode labels.

For each \(\alpha\in F\), let

\[
u_\alpha(t,x)
\]

be one actual smooth divergence-free physical velocity wave obtained from the already pinned local source realization, including its cutoff/curl reconstruction, and let

\[
p_\alpha(t,x)
\]

be its associated linear pressure contribution when present.

Let

\[
u_0,\qquad p_0
\]

denote the common smooth background/root/mean field about which the finite supernode is inserted.

Define

\[
\boxed{
u_F
=
u_0+\sum_{\alpha\in F}u_\alpha,
\qquad
p_F
=
p_0+\sum_{\alpha\in F}p_\alpha+p_F^{nl},
}
\tag{SA1}
\]

where \(p_F^{nl}\) denotes the pressure obtained from the whole-space Leray projection of the explicit nonlinear finite sum below.

Because \(F\) is finite, all differentiations and summations commute classically.

Because every \(u_\alpha\) and \(u_0\) are divergence free,

\[
\boxed{
\nabla\cdot u_F=0.
}
\tag{SA2}
\]

No support-disjointness is used in (SA1)--(SA2).

---

## 2. Literal physical residual identity

The pinned source defines the viscosity-one residual by

\[
\boxed{
\mathcal N(u,p)
=
\partial_tu+(u\cdot\nabla)u-\Delta u+\nabla p.
}
\tag{SA3}
\]

Put

\[
L(u,p)
:=
\partial_tu-\Delta u+\nabla p,
\]

and

\[
B(u,v)
:=
(u\cdot\nabla)v.
\]

Then

\[
\mathcal N(u,p)
=
L(u,p)+B(u,u).
\]

By linearity of \(L\) and bilinearity of \(B\),

\[
\begin{aligned}
\mathcal N(u_F,p_0+\sum_\alpha p_\alpha)
={}&
\mathcal N(u_0,p_0)\\
&+
\sum_{\alpha\in F}
\left[
L(u_\alpha,p_\alpha)
+B(u_0,u_\alpha)
+B(u_\alpha,u_0)
\right]\\
&+
\sum_{\alpha,\beta\in F}
B(u_\alpha,u_\beta).
\end{aligned}
\tag{SA4}
\]

Equation (SA4) is an exact finite algebraic identity.

In particular, for \(\alpha\ne\beta\), the term

\[
B(u_\alpha,u_\beta)
\]

is retained explicitly.

No theorem asserting that cross-label products vanish is invoked.

---

## 3. Whole-space projected form

Let \(\mathbb P\) be the whole-space Leray projector.

Since all velocities are divergence free, the projected evolution is

\[
\boxed{
\partial_tu_F-\Delta u_F
+
\mathbb P B(u_F,u_F)
=0
}
\tag{SA5}
\]

if and only if the projected finite residual vanishes.

Expanding,

\[
\begin{aligned}
\mathbb P\mathcal N_{vel}(u_F)
={}&
\mathbb P\mathcal N_{vel}(u_0)\\
&+
\sum_{\alpha\in F}
\mathbb P
\left[
(\partial_t-\Delta)u_\alpha
+B(u_0,u_\alpha)
+B(u_\alpha,u_0)
\right]\\
&+
\sum_{\alpha,\beta\in F}
\mathbb P B(u_\alpha,u_\beta).
\end{aligned}
\tag{SA6}
\]

The pressure \(p_F^{nl}\) is then recovered by the standard whole-space pressure/Leray relation.

The branch theorem
phase_adapted_whole_space_leray_intertwining.md
allows the same identity to be represented in the exact phase-adapted coefficient coordinates mode by mode.

Again no internal support-disjointness is needed.

---

## 4. Character addition for the finite cross terms

Suppose the \(\alpha\)-wave has oscillatory character \(K_\alpha\).

The local source wave realization has the form

\[
u_\alpha
=
a_\alpha e^{i\Theta_\alpha}
+
\overline{a_\alpha e^{i\Theta_\alpha}}
\]

after complexification.

A product of two positive-frequency components has character

\[
\boxed{
K_{\alpha\beta}
=
K_\alpha+K_\beta.
}
\tag{SA7}
\]

A product of one positive and one negative component has character

\[
\boxed{
K_{\alpha\bar\beta}
=
K_\alpha-K_\beta.
}
\tag{SA8}
\]

Thus every term in the finite double sum in (SA6) can be grouped by exact character addition.

For the low-\(u\) beta-\((2,1)\) orbit this reproduces, without any disjoint-support argument,

\[
C_j+C_k=Q_{j+k-1},
\]

\[
Q_n-C_j=C_{n-j+1},
\]

and

\[
C_j-C_k=(j-k)M.
\tag{SA9}
\]

The designated \(M\)-translation terms are selected explicitly; every other cross term is routed to the corresponding mean/nonzero complement according to its character.

---

## 5. Local jet estimates do not require label disjointness

The pinned source theorem

\[
\texttt{PhysicalResidualJetBounds.product\_jet\_bound\_local}
\]

states a local product derivative estimate for arbitrary smooth germs.

Likewise

\[
\texttt{PhysicalResidualJetBounds.mode\_jet\_bound\_local}
\]

controls one amplitude times one physical character.

Neither theorem assumes that two source labels have disjoint supports.

Therefore, for fixed derivative order \(m\), every retained cross term satisfies a local estimate of the form

\[
\boxed{
\|D^{\le m} B(u_\alpha,u_\beta)\|
\le
C_m
\|u_\alpha\|_{m+1}
\|u_\beta\|_{m+1}
}
\tag{SA10}
\]

in the corresponding physical/source local jet majorants.

After the already-audited source growth bookkeeping this becomes

\[
\boxed{
\|\mathbb P B(u_\alpha,u_\beta)\|_{X_m}
\le
C_mS^{A_m}
\|u_\alpha\|_{X_{m+c}}
\|u_\beta\|_{X_{m+1+c}},
}
\tag{SA11}
\]

provided one later chooses the explicit common norm and derivative index ledger required by Gate 1E.

Equation (SA11) is an estimate for a **present** cross term.  No cross term is discarded because of its label.

---

## 6. What source disjointness theorems are no longer used internally

Inside the supernode one must not invoke the following implications from the original source architecture:

- pairwise label-carrier disjointness;
- extraction regularity proved from that disjointness;
- diagonal reduction of products by disjoint padded slots;
- vanishing of cross-label curl products from disjoint supports.

In particular, the branch low-\(u\) proof must not use

\[
\texttt{ActualCycleResidualBounds.extraction\_regular}
\]

as the theorem that reconstructs the internal supernode residual.

The replacement is the direct finite expansion (SA4)--(SA8).

Outside the finite supernode, ordinary source labels/supernodes may still retain the original disjoint architecture.

---

## 7. Composite-supernode interpretation

Equivalently, one may regard the finite family \(F\) as one composite physical label

\[
\mathfrak S
=
\{u_\alpha:\alpha\in F\}.
\]

Its internal residual is defined by the exact finite formula (SA6).

The only disjointness required at the outer level is between the support of this **composite object** and unrelated source labels, if one wishes to reuse the original source finite-color assembly externally.

No claim is made that the pinned source already contains this composite-label theorem.  The branch is explicitly defining and proving the finite internal algebra itself.

---

## 8. Relation to covariance / mean output

The original source uses label disjointness in several covariance simplifications.

For the overlapped supernode those diagonal simplifications are not imported.

Instead, the mean output is the literal zero-character part of

\[
\sum_{\alpha,\beta\in F}
\mathbb P B(u_\alpha,u_\beta).
\tag{SA12}
\]

The weighted convolution theorem

\[
\texttt{beta21\_lowu\_orbit\_covariance\_weighted\_convolution.md}
\]

is to be interpreted as an estimate of this explicit sum, not as a reuse of a source theorem that first discards cross-label pairs.

This distinction is essential.

---

## 9. Exact scope of the repair

The structural disjointness gap of the Gate 1 audit is repaired at the algebraic level:

\[
\boxed{
\text{internal supernode overlap does not require source label-disjoint residual extraction;}
}
\]

\[
\boxed{
\text{the exact finite physical residual can be expanded directly and all cross terms retained.}
}
\tag{SA13}
\]

What this theorem does **not** yet prove:

1. a uniform finite-\(S\) normal form for the designated orbit;
2. the common Banach norm in which every term in (SA6) is controlled;
3. certified negative action margins for all non-designated terms;
4. the three-block tail/mean/nonzero contraction;
5. the final finite-dimensional reset solve.

Thus Gate 1A is closed as an algebraic/source-compatibility reduction, but Gate 1 as a whole remains open.

---

## 10. Updated Gate 1 order

After this repair the preferred order is

\[
\boxed{
\text{Gate 1A: finite overlapped residual algebra — CLOSED;}
}
\]

\[
\boxed{
\text{Gate 1B: exact finite-}S\text{ tangent normal form — OPEN;}
}
\]

\[
\boxed{
\text{Gate 1C: discrete profile / Fredholm repair — OPEN;}
}
\]

followed by the certified margins, derivative-index ledger, majorant three-block contraction, and finite-dimensional Lyapunov--Schmidt solve.

No downstream Gate 2 or Gate 3 theorem is re-promoted by this local repair alone.
