# Compact-orbit exact-reset obstruction for the low-`u` bilateral mechanism

**Status:** PROVED ALGEBRAIC OBSTRUCTION / LOCAL TARGET CORRECTED.  A nonzero finitely supported orbit vector cannot be an exact fixed vector of the limiting bilateral Poincare map.  Since the actual source primary bank at fixed `S` has compact slope support, the literal statement “the complete finite designated primary bank resets exactly by itself” is impossible already at principal homogeneous level.

This does **not** obstruct an exact full-state reset.  The correct object is

\[
\boxed{
\text{central designated orbit profile}
+\text{ an infinite source-small analytic-lattice tail}
}
\]

whose full Poincare image equals itself.  The tail may live in the exact correction sector rather than in the compact primary-wave bank.  The source boundary defect is exponentially small, so this corrected target is compatible with the existing correction budget.

Accordingly, `beta21_lowu_exact_finiteS_local_reset.md` must not be interpreted as an exact compact-bank fixed-vector theorem.

## 1. Shift convention

Let `R` be the bilateral unit shift

\[
(Rc)_j=c_{j-1}.
\tag{CO1}
\]

The catalyst limiting fixed equation is

\[
\boxed{e^{\lambda_CR}c=Rc,}
\tag{CO2}
\]

and the parent equation is

\[
\boxed{e^{\mu_PR}q=R^2q.}
\tag{CO3}

Both `lambda_C` and `mu_P` are nonzero at the selected low-`u` point.

## 2. No nonzero finitely supported catalyst fixed vector

Assume `c` is finitely supported and nonzero.  Let

\[
j_0:=\min\{j:c_j\ne0\}.
\]

Then

\[
c_j=0\qquad(j<j_0).
\]

Expand

\[
e^{\lambda_CR}
=I+\lambda_CR+\frac{\lambda_C^2}{2!}R^2+\cdots.
\]

At the leftmost nonzero component,

\[
(R^kc)_{j_0}=c_{j_0-k}=0
\qquad(k\ge1).
\]

Therefore

\[
\boxed{
(e^{\lambda_CR}c)_{j_0}=c_{j_0}\ne0.
}
\tag{CO4}

But

\[
(Rc)_{j_0}=c_{j_0-1}=0.
\tag{CO5}

Equations (CO4)--(CO5) contradict (CO2).

Hence

\[
\boxed{
\ker_{c_{00}}\left(e^{\lambda_CR}-R\right)=\{0\},
}
\tag{CO6}

where `c_00` denotes finitely supported bilateral sequences.

## 3. Parent sector

Let `q` be nonzero and finitely supported, with leftmost nonzero index `j_0`.  As above,

\[
(e^{\mu_PR}q)_{j_0}=q_{j_0}\ne0,
\]

whereas

\[
(R^2q)_{j_0}=q_{j_0-2}=0.
\]

Thus

\[
\boxed{
\ker_{c_{00}}\left(e^{\mu_PR}-R^2\right)=\{0\}.
}
\tag{CO7}

The obstruction is independent of the numerical working point; it uses only nonzero finite support and the positive reset shift.

## 4. Why the actual primary bank is finite at fixed `S`

The source Gaussian slot cutoff is supported in

\[
z\in[2/3,4/3].
\]

At fixed `S`, orbit slopes move by

\[
\Delta z_C\asymp S^{-1},
\qquad
\Delta z_P\asymp S^{-1}.
\]

Therefore only `O(S)` orbit indices can lie in the source-supported slope interval.  Outside this interval the primary source packet is exactly zero.

Thus the actual designated **primary-wave** orbit bank is finite at every finite source level.

The strict core `|z-x|<=w` used in the low-`u` action audit is even smaller; its boundary values are exponentially suppressed relative to the central action.

## 5. Consequence for the finite-`S` profile obligation

The missing theorem in
`beta21_lowu_finiteS_designated_profile_obligation.md`
cannot be stated as

\[
\mathcal P_{b,S}U_{b,S}=U_{b,S}
\]

with `U_{b,S}` restricted to a compact primary-bank sequence and no additional tail.

The correct finite-`S` decomposition is

\[
\boxed{
U_S
=U_{core,S}+z_{tail,S},
}
\tag{CO8}

where

- `U_core,S` is the canonical tangent-Gaussian orbit on the source-supported central bank;
- `z_tail,S` belongs to the completed analytic correction lattice and is not required to be a primary-wave packet;
- the full fixed equation is
  \[
  \boxed{\mathcal P_S(U_{core,S}+z_{tail,S})=U_{core,S}+z_{tail,S}.}
  \tag{CO9}
  \]

The zero-residual PDE correction and the Poincare handoff must therefore be solved simultaneously or by a Lyapunov--Schmidt decomposition.

## 6. Size of the boundary defect

On the strict orbit core, the large-deviation actions satisfy

\[
H_1\le-c_{bd,C}<0,
\qquad
H_2\le-c_{bd,P}<0
\]

at the artificial core boundary.  At the full Gaussian slot boundary the source cutoff is flat/zero and the physical central profile is even smaller.

Thus truncating an infinite tangent-Gaussian bilateral profile to the source-supported primary bank creates a handoff defect of the schematic size

\[
\boxed{
\|d_{bd,S}\|
\le S^Ae^{-cS}
}
\tag{CO10}

for fixed `A,c>0` in the already audited analytic/action norm.

This is the same scale already admitted by the local correction radius

\[
R_S
\lesssim
S^A\varepsilon^{a_*}+S^Ae^{-cS}.
\tag{CO11}

Therefore the compact-support obstruction changes the architecture but does not create a size obstruction.

## 7. Why the correction lattice can in principle carry the tail

The exact phase-adapted correction space is a completed weighted auxiliary Fourier lattice, not `c_00`.  The coupled zero-residual theorem already solves infinitely many non-designated harmonics by a forward Volterra/Banach argument.

Hence there is no algebraic requirement that the **full exact state** have finite harmonic support merely because the designated primary source bank does.

What must be proved is stronger than the old zero-residual theorem: the correction tail must satisfy the reset/handoff fixed equation as well as the PDE residual equation.

## 8. Corrected Lyapunov--Schmidt target

Let `X_core,S` be the smooth tangent-Gaussian profile sector and `X_tail,S` the analytic correction lattice.  Write the one-cell exact map as

\[
\mathscr P_S(U,z)
=
\begin{pmatrix}
\mathscr P_{core,S}(U,z)\\
\mathscr P_{tail,S}(U,z)
\end{pmatrix}.
\]

The corrected local theorem should solve

\[
\boxed{
\mathscr P_{core,S}(U,z)=U,
\qquad
\mathscr P_{tail,S}(U,z)=z,
}
\tag{CO12}

with

\[
U=U_{TG,S}+o(1)
\]

in the tangent-Gaussian profile norm and

\[
\boxed{
\|z\|_{tail}
\le S^A\varepsilon^{a_*}+S^Ae^{-cS}.
}
\tag{CO13}

The three macroscopic parameters and the root polarization/amplitude remain available to enforce the central dispersion/phase normalization.  The infinite-dimensional profile and tail equations are then solved by transport/Volterra methods, not by pretending the compact primary bank is an exact eigenvector.

## 9. Relation to spectral instability

`beta21_lowu_intercell_spectral_stability_audit.md` shows that arbitrary lattice-rough perturbations contain expanding directions.  Therefore (CO12) should not be attacked by a raw contraction on the full bilateral `ell^2` state.

The preferred decomposition is:

1. solve the smooth central profile equation using the first-order continuum/Volterra operator;
2. solve the exponentially small boundary and PDE tail in the analytic complement with its stable/full-symbol propagator;
3. use the finite macroscopic parameters for the remaining central normalization conditions.

This respects both the compact-support obstruction and the rough-spectrum instability.

## 10. Corrected current status

The valid local achievements are now:

- principal low-`u` bilateral mechanism and action gaps;
- one physical Cauchy root can generate both shift sectors by polarization tuning;
- leading continuum finite-`S` profile equation is physically Gaussian-admissible;
- exact zero Navier--Stokes residual can be solved around a prescribed designated state;
- source-supported boundary defect is exponentially small.

Still missing:

\[
\boxed{
\text{one exact full-state core+tail Poincare fixed point at finite }S.
}
\tag{CO14}

That theorem, not an exact compact-bank eigenvector theorem, is the next local publication threshold.
