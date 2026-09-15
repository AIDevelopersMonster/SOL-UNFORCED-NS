# Source-matched realization of the seven beta-zero mean-root controls

**Status:** PROVED PRINCIPAL/SOURCE-CLASS REALIZATION THEOREM. The seven direct root-source profiles required by `beta21_second_gate_mean_root_seven_control_vandermonde.md` can be generated internally, without external forcing, by seven small homogeneous growing subpackets in the already present `C_new=P-D` character.

The key action fact is that `C_new` is generated **below** its own natural unit-beta envelope. Therefore a source-native homogeneous `C_new` packet may be multiplied by an exponentially small coefficient to match the generated `C_new` action. Its difference interaction with the surviving `D` then generates the beta-zero root `M` at exactly the promoted root action. No exponentially large control amplitude is required.

## 1. Generated `C_new` scale

At the second-collision working section,

\[
A_P=-0.10519727146343909\ldots,
\qquad
A_D=-0.02407863050407955\ldots.
\tag{SRM1}
\]

The unavoidable first difference child

\[
C_{new}=P-D
\]

is generated at action

\[
\boxed{
A_C^{gen}=A_P+A_D
=-0.12927590196751864\ldots.
}
\tag{SRM2}
\]

Its reduced slope is

\[
z_C=1.218506242359214\ldots,
\]

and its natural unit-beta envelope is

\[
\boxed{
\mathcal E_{1,4}(z_C)
=-0.06603621737409447\ldots.
}
\tag{SRM3}
\]

Hence

\[
\boxed{
\delta_C
:=
\mathcal E_{1,4}(z_C)-A_C^{gen}
=0.06323968459342416\ldots>0.
}
\tag{SRM4}
\]

The generated `C_new` packet is therefore smaller than a natural homogeneous growing `C_new` pulse by the action factor

\[
e^{-\delta_C\Lambda_\ell}.
\tag{SRM5}
\]

## 2. Seven source-native homogeneous subpackets

Use the source homogeneous-pulse theorem in the same `C_new` character and growing polarization. Choose seven fixed smooth source-native translated labels/subpackets

\[
\widehat C_j,
\qquad j=1,\ldots,7,
\tag{SRM6}
\]

with distinct centers inside one bounded source collar around the second collision. Each is an exactly admissible homogeneous growing packet before curl reconstruction, with the standard source envelope and fixed packet seminorm bounds.

Define normalized controls

\[
\boxed{
C_{ctrl}(p)
=\eta_\ell\sum_{j=1}^7p_j\widehat C_j,
\qquad p\in\mathbb C^7,
}
\tag{SRM7}
\]

where at the reference section

\[
\boxed{
\eta_\ell
:=e^{-\delta_C\Lambda_\ell}
\le1.
}
\tag{SRM8}
\]

For translated centers one may equivalently use the centerwise exact envelope normalization `eta_{ell,j}`. On a bounded source-`v` collar the reduced slope drift is `O(S_*^{-1})`, so the ratios of these centerwise normalizations differ only by fixed `e^{O(1)}` factors and all source seminorm estimates remain uniform.

Because `eta_ell<=1`, multiplication by this level-dependent factor only improves every source coefficient upper bound. Parameter derivatives satisfy

\[
\boxed{
\|D_p C_{ctrl}\|_{pkt}
\le C\eta_\ell
\le C.
}
\tag{SRM9}
\]

No inverse small factor is introduced.

## 3. No new lattice generator

Every control subpacket has

\[
\operatorname{char}(\widehat C_j)=\operatorname{char}(C_{new})=P-D.
\tag{SRM10}
\]

Thus

\[
\boxed{
\operatorname{rank}_{\mathbb Z}
\langle P,D,\widehat C_1,\ldots,\widehat C_7\rangle
=
\operatorname{rank}_{\mathbb Z}\langle P,D\rangle.
}
\tag{SRM11}
\]

The control bank adds amplitudes/support labels, not new frequencies.

## 4. Same-character control self-interaction

All `C_j` use the same phase and principal growing polarization. At principal WKB order their mutual self-interaction is proportional to

\[
(a_C\cdot k_C)a_C=0
\]

by incompressibility. Therefore

\[
\boxed{
\Pi_{2C}^{principal}
\left[
\mathcal B(C_i,C_j)+\mathcal B(C_j,C_i)
\right]=0.
}
\tag{SRM12}
\]

Localized coefficient derivatives and curl/frame corrections belong to the already-audited lower source classes and carry positive source gains.

## 5. Direct beta-zero root source

Interact one control pulse with the fixed surviving `D` packet. The difference character is

\[
D-C_{new}=2D-P=M.
\tag{SRM13}
\]

The principal beta-zero projection was proved nonzero in `beta21_second_gate_mean_root_factorization.md` and explicitly audited in `beta21_second_gate_mean_root_polarization_audit.md`.

Thus each normalized control produces

\[
\boxed{
q_{M,j}(v)
=\kappa_M(v)D(v)\,\eta_{\ell,j}\chi_j(v)p_j
+\operatorname{l.o.t.},
}
\tag{SRM14}
\]

with

\[
|\kappa_M(v)D(v)|\ge\kappa_*>0
\]

after fixed phase/action normalization on a sufficiently short collar.

The control action is

\[
A_C^{ctrl}=A_C^{gen},
\]

so the generated root source has action

\[
\boxed{
A_C^{ctrl}+A_D
=A_P+2A_D
=A_M.
}
\tag{SRM15}
\]

This is exactly the minimal promoted action of the beta-zero root derived in the mean-root factorization theorem.

Hence the controls are **action matched** to the dangerous genealogy.

## 6. Unavoidable sum sideband is subleading

The same control packet and `D` also have the sum character

\[
C_{new}+D=P.
\tag{SRM16}
\]

Its control-generated action is again

\[
A_P^{side}=A_C^{ctrl}+A_D=A_M.
\tag{SRM17}
\]

Compare this with the transported designated parent action `A_P`:

\[
\boxed{
A_P^{side}-A_P
=2A_D
=-0.0481572610081591\ldots<0.
}
\tag{SRM18}
\]

Therefore

\[
\frac{P_{side}}{P_{des}}
\lesssim
S_*^C
\exp[-0.0481572\ldots\Lambda_\ell]
\to0.
\tag{SRM19}
\]

Any subsequent contribution `P_side+D -> E` inherits the same fixed action deficit relative to the intended designated `E=P+D` output.

Thus the unavoidable sum branch does not compete at leading action with the second-gate designated channel.

## 7. No new critical character outside the audited lattice set

A control `C_new` character is already the lattice combination `P-D`, and its assigned action is exactly the action of the generated first difference child. Any genealogy containing a control leaf therefore corresponds to an existing `(P,D)` genealogy with the same or more negative leaf action.

Consequently the control bank cannot increase the maximal leaf-action bound used in the complete second-gate critical audit. It creates no new supercritical character outside the already identified finite critical block.

## 8. Smooth translated root-source rank

After dividing each `q_{M,j}` by its fixed nonzero weight and action normalization, the seven profiles are fixed smooth translates up to a small coefficient perturbation on the bounded source collar.

At frozen coefficients, `beta21_second_gate_mean_root_seven_control_vandermonde.md` gives

\[
\det J_7\ne0.
\]

The Volterra response depends continuously on the smooth weight `kappa_M D` and the slowly varying frame coefficients. Hence, after fixing a sufficiently short positive collar,

\[
\boxed{
|\det J_{7,var}|\ge d_7/2>0.
}
\tag{SRM20}
\]

for all sufficiently high dyadic levels.

## 9. Curl realization and exact divergence freedom

Apply the source curl-potential construction to every homogeneous `C_new` control packet. This preserves the principal coefficient and action envelope while placing the reconstruction remainder in a lower source class with a positive epsilon gain.

Therefore the seven root controls may be included in the approximate designated field as exactly divergence-free physical packets. They are internal initial/design degrees of freedom, not external Navier--Stokes forcing.

## 10. Consequence

The source-realization problem for the root-control bank is closed at principal/source-class level:

\[
\boxed{
7\ \text{small same-character }C_{new}\text{ pulses}
\Longrightarrow
7\ \text{action-matched direct }M\text{ source controls}
\Longrightarrow
\det J_{7,var}\ne0.
}
\tag{SRM21}

Together with one main second-collision amplitude parameter for the desired `E` output, this gives the correct eight-dimensional finite control architecture.

The remaining obligation is the exact parameter-dependent zero-residual transfer in **action-normalized coordinates**, verifying that the exact correction derivative is `o(1)` relative to each promoted root-family output scale. Only after that theorem may the routed second active gate be declared closed.
