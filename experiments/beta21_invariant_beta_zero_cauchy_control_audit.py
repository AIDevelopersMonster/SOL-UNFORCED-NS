"""Invariant beta-zero Cauchy-control audit for the corrected beta-(2,1) cell.

Working point:
    u = 2.5
    delta = 0.1375
    x = 0.7779445026067248...
    T = 2 delta.

The beta-zero root is M=P-2C.  The reset shear fixes every kM character.
This script records the principal action facts behind the finite Cauchy-control
repair attempt:

1. one M preload can action-match D-M -> C against the spent old catalyst;
2. one 2M preload can action-match 2M+C -> H against the M+D -> H layer;
3. the remaining parent layer has reset action -0.052619129... in the
   conservative same-time rooted source audit;
4. for every k>=1, a binary cancellation route
       kM + Q_k -> P_1,   Q_k := P_1-kM,
   with both incoming actions <=0 has a strictly decreasing reset-action
   profile.  Its maximum is the common t=0 value
       E_2(x)-E_2(x-2 delta),
   which misses the parent layer by 0.0884182525... .

The printed action margins are floating-point diagnostics.  The derivative
sign for item 4 is algebraic once Gamma_2 is known to be strictly decreasing
on the positive source window.
"""

import math

U = 2.5
DELTA = 0.1375
X = 0.77794450260672482712680064619405
T = 2.0 * DELTA


def turning(beta):
    return math.sqrt((1.0 + U * U) * beta ** (-4.0 / 3.0) - 1.0) / U


def primitive(beta, z):
    z = abs(z)
    return (
        math.asinh(U * z)
        - beta * beta / (1.0 + U * U) ** 1.5
        * (U * z + U ** 3 * z ** 3 / 3.0)
    )


def envelope(beta, z):
    return primitive(beta, z) - primitive(beta, turning(beta))


def gamma(beta, z):
    return (
        1.0 / math.sqrt(1.0 + U * U * z * z)
        - beta * beta * (1.0 + U * U * z * z)
        / (1.0 + U * U) ** 1.5
    )


A_P = envelope(2, X)
A_C = envelope(1, X + DELTA)
A_D = envelope(1, X - DELTA)
A_C_reset = envelope(1, X + 3.0 * DELTA)

# M=D-C has beta zero and constant radial normal U(z_D-z_C)=-2U delta.
LAMBDA_M = -(2.0 * U * DELTA) ** 2 / (1.0 + U * U) ** 1.5


def A_D_t(t):
    return envelope(1, X - DELTA + t)


def A_C_t(t):
    return envelope(1, X + DELTA + t)


def sample_max(f, a, b, n=200000):
    best = (-1.0e100, None)
    for j in range(n + 1):
        t = a + (b - a) * j / n
        y = f(t)
        if y > best[0]:
            best = (y, t)
    return best


# -------------------------------------------------------------------------
# 1. M action needed to match D-M -> C to the spent old C at reset.
# -------------------------------------------------------------------------
def C_cleanup_base(t):
    return (
        A_D_t(t)
        + LAMBDA_M * t
        + primitive(1, X + 3.0 * DELTA)
        - primitive(1, X + DELTA + t)
    )

base_C, t_C = sample_max(C_cleanup_base, 0.0, T, 20000)
A_M0 = A_C_reset - base_C

# -------------------------------------------------------------------------
# 2. H=C_2 enters the audited source window when z_H=1/2.
#    Match M+D -> H with 2M+C -> H using a physical 2M preload.
# -------------------------------------------------------------------------
t_H_min = max(0.0, 0.5 - (X - 3.0 * DELTA))


def H_from_M_D(t):
    return (
        A_M0 + LAMBDA_M * t
        + A_D_t(t)
        + primitive(1, X - DELTA)
        - primitive(1, X - 3.0 * DELTA + t)
    )


def H_from_2M_C_base(t):
    return (
        4.0 * LAMBDA_M * t
        + A_C_t(t)
        + primitive(1, X - DELTA)
        - primitive(1, X - 3.0 * DELTA + t)
    )

H_bad, t_H_bad = sample_max(H_from_M_D, t_H_min, T, 20000)
H_ctl_base, t_H_ctl = sample_max(H_from_2M_C_base, t_H_min, T, 20000)
A_2M0 = H_bad - H_ctl_base

# -------------------------------------------------------------------------
# 3. Conservative same-time rooted parent layer:
#       M + D + D -> P_1=P+2M.
#    Requiring the H intermediate to lie in its safe source window gives
#    t>=t_H_min.  The reset source action is maximized at T for this geometry.
# -------------------------------------------------------------------------
def parent_bad(t):
    return (
        A_M0 + LAMBDA_M * t
        + 2.0 * A_D_t(t)
        + primitive(2, X)
        - primitive(2, X - 2.0 * DELTA + t)
    )

A_parent_bad, t_parent_bad = sample_max(parent_bad, t_H_min, T, 20000)

# -------------------------------------------------------------------------
# 4. General invariant-harmonic binary route.
#
# Q_k=P_1-kM has beta two and reduced slope
#       z_Q = z_{P_1}+k delta.
# With zero (maximal admissible) incoming actions for kM and Q_k, its reset
# action is
#
# F_k(t)=k^2 lambda_M t
#       + [I_2(z_Q(t))-I_2(z_Q(0))]
#       + I_2(x)-I_2(z_{P_1}(t)).
#
# Hence
# F'_k = k^2 lambda_M + Gamma_2(z_{P_1}+k delta)-Gamma_2(z_{P_1}) < 0
# for k>=1 on the positive source window.
# -------------------------------------------------------------------------
def binary_parent_route(k, t):
    z_parent = X - 2.0 * DELTA + t
    z_q = z_parent + k * DELTA
    z_q0 = X + (k - 2.0) * DELTA
    return (
        k * k * LAMBDA_M * t
        + primitive(2, z_q) - primitive(2, z_q0)
        + primitive(2, X) - primitive(2, z_parent)
    )

common_binary_max = primitive(2, X) - primitive(2, X - 2.0 * DELTA)
parent_gap = A_parent_bad - common_binary_max

print("corrected working point")
print("A_P       = %+.16e" % A_P)
print("A_C       = %+.16e" % A_C)
print("A_D       = %+.16e" % A_D)
print("lambda_M  = %+.16e" % LAMBDA_M)
print()
print("C cleanup")
print("base reset max = %+.16e at t=%.16f" % (base_C, t_C))
print("required A_M(0)= %+.16e" % A_M0)
print()
print("H layer")
print("source-window entry t_H = %.16f" % t_H_min)
print("M+D reset max       = %+.16e at t=%.16f" % (H_bad, t_H_bad))
print("2M+C base reset max = %+.16e at t=%.16f" % (H_ctl_base, t_H_ctl))
print("required A_2M(0)    = %+.16e" % A_2M0)
print()
print("remaining parent layer")
print("A_parent_bad = %+.16e at t=%.16f" % (A_parent_bad, t_parent_bad))
print("binary kM+Qk max = %+.16e" % common_binary_max)
print("unavoidable gap    = %+.16e" % parent_gap)
print()
for k in range(1, 7):
    f0 = binary_parent_route(k, 0.0)
    # derivative sampled only as a diagnostic; the sign proof is analytic.
    deriv_max = -1.0e100
    for j in range(1001):
        t = T * j / 1000.0
        zp = X - 2.0 * DELTA + t
        zq = zp + k * DELTA
        derivative = (
            k * k * LAMBDA_M
            + gamma(2, zq)
            - gamma(2, zp)
        )
        deriv_max = max(deriv_max, derivative)
    print("k=%d  F_k(0)=%+.16e  max sampled F'_k=%+.16e" % (k, f0, deriv_max))
