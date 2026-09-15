# Immediate sibling obstruction in the second beta-(2,1) active collar

**Status:** PROVED PRINCIPAL/EXACT-ENVELOPE OBSTRUCTION TO A PASSIVE SECOND COLLAR. After the exact first active gate has produced the transported beta-two packet `P`, the second intended event

\[
P+D\longrightarrow E
\]

cannot be treated as a two-input collision unless the old catalyst `C` has already been physically removed from the overlap. In the current reset architecture `C` remains present. Therefore the same second collar also contains the quadratic sibling interaction

\[
\boxed{P+C\longrightarrow F:=2C+D.}
\]

At the finite-`u_*=4` ordered cleanup point the principal growing projection of this sibling is nonzero and its exact leaf-action defect relative to the natural beta-three envelope is strongly positive. Hence `F` cannot be assigned to the action-subcritical remainder. The second collar must itself be actively gated (or preceded by a new physical support theorem that removes `C`).

This note does not yet enumerate the complete second-gate critical block. It identifies the first unavoidable additional row and corrects the input-state model for the second collar.

## 1. State entering the second collar

The first active gate closes the shortcut exit coordinates but does not annihilate the original incoming packets as physical fields. Thus after the first collar the relevant leading characters are

\[
C,\qquad D,\qquad P=C+D.
\tag{SG2-1}
\]

The second intended edge is

\[
\boxed{P+D\to E=C+2D.}
\tag{SG2-2}
\]

If `C` overlaps the same second collision region, the quadratic Navier--Stokes nonlinearity simultaneously sees

\[
\boxed{P+C\to F=2C+D.}
\tag{SG2-3}
\]

No routing label can suppress (SG2-3) once all three physical fields coexist.

## 2. Exact finite-u ordered working point

Use the source-safe cleanup point

\[
u_*=4,
\qquad
\delta\approx0.175549605869429326,
\qquad
x=1-\delta\approx0.824450394130570674.
\tag{SG2-4}
\]

Use the ordered finite-`u` collision spacing recorded in `beta21_finite_u_cleanup_window.md`:

\[
\eta=0.005,
\qquad
s\approx0.213506242359214.
\tag{SG2-5}
\]

Thus the second collision time is

\[
\boxed{t_2=s+\eta\approx0.218506242359214.}
\tag{SG2-6}
\]

At this time the reduced slopes are

\[
z_C(t_2)=1+t_2,
\tag{SG2-7}
\]

\[
z_D(t_2)=1-2\delta+t_2,
\tag{SG2-8}
\]

\[
z_P(t_2)=x+t_2.
\tag{SG2-9}
\]

Numerically,

\[
\boxed{
\begin{aligned}
z_C&\approx1.218506242359214,\\
z_D&\approx0.867407030620355,\\
z_P&\approx1.042956636489785.
\end{aligned}}
\tag{SG2-10}
\]

## 3. Intended and sibling beta-three slopes

For the intended sum `(beta_P,beta_D)=(2,1)`,

\[
z_E
=\frac{2z_P+z_D}{3}
=x-\frac\delta3+t_2,
\tag{SG2-11}
\]

so

\[
\boxed{z_E\approx0.984440101199975.}
\tag{SG2-12}
\]

For the sibling sum `(beta_P,beta_C)=(2,1)`,

\[
z_F
=\frac{2z_P+z_C}{3}
=x+\frac\delta3+t_2,
\tag{SG2-13}
\]

hence

\[
\boxed{z_F\approx1.101473171779594.}
\tag{SG2-14}
\]

Both outputs have signed beta three.

## 4. Both principal quadratic projections are nonzero

For a sum interaction the principal growing projection is the exact source-frame expression

\[
A_+^+
=\frac{s_1-s_2}{2}
\left[
\frac{b_1-b_2+s_t(b_1s_1-b_2s_2)}{1+s_t^2}
+
\frac{b_1\sqrt{1+s_1^2}-b_2\sqrt{1+s_2^2}}
{\sqrt{1+s_t^2}}
\right],
\tag{SG2-15}
\]

with `s_j=u_* z_j`.

At the working point this gives

\[
\boxed{\kappa_{PD\to E}\approx+0.8589500478,}
\tag{SG2-16}
\]

and

\[
\boxed{\kappa_{PC\to F}\approx-0.5602544598.}
\tag{SG2-17}
\]

Thus neither edge is near a principal Leray/polarization zero. Source-frame `O(S_*^{-1})` corrections cannot erase either fixed nonzero margin at sufficiently high dyadic level.

## 5. Exact action of the transported P packet

Let `E_{beta,4}` denote the exact finite-`u` envelope primitive. At the first collision time `t_1=s`, the promoted `P` action is

\[
A_P(t_1)
=\mathcal E_{1,4}(z_C(t_1))
+\mathcal E_{1,4}(z_D(t_1)).
\tag{SG2-18}
\]

Transport it homogeneously to `t_2`:

\[
\boxed{
A_P(t_2)
=A_P(t_1)
+\mathcal E_{2,4}(z_P(t_2))
-\mathcal E_{2,4}(z_P(t_1)).
}
\tag{SG2-19}
\]

High-precision evaluation gives

\[
\boxed{A_P(t_2)\approx-0.105197271463439.}
\tag{SG2-20}
\]

At the same time,

\[
\boxed{
\mathcal E_{1,4}(z_D(t_2))
\approx-0.024078630504080,
}
\tag{SG2-21}
\]

\[
\boxed{
\mathcal E_{1,4}(z_C(t_2))
\approx-0.066036217374094.
}
\tag{SG2-22}
\]

## 6. Intended E and sibling F are both promoted far above their natural envelopes

The intended second-generation action is

\[
A_E(t_2)
=A_P(t_2)+\mathcal E_{1,4}(z_D(t_2)),
\tag{SG2-23}
\]

so

\[
A_E(t_2)
\approx-0.129275901967519.
\tag{SG2-24}
\]

Its natural beta-three envelope is

\[
\mathcal E_{3,4}(z_E)
\approx-1.911749628106056,
\tag{SG2-25}
\]

hence the intended promoted headroom is

\[
\boxed{
A_E-\mathcal E_{3,4}(z_E)
\approx+1.782473726138538.
}
\tag{SG2-26}
\]

For the sibling,

\[
A_F(t_2)
=A_P(t_2)+\mathcal E_{1,4}(z_C(t_2))
\tag{SG2-27}
\]

and therefore

\[
A_F(t_2)
\approx-0.171233488837534.
\tag{SG2-28}
\]

while

\[
\mathcal E_{3,4}(z_F)
\approx-2.909875828132590.
\tag{SG2-29}
\]

Thus

\[
\boxed{
A_F-\mathcal E_{3,4}(z_F)
\approx+2.738642339295056>0.
}
\tag{SG2-30}
\]

The unwanted sibling is therefore even farther above its natural envelope than the intended `E` packet.

On the source action scale this is an exponentially large relative effect. It cannot be absorbed by a fixed algebraic power of `epsilon` or by the source curl/frame remainder.

## 7. Structural consequence

The following second-collar model is invalid:

\[
\boxed{
(P,D)\text{ only}
\quad\Longrightarrow\quad
E\text{ only}.}
\tag{SG2-31}
\]

The actual leading physical overlap is at least

\[
\boxed{
(C,D,P)\text{ present}
\quad\Longrightarrow\quad
E\text{ and }F\text{ generated}.}
\tag{SG2-32}
\]

Therefore the first exact active gate does not by itself make the second event passive. A valid architecture must choose one of two routes:

1. prove a **physical support-removal theorem** placing `C` outside the second `P-D` overlap before `t_2`; or
2. construct a **second active gate** that keeps the intended `E` output while cancelling `F` and every further supercritical descendant generated inside the second collar.

No source-support theorem currently removes `C` at this stage. Hence the conservative current route is the second active-gate audit.

## 8. New frontier

The next exact problem is

\[
\boxed{
\textbf{enumerate the full second-collar promoted/critical descendant block generated from }(C,D,P).}
}
\tag{SG2-33}

Unlike the first collar, natural growing/neutral classification alone is insufficient: `F` is homogeneously beta-three decaying at its present slope but is strongly **promoted by its source interaction**. Therefore the audit must track both

- naturally critical characters; and
- homogeneously decaying characters whose forced genealogical action lies above their natural envelope.

Only after that enumeration should the second control budget and its response-rank theorem be fixed.

No autonomous full reset cell or unforced Navier--Stokes blowup theorem is claimed.
