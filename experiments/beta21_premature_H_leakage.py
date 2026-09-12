"""Diagnostic for premature same-collar H leakage in the beta-(2,1) cleanup family.

The turning-point cleanup gauge is
    x + delta = 1,
    E_2,u(x) = E_1,u(1-2 delta).

If the nonlinear descendants generated in the first relay collar are allowed to
iterate immediately, the designated late chain can collapse at the first collar:

    D + C -> P,
    P + D -> E,
    E - C -> Q,
    Q - C -> H.

At that collar the H character is H=2D-C, beta(H)=1, with reduced slope
    z_H(0)=1-4 delta.
At the reset face T=2 delta it has
    z_H(T)=1-2 delta.

The early H action at the reset face is therefore
    A_H^early(T)
      = 2 E_1,u(1-2 delta)
        + E_1,u(1-2 delta) - E_1,u(1-4 delta)
      = 3 A - E_1,u(1-4 delta),
where A=E_1,u(1-2 delta)=E_2,u(1-delta).

Positive A_H^early(T) means fixed-order algebraic/epsilon suppression from the
premature nonlinear genealogy is eventually overwhelmed by homogeneous pulse
growth on the S_* action scale.

This script is a reproducibility calculation, not outward-rounded interval
arithmetic.
"""

import math


def turning(beta, u):
    return math.sqrt((1.0 + u * u) * beta ** (-4.0 / 3.0) - 1.0) / u


def env(beta, u, z):
    xb = turning(beta, u)
    return (
        math.asinh(u * z)
        - math.asinh(u * xb)
        - beta * beta / (1.0 + u * u) ** 1.5
        * (u * (z - xb) + u**3 / 3.0 * (z**3 - xb**3))
    )


def bisect(f, a, b, n=140):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise RuntimeError((a, b, fa, fb))
    for _ in range(n):
        m = 0.5 * (a + b)
        fm = f(m)
        if fa * fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return 0.5 * (a + b)


def solve_delta(u):
    f = lambda d: env(2, u, 1.0 - d) - env(1, u, 1.0 - 2.0 * d)
    # The nontrivial cleanup branch exists in this bracket for the values printed.
    return bisect(f, 0.10, 0.249)


def principal_sum(b1, z1, b2, z2, u):
    s1 = u * z1
    s2 = u * z2
    bt = b1 + b2
    st = (b1 * s1 + b2 * s2) / bt
    return 0.5 * (s1 - s2) * (
        (b1 - b2 + st * (b1 * s1 - b2 * s2)) / (1.0 + st * st)
        + (b1 * math.sqrt(1.0 + s1 * s1) - b2 * math.sqrt(1.0 + s2 * s2))
        / math.sqrt(1.0 + st * st)
    )


def principal_diff(b1, z1, b2, z2, u):
    s1 = u * z1
    s2 = u * z2
    bt = b1 - b2
    st = (b1 * s1 - b2 * s2) / bt
    bracket = (
        b1 + b2
        + st * (b1 * s1 + b2 * s2)
        + (b1 * math.sqrt(1.0 + s1 * s1) + b2 * math.sqrt(1.0 + s2 * s2))
        * math.sqrt(1.0 + st * st)
    )
    return (s1 - s2) * bracket / (2.0 * (1.0 + st * st))


def row(u):
    d = solve_delta(u)
    x = 1.0 - d
    A = env(1, u, 1.0 - 2.0 * d)
    h0 = 1.0 - 4.0 * d
    early_H_reset = 3.0 * A - env(1, u, h0)
    cleanup = env(1, u, 1.0 + 2.0 * d) - env(2, u, x)
    return d, x, A, h0, early_H_reset, cleanup


print("cleanup branch and premature-H reset action")
for u in (1.62, 1.8, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 4.9):
    d, x, A, h0, leak, clean = row(u)
    print(
        f"u={u:4.2f} delta={d:.15f} x={x:.15f} "
        f"H0={h0:.15f} A_H_early(T)={leak:+.15e} "
        f"Delta_clean={clean:+.15e}"
    )

u = 4.0
d, x, A, h0, leak, clean = row(u)
zC = 1.0
zD = 1.0 - 2.0 * d
zP = x
zE = (2.0 * zP + zD) / 3.0
zQ = zD
zH = 2.0 * zQ - zC

print("\nu=4 collapsed-chain principal polarization coefficients")
print("C+D -> P   ", principal_sum(1, zC, 1, zD, u))
print("P+D -> E   ", principal_sum(2, zP, 1, zD, u))
print("E-C -> Q   ", principal_diff(3, zE, 1, zC, u))
print("Q-C -> H   ", principal_diff(2, zQ, 1, zC, u))
print("\nu=4 action data")
print("delta       ", d)
print("x           ", x)
print("A=E1(D0)   ", A)
print("H slope 0   ", h0)
print("H slope T   ", zD)
print("E1(H0)      ", env(1, u, h0))
print("A_H_early(T)", leak)
print("intended H(T) action = E2(x)", env(2, u, x))
print("early-minus-intended H action", leak - env(2, u, x))
