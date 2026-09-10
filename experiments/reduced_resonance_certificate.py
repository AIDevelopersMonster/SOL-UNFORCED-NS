#!/usr/bin/env python3
"""Rigorous interval certificate for the reduced beta-relay resonance.

Uses exact rational arithmetic for all algebraic terms and an atanh-series
remainder bound for log(Z). This certifies a sign change for the reduced
resonance function G on a rational interval.
"""

from fractions import Fraction

rho = Fraction(17, 12)
beta1 = Fraction(41, 48)
beta2 = Fraction(9, 16)
x1 = Fraction(71, 48)
y_minus = Fraction(469, 500)
y_plus = Fraction(939, 1000)


def ln_rational_bounds(z: Fraction, n: int = 30):
    if z <= 0:
        raise ValueError("z must be positive")
    if z < 1:
        lo, hi = ln_rational_bounds(1 / z, n)
        return -hi, -lo
    w = (z - 1) / (z + 1)
    s = Fraction(0, 1)
    wpow = w
    for k in range(n + 1):
        s += wpow / Fraction(2 * k + 1, 1)
        wpow *= w * w
    rem = wpow / Fraction(2 * n + 3, 1) / (1 - w * w)
    return 2 * s, 2 * (s + rem)


def G_bounds(y: Fraction, n: int = 30):
    xc = (beta1 * x1 - beta2 * y) / rho
    z = (x1 * y / xc) ** 3 * (beta1 * beta2) ** 2
    log_lo, log_hi = ln_rational_bounds(z, n)
    poly = Fraction(1, 1) - beta1 * beta1 * x1 ** 3 - beta2 * beta2 * y ** 3 + xc ** 3
    # 3G = log(z) + poly
    return (log_lo + poly) / 3, (log_hi + poly) / 3, xc, z


for name, y in [("y_minus", y_minus), ("y_plus", y_plus)]:
    lo, hi, xc, z = G_bounds(y)
    print(name)
    print("  y       =", y, float(y))
    print("  xc      =", xc, float(xc))
    print("  Z       =", z, float(z))
    print("  G lower =", float(lo))
    print("  G upper =", float(hi))
    print("  sign    =", "negative" if hi < 0 else "positive" if lo > 0 else "undetermined")

assert G_bounds(y_minus)[1] < 0
assert G_bounds(y_plus)[0] > 0
print("CERTIFIED: G(y_minus) < 0 < G(y_plus)")
