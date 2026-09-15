# Source-native `sigma` schedule for exact infinite-stage tiling

**Status:** PROVED GLOBAL SCHEDULING THEOREM FROM THE EXISTING TRAPPED-SPINE AND SOURCE-COORDINATE IDENTITIES. This note replaces the first-passage/fixed-q-decrement formulation of `native_variable_step_exact_cross_scale_tiling.md` by a cleaner schedule in the exact global source clock

\[
\sigma=-\log(1-t).
\]

The advantage is decisive: no monotonicity or uniform sign condition for `D_t q` is required. Every stage is assigned directly a source-native logarithmic time length

\[
\boxed{
\Delta\sigma_j
:=\sigma_{j+1}-\sigma_j
=\Lambda\varepsilon_j S_j,
\qquad
\varepsilon_j=q_j^h,
}
\tag{SN1}

and the trapped-spine identity

\[
q(\sigma)=\frac{e^{-\sigma}}{d(\eta(\sigma))},
\qquad
0<d_-\le d\le d_+<\infty,
\]

converts this directly into the `O(S_j)` fast-coordinate length required by the exact zero-residual machinery.

The earlier first-passage packing theorem remains a useful geometric diagnostic but is no longer the preferred exact global schedule.

## 1. Exact trapped-spine clock

Along the exact realized-background spine from `profile_characteristic_trapped_spine.md`,

\[
\boxed{
q(\sigma)=\frac{e^{-\sigma}}{d(\eta(\sigma))},
\qquad
\sigma=-\log(1-t),
}
\tag{SN2}

with

\[
\boxed{
0<d_-\le d(\eta(\sigma))\le d_+\le1
}
\tag{SN3}

for every sufficiently late `sigma`.

Hence

\[
\boxed{
c_qe^{-\sigma}\le q(\sigma)\le C_qe^{-\sigma}}
\tag{SN4}

with fixed positive constants.

No monotonicity of `q(sigma)` is asserted or needed.

## 2. Define the native stage sequence

Choose a fixed design constant `Lambda>0` and a sufficiently late starting point `sigma_0`.

Recursively set

\[
\boxed{
\sigma_{j+1}
=\sigma_j+\Lambda\varepsilon_jS_j,
\qquad
\varepsilon_j:=q(\sigma_j)^h.
}
\tag{SN5}

Because `h>0` and `q(sigma)->0`,

\[
\varepsilon_jS_j\to0
\]

for the source polynomial factor `S_j`; increase the starting level so that

\[
\boxed{
0<\Delta\sigma_j<\frac1{10}.}
\tag{SN6}

Thus every late stage is a near-identity motion in the exact global clock.

## 3. The stage sequence cannot accumulate at finite `sigma`

Suppose for contradiction that

\[
\sigma_j\uparrow\sigma_\infty<\infty.
\]

Then by (SN4),

\[
q(\sigma_j)\ge c_qe^{-\sigma_\infty}>0,
\]

so

\[
\varepsilon_j\ge c_\varepsilon>0.
\]

Also `S_j>=1`. Hence (SN5) gives

\[
\Delta\sigma_j\ge\Lambda c_\varepsilon>0,
\]

contradicting convergence of `sigma_j`.

Therefore

\[
\boxed{
\sigma_j\to\infty.
}
\tag{SN7}

Consequently

\[
\boxed{
t_j:=1-e^{-\sigma_j}\uparrow1}
\tag{SN8}

and, by (SN4),

\[
\boxed{q_j:=q(\sigma_j)\to0.}
\tag{SN9}

Thus the schedule contains infinitely many stages and accumulates only at the desired finite physical time.

## 4. Relative q-change is automatically small

From (SN2),

\[
\log\frac{q_{j+1}}{q_j}
=-\Delta\sigma_j
-\log\frac{d_{j+1}}{d_j}.
\tag{SN10}

The exact profile ODE on the compact trapped rectangle has uniformly bounded `d eta/d sigma`. Since `d(eta)=1-eta^2` has bounded logarithmic derivative there,

\[
\left|\log\frac{d_{j+1}}{d_j}\right|
\le C_d\Delta\sigma_j.
\tag{SN11}

Therefore

\[
\boxed{
\left|\log\frac{q_{j+1}}{q_j}\right|
\le C\Delta\sigma_j
=C\Lambda\varepsilon_jS_j
=o(1).
}
\tag{SN12}

Hence all q-normalized frames, source coefficients and phase data vary only by `o(1)` across one late stage, even if the instantaneous q-derivative changes sign.

This is exactly the perturbative condition required by the finite gate inverse-function arguments.

## 5. Physical time length

Since

\[
\frac{dt}{d\sigma}=1-t=e^{-\sigma}=q(\sigma)d(\eta(\sigma)),
\]

for `sigma in [sigma_j,sigma_{j+1}]`, (SN3), (SN6), and (SN12) imply

\[
\boxed{
\Delta t_j
\asymp
q_j\Delta\sigma_j
=
\Lambda q_j\varepsilon_jS_j
=
\Lambda q_j^{1+h}S_j.
}
\tag{SN13}

In particular the normalized physical-time length relative to the stage scale is

\[
\boxed{
\Delta s_j
:=\frac{\Delta t_j}{q_j}
=O(\Lambda\varepsilon_jS_j).
}
\tag{SN14}

This is the upper bound that a first-passage schedule did not supply without a sign condition on `D_t q`.

## 6. Source fast coordinate length

The exact source temporal-coordinate identity used in `native_variable_step_exact_cross_scale_tiling.md` is

\[
dT=\varepsilon\,dV
\]

(up to the fixed orientation convention), where `T` is normalized physical time and `V` is the fast pulse coordinate.

Since (SN14) gives

\[
\Delta T_j=O(\varepsilon_jS_j)
\]

and `epsilon` changes only by `1+o(1)` over one stage,

\[
\boxed{
\Delta V_j=O(\Lambda S_j).
}
\tag{SN15}

Thus the **entire stage** lies in exactly the `O(S_j)` fast-time regime for which the finite-collar exact zero-residual estimates have already been proved.

No separate fixed-ratio logarithmic bridge is required.

## 7. Fitting the complete nine-lobe cell

The corrected nine-lobe cell has physical duration

\[
\Delta t_j^{cell}
\le C_{cell}q_j^{1+h}S_j.
\tag{SN16}

Choose

\[
\boxed{\Lambda>2C_{cell}/c_t,}
\tag{SN17}

where `c_t>0` is the lower comparison constant in (SN13). Then the allocated stage interval has enough physical room for the complete finite circuit plus positive buffers.

Because both the allocated stage and the exact correction problem have `O(S_j)` fast length, the stage may be treated as one exact phase-adapted zero-residual solve.

## 8. Compatibility with the whole-space mean propagator

`global_fixed_order_leray_oseen_propagator.md` proves in normalized physical time `s` the fixed-order inequality

\[
\frac d{ds}\|m\|_{H^{m_0}}^2
+c\varepsilon\|m\|_{H^{m_0+1}}^2
\le C_{M,m_0}\|m\|_{H^{m_0}}^2+C\|F\|_{H^{m_0}}^2,
\]

with `C_{M,m_0}` independent of relay level.

By (SN14), one complete stage has

\[
|I_j|=O(\Lambda\varepsilon_jS_j).
\]

Therefore its homogeneous mean propagator satisfies

\[
\boxed{
\|\mathcal V_j\|_{H^{m_0}\to H^{m_0}}
\le
\exp(C_O\Lambda\varepsilon_jS_j).
}
\tag{SN18}

This is precisely the near-identity Oseen factor needed for mean-tail inheritance. The feared high-derivative background loss has already been removed by the fixed-order whole-space theorem.

## 9. Revised global architecture

The preferred schedule is now

\[
\boxed{
\sigma_{j+1}-\sigma_j
=\Lambda q_j^hS_j,
}
\]

not a prescribed q-ratio and not a first-passage q decrement.

One stage consists of:

1. one complete self-renewing nine-lobe active cell;
2. all dirty reserve generation and routed waste;
3. all inter-collar transport;
4. the small q/frame shift to the next canonical normalized section;
5. one exact whole-space nonzero/mean correction solve.

The stage has `O(S_j)` fast length and `O(epsilon_j S_j)` normalized physical length.

## 10. Consequence

The scalar monotonicity issue for `q` is removed from the exact global construction. In particular, no proof of

\[
-\dot q\ge c>0
\]

on the whole trapped corridor is needed.

The remaining global analysis is now:

- close the source-normalized inherited mean/pressure tail using (SN18);
- re-audit reserve-waste energy summability under the present variable `sigma` schedule;
- prove compatible finite-stage exact solutions define one smooth solution on every compact time interval before `t=1`;
- prove the renewed designated packet forces the intended blowup norm as `t up to1`.

No global unforced Navier--Stokes blowup theorem is claimed here.
