# Strong-`H` active-renewal bifurcation in the beta-(2,1) reset family

**Status:** COMPUTER-ASSISTED EXACT-ENVELOPE BIFURCATION THEOREM. Once the reset architecture uses exact active gates rather than passive cleanup, the sign change that previously marked failure of the spent-catalyst cleanup mechanism becomes useful. The unavoidable leading root-generated fourth-state

\[
H=2D-C
\]

can feed the final edge

\[
H+D\to P_{new}=3D-C.
\]

For the exact turning-point family, the final renewed-parent action equation has no causal solution for `u<u_crit`, touches the reset face at the same critical value

\[
u_{crit}\approx4.96475611525,
\]

and has a causal pre-face root for the tested values `u>u_crit`.

Thus the old passive-cleanup sign restriction and the new active-renewal condition point in opposite directions. The active programme should no longer regard `u>u_crit` as excluded merely because the spent old catalyst is not passively below the renewed parent.

This note does not yet re-audit the first three active gates at a new value of `u`; that is the next mandatory redesign step.

## 1. Turning-point family

For each admissible `u`, let `delta=delta(u)` solve

\[
\boxed{
\mathcal E_{2,u}(1-\delta)
=\mathcal E_{1,u}(1-2\delta).
}
\tag{SH1}
\]

Set

\[
x=1-\delta,
\qquad
T=2\delta.
\tag{SH2}
\]

Then at the reset face

\[
z_D(T)=1,
\]

and the renewed beta-two character

\[
P_{new}=3D-C
\]

has reduced slope

\[
\boxed{z_{P_{new}}(T)=x.}
\tag{SH3}
\]

## 2. Use the strong root-generated `H`

The fourth-gate obstruction proves that the leading unavoidable `H=2D-C` is generated at the root action

\[
\boxed{
A_H^{root}(t)
=A_C(t)+2A_D(t).
}
\tag{SH4}

If this `H` interacts with `D` at time `t`, the newly generated beta-two `P_new` has source action

\[
\boxed{
A_{P_{new}}(t)
=A_C(t)+3A_D(t).
}
\tag{SH5}

The character slope at generation is

\[
\boxed{
z_{P_{new}}(t)
=1-3\delta+t.
}
\tag{SH6}

Propagating this beta-two packet to the reset face gives

\[
A_{P_{new}}(T)
=A_C(t)+3A_D(t)
+\mathcal E_{2,u}(x)
-\mathcal E_{2,u}(1-3\delta+t).
\tag{SH7}

The renewal requirement is

\[
A_{P_{new}}(T)=\mathcal E_{2,u}(x).
\]

The terminal target therefore cancels exactly from both sides, leaving the scalar equation

\[
\boxed{
F_u(t)
:=
\mathcal E_{1,u}(1+t)
+3\mathcal E_{1,u}(1-2\delta+t)
-\mathcal E_{2,u}(1-3\delta+t)
=0.
}
\tag{SH8}

This is the exact strong-`H` active-renewal equation.

## 3. Value at the reset face equals the old cleanup defect

At `t=T=2delta`,

\[
1-2\delta+T=1,
\]

and

\[
1-3\delta+T=1-\delta=x.
\]

Since

\[
\mathcal E_{1,u}(1)=0,
\]

we obtain

\[
F_u(T)
=\mathcal E_{1,u}(1+2\delta)
-\mathcal E_{2,u}(1-\delta).
\tag{SH9}

But `1+2delta=x+3delta`, so

\[
\boxed{
F_u(T)=\Delta_{clean}(u),
}
\tag{SH10}

where `Delta_clean` is exactly the spent-catalyst cleanup defect from `beta21_finite_u_cleanup_window.md`.

Therefore the previously computed sign change

\[
\Delta_{clean}(u_{crit})=0
\]

is automatically the reset-face bifurcation point of the strong-`H` renewal equation.

## 4. Numerical bifurcation

The companion script `experiments/beta21_strong_H_renewal_bifurcation.py` evaluates (SH8) using the exact finite-`u` envelope.

For all tested subcritical values `u<u_crit`,

\[
F_u(0)<0,
\qquad
F_u(T)<0,
\]

and no sign-changing causal root is found.

At

\[
\boxed{
u_{crit}\approx4.96475611525,}
\tag{SH11}
\]

one has

\[
F_{u_{crit}}(T)=0
\]

to working precision: the renewal root touches the reset face.

For tested values above the threshold, a causal root appears strictly before `T`.

Representative values are

\[
\begin{array}{c|c|c}
u&T&t_*\\ \hline
5.0&0.342193163003049&0.342151775970742\\
5.2&0.341005890368231&0.340747370554218\\
5.5&0.339464432540146&0.338928544601247\\
6.0&0.337394939818287&0.336494599305936\\
7.0&0.334514941909015&0.333122201545740\\
10.0&0.330464121566572&0.328407050537777
\end{array}
\tag{SH12}

with margins

\[
\begin{array}{c|c}
u&T-t_*\\ \hline
5.0&4.1387\times10^{-5}\\
5.2&2.5852\times10^{-4}\\
5.5&5.3589\times10^{-4}\\
6.0&9.0034\times10^{-4}\\
7.0&1.3927\times10^{-3}\\
10.0&2.0571\times10^{-3}
\end{array}
\tag{SH13}

Thus the final active-renewal event acquires a genuine positive causal margin once `u` moves above the old cleanup threshold.

## 5. Architectural reversal

In the passive-cleanup architecture, the desired condition was

\[
\Delta_{clean}(u)<0,
\]

because one wanted the spent old `C` to lie below the renewed parent at the reset face. This forced

\[
u<u_{crit}.
\]

The active-gate architecture no longer relies on discarding old `C` by action filtering. The old `C,D` parents remain explicitly in the finite controlled dynamics.

For the strong-`H` final renewal, the useful condition is instead

\[
F_u(T)=\Delta_{clean}(u)>0,
\]

together with `F_u` negative earlier in the causal interval, producing a pre-face root. This points to

\[
\boxed{
u>u_{crit}.}
\tag{SH14}

Hence the sign that invalidated passive cleanup is exactly the sign that opens the active-renewal route.

## 6. What this does and does not prove

This result proves an exact-envelope **design bifurcation**, not a complete reset cell at `u>u_crit`.

Changing `u` changes:

- the turning-point root `delta(u)`;
- all parent and descendant envelope rates;
- the finite naturally-critical sets and action defects;
- the frozen polarization coefficients;
- the PBH spectral separations;
- the admissible active-collar widths.

Therefore the first three active-gate theorems established at `u=4` cannot simply be transplanted to `u=5`, `6`, or another supercritical value by assertion.

The next mandatory programme step is to choose one supercritical source-safe working point, preferably with a visible final causal margin (for example `u=5.5` or `u=6`), and redo the finite critical/rank audits for gates one through three there.

If those audits preserve finite controllability, the strong-`H` route removes the two-scale fourth-gate obstruction and gives a plausible full active reset cell.

No full reset-cell or blowup theorem is claimed here.
