from mpmath import mp

mp.dps = 80
u = mp.mpf(4)


def xturn(beta):
    beta = mp.mpf(beta)
    z = (1 + u*u) * beta**(-mp.mpf(4)/3) - 1
    if z < 0:
        return None
    return mp.sqrt(z) / u


def envelope(beta, x):
    beta = mp.mpf(beta)
    x = mp.mpf(x)
    xt = xturn(beta)
    if xt is None:
        raise ValueError("no real turning point")
    return (
        mp.asinh(u*x) - mp.asinh(u*xt)
        - beta**2 / (1 + u*u)**(mp.mpf(3)/2)
        * (u*(x-xt) + u**3/mp.mpf(3)*(x**3-xt**3))
    )


def resonance(delta):
    return envelope(2, 1-delta) - envelope(1, 1-2*delta)


delta = mp.findroot(resonance, (mp.mpf("0.17"), mp.mpf("0.18")))
x = 1-delta
A = envelope(1, 1-2*delta)

print("delta =", mp.nstr(delta, 60))
print("x     =", mp.nstr(x, 60))
print("A_D   =", mp.nstr(A, 60))
print()

# K_{m,n}=m D+n C, B=m+n>0.  At the first late gate section
# z_D=1-2 delta, z_C=1, so the B-normalized reduced slope is
# xi_{B,m}=1-2m delta/B.
# C is at its turning point and has action 0.  Thus the largest
# leaf-product action of any genealogy carrying K_{m,n} is |m| A_D;
# extra cancelling D pairs only make the action more negative.

rows = []
for B in range(1, 9):
    xt = xturn(B)
    critical = []
    for m in range(-100, 101):
        n = B-m
        xi = 1 - 2*mp.mpf(m)*delta/mp.mpf(B)
        if abs(xi) <= xt:
            defect = abs(m)*A - envelope(B, abs(xi))
            critical.append((m, n, xi, defect))
            rows.append((B, m, n, xi, defect))
    print("B=", B, "turn=", mp.nstr(xt, 18),
          "m-range=", critical[0][0], "..", critical[-1][0],
          "count=", len(critical))
    for m,n,xi,defect in critical:
        if defect > 0:
            print("  POS", m, n, "xi=", mp.nstr(xi, 18),
                  "defect=", mp.nstr(defect, 24))
    neg = [r[3] for r in critical if r[3] < 0]
    if neg:
        print("  max negative defect =", mp.nstr(max(neg), 24))

print()
print("positive-action critical modes:")
for B,m,n,xi,defect in rows:
    if defect > 0:
        print(B, m, n, mp.nstr(xi, 20), mp.nstr(defect, 30))

# Useful margins quoted by the proof note.
print()
for B,m in [(1,2),(1,3),(1,4),(2,6)]:
    n = B-m
    xi = 1 - 2*mp.mpf(m)*delta/mp.mpf(B)
    defect = abs(m)*A - envelope(B, abs(xi))
    print((B,m,n), "xi=", mp.nstr(xi, 30),
          "defect=", mp.nstr(defect, 40))

# Principal rate threshold.  B>=9 has no real turning point at u=4,
# so every such mode is strictly forward-decaying at principal level.
print()
print("(1+u^2)^(3/4) =", mp.nstr((1+u*u)**(mp.mpf(3)/4), 30))
