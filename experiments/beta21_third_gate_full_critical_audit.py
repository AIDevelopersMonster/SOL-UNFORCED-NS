"""Exact-envelope audit for the third beta-(2,1) active gate.

Working timing:
    t1 = 0.213506242359214
    t2 = t1 + 0.005
    t3 = t2 + 0.0005

The second active gate prescribes P=M=X2=...=X10=0 at its exit and a
nonzero E output.  At t3 the transported E is already slightly below the
fresh C,D leaf bound, so the maximal incoming action bank reduces again to
C,D.  We enumerate the full naturally-critical positive-beta lattice, record
the six positive-defect root modes, and compare the promoted Q=2D action to
its natural beta-two envelope.

This is a reproducibility calculation, not outward-rounded interval
arithmetic.
"""

import math

U = 4.0
DELTA = 0.1755496058694293259805486194
T1 = 0.213506242359214
T2 = T1 + 0.005
T3 = T2 + 0.0005


def turning(beta):
    y = (1.0 + U * U) * beta ** (-4.0 / 3.0) - 1.0
    if y < 0.0:
        return None
    return math.sqrt(y) / U


def env(beta, x):
    xb = turning(beta)
    return (
        math.asinh(U * x)
        - math.asinh(U * xb)
        - beta * beta / (1.0 + U * U) ** 1.5
        * (U * (x - xb) + U**3 / 3.0 * (x**3 - xb**3))
    )


def zc(t):
    return 1.0 + t


def zd(t):
    return 1.0 - 2.0 * DELTA + t


def ze(t):
    return 1.0 - 4.0 * DELTA / 3.0 + t


def character_xi(B, m, t):
    n = B - m
    return (m * zd(t) + n * zc(t)) / B


def defect(B, m, t):
    n = B - m
    ac = env(1, zc(t))
    ad = env(1, zd(t))
    xi = character_xi(B, m, t)
    leaf = abs(m) * ad + abs(n) * ac
    return leaf - env(B, abs(xi))


AC2 = env(1, zc(T2))
AD2 = env(1, zd(T2))
AE2 = AC2 + 2.0 * AD2
AE3_TRANSPORTED = AE2 + env(3, ze(T3)) - env(3, ze(T2))

AC3 = env(1, zc(T3))
AD3 = env(1, zd(T3))
AE3_FRESH = AC3 + 2.0 * AD3
AP3_FRESH = AC3 + AD3
AM3 = AP3_FRESH

# The intended E-C -> Q genealogy costs one additional C leaf.  Equivalently
# the competing root-side path X2+C -> Q has the same absolute-leaf action.
AQ3 = 2.0 * AC3 + 2.0 * AD3
AQ3_FROM_TRANSPORTED_E = AE3_TRANSPORTED + AC3
AQ3_NATURAL = env(2, zd(T3))

print("third-gate timing")
print(f"t2 = {T2:.15f}")
print(f"t3 = {T3:.15f}")
print()
print("incoming actions")
print(f"A_C                = {AC3:+.15e}")
print(f"A_D                = {AD3:+.15e}")
print(f"A_P fresh          = {AP3_FRESH:+.15e}")
print(f"A_M                = {AM3:+.15e}")
print(f"A_E transported    = {AE3_TRANSPORTED:+.15e}")
print(f"A_E fresh leaf     = {AE3_FRESH:+.15e}")
print(f"E transported-fresh= {AE3_TRANSPORTED-AE3_FRESH:+.15e}")
print()
print("promoted Q")
print(f"A_Q fresh genealogy       = {AQ3:+.15e}")
print(f"A_Q from transported E    = {AQ3_FROM_TRANSPORTED_E:+.15e}")
print(f"E-route deficit vs fresh  = {AQ3_FROM_TRANSPORTED_E-AQ3:+.15e}")
print(f"natural E_2(Q)            = {AQ3_NATURAL:+.15e}")
print(f"promoted Q defect         = {AQ3-AQ3_NATURAL:+.15e}")
print()

critical = []
for B in range(1, 9):
    xb = turning(B)
    rows = []
    for m in range(-32, 65):
        xi = character_xi(B, m, T3)
        if abs(xi) <= xb + 1.0e-13:
            n = B - m
            D = defect(B, m, T3)
            row = (B, m, n, xi, D)
            rows.append(row)
            critical.append(row)
    if rows:
        print(
            f"B={B}: m={rows[0][1]}..{rows[-1][1]}  "
            f"count={len(rows)}"
        )

positive = [r for r in critical if r[4] > 0.0]
negative = sorted((r for r in critical if r[4] < 0.0), key=lambda r: -r[4])

print()
print(f"total naturally critical = {len(critical)}")
print("positive-defect modes")
for B, m, n, xi, D in positive:
    print(
        f"(B,m,n)=({B},{m},{n})  xi={xi:+.12f}  "
        f"Delta={D:+.15e}"
    )

print()
print("closest negative modes")
for B, m, n, xi, D in negative[:6]:
    print(
        f"(B,m,n)=({B},{m},{n})  xi={xi:+.12f}  "
        f"Delta={D:+.15e}"
    )

# A short forward width preserving the six-mode sign classification.
W3 = 1.0e-4
print()
print(f"width check w3={W3}")
print(
    "weak positive (3,10,-7): ",
    f"{defect(3,10,T3+W3):+.15e}",
)
print(
    "closest negative (2,8,-6): ",
    f"{defect(2,8,T3+W3):+.15e}",
)
