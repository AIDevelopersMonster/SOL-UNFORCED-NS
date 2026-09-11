# Reconstruction versus whole-space Leray: the remaining coefficient-space interface

**Status:** OPEN MICROLLOCAL INTERTWINING OBLIGATION / CORRECTION TO A TOO-FAST GLOBAL CLOSURE READING.

The preceding whole-space notes correctly prove that the physical Leray projector is bounded on ordinary physical `H^{m_0}(R^3)` and that the time-forward Oseen energy estimate is stable there. This does **not** yet imply that the resulting physical angular-mean solution belongs to the exact common-torus coefficient class used by `nonzero_harmonic_forward_reduction.md`.

This note isolates the missing bridge. It is the last local representation issue before one may promote the mean fixed point to an exact local relay theorem in the original packet calculus.

## 1. Two spaces are presently being used

The nonzero theorem is formulated before physical reconstruction. A coefficient field has the form

\[
a=a(x,y),\qquad y\in\mathbb T^2,
\]

with analytic/weighted control in the auxiliary Fourier index. The physical field is obtained by a phase reconstruction

\[
\boxed{
(\mathcal R_\ell a)(x)
=a\bigl(x,\Phi_\ell(x)\bigr),
}
\tag{RL1}
\]

where `Phi_ell` contains the fast radial/temporal/axial source phases.

The exact physical Leray projector is

\[
\boxed{
\mathbb P_{\rm ws}=I-\nabla\Delta^{-1}\operatorname{div}
}
\tag{RL2}
\]

on `R^3`.

The coefficient-space mean theorem would require an operator `P_coeff,ell` such that

\[
\boxed{
\mathbb P_{\rm ws}\mathcal R_\ell
=\mathcal R_\ell\mathbb P_{\rm coeff,\ell}
}
\tag{RL3}
\]

or at least a controlled approximate intertwining with a remainder lying in an already-small source class.

No such theorem has yet been proved in the branch.

## 2. Why ordinary H^m boundedness is insufficient

Physical Sobolev control gives, for `m_0>5/2`,

\[
\|u\|_{W^{1,\infty}(K)}
\lesssim\|u\|_{H^{m_0}(\mathbb R^3)}.
\tag{RL4}
\]

This is enough to multiply a compactly supported physical wave by `u` at a fixed derivative order. But the nonzero packet theorem also controls the genealogy of auxiliary harmonics and uses the weighted lattice norm

\[
\sum_{\nu\ne0}e^{\sigma|\nu|}(1+|\nu|)^r\|z_\nu\|_{\rm pkt}.
\tag{RL5}
\]

A physical `H^{m_0}` estimate alone does not reconstruct the individual auxiliary Fourier coefficients of `u`, nor their exponential lattice weight.

Hence the implication

\[
\boxed{
\|m\|_{H^{m_0}(\mathbb R^3)}\ll1
\quad\Longrightarrow\quad
m\text{ is admissible in the coefficient-space map }z=z(m)
}
\tag{RL6}
\]

has not been established.

## 3. Exact form on one auxiliary Fourier mode

Write

\[
a(x,y)=\sum_{k\in\mathbb Z^2}a_k(x)e^{2\pi i k\cdot y}.
\tag{RL7}
\]

Then

\[
\mathcal R_\ell a
=\sum_k a_k(x)e^{2\pi i k\cdot\Phi_\ell(x)}.
\tag{RL8}
\]

For one mode, physical differentiation gives

\[
\boxed{
\nabla_x\bigl(a_ke^{2\pi i k\cdot\Phi_\ell}\bigr)
=e^{2\pi i k\cdot\Phi_\ell}
\left[
\nabla a_k
+2\pi i\,(\nabla\Phi_\ell)^Tk\,a_k
\right].
}
\tag{RL9}
\]

Thus the physical Leray symbol is sampled near the local covector

\[
\boxed{
\Xi_{\ell,k}(x):=2\pi(\nabla\Phi_\ell(x))^Tk.
}
\tag{RL10}
\]

At principal WKB order one expects

\[
\boxed{
\mathbb P_{\rm ws}
\left(a_ke^{ik\cdot\Phi_\ell}\right)
\approx
e^{ik\cdot\Phi_\ell}
P\bigl(\Xi_{\ell,k}(x)\bigr)a_k,
}
\tag{RL11}
\]

with lower-order pseudodifferential corrections involving derivatives of `a_k` and `Phi_ell`.

Since `P(xi)` is homogeneous of degree zero, its derivatives obey

\[
|\partial_\xi^\alpha P(\xi)|
\lesssim_\alpha |\xi|^{-|\alpha|}.
\tag{RL12}
\]

Therefore large carrier frequency is potentially favorable, but only if `|Xi_{ell,k}|` has an adequate lower bound on the relevant coefficient lattice.

## 4. Two frequency regimes

The correct proof should split the auxiliary lattice.

### 4.1 High reconstructed physical frequency

If

\[
|\Xi_{\ell,k}(x)|\ge c\Lambda_\ell\langle k\rangle^{-A}
\tag{RL13}
\]

on the active collar, semiclassical pseudodifferential expansion of the order-zero Leray multiplier yields coefficientwise bounds with only polynomial losses in `k`. The existing exponential lattice weight `e^{sigma|k|}` absorbs every fixed polynomial loss.

In this regime one expects

\[
\boxed{
\|\mathbb P_{\rm coeff,\ell}a\|_{\mathfrak A_{\sigma',0}}
\le C_M\|a\|_{\mathfrak A_{\sigma,0}},
\qquad \sigma'<\sigma,
}
\tag{RL14}
\]

or, with a sharper analytic-symbol argument, possibly the same radius.

### 4.2 Low/near-cancelled reconstructed frequency

If `Xi_{ell,k}` can be small, the WKB expansion is not uniform. Those modes must be treated separately. The v0.8 branch already contains two relevant pieces of structure:

- the finite critical-block decomposition for nonzero harmonic modes;
- Diophantine lower bounds for the source phase directions.

What has not yet been checked is that these statements imply a uniform dichotomy for the **mean auxiliary lattice** entering the physical Leray projector.

This is now a finite, explicit arithmetic/microlocal audit rather than a generic pressure problem.

## 5. What would close the bridge

It is enough to prove the following coefficient-space Leray theorem.

### Target theorem

For one frozen relay design, there exist `sigma_*>0`, a fixed derivative order `m_0`, and `C_M<infty` such that the reconstructed whole-space projector admits an induced coefficient map satisfying

\[
\boxed{
\mathbb P_{\rm ws}\mathcal R_\ell a
=\mathcal R_\ell(\mathbb P_{\rm coeff,\ell}a),
}
\tag{RL15}
\]

on the source coefficient class, with

\[
\boxed{
\|\mathbb P_{\rm coeff,\ell}a\|_{\mathfrak A_{\sigma_*,0}^{m_0}}
\le C_M\|a\|_{\mathfrak A_{\sigma_*,0}^{m_0}}
}
\tag{RL16}
\]

uniformly in the dyadic level.

An approximate identity

\[
\mathbb P_{\rm ws}\mathcal R_\ell a
=\mathcal R_\ell(\mathbb P_{\rm coeff,\ell}a)+r_\ell
\tag{RL17}
\]

would also suffice if

\[
\|r_\ell\|
\le o(1)\|a\|
\tag{RL18}
\]

in the physical/core norm used by the nonlinear return map.

## 6. Consequence for the current fixed point

`mean_inhomogeneous_self_map_bound.md` correctly proves a physical-space Banach fixed point for the projected mean equation, assuming the nonlinear map is interpreted in that physical Sobolev realization.

However coupling this fixed point back into the already-proved coefficient-space nonzero theorem still requires (RL15)-(RL16) or an equivalent physical-space reformulation of the nonzero theorem.

Therefore the statement

\[
\text{“local mean fixed point closed”}
\]

is presently true only at the **physical projected mean subsystem** level, not yet at the full common-torus relay-system level.

## 7. Publication consequence

This gap is too central to hide in notation. The exact local whole-space zero-force relay theorem should **not** be declared publication-ready until the reconstruction--Leray bridge is proved.

The next attack is now sharply defined:

\[
\boxed{
\textbf{prove uniform coefficient-space control of the physical Leray projector under the source phase reconstruction.}
}
\]

If this succeeds, the pressure/localization/interface obstacles collapse into one bounded order-zero operator, and the branch can return immediately to the final local relay theorem assembly.