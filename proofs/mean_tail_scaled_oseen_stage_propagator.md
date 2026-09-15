# Scaled Oseen one-stage propagator for inherited mean tails

**Status:** PROVED FROM THE EXISTING WHOLE-SPACE FIXED-ORDER OSEEN THEOREM AND THE SOURCE-NATIVE `sigma` SCHEDULE. This closes the analytic hypothesis `(MT9)` isolated in `mean_tail_source_normalized_inheritance_reduction.md`.

The key inputs are already proved:

1. `global_fixed_order_leray_oseen_propagator.md` gives a whole-space fixed-order mean energy inequality in normalized physical time with a generator constant independent of relay level;
2. `sigma_native_exact_stage_schedule.md` gives one complete stage normalized physical length

\[
|I_j|=O(\Lambda\varepsilon_jS_j).
\]

Therefore the inherited homogeneous mean tail amplifies by only

\[
\exp(C_O\Lambda\varepsilon_jS_j),
\]

while the newly generated mean correction has the existing source-small size `S_j^C epsilon_j^{1-kappa_s}`.

## 1. Whole-space fixed-order energy inequality

Fix `m_0>=6`. The global whole-space theorem proves, in normalized physical time `s`,

\[
\boxed{
\frac d{ds}\|m\|_{H^{m_0}}^2
+c\varepsilon_j\|m\|_{H^{m_0+1}}^2
\le
C_{M,m_0}\|m\|_{H^{m_0}}^2
+C\|F\|_{H^{m_0}}^2.
}
\tag{OS1}

The constant

\[
C_{M,m_0}<\infty
\]

is independent of relay level, carrier frequency, harmonic truncation, and radial phase. All source-varying high-jet coefficient pieces have already been separated into an `o(1)` remainder in the proof of that theorem.

Discarding dissipation and applying Gronwall over a time interval of length `L` gives the homogeneous bound

\[
\boxed{
\|\mathcal V_j(s,s_0)f\|_{H^{m_0}}
\le
\exp(C_O L)\|f\|_{H^{m_0}}
}
\tag{OS2}

for a fixed design constant `C_O`.

## 2. One complete stage has short normalized physical duration

The source-native schedule is

\[
\sigma_{j+1}-\sigma_j
=\Lambda\varepsilon_jS_j,
\qquad
\varepsilon_j=q_j^h.
\]

`Sigma_native_exact_stage_schedule.md` (file `sigma_native_exact_stage_schedule.md`) proves

\[
\boxed{
|I_j|
\le C_s\Lambda\varepsilon_jS_j
}
\tag{OS3}

in the normalized physical time used by the mean Oseen equation.

Insert (OS3) into (OS2):

\[
\boxed{
\|\mathcal V_j\|_{H^{m_0}\to H^{m_0}}
\le
\exp(C_O'\Lambda\varepsilon_jS_j).
}
\tag{OS4}

Absorb the fixed `Lambda` into the design constant when convenient. This is exactly the near-identity homogeneous factor required by `(MT9)`.

## 3. Additive mean generated in one stage

The exact local zero-residual theorem and its inhomogeneous self-map estimate give, uniformly over the compact renewed gate/lobe state,

\[
\boxed{
\|m_j^{new}\|_{H^{m_0}}
\le
C_F S_j^{C_1}\varepsilon_j^{1-\kappa_s},
\qquad
\kappa_s=10^{-5}.
}
\tag{OS5}

The fixed finite nine-lobe enlargement changes only `C_F,C_1`; it does not change the positive epsilon exponent because the number of source profiles is independent of `j`.

Thus if `M_j` is the inherited whole-space mean state entering stage `j`, the linear-plus-new-source decomposition yields

\[
\boxed{
N_{j+1}
\le
\exp(C_O'\Lambda\varepsilon_jS_j)N_j
+C_F S_j^{C_1}\varepsilon_j^{1-\kappa_s},
}
\tag{OS6}

where `N_j` is the fixed-order whole-space Sobolev/phase-adapted norm controlling the finite jets required by the next cell.

Equation (OS6) is `(MT9)`.

## 4. Bootstrap with the inherited tail inside the coefficients

The whole-space Oseen theorem was first written around the reconstructed slow base. In the global relay, the already accumulated mean tail is also part of the actual advecting/background field.

This does not create a circular obstruction. Use the comparison exponent from `mean_tail_source_normalized_inheritance_reduction.md`: choose

\[
0<\mu<D=\frac12-h
\]

and bootstrap

\[
N_j\le Kq_j^{-\mu}.
\tag{OS7}

By Sobolev embedding and the source normalization, the induced coefficient perturbations satisfy

\[
q_j^A\|M_j\|_\infty
+q_j^{1/2}\|\partial_rM_j\|_\infty
+q_j^D\|\partial_zM_j\|_\infty
=o(1),
\tag{OS8}

with the analogous finite derivative bounds used by the fixed-order Oseen energy estimate.

Hence the accumulated tail changes the normalized Oseen generator by an operator whose fixed-order coefficient norm is `o(1)`. After increasing the starting level,

\[
C_O'\mapsto C_O'+1
\]

is enough to absorb this perturbation uniformly.

Thus (OS6) remains valid throughout the bootstrap region.

The discrete comparison argument of the inheritance reduction then improves/propagates (OS7), closing the induction.

## 5. Consequence: source-normalized inherited tail is negligible

Combining (OS6) with `mean_tail_source_normalized_inheritance_reduction.md`, for any

\[
\mu>
 h\kappa_s+\eta+rac{C_*}{\Lambda}
\]

one obtains, after choosing `Lambda` large and the starting level late,

\[
\boxed{
N_j\le C_\mu q_j^{-\mu}.
}
\tag{OS9}

Because

\[
h\kappa_s\le10^{-8}
\]

and `Lambda` is a free fixed design parameter, choose

\[
\boxed{\mu<D.}
\tag{OS10}

Then every normalized mean jet relevant to the relay coefficients tends to zero. In particular,

\[
q_j^A\|M_j\|_\infty\to0,
\]

\[
q_j^{1/2}\|\partial_rM_j\|_\infty\to0,
\]

\[
q_j^D\|\partial_zM_j\|_\infty\to0.
\tag{OS11}

The whole-space pressure gradient is controlled through the already-proved order-zero Leray/Riesz realization and inherits the same finite-jet smallness at the level required by the local gates.

## 6. What this closes

The previously open statement

\[
\boxed{
\text{old whole-space mean/pressure tails remain admissible at all later renewed cells}
}
\]

is now closed at fixed finite derivative order, under the same source/numerical certification assumptions as the local zero-residual theorem.

Strict local margins are therefore preserved from some global starting level onward:

- source-cone margins;
- action gaps;
- polarization nonvanishing;
- finite spectral separation;
- active-gate Jacobian margins.

The mean tail is allowed to grow in an unscaled whole-space norm by a tiny negative power of `q`; what matters is that every source-normalized local coefficient perturbation is `o(1)`.

## 7. Remaining global obligations

Closing the inherited mean tail does **not** yet prove a global unforced blowup solution. Remaining tasks include:

1. repair the routed-reserve energy summability proof for the source-native variable `sigma` schedule rather than a geometric q-sequence;
2. formulate finite-stage consistency/uniqueness so that the exact stage solutions define one exact smooth solution on every `[0,T]`, `T<1`;
3. prove finite total kinetic energy of the complete designated plus waste state;
4. prove a lower bound on the renewed designated packet that forces divergence of an appropriate regularity quantity as `t\uparrow1`.

No Clay-problem or complete unforced finite-time blowup theorem is claimed here.
