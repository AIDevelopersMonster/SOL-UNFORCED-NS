# Physical Fourier Poincare reduction: reset shear and beta-zero-memory obstruction

**Status:** PROVED PRINCIPAL/CAUCHY-STATE STRUCTURAL THEOREM AT THE CORRECTED `u=2.5` WORKING POINT, WITH NUMERICAL MARGINS REQUIRING INTERVAL CERTIFICATION FOR PUBLICATION. This note replaces the temporally localized active-control interpretation by genuine physical Fourier/Cauchy coordinates and proves two facts.

1. The beta-(2,1) character reset is an exact unipotent shear with a distinguished beta-zero invariant direction.
2. Using that invariant beta-zero direction as an autonomous Cauchy memory strong enough to remove the old catalyst inevitably creates a renewed beta-two parent that is exponentially too strong at the reset face. A same-character homogeneous preload cannot cancel even the minimal excess because it would require positive input action, above the natural source-envelope maximum.

Thus the simplest physical-Fourier Poincare repair based only on the existing rank-two `(P,C)` lattice and its beta-zero memory `M=P-2C` fails. The temporal-control rank calculations remain useful local response calculations, but they cannot be replaced merely by retaining `M` as a renewed physical Cauchy coordinate.

This theorem does **not** rule out every autonomous finite Fourier-state repair. It rules out the canonical beta-zero-memory repair and reveals the exact reset shear that every future physical-state construction must respect.

## 1. Corrected working point

Freeze

\[
u=2.5,
\qquad
\delta=0.1375,
\qquad
x=0.7779445026067248271\ldots,
\qquad
T=2\delta=0.275.
\]

The corrected first-relay resonance is

\[
\mathcal E_{2,u}(x)+\mathcal E_{1,u}(x+\delta)
=\mathcal E_{1,u}(x-\delta).
\tag{PS1}
\]

The input lattice basis is `(P,C)` with

\[
\beta(P)=2,
\qquad
\beta(C)=1,
\]

and the kinematic reset relabels

\[
P' = 3P-4C,
\qquad
C' = P-C.
\tag{PS2}
\]

## 2. Exact reset shear

For a general lattice character

\[
K=aP+bC
\]

write

\[
\beta(K)=2a+b.
\]

Applying (PS2),

\[
R(K)
=a(3P-4C)+b(P-C)
=(3a+b)P+(-4a-b)C.
\]

Define

\[
\boxed{M:=P-2C.}
\tag{PS3}
\]

Then

\[
K+\beta(K)M
=(a+2a+b)P+(b-4a-2b)C
=(3a+b)P+(-4a-b)C.
\]

Therefore

\[
\boxed{
R(K)=K+\beta(K)M.
}
\tag{PS4}

This is the exact algebraic form of the beta-(2,1) Poincare relabeling.

Since

\[
\beta(M)=0,
\]

we obtain the invariant direction

\[
\boxed{R(M)=M.}
\tag{PS5}

Thus the reset matrix is a unipotent shear, not a generic hyperbolic map. In the ordered basis `(M,C)` it has one unit Jordan direction.

## 3. Root orbit under reset

Let

\[
D:=P-C
\]

and define the beta-one root orbit

\[
\boxed{
X_k:=D+kM
=(k+1)P-(2k+1)C,
\qquad k\ge0.
}
\tag{PS6}

Every `X_k` has beta one. By (PS4),

\[
\boxed{R(X_k)=X_{k+1}.}
\tag{PS7}

In particular

\[
D\to H\to R_3\to X_3\to\cdots,
\]

where

\[
H=2D-C=D+M,
\qquad
R_3=3D-2C=D+2M.
\]

So the familiar entrance root chain is exactly the Jordan orbit of the reset shear.

At the reset face the natural old-`D,C` leaf actions are

\[
A_D(T)=\mathcal E_{1,u}(x+\delta)
=-0.0085566130822\ldots,
\tag{PS8}
\]

\[
A_C(T)=\mathcal E_{1,u}(x+3\delta)
=-0.0440625161971\ldots,
\tag{PS9}
\]

while the renewed parent target is

\[
A_P^*=\mathcal E_{2,u}(x)
=-0.1463388020904\ldots.
\tag{PS10}
\]

The root-orbit leaf action is

\[
A_{X_k}^{leaf}(T)
=(k+1)A_D(T)+kA_C(T).
\tag{PS11}
\]

Numerically,

\[
\begin{array}{c|c|c}
k&A_{X_k}^{leaf}(T)&A_{X_k}^{leaf}(T)-A_P^*\\ \hline
0&-0.00855661&+0.13778219\\
1&-0.06117574&+0.08516306\\
2&-0.11379487&+0.03254393\\
3&-0.16641400&-0.02007520
\end{array}
\tag{PS12}

Thus `D,H,R3` remain above the parent target layer, whereas `X3` lies below it by a fixed action gap. This explains why a four-state entrance audit is the natural finite truncation of the reset Jordan chain.

## 4. Parent orbit is already supercritical without active removal

Applying `R` repeatedly to the beta-two parent gives

\[
\boxed{
R^n(P)=P+2nM
=(2n+1)D-(2n-1)C.
}
\tag{PS13}

For `n=1`, this is the renewed-parent character

\[
P_{new}=3D-C.
\]

Its old-leaf reset action is

\[
3A_D(T)+A_C(T)
=-0.0697323554437\ldots.
\tag{PS14}
\]

Hence

\[
\boxed{
3A_D(T)+A_C(T)-A_P^*
=+0.0766064466467\ldots>0.
}
\tag{PS15}

So the first parent shear image is exponentially stronger than the desired renewed parent if it survives as an ordinary old-lattice leaf genealogy. The next image drops below target, but the first one already has to be eliminated or structurally suppressed.

This is a physical-state reformulation of the genealogy obstruction: the dangerous mode is not an arbitrary auxiliary trace; it is the first nontrivial beta-two Jordan image of the reset map.

## 5. Candidate autonomous repair: retain beta-zero memory `M`

The temporal-control obstruction suggests replacing future profile knobs by genuine Cauchy amplitudes. The most canonical available direction is precisely the reset invariant

\[
M=P-2C.
\]

It is beta zero and therefore survives the relabeling as the same character.

For the corrected geometry, `M=D-C` has constant radial-normal difference. Its frozen beta-zero action rate is

\[
\boxed{
\lambda_M
=-\frac{(2u\delta)^2}{(1+u^2)^{3/2}}
=-0.02421243094765\ldots.
}
\tag{PS16}
\]

Thus a homogeneous Cauchy preload with input action `A_M(0)` has

\[
A_M(s)=A_M(0)+\lambda_M s.
\tag{PS17}
\]

A natural idea is to use the difference interaction

\[
D-M\to C
\tag{PS18}
\]

to cancel the old catalyst autonomously.

The principal coefficient is nonzero. On the late interval `[t_*,T]`, the diagnostic audit gives

\[
\boxed{
|\kappa_{D-M\to C}|>2.79.
}
\tag{PS19}

Thus polarization is not the obstruction.

## 6. Action threshold for catalyst cancellation

For (PS18) to compete with the old natural catalyst at leading exponential order at time `s`, one needs

\[
A_D(s)+A_M(s)\ge A_C(s).
\tag{PS20}
\]

Equivalently,

\[
\boxed{
A_M(s)\ge A_C(s)-A_D(s).
}
\tag{PS21}

At the old strong-`H` center

\[
t_*=0.225129116982868\ldots,
\]

the required input action would be

\[
A_M(0)
=A_C(t_*)-A_D(t_*)-\lambda_Mt_*
=+0.00313195989927\ldots>0.
\tag{PS22}
\]

which is above the natural `O(1)` action ceiling `0`. Hence a natural beta-zero preload cannot cancel the catalyst at that exact collar.

For the maximal natural choice `A_M(0)=0`, equality first occurs later, at

\[
\boxed{
s_M=0.230030678322563\ldots.
}
\tag{PS23}

This makes the beta-zero memory route superficially plausible: one could delay catalyst cleanup by about `4.90e-3` in normalized time.

## 7. Fatal consequence: the same `M` creates a supercritical parent

The difficulty is that a beta-zero memory strong enough to satisfy (PS21) cannot be removed by the ordinary `D-C\to M` source at the same leading action. Indeed that quadratic source has action

\[
A_D(s)+A_C(s),
\]

whereas from (PS21)

\[
A_M(s)-[A_D(s)+A_C(s)]
\ge -2A_D(s)>0
\tag{PS24}
\]

throughout the late interval because `A_D(s)<0` before the reset face. Thus the preloaded `M` is exponentially stronger than any opposing `M` generated from the ordinary `D,C` pair. It survives to reset at leading order.

But the selected physical quadratic coefficients satisfy, on `[t_*,T]`,

\[
\boxed{
|\kappa_{M+D\to H}|>8.50,
}
\tag{PS25}
\]

\[
\boxed{
|\kappa_{H+D\to P_{new}}|>0.1919.
}
\tag{PS26}

Hence the unavoidable genealogy

\[
M+D\to H,
\qquad
H+D\to P_{new}
\tag{PS27}
\]

is present with fixed nonzero polarization margins.

From (PS21), propagate the beta-zero action to `T`:

\[
A_M(T)
\ge
A_C(s)-A_D(s)+\lambda_M(T-s).
\tag{PS28}
\]

Therefore the resulting beta-two parent has reset action at least

\[
A_{P_{new}}^{(M)}(T)
\ge
A_C(s)-A_D(s)+\lambda_M(T-s)+2A_D(T).
\tag{PS29}
\]

Subtract the desired target `A_P^*` and define

\[
G(s)
:=A_C(s)-A_D(s)+\lambda_M(T-s)+2A_D(T)-A_P^*.
\tag{PS30}
\]

Using

\[
A_C'(s)=\Gamma_1(x+\delta+s),
\qquad
A_D'(s)=\Gamma_1(x-\delta+s),
\]

we have

\[
G'(s)
=\Gamma_1(x+\delta+s)
-\Gamma_1(x-\delta+s)
-\lambda_M.
\tag{PS31}
\]

For `z>0`,

\[
\Gamma_1'(z)
=-\frac{u^2z}{(1+u^2z^2)^{3/2}}
-\frac{2u^2z}{(1+u^2)^{3/2}}<0.
\tag{PS32}
\]

A crude uniform bound from only the second negative term gives

\[
G'(s)
\le
-\frac{2u^2(x-\delta)}{(1+u^2)^{3/2}}(2\delta)
-\lambda_M
<-0.0885
\tag{PS33}
\]

on `[0,T]`. Thus `G` is strictly decreasing and its minimum occurs at `T`.

At `s=T`,

\[
G(T)
=A_C(T)+A_D(T)-A_P^*.
\]

Numerically,

\[
\boxed{
G(T)=+0.0937196728111\ldots>0.
}
\tag{PS34}

Consequently

\[
\boxed{
A_{P_{new}}^{(M)}(T)-A_P^*
\ge0.0937196728\ldots
}
\tag{PS35}

for **every** late time at which the beta-zero memory is strong enough to cancel the catalyst at leading action.

This is exponentially fatal: the unwanted parent wins by

\[
\exp\{0.0937\,\Lambda_\ell\}
\]

up to only polynomial/source-small prefactors.

## 8. A same-character homogeneous preload cannot cancel the fatal parent

One might try to preload the same beta-two character `P_new=3P-4C` with opposite phase so that it cancels the unavoidable contribution (PS27) at `T`.

At the entrance this character has reduced slope

\[
z_{P_{new}}(0)=x-2\delta.
\]

Its natural beta-two envelope action there is

\[
\mathcal E_{2,u}(x-2\delta)
=-0.00530142026777\ldots.
\tag{PS36}

A homogeneous packet on that character gains the deterministic action increment

\[
\mathcal E_{2,u}(x)-\mathcal E_{2,u}(x-2\delta)
=-0.141037381823\ldots
\tag{PS37}

by the reset face.

Even the **minimal** fatal parent action from (PS34) is

\[
A_C(T)+A_D(T)
=-0.0526191292793\ldots.
\tag{PS38}

Therefore a preloaded opposite-phase beta-two packet would need entrance action

\[
\begin{aligned}
A_{pre}^{req}
&=[A_C(T)+A_D(T)]
-[\mathcal E_{2,u}(x)-\mathcal E_{2,u}(x-2\delta)]\\
&=+0.0884182525433\ldots.
\end{aligned}
\tag{PS39}

Hence

\[
\boxed{A_{pre}^{req}>0.}
\tag{PS40}

But the source envelope is normalized to have maximal natural action `0` at its turning point. An `O(1)` homogeneous source packet cannot carry positive action.

Thus same-character homogeneous preloading cannot cancel even the weakest beta-zero-memory-generated fatal parent.

## 9. Poincare consequence

The physical Fourier-state route has nevertheless revealed the correct semantic state structure:

- `M=P-2C` is the unique invariant direction of the reset shear;
- `D,H,R3,...` form its beta-one Jordan orbit;
- `P,P_new,...` form the beta-two shear orbit.

However the simplest invariant-state attempt

\[
(P,C,M)_{in}
\longmapsto
(P',C',M')_{out}
\]

cannot realize catalyst cleanup while staying in the admissible natural-action regime. If `M` is too weak, it cannot remove `C`; if it is strong enough, it forces an exponentially supercritical `P_new` via (PS27), and that excess cannot be cancelled by a natural same-character preload.

Therefore

\[
\boxed{
\text{beta-zero memory alone does not repair the active-control Cauchy gap.}
}
\tag{PS41}

## 10. New frontier

A successful autonomous physical-state mechanism must now evade the implication

\[
\text{leading catalyst cancellation}
\Longrightarrow
M+D\to H\to P_{new}
\text{ with positive reset-action excess}.
\]

The remaining plausible routes are narrower:

1. a genuinely different physical character/generator whose cancellation edge does not share the `M+D\to H\to P_new` shortcut;
2. a coupled finite state in which the dangerous parent is cancelled by another **source-admissible leading genealogy** rather than by a homogeneous preload;
3. a different reset geometry where the analogue of (PS34) changes sign while the mandatory resonance and source-cone conditions survive;
4. a structural polarization zero on the fatal return path in a different geometry.

The next research step should therefore search over **alternative catalyst-cancellation characters / reset geometries**, not add more temporal profiles to the present gate.

No autonomous unforced reset cell or Navier--Stokes blowup theorem is claimed here.

Reproducibility script: `experiments/beta21_reset_shear_beta_zero_memory_audit.py`.
