"""Exact finite-u source-envelope diagnostic for the beta-(2,1) reset design.

We impose simultaneously

    x + delta = 1

so the surviving beta-one child is exactly at its source turning point, and the
first relay resonance

    E_2,u(x) + E_1,u(x+delta) = E_1,u(x-delta).

Because E_1,u(1)=0, this reduces to

    E_2,u(1-delta) = E_1,u(1-2 delta).

The cleanup defect is

    Delta_clean(u) = E_1,u(x+3 delta) - E_2,u(x).

Negative Delta_clean means the spent old catalyst is exponentially below the
renewed beta-two parent at the reset face T=2 delta.

The script also solves the exact simultaneous and ordered reset-action equations.
It is a reproducibility calculation, not outward-rounded interval arithmetic.
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


def cleanup_data(u):
    d = solve_delta(u)
    x = 1.0 - d
    parent = env(2, u, x)
    spent = env(1, u, x + 3.0 * d)
    return d, x, spent - parent, parent, spent


def simultaneous_reset_s(u, x, d):
    T = 2.0 * d

    def defect(s):
        return (
            3.0 * env(1, u, x + d + s)
            + 2.0 * env(1, u, x - d + s)
            - env(1, u, x - 3.0 * d + s)
            + env(1, u, x - d)
            + env(1, u, x + d)
            - env(2, u, x)
        )

    # The relevant root is the one inside the causal interval.
    left = 0.0
    fl = defect(left)
    for j in range(1, 2001):
        right = T * j / 2000.0
        fr = defect(right)
        if fl * fr < 0:
            return bisect(defect, left, right)
        left, fl = right, fr
    raise RuntimeError("no simultaneous reset root")


def ordered_reset_s(u, x, d, eta):
    T = 2.0 * d

    def C(t):
        return env(1, u, x + d + t)

    def D(t):
        return env(1, u, x - d + t)

    def final_action(s):
        t1 = s
        t2 = s + eta
        t3 = s + 2.0 * eta
        t4 = s + 3.0 * eta

        P1 = C(t1) + D(t1)
        P2 = P1 + env(2, u, x + t2) - env(2, u, x + t1)
        E2 = P2 + D(t2)
        E3 = E2 + env(3, u, x - d / 3.0 + t3) - env(3, u, x - d / 3.0 + t2)
        Q3 = E3 + C(t3)
        Q4 = Q3 + env(2, u, x - d + t4) - env(2, u, x - d + t3)
        H4 = Q4 + C(t4)
        HT = H4 + env(1, u, x - 3.0 * d + T) - env(1, u, x - 3.0 * d + t4)
        return HT + D(T)

    f = lambda s: final_action(s) - env(2, u, x)
    upper = T - 3.0 * eta
    left = 0.0
    fl = f(left)
    for j in range(1, 2001):
        right = upper * j / 2000.0
        fr = f(right)
        if fl * fr < 0:
            return bisect(f, left, right), final_action
        left, fl = right, fr
    raise RuntimeError("no ordered reset root")


print("finite-u turning-point cleanup table")
for u in (2.0, 3.0, 4.0, 4.5, 4.9, 5.0, 7.0, 10.0, 20.0, 100.0):
    d, x, dc, parent, spent = cleanup_data(u)
    print(
        f"u={u:5.1f}  delta={d:.15f}  x={x:.15f}  "
        f"Delta_clean={dc:+.15e}"
    )

ucrit = bisect(lambda u: cleanup_data(u)[2], 4.0, 5.0)
dcrit, xcrit, _, _, _ = cleanup_data(ucrit)
print("\ncritical cleanup value")
print(f"u_crit  = {ucrit:.15f}")
print(f"delta   = {dcrit:.15f}")
print(f"x       = {xcrit:.15f}")
print(f"u/sqrt(1+u^2) = {ucrit / math.sqrt(1.0 + ucrit*ucrit):.15f}")
print(f"required kappa from theorem-4.6 bound = {2.0/(1.0+ucrit*ucrit):.15f}")

# Concrete exact-source working point.
u = 4.0
d, x, dc, parent, spent = cleanup_data(u)
s0 = simultaneous_reset_s(u, x, d)
eta = 0.005
so, final_action = ordered_reset_s(u, x, d, eta)
T = 2.0 * d
print("\nworking point u=4")
print(f"x       = {x:.15f}")
print(f"delta   = {d:.15f}")
print(f"T       = {T:.15f}")
print(f"s_sim   = {s0:.15f}")
print(f"s_ord   = {so:.15f}")
print(f"eta     = {eta:.15f}")
print(f"T-t4    = {T-(so+3.0*eta):.15f}")
print(f"H slope at t4 = {x-3.0*d+so+3.0*eta:.15f}")
print(f"spent-C cleanup defect = {dc:+.15e}")
print(f"ordered reset residual = {final_action(so)-parent:+.15e}")
print(f"surviving D action at reset = {env(1,u,x+d):+.15e}")
