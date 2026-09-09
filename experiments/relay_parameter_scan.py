#!/usr/bin/env python3
"""
Reproduce the current reduced beta-relay witness.

This script checks only reduced arithmetic/model equations.
It does NOT prove a PDE relay lemma.
"""

import math

r = 17 / 12
h = 2 * math.log2(r) - 1

# Preferred v0.2 relay pair.  Both beta-dependent turning points
# lie in the raw OpenAI pulse interval |s|/u_* in [1/2, 3/2].
beta1 = 5 / 6
beta2 = 7 / 12
beta_minus = beta1 - beta2

xc = 17 / 32
x1 = 1.4227047612075736
y2 = 0.742256801725105
x2 = -y2


def F(beta, x):
    return 1 / x - beta * beta * x * x


def J(beta, x):
    return beta ** (2 / 3) * (
        math.log(x * beta ** (2 / 3))
        - (beta * beta / 3) * (x ** 3 - beta ** -2)
    )


phase_residual = beta1 * x1 - beta2 * y2 - r * xc
envelope_residual = J(beta1, x1) + J(beta2, y2) - J(1, xc)

turn1 = beta1 ** (-2 / 3)
turn2 = beta2 ** (-2 / 3)
turning_threshold = (2 / 3) ** 1.5

# Formal difference-branch reduced slope.  This lies outside the standard
# raw pulse interval and is only a diagnostic for strong damping, not a
# proof that the sideband is already controlled in the PDE construction.
x_minus = (beta1 * x1 + beta2 * y2) / beta_minus

print("SOL-UNFORCED-NS reduced beta-relay check v0.2")
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
print(f"phase residual          = {phase_residual:.3e}")
print(f"envelope residual       = {envelope_residual:.3e}")
print()
print(f"x1                       = {x1:.16f}")
print(f"x2                       = {x2:.16f}")
print(f"xc                       = {xc:.16f}")
print(f"F_beta1(x1)              = {F(beta1, x1): .12f}")
print(f"F_beta2(|x2|)            = {F(beta2, y2): .12f}")
print(f"F_1(xc)                  = {F(1, xc): .12f}")
print(f"x_minus                  = {x_minus: .12f}")
print(f"F_beta_minus(x_minus)    = {F(beta_minus, x_minus): .12f}")
print()
print("Desired signs:")
print("  old parent: negative")
print("  catalyst:   positive")
print("  child:      positive")
print("  sideband diagnostic: negative")
print()
print("Caution: x_minus lies outside the standard raw pulse interval; the")
print("sideband still needs a separate nonresonant/damped-source estimate.")
