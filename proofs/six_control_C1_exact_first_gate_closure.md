# Six-control `C^1` transfer and exact first active-gate closure

**Status:** PROVED EXACT LOCAL ZERO-RESIDUAL SIX-CONTROL GATE THEOREM, CONDITIONAL ONLY ON THE RECORDED FINITE NUMERICAL ENVELOPE CERTIFICATES. The four-parameter theorem in `four_control_C1_zero_residual_dependence.md` extends to the sufficient six-coordinate first-gate block

\[
(P,E,Q,H,P_{new},R_3).
\]

For six internally generated catalyst-subpacket controls, the exact phase-adapted local zero-residual solution depends `C^1` on the six complex amplitudes, the exact exit Jacobian is the six-state smooth-profile principal matrix plus `o(1)`, and the nonzero principal Vandermonde determinant persists. Hence, at every sufficiently high dyadic level, there is a nearby six-control vector for which

\[
(P,E,Q,H,P_{new},R_3)_{out}
=(P_*,0,0,0,0,0),
\qquad P_*\ne0.
\]

Together with the full first-gate critical audit and the positive-width action certificate, this closes the **first genealogy-breaking active collar** at the working-research level.

The only publication-hardening caveat is numerical certification: `beta21_first_gate_full_critical_audit.md` and `beta21_first_gate_width_margin.md` presently use high-precision exact-envelope evaluation rather than interval arithmetic. No additional PDE inverse or control-rank theorem is missing.

## 1. Six internal catalyst controls

Work at the source-safe finite-`u_*` point

\[
u_*=4.
\tag{S6C1}
\]

Let the intended first gate be

\[
C+D\longrightarrow P.
\tag{S6C2}
\]

Choose six fixed smooth profiles

\[
\chi_j\in C_c^\infty(I_*),
\qquad j=1,\ldots,6,
\tag{S6C3}
\]

with pairwise distinct centers and supports inside one sufficiently short forward collision collar `I_*`. Define

\[
\boxed{
C(p)=C_{base}+\sum_{j=1}^{6}p_jC_j,
\qquad p=(p_1,\ldots,p_6)\in\mathbb C^6,
}
\tag{S6C4}
\]

where every `C_j` has the same phase and principal polarization as the incoming catalyst `C`, with coefficient profile `chi_j`.

The proof of `catalyst_subpacket_direct_P_realization.md` uses only finiteness of the family, not the number four. Therefore it applies verbatim to six controls:

1. every `C_j` carries the original catalyst character;
2. no new lattice generator is introduced;
3. `C_j+D` has the designated `P=C+D` phase;
4. the principal `P` projection is separated from zero on a sufficiently short collar;
5. same-phase catalyst-control self-interactions vanish at principal WKB order by incompressibility;
6. each control is realized by the source curl construction as an exactly divergence-free packet, with lower-order curl remainder.

Thus the six parameters are internal approximate-field degrees of freedom, not external forcing.

## 2. One fixed positive gate width

The exact-envelope audit proves that every uncontrolled center-critical character stays action-subcritical on

\[
0\le t\le10^{-3}
\tag{S6C5}
\]

with conservative margin

\[
\gamma_{gate}=7\times10^{-3}.
\tag{S6C6}
\]

The six-state source response matrix depends continuously on the slowly varying principal coefficients and on the nonvanishing weight multiplying each catalyst profile. By `six_control_smooth_gate_vandermonde.md`, its frozen determinant is nonzero. Hence there exists

\[
w_{rank}>0
\tag{S6C7}
\]

such that the principal six-control rank persists on every sufficiently short collar of width at most `w_rank` around the reference gate section.

Set

\[
\boxed{
w_*:=\min(10^{-3},w_{rank})>0.
}
\tag{S6C8}
\]

This separates the two logically distinct small-width requirements:

- `10^{-3}` is an explicit action-gap width certificate;
- `w_rank` is the open-rank/source-coefficient width supplied by continuity.

Both are fixed after the finite-`u` gate geometry is frozen and are independent of the dyadic level `ell`.

Because the interval has positive length, choose six distinct centers inside it. For example, after rescaling the collar to `[0,w_*]`, one may take six equally spaced centers in the middle three quarters and choose each fixed profile support narrower than one quarter of the center spacing. All profile derivative constants are then finite design constants independent of `ell`.

## 3. Six-control parameter set

Let `p^0` be the frozen principal control vector from the six-state solve and choose a fixed compact neighborhood

\[
K_p=\{p\in\mathbb C^6:|p-p^0|\le r_p\}
\tag{S6C9}
\]

small enough that

1. the designated incoming amplitudes remain bounded;
2. the incoming `D` coefficient remains separated from zero;
3. the source cone remains strict;
4. the six control profiles remain inside `I_*`;
5. the slowly varying six-state principal determinant stays separated from zero;
6. all uncontrolled center-critical modes remain assigned to the action-subcritical remainder.

Since only finitely many normalized designated coefficients vary, all source packet seminorms are uniform on `K_p`.

Each catalyst coefficient is affine in `p`:

\[
a_C(v;p)
=a_C^{base}(v)+\sum_{j=1}^{6}p_j\chi_j(v)a_C^{ref}(v),
\tag{S6C10}
\]

so

\[
\partial_{p_j}a_C=\chi_j a_C^{ref},
\qquad
D_p^2a_C=0.
\tag{S6C11}
\]

Consequently

\[
\boxed{
\sup_{p\in K_p}
\bigl(
\|a_C(p)\|_{pkt}+\|D_pa_C(p)\|_{pkt}
\bigr)
\le C_{K_p}.
}
\tag{S6C12}
\]

The change from four to six parameters changes only this finite design constant.

## 4. Parameter differentiation does not change source exponents

The source packet calculus is closed under finite sums and finite products. Differentiating in one of the six control amplitudes replaces one bounded catalyst coefficient by one bounded fixed control coefficient. It does not differentiate the high carrier phase and does not create a negative power of `epsilon`.

Hence the controlled nonzero residual satisfies, uniformly on `K_p`,

\[
\boxed{
\|f_p\|_{\mathfrak A_{\sigma,0}}
+\|D_pf_p\|_{\mathfrak A_{\sigma,0}}
\le
CS_*^A
\left(
\varepsilon^{1/5}+e^{-cS_*}
\right).
}
\tag{S6C13}
\]

The mean forcing obeys

\[
\boxed{
\|F_{mean,p}\|
+\|D_pF_{mean,p}\|
\le
CS_*^A\varepsilon^{1-\kappa_s}.
}
\tag{S6C14}
\]

All source-frame errors, curl remainders and localization derivatives retain the positive gains already used in the four-control theorem.

## 5. `C^1` nonzero solve in six parameters

For fixed mean input `m`, write the exact nonzero equation as

\[
\partial_vz
=\mathcal L_{p,m}(v)z
+f_{p,m}
+\mathcal B(z,z),
\tag{S6C15}
\]

with

\[
\mathcal L_{p,m}=\mathcal D+\mathcal K_{p,m}.
\]

On the fixed six-parameter compact set,

\[
\boxed{
\|\mathcal K_{p,m}z\|_{\mathfrak A_{\sigma,0}}
+
\|D_p\mathcal K_{p,m}z\|_{\mathfrak A_{\sigma,0}}
\le C\|z\|_{\mathfrak A_{\sigma,1}}.
}
\tag{S6C16}
\]

The full-linearized Volterra propagator therefore satisfies

\[
\boxed{
\|V_{p,m}(v,w)\|
+
\|D_pV_{p,m}(v,w)\|
\le C_{K_p,I_*}
}
\tag{S6C17}
\]

in the same graph norms as the local theorem.

The nonzero Duhamel map remains a contraction on a ball of radius

\[
\rho_\ell
\le
CS_*^A
\left(
\varepsilon^{1/5}+e^{-cS_*}
\right)
\to0.
\tag{S6C18}
\]

For sufficiently large `ell`, its derivative in the unknown has norm at most `1/2`. The parameter-dependent contraction theorem gives a unique

\[
z=z(p,m)
\tag{S6C19}
\]

which is `C^1` in all six complex parameters. Differentiating the fixed-point equation yields

\[
\boxed{
\|D_pz(p,m)\|_X
\le
CS_*^{A'}
\left(
\varepsilon^{1/5}+e^{-cS_*}
\right)
=o(1).
}
\tag{S6C20}
\]

Again, the number six appears only in the harmless finite constant.

## 6. `C^1` angular-mean solve

Insert `z(p,m)` into the exact phase-adapted whole-space mean map. The controlled mean contraction factor is the same one used in the local zero-residual theorem:

\[
q_\ell
\le
CS_*^A
\left[
\varepsilon^{9/50-2\kappa_s}
+\varepsilon^{1/2-\kappa_s}
+\varepsilon^{1-2\kappa_s}
+\rho_\ell+r_\ell
\right]
\to0.
\tag{S6C21}
\]

Uniformity on `K_p` follows from (S6C12)--(S6C14). For high enough level, `q_ell<=1/2`. The parameter-dependent contraction theorem gives a unique mean fixed point

\[
m=m(p)
\tag{S6C22}
\]

with

\[
\boxed{
\|D_pm(p)\|_{\mathfrak M_{\sigma,m_0}}
=o(1).
}
\tag{S6C23}
\]

The chain rule then gives

\[
\boxed{
\|D_pz(p,m(p))\|_X=o(1).
}
\tag{S6C24}
\]

Thus the exact stable nonzero complement and the exact angular mean change only `o(1)` under an `O(1)` variation of the six normalized finite controls.

## 7. Exact unforced local solution family

For every `p\in K_p`, set

\[
U_\ell(p)
=U_{des,\ell}(p)+z_\ell(p)+m_\ell(p).
\tag{S6C25}
\]

The nonzero fixed point kills all nonzero-harmonic residuals and the mean fixed point kills the angular mean. Exact phase-adapted reconstruction therefore gives

\[
\boxed{
\mathcal N_{phys}(\mathcal R_\ell U_\ell(p))=0
}
\tag{S6C26}
\]

on the positive-width first-gate collar `I_*`.

No external forcing is introduced. The six parameters only choose the internal catalyst subpacket amplitudes of the approximate designated field; the correction solve restores the exact unforced equation.

## 8. Six-coordinate exact exit map

Define

\[
\boxed{
\mathcal G_\ell(p)
=
(P,E,Q,H,P_{new},R_3)_{out}
\in\mathbb C^6.
}
\tag{S6C27}
\]

Split

\[
\mathcal G_\ell
=\mathcal G_{des,\ell}+\mathcal G_{corr,\ell}.
\tag{S6C28}
\]

The six-state smooth-profile calculation and source normalization give

\[
D_p\mathcal G_{des,\ell}
=J_{6,principal}
+O(S_*^{-1})
+O(S_*^A\varepsilon^{1/2-\kappa_s}),
\tag{S6C29}
\]

where, at the frozen reference coefficients,

\[
\boxed{
\det J_{6,principal}
=
\frac{a^5b^4g^3h^2r}{2!3!4!5!}
\mu_0^6
\prod_{i<j}(L_j-L_i)
\ne0.
}
\tag{S6C30}
\]

For the actual slowly varying six profiles on `I_*`, the matrix is a fixed small perturbation of this reference matrix and remains invertible by the definition of `w_rank`.

The exit functionals are bounded linear traces in the finite packet coordinates. Therefore (S6C23)--(S6C24) imply

\[
\boxed{
\|D_p\mathcal G_{corr,\ell}\|=o(1).
}
\tag{S6C31}
\]

Combining (S6C29)--(S6C31),

\[
\boxed{
D_p\mathcal G_\ell
=J_{6,var}+o(1),
}
\tag{S6C32}
\]

where the fixed positive-width principal matrix `J_{6,var}` is invertible.

## 9. Persistence of the six-control determinant

Let

\[
d_6:=|\det J_{6,var}|>0.
\tag{S6C33}
\]

Since the convergence in (S6C32) is uniform on a sufficiently small fixed neighborhood of `p^0`, determinant continuity gives, for all sufficiently high dyadic levels,

\[
\boxed{
|\det D_p\mathcal G_\ell(p)|
\ge\frac12d_6>0.
}
\tag{S6C34}
\]

Thus the exact six-control exit map is locally invertible as a real `12 x 12` map, with the conjugate-real realization of the complex controls understood.

## 10. Exact first active gate

The frozen principal triangular solve supplies `p^0` such that

\[
\mathcal G_0(p^0)
=(P_*,0,0,0,0,0),
\qquad P_*\ne0.
\tag{S6C35}
\]

The exact map differs from the fixed positive-width principal map by `o(1)` in `C^1`. Hence the quantitative inverse/implicit-function theorem gives a unique nearby vector

\[
\boxed{
p_\ell=p^0+o(1)
}
\tag{S6C36}
\]

such that

\[
\boxed{
\mathcal G_\ell(p_\ell)
=(P_*,0,0,0,0,0).
}
\tag{S6C37}
\]

The full critical audit shows that the only non-designated center characters with positive action defect are `H` and `R_3`, both included in the controlled block. The finite-width audit shows that every uncontrolled center-critical mode satisfies

\[
\Delta(t)\le-\gamma_{gate}
\tag{S6C38}
\]

throughout the action-certified part of the collar. Modes outside the finite critical set are forward stable, with high modes quadratically damped.

Consequently the first active collision collar has the exact input-output property

\[
\boxed{
(C,D)_{in}
\longmapsto
P_{out}=P_*\ne0,
}
\tag{S6C39}
\]

with all five displayed shortcut traces zero and every remaining non-designated critical coordinate action-subcritical or forward-stable.

This is the desired genealogy-breaking gate for the first event.

## 11. Closure statement

At the working-research level the first beta-(2,1) active gate is now closed by the chain

\[
\boxed{
\begin{gathered}
\text{full finite critical enumeration}\\
+\ \text{positive-width action margin}\\
+\ \text{six internal catalyst controls}\\
+\ \text{smooth six-state Vandermonde rank}\\
+\ \text{exact local zero-residual solve}\\
+\ \text{uniform six-parameter }C^1\text{ transfer}\\
\Longrightarrow
\text{exact first active gate.}
\end{gathered}}
\tag{S6C40}
\]

No autonomous infinite cascade and no unforced Navier--Stokes blowup theorem is claimed.

## 12. Next frontier

The first gate may now be used as an input-output component of the ordered reset genealogy. The next event is

\[
\boxed{P+D\longrightarrow E.}
\tag{S6C41}
\]

The next research task is not to reprove the first gate. It is to perform for the second collar the same **local critical-descendant audit**:

1. identify which previously transported packets are physically present there;
2. enumerate every growing/neutral character reachable inside that overlap;
3. isolate supercritical shortcut descendants;
4. determine the minimal/sufficient internal control bank;
5. prove a positive-width rank/action theorem before concatenating the second gate.

The publication-hardening task for the first gate can proceed separately by replacing the high-precision numerical inequalities in the critical and width audits with interval-arithmetic certificates.
