"""High-precision diagnostic for causal unfolding of the beta-(2,1) reset microcascade.

The simultaneous late collision point is unfolded into four ordered event times
    t1=s, t2=s+eta, t3=s+2 eta, t4=s+3 eta
with reset face T=2 delta.

For each eta the script solves:
  1. first relay resonance,
  2. exact final parent-action renewal,
  3. stationarity of the reset action with respect to the common shift s.

This is a reproducibility calculation, not outward-rounded interval arithmetic.
"""

import mpmath as mp

mp.mp.dps = 80


def I(beta, z):
    beta = mp.mpf(beta)
    return (
        mp.log(z * beta ** (mp.mpf(2) / 3))
        - beta**2 / 3 * (z**3 - beta ** (-2))
    )


def first_resonance(x, d):
    return I(2, x) + I(1, x + d) - I(1, x - d)


def final_action(x, d, s, eta):
    t1 = s
    t2 = s + eta
    t3 = s + 2 * eta
    t4 = s + 3 * eta
    T = 2 * d

    C = lambda t: I(1, x + d + t)
    D = lambda t: I(1, x - d + t)

    # C + D -> P at t1
    P1 = C(t1) + D(t1)
    # propagate P to t2
    P2 = P1 + I(2, x + t2) - I(2, x + t1)

    # P + D -> E at t2
    E2 = P2 + D(t2)
    # propagate E to t3
    E3 = E2 + I(3, x - d / 3 + t3) - I(3, x - d / 3 + t2)

    # E - C -> Q at t3
    Q3 = E3 + C(t3)
    # propagate Q to t4
    Q4 = Q3 + I(2, x - d + t4) - I(2, x - d + t3)

    # Q - C -> H at t4
    H4 = Q4 + C(t4)
    # propagate H to reset face T
    HT = H4 + I(1, x - 3 * d + T) - I(1, x - 3 * d + t4)

    # H + D -> P_new at T
    return HT + D(T)


def reset_defect(x, d, s, eta):
    return final_action(x, d, s, eta) - I(2, x)


def stationarity(x, d, s, eta):
    return mp.diff(lambda ss: reset_defect(x, d, ss, eta), s)


def solve_eta(eta, seed):
    x0, d0, s0 = seed
    return mp.findroot(
        lambda x, d, s: (
            first_resonance(x, d),
            reset_defect(x, d, s, eta),
            stationarity(x, d, s, eta),
        ),
        (x0, d0, s0),
        tol=mp.mpf("1e-60"),
        maxsteps=100,
    )


seed = (
    mp.mpf("0.7859855569295219140"),
    mp.mpf("0.07069967306663885738"),
    mp.mpf("0.14119460888766346057"),
)

for eta in map(mp.mpf, ["0", "1e-6", "5e-6", "1e-5", "2e-5", "4e-5"]):
    x, d, s = solve_eta(eta, seed)
    seed = (x, d, s)
    T = 2 * d
    margin = T - (s + 3 * eta)

    funcs = [
        lambda X, D, S: first_resonance(X, D),
        lambda X, D, S: reset_defect(X, D, S, eta),
        lambda X, D, S: stationarity(X, D, S, eta),
    ]
    vals = [x, d, s]
    J = mp.matrix(3)
    for i, f in enumerate(funcs):
        for j in range(3):
            def one_var(z, i=i, j=j):
                args = list(vals)
                args[j] = z
                return funcs[i](*args)
            J[i, j] = mp.diff(one_var, vals[j])

    print("eta     =", mp.nstr(eta, 20))
    print("x       =", mp.nstr(x, 30))
    print("delta   =", mp.nstr(d, 30))
    print("s       =", mp.nstr(s, 30))
    print("T       =", mp.nstr(T, 30))
    print("T-t4    =", mp.nstr(margin, 30))
    print("det J   =", mp.nstr(mp.det(J), 30))
    print("res     =", mp.nstr(reset_defect(x, d, s, eta), 8))
    print()
