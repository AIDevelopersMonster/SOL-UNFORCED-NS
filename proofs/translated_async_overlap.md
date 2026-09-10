# Translated asynchronous overlap on the auxiliary torus

**Status:** PROVED GEOMETRIC LEMMA inside the published auxiliary-rectangle framework. This lemma concerns support geometry only.

## 1. Local pulse coordinate

For a label \(\gamma\), write its auxiliary rectangle as

\[
R_\gamma=\{c_\gamma+\xi v_r+\eta v_t:|\xi|,|\eta|<r_0\}.
\]

With

\[
v_\gamma=\frac{\eta_\gamma+r_0}{c_i},
\qquad
L_{s,\gamma}=\frac{2r_0}{c_i},
\]

the normalized pulse coordinate

\[
x_\gamma=\frac{|s_\gamma|}{u_*}=\frac12+\frac{v_\gamma}{L_{s,\gamma}}
\]

is equivalent to

\[
\boxed{\eta_\gamma=2r_0(x_\gamma-1).}
\]

Thus prescribed pulse coordinates can be realized at one common torus point by translating the rectangle centers.

## 2. Common overlap lemma

Fix finitely many target coordinates \(x_j\in(1/2,3/2)\). Choose one lift \(Y_0\) and put

\[
\eta_j=2r_0(x_j-1),
\qquad
 c_j=Y_0-\eta_jv_t\pmod{\mathbb Z^2}.
\]

Then \(Y_0\in R_j\) for all labels and has the prescribed local coordinate in each rectangle. A common collar exists with temporal half-width

\[
\rho r_0,
\qquad
\rho<\min_j(1-2|x_j-1|).
\]

The common-covering-torus extension for neighboring dyadic charts is unchanged: bounded covering depth gives only a fixed distortion constant.

## 3. Sparse separation

Designated relay labels may be grouped into finite supernodes with prescribed internal offsets. A generic-center coloring argument then preserves exact disjointness between all non-designated supernodes after choosing sufficiently small \(r_0\).

## 4. Updated v0.4 witness

For

\[
x_1=0.90625,
\qquad
y_0\approx1.2260460510,
\qquad
x_c\approx0.7263647213,
\]

the normalized distances to the raw pulse endpoints are

\[
\min\{x_j-1/2,\,3/2-x_j\}\approx0.22636.
\]

Equivalently, the smallest normalized temporal rectangle margin is about

\[
\boxed{0.4527}
\]

in the \(\eta/r_0\) convention. This is far more generous than the obsolete near-endpoint witnesses.

## 5. Consequence

The corrected difference relay has ample auxiliary support room for a bounded-\(v\) seeding collar. The remaining obstruction is not overlap geometry but the full localized PDE interaction and exact correction closure.
