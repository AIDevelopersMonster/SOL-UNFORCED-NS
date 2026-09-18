# Finite-`S` profile normal form coefficients for the low-`u` orbit

**Status:** SUPERSEDED IN ITS ONE-SIDED NORMAL FORM. THE REAL DESIGNATED ROOT GENERATES BOTH FORWARD AND BACKWARD ORBIT SHIFTS, SO THE COEFFICIENTS `v_b,B_b` BELOW ARE NOT THE CURRENT REAL-ROOT VALUES. SEE `beta21_lowu_real_root_bidirectional_principal_reset.md`. THE PHYSICAL ACTION CURVATURE CALCULATION REMAINS REUSABLE.

This note continues `beta21_lowu_finiteS_designated_profile_obligation.md` after the single-root compatibility correction in `beta21_lowu_single_root_coupling_ratio.md`.

The tuned beta-zero Cauchy root has a boundary-layer polarization whose `K` component is `O(S^{-1})`.  This makes the beta-one and beta-two root-shift couplings simultaneously compatible with the limiting dispersion point.  The first variation of those couplings across the central orbit window produces the affine multiplication term in the continuum fixed-profile operator

\[
\mathcal L_b=v_b\partial_y+B_by+C_b.
\]

The main result here is that the explicitly computed `B_b` does **not** destroy physical large-deviation localization.  In both sectors the physical action Gaussian has a substantial margin over the coefficient-profile anti-Gaussian drift.

No exact discrete finite-`S` profile is claimed yet.

## 1. Working constants

Use

\[
u=1.8,
\qquad
x=0.70,
\qquad
\kappa_*=0.894049167184884\ldots.
\]

The limiting orbit data are

\[
\rho_C=0.3510126502440001\ldots,
\]

\[
\rho_P=-2.147691668824314
+1.235899139340218\,i,
\]

\[
\lambda_C=-2.982607649202283\ldots,
\]

\[
\mu_P=-0.845013757547658\ldots.
\]

Let

\[
T_*:=2\kappa_*
=1.788098334369768\ldots.
\tag{PN1}
\]

The limiting shift-generator strengths are therefore

\[
\boxed{
a_{C,0}:=\lambda_C/T_*
=-1.668033346864858\ldots,}
\tag{PN2}
\]

\[
\boxed{
a_{P,0}:=\mu_P/T_*
=-0.472576782442723\ldots.}
\tag{PN3}

## 2. Tuned single-root polarization

Let

\[
L_x:=\sqrt{1+x^2}
=1.220655561573370\ldots.
\]

The source-frame beta-two/beta-one ratio is

\[
R_*:=\mu_P/\lambda_C
=0.2833137498905236\ldots.
\]

The polarization theorem gives

\[
\tau_*
=\frac{1-R_*}{2(R_*-2)}
=-0.2087411867089201\ldots.
\tag{PN4}
\]

At finite `S`, write the root radial phase increment as

\[
m_S=2\kappa_S/S
\]

and choose

\[
k_S=\frac{m_Sr}{L_x}\tau_S,
\qquad
\tau_S=\tau_*+O(S^{-1}).
\]

The growing root-shift coefficient derived in `beta21_lowu_single_root_coupling_ratio.md` is

\[
A_b^+(s)
=
\frac{m_Sr}{2}
\left[
\frac{2b\tau_*}{L_x}
+\frac1{\sqrt{1+s^2}}
\right]
+O(m_S^2)+O(m_S|s-x|^2)
\tag{PN5}
\]

on the central profile window.  The displayed formula is sufficient for the first slope derivative.

## 3. Common first slope derivative

Define

\[
F_b(s)
:=
\frac{b\tau_*}{L_x}
+\frac1{2\sqrt{1+s^2}}.
\tag{PN6}

Then

\[
A_b^+(s)=m_SrF_b(s)+O(m_S^2).
\]

At `s=x`,

\[
F_1(x)=\frac{\tau_*+1/2}{L_x}
=0.238608516980548\ldots,
\tag{PN7}
\]

\[
F_2(x)=\frac{2\tau_*+1/2}{L_x}
=0.067601073701576\ldots,
\tag{PN8}
\]

and

\[
\boxed{
F_b'(x)
=-\frac{x}{2(1+x^2)^{3/2}}
=-0.192437028309842\ldots
}
\tag{PN9}
\]

for **both** `b=1` and `b=2`.

Choose the common scalar root amplitude so that the beta-one coupling equals `a_C,0`.  The same scalar then gives the beta-two value `a_P,0` by the tuned ratio.  Therefore the first source-frame slope derivatives satisfy

\[
\boxed{
a_C'(x)=a_P'(x)=:a_*'.}
\tag{PN10}

Using (PN2), (PN7), and (PN9),

\[
\boxed{
a_*'
=a_{C,0}\frac{F_1'(x)}{F_1(x)}
=1.345263716712010\ldots.}
\tag{PN11}

A finite nonzero sector normalization ratio `chi_2/chi_1`, if introduced by the exact source packet convention, changes (PN10)--(PN11) by explicit constant factors.  The present theorem is in the source-frame growing-coordinate convention of the polarization calculation.

## 4. Central profile scaling

Let

\[
h_S=S^{-1/2},
\qquad
y=jh_S.
\]

The catalyst and parent slope grids are

\[
z_{C,j}=x+d_Ch_Sy+O(S^{-1}),
\qquad
d_C:=2\kappa_*,
\tag{PN12}

\[
z_{P,j}=x+d_Ph_Sy+O(S^{-1}),
\qquad
d_P:=\kappa_*.
\tag{PN13}

After removing the limiting geometric factors

\[
c_j=\rho_C^jf_C(y),
\qquad
q_j=\rho_P^jf_P(y),
\]

the shift acts as

\[
R=\rho_b e^{h_S\partial_y}.
\]

## 5. First-order Poincare expansion

For one sector write the principal variable-coefficient shift equation as

\[
\partial_\tau u
=a_b(z_j)Ru,
\qquad
0\le\tau\le T_*.
\tag{PN14}

On the central window,

\[
a_b(z_j)
=a_{b,0}+h_Sd_ba_*'y+O(h_S^2(1+y^2)).
\tag{PN15}

Also

\[
R
=\rho_b\left(I+h_S\partial_y+O(h_S^2\partial_y^2)\right).
\tag{PN16}

Since the zeroth-order operator `a_{b,0}rho_b` is scalar, it commutes with the first-order profile operator.  Therefore over one cell

\[
\exp\left(T_*a_b(z)R\right)
=
\exp(T_*a_{b,0}\rho_b)
\left[
I+h_ST_*\rho_b
\left(a_{b,0}\partial_y+d_ba_*'y\right)
+O(h_S^2)
\right].
\tag{PN17}

The reset relabelling contributes

\[
R^{-m_b}
=\rho_b^{-m_b}
\left[I-m_bh_S\partial_y+O(h_S^2)\right],
\tag{PN18}

with

\[
m_C=1,
\qquad
m_P=2.
\]

The fixed dispersion equations cancel the zeroth-order scalar.  Hence

\[
\boxed{
\mathcal P_{b,S}^{tan}
=I+h_S\left(v_b\partial_y+B_by\right)
+O(h_S^2),
}
\tag{PN19}

before the finite-`S` centering/parameter-drift constant term is included, where

\[
\boxed{
v_b=T_*a_{b,0}\rho_b-m_b}
\tag{PN20}

and

\[
\boxed{
B_b=T_*\rho_bd_ba_*'.}
\tag{PN21}

A constant term `C_b` is produced by `O(S^{-1})` parameter drift and integer centering; it translates the Gaussian center and does not affect the quadratic localization test below.

## 6. Explicit transport coefficients

For the catalyst,

\[
\boxed{
v_C=\lambda_C\rho_C-1
=-2.046933015584520\ldots.}
\tag{PN22}

For the parent,

\[
\boxed{
v_P=\mu_P\rho_P-2}
\]

and numerically

\[
\boxed{
v_P
=-0.185170992872966
-1.044351775683794\,i.}
\tag{PN23}

Both are nonzero, as required for the first-order Volterra profile equation.

## 7. Explicit Gaussian-drift coefficients

Using (PN21),

\[
\boxed{
B_C
=T_*\rho_C(2\kappa_*)a_*'
=1.509777659068068\ldots,}
\tag{PN24}

while

\[
\boxed{
B_P
=T_*\rho_P\kappa_*a_*'
=-4.618831967884313
+2.657928294237038\,i.}
\tag{PN25}

Therefore

\[
\boxed{
\frac{B_C}{v_C}
=-0.737580393482948\ldots,}
\tag{PN26}

and

\[
\boxed{
\frac{B_P}{v_P}
=-1.707207600704530
-4.725378372738304\,i.}
\tag{PN27}

The coefficient profiles by themselves are therefore mildly anti-Gaussian in real part.  Physical action localization must be included before deciding admissibility.

## 8. Physical action curvature

Recall

\[
H_b'(z)=u\bigl(\Gamma_b(z)-\Gamma_b(x)\bigr),
\]

so

\[
H_b''(x)=u\Gamma_b'(x).
\]

For

\[
\Gamma_b(z)
=\frac1{\sqrt{1+u^2z^2}}
-b^2\frac{1+u^2z^2}{(1+u^2)^{3/2}},
\]

we have

\[
\Gamma_b'(z)
=-\frac{u^2z}{(1+u^2z^2)^{3/2}}
-\frac{2b^2u^2z}{(1+u^2)^{3/2}}.
\tag{PN28}

At `u=1.8,x=0.70`,

\[
\boxed{H_1''(x)=-1.915959376503904\ldots,}
\tag{PN29}

\[
\boxed{H_2''(x)=-4.721509426848687\ldots.}
\tag{PN30}

Write

\[
H_b(x+s)=-\alpha_bs^2+O(s^3),
\qquad
\alpha_b:=-\frac12H_b''(x)>0.
\]

Thus

\[
\boxed{\alpha_1=0.957979688251952\ldots,}
\tag{PN31}

\[
\boxed{\alpha_2=2.360754713424344\ldots.}
\tag{PN32}

## 9. Exact leading localization criterion

The continuum profile equation

\[
v_bf_b'(y)+(B_by+C_b)f_b(y)=0
\]

has quadratic factor

\[
\exp\left(-\frac{B_b}{2v_b}y^2\right).
\]

The physical action factor on the same central scale is

\[
\exp\left(-\alpha_bd_b^2y^2\right).
\]

Hence the total squared-amplitude Gaussian remains decaying whenever

\[
\boxed{
\Re(B_b/v_b)>-2\alpha_bd_b^2.
}
\tag{PN33}

For the catalyst,

\[
-2\alpha_1d_C^2
=-6.125888586540805\ldots,
\]

while

\[
\Re(B_C/v_C)
=-0.737580393482948\ldots.
\]

Thus

\[
\boxed{
\Re(B_C/v_C)-(-2\alpha_1d_C^2)
\approx5.38831>0.
}
\tag{PN34}

For the parent,

\[
-2\alpha_2d_P^2
=-3.774015391959207\ldots,
\]

while

\[
\Re(B_P/v_P)
=-1.707207600704530\ldots.
\]

Thus

\[
\boxed{
\Re(B_P/v_P)-(-2\alpha_2d_P^2)
\approx2.06681>0.
}
\tag{PN35}

Both sectors therefore retain a strict Gaussian localization margin.

## 10. Consequence

The leading continuum profile equations are admissible in the physical large-deviation orbit norm:

\[
\boxed{
\text{finite-`S` slope variation does not destroy bilateral localization.}
}
\tag{PN36}

The result is stronger than a formal solution of the profile ODE: the anti-Gaussian coefficient correction is quantitatively dominated by the already-proved physical action confinement.

## 11. Remaining exact steps

The local designated-profile frontier is now:

1. pin the exact source packet normalization ratio `chi_2/chi_1` in the coupling theorem;
2. compute the constant drift terms `C_C,C_P` from the exact finite-`S` centering and parameter corrections;
3. derive the full `O(h_S^2)` remainder in (PN19) in a Gaussian profile norm;
4. solve the exact finite-difference fixed-profile equation by a discrete Volterra/transport construction;
5. prove convergence of that discrete profile to the continuum Gaussian solution;
6. reinsert the already-controlled coupled PDE complement and restore the corrected exact finite-`S` local reset theorem.

Only after those steps should the global inter-cell shadowing construction be resumed.
