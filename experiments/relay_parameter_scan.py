#!/usr/bin/env python3
"""
Reproduce the v0.1 reduced β-relay witness.

This script checks only the reduced arithmetic/model equations.
It does NOT prove a PDE relay lemma.
"""

import math

r = 17 / 12
h = 2 * math.log2(r) - 1

beta1 = 93 / 100
beta2 = 73 / 150
beta_minus = beta1 - beta2

xc = 17 / 32
x1 = 1.550891747
x2 = -1.417243476

def F(beta, x):
    return 1 / x - beta * beta * x * x

def J(beta, x):
    return beta ** (2 / 3) * (
        math.log(x * beta ** (2 / 3))
        - (beta * beta / 3) * (x ** 3 - beta ** -2)
    )

phase_residual = beta1 * x1 + beta2 * x2 - r * xc
envelope_residual = J(1, xc) - (J(beta1, x1) + J(beta2, abs(x2)))

# Difference-branch slope under the current reduced bookkeeping.
x_minus = (beta1 * x1 - beta2 * x2) / beta_minus

print("SOL-UNFORCED-NS reduced beta-relay check")
print("-----------------------------------------")
print(f"r                  = {r:.16f}")
print(f"h                  = {h:.16f}")
print(f"beta1 + beta2      = {beta1 + beta2:.16f}")
print(f"beta_minus         = {beta_minus:.16f}")
print(f"phase residual     = {phase_residual:.3e}")
print(f"envelope residual  = {envelope_residual:.3e}")
print()
print(f"F_beta1(x1)        = {F(beta1, x1): .12f}")
print(f"F_beta2(|x2|)      = {F(beta2, abs(x2)): .12f}")
print(f"F_1(xc)            = {F(1, xc): .12f}")
print(f"x_minus            = {x_minus: .12f}")
print(f"F_beta_minus(x-)   = {F(beta_minus, x_minus): .12f}")
print()
print("Desired signs:")
print("  old parent:  negative")
print("  catalyst:    positive")
print("  child:       positive")
print("  sideband:    negative")
