# Chart-invariant physical carrier scale

**Status:** DERIVED FROM SOURCE NORMALIZATIONS. This corrects the earlier working claim that the physical carrier at a fixed physical point gains a factor `2^((1+h)/2)` when one passes from one overlapping dyadic chart to the next.

Primary source: OpenAI, *Finite Time Blowup for Navier–Stokes*, equations (4.4)–(4.5), (4.11), (6.1), (6.6), (7.1)–(7.4).

## 1. Profile and chart coordinates

Let

\[
A=\frac12+h,
\qquad
X=\frac{r^2}{2q}.
\]

The order-zero physical tangential velocity is

\[
u_\theta^{(0)}=q^{-A}E(X,\eta),
\qquad
u_z^{(0)}=q^{-A}U(X,\eta).
\]

In a dyadic chart of scale \(Q\), the source uses

\[
R_Q=\frac r{\sqrt Q}
=\sqrt{\frac qQ}\,\sqrt{2X}
\]

and multiplies physical velocity by \(Q^A\). Therefore the order-zero chart tangential components are

\[
V_Q=\left(\frac Qq\right)^A E,
\qquad
G_Q=\left(\frac Qq\right)^A U.
\]

The chart angular velocity is

\[
F_Q:=\frac{V_Q}{R_Q}
=\left(\frac Qq\right)^{A+1/2}
\frac{E}{\sqrt{2X}}.
\]

Set

\[
c_Q:=\left(\frac Qq\right)^{A+1/2}
=\left(\frac Qq\right)^{1+h}.
\]

Then

\[
\boxed{F_Q=c_Q F_{\rm prof}}
\tag{C1}
\]

with \(F_{\rm prof}=E/\sqrt{2X}\).

## 2. The frozen shear scales by the same factor

The source defines the chart shear vector

\[
g_Q=(R_Q(F_Q)_{R_Q},(G_Q)_{R_Q}).
\]

Since

\[
R_Q\partial_{R_Q}=2X\partial_X
\]

at fixed \((q,Q,\eta)\), the first component of \(g_Q\) carries the factor \(c_Q\). Also

\[
\partial_{R_Q}X=\frac{Q}{q}R_Q
=\sqrt{\frac Qq}\sqrt{2X},
\]

so the second component carries the same factor. Equivalently, using the source identity

\[
g_0=F_0(-a,b_s),
\]

where \(a,b_s\) are dimensionless profile quantities, one obtains directly

\[
\boxed{g_Q=c_Q g_{\rm prof}.}
\tag{C2}
\]

Hence the unit direction

\[
N=\frac{g_Q}{|g_Q|},
\qquad K=N^\perp
\]

is independent of the dyadic chart used to represent the same order-zero physical point.

## 3. Scaling of \(\lambda_0\)

The source defines

\[
\lambda_{0,Q}^2
=-2F_QN_\theta\bigl(2F_QN_\theta+|g_Q|\bigr).
\]

By (C1)–(C2), both \(F_Q\) and \(|g_Q|\) acquire the same positive factor \(c_Q\). Therefore

\[
\boxed{
\lambda_{0,Q}=c_Q\lambda_{0,{\rm prof}}.
}
\tag{C3}
\]

This is the factor that was omitted in the bootstrap carrier-scaling heuristic.

## 4. Exact cancellation of the dyadic chart scale

For the source pulse,

\[
k_Q=\lceil\varepsilon_Q^{-1/2}\rceil,
\qquad
\varepsilon_Q=Q^h,
\]

and

\[
B_{s,Q}^2
=
\frac{\lambda_{0,Q}}
{\varepsilon_Q k_Q^2(1+u_*^2)^{3/2}}.
\]

Thus the ceiling in \(k_Q\) cancels exactly from the product

\[
\boxed{
k_QB_{s,Q}
=
\frac{\sqrt{\lambda_{0,Q}}}
{\sqrt{\varepsilon_Q}(1+u_*^2)^{3/4}}.
}
\tag{C4}
\]

The normalized spatial operators satisfy

\[
D_r,\ D_z,\ D_\theta
=\sqrt Q\times(\text{physical spatial derivative}),
\]

so the leading physical carrier prefactor is

\[
\Omega_Q
:=Q^{-1/2}k_QB_{s,Q}.
\]

Insert (C3), \(c_Q=(Q/q)^{1+h}\), and \(\varepsilon_Q=Q^h\):

\[
\begin{aligned}
\Omega_Q
&=
Q^{-1/2}
\frac{(Q/q)^{(1+h)/2}\sqrt{\lambda_{0,{\rm prof}}}}
{Q^{h/2}(1+u_*^2)^{3/4}}\\
&=
\frac{q^{-(1+h)/2}\sqrt{\lambda_{0,{\rm prof}}}}
{(1+u_*^2)^{3/4}}.
\end{aligned}
\]

Therefore

\[
\boxed{
\Omega_Q
=
\Omega_{\rm phys}(q,X,\eta),
\quad\text{independent of }Q
}
\tag{C5}
\]

for two dyadic charts representing the same order-zero physical point and using the same \(u_*\).

## 5. Consequence for neighboring bands

At a point where two dyadic cutoffs overlap, changing from \(Q\) to \(Q/2\) does **not** create the physical carrier ratio

\[
2^{(1+h)/2}.
\]

That factor appears only if \(\lambda_0\) is incorrectly held fixed while the chart changes. The source normalization makes \(\lambda_0\) transform by (C3), cancelling the apparent dyadic frequency jump.

Thus the earlier repository statement

\[
\Omega_\ell\asymp Q_\ell^{-(1+h)/2}
\]

is not the correct comparison between overlapping charts at a fixed physical point.

The correct intrinsic scale is

\[
\boxed{
\Omega_{\rm phys}
\asymp q^{-(1+h)/2},
}
\tag{C6}
\]

with the profile-dependent factor displayed exactly in (C5).

## 6. Research consequence

The old relay design condition

\[
\beta_1+\beta_2=\frac{17}{12}
\]

was motivated by the spurious neighboring-chart ratio and must not be used as a physical cross-band locking law.

For collinear reference tangential directions at one physical interaction point, a unit-β child instead requires, depending on the chosen harmonic branch,

\[
\boxed{\epsilon_1\beta_1+\epsilon_2\beta_2=1,\qquad \epsilon_j\in\{\pm1\}.}
\tag{C7}
\]

The dyadic bands still matter for localization, coefficient classes, and auxiliary covering speed. They do **not** themselves supply a physical frequency jump.

This correction changes the relay architecture substantially and is now the governing carrier-scaling rule for SOL-UNFORCED-NS.
