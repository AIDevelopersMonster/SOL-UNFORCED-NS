"""Principal audit for the low-u beta-(2,1) boundary-layer reset.

Preferred working point:
    u = 1.8
    x = 0.70
    delta_S = kappa / S

The script records the limiting bilateral fixed-point parameters, physical
large-deviation localization, critical action gaps on the orbit core, scalar
transversality margins, and representative finite-S convergence values found
from the exact finite-u envelope/principal-symbol audit.

The finite-S convergence table below is a reproducibility snapshot of the
companion numerical quadrature used in the branch analysis. Publication use
should replace the floating values by interval-certified bounds.
"""

import cmath
import math

U = 1.8
X = 0.70
CORE = 0.03


def turning(beta, u=U):
    v = (1.0 + u*u) * beta ** (-4.0/3.0) - 1.0
    return math.sqrt(v)/u if v >= 0.0 else None


def primitive(beta, z, u=U):
    z = abs(z)
    return (
        math.asinh(u*z)
        - beta*beta/(1.0+u*u)**1.5
        * (u*z + u**3*z**3/3.0)
    )


def envelope(beta, z, u=U):
    xb = turning(beta, u)
    if xb is None:
        raise ValueError("no real turning point")
    return primitive(beta, z, u) - primitive(beta, xb, u)


def gamma(beta, z, u=U):
    return (
        1.0/math.sqrt(1.0+u*u*z*z)
        - beta*beta*(1.0+u*u*z*z)/(1.0+u*u)**1.5
    )


g1 = U * gamma(1, X)
g2 = U * gamma(2, X)
cos_theta = g2/(2.0*g1)
theta = math.acos(cos_theta)
kappa = (2.0*math.pi - 2.0*theta)/(4.0*g1*math.sin(theta))

rho_C = math.exp(-2.0*kappa*g1)
R_P = math.exp(-kappa*g2)
rho_P = R_P * complex(math.cos(theta), math.sin(theta))
lambda_C = math.log(rho_C)/rho_C
mu_P = -4.0*kappa*g1*math.exp(kappa*g2)


def fixed_C(rho=rho_C):
    return math.exp(lambda_C*rho)/rho


def fixed_P(k=kappa, th=theta):
    R = math.exp(-k*g2)
    rho = R * complex(math.cos(th), math.sin(th))
    mu = -4.0*k*g1*math.exp(k*g2)
    return cmath.exp(mu*rho)/(rho*rho)


def localization(beta, z):
    gb = U * gamma(beta, X)
    return envelope(beta, z) - envelope(beta, X) + (X-z)*gb

# Scalar transversality.
dlogC = lambda_C - 1.0/rho_C
dlogP = mu_P - 2.0/rho_P

# Real 2x2 parent Jacobian by a symmetric numerical derivative of the exact
# limiting scalar dispersion relation.
h = 1.0e-6
dK = (fixed_P(kappa+h, theta)-fixed_P(kappa-h, theta))/(2.0*h)
dT = (fixed_P(kappa, theta+h)-fixed_P(kappa, theta-h))/(2.0*h)
det_parent = dK.real*dT.imag - dT.real*dK.imag

# Critical feedback margins on |z-X|<=CORE, recorded from dense optimization.
GAP_CC_TO_Q = -0.05925018225
GAP_Q_MINUS_C_TO_C = -0.11675015251

finite_S = [
    # S, |P_multiplier-1|, |C_multiplier-1|
    (50,    5.038e-2, 3.089e-5),
    (100,   2.631e-2, 7.715e-6),
    (200,   1.346e-2, 1.928e-6),
    (500,   5.463e-3, 3.085e-7),
    (1000,  2.745e-3, 7.713e-8),
    (2000,  1.376e-3, 1.928e-8),
    (5000,  5.511e-4, 3.084e-9),
    (10000, 2.757e-4, 7.674e-10),
]

print("working point")
print("u      =", U)
print("x      =", X)
print("g1     = %+.16e" % g1)
print("g2     = %+.16e" % g2)
print("theta  = %.16f" % theta)
print("kappa  = %.16f" % kappa)
print("rho_C  =", rho_C)
print("rho_P  =", rho_P)
print("lambda = %+.16e" % lambda_C)
print("mu     = %+.16e" % mu_P)
print()
print("fixed multipliers")
print("C:", fixed_C())
print("P:", fixed_P())
print()
print("transversality")
print("dlog C =", dlogC)
print("dlog P =", dlogP)
print("d_k Fp =", dK)
print("d_t Fp =", dT)
print("det real parent Jacobian = %.16e" % det_parent)
print()
print("physical localization")
for z in (X-CORE, X+CORE):
    print("z=%.5f H1=%+.16e H2=%+.16e" %
          (z, localization(1,z), localization(2,z)))
print()
print("critical feedback margins")
print("C+C -> Q max defect      = %+.16e" % GAP_CC_TO_Q)
print("Q-C -> C max defect      = %+.16e" % GAP_Q_MINUS_C_TO_C)
print()
print("finite-S convergence snapshot")
for S, ep, ec in finite_S:
    print("S=%5d  parent=%9.3e  catalyst=%9.3e" % (S,ep,ec))
