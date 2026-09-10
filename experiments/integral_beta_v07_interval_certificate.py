#!/usr/bin/env python3
"""Interval-arithmetic certificate for the v0.7 rational half-step relay.

This script certifies only the scalar exact-envelope resonance signs used in
proofs/integral_beta_v07_global_action_filter.md.  It is not a PDE proof.
"""

import mpmath as mp

iv = mp.iv
iv.dps = 80


def asinh_iv(z):
    return iv.log(z + iv.sqrt(1 + z * z))


def E(beta, u, x):
    beta = iv.mpf(beta)
    u = iv.mpf(u)
    x = iv.mpf(x)
    xt = iv.sqrt((1 + u * u) * beta ** (-iv.mpf(4) / 3) - 1) / u
    return (
        asinh_iv(u * x)
        - asinh_iv(u * xt)
        - beta ** 2 / (1 + u * u) ** (iv.mpf(3) / 2)
        * (u * (x - xt) + u ** 3 * (x ** 3 - xt ** 3) / 3)
    )


x1 = iv.mpf(29) / 40
y = iv.mpf(1073) / 1440
xc = iv.mpf(203) / 288


def R(u):
    return E(2, u, x1) + E(1, u, y) - E(1, u, xc)


print("v0.7 exact-envelope resonance sign certificate")
print("R(20)  =", R(20))
print("R(100) =", R(100))
print()
print("Expected certified signs: R(20) < 0 < R(100).")

# High-precision non-rigorous locator for convenience.
mp.mp.dps = 80


def xturn(beta, u):
    return mp.sqrt((1 + u * u) * beta ** (-mp.mpf(4) / 3) - 1) / u


def Emp(beta, u, x):
    xt = xturn(beta, u)
    return (
        mp.asinh(u * x)
        - mp.asinh(u * xt)
        - beta ** 2 / (1 + u * u) ** (mp.mpf(3) / 2)
        * (u * (x - xt) + u ** 3 * (x ** 3 - xt ** 3) / 3)
    )


x1m = mp.mpf(29) / 40
ym = mp.mpf(1073) / 1440
xcm = mp.mpf(203) / 288


def Rmp(u):
    return Emp(2, u, x1m) + Emp(1, u, ym) - Emp(1, u, xcm)


u_root = mp.findroot(Rmp, (49, 50))
print("Numerical locator only: u_dagger =", mp.nstr(u_root, 30))
print("Residual =", mp.nstr(Rmp(u_root), 8))
