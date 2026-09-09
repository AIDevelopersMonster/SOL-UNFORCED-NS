# Translated asynchronous overlap on the auxiliary torus

**Status:** PROVED GEOMETRIC LEMMA inside the published auxiliary-rectangle framework. This lemma concerns support geometry only; it does not prove the nonlinear relay PDE estimate.

Primary source ingredients: OpenAI, *Finite Time Blowup for Navier–Stokes*, equations (6.10)–(6.12), Lemmas 6.1–6.2, and the common-torus path (6.21)–(6.22).

## 1. Local pulse coordinate as an affine torus coordinate

For a label \(\gamma\) in band \(\ell\), write its band rectangle as

\[
R_\gamma
=
\{c_\gamma+\xi v_r+\eta v_t:|\xi|,|\eta|<r_0\}
\]

and recall

\[
v_\gamma=\frac{\eta_\gamma+r_0}{c_i},
\qquad
L_{s,\gamma}=\frac{2r_0}{c_i}.
\]

For a sign-fixed OpenAI pulse,

\[
\frac{|s_\gamma(v_\gamma)|}{u_*}
=
\frac12+\frac{v_\gamma}{L_{s,\gamma}}.
\]

Hence prescribing a normalized pulse coordinate

\[
x_\gamma:=\frac{|s_\gamma|}{u_*}\in\left(\frac12,\frac32\right)
\]

is equivalent to prescribing

\[
\boxed{
\eta_\gamma
=
2r_0(x_\gamma-1).
}
\tag{T1}
\]

The distance from this point to the two temporal sides of the rectangle is

\[
\boxed{
\operatorname{margin}_\gamma
=
r_0\big(1-2|x_\gamma-1|\big)>0.
}
\tag{T2}
\]

## 2. Same-band translated-overlap lemma

### Lemma

Fix finitely many labels in the same band and target pulse coordinates

\[
x_j\in(1/2,3/2),\qquad j=1,\dots,m.
\]

Then their rectangle centers can be chosen so that there is a common torus point \(Y_0\) at which every label has exactly the prescribed pulse coordinate \(x_j\).

Moreover, if

\[
\rho<\min_j\big(1-2|x_j-1|\big),
\]

then the labels share a common collar around \(Y_0\) of temporal half-width \(\rho r_0\) in the \(v_t\)-direction and of any fixed transverse half-width smaller than \(r_0\).

### Proof

Choose one lift \(Y_0\in\mathbb R^2\). Set the transverse target coordinate to zero and define

\[
\eta_j:=2r_0(x_j-1).
\]

Choose

\[
\boxed{c_j=Y_0-\eta_jv_t\pmod{\mathbb Z^2}.}
\tag{T3}
\]

Then

\[
Y_0-c_j=\eta_jv_t,
\]

so \(Y_0\in R_j\) and (T1) gives the desired pulse coordinate. If \(|\delta|<\rho r_0\), then at \(Y_0+\delta v_t\) the local temporal coordinate becomes \(\eta_j+\delta\). By (T2) this remains strictly inside every rectangle. The transverse statement is identical. ∎

## 3. Common-torus version for neighboring bands

Let the relevant bands differ by at most the fixed \(\Delta_{\max}\) of Lemma 6.1 and pass to the common torus \(H\) of Lemma 6.2. A lifted rectangle has the form

\[
J_g^{-\Delta_j}
\big(c_j+k_j+\xi v_r+\eta v_t\big).
\]

Choose a common-torus point \(H_0\) and prescribe \(\eta_j\) by (T1). Then define

\[
\boxed{
 c_j+k_j
=
J_g^{\Delta_j}H_0-\eta_jv_t
}
\tag{T4}
\]

with any permitted lattice representative. This makes \(H_0\) a lift of the required local coordinate for every band.

Because \(0\le\Delta_j\le\Delta_{\max}\), the matrices \(J_g^{\pm\Delta_j}\) have uniformly bounded norms. Therefore the intersection contains a common-torus collar of radius

\[
\boxed{
 c_{\Delta}\,r_0
\min_j\big(1-2|x_j-1|\big)
}
\tag{T5}
\]

for a constant \(c_\Delta>0\) depending only on the fixed covering-depth bound, not on the dyadic band.

The common-torus coordinate changes introduce only the bounded derivative factors already allowed by Lemma 6.2.

## 4. Compatibility with sparse separation

The complete-disjointness construction of Lemma 6.1 can be modified by treating each designated relay family as a finite **supernode**.

Inside a supernode, relative offsets such as (T3)–(T4) are prescribed. Between distinct supernodes whose slow supports meet, demand separation of every pair of enlarged component rectangles.

The proof is the same finite-color/generic-center argument as Lemma 6.1: after fixing the finite internal offsets, every unwanted intersection excludes one proper affine congruence among finitely many color-base centers. For \(\Delta>0\), invertibility of \(J_g^\Delta-I\) gives the same self-color exclusion used in the source proof. A generic finite tuple of base centers avoids all forbidden congruences, and then one sufficiently small common \(r_0\) separates all non-designated pairs.

Thus one may impose simultaneously:

\[
\boxed{
\text{prescribed finite overlaps inside relay supernodes}
}
\]

and

\[
\boxed{
\text{exact disjointness for all non-designated interactions.}
}
\]

## 5. Current relay witness and geometric margin

For the present preferred reduced witness

\[
\beta_1=\frac{55}{64},
\qquad
\beta_2=\frac{107}{192},
\qquad
\beta_1+\beta_2=\frac{17}{12},
\]

use

\[
x_1=\frac{59}{40}=1.475,
\]

and the reduced transverse resonance root

\[
y_2\approx0.9498544185190722,
\qquad
x_c\approx0.5211050633031591.
\]

The corresponding temporal rectangle coordinates are

\[
\frac{\eta_1}{r_0}=0.95,
\qquad
\frac{\eta_2}{r_0}\approx-0.1002911630,
\qquad
\frac{\eta_c}{r_0}\approx-0.9577898734.
\]

The smallest normalized temporal margin is

\[
\boxed{
\mu_{\rm geom}
:=
\min_j\big(1-|\eta_j|/r_0\big)
\approx0.0422101266.
}
\tag{T6}
\]

Hence a fixed band-independent overlap collar exists; for example any temporal half-width less than \(0.02r_0\) is safely inside all three raw rectangles before the bounded common-torus distortion is accounted for.

## 6. What this removes

The earlier concern that different relay coordinates \(x_1\ne y_2\ne x_c\) cannot occur at one physical auxiliary point is false. The centers \(c_\gamma\) are free auxiliary-torus parameters, and translating them in the \(v_t\) direction changes the local pulse coordinate at a common point without changing the slow coordinates.

Therefore **asynchronous pulse coordinates are geometrically compatible with the OpenAI auxiliary-torus architecture.**

## 7. What remains open

This lemma does not control the nonlinear terms created inside the permitted overlap. The next issue is to show that the desired parent-parent sum branch dominates while parent-child feedback and other newly enabled cross terms are negligible or removable.
