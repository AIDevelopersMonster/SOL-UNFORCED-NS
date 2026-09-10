#!/usr/bin/env python3
"""Diagnostics for SOL-UNFORCED-NS v0.6 integral-beta relay.

The theorem is in proofs/integral_beta_v06_finite_u_action_filter.md.
This script checks numerical roots and feedback action gaps; it is not the
rigorous certificate.
"""

import math

BETA1 = 2.0
BETA2 = 1.0
X1 = 0.75


def I(beta, x):
    return math.log(x) + (2.0/3.0)*math.log(beta) - beta*beta*x**3/3.0 + 1.0/3.0


def xturn(beta, u):
    a = beta ** (-2.0/3.0)
    return math.sqrt(a*a + (a*a - 1.0)/u**2)


def E(beta, u, x):
    xt = xturn(beta, u)
    return (
        math.asinh(u*x) - math.asinh(u*xt)
        - beta*beta/(1.0+u*u)**1.5
        * (u*(x-xt) + u**3*(x**3-xt**3)/3.0)
    )


def G(u, y):
    xc = 1.5 - y
    return E(2.0, u, X1) + E(1.0, u, y) - E(1.0, u, xc)


def solve(u, lo=0.76, hi=0.80):
    flo = G(u, lo)
    fhi = G(u, hi)
    if flo*fhi >= 0:
        raise RuntimeError("root not bracketed")
    for _ in range(100):
        mid = 0.5*(lo+hi)
        fm = G(u, mid)
        if flo*fm <= 0:
            hi = mid
        else:
            lo = mid
            flo = fm
    return 0.5*(lo+hi)


def action_gap_m2(u, y):
    xc = 1.5-y
    x2 = 3.0-3.0*y
    A = E(2.0, u, X1)
    B = E(1.0, u, y)
    return 2.0*A + 3.0*B - E(1.0, u, x2)


print("SOL-UNFORCED-NS v0.6 integral-beta diagnostics")
print("------------------------------------------------")
for u in [20, 50, 100, 1000]:
    y = solve(float(u))
    xc = 1.5-y
    x2 = 3.0-3.0*y
    print(
        f"u={u:4d}  y={y:.15f}  xc={xc:.15f}  "
        f"x2={x2:.15f}  Delta2={action_gap_m2(float(u),y):+.12f}"
    )

print("\nReduced root ~ 0.7854873695884608")
print("The rigorous theorem proves existence/uniqueness for every u>=20 and")
print("an exponential action deficit for m2=(2,-3) and the whole in-window")
print("unit-beta feedback ladder except the deliberately resonant child.")
