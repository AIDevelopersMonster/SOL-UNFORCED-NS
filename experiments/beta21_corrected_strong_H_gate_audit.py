"""High-precision diagnostic audit for the corrected non-turning strong-H gate.

Working point:
    u = 2.5
    delta = 0.1375

The exact first-relay resonance is
    E_2(x) + E_1(x+delta) = E_1(x-delta).

The strong-H section t_* solves
    3 E_1(x-delta+t) + E_1(x+delta+t)
        = E_2(x-2 delta+t).

This script prints:
- the corrected root x and t_*;
- the ten reachable promoted conjugacy classes from C,D at t_*;
- the nearest omitted source-action gap;
- frozen full-symbol rates of the nine controlled states;
- the principal selected-tree edge coefficients;
- conservative sampled margins on |t-t_*| <= 1e-3.

It is a reproducibility/diagnostic certificate, not outward-rounded interval arithmetic.
"""

import math


U = 2.5
DELTA = 0.1375
WIDTH = 1.0e-3


def turning(beta, u):
    v = (1.0 + u*u) * beta ** (-4.0/3.0) - 1.0
    if v < 0.0:
        return None
    return math.sqrt(v) / u


def primitive(beta, u, z):
    z = abs(z)
    return (
        math.asinh(u*z)
        - beta*beta/(1.0+u*u)**1.5
        * (u*z + u**3*z**3/3.0)
    )


def env(beta, u, z):
    xb = turning(beta, u)
    if xb is None:
        raise ValueError("env normalization requires a real turning point")
    return primitive(beta, u, z) - primitive(beta, u, xb)


def bisect(f, a, b, n=120):
    fa = f(a)
    fb = f(b)
    if fa*fb > 0:
        raise RuntimeError((a,b,fa,fb))
    for _ in range(n):
        m = 0.5*(a+b)
        fm = f(m)
        if fa*fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return 0.5*(a+b)


def first_sign_change(f, a, b, steps=10000):
    x0 = a
    f0 = f(x0)
    for j in range(1, steps+1):
        x1 = a + (b-a)*j/steps
        f1 = f(x1)
        if f0*f1 < 0:
            return bisect(f, x0, x1)
        x0, f0 = x1, f1
    raise RuntimeError("no sign change")


def solve_x(u, d):
    f = lambda x: env(2,u,x) + env(1,u,x+d) - env(1,u,x-d)
    return first_sign_change(f, max(0.45,d+1e-6), 1.35-d)


def solve_tstar(u, x, d):
    T = 2*d
    f = lambda t: (
        3*env(1,u,x-d+t)
        + env(1,u,x+d+t)
        - env(2,u,x-2*d+t)
    )
    return first_sign_change(f, 0.0, T)


def gamma(beta, u, z):
    return (
        1.0/math.sqrt(1.0+u*u*z*z)
        - beta*beta*(1.0+u*u*z*z)/(1.0+u*u)**1.5
    )


def sum_coeff(b1,z1,b2,z2,u):
    s1 = u*z1
    s2 = u*z2
    bt = b1+b2
    st = (b1*s1+b2*s2)/bt
    bracket = (
        (b1-b2 + st*(b1*s1-b2*s2))/(1.0+st*st)
        + (b1*math.sqrt(1.0+s1*s1)-b2*math.sqrt(1.0+s2*s2))
          / math.sqrt(1.0+st*st)
    )
    return 0.5*(s1-s2)*bracket


def beta_zero_root_data(zD,zC,u):
    sD = u*zD
    sC = u*zC
    m = sD-sC
    S = sD+sC
    R = math.sqrt(1.0+sD*sD)+math.sqrt(1.0+sC*sC)
    # c0=-1 normalization; only nonvanishing/margins matter.
    bM = (0.0,-S,-R)
    root_norm = abs(m)*math.sqrt(S*S+R*R)
    return m,bM,root_norm


def wave_plus_root_coeff(beta,z,m,bM,u):
    s = u*z
    g = (1.0,-s,-math.sqrt(1.0+s*s))
    # Q=(g . m e_r)bM + (bM . beta(s e_r+K))g
    q = [m*bM[j] + beta*bM[1]*g[j] for j in range(3)]
    st = s + m/beta
    ah = (q[0]-st*q[1])/(1.0+st*st)
    an = q[2]/(-math.sqrt(1.0+st*st))
    return 0.5*(ah+an)


def canonical(k):
    m,n = k
    beta = m+n
    if beta < 0 or (beta == 0 and m < 0):
        return (-m,-n)
    return k


def reachable_promoted(AC,AD,target,bound=10,maxiter=30,extra=0.10):
    best = {(1,0):AD,(-1,0):AD,(0,1):AC,(0,-1):AC}
    parent = {}
    floor = target-extra
    for _ in range(maxiter):
        changed = False
        items = list(best.items())
        for a,Aa in items:
            for b,Ab in items:
                if a == b:
                    # identical signed-character principal self-interaction vanishes
                    continue
                child = (a[0]+b[0],a[1]+b[1])
                if child == (0,0):
                    continue
                if abs(child[0]) > bound or abs(child[1]) > bound:
                    continue
                act = Aa+Ab
                if act < floor:
                    continue
                if act > best.get(child,-1e100)+1e-14:
                    best[child] = act
                    parent[child] = (a,b)
                    changed = True
        if not changed:
            break
    out = []
    for k,act in best.items():
        if canonical(k) != k:
            continue
        out.append((k,act,act-target,parent.get(k)))
    return sorted(out,key=lambda r:r[2],reverse=True)


x = solve_x(U,DELTA)
T = 2*DELTA
t = solve_tstar(U,x,DELTA)

print("working point")
print("u       = %.16f" % U)
print("delta   = %.16f" % DELTA)
print("x       = %.16f" % x)
print("t_*     = %.16f" % t)
print("T       = %.16f" % T)
print("T-t_*   = %.16f" % (T-t))
print()

AC = env(1,U,x+DELTA+t)
AD = env(1,U,x-DELTA+t)
AT = AC+3*AD
print("actions at t_*")
print("A_C              = %+.16e" % AC)
print("A_D              = %+.16e" % AD)
print("A_C+3 A_D target = %+.16e" % AT)
print("strong-H residual= %+.16e" % (AT-env(2,U,x-2*DELTA+t)))
print()

rows = reachable_promoted(AC,AD,AT)
prom = [r for r in rows if r[2] >= -1e-12]
omit = [r for r in rows if r[2] < -1e-12]
print("promoted conjugacy classes =",len(prom))
for r in prom:
    print(r)
print("nearest omitted =",omit[0])
print()

zD = x-DELTA+t
zC = x+DELTA+t
states = {
    "C":(0,1),
    "M":(1,-1),
    "P":(1,1),
    "H":(2,-1),
    "2D+C":(2,1),
    "D+2C":(1,2),
    "2C-D":(-1,2),
    "Pnew":(3,-1),
    "3D+C":(3,1),
}


def state_z(m,n,zD,zC):
    b = m+n
    return (m*zD+n*zC)/b


def state_rate(m,n,zD,zC):
    b = m+n
    if b == 0:
        nr = U*(m*zD+n*zC)
        return -(nr*nr)/(1.0+U*U)**1.5
    return gamma(b,U,state_z(m,n,zD,zC))

rates = {}
print("nine controlled full-symbol rates")
for name,(m,n) in states.items():
    rates[name] = state_rate(m,n,zD,zC)
    print("%-8s beta=%2d rate=%+.16e" % (name,m+n,rates[name]))

gap = min(abs(rates[a]-rates[b]) for i,a in enumerate(rates) for b in list(rates)[i+1:])
print("spectral gap = %.16e" % gap)
print()

zP = 0.5*(zD+zC)
zH = 2*zD-zC
z2DpC = (2*zD+zC)/3.0
mroot,bM,rootnorm = beta_zero_root_data(zD,zC,U)
edge = {
    "C+D->P":sum_coeff(1,zC,1,zD,U),
    "D-C->M(root norm)":rootnorm,
    "M+D->H":wave_plus_root_coeff(1,zD,mroot,bM,U),
    "H+D->Pnew":sum_coeff(1,zH,1,zD,U),
    "P+D->2D+C":sum_coeff(2,zP,1,zD,U),
    "(2D+C)+D->3D+C":sum_coeff(3,z2DpC,1,zD,U),
    "P+C->D+2C":sum_coeff(2,zP,1,zC,U),
    "C-M->2C-D":wave_plus_root_coeff(1,zC,-mroot,bM,U),
}
print("selected leading edge coefficients")
for name,val in edge.items():
    print("%-25s %+.16e" % (name,val))
print()

min_spec = 1e100
min_edge = 1e100
min_root = 1e100
min_omit = 1e100
for j in range(1001):
    ss = t-WIDTH + 2*WIDTH*j/1000.0
    zd = x-DELTA+ss
    zc = x+DELTA+ss
    ac = env(1,U,zc)
    ad = env(1,U,zd)
    target = ac+3*ad

    # exact reachable nearest omitted action certificate
    rr = reachable_promoted(ac,ad,target)
    oo = [r for r in rr if r[2] < -1e-12]
    min_omit = min(min_omit,-oo[0][2])

    rrates = [state_rate(m,n,zd,zc) for m,n in states.values()]
    for a in range(len(rrates)):
        for b in range(a+1,len(rrates)):
            min_spec = min(min_spec,abs(rrates[a]-rrates[b]))

    zp = 0.5*(zd+zc)
    zh = 2*zd-zc
    z2 = (2*zd+zc)/3.0
    mr,bmr,rnorm = beta_zero_root_data(zd,zc,U)
    vals = [
        sum_coeff(1,zc,1,zd,U),
        wave_plus_root_coeff(1,zd,mr,bmr,U),
        sum_coeff(1,zh,1,zd,U),
        sum_coeff(2,zp,1,zd,U),
        sum_coeff(3,z2,1,zd,U),
        sum_coeff(2,zp,1,zc,U),
        wave_plus_root_coeff(1,zc,-mr,bmr,U),
    ]
    min_edge = min(min_edge,min(abs(v) for v in vals))
    min_root = min(min_root,rnorm)

print("sampled margins on |t-t_*|<=1e-3")
print("min omitted action gap = %.16e" % min_omit)
print("min spectral gap       = %.16e" % min_spec)
print("min wave-edge |kappa|  = %.16e" % min_edge)
print("min root projection    = %.16e" % min_root)
