# Exact two-collar renewal state by a uniform implicit-function theorem

**Status:** PROVED EXACT LOCAL AUTONOMOUS TWO-COLLAR RENEWAL THEOREM IN THE BRANCH'S PHASE-ADAPTED REALIZATION. For every sufficiently high relay level and every slow parameter in a compact strict-cone set, the exact zero-residual two-event cell admits a nonzero regenerated beta-two/beta-one state with fixed magnitudes and freely reset phases. This theorem uses the uniform `C^1` comparison in `uniform_C1_two_collar_renewal_map.md` and the source-normalized nondegenerate coefficient field in `source_normalized_two_event_coefficients.md`.

It does **not** prove that such exact cells can yet be chained through infinitely many physical scales. The next obstruction is cross-`q` shadowing of the exact renewal section and global summability.

## 1. Principal magnitude map

Let

\[
a(p)=|\kappa_1^0(p)|,
\qquad
b(p)=|\kappa_2^0(p)|,
\]

with

\[
0<a_-\le a(p)\le a_+,
\qquad
0<b_-\le b(p)\le b_+.
\tag{ER1}
\]

The principal magnitude renewal map is

\[
\mathcal R^{{\rm mag}}_{0,p}(x,y)
=
\left(a(p)b(p)xy^2,\ a(p)xy\right).
\tag{ER2}
\]

Its nonzero fixed magnitude section is

\[
\boxed{
 x_0(p)=a(p)^{-1},
\qquad
 y_0(p)=[a(p)b(p)]^{-1/2}.
}
\tag{ER3}
\]

Define the fixed-point residual

\[
F_{0,p}(x,y)
:=\mathcal R^{{\rm mag}}_{0,p}(x,y)-(x,y).
\tag{ER4}
\]

Then

\[
F_{0,p}(x_0(p),y_0(p))=0.
\tag{ER5}
\]

A direct calculation gives

\[
D F_{0,p}(x_0,y_0)
=
\begin{pmatrix}
0&2a(p)b(p)x_0y_0\\
a(p)y_0&0
\end{pmatrix},
\tag{ER6}
\]

and therefore

\[
\boxed{
\det D F_{0,p}(x_0(p),y_0(p))=-2
}
\tag{ER7}
\]

for every `p`. Thus the inverse Jacobian is uniformly bounded over the compact slow set.

## 2. Exact map and smooth modulus coordinates

Let

\[
\mathscr R_{\ell,p}:\mathbb C^2\to\mathbb C^2
\]

be the exact two-collar zero-residual map from `uniform_C1_two_collar_renewal_map.md`.

Choose a compact neighborhood `K_A` of the principal renewal section that stays a fixed positive distance from either complex coordinate axis. Then the modulus map

\[
\Pi(z_2,z_1)=(|z_2|,|z_1|)
\]

is `C^1` on the corresponding phase-gauge slice. Use the two independent torus translation phases to gauge the incoming amplitudes to a fixed reference phase pair before taking magnitudes.

Define

\[
\mathcal R^{{\rm mag}}_{\ell,p}
:=\Pi\circ\mathscr R_{\ell,p}\circ\iota_p,
\tag{ER8}
\]

where `iota_p(x,y)` inserts the chosen reference phases. The phase gauge affects only the arguments of the complex amplitudes, not their magnitudes.

The uniform `C^1` theorem gives

\[
\boxed{
\sup_{p\in P}
\|\mathcal R^{{\rm mag}}_{\ell,p}
-\mathcal R^{{\rm mag}}_{0,p}\|_{C^1(K_{\rm mag})}
\to0.
}
\tag{ER9}
\]

## 3. Uniform implicit-function theorem

Define

\[
F_{\ell,p}(x,y)
:=\mathcal R^{{\rm mag}}_{\ell,p}(x,y)-(x,y).
\tag{ER10}
\]

By (ER9),

\[
F_{\ell,p}\to F_{0,p}
\]

uniformly in `C^1` on one fixed neighborhood of the compact section `(x_0(p),y_0(p))`.

Because the principal Jacobian determinant is exactly `-2`, compactness yields numbers

\[
r_*>0,\qquad C_*<\infty,
\]

such that the balls

\[
B_{r_*}(x_0(p),y_0(p))
\]

are all contained in the fixed positive quadrant neighborhood and

\[
\|D F_{0,p}(x_0(p),y_0(p))^{-1}\|\le C_*
\]

for every `p`.

For sufficiently large `ell`, the `C^1` error is so small that the quantitative implicit-function theorem applies uniformly. Therefore for every `p in P` there exists a unique exact fixed magnitude

\[
\boxed{
(x_{\ell}(p),y_{\ell}(p))
\in B_{r_*}(x_0(p),y_0(p))
}
\tag{ER11}
\]

satisfying

\[
\boxed{
\mathcal R^{{\rm mag}}_{\ell,p}
(x_\ell(p),y_\ell(p))
=(x_\ell(p),y_\ell(p)).
}
\tag{ER12}
\]

Moreover

\[
\boxed{
\sup_{p\in P}
\bigl(|x_\ell(p)-x_0(p)|+|y_\ell(p)-y_0(p)|\bigr)
\le C\Delta_\ell
\to0.
}
\tag{ER13}
\]

Since the principal section stays a fixed positive distance from zero, after increasing the starting level,

\[
\boxed{
0<c_0\le x_\ell(p),y_\ell(p)\le C_0<\infty
}
\tag{ER14}
\]

uniformly in `ell,p`.

## 4. Exact phase reset

The physical field is real after adding conjugate modes, but the two generator amplitudes carry two independent complex phases.

A translation by `c in T^2` sends

\[
A_j\mapsto e^{2\pi i e_j\cdot c}A_j,
\qquad j=1,2.
\tag{ER15}
\]

Since `e_1,e_2` form the integer character basis of the two-generator lattice, the two phases in (ER15) can be assigned independently.

Therefore, once the exact cell returns the magnitudes (ER12), choose the next supernode torus center so that the outgoing phase pair is reset exactly to the designated incoming reference phases. This operation changes neither the amplitude magnitudes nor the beta values nor the physical carrier magnitude.

Thus there exists, for every sufficiently high level and every admissible slow parameter, a nonzero complex input state

\[
\boxed{A_{\ell,p}^{\rm ren}\ne0}
\tag{ER16}
\]

such that the exact cell output is gauge-equivalent to the same normalized two-component state.

## 5. Exact local autonomous renewal theorem

Combining the exact zero-residual correction solve with Sections 1--4 gives:

### Theorem

For one frozen sufficiently large v0.8 design `M`, there exists `ell_0` such that for every `ell>=ell_0` and every `p in K_slow`, the exact unforced Navier--Stokes coefficient system on one two-event relay cell admits a real, divergence-free, zero-residual solution whose designated incoming state consists of one beta-two parent and one beta-one catalyst with magnitudes in the uniform compact range (ER14), and whose outgoing state regenerates the same two beta channels with exactly the same magnitudes after the permitted torus phase reset.

Equivalently,

\[
\boxed{
(\beta=2,\beta=1)
\longmapsto
(\beta=2,\beta=1)
}
\tag{ER17}
\]

is an **exact autonomous local renewal operation**, not only a principal envelope model.

The non-designated correction remains in the action-subcritical/mean-small outgoing class already controlled by the branch estimates.

## 6. What is not proved

This theorem is local in physical scale. It does not yet prove:

1. that the exact renewal state at level `ell` is carried by the physical Navier--Stokes evolution into the admissible incoming section of a smaller-`q` cell;
2. that the required next supernode can be placed along the same trapped material spine with all inherited tails uniformly small;
3. that infinitely many exact cells can be packed before `t=1` with convergent corrections away from the singular point;
4. that the resulting global field arises from one smooth finite-energy initial datum;
5. finite-time blowup for unforced 3D Navier--Stokes.

The sharp next theorem is a **cross-scale renewal-section shadowing theorem**.