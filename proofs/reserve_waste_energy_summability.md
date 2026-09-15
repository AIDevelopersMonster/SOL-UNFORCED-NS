# Energy summability of routed-away reserve descendants

**Status:** PROVED SCALE/ENERGY SUMMABILITY THEOREM FOR A FIXED FINITE NUMBER OF NORMALIZED PACKETS PER RELAY LEVEL, UNDER THE SOURCE SIMILARITY-SUPPORT AND PRIMARY-WAVE SCALINGS ALREADY USED IN THIS BRANCH. This theorem supports the `dirty reserve lane` architecture from `control_profile_map_definition_correction.md`.

It proves finite total `L^2` energy for reserve side-products that are generated forward, then routed permanently away from every future designated relay supernode. It does **not** assert uniform high-Sobolev bounds as `t up to 1`; such uniform bounds would be incompatible with the intended high-frequency cascade. For every fixed `t<1`, only finitely many sufficiently late relay levels have occurred, so smoothness before the accumulation time is a separate local-in-time issue.

## 1. Source height range

The source construction proves

\[
\boxed{
0<h\le \frac1{1000}.
}
\tag{RW1}

This is recorded in `NavierStokes/BaseWitnessClosure.lean` for the realized `ActualPrimary.h`.

Put

\[
A=\frac12+h,
\qquad
D=\frac12-h,
\qquad
\gamma=\frac{1+h}{2}.
\tag{RW2}

The branch cross-scale normalization gives the physical oscillatory carrier/amplitude law

\[
\boxed{
|U_{osc,j}|\lesssim q_j^{-\gamma}
}
\tag{RW3}

for every fixed normalized designated packet profile (up to design-dependent constants), while the source-native coefficient carries the square-root epsilon factor `epsilon_j^{1/2}=q_j^{h/2}`. This is the same physical scaling already used in the corrected two-channel small-log transfer theorem.

## 2. Physical support volume

On the trapped similarity annulus,

\[
r\asymp q^{1/2},
\qquad
z=q^D\eta,
\qquad D=\frac12-h.
\]

A packet whose normalized radial/axial support widths stay `O(1)` therefore has physical widths

\[
\Delta r\lesssim q^{1/2},
\qquad
\Delta z\lesssim q^D.
\]

In cylindrical coordinates the volume element is

\[
r\,dr\,d\theta\,dz.
\]

On the active annulus `r ~ q^{1/2}`, and the angular support has at most fixed `O(1)` size. Hence every fixed normalized packet lobe has physical volume

\[
\boxed{
|\operatorname{supp}W_j|
\lesssim
q_j^{1/2}\,q_j^{1/2}\,q_j^D
=
q_j^{1+D}
=
q_j^{3/2-h}.
}
\tag{RW4}

The same estimate holds for any fixed finite family of translated source lobes because translations do not change the scale exponents.

## 3. One-packet energy bound

Combine (RW3) and (RW4):

\[
\begin{aligned}
\|W_j\|_{L^2}^2
&\lesssim
|\operatorname{supp}W_j|\,
\|W_j\|_{L^\infty}^2\\
&\lesssim
q_j^{3/2-h}
q_j^{-2\gamma}.
\end{aligned}
\]

Since

\[
2\gamma=1+h,
\]

we obtain

\[
\boxed{
\|W_j\|_{L^2}^2
\lesssim
q_j^{1/2-2h}.
}
\tag{RW5}

By (RW1),

\[
\boxed{
\frac12-2h
\ge
\frac12-\frac2{1000}
=0.498>0.
}
\tag{RW6}

Thus the physical energy of one normalized packet tends to zero as the relay scale tends to zero even though its pointwise amplitude/frequency grows.

## 4. Fixed finite waste multiplicity

Suppose every relay cell creates at most `N_waste` routed-away reserve descendants, where

\[
N_{waste}<\infty
\]

is independent of level. Let their normalized amplitudes remain in one fixed bounded compact set, as is the case for any fixed finite source-action genealogy used only as reserve waste.

Then for a design constant `C_w`,

\[
\boxed{
E_j^{waste}
:=
\sum_{a=1}^{N_{waste}}
\|W_{j,a}\|_{L^2}^2
\le
C_w q_j^{1/2-2h}.
}
\tag{RW7}

No action cancellation is needed for this estimate. The only requirements are fixed finite multiplicity and bounded normalized amplitudes.

## 5. Geometric relay sequence

For

\[
q_j=q_0\vartheta^j,
\qquad 0<\vartheta<1,
\]

(RW7) gives

\[
E_j^{waste}
\le
C_w q_0^{1/2-2h}
\vartheta^{j(1/2-2h)}.
\]

Because the exponent is positive,

\[
\boxed{
\sum_{j=0}^\infty E_j^{waste}<\infty.
}
\tag{RW8}

Thus a fixed finite amount of routed-away normalized waste may be generated at every relay level without producing infinite total kinetic energy.

## 6. Why support routing matters

Energy summability alone does not make the waste dynamically irrelevant. We additionally impose the support condition:

\[
\boxed{
\operatorname{supp}W_{j,a}
\cap
\mathcal S_k^{relay}
=\varnothing
\quad\text{for all sufficiently later }k>j,
}
\tag{RW9}

where `S_k^{relay}` is the finite union of designated supernodes/corridors of later cells.

Under (RW9), the waste packets cannot participate in the finite leading collision graph that defines future renewal. They remain part of the exact PDE field and of the infinite stable/non-designated correction problem, but they do not become new relay-state coordinates.

The translated auxiliary-rectangle/support-separation machinery used throughout the finite-bank theorem supplies this kind of non-incidence condition for every **fixed finite** set of packets at one level. Global sparse packing must impose it recursively along the trapped spine.

## 7. Dirty reserve lanes

A reserve lane is therefore allowed to perform only the desired forward generation

\[
P-C_j\to D_j
\]

without solving an independent exact four-control cancellation problem for every side product.

The generated `D_j` is retained as a physical output lobe for the next unit-beta bank. Any finitely many companion descendants produced in the same reserve event are routed away from all future relay supernodes and counted in `E_j^{waste}`.

By (RW8) their total energy over the entire infinite cascade is finite.

This removes the recursive objection

\[
\text{`every reserve lobe needs its own four-profile exact-clean subbank'.}
\]

Exact active cancellation is required only in the small number of lanes that will themselves continue to collide on the singular relay spine.

## 8. Smoothness scope

A spatial derivative of order `m` costs powers of the growing physical carrier and therefore (RW8) is **not** a claim of a uniformly summable `H^m` tail as `t up to 1`.

For the desired blowup-type architecture this is not the relevant requirement. The correct requirements are:

1. one smooth finite-energy initial datum;
2. a smooth exact solution on every compact interval `[0,T]` with `T<1`;
3. possible divergence of high norms only as the accumulation time is approached.

Because relay levels accumulate only at `t=1`, every fixed `T<1` intersects only finitely many sufficiently late generated reserve levels. Thus the present energy theorem is compatible with, but does not by itself prove, the required pre-blowup smoothness.

## 9. Consequence for the lobe-bank frontier

The profile-renewal problem may now use a fixed finite physical unit-beta lobe bank with two kinds of lanes:

- **clean active lanes**, for which the exact entrance/strong-`H`/terminal cancellation theorems enforce designated exit traces;
- **dirty reserve lanes**, which merely generate the unit-beta lobes needed to replenish the next bank and route their finite side products permanently away from the relay circuit.

Because the dirty side products are energy-summable, they do not force recursive clean-control subbanks.

The remaining lobe-renewal obligation is therefore finite and geometric: choose a fixed number of incoming unit-beta lobes and show that one cell produces the same number of admissible outgoing unit-beta lobes, with enough profile nondegeneracy to realize the next cell's translated-control ranks.

No global unforced blowup theorem is claimed here.
