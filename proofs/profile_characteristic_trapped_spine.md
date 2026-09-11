# A trapped material characteristic in the active similarity annulus

**Status:** PROVED SOURCE-DERIVED BACKGROUND THEOREM. The theorem is for the realized axisymmetric background `u_B` of OpenAI Proposition 5.5. It removes the cumulative slow-profile drift obstruction for the *geometry* of an infinite relay spine. It does **not** by itself close the autonomous oscillatory amplitude recurrence or the global unforced assembly.

Primary source: OpenAI, *Finite Time Blowup for Navier--Stokes*, Lemma 4.1, equations (4.7)--(4.9), Theorem 4.6, Proposition 4.10, Appendix B (especially (B.1), (B.14), Proposition B.5), and Proposition 5.5 / (5.42).

## 1. Exact leading material equations in similarity coordinates

Recall

\[
\tau=1-t,
\qquad
A=\frac12+h,
\qquad
D=\frac12-h,
\qquad
\tau=q(1-\eta^2),
\qquad
z=q^D\eta,
\qquad
X=\frac{r^2}{2q}.
\tag{TS1}
\]

Put

\[
d:=1-\eta^2,
\qquad
L:=1-2h\eta^2.
\tag{TS2}
\]

The leading axisymmetric field is

\[
u_z^{(0)}=q^{-A}U(X,\eta),
\qquad
r u_r^{(0)}=V_0(X,\eta).
\tag{TS3}
\]

Lemma 4.1 gives

\[
q_t=-L^{-1},
\qquad
q_z=\frac{2\eta q^{1-D}}{L},
\tag{TS4}
\]

\[
\eta_t=\frac{D\eta}{qL},
\qquad
\eta_z=\frac{d}{q^D L},
\tag{TS5}
\]

and

\[
X_t=\frac{X}{qL},
\qquad
X_z=-\frac{2\eta X}{q^D L},
\qquad
X_r=\frac rq.
\tag{TS6}
\]

Since `A+D=1`, the leading material derivative satisfies

\[
\boxed{
D_t^{(0)}q
=-\frac{1-2\eta U}{L}.
}
\tag{TS7}
\]

Define, exactly as in source (4.8),

\[
\boxed{
W=1-2D\eta A_X(U)-d\,\partial_\eta A_X(U),
\qquad
H_c=D\eta+dU.
}
\tag{TS8}
\]

Then (TS5) gives immediately

\[
\boxed{
D_t^{(0)}\eta
=\frac{H_c}{qL}.
}
\tag{TS9}
\]

For `X`, use source (4.7),

\[
V_0=
\frac XL
\left(2\eta U-2D\eta A_X(U)-d\partial_\eta A_X(U)\right).
\tag{TS10}
\]

Substitution into (TS6) yields the exact cancellation

\[
\begin{aligned}
D_t^{(0)}X
&=\frac{X}{qL}
-\frac{2\eta XU}{qL}
+\frac{V_0}{q}\\
&=\frac{XW}{qL}.
\end{aligned}
\]

Hence

\[
\boxed{
D_t^{(0)}X=\frac{XW}{qL},
\qquad
D_t^{(0)}\eta=\frac{H_c}{qL}.
}
\tag{TS11}
\]

These equations are not an extra model: they are an exact consequence of the source similarity coordinates and leading incompressible background.

## 2. A simultaneous zero of `(W,H_c)` inside the active annulus

The source construction supplies opposite signs on the four faces of the rectangle

\[
\mathcal A=[X_a,X_b]\times[-1,1].
\]

### Inner radial face

Proposition 4.10 fixes

\[
X_a=4/\Lambda.
\tag{TS12}
\]

Proposition B.5 leaves the analytic axis profile unchanged for `X<=X_a`. In the analytic construction, (B.14) gives

\[
W=W_*+\Lambda^{-1}B,
\tag{TS13}
\]

with `B` uniformly bounded on the fixed scaled interval, while (B.1) gives

\[
\boxed{-W_*>2.8}
\tag{TS14}
\]

uniformly for `eta in [-1,1]`. The hierarchy chooses `Lambda` sufficiently large before the final profile is fixed. Thus there is a source-dependent constant `c_a>0` such that

\[
\boxed{W(X_a,\eta)\le-c_a<0}
\tag{TS15}
\]

for all `eta`.

The later joining/shear operations do not alter the first edge; this is also stated in the proof of Theorem 4.6.

### Outer radial face

Theorem 4.6(v) gives

\[
U=0\quad\text{for }X\ge X_v,
\qquad X_v<X_b,
\tag{TS16}
\]

and the exact moment identity

\[
M(\infty,\eta)=\int_0^\infty U(x,\eta)\,dx=0.
\tag{TS17}
\]

Since `U` vanishes beyond `X_v`, (TS17) implies

\[
A_X(U)(X_b,\eta)=0,
\qquad
\partial_\eta A_X(U)(X_b,\eta)=0.
\]

Therefore

\[
\boxed{W(X_b,\eta)=1>0.}
\tag{TS18}
\]

### Axial faces

At `eta=+-1`, `d=0`, so (TS8) gives exactly

\[
\boxed{
H_c(X,-1)=-D<0,
\qquad
H_c(X,1)=D>0
}
\tag{TS19}
\]

for every `X`.

The map

\[
(X,\eta)\mapsto (W(X,\eta),H_c(X,\eta))
\]

is continuous. Equations (TS15), (TS18), and (TS19) satisfy the Poincare--Miranda sign conditions. Hence there exists

\[
\boxed{
(X_*,\eta_*)\in(X_a,X_b)\times(-1,1)
}
\tag{TS20}
\]

such that

\[
\boxed{
W(X_*,\eta_*)=0,
\qquad
H_c(X_*,\eta_*)=0.
}
\tag{TS21}
\]

Thus the leading similarity flow has at least one stationary profile point in the active annulus.

At a zero of `H_c`,

\[
U=-\frac{D\eta}{d}.
\]

Consequently, if

\[
\chi:=1-2\eta U,
\]

then

\[
\chi
=1+\frac{2D\eta^2}{d}
=\frac{1-2h\eta^2}{1-\eta^2}
=\frac Ld>0.
\tag{TS22}
\]

Hence at the leading stationary profile point

\[
\boxed{
D_t^{(0)}q=-\frac1{d_*}<0.
}
\tag{TS23}
\]

Along the corresponding leading material trajectory, `X=X_*`, `eta=eta_*`, and therefore

\[
\boxed{
q(t)=q(t_0)-\frac{t-t_0}{d_*}.
}
\tag{TS24}
\]

It reaches `q=0` in finite physical time while its normalized profile position remains fixed.

## 3. Exact realized background: asymptotically autonomous profile dynamics

The actual source background is `u_B`, not only its leading term. Proposition 5.5 / (5.42) gives uniformly on a fixed enlargement of the active annulus

\[
q^A u_{z,B}=U+O(q^{2h}),
\tag{TS25}
\]

and

\[
q^{1/2}u_{r,B}
=\frac{V_0}{\sqrt{2X}}+O(q^{2h}),
\tag{TS26}
\]

with the same form after every prescribed fixed number of normalized derivatives.

Repeating the calculation of Section 1 therefore gives the exact material-coordinate system for `u_B` in the form

\[
\boxed{
\dot X
=\frac{XW+R_X(q,X,\eta)}{qL},
\qquad
\dot\eta
=\frac{H_c+R_\eta(q,X,\eta)}{qL},
}
\tag{TS27}
\]

where, on the fixed annulus,

\[
\boxed{
|R_X|+|R_\eta|\le C q^{2h}.
}
\tag{TS28}
\]

The natural global clock is not `-log q` (whose monotonicity would require an extra argument), but

\[
\boxed{\sigma:=-\log\tau=-\log(1-t).}
\tag{TS29}
\]

Since `tau=qd`, one has `d sigma/dt=1/tau=1/(qd)`. Thus (TS27) becomes

\[
\boxed{
\frac{dX}{d\sigma}
=\frac dL\left(XW+R_X\right),
\qquad
\frac{d\eta}{d\sigma}
=\frac dL\left(H_c+R_\eta\right).
}
\tag{TS30}
\]

On any strip bounded away from `eta=+-1`, this vector field is uniformly bounded, and its nonautonomous error is exponentially small:

\[
q^{2h}
=\left(\frac{e^{-\sigma}}d\right)^{2h}
\le C e^{-2h\sigma}.
\tag{TS31}
\]

## 4. Reverse-time trapping gives an exact background spine

By continuity of `H_c` and the strict signs (TS19), choose a fixed `delta_eta>0` so small that, uniformly in `X in [X_a,X_b]`,

\[
H_c(X,-1+\delta_\eta)\le-c_\eta<0,
\qquad
H_c(X,1-\delta_\eta)\ge c_\eta>0.
\tag{TS32}
\]

Put

\[
\boxed{
\mathcal R
=[X_a,X_b]\times[-1+\delta_\eta,1-\delta_\eta].
}
\tag{TS33}
\]

Because (TS15), (TS18), and (TS32) are strict, (TS28)--(TS31) imply that for all sufficiently large `sigma` the forward vector field in (TS30) points **strictly outward** on every face of `R`:

- at `X=X_a`, `dX/dsigma<0`;
- at `X=X_b`, `dX/dsigma>0`;
- at `eta=-1+delta_eta`, `deta/dsigma<0`;
- at `eta=1-delta_eta`, `deta/dsigma>0`.

Equivalently, the reverse-time vector field points strictly inward on all four faces.

Fix a sufficiently large `sigma_0`. For every `N>sigma_0`, choose one fixed interior point `Y_c in int R` as terminal data at `sigma=N` and solve (TS30) backward to `sigma_0`. Strict inward pointing for the reverse flow implies that the backward solution remains in `R`.

Its value at `sigma_0` lies in the compact rectangle `R`. Take `N_j -> infinity` and a convergent subsequence of these initial values,

\[
Y_{N_j}(\sigma_0)\to Y_0\in\mathcal R.
\]

Let `Y(sigma)` be the forward solution with initial value `Y_0`. For every finite `Sigma>sigma_0`, continuous dependence of ODE solutions on initial data gives

\[
Y_{N_j}\to Y
\]

uniformly on `[sigma_0,Sigma]` once `N_j>Sigma`. Since every `Y_{N_j}` lies in the closed rectangle `R`, so does `Y`. As `Sigma` was arbitrary,

\[
\boxed{
Y(\sigma)=(X(\sigma),\eta(\sigma))\in\mathcal R
\quad\text{for every }\sigma\ge\sigma_0.
}
\tag{TS34}
\]

This is an exact material characteristic of the realized background `u_B` that remains forever in the active similarity annulus as `t up to 1`.

Because `eta` stays a fixed positive distance from `+-1`,

\[
0<d_{\min}\le d(\eta(\sigma))\le1.
\]

Therefore

\[
\boxed{
q(\sigma)=\frac{e^{-\sigma}}{d(\eta(\sigma))}\asymp e^{-\sigma}\to0.
}
\tag{TS35}
\]

Also

\[
r(\sigma)=\sqrt{2qX}\to0,
\qquad
z(\sigma)=q^D\eta\to0.
\tag{TS36}
\]

Thus the exact background spine approaches the singular point while staying in a fixed compact subset of the active profile annulus.

## 5. Stability of the trapping mechanism

The proof used only four strict boundary inequalities. Therefore it is open under any velocity perturbation `delta u` satisfying, on the boundary of `R`,

\[
q^A\delta u_z=o(1),
\qquad
q^{1/2}\delta u_r=o(1)
\tag{TS37}
\]

as `q->0`.

This is the correct robustness form for a later global relay assembly: primary oscillatory velocities are smaller than the leading tangential background by the source factor `epsilon^{1/2}=q^{h/2}`, and the mean/nonzero correction classes carry further positive powers. However this note does **not** assume that the infinite unforced assembly has already been constructed; (TS37) is only the stability criterion it must satisfy.

## 6. Consequence for cross-scale relay geometry

The previous small-log-step argument worried implicitly that `O(L_vartheta)` profile drift could accumulate without bound over infinitely many scale transitions. Equation (TS34) removes that geometric failure mode for the realized background: one can choose a material spine that remains in one fixed compact active rectangle for all sufficiently late times.

The source cone margins of Theorem 4.6 are uniform on the closed annulus and independent of physical `q`. Hence a relay construction whose local constants are chosen uniformly on `R` does not lose admissibility merely because the slow profile point drifts from stage to stage.

The natural stage clock is `sigma=-log(1-t)`. Along the trapped spine, `q asymp exp(-sigma)`, so any sequence

\[
\sigma_j=\sigma_0+jL
\]

with fixed `L>0` gives geometric physical concentration up to uniform constants.

## 7. What is closed and what is not

Closed here:

\[
\boxed{
\text{there exists an exact }u_B\text{-material spine staying in the active annulus for all late times.}
}
\]

In particular, an infinite relay sequence is not obstructed by inevitable escape of the slow similarity coordinates `(X,eta)`.

Still open:

1. the oscillatory **amplitude renewal problem** -- one-step nonvanishing of a transported child does not by itself prevent multiplicative amplitude decay over infinitely many stages;
2. supply/recycling of every designated parent mode needed by the next relay;
3. placement of the complete interacting supernodes around the trapped spine with all non-designated cross-products controlled;
4. one global exact unforced solution, rather than a sequence of independently exact local collars;
5. finite-time blowup for unforced 3D Navier--Stokes.

The next attack should therefore move from geometric trapping to autonomous regeneration of the complete designated wave state.