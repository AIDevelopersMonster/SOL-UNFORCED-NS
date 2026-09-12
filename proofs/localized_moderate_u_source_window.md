# Localized moderate-`u_*` source-safe window near the stress edges

**Status:** PROVED SOURCE-FRAME LOCAL SAFE-REGION THEOREM / DERIVED FINITE-PALETTE REDUCTION. The global cone audit in `source_cone_moderate_u_compatibility_audit.md` asked for a numerical bound on the full-annulus supremum of the Section 7 cone ratio. That global bound is unnecessary if the autonomous relay labels are confined to a source-safe subregion. The source itself proves that the phase cone ratio tends to **zero** at both radial stress edges. Consequently every fixed finite value `u_0>0`, in particular the cleanup value `u_0=4`, is admissible on a sufficiently short but fixed inner (and outer) radial collar.

This removes the **local source-cone obstruction** to the moderate-`u_*` cleanup design. It does **not** yet prove an infinite relay: the child must still be routed from cell to cell while remaining in a safe region, and the finite-palette modification of Sections 7--9 requires a downstream uniformity audit.

Primary source: OpenAI, *Finite Time Blowup for Navier--Stokes*, Theorem 4.6(iii), Proposition B.5 / (B.30), Lemma C.1, Proposition C.2, Proposition C.3, and equations (7.1)--(7.3).

## 1. The local Section 7 cone ratio

For `X_a<X<X_b`, write

\[
 n=\frac{T_0}{|T_0|}
\]

for the unit leading-stress direction, and use the source shear variables `t_s,v_s`. The Section 7 frame satisfies

\[
 c_0^2=\frac{v_s-2}{2}.
\]

By the identities immediately following source (7.1), the phase cone ratio is

\[
\boxed{
\mathcal R(X,\eta)
:=
\left|
 c_0\frac{T_0\cdot K}{T_0\cdot N}
\right|
=
\sqrt{\frac{v_s-2}{2}}
\left|
\frac{n_z-t_sn_\theta}{n_\theta+t_sn_z}
\right|.
}
\tag{LM1}
\]

The Section 7 packet parameter `u_*>0` is admissible at a representative whenever

\[
\boxed{
\mathcal R(X,\eta)
<
\vartheta(u_*):=\frac{u_*}{\sqrt{1+u_*^2}}.
}
\tag{LM2}
\]

The published proof takes one `u_*` large enough for the supremum over the whole annulus. For a relay occupying only a fixed subregion, only the local version (LM2) is needed at its representatives.

## 2. Exact zero of the cone ratio at the inner stress edge

Proposition B.5 proves the flat factorization

\[
T_0=e_a B_0,
\qquad
B_0(0,\eta)\ne0,
\tag{LM3}
\]

at the inner radial edge. Proposition C.3 then identifies the limiting unit stress direction as a positive scalar multiple of the limiting shear:

\[
 n(X_a,\eta)\parallel(1,t_s(X_a,\eta)).
\tag{LM4}
\]

Equivalently, uniformly for `-1<=eta<=1`,

\[
\boxed{
 n_z-t_sn_\theta=0
\quad\text{at }X=X_a,
}
\tag{LM5}
\]

while

\[
 n_\theta+t_sn_z>0.
\tag{LM6}
\]

The same edge construction has `v_s>2+c` and all relevant normalized frame quantities extend smoothly to the closed edge. Therefore (LM1) has the continuous edge value

\[
\boxed{
\mathcal R(X_a,\eta)=0
\qquad(-1\le\eta\le1).
}
\tag{LM7}
\]

This is stronger than merely knowing `mathcal R<1`.

## 3. Uniform fixed-width moderate-`u` collar

Fix **any** number

\[
u_0>0.
\]

Then

\[
\vartheta_0:=\vartheta(u_0)>0.
\]

By (LM7), continuity of `mathcal R` on the closed annulus with the source edge interpretation, and compactness of `[-1,1]`, there exists

\[
\boxed{\rho(u_0)>0}
\tag{LM8}
\]

such that

\[
\boxed{
\mathcal R(X,\eta)<\vartheta_0
\quad
\text{for }
X_a\le X\le X_a+\rho(u_0),
\ -1\le\eta\le1.
}
\tag{LM9}
\]

Thus every slow-box representative in this collar admits the Section 7 phase construction with the **fixed value** `u_*=u_0`.

In particular, for the cleanup choice

\[
\boxed{u_0=4,\qquad \vartheta_0=4/\sqrt{17}\approx0.9701425,}
\tag{LM10}
\]

there is a fixed nonempty inner collar on which `u_*=4` is source-certified without any numerical lower bound on the global Theorem 4.6 constant `kappa`.

### Nondegenerate interior slab

Because Theorem 4.6 says `T_0` is nonzero throughout the open annulus, choose for example

\[
\mathcal S_{u_0}
:=
[X_a+\rho(u_0)/3,\ X_a+2\rho(u_0)/3]\times[-1,1].
\tag{LM11}
\]

This compact slab lies strictly inside the active annulus. Hence `|T_0|` has a positive minimum there. The positive frame/growth quantities in Theorem 4.6(iii), including the quantity defining `lambda_0`, also have positive lower bounds. Therefore using `u_*=u_0` on `mathcal S_{u_0}` is not a degenerate zero-stress edge limit: the packet amplitudes and frame constants remain finite and uniformly nonzero.

## 4. The outer edge has the same local property

Proposition C.3 gives at the outer radial edge

\[
 n(X_b,\eta)=(1,0),
\qquad
t_s(X_b,\eta)=0.
\tag{LM12}
\]

Hence again

\[
 n_z-t_sn_\theta=0,
\]

and therefore

\[
\boxed{\mathcal R(X_b,\eta)=0.}
\tag{LM13}
\]

The same compactness argument yields, for every fixed `u_0>0`, a fixed outer source-safe collar

\[
X_b-\rho_b(u_0)\le X\le X_b.
\tag{LM14}
\]

Thus moderate `u_*` is not a rare point phenomenon: both stress edges furnish open safe regions.

## 5. An explicit bound inside the variance-modified cone states

Appendix C gives an independent quantitative observation. In Lemma C.1 put

\[
P=P_c(t),\qquad J=J_c(t).
\]

For fixed `(P,J)`, the upper admissible shear strength `U(P,J)>2` is the smaller root of

\[
\boxed{
2(P-U)^2=(U-2)J^2.
}
\tag{LM15}
\]

The construction chooses `delta_L>0` so that

\[
U>2+\delta_L,
\tag{LM16}
\]

and wherever the variance cutoff is nonzero it has

\[
2<v\le v_*:=2+\frac{\delta_L}{2}.
\tag{LM17}
\]

For such a cone state the Section 7 ratio squared is

\[
\boxed{
\mathcal R_v^2
=
\frac{(v-2)J^2}{2(P-v)^2}.
}
\tag{LM18}
\]

For `2<v<P` the right side is strictly increasing in `v`. From (LM16)--(LM17),

\[
v<\frac{U+2}{2}.
\]

Consequently

\[
\begin{aligned}
\mathcal R_v^2
&<
\frac{((U+2)/2-2)J^2}
{2(P-(U+2)/2)^2}\\
&=
\frac{(U-2)J^2}
{4(P-(U+2)/2)^2}\\
&=
\frac{(P-U)^2}
{2(P-(U+2)/2)^2}
<\frac12,
\end{aligned}
\tag{LM19}
\]

where the penultimate equality uses (LM15). Hence the ideal cone states of Lemma C.1 satisfy

\[
\boxed{
\mathcal R_v<\frac1{\sqrt2}
}
\tag{LM20}
\]

wherever the variance cutoff is active.

Since

\[
\frac1{\sqrt2}<\frac4{\sqrt{17}},
\]

`u_*=4` has a very large cone margin on those ideal states. Proposition C.2 realizes the loop by a finite high radial frequency `N`, with the actual shear and stress data converging to the loop data at the required fixed parameter orders. Thus, after taking `N` sufficiently large in the source hierarchy, the strict `u_*=4` inequality persists on every compact subset on which this variance-modified regime is active.

This is an additional safe-region mechanism; the edge-collar theorem in Sections 2--4 does not depend on it.

## 6. Derived finite-palette reduction

The source chooses one global `u_*` before (7.2) to make all label estimates uniform. At the algebraic phase-construction level, however, `u_*` enters the label data through

\[
B_s^2
=
\frac{\lambda_0}
{\varepsilon k^2(1+u_*^2)^{3/2}},
\qquad
s(v)=\sigma\left(\frac{u_*}{2}+\frac{u_*v}{L_s}\right),
\tag{LM21}
\]

and the wave numbers are then frozen constants for that label. No slow or auxiliary derivative differentiates `u_*` itself.

Therefore the following **finite-palette reduction** is available at the phase-definition and fixed-finite-stage estimate level:

- use `u_\gamma=4` for the relay supernode labels whose slow boxes lie in a compact source-safe slab such as (LM11);
- retain a source-global admissible value `u_{hi}` for generic labels elsewhere;
- take uniform constants as maxima/minima over the finite palette `{4,u_hi}`.

Because the palette is finite and bounded away from zero and infinity, every explicit smooth algebraic factor of `u_\gamma` in the phase, frame, amplitude, and fixed finite derivative estimates has uniform bounds.

**Scope of this reduction.** The published Sections 7--9 were written with one common global `u_*`. A full publication-level theorem with a label-dependent finite palette therefore still requires a line-by-line downstream audit, especially at common-torus relabeling, harmonic interaction, and correction stages. The present result proves that there is no local cone or differentiation obstruction to that audit; it does not silently replace it.

## 7. What this resolves

The previous global audit left the moderate cleanup mechanism conditional on an unknown full-annulus number such as

\[
R_*<4/\sqrt{17}.
\]

For a localized relay this condition is unnecessary. We now have the unconditional source-derived statement

\[
\boxed{
\exists\ \text{fixed nonempty active radial slab on which }u_*=4
\text{ satisfies the exact Section 7 cone condition uniformly in }\eta.
}
\tag{LM22}
\]

Combining this with `beta21_finite_u_cleanup_window.md` shows that the same moderate value `u_*=4` can simultaneously satisfy, at the exact-source envelope level,

\[
\boxed{
\text{finite-}u\text{ relay/reset/cleanup equations}
\quad+\quad
\text{the source phase cone condition on a nondegenerate active region}.
}
\tag{LM23}
\]

This closes the **local source-cone barrier** identified in the preceding audit.

## 8. New sharp global barrier

The unresolved issue is now geometric transport, not the local phase cone.

`profile_characteristic_trapped_spine.md` proves that the leading background has at least one stationary similarity point

\[
W=H_c=0
\]

somewhere in the active annulus, yielding a trapped physical characteristic. That theorem does **not** locate the stationary point inside either moderate-`u` source-safe collar. Conversely, the source-safe edge collars are not known to be invariant under the material flow.

Therefore the next global question is

\[
\boxed{
\text{Can a repeatable relay spine be kept inside a moderate-}u\text{ safe set?}
}
\tag{LM24}
\]

A sufficient next theorem would be either:

1. locate or force a simultaneous zero `W=H_c=0` in a region where `mathcal R<4/sqrt(17)`; or
2. construct a source-compatible cross-scale routing map whose relay representatives return to the safe slab each cell while preserving the renewed pair.

Until one of these is proved, the local moderate-`u` source obstruction is closed, but the infinite autonomous cascade remains open.