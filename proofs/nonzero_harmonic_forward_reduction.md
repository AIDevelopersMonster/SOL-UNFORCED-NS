# Full-linearized forward reduction for the nonzero harmonic block

**Status:** PROVED ABSTRACT/SOURCE-EMBEDDED REDUCTION. This note repairs a gap in the first version of `forward_relay_input_output_closure.md`: mixed terms with the designated packets cannot simply be declared small in operator norm. They must be absorbed into the full linearized evolution. After doing this, the entire nonzero-angular-harmonic block admits a bounded forward propagator and a small nonlinear fixed point on a bounded relay collar. The remaining local equation is the angular-mean block of Section 8 of the source construction.

This is not yet a proof of exact local zero-force Navier--Stokes closure, because the angular mean is not contained in the two-generator nonzero-harmonic lattice.

## 1. Correct small parameter

Start from one finite source-type correction state adapted to the v0.8 designated overlap. The conservative choice is the source stage-0 exponents:

\[
B_0=0.7,
\qquad
C_0^*=1.2,
\]

while the primary nonzero wave amplitude has exponent `1/2`.

Thus the supported nonzero-harmonic defect is not, in general, exponentially flat. Relative to the primary wave scale its conservative smallness is

\[
\boxed{
\rho_{\rm alg,\ell}
:=S_*^{C_M}\varepsilon^{B_0-1/2}
=S_*^{C_M}\varepsilon^{1/5}.
}
\tag{N1}

The v0.8 action filter adds a second, much smaller contribution

\[
\rho_{\rm act,\ell}
:=S_*^{C_M}e^{-c_MS_*}.
\tag{N2}

We therefore use

\[
\boxed{
\rho_\ell
:=C_M(\rho_{\rm alg,\ell}+\rho_{\rm act,\ell})
\longrightarrow0.
}
\tag{N3}

Calling the whole defect `F_flat` was too strong; only the action-subcritical and source cutoff/base pieces are flat. The stage-0 supported wave residual is algebraically small.

## 2. Weighted nonzero-harmonic spaces

For `nu=(a,b) in Z^2\setminus{0}` let

\[
|\nu|_1=|a|+|b|.
\]

Define, for `r=0,1`,

\[
\boxed{
\|z\|_{\mathfrak A_{\sigma,r}}
=
\sum_{\nu\ne0}
 e^{\sigma|\nu|_1}
 (1+|\nu|_1)^r
 \|z_\nu\|_{\rm pkt}.
}
\tag{N4}

The packet seminorm contains one fixed finite collection of slow/source derivatives and the source-localized envelope weights. The `r=1` norm pays for one output-carrier factor in the Navier--Stokes bilinear symbol.

## 3. Split the full linearized operator correctly

Let `U_0` denote the fixed approximate relay state: slow base, the designated parent/catalyst/child packets, and one fixed finite collection of source-type mean corrections. Write the nonzero-harmonic correction as `z`.

The equation linearized at `U_0` is not the mode-diagonal pulse operator alone. It has the form

\[
\boxed{
\partial_v z
=\mathcal D(v)z+\mathcal K(v)z+f+\mathcal B(z,z),
}
\tag{N5}

where:

- `D` is the mode-diagonal source pulse/frame/viscous operator;
- `K z` contains **all** mixed linear terms `B(U_0,z)+B(z,U_0)` not already included in `D`, together with the fixed localized coefficient perturbations;
- `f` is the remaining supported nonzero-harmonic defect;
- `B(z,z)` is quadratic in the new correction.

This removes the unjustified claim that the mixed term must have an operator norm tending to zero.

## 4. Smoothing for the diagonal evolution

Freeze one admissible v0.8 design `M` and one bounded correction interval `I=[v_-,v_+]`. The finite-critical-block theorem gives bounded evolution on the finitely many low modes. On the high stable modes the principal rate satisfies

\[
\Gamma_\nu(v)\le-c_M|\nu|_1^2.
\]

The source frame matrices and their inverses are uniformly bounded for the frozen design. Hence the diagonal fundamental solution `V_D(v,w)` obeys

\[
\boxed{
\|V_D(v,w)g\|_{\mathfrak A_{\sigma,0}}
\le C_M\|g\|_{\mathfrak A_{\sigma,0}},
}
\tag{N6}

and

\[
\boxed{
\|V_D(v,w)g\|_{\mathfrak A_{\sigma,1}}
\le
C_M\bigl(1+(v-w)^{-1/2}\bigr)
\|g\|_{\mathfrak A_{\sigma,0}}.
}
\tag{N7}

Indeed, on the high block this is the elementary estimate

\[
(1+n)e^{-c_Mn^2(v-w)}
\le C_M(1+(v-w)^{-1/2}),
\]

while the low block is finite.

## 5. The designated mixed operator is first order, not small

The field `U_0` has only a fixed finite set of designated angular/lattice shifts at principal order, plus fixed finite source corrections. The source incompressibility calculation leaves at most one output-carrier factor. Therefore

\[
\boxed{
\|\mathcal K(v)z\|_{\mathfrak A_{\sigma,0}}
\le C_M\|z\|_{\mathfrak A_{\sigma,1}},
}
\tag{N8}

uniformly on the bounded relay interval.

No small factor is asserted in (N8). This is the correct treatment of the parent/catalyst/child mixed linearization.

## 6. Full linearized forward propagator

Variation of constants relative to `D` gives

\[
V(v,w)
=V_D(v,w)
+
\int_w^v V_D(v,s)\mathcal K(s)V(s,w)\,ds.
\tag{N9}

The kernel

\[
h(t)=C_M(1+t^{-1/2})
\]

is integrable on every bounded interval. Choose a subdivision length `d_M>0` so that

\[
\int_0^{d_M}h(t)\,dt<\frac12.
\]

On each subinterval the Volterra map is a contraction in the standard graph norm; concatenating finitely many subintervals across `I` gives a full propagator with constants depending only on the frozen design and `|I|`.

Consequently

\[
\boxed{
\|V(v,w)g\|_{\mathfrak A_{\sigma,0}}
\le K_M\|g\|_{\mathfrak A_{\sigma,0}},
}
\tag{N10}

and the one-derivative parabolic smoothing persists:

\[
\boxed{
\|V(v,w)g\|_{\mathfrak A_{\sigma,1}}
\le
K_M(1+(v-w)^{-1/2})
\|g\|_{\mathfrak A_{\sigma,0}}.
}
\tag{N11}

The constants are independent of a harmonic truncation and correction stage because `K` is the fixed linearization at `U_0`, not a stage-dependent sequence of inverses.

## 7. Quadratic Duhamel estimate

The source-embedded bilinear symbol theorem gives

\[
\boxed{
\|\mathcal B(z_1,z_2)\|_{\mathfrak A_{\sigma,0}}
\le C_M
\|z_1\|_{\mathfrak A_{\sigma,1}}
\|z_2\|_{\mathfrak A_{\sigma,1}}.
}
\tag{N12}

Using (N11),

\[
\begin{aligned}
&\left\|
\int_{v_-}^{v}
V(v,s)\mathcal B(z,z)(s)\,ds
\right\|_{\mathfrak A_{\sigma,1}}\\
&\qquad\le
C_M
\int_{v_-}^{v}
(1+(v-s)^{-1/2})ds
\|z\|_{C(I;\mathfrak A_{\sigma,1})}^2\\
&\qquad\le C_{M,I}\|z\|^2.
\end{aligned}
\tag{N13}

The same calculation gives the usual bilinear Lipschitz estimate.

## 8. Nonzero-harmonic fixed point, conditional on a mean input

Let `m` be an angularly invariant mean correction lying in a small fixed source mean class. Its effect on the nonzero harmonics is another first-order coefficient perturbation, and for `m` in a sufficiently small ball it is absorbed into `K` without changing (N10)--(N11) except for the design constant.

Thus, for each such `m`, the Duhamel equation

\[
\boxed{
 z(v)=V_m(v,v_-)z_{\rm in}
 +\int_{v_-}^{v}V_m(v,s)
 [f_m(s)+\mathcal B(z,z)(s)]\,ds
}
\tag{N14}

has a unique solution whenever

\[
\|z_{\rm in}\|_{\mathfrak A_{\sigma,1}}
+\|f_m\|_{L^\infty\mathfrak A_{\sigma,0}}
\le c_{M,I}
\]

and, in particular, for the relay defect size (N3) at sufficiently large dyadic level.

Moreover

\[
\boxed{
\|z(m)\|_{C(I;\mathfrak A_{\sigma,1})}
\le C_{M,I}\rho_\ell,
}
\tag{N15}

and the solution depends locally Lipschitz-continuously on `m` and on the incoming nonzero-harmonic correction.

Therefore the full local problem admits a Lyapunov--Schmidt-type reduction

\[
\boxed{
\text{exact nonzero harmonics }z=z(m)
\quad\Longrightarrow\quad
\text{one remaining angular-mean equation for }m.
}
\tag{N16}

## 9. Divergence-free source class on the nonzero block

The unknown is taken in the source potential representation. Each harmonic velocity is realized as the exact curl of its oscillatory vector potential, retaining conjugate pairs. Therefore every partial sum is real and divergence-free, and the analytic lattice convergence in `A_{sigma,1}` passes this identity to the full nonzero-harmonic sum.

The associated nonzero pressure harmonics are those supplied by the amplitude/Leray equations. Thus the reduction above takes place inside the exact divergence-free source class; no post-hoc projection of the velocity is needed.

## 10. What remains

The angular mean `nu=0` is not part of the lattice estimate (N4). Quadratic products of a harmonic with its conjugate generate this block even when every nonzero descendant is action-subcritical.

The source handles it by the Section 8 pressure/radial inverses, the auxiliary-torus zero-mean temporal inverse, and the five-dimensional moment correction. Those maps must be incorporated into an **exact infinite correction scheme** before one can conclude

\[
R(U)=0
\]

for the complete local field.

Thus the corrected local frontier is the mean block, not the nonzero-harmonic lattice.
