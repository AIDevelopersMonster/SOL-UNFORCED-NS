# Gate 1B/C: singular finite-\(S\) central-profile problem

**Status:** EXACT PROBLEM REFORMULATION / THE OLD NEUMANN ARGUMENT IS INVALID AT THE DISPLAYED DERIVATIVE ORDERS.  THE FINITE-\(S\) CENTRAL PROFILE IS A SINGULARLY PERTURBED TRANSPORT/DIFFERENCE PROBLEM, NOT A ROUTINE BOUNDED PERTURBATION OF THE CONTINUUM FIRST-ORDER OPERATOR.

This note sharpens items A--C of

\[
\texttt{beta21_lowu_gate1_adversarial_reaudit.md}.
\]

It does not prove the exact discrete profile.  It identifies the correct theorem that must replace the current derivative-losing Neumann argument.

---

## 1. Why the second derivative is structural

Put

\[
h:=S^{-1/2}.
\]

On the tangent scale \(y=jh\), one orbit shift is

\[
R
=
\rho\,e^{h\partial_y}.
\]

Therefore, for a smooth profile,

\[
R
=
\rho
\left[
I+h\partial_y+\frac{h^2}{2}\partial_y^2
+\frac{h^3}{6}\partial_y^3+\cdots
\right].
\tag{SP1}
\]

The second derivative in (SP1) is not a source error.  It is part of the exact lattice shift itself.

Consequently any full expansion of the one-cell tangent Poincare map necessarily has the form

\[
\boxed{
\mathcal P_h-I
=
hL+h^2K_h,
}
\tag{SP2}
\]

where \(K_h\) contains a genuine second-order differential component.

The leading operator is

\[
\boxed{
L
=
v\partial_y+By+C.
}
\tag{SP3}
\]

---

## 2. Dividing by \(h\) exposes the singular perturbation

The exact fixed-profile equation is

\[
(\mathcal P_h-I)f=0.
\]

Using (SP2),

\[
\boxed{
Lf+hK_hf=0.
}
\tag{SP4}
\]

If \(K_h\) contains

\[
a_2(y)\partial_y^2,
\]

then (SP4) contains

\[
\boxed{
v f'
+(By+C)f
+h\,a_2(y)f''
+\cdots
=0.
}
\tag{SP5}
\]

Although the coefficient of \(f''\) is \(h\), the equation has changed order.

This is a singular perturbation.

---

## 3. Why the old Neumann argument fails

The old proof used

\[
G:L^{-1}:X^m\to X^{m+1}
\]

and a remainder

\[
K_h:X^{m+2}\to X^m.
\]

Thus

\[
GK_h:X^{m+2}\to X^{m+1}.
\]

It is not an operator on one fixed Banach space.

Writing

\[
(I+hGK_h)^{-1}
\]

as a Neumann series therefore has no meaning with only these mapping properties.

The small scalar \(h\) does not repair the lost derivative.

\[
\boxed{
\text{small coefficient}\ne\text{bounded perturbation when differential order increases.}
}
\tag{SP6}
\]

---

## 4. A model fast branch

Consider the constant-coefficient model

\[
v f'+h a f''=0,
\qquad
va\ne0.
\tag{SP7}
\]

Its characteristic equation is

\[
\lambda(v+ha\lambda)=0.
\]

Besides the slow mode \(\lambda=0\), there is a fast mode

\[
\boxed{
\lambda_{fast}
=
-\frac{v}{ha}.
}
\tag{SP8}
\]

Thus the perturbed equation contains a solution on the scale

\[
e^{-vy/(ha)}.
\]

As \(h\to0\), this mode is invisible in the first-order continuum equation.

For the actual Gaussian problem the coefficients vary, but the same warning remains: one must prove that the physical bilateral Gaussian space excludes all unwanted fast modes or fixes them uniquely through boundary/decay conditions.

This cannot be inferred from the continuum kernel dimension alone.

---

## 5. The Fredholm index may not be inherited automatically

The continuum operator

\[
L=v\partial_y+By+C
\]

has an explicit Gaussian-type kernel after imposing physical weighted admissibility.

But the exact finite-\(h\) problem is not simply

\[
L+\text{bounded compact perturbation}.
\]

Therefore the statements

\[
\dim\ker L=1
\]

and

\[
\operatorname{coker}L=0
\]

do not automatically imply the same index statement for the exact profile operator.

A publication-level theorem must prove directly that, for all sufficiently small \(h\),

1. the exact admissible kernel has the desired dimension;
2. no unwanted fast branch belongs to the bilateral physical Gaussian space;
3. after one normalization the profile is unique;
4. the solution converges to the continuum Gaussian profile.

---

## 6. Preferred repair: solve the exact difference equation, not its derivative expansion

The physical orbit is discrete.

The most conservative route is therefore to avoid treating (SP5) as the fundamental equation.

Let

\[
\mathcal P_{b,S}^{tan}
\]

be the exact finite-\(S\) tangent-normalized Poincare operator acting on the sequence

\[
f_j.
\]

The correct theorem should solve

\[
\boxed{
\mathcal P_{b,S}^{tan}f=f
}
\tag{SP9}
\]

directly in a weighted sequence space.

The continuum operator \(L_b\) should be used only to

- identify the slow profile;
- determine the correct normalization;
- construct an approximate solution;
- estimate the inverse / exponential dichotomy of the exact discrete recurrence.

This avoids manufacturing an artificial derivative-losing Neumann problem.

---

## 7. What an exact discrete theorem must establish

Choose a physical weighted sequence norm

\[
\|f\|_{\mathcal X_{b,S}}
\]

adapted to the exact action \(H_b(z_j)\).

A correct finite-\(S\) central theorem must prove:

### 7.1 Existence

There exists

\[
f_{b,S}\ne0
\]

such that

\[
\mathcal P_{b,S}^{tan}f_{b,S}=f_{b,S}.
\]

### 7.2 One normalization

For one explicit bounded functional \(\ell_{b,S}\),

\[
\ell_{b,S}(f_{b,S})=1.
\]

### 7.3 Uniqueness

The normalized admissible fixed profile is unique in a fixed neighborhood of the continuum profile.

### 7.4 No fast admissible branch

Every second independent local branch generated by the higher-order/discrete character violates at least one bilateral physical decay condition.

### 7.5 Quantitative convergence

For the interpolation \(y=j/\sqrt S\),

\[
\boxed{
\|f_{b,S}-\phi_b\|_{\mathcal X}
\le
CS^{-\alpha}
}
\tag{SP10}
\]

for some fixed \(\alpha>0\).

The old target \(\alpha=1/2\) is desirable but not required for the subsequent source-small perturbation architecture unless another estimate explicitly needs that rate.

### 7.6 Parameter regularity

The normalized exact profile must be \(C^1\) (and later \(C^2\) for Gate 2) in the genuine finite macroscopic parameter set with only controlled polynomial losses.

---

## 8. Two possible proof routes

### Route A: exact discrete Volterra / transfer recurrence

Use the exact shift structure to derive a finite-order recurrence or a Volterra representation for the profile coefficients.

Then establish an exponential dichotomy between

- one slow physical branch;
- all fast/nonphysical branches.

This is the preferred route if the exact one-cell map can be represented by a sufficiently local shift kernel.

### Route B: semiclassical tame inverse

Work on a scale of Gaussian Sobolev/graph spaces and prove a tame inverse for

\[
L+hK_h
\]

with estimates that recover derivative loss.

This is a Nash--Moser / singular-perturbation theorem, not an ordinary Banach Neumann theorem.

It is more general but substantially heavier.

---

## 9. Exact next data needed from the one-cell operator

Before choosing Route A or B, Gate 1 must record the exact normalized one-cell operator in a form that exposes:

1. its shift kernel \(R^k\);
2. the decay of the \(k\)-kernel coefficients;
3. finite-\(S\) dependence on slope \(z_j\);
4. source modal/frame terms;
5. reset relabelling;
6. parameter dependence.

For an exponential shift semigroup, factorial decay of the \(R^k\) coefficients strongly favors Route A.

The next concrete file should therefore be an **exact designated generator/Poincare definition**, not another continuum Taylor expansion.

---

## 10. Corrected status of the old discrete-profile theorem

Until (SP9)--(SP10) are proved directly or a valid tame inverse replaces the derivative-losing Neumann series,

\[
\boxed{
\texttt{beta21_lowu_exact_discrete_central_profile.md}
\text{ is conditional and must not be cited as a theorem.}
}
\tag{SP11}
\]

This is a substantive proof correction.

No Gate 1 closure follows from the continuum profile calculation alone.
