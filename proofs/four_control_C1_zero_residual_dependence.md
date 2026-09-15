# Uniform `C^1` dependence of the local zero-residual solve on four catalyst controls

**Status:** PROVED PARAMETER-DEPENDENCE THEOREM INSIDE THE AUDITED LOCAL SOURCE CLASSES. For the four catalyst-subpacket controls constructed in `catalyst_subpacket_direct_P_realization.md`, the exact local nonzero-harmonic and angular-mean zero-residual fixed point depends `C^1` on the complex control vector on a sufficiently small fixed neighborhood. The correction and its control derivative retain the same positive source small factors as the uncontrolled local theorem. Consequently the exact finite exit Jacobian is the designated/principal finite Jacobian plus `o(1)` as the dyadic level tends to infinity.

This theorem closes the parameter-regularity obligation isolated in the catalyst-realization note, for the displayed finite critical block and one frozen collision collar. It does not yet prove that `(P,E,Q,H)` is the **complete** gate-critical exit set; that enumeration remains the next audit before a full five-event active reset circuit can be claimed.

## 1. Four-control parameter set

Let

\[
p=(p_1,p_2,p_3,p_4)\in\mathbb C^4
\tag{PC1}
\]

be the catalyst-subpacket amplitudes. Fix a compact ball

\[
K_p=\{p:|p-p^0|\le r_p\}
\tag{PC2}
\]

small enough that

1. all designated incoming amplitudes remain bounded and the surviving `D` amplitude stays separated from zero;
2. the `u_*=4` source-cone margin remains strict;
3. all four catalyst subpacket profiles remain supported in the chosen collision collar;
4. the principal finite response determinant remains separated from zero by the margin obtained in `smooth_profile_active_gate_vandermonde.md` and `catalyst_subpacket_direct_P_realization.md`.

Because only finitely many normalized designated coefficients are varied, every source packet seminorm of the approximate designated field is bounded uniformly for `p in K_p`.

## 2. Parameter differentiation preserves source classes

Each controlled catalyst coefficient has the form

\[
a_C(v;p)
=a_C^{base}(v)+\sum_{j=1}^4p_j\chi_j(v)a_C^{ref}(v).
\tag{PC3}
\]

Hence

\[
\partial_{p_j}a_C(v;p)
=\chi_j(v)a_C^{ref}(v),
\tag{PC4}
\]

and higher derivatives in `p` vanish at the coefficient level. The profiles `chi_j` are fixed smooth compactly supported functions.

Therefore every finite slow/source derivative used in the packet norm obeys

\[
\boxed{
\sup_{p\in K_p}
\left(
\|a_C(p)\|_{pkt}
+\|D_pa_C(p)\|_{pkt}
\right)
\le C_{K_p}.
}
\tag{PC5}

The same statement passes through finite products by Leibniz' rule. Thus differentiating a stage-zero residual with respect to `p` changes constants but does not change its source epsilon exponent or its action factor.

In particular, if the uncontrolled supported nonzero residual satisfies

\[
\|f_p\|_{\mathfrak A_{\sigma,0}}
\le C S_*^A
\left(
\varepsilon^{1/5}+e^{-cS_*}
\right),
\tag{PC6}
\]

then the four-control family satisfies uniformly

\[
\boxed{
\|D_pf_p\|_{\mathfrak A_{\sigma,0}}
\le C S_*^{A'}
\left(
\varepsilon^{1/5}+e^{-cS_*}
\right).
}
\tag{PC7}

Likewise every inhomogeneous mean forcing term retains the source gain

\[
\boxed{
\|F_{mean,p}\|+
\|D_pF_{mean,p}\|
\le C S_*^A\varepsilon^{1-\kappa_s}.
}
\tag{PC8}

The curl remainders and phase/frame errors retain their previously audited gains because differentiation in `p` acts on amplitude coefficients, not on the high carrier phase.

## 3. `C^1` full nonzero propagator

For fixed mean input `m`, the controlled nonzero equation has the form

\[
\partial_v z
=\mathcal L_{p,m}(v)z
+f_{p,m}(v)
+\mathcal B(z,z),
\tag{PC9}
\]

where

\[
\mathcal L_{p,m}=\mathcal D+\mathcal K_{p,m}.
\]

On `K_p` and the small mean ball, the mixed operator and its parameter derivative satisfy

\[
\boxed{
\|\mathcal K_{p,m}z\|_{\mathfrak A_{\sigma,0}}
+\|D_p\mathcal K_{p,m}z\|_{\mathfrak A_{\sigma,0}}
\le C\|z\|_{\mathfrak A_{\sigma,1}}.
}
\tag{PC10}

The Volterra construction of `nonzero_harmonic_forward_reduction.md` therefore applies uniformly in `p`. Let

\[
V_{p,m}(v,w)
\]

be the full linear propagator. Differentiating its Volterra equation gives

\[
D_pV_{p,m}(v,w)
=
\int_w^v
V_{p,m}(v,s)
(D_p\mathcal K_{p,m})(s)
V_{p,m}(s,w)\,ds.
\tag{PC11}
\]

Using the bounded forward estimate and the integrable one-derivative smoothing kernel yields

\[
\boxed{
\|V_{p,m}(v,w)\|
+\|D_pV_{p,m}(v,w)\|
\le C_{K_p,I}
}
\tag{PC12}

in the graph norms used by the nonzero theorem, uniformly for `p in K_p`.

## 4. `C^1` nonzero fixed point and small derivative

Let the nonzero Duhamel map be

\[
\mathcal S_{p,m}(z)
=V_{p,m}(\cdot,v_-)z_{in,p}
+\int_{v_-}^{\cdot}
V_{p,m}(\cdot,s)
\left[f_{p,m}+\mathcal B(z,z)\right](s)ds.
\tag{PC13}

The source construction gives, uniformly on `K_p`, a contraction on a ball of radius

\[
\rho_\ell
\le C S_*^A
\left(
\varepsilon^{1/5}+e^{-cS_*}
\right)
\to0.
\tag{PC14}

Choose the level so that

\[
\|D_z\mathcal S_{p,m}\|\le\frac12
\tag{PC15}
\]

throughout the ball. The parameter-dependent contraction theorem gives a unique `C^1` fixed point

\[
z=z(p,m).
\tag{PC16}
\]

Differentiating

\[
z=\mathcal S_{p,m}(z)
\]

gives

\[
(I-D_z\mathcal S_{p,m})D_pz
=D_p\mathcal S_{p,m}.
\tag{PC17}
\]

By (PC15),

\[
\|(I-D_z\mathcal S)^{-1}\|\le2.
\tag{PC18}
\]

Using (PC7), (PC12) and the fact that every term containing the small fixed point `z` contributes another factor `rho_ell`, one obtains

\[
\boxed{
\|D_pz(p,m)\|_X
\le C S_*^{A'}
\left(
\varepsilon^{1/5}+e^{-cS_*}
\right)
=o(1).
}
\tag{PC19}

Thus the exact non-designated nonzero correction changes only `o(1)` under an `O(1)` normalized variation of the four controls.

## 5. Controlled mean map

Substitute the exact nonzero solution into the phase-adapted mean map:

\[
\mathcal T_{p,\ell}(m)
=\int
\mathcal V_{mean,p}
\left[
F_{mean,p}
+\mathcal F_{nl,p}(m,z(p,m))
\right].
\tag{PC20}

The same whole-space Leray--Oseen bound is uniform on `K_p`, since the four controls perturb only a finite set of compactly supported designated coefficients in a bounded source class. Its parameter derivative is bounded by the differentiated Duhamel identity exactly as in Section 3.

The mean contraction factor satisfies uniformly

\[
q_\ell
\le C S_*^A
\left[
\varepsilon^{9/50-2\kappa_s}
+\varepsilon^{1/2-\kappa_s}
+\varepsilon^{1-2\kappa_s}
+\rho_\ell
+r_\ell
\right]
\to0.
\tag{PC21}
\]

Choose the level so that `q_ell<=1/2`. The parameter-dependent contraction theorem gives a unique `C^1` mean fixed point

\[
m=m(p).
\tag{PC22}
\]

The inhomogeneous estimate (PC8), together with (PC19) and the positive Lipschitz gains, yields

\[
\boxed{
\|D_pm(p)\|_{\mathfrak M_{\sigma,m_0}}
\le C S_*^{A'}\varepsilon^{1-\kappa_s}
+o(1)
=o(1).
}
\tag{PC23}

Finally set

\[
z(p):=z(p,m(p)).
\]

The chain rule and (PC19),(PC23) give

\[
\boxed{
\|D_pz(p)\|_X=o(1).
}
\tag{PC24}

## 6. Exact physical residual for every parameter

For each `p in K_p`, the nonzero fixed point kills every nonzero coefficient harmonic and the mean fixed point kills the angular mean. Exact phase-adapted reconstruction therefore gives

\[
\boxed{
\mathcal N_{phys}
\left(
\mathcal R_\ell
[U_{des}(p)+z(p)+m(p)]
\right)=0
}
\tag{PC25}

on the frozen collision collar.

Thus the four controls parameterize a genuine local family of exact unforced solutions, not solutions of a PDE with four external source terms. The controls occur only in the finite approximate/designated packet data; all residual forcing is cancelled internally by the exact correction solve.

## 7. Exit map and its Jacobian

Let

\[
\mathcal G_\ell(p)
=
(P_{out},E_{out},Q_{out},H_{out})
\tag{PC26}
\]

be the four phase-normalized critical exit coordinates of the exact solution family.

Split

\[
\mathcal G_\ell(p)
=\mathcal G_{des,\ell}(p)
+\mathcal G_{corr,\ell}(p).
\tag{PC27}
\]

The designated source-normalization and smooth-profile calculations give

\[
D_p\mathcal G_{des,\ell}
=J_{principal}+O(S_*^{-1})
+O(S_*^A\varepsilon^{1/2-\kappa_s}),
\tag{PC28}
\]

where `J_principal` is the finite-width catalyst-control response matrix with the nonzero Vandermonde determinant from `smooth_profile_active_gate_vandermonde.md` / `catalyst_subpacket_direct_P_realization.md`.

The correction exit trace is bounded by the correction norms. Equations (PC23)--(PC24) give

\[
\boxed{
\|D_p\mathcal G_{corr,\ell}\|=o(1).
}
\tag{PC29}

Therefore

\[
\boxed{
D_p\mathcal G_\ell
=J_{principal}+o(1)
}
\tag{PC30}
\]

uniformly on a sufficiently small fixed neighborhood of the principal control solution.

This is the parameter estimate required in (CR28) and (AG21).

## 8. Persistence of rank

Let

\[
d_*:=|\det J_{principal}|>0.
\tag{PC31}
\]

Since determinant is continuous and (PC30) is uniform, for all sufficiently high levels

\[
\boxed{
|\det D_p\mathcal G_\ell|
\ge\frac12d_*>0.
}
\tag{PC32}

Hence the exact four-control map is locally biholomorphic as a real `8 x 8` map (equivalently complex-invertible at the phase-normalized principal level, with the exact real/conjugate realization understood).

## 9. Exact one-collar gate for the displayed critical block

Suppose the principal finite system has a control vector `p^0` satisfying

\[
\mathcal G_0(p^0)
=(P_*,0,0,0),
\qquad P_*\ne0.
\tag{PC33}

The exact exit map differs from the principal map by `o(1)` in `C^1`. The quantitative inverse/implicit-function theorem and (PC32) therefore give, for every sufficiently high dyadic level, a unique nearby vector

\[
\boxed{p_\ell=p^0+o(1)}
\tag{PC34}
\]

such that

\[
\boxed{
\mathcal G_\ell(p_\ell)
=(P_*,0,0,0).
}
\tag{PC35}

Thus, **for the displayed critical block `(P,E,Q,H)`**, the first genealogy-breaking collar is closed as an exact phase-adapted unforced local gate, conditional only on the block being complete.

## 10. Scope and next frontier

What is now closed:

\[
\boxed{
\text{internal four-control realization}
+\text{ finite-width rank}
+\text{ exact local zero residual}
+\text{ }C^1\text{ rank persistence}
}
\tag{PC36}

for the finite block `(P,E,Q,H)` on one frozen source-safe collar.

What remains before declaring the first gate fully complete is **finite critical-block enumeration**:

\[
\boxed{
\textbf{list every growing/neutral exit character produced in the controlled collar and prove that each is either in }\{P,E,Q,H\}\textbf{ or uniformly action-subcritical.}
}
\tag{PC37}

If no additional critical exit coordinate exists, (PC35) is the exact one-collar gate theorem. If additional modes exist, enlarge the control matrix by one complex row/control per independent critical coordinate and repeat the same finite-dimensional argument.

Only after this enumeration should the gate be concatenated through the five ordered reset events. No autonomous infinite relay or unforced Navier--Stokes blowup theorem is claimed here.
