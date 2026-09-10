# Analytic lattice bound for the localized Navier-Stokes quadratic symbol

**Status:** PROVED ABSTRACT-PACKET BILINEAR LEMMA / SOURCE-EMBEDDED SYMBOL BOUND. Under the packet seminorm and one-output-carrier structure already used in Lemma 9.2 of the source calculation, the full quadratic lattice convolution loses at most one power of the output harmonic index. Combined with the quadratic high-mode smoothing from `finite_critical_block_uniform_stable_inverse.md`, the nonlinear stable-complement map is bounded on an analytic weighted `l^1` lattice space.

This theorem still does not solve the finite critical compatibility block.

## 1. Weighted packet space

Let

\[
\nu=(a,b)\in\mathbb Z^2,
\qquad
|\nu|:=|a|+|b|.
\]

Fix `sigma>0` and define

\[
\boxed{
\|z\|_{\mathfrak A_\sigma}
:=
\sum_{\nu\in\mathbb Z^2}
 e^{\sigma|\nu|}
 (1+|\nu|)
 \|z_\nu\|_{\rm pkt}.
}
\tag{Q1}
\]

The packet seminorm contains the fixed finite family of slow derivatives used in the local relay theorem and the source-localized action weight from `source_localized_action_preservation.md`.

The exponential factor is submultiplicative:

\[
e^{\sigma|\nu+\mu|}
\le
 e^{\sigma|\nu|}e^{\sigma|\mu|}.
\tag{Q2}
\]

Also

\[
1+|\nu+\mu|
\le
(1+|\nu|)+(1+|\mu|).
\tag{Q3}
\]

## 2. One-output-carrier structure

Write the localized Navier-Stokes bilinear term schematically as

\[
\mathcal B(z,w)
=\mathbb P[(z\cdot\nabla)w+(w\cdot\nabla)z].
\]

After decomposing into lattice phases, the coefficient at output index

\[
\kappa=\nu+\mu
\]

has the form

\[
\mathcal B_\kappa(z,w)
=
\sum_{\nu+\mu=\kappa}
\mathcal M(\kappa;\nu,\mu)
[z_\nu,w_\mu].
\]

The source wave-wave calculation and exact incompressibility eliminate the naively worst derivative loss: one may take

\[
\boxed{
\|\mathcal M(\kappa;\nu,\mu)[z_\nu,w_\mu]\|_{\rm pkt}
\le
C_M(1+|\kappa|)
\|z_\nu\|_{\rm pkt}
\|w_\mu\|_{\rm pkt}.
}
\tag{Q4}
\]

The constant depends on the frozen v0.8 design, fixed packet derivative order, and compact relay collar, but not on the lattice indices or correction stage.

This is the lattice version of the one-output-carrier factor left after the Lemma 9.2 incompressibility cancellation.

## 3. Bilinear estimate before inversion

Multiply (Q4) by the exponential output weight and use (Q2):

\[
\begin{aligned}
&e^{\sigma|\kappa|}
\|\mathcal B_\kappa(z,w)\|_{\rm pkt}\\
&\le
C_M
\sum_{\nu+\mu=\kappa}
 e^{\sigma|\nu|}e^{\sigma|\mu|}
(1+|\kappa|)
\|z_\nu\|_{\rm pkt}
\|w_\mu\|_{\rm pkt}.
\end{aligned}
\]

Using (Q3),

\[
1+|\kappa|
\le
(1+|\nu|)+(1+|\mu|),
\]

and summing over `kappa` gives

\[
\boxed{
\|\mathcal B(z,w)\|_{\mathfrak A_\sigma^{(0)}}
\le
2C_M
\|z\|_{\mathfrak A_\sigma}
\|w\|_{\mathfrak A_\sigma},
}
\tag{Q5}
\]

where `A_sigma^(0)` denotes the same exponential `l^1` norm without the extra factor `(1+|kappa|)`.

Thus the quadratic nonlinearity loses at most one lattice derivative.

## 4. Stable inverse restores two lattice derivatives

From `finite_critical_block_uniform_stable_inverse.md`, for every stable-complement mode

\[
\boxed{
\|G_\kappa f_\kappa\|_{\rm pkt}
\le
\frac{C_M}{1+|\kappa|^2}
\|f_\kappa\|_{\rm pkt}.
}
\tag{Q6}
\]

Therefore

\[
(1+|\kappa|)
\|G_\kappa f_\kappa\|_{\rm pkt}
\le
C_M\|f_\kappa\|_{\rm pkt}.
\]

After summation,

\[
\boxed{
\|\mathcal G_S f\|_{\mathfrak A_\sigma}
\le
C_M
\|f\|_{\mathfrak A_\sigma^{(0)}}.
}
\tag{Q7}
\]

Combining (Q5) and (Q7),

\[
\boxed{
\|\mathcal G_S\mathcal B(z,w)\|_{\mathfrak A_\sigma}
\le
C_M
\|z\|_{\mathfrak A_\sigma}
\|w\|_{\mathfrak A_\sigma}.
}
\tag{Q8}
\]

Hence the infinite stable complement is closed under the nonlinear correction map.

## 5. Lipschitz estimate

By bilinearity,

\[
\mathcal B(z,z)-\mathcal B(\widetilde z,\widetilde z)
=
\mathcal B(z-\widetilde z,z)
+
\mathcal B(\widetilde z,z-\widetilde z).
\]

Using (Q8),

\[
\boxed{
\|\mathcal G_S[\mathcal B(z,z)-\mathcal B(\widetilde z,\widetilde z)]\|_{\mathfrak A_\sigma}
\le
C_M
(\|z\|_{\mathfrak A_\sigma}+\|\widetilde z\|_{\mathfrak A_\sigma})
\|z-\widetilde z\|_{\mathfrak A_\sigma}.
}
\tag{Q9}
\]

Therefore on a ball of radius `R`, the quadratic stable-complement map has contraction constant at most `2C_M R`.

## 6. Interaction with the action weight

The packet seminorm in (Q1) may be multiplied modewise by the v0.8 action renormalization. `source_localized_action_preservation.md` proves that every non-designated genealogy retains a fixed factor `e^{-c_M S_*}` under the localized finite-stage operations.

Because genealogical source actions add under products, the renormalized weights are submultiplicative in exactly the same sense as the exponential lattice weight. Thus the estimates (Q5)–(Q9) remain valid with the action factor included, with only a design-dependent constant.

Consequently the small forcing produced by all non-designated action-subcritical descendants has norm

\[
\boxed{
\|F_{\rm flat}\|_{\mathfrak A_\sigma^{(0)}}
\le
C_M S_*^{C_M}e^{-c_M S_*}.
}
\tag{Q10}
\]

Applying the stable inverse,

\[
\boxed{
\|\mathcal G_SF_{\rm flat}\|_{\mathfrak A_\sigma}
\le
C_M S_*^{C_M}e^{-c_M S_*}.
}
\tag{Q11}
\]

This tends to zero faster than every algebraic dyadic scale.

## 7. Stable-complement contraction

Let

\[
\rho_\ell:=C_M S_*^{C_M}e^{-c_M S_*}.
\]

For sufficiently large `ell`, choose the ball

\[
B_{2\rho_\ell}
\subset\mathfrak A_\sigma.
\]

The map

\[
\mathcal T_S(z)
=
-\mathcal G_S\big(F_{\rm flat}+\mathcal B(z,z)+\mathcal B(z,U_{\rm crit})\big)
\]

is contractive provided the finite critical component `U_crit` has already been chosen so that its non-designated output enters only at the same action-subcritical size. In particular, if

\[
\|U_{\rm crit}\|_{\mathfrak A_\sigma}\le C\rho_\ell,
\]

then for large `ell`

\[
\boxed{
\mathcal T_S(B_{2\rho_\ell})\subset B_{2\rho_\ell},
\qquad
\operatorname{Lip}(\mathcal T_S)<\frac12.
}
\tag{Q12}
\]

Thus the **infinite-dimensional stable complement is no longer the obstruction**.

## 8. Remaining finite-dimensional problem

The only unresolved local zero-force step is now the finite critical block from `finite_critical_block_uniform_stable_inverse.md`.

Let

\[
\mathfrak X_{\rm crit}
=\operatorname{span}\{\nu_1,\dots,\nu_N\}.
\]

Exact compact support produces a finite family of compatibility moments

\[
\mathcal M_j(p,Z)=0,
\qquad j=1,\dots,N_c.
\]

If a finite set of internal collar amplitudes/phases `p=(p_1,...,p_{N_c})` can be chosen with

\[
\det D_p\mathcal M\ne0,
\]

then the implicit-function theorem solves the critical block, after which (Q12) closes the stable infinite-dimensional complement by contraction.

Therefore the next theorem-level target is a **multi-collar finite critical transversality theorem**.
