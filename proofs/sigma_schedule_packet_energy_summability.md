# Packet-energy summability on the source-native `sigma` schedule

**Status:** PROVED. This note repairs the geometric-q assumption in `reserve_waste_energy_summability.md` after the global schedule was changed to

\[
\sigma_{j+1}-\sigma_j
=\Lambda\varepsilon_jS_j,
\qquad
\varepsilon_j=q_j^h.
\]

The new sequence `q_j` need not decay geometrically in the cell index. Nevertheless it decays at least like a very high negative power of `j`, which is more than sufficient for the packet-energy series. The proof uses only the trapped-spine identity `q=e^{-sigma}/d`, the source bound `0<h<=10^{-3}`, and `S_j>=1`.

The conclusion applies to any fixed finite number of normalized designated or routed-away packet lobes per stage.

## 1. Trapped-spine comparison

On the exact trapped spine,

\[
q_j
=\frac{e^{-\sigma_j}}{d_j},
\qquad
0<d_-\le d_j\le d_+\le1.
\tag{SE1}

Hence

\[
\varepsilon_j
=q_j^h
=e^{-h\sigma_j}d_j^{-h}.
\tag{SE2}

Define

\[
\boxed{Y_j:=e^{h\sigma_j}.}
\tag{SE3}

Then

\[
\boxed{Y_j\varepsilon_j=d_j^{-h}.}
\tag{SE4}

Because `d_j` stays in a fixed compact positive interval, there are fixed constants

\[
0<c_d\le Y_j\varepsilon_j\le C_d<\infty.
\tag{SE5}

## 2. Linear lower growth of `Y_j`

The native schedule gives

\[
\Delta\sigma_j
=\Lambda\varepsilon_jS_j,
\qquad S_j\ge1.
\tag{SE6}

Therefore

\[
\begin{aligned}
Y_{j+1}-Y_j
&=Y_j\left(e^{h\Delta\sigma_j}-1\right)\\
&\ge hY_j\Delta\sigma_j\\
&=h\Lambda Y_j\varepsilon_jS_j\\
&\ge h\Lambda c_d.
\end{aligned}
\]

Thus

\[
\boxed{
Y_j\ge Y_0+c_*j,
\qquad
c_*:=h\Lambda c_d>0.
}
\tag{SE7}

In particular,

\[
\boxed{Y_j\gtrsim1+j.}
\tag{SE8}

## 3. Polynomial upper bound for `q_j`

Since

\[
e^{-\sigma_j}=Y_j^{-1/h},
\]

(S1) and (SE8) give

\[
\boxed{
q_j
\le C(1+j)^{-1/h}.
}
\tag{SE9}

This crude estimate ignores the factor `S_j`, so the true decay is at least as fast. It is already overwhelmingly sufficient because `1/h>=1000`.

## 4. One normalized packet

The physical support/amplitude calculation of `reserve_waste_energy_summability.md` gives for every fixed normalized packet lobe

\[
\boxed{
\|W_j\|_{L^2}^2
\le C q_j^{\alpha},
\qquad
\alpha:=\frac12-2h.
}
\tag{SE10}

The source bound

\[
0<h\le10^{-3}
\]

implies

\[
\alpha>0.
\]

Insert (SE9):

\[
\|W_j\|_{L^2}^2
\le
C(1+j)^{-\alpha/h}.
\tag{SE11}

Now

\[
\boxed{
\frac\alpha h
=\frac1{2h}-2
\ge500-2
=498.
}
\tag{SE12}

Hence

\[
\boxed{
\sum_{j=0}^{\infty}\|W_j\|_{L^2}^2<\infty.
}
\tag{SE13}

The convergence margin is enormous.

## 5. Fixed finite packet bank per stage

Let at most `N_*<infinity` packet lobes occur at stage `j`, with `N_*` independent of `j` and normalized amplitudes in one fixed bounded set.

Then

\[
E_j^{packets}
\le C_*q_j^\alpha,
\]

so by (SE13)

\[
\boxed{
\sum_jE_j^{packets}<\infty.
}
\tag{SE14}

This includes simultaneously:

- the nine renewed designated unit-beta lobes;
- the finite beta-two designated parent packet(s);
- every fixed finite active-gate temporary packet family;
- every fixed finite dirty-reserve waste family routed away from the relay spine.

Thus the finite lobe architecture does not create an infinite kinetic-energy budget merely because infinitely many stages accumulate at `t=1`.

## 6. Correction of the earlier reserve-waste theorem

`reserve_waste_energy_summability.md` proved the one-stage energy exponent correctly but used a geometric sequence

\[
q_j=q_0\vartheta^j
\]

to sum it.

The preferred global architecture now uses the source-native `sigma` schedule instead. Equations (SE7)--(SE13) replace that geometric-series argument.

Therefore the conclusion of the reserve-waste theorem remains valid under the current schedule:

\[
\boxed{
\sum_jE_j^{waste}<\infty.
}
\tag{SE15}

No fixed-ratio q assumption is required.

## 7. Scope

This is a kinetic-energy summability result for the oscillatory/designated/reserve packet families. It does not by itself prove:

1. finite total energy of every component of the realized slow background;
2. a global exact solution on `[0,1)`;
3. uniform high-Sobolev summability as `t\uparrow1`;
4. blowup of a specific norm.

Those are separate global obligations.

For every fixed `T<1`, only finitely many sufficiently late stages have occurred, so the accumulation of high packet frequencies is compatible with ordinary smoothness on compact pre-accumulation time intervals.
