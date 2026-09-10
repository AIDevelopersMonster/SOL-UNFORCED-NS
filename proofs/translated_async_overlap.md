# Translated asynchronous overlap on the auxiliary torus

**Status:** PROVED GEOMETRIC LEMMA inside the auxiliary-rectangle framework. This concerns support geometry only.

## 1. Affine pulse coordinate

For a label rectangle

\[
R_\gamma=\{c_\gamma+\xi v_r+\eta v_t:|\xi|,|\eta|<r_0\},
\]

with \(v=(\eta+r_0)/c_i\) and \(L_s=2r_0/c_i\), a sign-fixed pulse has normalized coordinate

\[
x=\frac{|s|}{u_*}=\frac12+\frac{v}{L_s}.
\]

Hence

\[
\boxed{\eta=2r_0(x-1).}
\tag{T1}
\]

Choosing a common torus point \(Y_0\) and centers

\[
\boxed{c_j=Y_0-2r_0(x_j-1)v_t\pmod{\mathbb Z^2}}
\tag{T2}
\]

realizes any finite collection \(x_j\in(1/2,3/2)\) at the same physical auxiliary point.

The normalized temporal margin is

\[
\mu_j=1-2|x_j-1|>0.
\tag{T3}
\]

Thus a common collar of any half-width smaller than \(r_0\min_j\mu_j\) exists. The same statement passes to neighboring-band common tori with only a fixed bounded distortion because the covering-depth difference is bounded.

## 2. Sparse supernodes

A designated relay family may be treated as one finite supernode with prescribed internal offsets (T2), while generic center choices retain exact disjointness between distinct supernodes. This modifies only the final separation step of the source finite-color construction; the local affine overlap statement itself is exact.

## 3. v0.4 margin

For the corrected difference relay,

\[
x_1=0.90625,
\qquad y_0\approx1.2260460510,
\qquad x_c\approx0.7263647213.
\]

Therefore

\[
\eta_1/r_0=-0.1875,
\]

\[
\eta_2/r_0\approx0.4520921020,
\]

\[
\eta_c/r_0\approx-0.5472705574.
\]

The smallest normalized temporal margin is

\[
\boxed{\mu_{\rm geom}\approx0.4527294426.}
\]

This is much larger than in the obsolete v0.3 geometry. In particular, a temporal half-width \(0.2r_0\) fits safely inside all three raw rectangles before any fixed common-torus distortion.

## 4. Scope

The lemma proves that asynchronous parent/catalyst/child coordinates are geometrically compatible with one common overlap collar. It does not estimate the nonlinear interaction inside that collar.
