"""Reproducibility audit for the corrected beta-(2,1) reset shear and
beta-zero-memory Cauchy repair.

This script checks, at the corrected u=2.5 working point,

1. the exact unipotent reset shear R(K)=K+beta(K) M;
2. the reset-action head/tail split along the beta-one root orbit;
3. the fixed positive parent-orbit leakage of P_new;
4. the action condition for a beta-zero M preload to source the old catalyst C;
5. the resulting unavoidable M+D->H->P_new supercritical reset contribution;
6. the natural-envelope impossibility of cancelling that contribution with a
   homogeneous same-character P_new preload.

The numerical values are diagnostic floating-point certificates. The algebraic
identities and monotonicity argument are exact; publication use of the printed
margins should be interval-certified.
"""

import math

U = 2.5
DELTA = 0.1375
X = 0.77794450260672482712680064619405
TSTAR = 0.22512911698286797975123849107983
T = 2.0 * DELTA


def turning(beta):
    value = (1.0 + U * U) * beta ** (-4.0 / 3.0) - 1.0
    if value < 0.0:
        raise ValueError("no real turning point")
    return math.sqrt(value) / U


def primitive(beta, z):
    z = abs(z)
    return (
        math.asinh(U * z)
        - beta * beta / (1.0 + U * U) ** 1.5
        * (U * z + U ** 3 * z ** 3 / 3.0)
    )


def env(beta, z):
    xb = turning(beta)
    return primitive(beta, z) - primitive(beta, xb)


def gamma(beta, z):
    return (
        1.0 / math.sqrt(1.0 + U * U * z * z)
        - beta * beta * (1.0 + U * U * z * z) / (1.0 + U * U) ** 1.5
    )


def beta_zero_data(zD, zC):
    sD = U * zD
    sC = U * zC
    m = sD - sC
    S = sD + sC
    R = math.sqrt(1.0 + sD * sD) + math.sqrt(1.0 + sC * sC)
    bM = (0.0, -S, -R)
    return m, bM


def wave_plus_root_coeff(beta, z, m, bM):
    s = U * z
    g = (1.0, -s, -math.sqrt(1.0 + s * s))
    q = [m * bM[j] + beta * bM[1] * g[j] for j in range(3)]
    st = s + m / beta
    ah = (q[0] - st * q[1]) / (1.0 + st * st)
    an = q[2] / (-math.sqrt(1.0 + st * st))
    return 0.5 * (ah + an)


def sum_coeff(b1, z1, b2, z2):
    s1 = U * z1
    s2 = U * z2
    bt = b1 + b2
    st = (b1 * s1 + b2 * s2) / bt
    bracket = (
        (b1 - b2 + st * (b1 * s1 - b2 * s2)) / (1.0 + st * st)
        + (
            b1 * math.sqrt(1.0 + s1 * s1)
            - b2 * math.sqrt(1.0 + s2 * s2)
        ) / math.sqrt(1.0 + st * st)
    )
    return 0.5 * (s1 - s2) * bracket


# --- exact lattice reset algebra ------------------------------------------
# Coordinates are (a,b) for a P + b C; beta(a,b)=2a+b.
P = (1, 0)
C = (0, 1)
M = (1, -2)


def add(A, B):
    return (A[0] + B[0], A[1] + B[1])


def scale(k, A):
    return (k * A[0], k * A[1])


def beta(A):
    return 2 * A[0] + A[1]


def reset(A):
    # P -> 3P-4C, C -> P-C.
    a, b = A
    return (3 * a + b, -4 * a - b)


for a in range(-5, 6):
    for b in range(-8, 9):
        K = (a, b)
        assert reset(K) == add(K, scale(beta(K), M))
assert reset(M) == M

D = add(P, scale(-1, C))
print("reset shear")
print("M =", M, "beta(M)=", beta(M), "R(M)=", reset(M))
for k in range(5):
    Xk = add(D, scale(k, M))
    print("X_%d = %s  R(X_%d)=%s" % (k, Xk, k, reset(Xk)))
print()

# --- corrected action data ------------------------------------------------
AP = env(2, X)
AD_T = env(1, X + DELTA)
AC_T = env(1, X + 3.0 * DELTA)

print("reset actions")
print("A_P target = %+.16e" % AP)
print("A_D(T)     = %+.16e" % AD_T)
print("A_C(T)     = %+.16e" % AC_T)
print()

print("beta-one root orbit head/tail")
for k in range(6):
    action = (k + 1) * AD_T + k * AC_T
    print(
        "k=%d  action=%+.16e  action-A_P=%+.16e"
        % (k, action, action - AP)
    )
print()

# Parent orbit old-C,D leaf actions.
print("parent orbit")
for n in range(1, 4):
    # R^n(P)=(2n+1)D-(2n-1)C.
    action = (2 * n + 1) * AD_T + (2 * n - 1) * AC_T
    print(
        "J_%d action=%+.16e  action-A_P=%+.16e"
        % (n, action, action - AP)
    )
print()

# --- beta-zero M memory ---------------------------------------------------
zD0 = X - DELTA
zC0 = X + DELTA
# M=D-C has constant beta-zero radial-normal scalar U(z_D-z_C).
LAMBDA_M = -(U * (zD0 - zC0)) ** 2 / (1.0 + U * U) ** 1.5
print("lambda_M = %+.16e" % LAMBDA_M)


def A_C(s):
    return env(1, X + DELTA + s)


def A_D(s):
    return env(1, X - DELTA + s)


def required_M_input_for_C_cleanup(s):
    # A_M(s)=A0+lambda_M*s must equal A_C(s)-A_D(s).
    return A_C(s) - A_D(s) - LAMBDA_M * s


def bisection(f, a, b, iters=100):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0.0:
        raise RuntimeError("no sign change")
    for _ in range(iters):
        m = 0.5 * (a + b)
        fm = f(m)
        if fa * fm <= 0.0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return 0.5 * (a + b)


sM = bisection(required_M_input_for_C_cleanup, 0.0, T)
print("O(1) M-input cleanup threshold s_M = %.16f" % sM)
print(
    "required A_M(0) at old t_* = %+.16e"
    % required_M_input_for_C_cleanup(TSTAR)
)
print()

# If M is ever strong enough to source/cancel C at leading action at a time s,
# then A_M(s)>=A_C(s)-A_D(s). Propagating the same beta-zero memory to T gives
# A_M(T)>=A_C(s)-A_D(s)+lambda_M*(T-s). Its unavoidable two-D descendant has
# reset source action A_M(T)+2A_D(T).
def fatal_gap(s):
    return (
        A_C(s)
        - A_D(s)
        + LAMBDA_M * (T - s)
        + 2.0 * AD_T
        - AP
    )

# Exact monotonicity: gamma_1 is strictly decreasing for z>0. Moreover the
# second term in gamma' alone gives a simple uniform negative bound on G'.
zD_min = X - DELTA
uniform_gamma_difference_upper = -(
    2.0 * U * U * zD_min / (1.0 + U * U) ** 1.5
) * (2.0 * DELTA)
uniform_Gprime_upper = uniform_gamma_difference_upper - LAMBDA_M
assert uniform_Gprime_upper < 0.0

G_T = fatal_gap(T)
print("fatal M-memory parent gap")
print("uniform upper bound on G'(s) = %+.16e" % uniform_Gprime_upper)
print("min_s G(s) = G(T) = %+.16e" % G_T)
print()

# Principal coefficient margins for the unavoidable path M+D->H->P_new and
# the catalyst source D-M->C on the late interval [t_*,T].
mins = [float("inf")] * 3
for j in range(2001):
    s = TSTAR + (T - TSTAR) * j / 2000.0
    zD = X - DELTA + s
    zC = X + DELTA + s
    m, bM = beta_zero_data(zD, zC)
    zH = 2.0 * zD - zC
    vals = (
        wave_plus_root_coeff(1, zD, m, bM),       # M+D -> H
        sum_coeff(1, zH, 1, zD),                  # H+D -> P_new
        wave_plus_root_coeff(1, zD, -m, bM),      # D-M -> C
    )
    for i, value in enumerate(vals):
        mins[i] = min(mins[i], abs(value))

print("sampled late coefficient margins")
print("min |M+D -> H|      = %.16e" % mins[0])
print("min |H+D -> P_new|  = %.16e" % mins[1])
print("min |D-M -> C|      = %.16e" % mins[2])
print()

# A homogeneous same-character P_new preload starts at reduced slope X-2d and
# reaches X at reset. To cancel even the *minimal* M-induced parent action
# F_min=A_C(T)+A_D(T), its input action would have to exceed the natural
# envelope maximum 0.
E2_J1_in = env(2, X - 2.0 * DELTA)
prop_increment = AP - E2_J1_in
F_min = AC_T + AD_T
required_J1_input = F_min - prop_increment
print("same-character P_new preload")
print("E2(X-2delta)          = %+.16e" % E2_J1_in)
print("minimal bad final act = %+.16e" % F_min)
print("required input action  = %+.16e" % required_J1_input)
assert required_J1_input > 0.0
