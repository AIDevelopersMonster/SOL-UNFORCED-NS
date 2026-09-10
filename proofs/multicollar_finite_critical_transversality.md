# Multi-collar transversality for a finite critical block

**Status:** PROVED ABSTRACT CONTROL THEOREM / CONDITIONAL RELAY APPLICATION. The theorem proves exact finite-dimensional rank for a family of scalar compact-support compatibility moments when their kernel functions are linearly independent on the relay interval. It generalizes `two_collar_compatibility_rank.md` from one moment to an arbitrary finite block. For SOL-UNFORCED-NS, the remaining source-specific task is to prove linear independence of the actual critical-mode moment kernels and realize the corresponding collar controls by exact localized curl-generated packets without destroying the designated child amplitude.

## 1. Finite compatibility system

Let `I=(v_-,v_+)` be the relay interval. Suppose the critical block has `N` complex compatibility functionals

\[
\mathcal M_i(p)=\sum_{j=1}^{N}J_{ij}p_j+O(|p|^2),
\qquad i=1,\dots,N,
\]

where `p_j in C` are amplitudes of `N` independently tunable narrow control collars.

At principal linear level assume

\[
J_{ij}=K_i(\tau_j),
\tag{M1}
\]

where `tau_j in I` are the collar centers and

\[
K_1,\dots,K_N:I\to\mathbb C
\]

are continuous moment kernels determined by the critical propagators and couplings.

The rank question is whether one can choose distinct collar centers so that

\[
\det[K_i(\tau_j)]_{i,j=1}^N\ne0.
\]

## 2. Sampling lemma

### Lemma 2.1

If the continuous functions `K_1,...,K_N` are linearly independent over `C` on `I`, then there exist distinct points

\[
\tau_1,\dots,\tau_N\in I
\]

such that

\[
\boxed{
\det[K_i(\tau_j)]_{i,j=1}^N\ne0.
}
\tag{M2}

### Proof

Proceed by induction on `N`.

For `N=1`, linear independence means `K_1` is not identically zero, so choose `tau_1` with `K_1(tau_1)!=0`.

Assume the statement for `N-1`. Since `K_1,...,K_{N-1}` are linearly independent, choose distinct `tau_1,...,tau_{N-1}` such that the `(N-1)x(N-1)` matrix

\[
A=[K_i(\tau_j)]_{i,j=1}^{N-1}
\]

is invertible.

For `tau in I`, define

\[
D(\tau)=
\det
\begin{pmatrix}
K_1(\tau_1)&\cdots&K_1(\tau_{N-1})&K_1(\tau)\\
\vdots&&\vdots&\vdots\\
K_N(\tau_1)&\cdots&K_N(\tau_{N-1})&K_N(\tau)
\end{pmatrix}.
\]

Expanding along the last column gives

\[
D(\tau)=\sum_{i=1}^Nc_iK_i(\tau),
\]

with coefficients `c_i` independent of `tau`. The cofactor of `K_N(tau)` is `det A != 0`, so not all `c_i` vanish. If `D(tau)` were identically zero, this would be a nontrivial linear relation among `K_1,...,K_N`, contradiction. Therefore `D(tau_N)!=0` for some `tau_N`. Since `D(tau_j)=0` for `j<N` because two columns coincide, the chosen `tau_N` is automatically distinct. ∎

## 3. Smooth narrow collars preserve rank

Fix a nonnegative bump `psi in C_c^infty((-1,1))` with unit integral and define

\[
q_{j,\delta}(v)
=\delta^{-1}\psi\!\left(\frac{v-\tau_j}{\delta}\right).
\]

The corresponding exact linearized compatibility matrix is

\[
J_{ij}(\delta)
=\int_I K_i(v)q_{j,\delta}(v)\,dv.
\tag{M3}
\]

By continuity,

\[
J_{ij}(\delta)\to K_i(\tau_j)
\qquad(\delta\to0).
\]

Hence

\[
\det J(\delta)	o\det[K_i(\tau_j)]\ne0.
\]

Therefore for all sufficiently small `delta`,

\[
\boxed{\det J(\delta)\ne0.}
\tag{M4}

Thus exact rank survives smooth localization.

## 4. Including a prescribed child-output condition

Suppose in addition one must prescribe one complex desired-child output

\[
\mathcal C(p)=C_*.
\]

Let its linearized kernel be `K_0`. Then use `N+1` complex collars and augment the kernel family to

\[
K_0,K_1,\dots,K_N.
\]

If this augmented family is linearly independent on `I`, the same sampling lemma yields centers

\[
\tau_0,\dots,\tau_N
\]

for which the `(N+1)x(N+1)` Jacobian of

\[
(\mathcal C,\mathcal M_1,\dots,\mathcal M_N)
\]

has nonzero determinant.

Hence the linearized system can simultaneously impose

\[
\boxed{
\mathcal C=C_*\ne0,
\qquad
\mathcal M_1=\cdots=\mathcal M_N=0.
}
\tag{M5}

The number `N+1` of complex controls is generically minimal: one complex equation is used to prescribe child output and `N` complex equations kill the `N` compatibility moments.

## 5. Persistence under small packet perturbations

Let `J_0` be a full-rank principal control matrix obtained above. If the exact localized packet system produces

\[
J_\ell=J_0+E_\ell,
\]

with

\[
\|E_\ell\|\to0
\qquad(\ell\to\infty),
\]

then invertibility persists for sufficiently large `ell`.

Indeed, if

\[
\|J_0^{-1}E_\ell\|<1,
\]

then

\[
J_\ell
=J_0(I+J_0^{-1}E_\ell)
\]

and the Neumann series gives

\[
\boxed{
\|J_\ell^{-1}\|
\le
\frac{\|J_0^{-1}\|}{1-\|J_0^{-1}E_\ell\|}.
}
\tag{M6}

The source-localized action-preservation theorem shows that the known phase/frame/curl corrections are algebraic in the dyadic level and therefore tend to zero after the principal controls are normalized at fixed design `M`.

## 6. Implicit-function consequence

Let `F(p,z)` collect the prescribed child-output equation and the finite compatibility moments, where `z` denotes the infinite stable-complement correction. Suppose

\[
F(p_0,0)=0
\]

and

\[
D_pF(p_0,0)
\]

is invertible by Sections 2–5. Then the finite-dimensional implicit-function theorem gives a unique local map

\[
\boxed{p=p(z)}
\tag{M7}
\]

for sufficiently small stable correction `z`, with

\[
F(p(z),z)=0.
\]

Thus the finite critical block can be slaved to the infinite stable complement once the kernel-independence hypothesis is verified for the actual relay system.

## 7. Relation to the stable-complement contraction

`analytic_quadratic_symbol_bound.md` proves that, after the critical variables are chosen at action-subcritical size, the infinite stable complement is contractive in the analytic weighted lattice space.

Combining that theorem with (M7) gives the standard Lyapunov-Schmidt architecture:

\[
\boxed{
\text{finite critical solve}
+\text{ infinite stable contraction}.
}
\tag{M8}

No infinite family of independent compatibility conditions remains.

## 8. What remains source-specific

This theorem reduces the finite-dimensional problem to one concrete condition:

\[
\boxed{
K_0,K_1,\dots,K_N
\text{ are linearly independent on the relay interval.}
}
\tag{M9}

For the first single feedback mode, `two_collar_compatibility_rank.md` already proves the relevant two-kernel independence through strict monotonicity of the ratio `mu(tau)/C(tau)`.

For the full v0.8 finite critical set, the next task is to derive the actual critical kernels from the principal propagators and couplings and test whether their Wronskian/sampling determinant is nonzero. If the kernel family is independent, the finite block is solved by this theorem; if a dependence appears, it identifies an exact structural obstruction and indicates how many additional independent control packet types are required.
