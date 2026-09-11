"""High-precision reduced certificate for the beta-(2,1) clock-reset microcascade.

This is a diagnostic/reproducibility script, not outward-rounded interval arithmetic.
It solves the three reduced equations used in
proofs/beta21_clock_reset_microcascade_candidate.md and prints the Jacobian,
concavity, and action ledger.
"""

import mpmath as mp

mp.mp.dps = 80


def I(beta, z):
    beta = mp.mpf(beta)
    return (
        mp.log(z * beta ** (mp.mpf(2) / 3))
        - beta**2 / 3 * (z**3 - beta ** (-2))
    )


def Ip(beta, z):
    beta = mp.mpf(beta)
    return 1 / z - beta**2 * z**2


def Ipp(beta, z):
    beta = mp.mpf(beta)
    return -1 / z**2 - 2 * beta**2 * z


def first_resonance(x, d, s):
    del s
    return I(2, x) + I(1, x + d) - I(1, x - d)


def reset_action_defect(x, d, s):
    # Four micro-interactions occur near s; H=3D-P then propagates to T=2d,
    # and the final H+D -> P_new interaction occurs at T.
    T = 2 * d
    return (
        3 * I(1, x + d + s)
        + 2 * I(1, x - d + s)
        - I(1, x - 3 * d + s)
        + I(1, x - 3 * d + T)
        + I(1, x - d + T)
        - I(2, x - 2 * d + T)
    )


def reset_stationarity(x, d, s):
    return (
        3 * Ip(1, x + d + s)
        + 2 * Ip(1, x - d + s)
        - Ip(1, x - 3 * d + s)
    )


x, d, s = mp.findroot(
    (first_resonance, reset_action_defect, reset_stationarity),
    (mp.mpf("0.786"), mp.mpf("0.0707"), mp.mpf("0.1412")),
    tol=mp.mpf("1e-60"),
    maxsteps=100,
)
T = 2 * d

print("x       =", mp.nstr(x, 60))
print("delta   =", mp.nstr(d, 60))
print("s_star  =", mp.nstr(s, 60))
print("T=2d    =", mp.nstr(T, 60))
print("T-s     =", mp.nstr(T - s, 60))
print("s/d     =", mp.nstr(s / d, 40))
print()
print("residuals")
print(mp.nstr(first_resonance(x, d, s), 20))
print(mp.nstr(reset_action_defect(x, d, s), 20))
print(mp.nstr(reset_stationarity(x, d, s), 20))

funcs = [first_resonance, reset_action_defect, reset_stationarity]
vars0 = [x, d, s]
J = mp.matrix(3)
for i, f in enumerate(funcs):
    for j in range(3):
        def one_var(z, i=i, j=j):
            args = list(vars0)
            args[j] = z
            return funcs[i](*args)
        J[i, j] = mp.diff(one_var, vars0[j])

print()
print("Jacobian =")
print(mp.nstr(J, 40))
print("det(J) =", mp.nstr(mp.det(J), 50))

rss = (
    3 * Ipp(1, x + d + s)
    + 2 * Ipp(1, x - d + s)
    - Ipp(1, x - 3 * d + s)
)
print("d2 defect / ds2 =", mp.nstr(rss, 40))

# Action ledger for the ordered character chain.
Ic = I(1, x + d + s)
Id = I(1, x - d + s)
A_Pboost = Ic + Id
A_E = Ic + 2 * Id
A_Q = 2 * Ic + 2 * Id
A_H = 3 * Ic + 2 * Id

slopes = {
    "P_boost": (2, x + s),
    "E=P+D": (3, x + s - d / 3),
    "Q=2D": (2, x - d + s),
    "H=3D-P": (1, x - 3 * d + s),
}
actions = {
    "P_boost": A_Pboost,
    "E=P+D": A_E,
    "Q=2D": A_Q,
    "H=3D-P": A_H,
}

print()
print("microcascade action ledger at s_star")
for name in ["P_boost", "E=P+D", "Q=2D", "H=3D-P"]:
    beta, z = slopes[name]
    nat = I(beta, z)
    act = actions[name]
    print(
        name,
        "beta=", beta,
        "slope=", mp.nstr(z, 20),
        "action=", mp.nstr(act, 20),
        "natural=", mp.nstr(nat, 20),
        "defect=", mp.nstr(act - nat, 20),
    )

H_T = x - d
D_T = x + d
Pnew_T = x
A_H_T = A_H + I(1, H_T) - I(1, x - 3 * d + s)
A_Pnew = A_H_T + I(1, D_T)
print()
print("final reset")
print("H(T) slope   =", mp.nstr(H_T, 20))
print("D(T) slope   =", mp.nstr(D_T, 20))
print("P_new slope  =", mp.nstr(Pnew_T, 20))
print("P_new action =", mp.nstr(A_Pnew, 30))
print("target action=", mp.nstr(I(2, x), 30))
print("difference   =", mp.nstr(A_Pnew - I(2, x), 30))
