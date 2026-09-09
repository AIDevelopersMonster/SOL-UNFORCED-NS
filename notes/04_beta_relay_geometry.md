# Note 04 — β-relay geometry

Introduce an intermediate carrier scaling

\[
n_{\Phi,\beta}\approx \beta B_s(s e_r+K).
\]

At principal level:

- the direction of the shear-sensitive phase normal is unchanged;
- viscous damping scales like \(\beta^2\);
- two parent β-values can be selected so their sum matches the next physical band ratio.

## 1. Band ratio

Choose

\[
r=\frac{17}{12}.
\]

Then

\[
2^{(1+h)/2}=\frac{17}{12},
\qquad
h=2\log_2\frac{17}{12}-1
\approx0.005000681058366707<\frac1{100}.
\]

## 2. Corrections to earlier working witnesses

Two earlier bootstrap candidates are now deprecated for different reasons.

### v0.1

The pair

\[
\beta_1=0.93,
\qquad
\beta_2=\frac{73}{150}
\]

matched the next-band ratio algebraically, but

\[
\beta_2^{-2/3}>\frac32,
\]

so the second parent had no internal turning point in the raw pulse interval.

### v0.2

The pair

\[
\beta_1=\frac56,
\qquad
\beta_2=\frac7{12}
\]

fixed that issue, but the associated resonance computation used an envelope primitive carrying an erroneous extra factor \(\beta^{2/3}\). The correct common-\(L_s\) reduced primitive derived from the source pulse equation is

\[
\boxed{
I_\beta(x)
=
\log\!\big(x\beta^{2/3}\big)
-
\frac{\beta^2}{3}\big(x^3-\beta^{-2}\big),
}
\]

with

\[
I_\beta'(x)=F_\beta(x)=\frac1x-\beta^2x^2.
\]

Therefore the old v0.2 numerical witness is also deprecated.

This correction is recorded in `proofs/beta_phase_stability.md`.

## 3. Interior-turning threshold

The large-\(u_*\) turning point is

\[
x_\beta=\beta^{-2/3}.
\]

A sufficient condition for it to lie below the raw endpoint \(3/2\) is

\[
\boxed{
\beta>\left(\frac23\right)^{3/2}\approx0.544331.
}
\]

## 4. Preferred v0.3 rational relay pair

Use

\[
\boxed{
\beta_1=\frac{41}{48},
\qquad
\beta_2=\frac9{16}.
}
\]

Then

\[
\beta_1+\beta_2
=
\frac{41}{48}+\frac{27}{48}
=
\frac{17}{12}
=r.
\]

Both β-values exceed the interior-turning threshold. Their reduced turning points are

\[
\beta_1^{-2/3}\approx1.110806094,
\qquad
\beta_2^{-2/3}\approx1.467523222.
\]

Choose an exact rational coordinate for the decaying parent,

\[
\boxed{x_1=\frac{71}{48}\approx1.479166667.}
\]

For the second parent use opposite signed slope, \(x_2=-y_2\), and impose the reduced phase relation

\[
\boxed{
\beta_1x_1-\beta_2y_2=rx_c.
}
\tag{R1}
\]

Together with reduced envelope balance

\[
\boxed{
I_{\beta_1}(x_1)+I_{\beta_2}(y_2)=I_1(x_c),
}
\tag{R2}
\]

this leaves one scalar equation for \(y_2\), because

\[
x_c=\frac{\beta_1x_1-\beta_2y_2}{r}.
\]

The numerical root is

\[
\boxed{
y_2\approx0.9381374363215359,}
\]

which gives

\[
\boxed{x_c\approx0.519354743421351.}
\]

Both values lie strictly inside the raw interval \([1/2,3/2]\).

## 5. Transversality

Define

\[
R(y)
=
I_{\beta_1}(x_1)
+
I_{\beta_2}(y)
-
I_1\!\left(
\frac{\beta_1x_1-\beta_2y}{r}
\right).
\]

At the v0.3 root,

\[
\boxed{R'(y_2)\approx1.4449>1.4.}
\]

Thus the reduced resonance is transverse, not a tangential numerical coincidence.

This matters because the exact finite-\(u_*\) envelope differs from the reduced one by \(O(u_*^{-2})\) in \(C^1\). The implicit-function mechanism therefore predicts persistence of the relay root for all sufficiently large admissible \(u_*\).

## 6. Growth/decay orientation

For the reduced net-growth profile

\[
F_\beta(x)=\frac1x-\beta^2x^2,
\]

the v0.3 witness satisfies

\[
F_{41/48}(x_1)\approx-0.920262<0,
\]

\[
F_{9/16}(y_2)\approx+0.787472>0,
\]

\[
F_1(x_c)\approx+1.655737>0.
\]

Hence

\[
\boxed{
\text{decaying old parent}
+
\text{growing catalyst}
\longrightarrow
\text{growing child}
}
\]

survives after correcting the envelope primitive.

## 7. Finite-\(u_*\) numerical persistence check

Using the exact normalized envelope primitive from `proofs/beta_phase_stability.md`, keep \(\beta_1,\beta_2,x_1\) fixed and solve the exact envelope equation together with the same leading phase relation.

Representative roots are:

| \(u_*\) | \(y_2(u_*)\) | \(x_c(u_*)\) |
|---:|---:|---:|
| 10 | 0.9411505724 | 0.5181583512 |
| 20 | 0.9388940430 | 0.5190543261 |
| 50 | 0.9382586450 | 0.5193066165 |
| 100 | 0.9381677439 | 0.5193427095 |
| 1000 | 0.9381377394 | 0.5193546231 |

The roots converge to the reduced witness and preserve the required parent/child growth signs throughout this sample.

This is still a numerical persistence check, not a proof, but together with the transverse reduced root and the \(C^1\) asymptotic estimate it gives a clear route to a rigorous finite-\(u_*\) existence proposition.

## 8. Important asymmetry in the source geometry

The source pulse coordinate on a fixed sign rectangle satisfies

\[
|s(v)|=u_*\left(\frac12+\frac{v}{L_s}\right).
\]

Therefore two packets evaluated at the same physical \(v\) have the same \(|s|/u_*\). Our relay uses different reduced coordinates \(x_1\neq y_2\neq x_c\).

So a relay cannot be realized by simply placing all three packets on the same unshifted pulse rectangle.

The β-dependent recentering from `proofs/beta_phase_stability.md` is therefore not merely convenient: some additional **relative pulse translation / asynchronous support placement** is required to make the three local coordinates meet at one physical overlap collar.

This is now the central geometric proof obligation.

## 9. Status

- Correct envelope primitive: **DERIVED**.
- v0.3 reduced relay root: **NUMERICAL, TRANSVERSE**.
- finite-\(u_*\) persistence: **NUMERICAL CHECKED; analytic proof route identified**.
- realization by translated localized curl-generated packets: **OPEN**.
- sideband disposal: **OPEN**.
