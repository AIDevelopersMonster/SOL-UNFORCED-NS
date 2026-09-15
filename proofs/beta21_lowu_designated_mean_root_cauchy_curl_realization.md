# Cauchy/curl realization of the designated beta-zero mean root in the source-normalized whole-space chart

**Status:** PROVED LOCAL EXACT-DIVERGENCE-FREE CURL REDUCTION + UNIFORM SEMICLASSICAL ROOT-JET BUDGET / EXACT COMMON-COVER PHASE IDENTIFICATION STILL TO BE PINNED.  This revision removes an inapplicable shortcut: the source `primaryCurlRemainder` theorem assumes a nonzero harmonic, so it cannot be invoked directly for the angular-mean beta-zero root.  The needed estimate instead follows from the explicit curl construction below.

The low-`u` boundary-layer cell requires a pre-existing beta-zero mean root

\[
M=P-2C
\]

on the incoming physical Cauchy slice.  In the isotropically normalized whole-space chart its amplitude is `O(h)`, its covector is `O((hS)^{-1})`, and every non-principal coefficient derivative gains an additional factor `h`.  Thus the normalized transport coefficient `M_des/h` has uniformly bounded semiclassical jets; all positive-order principal jets are actually `O(S^{-1})` or smaller.

No exact reset cell or global cascade is claimed here.

## 1. Whole-space normalized chart

Let

\[
h:=\sqrt\varepsilon,
\qquad
 y=\frac{x-x_0}{\sqrt Q}.
\]

For physical velocity `u_phys`, write the source-normalized representative

\[
\widetilde u(y)=Q^A u_{phys}(x_0+\sqrt Q\,y).
\]

The source carrier normalization gives

\[
\boxed{h\,kB_s\asymp1.}
\tag{CR1}
\]

The natural semiclassical derivative is therefore

\[
\boxed{D_h:=h\nabla_y=h\sqrt Q\,\nabla_x.}
\tag{CR2}
\]

The dilation maps `R^3` onto `R^3`; no artificial boundary is introduced.

## 2. Exact root phase

Define the root phase by the exact character relation

\[
\boxed{\Theta_M:=\Theta_P-2\Theta_C.}
\tag{CR3}
\]

and in normalized coordinates

\[
\widetilde\Theta_M(y)=\Theta_M(x_0+\sqrt Q\,y),
\qquad
\Xi_M:=\nabla_y\widetilde\Theta_M.
\]

The angular coefficient cancels because `beta(P)-2 beta(C)=0`.  At the boundary-layer scale

\[
\delta_S=\kappa/S
\]

the remaining radial/normal mismatch is a fixed nonzero multiple of `delta_S`.  Hence on a strict core the exact finite-`S` coefficients have the target two-sided estimate

\[
\boxed{
\frac{c_-}{S}
\le h|\Xi_M|
\le\frac{c_+}{S}
}
\tag{CR4}
\]

for fixed positive `c_-,c_+`.  Equivalently,

\[
\boxed{|\Xi_M|\asymp(hS)^{-1}.}
\tag{CR5}
\]

Pinning the constants in (CR4) to the exact common-cover phase formula remains a source-notation task; the scaling follows directly from (CR1) and the exact character slope separation.

## 3. Transverse root polarization

The frozen beta-zero polarization is

\[
\boxed{b_M=-S_MK+c_0R_MN}
\tag{CR6}
\]

with no radial component, while the beta-zero phase normal is radial.  Thus `b_M dot Xi_M=0` at principal order.  On the strict core choose its exact smooth transverse projection

\[
\widetilde b_M\cdot\Xi_M=0.
\tag{CR7}
\]

The projection changes the frozen vector only by the allowed finite-`S`/slow-frame error.

## 4. Exact curl and physical Cauchy field

Choose a normalized source-admissible cutoff `chi(y)` equal to one on the orbit core and let `a_M` be the normalized complex root amplitude.  Define

\[
\boxed{
\widetilde A_M
=
\chi
\frac{h a_M}{i|\Xi_M|^2}
(\Xi_M\times\widetilde b_M)
 e^{i\widetilde\Theta_M}.
}
\tag{CR8}

Set

\[
\boxed{
\widetilde M_{des}=2\Re(\nabla_y\times\widetilde A_M).
}
\tag{CR9}

Then

\[
\boxed{\nabla_y\cdot\widetilde M_{des}=0}
\tag{CR10}
\]

exactly.

Pull back to the physical slice by

\[
M_{des}^{phys}(x)
=Q^{-A}
\widetilde M_{des}
\left(\frac{x-x_0}{\sqrt Q}\right).
\tag{CR11}
\]

Isotropic dilation preserves zero divergence, so this is honest divergence-free Cauchy data, not a future-time control.

## 5. Principal term and direct localization remainder

When the curl hits the exponential,

\[
\nabla_y e^{i\widetilde\Theta_M}=i\Xi_Me^{i\widetilde\Theta_M}.
\]

Using transversality,

\[
\Xi\times(\Xi\times b)=-|\Xi|^2b.
\]

Hence

\[
\boxed{
\nabla_y\times\widetilde A_M
=
\chi h a_M\widetilde b_Me^{i\widetilde\Theta_M}
+R_M^{curl}.
}
\tag{CR12}
\]

The vector-potential prefactor is

\[
\frac{h}{|\Xi_M|}
\asymp h^2S.
\]

A derivative falling on the normalized cutoff, frame or polarization therefore gives

\[
\boxed{
\|R_M^{curl}\|_\infty
\le Ch^2S\,\operatorname{poly}(S).
}
\tag{CR13}
\]

Thus

\[
\boxed{
\widetilde M_{des}
=h a_M\widetilde b_Me^{i\widetilde\Theta_M}
+O(h^2S\,\operatorname{poly}(S))
}
\tag{CR14}
\]

on the interaction core, and the relative error is

\[
\boxed{hS\,\operatorname{poly}(S)=o(1).}
\tag{CR15}
\]

## 6. Sharpened semiclassical jets

The key point is that the crude statement `h poly(S)` is not the correct bound for positive-order derivatives of the normalized coefficient.

For the principal term, every `D_h` derivative hitting the phase contributes

\[
h\Xi_M=O(S^{-1}).
\]

If a `D_h` derivative hits a normalized cutoff/frame/polarization coefficient, it contributes an **additional factor `h`** times a fixed-order source-polynomial jet.  Hence, for every fixed `a>=1`,

\[
\boxed{
\|D_h^a\widetilde M_{des}\|_\infty
\le
C_a h
\left[
S^{-a}+h\,\operatorname{poly}(S)
\right].
}
\tag{CR16}
\]

At order zero,

\[
\boxed{
\|\widetilde M_{des}\|_\infty
\le Ch[1+o(1)].
}
\tag{CR17}
\]

Equivalently, for the transport coefficient

\[
V_M:=\widetilde M_{des}/h,
\]

we have

\[
\boxed{
\|V_M\|_\infty\le C,
}
\tag{CR18}
\]

and for every fixed `a>=1`,

\[
\boxed{
\|D_h^aV_M\|_\infty
\le
C_a\left[S^{-a}+h\,\operatorname{poly}(S)\right]
=o(1)+O(S^{-a}).
}
\tag{CR19}
\]

This is the uniform coefficient estimate needed for the root-augmented Oseen generator.  No `exp(poly(S))` Gronwall factor is forced by the root.

## 7. Why the published nonzero-harmonic curl theorem is not used

The source theorem `PrimaryPulseBounds.primaryCurlRemainder_class` is derived from `CurlClassBounds.normalCurlRemainder_class` under the hypothesis

\[
\texttt{harmonic n != 0}.
\]

Our root has zero angular harmonic.  Therefore that theorem cannot be cited directly for (CR13)--(CR19).

The estimates here instead use the explicit exact curl (CR8)--(CR12).  This is sufficient because the root still has a nonzero radial reconstructed covector (CR4), even though its angular frequency is zero.

## 8. Principal self-advection and viscosity

The transverse principal wave satisfies

\[
\Pi_{principal}\mathcal B(M_{des},M_{des})=0,
\tag{CR20}
\]

including the conjugate zero-frequency cross term.

Also

\[
|\Xi_M|^2\asymp(h^2S^2)^{-1},
\]

so the normalized viscous rate is

\[
\boxed{
\varepsilon|\Xi_M|^2
=h^2|\Xi_M|^2
\asymp S^{-2}.
}
\tag{CR21}
\]

Across one `O(1)` boundary-layer collar the principal root therefore persists with multiplier

\[
\boxed{1+O(S^{-2}).}
\tag{CR22}
\]

## 9. Remaining exact source obligations

The direct curl removes the nonzero-harmonic applicability issue.  The remaining source tasks are now narrow:

1. pin the exact common-cover formula for `Theta_M=Theta_P-2Theta_C`;
2. prove the two-sided normalized covector bound (CR4) with explicit constants at `u=1.8`, `x=0.70`, `kappa=kappa_*`;
3. identify `chi` with an admissible normalized source cutoff whose fixed-order `y`-jets satisfy the source polynomial bounds used above;
4. carry (CR19) into the whole-space root-augmented mean propagator.

## 10. Consequence

The designated beta-zero mean root has an exact divergence-free Cauchy realization and, in the correct source-normalized whole-space chart,

\[
\boxed{
\widetilde M_{des}/h=O(1),
\qquad
D_h^a(\widetilde M_{des}/h)
=O(S^{-a})+o(1)\quad(a\ge1).
}
\]

Thus its fast physical oscillation does **not** generate a large coefficient constant in the semiclassical Oseen problem.  The next step is to use (CR18)--(CR19) in the projected whole-space mean equation and then couple that solve to the nonzero orbit block.
