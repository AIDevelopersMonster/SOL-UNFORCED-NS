# Real-root bidirectional low-\(u\) principal reset

**Status:** CORRECTED PRINCIPAL MODEL / THE PREVIOUS ONE-SIDED ROOT-SHIFT GENERATOR IS INVALID FOR A REAL CAUCHY ROOT.  A NEW BIDIRECTIONAL LIMITING FIXED POINT WITH NONSINGULAR FOUR-REAL-DIMENSIONAL TRANSVERSALITY IS EXHIBITED.  FINITE-\(S\) SOURCE-LEVEL OPERATOR REALIZATION, CERTIFIED NUMERICS, AND THE EXACT DISCRETE PROFILE REMAIN OPEN.

This note repairs a structural omission in

- beta21_lowu_boundary_layer_bilateral_orbit_reset.md;
- beta21_lowu_single_root_coupling_ratio.md;
- beta21_lowu_profile_normal_form_coefficients.md.

The designated beta-zero Cauchy root is a real physical field.  Therefore its positive character \(+M\) is accompanied by the conjugate character \(-M\).  The pinned source theorem

\[
\texttt{WaveInteractionBounds.real\_modes\_identity}
\]

states exactly that the real interaction of two complex modes produces **both the sum and the difference harmonics**.

Consequently a positive-beta orbit mode \(C_j\) or \(Q_n\) interacts with both root characters:

\[
M+C_j=C_{j+1},
\qquad
(-M)+C_j=C_{j-1},
\]

and similarly in the parent sector.

The limiting designated generator is therefore bidirectional.

No exact finite-\(S\) Gate 1 closure is claimed here.

---

## 1. Exact real-reconstruction reason

The pinned source identity has the schematic form

\[
\operatorname{Transport}(\Re u,\Re v)
=
\frac12\Re\!\left[
T(u,v)e^{i(\nu+\xi)\Phi}
+
T(u,\bar v)e^{i(\nu-\xi)\Phi}
\right].
\tag{BR1}
\]

Thus a real root reconstructed from

\[
M_{des}=2\Re(M_+)
\]

necessarily generates both

\[
K+M
\quad\text{and}\quad
K-M.
\]

This is not an angular-average effect and is not source-small.

The earlier one-sided generator

\[
a_bR
\]

therefore omitted a principal term.

---

## 2. Forward and backward root couplings

Use the exact principal growing projection from

\[
\texttt{beta21\_lowu\_single\_root\_coupling\_ratio.md}.
\]

Let the positive root phase increment be

\[
m>0
\]

and choose the boundary-layer polarization

\[
k=\frac{mr}{L_x}\tau,
\qquad
L_x=\sqrt{1+x^2}.
\]

For interaction with \(+M\),

\[
A_{b,+}
=
\frac{mr}{L_x}
\left(
\frac12+b\tau
\right)
+O(m^2r).
\tag{BR2}
\]

For the conjugate root interaction with \(-M\), the same exact projection formula gives

\[
\boxed{
A_{b,-}
=
\frac{mr}{L_x}
\left(
-\frac12+b\tau
\right)
+O(m^2r).
}
\tag{BR3}
\]

The sign change in the \(1/2\) term comes from reversing the root phase increment, while the \(K\)-polarization contribution is retained by complex conjugation.

At the old working value

\[
\tau_*=-0.208741\ldots,
\]

the backward coefficients are not small.  In fact their leading magnitudes exceed the forward ones.

Therefore the previous one-sided limiting shift system is not the correct real-root principal model.

---

## 3. Correct bidirectional limiting generator

Absorb the common root amplitude, the real-reconstruction factor, and the full-cell time normalization into one real scalar

\[
A.
\]

For fixed real design parameter \(\tau\), define

\[
c_{b,+}:=\frac12+b\tau,
\qquad
c_{b,-}:=-\frac12+b\tau.
\tag{BR4}
\]

Let \(R\) be the unit orbit shift.

The corrected limiting generator in sector \(b\) is

\[
\boxed{
G_b
=
A\left(
c_{b,+}R+c_{b,-}R^{-1}
\right).
}
\tag{BR5}
\]

The reset relabelling is still

\[
R^{-m_b},
\qquad
m_1=1,\quad m_2=2.
\]

Hence the corrected limiting Poincare operators are

\[
\boxed{
\mathcal P_b
=
R^{-m_b}
\exp\!\left[
A(c_{b,+}R+c_{b,-}R^{-1})
\right].
}
\tag{BR6}
\]

Because \(R\) and \(R^{-1}\) commute, (BR6) is exact at limiting translation-invariant principal level.

---

## 4. Geometric fixed-profile equations

For a geometric bilateral mode

\[
Rf=\rho_bf,
\]

the corrected fixed equation is

\[
\boxed{
\frac{
\exp\!\left[
A(c_{b,+}\rho_b+c_{b,-}\rho_b^{-1})
\right]
}{
\rho_b^{m_b}
}
=1.
}
\tag{BR7}
\]

Physical action balance fixes

\[
\boxed{
\rho_C=e^{-2\kappa g_1}>0,
}
\tag{BR8}
\]

and

\[
\boxed{
|\rho_P|=e^{-\kappa g_2}>1,
}
\tag{BR9}
\]

where at \(u=1.8,x=0.70\),

\[
g_1=0.58550080577840348\ldots,
\]

\[
g_2=-1.01494921853203834\ldots.
\]

A particularly simple real-symmetric parent branch is

\[
\boxed{
\rho_P=-e^{-\kappa g_2},
\qquad
\theta=\pi.
}
\tag{BR10}
\]

Then both fixed equations are real.

---

## 5. A corrected working point

Fix the root-polarization design constant

\[
\boxed{\tau=-5.}
\tag{BR11}
\]

Then

\[
c_{1,+}=-4.5,
\qquad
c_{1,-}=-5.5,
\]

\[
c_{2,+}=-9.5,
\qquad
c_{2,-}=-10.5.
\tag{BR12}
\]

Solving the two real equations from (BR7) on the branch (BR10) gives

\[
\boxed{
\kappa_\diamond
=
0.61048308467122222\ldots,
}
\tag{BR13}
\]

\[
\boxed{
A_\diamond
=
0.053177265707723206\ldots.
}
\tag{BR14}
\]

The geometric ratios are

\[
\boxed{
\rho_{C,\diamond}
=
0.48925244465517379\ldots,
}
\tag{BR15}
\]

\[
\boxed{
\rho_{P,\diamond}
=
-1.85820195573610782\ldots.
}
\tag{BR16}
\]

The full-cell forward/backward coefficients are

\[
\lambda_{C,+}
=
A_\diamond c_{1,+}
=
-0.23929769568475443\ldots,
\]

\[
\lambda_{C,-}
=
A_\diamond c_{1,-}
=
-0.29247496139247764\ldots,
\tag{BR17}
\]

and

\[
\lambda_{P,+}
=
A_\diamond c_{2,+}
=
-0.50518402422337046\ldots,
\]

\[
\lambda_{P,-}
=
A_\diamond c_{2,-}
=
-0.55836128993109367\ldots.
\tag{BR18}
\]

Directly,

\[
\lambda_{C,+}\rho_C
+
\lambda_{C,-}\rho_C^{-1}
=
\log\rho_C,
\]

and

\[
\lambda_{P,+}\rho_P
+
\lambda_{P,-}\rho_P^{-1}
=
2\log|\rho_P|.
\]

Therefore

\[
\boxed{
\mathcal P_C(\rho_C^j)=\rho_C^j,
\qquad
\mathcal P_P(\rho_P^j)=\rho_P^j.
}
\tag{BR19}
\]

The second equation uses the parent logarithm branch corresponding to

\[
\theta=\pi,
\qquad
2\theta-2\pi=0.
\]

---

## 6. Root phase restores the correct four-real-dimensional parameter ledger

A real physical root may carry a spatial phase \(\phi_M\).

Let its positive Fourier coefficient have phase

\[
e^{i\phi_M}
\]

and its conjugate coefficient therefore have phase

\[
e^{-i\phi_M}.
\]

The corrected exponent in sector \(b\) is

\[
\boxed{
E_b
=
A\left[
e^{i\phi_M}c_{b,+}\rho_b
+
e^{-i\phi_M}c_{b,-}\rho_b^{-1}
\right].
}
\tag{BR20}
\]

Define the complex residuals

\[
F_C
=
e^{E_1}\rho_C^{-1}-1,
\]

\[
F_P
=
e^{E_2}\rho_P^{-2}-1.
\tag{BR21}
\]

Use the four real parameters

\[
\boxed{
(\kappa,A,\theta,\phi_M).
}
\tag{BR22}
\]

At the corrected point

\[
(\kappa_\diamond,A_\diamond,\pi,0)
\]

the four real equations

\[
\Re F_C=\Im F_C=\Re F_P=\Im F_P=0
\]

hold.

Thus the corrected model has the correct square macroscopic parameter ledger without using \(\tau\) as an implicit-function variable.

---

## 7. Explicit transversality block structure

At the real-symmetric point define

\[
D_b
=
c_{b,+}\rho_b+c_{b,-}\rho_b^{-1},
\]

\[
J_b
=
c_{b,+}\rho_b-c_{b,-}\rho_b^{-1}.
\tag{BR23}
\]

For the catalyst,

\[
D_C=-13.4432763035867537\ldots,
\]

\[
J_C=9.04000430169018956\ldots.
\]

For the parent,

\[
D_P=23.3035422738591901\ldots,
\]

\[
J_P=12.0022948851268585\ldots.
\tag{BR24}
\]

At a fixed point, differentiation of (BR21) gives the real block

\[
D_{(\kappa,A)}
\begin{pmatrix}
\Re F_C\\
\Re F_P
\end{pmatrix}
=
\begin{pmatrix}
-2g_1(AJ_C-1) & D_C\\
g_2(2-AJ_P) & D_P
\end{pmatrix}.
\tag{BR25}
\]

Numerically,

\[
\boxed{
J_{\rm real}
=
\begin{pmatrix}
0.6080745425566705 & -13.443276303586754\\
-1.3821078857246367 & 23.303542273859190
\end{pmatrix}.
}
\tag{BR26}
\]

Its determinant is

\[
\boxed{
\det J_{\rm real}
=
-4.4097673810354380\ldots\ne0.
}
\tag{BR27}
\]

The imaginary block in variables \((\theta,\phi_M)\) is

\[
D_{(\theta,\phi_M)}
\begin{pmatrix}
\Im F_C\\
\Im F_P
\end{pmatrix}
=
\begin{pmatrix}
0&AJ_C\\
AJ_P-2&AJ_P
\end{pmatrix}.
\tag{BR28}
\]

Numerically,

\[
\boxed{
J_{\rm imag}
=
\begin{pmatrix}
0&0.4807227107499400\\
-1.3617507757911619&0.6382492242088381
\end{pmatrix}.
}
\tag{BR29}
\]

Hence

\[
\boxed{
\det J_{\rm imag}
=
0.6546245243041611\ldots\ne0.
}
\tag{BR30}
\]

The complete four-real-dimensional Jacobian is block triangular at this symmetric point, so

\[
\boxed{
\det J_\diamond
=
-2.8867418741023299\ldots\ne0.
}
\tag{BR31}
\]

A direct singular-value diagnostic gives

\[
\boxed{
s_{\min}(J_\diamond)
\approx0.1637.
}
\tag{BR32}
\]

Thus the corrected real-root fixed point is transversely nondegenerate.

---

## 8. Corrected central transport coefficients

The forward and backward slope-coupling functions have opposite first derivatives.

At leading order,

\[
F_{b,+}(s)
=
\frac{b\tau}{L_x}
+
\frac1{2\sqrt{1+s^2}},
\]

\[
F_{b,-}(s)
=
\frac{b\tau}{L_x}
-
\frac1{2\sqrt{1+s^2}}.
\tag{BR33}
\]

Therefore

\[
F_{b,+}'(x)
=
-\frac{x}{2(1+x^2)^{3/2}},
\]

\[
F_{b,-}'(x)
=
+\frac{x}{2(1+x^2)^{3/2}}.
\tag{BR34}
\]

After tangent normalization \(R=\rho e^{h\partial_y}\), the first-order continuum transport coefficient becomes

\[
\boxed{
v_b
=
A(c_{b,+}\rho_b-c_{b,-}\rho_b^{-1})
-
m_b
=
AJ_b-m_b.
}
\tag{BR35}
\]

At the corrected point,

\[
\boxed{
v_C=-0.5192772892500600\ldots,
}
\tag{BR36}
\]

\[
\boxed{
v_P=-1.3617507757911619\ldots.
}
\tag{BR37}
\]

Both are safely nonzero.

Let

\[
f_*'
=
-\frac{x}{2(1+x^2)^{3/2}}.
\]

The affine \(y\)-coefficient is

\[
\boxed{
B_b
=
A\,d_bL_xf_*'
\left(
\rho_b-\rho_b^{-1}
\right),
}
\tag{BR38}
\]

with

\[
d_C=2\kappa_\diamond,
\qquad
d_P=\kappa_\diamond.
\]

Numerically,

\[
\boxed{
\Re(B_C/v_C)
\approx-0.04566187,
}
\tag{BR39}
\]

\[
\boxed{
\Re(B_P/v_P)
\approx-0.00739219.
}
\tag{BR40}
\]

The physical action localization thresholds are approximately

\[
-2\alpha_1d_C^2
\approx-2.85623,
\]

\[
-2\alpha_2d_P^2
\approx-1.75966.
\tag{BR41}
\]

Thus the corrected bidirectional continuum profile retains very large Gaussian admissibility margins.

This does **not** yet prove the exact discrete profile.

---

## 9. Analytic-weight budget survives at \(\sigma_0=0.005\)

The orbit-index span scales like \(1/\kappa\).

Relative to the old value \(\kappa_*=0.894049\ldots\), the corrected value increases the index-density constants by the factor

\[
\frac{0.894049\ldots}{0.610483\ldots}
\approx1.4645.
\]

Using the previous conservative constants gives approximately

\[
C_C^{new}\approx0.0737,
\qquad
C_Q^{new}\approx0.1474.
\]

At

\[
\sigma_0=0.005,
\]

the analytic prices are therefore about

\[
3.69\times10^{-4}S,
\qquad
7.37\times10^{-4}S.
\]

They remain below the existing physical boundary gaps

\[
c_{bd,C}\approx8.61\times10^{-4},
\]

\[
c_{bd,Q}\approx2.106\times10^{-3}.
\]

Thus the existing conservative analytic radius

\[
\boxed{\sigma_0=0.005}
\]

is still compatible with the corrected principal point.

The old detailed constants must nevertheless be recomputed before publication.

---

## 10. Consequences for the old theorem chain

The following old statements are superseded:

1. the one-sided principal generator
   \[
   \partial_\tau u=a_bRu;
   \]
2. the dispersion equations
   \[
   e^{\lambda_C\rho_C}/\rho_C=1,
   \qquad
   e^{\mu_P\rho_P}/\rho_P^2=1;
   \]
3. the normal-form coefficients computed from only the \(+M\) direction.

They must be replaced by (BR5)--(BR7) and the corrected coefficients above.

The following parts survive unchanged at the level of current evidence:

- orbit character algebra;
- physical action functions \(H_b\);
- low-\(u\) high-beta stability;
- non-\(M\) action-gap mechanism, since it depends on \(u,x\) and core slopes rather than on the one-sided root approximation;
- real Cauchy/curl realization of the root;
- source-local bilinear calculus;
- the need for an exact discrete finite-\(S\) profile theorem.

---

## 11. Revised Gate 1B frontier

The next exact theorem is now:

> Construct the exact finite-\(S\) designated generator with **both** root sidebands, prove that after action/tangent normalization it converges to the bidirectional operator (BR5), and solve the exact variable-coefficient fixed-profile problem near the corrected principal point (BR13)--(BR16).

The exact finite-\(S\) generator should have the schematic tridiagonal form

\[
\boxed{
(G_{b,S}(v)a)_j
=
d_{b,j}(v)a_j
+
p_{b,j}(v)a_{j-1}
+
q_{b,j}(v)a_{j+1},
}
\tag{BR42}
\]

with \(p,q\) produced by the \(+M,-M\) root pair.

Its one-cell propagator is no longer one-sided Volterra in orbit index.  The correct next method is therefore a **two-sided discrete exponential-dichotomy / Jacobi-type profile analysis**, not the one-sided recurrence proposed before the conjugate-root correction was found.

No Gate 1 closure follows yet.
