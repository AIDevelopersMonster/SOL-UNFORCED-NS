#!/usr/bin/env python3
"""High-precision diagnostic for the v0.5 integral-beta relay candidate.

This script is numerical support only. The reduced sign change is certified
separately in proofs/integral_beta_v05_reduced_resonance.md.
"""

import mpmath as mp

mp.mp.dps = 60

beta1 = mp.mpf(2)
beta2 = mp.mpf(1)
x1 = mp.mpf(4) / 5


def I(beta, x):
    return mp.log(x) + mp.mpf(2) / 3 * mp.log(beta) - beta**2 * x**3 / 3 + mp.mpf(1) / 3


def F(beta, x):
    return 1 / x - beta**2 * x**2


def xc(y):
    return 2 * x1 - y


def G(y):
    return I(beta1, x1) + I(beta2, y) - I(1, xc(y))


def xturn(beta, u):
    return mp.sqrt((1 + u*u) * beta**(-mp.mpf(4)/3) - 1) / u


def E(beta, u, x):
    xt = xturn(beta, u)
    return (
        mp.asinh(u*x)
        - mp.asinh(u*xt)
        - beta**2 / (1 + u*u)**(mp.mpf(3)/2)
        * (u*(x-xt) + u**3 * (x**3-xt**3) / 3)
    )


def Gu(u, y):
    return E(beta1, u, x1) + E(beta2, u, y) - E(1, u, xc(y))


y0 = mp.findroot(G, (mp.mpf('0.89'), mp.mpf('0.891')))
print('v0.5 reduced root')
print('y0 =', mp.nstr(y0, 30))
print('xc =', mp.nstr(xc(y0), 30))
print('F2(x1) =', mp.nstr(F(2, x1), 20))
print('F1(y0) =', mp.nstr(F(1, y0), 20))
print('F1(xc) =', mp.nstr(F(1, xc(y0)), 20))
print('sum beta = 3')
print('sum x =', mp.nstr((2*x1+y0)/3, 20))
print('sum F =', mp.nstr(F(3, (2*x1+y0)/3), 20))
print('feedback T(1,-2) =', beta1 - 2*beta2)
print()
print('finite-u diagnostics')
for u in [20, 30, 50, 100, 1000]:
    u = mp.mpf(u)
    y = mp.findroot(lambda yy: Gu(u, yy), (mp.mpf('0.85'), mp.mpf('0.95')))
    print('u=', int(u), ' y=', mp.nstr(y, 24), ' xc=', mp.nstr(xc(y), 24), ' residual=', mp.nstr(Gu(u,y), 5))
