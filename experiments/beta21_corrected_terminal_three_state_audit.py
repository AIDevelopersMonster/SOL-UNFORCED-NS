"""Diagnostic audit for the corrected post-strong-H terminal gate.

After the exact strong-H gate has set old C=0, the only designated leading
bank is (P_new,D).  This script verifies that the only new source-promoted
characters above the renewed beta-two target are

    H = P_new-D,
    M = P_new-2D,

while P_new+D and regenerated C=3D-P_new are action-subcritical.  It also
prints principal polarization margins for P_new-D -> H and H-D -> M.

This is a reproducibility certificate, not outward-rounded interval arithmetic.
"""

import math

U = 2.5
DELTA = 0.1375
X = 0.77794450260672482712680064619405
TSTAR = 0.22512911698286797975123849107983
T = 2*DELTA
TERM = TSTAR+0.005
WIDTH = 1.0e-3


def turning(beta):
    return math.sqrt((1+U*U)*beta**(-4.0/3.0)-1.0)/U


def primitive(beta,z):
    z=abs(z)
    return (
        math.asinh(U*z)
        - beta*beta/(1+U*U)**1.5
        * (U*z+U**3*z**3/3.0)
    )


def env(beta,z):
    xb=turning(beta)
    return primitive(beta,z)-primitive(beta,xb)


def zD(s): return X-DELTA+s

def zP(s): return X-2*DELTA+s

def AD(s): return env(1,zD(s))

def AP(s): return env(2,zP(s))


def zchar(m,n,s):
    # character m D + n P_new, beta=m+2n
    b=m+2*n
    return (m*zD(s)+2*n*zP(s))/b


def propagated_action(m,n,s):
    source=abs(m)*AD(s)+abs(n)*AP(s)
    b=m+2*n
    if b==0:
        # conservative: ignore the additional beta-zero stable damping
        return source
    if b<0:
        m,n,b=-m,-n,-b
    return source+primitive(b,zchar(m,n,T))-primitive(b,zchar(m,n,s))


def diff_coeff(b1,z1,b2,z2):
    s1=U*z1
    s2=U*z2
    bt=b1-b2
    st=(b1*s1-b2*s2)/bt
    bracket=(
        b1+b2
        +st*(b1*s1+b2*s2)
        +(b1*math.sqrt(1+s1*s1)+b2*math.sqrt(1+s2*s2))
         *math.sqrt(1+st*st)
    )
    return (s1-s2)*bracket/(2*(1+st*st))


def root_norm_HD(s):
    zd=zD(s)
    zp=zP(s)
    zh=2*zp-zd
    sh=U*zh
    sd=U*zd
    return abs(sh-sd)*math.sqrt(
        (sh+sd)**2
        +(math.sqrt(1+sh*sh)+math.sqrt(1+sd*sd))**2
    )


def maximize(m,n,steps=5000):
    best=-1e100
    bests=None
    for j in range(steps+1):
        s=TSTAR+(T-TSTAR)*j/steps
        a=propagated_action(m,n,s)
        if a>best:
            best=a
            bests=s
    return best,bests


target=env(2,X)
print("target P_new action at reset = %+.16e" % target)
print()
for name,mn in [
    ("H=P-D",(-1,1)),
    ("M=P-2D",(-2,1)),
    ("P+D",(1,1)),
    ("Cregen=3D-P",(3,-1)),
    ("2H",(-2,2)),
]:
    a,s=maximize(*mn)
    print("%-16s max=%+.16e gap=%+.16e at %.16f" % (name,a,a-target,s))

print()
print("terminal collar center = %.16f" % TERM)
print("remaining time to reset = %.16f" % (T-TERM))
print("P-D -> H coefficient   = %+.16e" % diff_coeff(2,zP(TERM),1,zD(TERM)))
print("H-D -> M root norm     = %+.16e" % root_norm_HD(TERM))

min_diff=1e100
min_root=1e100
for j in range(1001):
    s=TERM-WIDTH+2*WIDTH*j/1000.0
    min_diff=min(min_diff,abs(diff_coeff(2,zP(s),1,zD(s))))
    min_root=min(min_root,root_norm_HD(s))
print("min |P-D -> H| on width = %.16e" % min_diff)
print("min H-D root norm        = %.16e" % min_root)
