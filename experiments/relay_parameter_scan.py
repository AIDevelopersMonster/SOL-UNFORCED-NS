#!/usr/bin/env python3
"""
Reproduce the current reduced beta-relay witness v0.3.

This script checks only reduced arithmetic/model equations and a finite-u_*
continuation diagnostic. It does NOT prove a PDE relay lemma.
"""

import math

r = 17 / 12
h = 2 * math.log2(r) - 1

# Preferred v0.3 pair.
beta1 = 41 / 48
beta2 = 9 / 16
beta_minus = beta1 - beta2

# Fixed rational coordinate for the decaying parent.
x1 = 71 / 48

# Reduced witness root.
y2 = 0.9381374363215359
xc = (beta1 * x1 - beta2 * y2) / r


def F(beta, x):
    return 1 / x - beta * beta * x * x


def I(beta, x):
    """Correct common-L_s reduced envelope primitive."""
    turn = beta ** (-2 / 3)
    return math.log(x / turn) - (beta * beta / 3) * (x ** 3 - turn ** 3)


def exact_turn(beta, u):
    return math.sqrt((1 + u * u) * beta ** (-4 / 3) - 1) / u


def E(beta, x, u):
    """Exact normalized envelope primitive centered at exact turning point."""
    xt = exact_turn(beta, u)
    y = u * x
    yt = u * xt
    return (
        math.asinh(y)
        - math.asinh(yt)
        - (beta * beta / (1 + u * u) ** 1.5)
        * ((y - yt) + (y ** 3 - yt ** 3) / 3)
    )


def F_exact(beta, x, u):
    y = u * x
    return 1 / math.sqrt(1 + y * y) - beta * beta * (1 + y * y) / (1 + u * u) ** 1.5


phase_residual = beta1 * x1 - beta2 * y2 - r * xc
envelope_residual = I(beta1, x1) + I(beta2, y2) - I(1, xc)
transversality = F(beta2, y2) + (beta2 / r) * F(1, xc)

turn1 = beta1 ** (-2 / 3)
turn2 = beta2 ** (-2 / 3)
turning_threshold = (2 / 3) ** 1.5

print("SOL-UNFORCED-NS reduced beta-relay check v0.3")
print("------------------------------------------------")
print(f"r                       = {r:.16f}")
print(f"h                       = {h:.16f}")
print(f"turning beta threshold  = {turning_threshold:.16f}")
print(f"beta1                   = {beta1:.16f}")
print(f"beta2                   = {beta2:.16f}")
print(f"beta1 + beta2           = {beta1 + beta2:.16f}")
print(f"beta_minus              = {beta_minus:.16f}")
print(f"turn1                   = {turn1:.16f}")
print(f"turn2                   = {turn2:.16f}")
print(f"x1                       = {x1:.16f}")
print(f"y2                       = {y2:.16f}")
print(f"xc                       = {xc:.16f}")
print(f"phase residual          = {phase_residual:.3e}")
print(f"envelope residual       = {envelope_residual:.3e}")
print(f"R'(y2)                  = {transversality:.12f}")
print()
print(f"F_beta1(x1)             = {F(beta1, x1): .12f}")
print(f"F_beta2(y2)             = {F(beta2, y2): .12f}")
print(f"F_1(xc)                 = {F(1, xc): .12f}")
print()
print("Finite-u_* exact-envelope continuation diagnostics")
for u in [10, 20, 50, 100, 1000]:
    # Newton with a very small hand-written solver around the reduced root.
    y = y2
    for _ in range(20):
        xchild = (beta1 * x1 - beta2 * y) / r
        R = E(beta1, x1, u) + E(beta2, y, u) - E(1, xchild, u)
        # numerical derivative
        d = 1e-7
        yp = y + d
        ym = y - d
        xp = (beta1 * x1 - beta2 * yp) / r
        xm = (beta1 * x1 - beta2 * ym) / r
        Rp = E(beta1, x1, u) + E(beta2, yp, u) - E(1, xp, u)
        Rm = E(beta1, x1, u) + E(beta2, ym, u) - E(1, xm, u)
        der = (Rp - Rm) / (2 * d)
        y -= R / der
    xchild = (beta1 * x1 - beta2 * y) / r
    print(
        f"u={u:4d}  y2={y:.12f}  xc={xchild:.12f}  "
        f"signs=({F_exact(beta1,x1,u):+.6e},"
        f"{F_exact(beta2,y,u):+.6e},"
        f"{F_exact(1,xchild,u):+.6e})"
    )

print()
print("Interpretation:")
print("  parent1: decaying")
print("  parent2: growing")
print("  child:   growing")
print("  reduced resonance is transverse")
print()
print("Open obligations: asynchronous translated support geometry, localized")
print("curl-generated interaction estimate, and nonresonant sideband disposal.")
