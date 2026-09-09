# Working algebra — one-way triad gate

Let \(p,q\in\mathbb R^3\) satisfy

\[
|p|=|q|=P,
\qquad
p\nparallel q.
\]

Define

\[
n=\frac{p\times q}{|p\times q|},
\]

\[
e_p=\frac{n\times p}{P},
\qquad
e_q=\frac{n\times q}{P}.
\]

Take divergence-free polarizations

\[
a=e_p-\gamma n,
\qquad
b=e_q+\gamma n.
\]

For the sum mode \(k_+=p+q\), the quadratic interaction is

\[
B_+
=
(a\cdot q)b+(b\cdot p)a.
\]

For the difference mode \(k_-=p-q\), the corresponding interaction has the sign pattern

\[
B_-
=
-(a\cdot q)b+(b\cdot p)a.
\]

The candidate identities are

\[
\mathbb P_{k_+}B_+
=
2\gamma P\sin\theta\, n,
\]

and

\[
\mathbb P_{k_-}B_-
=
0.
\]

## Status

This is elementary Fourier/Leray algebra and should be checked symbolically and written as a short standalone lemma before use.

## Caution

The current β-relay route does not require exact annihilation of the difference branch; it may instead exploit strong viscous damping. This file is retained because the identity can still be useful for polarization engineering.
