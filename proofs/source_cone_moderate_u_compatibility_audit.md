# Source stress-cone audit for the moderate-`u_*` cleanup window

**Status:** SOURCE-LINE AUDIT COMPLETE / COMPATIBILITY REDUCED TO ONE UNQUANTIFIED SOURCE CONSTANT. The published OpenAI construction does **not** impose an intrinsic requirement that `u_*` be asymptotically large. It requires only one strict cone inequality. However, the paper proves the needed cone margin by compactness and does not publish a numerical lower bound for it. Therefore the present cleanup window `u_*<4.964756...` is **not yet source-certified**, but it is also **not ruled out**.

Primary source: OpenAI, *Finite Time Blowup for Navier--Stokes*, Theorem 4.6(iii), equations (4.26), (7.1), and the choice immediately before (7.2), plus Proposition C.3.

## 1. Exact source requirement on `u_*`

At each representative point the source defines the tangential frame and growth parameter and then states that the strict cone margin permits choosing one `u_*>0` such that

\[
\boxed{
\frac{u_*}{\sqrt{1+u_*^2}}>R_* ,
}
\tag{SC1}
\]

where

\[
\boxed{
R_*:=\sup_{[X_a,X_b]\times[-1,1]}
\left|
 c_0\,
 \frac{T_{0,*}\cdot K}{T_{0,*}\cdot N}
\right|<1.
}
\tag{SC2}
\]

After that single choice the source freezes `u_*` and defines the packet shear by

\[
s(v)=\sigma\left(\frac{u_*}{2}+\frac{u_*v}{L_s}\right).
\]

Thus the paper does **not** state a separate lower bound such as `u_*>=10`, `u_*>>1`, or `u_*=M^2`. Large `u_*` was a design choice in our older v0.8 family, not a source theorem requirement.

## 2. Theorem 4.6 converts the unknown ratio to the cone-margin constant

Theorem 4.6(iii) supplies a fixed `kappa in (0,2)` such that, for the unit stress direction `n=T_0/|T_0|`,

\[
n_\theta+t_s n_z\ge\kappa,
\tag{SC3}
\]

and

\[
(v_s-2)(n_z-t_s n_\theta)^2
\le
(2-\kappa)(n_\theta+t_s n_z)^2.
\tag{SC4}
\]

The source identities immediately before (7.2) give

\[
c_0^2=\frac{v_s-2}{2},
\tag{SC5}
\]

and identify the quotient without `c_0` with

\[
\left|
\frac{n_z-t_sn_\theta}{n_\theta+t_sn_z}
\right|.
\tag{SC6}
\]

Therefore (SC4)--(SC6) imply the uniform estimate

\[
\boxed{
R_*^2\le1-\frac\kappa2.
}
\tag{SC7}
\]

A sufficient source-compatible condition on a proposed `u_*` is consequently

\[
\frac{u_*^2}{1+u_*^2}
>1-\frac\kappa2,
\]

i.e.

\[
\boxed{
\kappa>\frac{2}{1+u_*^2}.
}
\tag{SC8}
\]

This is sufficient because (SC7) may not be sharp; the exact criterion remains (SC1).

## 3. Numerical thresholds for the cleanup window

The exact-source cleanup computation in `beta21_finite_u_cleanup_window.md` gives

\[
\boxed{u_{\rm crit}\approx4.964756115.}
\tag{SC9}
\]

At the upper endpoint,

\[
\frac{u_{\rm crit}}{\sqrt{1+u_{\rm crit}^2}}
\approx0.9803121065,
\tag{SC10}
\]

and the sufficient Theorem-4.6 margin is

\[
\boxed{
\kappa>\frac{2}{1+u_{\rm crit}^2}
\approx0.07797635.
}
\tag{SC11}
\]

For the concrete working point `u_*=4`,

\[
\frac4{\sqrt{17}}\approx0.97014250,
\]

so the sufficient margin is

\[
\boxed{
\kappa>\frac2{17}\approx0.11764706.
}
\tag{SC12}
\]

For `u_*=2`, the corresponding sufficient requirement is the much stronger

\[
\kappa>0.4.
\tag{SC13}
\]

Hence, **using only the published `kappa`-bound**, existence of at least one source-compatible value inside the cleanup window would follow from

\[
\boxed{\kappa>0.07797635.}
\tag{SC14}
\]

Again, (SC14) is sufficient, not necessary: the exact ratio `R_*` can be smaller than the upper bound in (SC7).

## 4. What the source actually proves about `kappa`

Proposition C.3 proves Theorem 4.6(iii) as follows. The admissible cone inequalities are strict in the interior. At both radial edges the limiting normalized stress direction lies strictly inside the cone; in fact the cone-defect expression has limiting value `2`. The relevant positive quantities extend continuously to the compact closed annulus. Their compact positive minima then produce a single

\[
0<\kappa<2.
\]

This is an existence/compactness argument. The paper does **not** evaluate that minimum numerically and does not give an explicit lower bound such as `kappa>0.08` or `kappa>0.12`.

Consequently, the published theorem alone cannot certify (SC11) or (SC12).

## 5. Verdict

The moderate-`u_*` cleanup mechanism survives the source audit in the following precise sense:

\[
\boxed{
\text{the source does not require }u_*\gg1;
\quad
\text{it requires only }u_*/\sqrt{1+u_*^2}>R_*.
}
\tag{SC15}
\]

But the current paper leaves `R_*` (equivalently a usable numerical `kappa`) unquantified. Therefore

\[
\boxed{
\text{`u_*=4` is presently SOURCE-COMPATIBLE CONDITIONALLY, not SOURCE-CERTIFIED.}
}
\tag{SC16}
\]

The exact next proof obligation is no longer vague: obtain either

\[
\boxed{R_*<0.9803121065}
\]

for at least one explicit admissible leading profile (enough for some value below `u_crit`), or the stronger convenient bound

\[
\boxed{\kappa>0.07797635.}
\]

For the specific `u_*=4` working point one needs either

\[
R_*<0.9701425001
\]

or, by the sufficient theorem bound,

\[
\kappa>2/17.
\]

## 6. Research consequence

This audit changes the priority. There is no reason yet to abandon the moderate-`u_*` directed-cleanup architecture. The decisive source-side task is to **quantify the cone margin of an explicit profile**. The Appendix B/C construction contains several existentially chosen finite parameters, so this may require a separate certified numerical reconstruction rather than merely rereading Theorem 4.6.

Until that reconstruction is done, all later support-gated cascade claims should carry the hypothesis `(SC1)` with `u_*<u_crit` rather than assuming the source cone automatically permits `u_*=4`.