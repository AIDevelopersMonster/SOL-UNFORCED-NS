#!/usr/bin/env python3
"""Numerical diagnostic for the proved finite-u envelope persistence theorem.

The proof itself is in proofs/finite_u_relay_persistence.md.
This script is only a high-precision sanity check; it is not the rigorous certificate.
"""

import mpmath as mp

mp.mp.dps = 60

rho = mp.mpf(17) / 12
beta1 = mp.mpf(41) / 48
beta2 = mp.mpf(9) / 16
x1 = mp.mpf(71) / 48


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


def xc(y):
    return (beta1*x1 - beta2*y) / rho


def G(u, y):
    return E(beta1, u, x1) + E(beta2, u, y) - E(1, u, xc(y))


def solve(u):
    return mp.findroot(lambda y: G(u, y), (mp.mpf('0.90'), mp.mpf('0.97')))


print('SOL-UNFORCED-NS finite-u relay persistence check')
print('------------------------------------------------')
for u in [20, 25, 50, 100, 1000]:
    y = solve(mp.mpf(u))
    print(
        f'u={u:4d}  y={mp.nstr(y, 18)}  '
        f'xc={mp.nstr(xc(y), 18)}  '
        f'G={mp.nstr(G(mp.mpf(u), y), 5)}'
    )

print('\nThe rigorous theorem proves existence and uniqueness for every u >= 20.')
