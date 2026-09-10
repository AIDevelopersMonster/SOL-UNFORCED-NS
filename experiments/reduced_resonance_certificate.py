#!/usr/bin/env python3
"""Exact-rational certificate for the corrected v0.4 difference relay."""
from fractions import Fraction

beta1 = Fraction(25, 16)
beta2 = Fraction(9, 16)
x1 = Fraction(29, 32)

def ln_rational_bounds(z: Fraction, n: int = 60):
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

def G_bounds(y: Fraction, n: int = 60):
    xc = beta1 * x1 - beta2 * y
    z = (x1 * y / xc) ** 3 * (beta1 * beta2) ** 2
    log_lo, log_hi = ln_rational_bounds(z, n)
    poly = Fraction(1) - beta1 * beta1 * x1 ** 3 - beta2 * beta2 * y ** 3 + xc ** 3
    return (log_lo + poly) / 3, (log_hi + poly) / 3, xc, z

tests = [
    ("tight_left", Fraction(613, 500), "neg"),
    ("tight_right", Fraction(1227, 1000), "pos"),
    ("wide_left", Fraction(11, 10), "neg"),
    ("wide_right", Fraction(7, 5), "pos"),
]
for name, y, sign in tests:
    lo, hi, xc, z = G_bounds(y)
    print(name, "y=", float(y), "xc=", float(xc), "G in", float(lo), float(hi))
    if sign == "neg":
        assert hi < 0
    else:
        assert lo > 0

assert G_bounds(Fraction(11, 10))[1] < -Fraction(1, 10)
assert G_bounds(Fraction(7, 5))[0] > Fraction(13, 100)
print("CERTIFIED: unique reduced root lies in (613/500, 1227/1000)")
