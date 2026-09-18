"""Audit the corrected bidirectional real-root low-u principal reset.

The real designated root contains both +M and -M Fourier characters.
Therefore the limiting designated generator contains both R and R^{-1}.

This script records one convenient corrected principal working point:
    tau = -5
    theta = pi
and checks:
  * catalyst and parent fixed equations,
  * forward/backward full-cell coefficients,
  * the 4x4 real transversality Jacobian in (kappa,A,theta,phi_M),
  * corrected first-order profile coefficients and localization margins.

Publication use should replace floating evaluations by interval-certified bounds.
"""

import cmath
import math
import numpy as np

U = 1.8
X = 0.70
TAU = -5.0


def gamma(beta, z, u=U):
    return (
        1.0 / math.sqrt(1.0 + u*u*z*z)
        - beta*beta*(1.0 + u*u*z*z)/(1.0 + u*u)**1.5
    )


G1 = U * gamma(1, X)
G2 = U * gamma(2, X)


def fixed_data(kappa, amplitude, theta=math.pi, phi=0.0):
    rho_c = math.exp(-2.0*kappa*G1)
    rho_p = math.exp(-kappa*G2) * cmath.exp(1j*theta)
    ep = cmath.exp(1j*phi)
    em = cmath.exp(-1j*phi)

    c1p = 0.5 + TAU
    c1m = -0.5 + TAU
    c2p = 0.5 + 2.0*TAU
    c2m = -0.5 + 2.0*TAU

    e_c = amplitude*(ep*c1p*rho_c + em*c1m/rho_c)
    e_p = amplitude*(ep*c2p*rho_p + em*c2m/rho_p)

    f_c = cmath.exp(e_c)/rho_c - 1.0
    f_p = cmath.exp(e_p)/(rho_p*rho_p) - 1.0
    return rho_c, rho_p, f_c, f_p


# Corrected root of the two real symmetric fixed equations.
KAPPA = 0.610483084671222221636964364712
AMP = 0.0531772657077232063511162956775
THETA = math.pi
PHI = 0.0

rho_c, rho_p, f_c, f_p = fixed_data(KAPPA, AMP, THETA, PHI)

c1p = 0.5 + TAU
c1m = -0.5 + TAU
c2p = 0.5 + 2.0*TAU
c2m = -0.5 + 2.0*TAU

lam_cp = AMP*c1p
lam_cm = AMP*c1m
lam_pp = AMP*c2p
lam_pm = AMP*c2m

D1 = c1p*rho_c + c1m/rho_c
J1 = c1p*rho_c - c1m/rho_c
D2 = c2p*rho_p.real + c2m/rho_p.real
J2 = c2p*rho_p.real - c2m/rho_p.real

# Analytic Jacobian at theta=pi, phi=0.
d_fc_k = -2.0*G1*(AMP*J1 - 1.0)
d_fc_A = D1
d_fc_phi = AMP*J1

d_fp_k = G2*(2.0 - AMP*J2)
d_fp_A = D2
d_fp_theta = AMP*J2 - 2.0
d_fp_phi = AMP*J2

J = np.array([
    [d_fc_k, d_fc_A, 0.0, 0.0],
    [0.0, 0.0, 0.0, d_fc_phi],
    [d_fp_k, d_fp_A, 0.0, 0.0],
    [0.0, 0.0, d_fp_theta, d_fp_phi],
], dtype=float)

# Corrected continuum profile coefficients.
Lx = math.sqrt(1.0 + X*X)
fp = -X/(2.0*(1.0 + X*X)**1.5)
d_c = 2.0*KAPPA
d_p = KAPPA

v_c = AMP*J1 - 1.0
v_p = AMP*J2 - 2.0
B_c = AMP*d_c*Lx*fp*(rho_c - 1.0/rho_c)
B_p = AMP*d_p*Lx*fp*(rho_p.real - 1.0/rho_p.real)


def gamma_prime(beta, z, u=U):
    return (
        -u*u*z/(1.0 + u*u*z*z)**1.5
        -2.0*beta*beta*u*u*z/(1.0 + u*u)**1.5
    )


alpha1 = -0.5*U*gamma_prime(1, X)
alpha2 = -0.5*U*gamma_prime(2, X)

threshold_c = -2.0*alpha1*d_c*d_c
threshold_p = -2.0*alpha2*d_p*d_p

print("corrected bidirectional principal point")
print("tau      =", TAU)
print("kappa    = %.16f" % KAPPA)
print("A        = %.16f" % AMP)
print("theta    = %.16f" % THETA)
print("rho_C    =", rho_c)
print("rho_P    =", rho_p)
print()
print("fixed residuals")
print("F_C =", f_c)
print("F_P =", f_p)
print()
print("full-cell shift coefficients")
print("C +M =", lam_cp, " C -M =", lam_cm)
print("P +M =", lam_pp, " P -M =", lam_pm)
print()
print("4x4 Jacobian")
print(J)
print("det =", np.linalg.det(J))
print("singular values =", np.linalg.svd(J, compute_uv=False))
print()
print("profile coefficients")
print("v_C =", v_c, "B_C =", B_c, "B_C/v_C =", B_c/v_c)
print("v_P =", v_p, "B_P =", B_p, "B_P/v_P =", B_p/v_p)
print("localization thresholds")
print("C:", threshold_c)
print("P:", threshold_p)
