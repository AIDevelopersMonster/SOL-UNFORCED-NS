# Exact phase-adapted whole-space Leray intertwining

**Status:** PROVED EXACT COEFFICIENT-SPACE THEOREM. This closes the microlocal interface isolated in `reconstruction_leray_intertwining_obligation.md`. No WKB expansion, lower bound on the reconstructed covector, or high/low frequency split is needed.

The key point is elementary but stronger than the previous symbol-level discussion: the whole-space Leray projector is bounded on physical Sobolev space, multiplication by one reconstructed phase is unitary on `L^2`, and the correct coefficient derivatives are the exact covariant pullbacks of physical derivatives. In that norm the conjugated Leray projector commutes with every covariant derivative exactly.

## 1. Reconstruction mode and phase modulation

For an auxiliary Fourier index

\[
k\in\mathbb Z^2
\]

write

\[
\boxed{
\theta_{\ell,k}(x,s):=2\pi k\cdot\Phi_\ell(x,s)
}
\tag{PA1}
\]

and let

\[
\boxed{
M_{\ell,k}(s)f(x):=e^{i\theta_{\ell,k}(x,s)}f(x).
}
\tag{PA2}
\]

Then the reconstruction of

\[
a(x,y,s)=\sum_{k\in\mathbb Z^2}a_k(x,s)e^{2\pi i k\cdot y}
\]

is

\[
\boxed{
\mathcal R_\ell a
=\sum_k M_{\ell,k}a_k.
}
\tag{PA3}
\]

Since `theta_{ell,k}` is real,

\[
\boxed{
\|M_{\ell,k}f\|_{L^2}=\|f\|_{L^2}.
}
\tag{PA4}
\]

No assumption on `|nabla theta_{ell,k}|` is used here.

## 2. Exact induced coefficient Leray operator

Let

\[
\mathbb P:=I-\nabla\Delta^{-1}\operatorname{div}
\]

be the physical whole-space Leray projector on `R^3`. Define, mode by mode,

\[
\boxed{
\mathbb P_{\ell,k}^{\rm cov}
:=M_{\ell,k}^{-1}\mathbb P M_{\ell,k}.
}
\tag{PA5}
\]

and set

\[
\boxed{
(\mathbb P_{\rm coeff,\ell}a)_k
:=\mathbb P_{\ell,k}^{\rm cov}a_k.
}
\tag{PA6}
\]

For every finitely supported auxiliary Fourier series, linearity gives the exact identity

\[
\begin{aligned}
\mathbb P\mathcal R_\ell a
&=\sum_k\mathbb P M_{\ell,k}a_k\\
&=\sum_k M_{\ell,k}\mathbb P_{\ell,k}^{\rm cov}a_k\\
&=\mathcal R_\ell(\mathbb P_{\rm coeff,\ell}a).
\end{aligned}
\]

Hence

\[
\boxed{
\mathbb P\mathcal R_\ell
=\mathcal R_\ell\mathbb P_{\rm coeff,\ell}.
}
\tag{PA7}
\]

This is exact, not asymptotic.

## 3. Covariant derivatives

For a Cartesian spatial derivative `partial_j`, define its coefficient pullback

\[
\boxed{
\nabla_{\ell,k,j}^{\rm cov}
:=M_{\ell,k}^{-1}\partial_jM_{\ell,k}
=\partial_j+i\partial_j\theta_{\ell,k}.
}
\tag{PA8}
\]

For a multi-index `alpha`, let

\[
(\nabla_{\ell,k}^{\rm cov})^\alpha
:=M_{\ell,k}^{-1}\partial^\alpha M_{\ell,k}.
\tag{PA9}
\]

Because the physical Leray projector is a constant-coefficient Fourier multiplier,

\[
\partial^\alpha\mathbb P=\mathbb P\partial^\alpha.
\tag{PA10}
\]

Therefore

\[
\begin{aligned}
(\nabla_{\ell,k}^{\rm cov})^\alpha
\mathbb P_{\ell,k}^{\rm cov}
&=M_{\ell,k}^{-1}\partial^\alpha\mathbb P M_{\ell,k}\\
&=M_{\ell,k}^{-1}\mathbb P\partial^\alpha M_{\ell,k}\\
&=\mathbb P_{\ell,k}^{\rm cov}
(\nabla_{\ell,k}^{\rm cov})^\alpha.
\end{aligned}
\]

Thus

\[
\boxed{
[(\nabla_{\ell,k}^{\rm cov})^\alpha,
\mathbb P_{\ell,k}^{\rm cov}]=0.
}
\tag{PA11}
\]

The large derivatives of the phase never appear as commutator errors; they are built into the covariant derivative itself.

## 4. Exact fixed-order norm bound

Define

\[
\boxed{
\|a_k\|_{H^{m}_{\ell,k,\rm cov}}^2
:=
\sum_{|\alpha|\le m}
\|(\nabla_{\ell,k}^{\rm cov})^\alpha a_k\|_{L^2(\mathbb R^3)}^2.
}
\tag{PA12}
\]

Equivalently,

\[
\boxed{
\|a_k\|_{H^{m}_{\ell,k,\rm cov}}
=\|M_{\ell,k}a_k\|_{H^m(\mathbb R^3)}.
}
\tag{PA13}
\]

Since `P` is the orthogonal `L^2` projection onto divergence-free vector fields, (PA11) gives

\[
\boxed{
\|\mathbb P_{\ell,k}^{\rm cov}a_k\|_{H^{m}_{\ell,k,\rm cov}}
\le
\|a_k\|_{H^{m}_{\ell,k,\rm cov}}.
}
\tag{PA14}
\]

This estimate is uniform in

\[
\ell,\qquad k,\qquad \theta_{\ell,k},\qquad
|\nabla\theta_{\ell,k}|.
\]

In particular no near-cancelled reconstructed frequency causes a loss.

## 5. Weighted auxiliary lattice space

For `sigma>0` and fixed derivative order `m`, define

\[
\boxed{
\|a\|_{\mathfrak M_{\sigma,m}}
:=
\sum_{k\in\mathbb Z^2}
 e^{\sigma|k|_1}
\|a_k\|_{H^{m}_{\ell,k,\rm cov}}.
}
\tag{PA15}
\]

Then (PA14) yields immediately

\[
\boxed{
\|\mathbb P_{\rm coeff,\ell}a\|_{\mathfrak M_{\sigma,m}}
\le
\|a\|_{\mathfrak M_{\sigma,m}}.
}
\tag{PA16}
\]

The weighted `l^1` summability also implies absolute convergence after reconstruction in physical `H^m`, so (PA7) extends from finite Fourier sums to the completion.

Thus the target estimates (RL15)--(RL16) of `reconstruction_leray_intertwining_obligation.md` hold with no loss of analytic lattice radius.

## 6. Exact product calculus in the same norm

The phase is linear in the auxiliary index:

\[
\boxed{
\theta_{\ell,k+j}=\theta_{\ell,k}+\theta_{\ell,j}.
}
\tag{PA17}
\]

Hence for coefficient modes `a_k,b_j`,

\[
M_{\ell,k+j}(a_kb_j)
=(M_{\ell,k}a_k)(M_{\ell,j}b_j).
\tag{PA18}
\]

Equivalently the covariant Leibniz rule is exact:

\[
\boxed{
\nabla_{\ell,k+j}^{\rm cov}(a_kb_j)
=(\nabla_{\ell,k}^{\rm cov}a_k)b_j
+a_k(\nabla_{\ell,j}^{\rm cov}b_j).
}
\tag{PA19}
\]

For `m>3/2`, ordinary physical `H^m(R^3)` is a Banach algebra. Using (PA13), (PA18), and

\[
e^{\sigma|k+j|_1}
\le e^{\sigma|k|_1}e^{\sigma|j|_1},
\]

we obtain

\[
\boxed{
\|ab\|_{\mathfrak M_{\sigma,m}}
\le C_m
\|a\|_{\mathfrak M_{\sigma,m}}
\|b\|_{\mathfrak M_{\sigma,m}}.
}
\tag{PA20}
\]

Thus the same coefficient space is closed simultaneously under reconstruction, physical multiplication, fixed-order derivatives, and whole-space Leray projection.

## 7. Local use of a noncompact Leray output

The operator `P` is nonlocal, so `P_{ell,k}^{cov}a_k` need not have compact spatial support even if `a_k` does. This does not obstruct coupling to the compact nonzero relay packets.

Let `K` contain the support of every designated/nonzero packet and its first derivatives on the relay collar, and choose a fixed smooth cutoff

\[
\chi\equiv1
\]

on a neighborhood of `K`. Define

\[
\boxed{
\mathbb P_{\ell,k}^{\rm loc}a_k
:=\chi\mathbb P_{\ell,k}^{\rm cov}a_k.
}
\tag{PA21}
\]

Multiplication by the fixed cutoff is bounded at fixed Sobolev order, so

\[
\boxed{
\|\mathbb P_{\ell,k}^{\rm loc}a_k\|_{H^m_{\ell,k,\rm cov}(K')}
\le C_{\chi,m}
\|a_k\|_{H^m_{\ell,k,\rm cov}}.
}
\tag{PA22}
\]

For a packet `w` supported in `K`, the first-order Navier--Stokes mixed terms satisfy exactly

\[
\boxed{
(w\cdot\nabla)m
=(w\cdot\nabla)(\chi m),
\qquad
(m\cdot\nabla)w
=(\chi m\cdot\nabla)w.
}
\tag{PA23}
\]

The equality is exact because `chi=1` and `nabla chi=0` on a neighborhood containing the supports relevant to `w` and `nabla w`.

Thus the noncompact pressure/Leray tail need not itself belong to the compact packet support class; only its restriction to the packet core enters the nonzero equation.

## 8. Relation to source characteristic derivatives

The source common-torus derivatives are precisely pullbacks of physical derivatives under reconstruction. For example, the large radial phase derivative is encoded as

\[
D_r=\partial_R+a_\ell(R)v_r\cdot\partial_y,
\]

which on the `k`th auxiliary mode is the corresponding covariant physical radial derivative. The same statement holds for the normalized axial/time characteristic derivatives used in the packet seminorm.

On the fixed annular/core chart, Cartesian covariant derivatives and the finite family of cylindrical/source characteristic derivatives are equivalent at every fixed order, up to constants from the fixed smooth frame and the already allowed source-polynomial bookkeeping. Hence (PA16) and (PA22) give the uniform local coefficient estimates required to insert the whole-space mean into `nonzero_harmonic_forward_reduction.md`.

No additional Diophantine or WKB estimate is needed.

## 9. Resolution of the previous low-frequency concern

The previous obligation split the lattice according to the reconstructed covector

\[
\Xi_{\ell,k}=\nabla\theta_{\ell,k}
\]

and worried about modes for which `|Xi_{ell,k}|` is small. That split is unnecessary.

The semiclassical symbol derivatives

\[
\partial_\xi^\alpha P(\xi)
\]

appear only if one approximates the conjugated operator by its principal WKB symbol. Here the operator is conjugated **exactly**, and its norm follows from physical `L^2/H^m` boundedness. Therefore no lower bound on `|Xi_{ell,k}|` enters the theorem.

In particular the genuine mean auxiliary mode `k=0` is harmless:

\[
\mathbb P_{\ell,0}^{\rm cov}=\mathbb P.
\]

## 10. Theorem closed

For every fixed `m` and `sigma>0`, the coefficient operator (PA6) satisfies

\[
\boxed{
\mathbb P\mathcal R_\ell
=\mathcal R_\ell\mathbb P_{\rm coeff,\ell},
\qquad
\|\mathbb P_{\rm coeff,\ell}\|_{\mathfrak M_{\sigma,m}\to\mathfrak M_{\sigma,m}}
\le1,
}
\tag{PA24}
\]

uniformly in the dyadic level and all auxiliary indices, when the coefficient norm is the exact phase-adapted pullback of physical Sobolev derivatives.

After a fixed core cutoff the resulting coefficient is admissible in every local mixed mean/nonzero product estimate at the same fixed derivative order.

This closes the reconstruction--Leray intertwining obligation. The next task is to formulate the whole-space angular-mean contraction directly in `mathfrak M_{sigma,m}` and couple it to the existing analytic nonzero lattice fixed point.