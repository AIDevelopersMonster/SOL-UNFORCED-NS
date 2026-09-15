from mpmath import mp

mp.dps = 80
u = mp.mpf(4)
delta = mp.mpf('0.1755496058694293259805486194')
t2 = mp.mpf('0.218506242359214')
zD = 1 - 2*delta + t2
zP = 1 - delta + t2
AP = mp.mpf('-0.10519727146343909')
AD = mp.mpf('-0.02407863050407955')


def xturn(beta):
    beta = mp.mpf(beta)
    rad = (1 + u*u) * beta**(-mp.mpf(4)/3) - 1
    if rad < 0:
        return None
    return mp.sqrt(rad) / u


def env(beta, x):
    beta = mp.mpf(abs(beta))
    x = mp.mpf(abs(x))
    xt = xturn(beta)
    if xt is None:
        raise ValueError('no real turning point')
    return (
        mp.asinh(u*x) - mp.asinh(u*xt)
        - beta**2/(1+u*u)**(mp.mpf(3)/2)
        * (u*(x-xt) + u**3/mp.mpf(3)*(x**3-xt**3))
    )

print('zP =', mp.nstr(zP, 50))
print('zD =', mp.nstr(zD, 50))
print('AP =', mp.nstr(AP, 50))
print('AD =', mp.nstr(AD, 50))
print()

rows = []
for B in range(1, 9):
    xt = xturn(B)
    critical = []
    for a in range(-100, 101):
        b = B - 2*a
        xi = (2*a*zP + b*zD)/B
        if abs(xi) <= xt:
            S = abs(a)*AP + abs(b)*AD
            E = env(B, abs(xi))
            defect = S - E
            row = (B, a, b, xi, S, E, defect)
            critical.append(row)
            rows.append(row)
    print('B=', B, 'a-range=', critical[0][1], '..', critical[-1][1], 'count=', len(critical))
    for B0,a,b,xi,S,E,defect in critical:
        if defect > mp.mpf('1e-30'):
            print('  POS', 'a=', a, 'b=', b,
                  'xi=', mp.nstr(xi, 20),
                  'defect=', mp.nstr(defect, 30))

print()
print('total positive-beta naturally critical modes =', len(rows))
print('strictly positive defect modes:')
for B,a,b,xi,S,E,defect in rows:
    if defect > mp.mpf('1e-30'):
        print(B, a, b, mp.nstr(xi, 30), mp.nstr(S, 30), mp.nstr(E, 30), mp.nstr(defect, 30))

neg = sorted([r for r in rows if r[-1] < -mp.mpf('1e-20')], key=lambda r: -r[-1])
print()
print('closest negative defects:')
for B,a,b,xi,S,E,defect in neg[:10]:
    print(B, a, b, mp.nstr(xi, 20), mp.nstr(defect, 30))

print()
print('(1+u^2)^(3/4) =', mp.nstr((1+u*u)**(mp.mpf(3)/4), 30))
