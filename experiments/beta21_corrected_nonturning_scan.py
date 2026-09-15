"""Corrected finite-u non-turning beta-(2,1) scan.

IMPORTANT: the exact first-relay resonance is

    E_2,u(x) + E_1,u(x+delta) = E_1,u(x-delta),

not the plus-plus equation used in one retracted exploratory scan.

For n=1 strong-H renewal the script solves

    3 E_1,u(x-d+t) + E_1,u(x+d+t)
        = E_2,u(x-2d+t),

checks the exact phase reset at T=2d, and audits terminal source-action
complexity.  The crude lattice count is an upper bound.  The reachable count
iterates quadratic sums of distinct already-reached characters, thereby
removing the most obvious same-phase self-interaction overcount.  It still
does not replace a full polarization/reachability theorem.
"""

import math


def turning(beta, u):
    v = (1.0 + u*u) * beta ** (-4.0/3.0) - 1.0
    if v < 0.0:
        return None
    return math.sqrt(v) / u


def env(beta, u, x):
    xb = turning(beta, u)
    x = abs(x)
    return (
        math.asinh(u*x) - math.asinh(u*xb)
        - beta*beta/(1.0+u*u)**1.5
        * (u*(x-xb) + u**3/3.0*(x**3-xb**3))
    )


def bisect(f, a, b, n=100):
    fa = f(a)
    fb = f(b)
    if fa*fb > 0.0:
        raise RuntimeError((a, b, fa, fb))
    for _ in range(n):
        m = 0.5*(a+b)
        fm = f(m)
        if fa*fm <= 0.0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return 0.5*(a+b)


def first_sign_change(f, a, b, steps=4000):
    x0 = a
    f0 = f(x0)
    for j in range(1, steps+1):
        x1 = a + (b-a)*j/steps
        f1 = f(x1)
        if f0*f1 < 0.0:
            return bisect(f, x0, x1)
        x0, f0 = x1, f1
    raise RuntimeError("no sign change")


def solve_x(u, d):
    f = lambda x: env(2,u,x) + env(1,u,x+d) - env(1,u,x-d)
    return first_sign_change(f, max(0.45,d+1e-4), 1.35-d)


def strong_h_root(u, x, d):
    T = 2.0*d
    f = lambda t: (
        3.0*env(1,u,x-d+t)
        + env(1,u,x+d+t)
        - env(2,u,x-2.0*d+t)
    )
    return first_sign_change(f, 0.0, T)


def canonical_promoted_count(AC, AD, AP):
    a = -AD
    c = -AC
    p = -AP
    M = int(p/a) + 2
    N = int(p/c) + 2
    rows = []
    for m in range(-M,M+1):
        for n in range(-N,N+1):
            if m == 0 and n == 0:
                continue
            B = m+n
            if B < 0 or (B == 0 and m < 0):
                continue
            leaf = abs(m)*AD + abs(n)*AC
            if leaf >= AP - 1e-12:
                rows.append((m,n,B,leaf))
    return rows


def reachable_promoted(AC, AD, AP, bound=30, maxiter=40):
    best = {(1,0):AD,(-1,0):AD,(0,1):AC,(0,-1):AC}
    for _ in range(maxiter):
        changed = False
        items = list(best.items())
        for a,Aa in items:
            for b,Ab in items:
                if a == b:
                    # Same signed character self-interaction vanishes at principal order.
                    continue
                child = (a[0]+b[0], a[1]+b[1])
                if child == (0,0):
                    continue
                if abs(child[0]) > bound or abs(child[1]) > bound:
                    continue
                act = Aa+Ab
                if act < AP-1e-12:
                    continue
                if act > best.get(child,-1e100)+1e-12:
                    best[child] = act
                    changed = True
        if not changed:
            break
    out = []
    for (m,n),act in best.items():
        B=m+n
        if B > 0 or (B == 0 and m > 0):
            out.append((m,n,B,act))
    return sorted(out, key=lambda r:(r[2],r[1],r[0]))


# Corrected compact candidate used by the companion theorem note.
u = 2.5
d = 0.1375
x = solve_x(u,d)
T = 2.0*d
t = strong_h_root(u,x,d)

AP = env(2,u,x)
AC0 = env(1,u,x+d)
AD0 = env(1,u,x-d)
AC_T = env(1,u,x+3*d)
AD_T = env(1,u,x+d)

print("corrected non-turning candidate")
print("u       =", u)
print("delta   =", d)
print("x       = %.15f" % x)
print("T       = %.15f" % T)
print("t_renew = %.15f" % t)
print("T-t     = %.15f" % (T-t))
print("Pnew generation slope = %.15f" % (x-2*d+t))
print()
print("first relay residual = %.16e" % (AP+AC0-AD0))
print("strong-H residual    = %.16e" % (
    3*env(1,u,x-d+t)+env(1,u,x+d+t)-env(2,u,x-2*d+t)
))
print()
print("A_P target  = %+.15e" % AP)
print("A_C input   = %+.15e" % AC0)
print("A_D input   = %+.15e" % AD0)
print("A_C boundary= %+.15e" % AC_T)
print("A_D boundary= %+.15e" % AD_T)

crude = canonical_promoted_count(AC_T,AD_T,AP)
reach = reachable_promoted(AC_T,AD_T,AP)
print()
print("crude promoted conjugacy classes =", len(crude))
print("reachable after same-phase-self-zero filter =", len(reach))
print("reachable rows (mD+nC, beta=m+n):")
for row in reach:
    print(row)
