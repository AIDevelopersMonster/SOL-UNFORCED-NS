"""Strong-H renewal bifurcation for the active beta-(2,1) reset cell.

After the first three active gates, the fourth character H=2D-C is generated
more strongly by the unavoidable mean-root path than by the nominal Q-C edge.
Accept that leading root H and ask whether the final edge

    H + D -> P_new = 3D - C

can land on the renewed beta-two parent action at the reset face T=2 delta.

For the turning-point family delta(u), the exact action equation reduces to

    F_u(t) = E_1,u(1+t)
             + 3 E_1,u(1-2 delta+t)
             - E_2,u(1-3 delta+t) = 0.

At t=T its value is exactly the old spent-C cleanup defect.  Consequently the
old cleanup sign change at u_crit is also the bifurcation point for the strong-H
active-renewal root.

This is a reproducibility calculation, not outward-rounded interval arithmetic.
"""

import math


def turning(beta, u):
    return math.sqrt((1.0 + u * u) * beta ** (-4.0 / 3.0) - 1.0) / u


def env(beta, u, x):
    xb = turning(beta, u)
    return (
        math.asinh(u * x)
        - math.asinh(u * xb)
        - beta * beta / (1.0 + u * u) ** 1.5
        * (u * (x - xb) + u**3 / 3.0 * (x**3 - xb**3))
    )


def bisect(f, a, b, n=120):
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
    return bisect(f, 0.10, 0.24)


def cleanup_defect(u):
    d = solve_delta(u)
    x = 1.0 - d
    return env(1, u, x + 3.0 * d) - env(2, u, x)


def renewal_function(u, d, t):
    return (
        env(1, u, 1.0 + t)
        + 3.0 * env(1, u, 1.0 - 2.0 * d + t)
        - env(2, u, 1.0 - 3.0 * d + t)
    )


def strong_H_root(u):
    d = solve_delta(u)
    T = 2.0 * d
    f = lambda t: renewal_function(u, d, t)

    roots = []
    left = 0.0
    fl = f(left)
    for j in range(1, 6001):
        right = T * j / 6000.0
        fr = f(right)
        if fl * fr < 0.0:
            roots.append(bisect(f, left, right))
        left, fl = right, fr
    return d, T, f(0.0), f(T), roots


ucrit = bisect(cleanup_defect, 4.0, 5.0)
print(f"u_crit = {ucrit:.15f}")
print()

for u in (4.0, 4.5, 4.9, ucrit, 5.0, 5.2, 5.5, 6.0, 7.0, 10.0, 20.0):
    d, T, f0, fT, roots = strong_H_root(u)
    print(f"u={u: .12f}")
    print(f"  delta = {d:.15f}")
    print(f"  T     = {T:.15f}")
    print(f"  F(0)  = {f0:+.15e}")
    print(f"  F(T)  = {fT:+.15e}")
    if roots:
        for r in roots:
            print(f"  root  = {r:.15f}   T-root={T-r:.15e}")
    else:
        print("  root  = none")
    print()
