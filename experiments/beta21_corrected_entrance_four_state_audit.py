"""Diagnostic audit for the corrected beta-(2,1) entrance gate.

At u=2.5, delta=0.1375 the exact first relay is

    P - C -> D

with source matching

    E_2(x) + E_1(x+delta) = E_1(x-delta).

The sufficient internal cancellation block is

    D,
    M=D-C,
    H=M+D=2D-C,
    R3=H+M=3D-2C.

The script checks:
- exact source matching;
- principal edge nonvanishing;
- stability on 0 <= t <= 1e-3;
- which entrance-generated characters can still lie above the later
  strong-H target action when propagated to t_*.

This is a reproducibility certificate, not outward-rounded interval arithmetic.
"""

import math

U = 2.5
DELTA = 0.1375
X = 0.77794450260672482712680064619405
TSTAR = 0.22512911698286797975123849107983
WIDTH = 1.0e-3


def turning(beta):
    return math.sqrt((1.0+U*U)*beta**(-4.0/3.0)-1.0)/U


def primitive(beta,z):
    z=abs(z)
    return (
        math.asinh(U*z)
        - beta*beta/(1.0+U*U)**1.5
        * (U*z+U**3*z**3/3.0)
    )


def env(beta,z):
    xb=turning(beta)
    return primitive(beta,z)-primitive(beta,xb)


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
    return (s1-s2)*bracket/(2.0*(1.0+st*st))


def beta_zero_data(z1,z2):
    s1=U*z1
    s2=U*z2
    m=s1-s2
    S=s1+s2
    R=math.sqrt(1+s1*s1)+math.sqrt(1+s2*s2)
    # c0=-1 normalization
    bM=(0.0,-S,-R)
    norm=abs(m)*math.sqrt(S*S+R*R)
    return m,bM,norm


def wave_plus_root_coeff(beta,z,m,bM):
    s=U*z
    g=(1.0,-s,-math.sqrt(1+s*s))
    q=[m*bM[j]+beta*bM[1]*g[j] for j in range(3)]
    st=s+m/beta
    ah=(q[0]-st*q[1])/(1+st*st)
    an=q[2]/(-math.sqrt(1+st*st))
    return 0.5*(ah+an)


def entrance_edges(t):
    zP=X+t
    zC=X+DELTA+t
    zD=X-DELTA+t
    kD=diff_coeff(2,zP,1,zC)
    m,bM,rootnorm=beta_zero_data(zD,zC)
    kH=wave_plus_root_coeff(1,zD,m,bM)
    zH=X-3*DELTA+t
    kR=wave_plus_root_coeff(1,zH,m,bM)
    return kD,rootnorm,kH,kR


def z_pc(m,n,t):
    # character m P + n C, beta=2m+n
    beta=2*m+n
    return (2*m*(X+t)+n*(X+DELTA+t))/beta


def propagated_action(m,n,A_source,s,t1):
    beta=2*m+n
    if beta < 0:
        m,n,beta=-m,-n,-beta
    if beta == 0:
        # conservative upper bound: ignore additional stable damping
        return A_source
    return A_source+primitive(beta,z_pc(m,n,t1))-primitive(beta,z_pc(m,n,s))


def canonical(k):
    m,n=k
    beta=2*m+n
    if beta<0 or (beta==0 and m<0):
        return (-m,-n)
    return k


def reachable_at(s,bound=10,maxiter=30):
    AP=env(2,X+s)
    AC=env(1,X+DELTA+s)
    best={(1,0):AP,(-1,0):AP,(0,1):AC,(0,-1):AC}
    parent={}
    for _ in range(maxiter):
        changed=False
        items=list(best.items())
        for a,Aa in items:
            for b,Ab in items:
                if a==b:
                    # same signed-character principal self-interaction vanishes
                    continue
                child=(a[0]+b[0],a[1]+b[1])
                if child==(0,0):
                    continue
                if abs(child[0])>bound or abs(child[1])>bound:
                    continue
                act=Aa+Ab
                if act < -1.0:
                    continue
                if act > best.get(child,-1e100)+1e-13:
                    best[child]=act
                    parent[child]=(a,b)
                    changed=True
        if not changed:
            break
    target=env(2,X-2*DELTA+TSTAR)
    out=[]
    for k,act in best.items():
        if canonical(k)!=k:
            continue
        m,n=k
        beta=2*m+n
        Af=propagated_action(m,n,act,s,TSTAR)
        out.append((k,beta,Af,Af-target,parent.get(k)))
    return sorted(out,key=lambda r:r[3],reverse=True)


AP=env(2,X)
AC=env(1,X+DELTA)
AD=env(1,X-DELTA)
print("input actions")
print("A_P = %+.16e" % AP)
print("A_C = %+.16e" % AC)
print("A_D = %+.16e" % AD)
print("relay residual = %+.16e" % (AP+AC-AD))
print()

print("center edge margins")
for name,val in zip(
    ["P-C->D","D-C->M root","M+D->H","H+M->R3"],
    entrance_edges(0.0),
):
    print("%-16s %+.16e" % (name,val))

mins=[1e100]*4
future_omit=1e100
for j in range(1001):
    s=WIDTH*j/1000.0
    vals=entrance_edges(s)
    for k,v in enumerate(vals):
        mins[k]=min(mins[k],abs(v))
    rows=reachable_at(s)
    promoted=[r for r in rows if r[3]>=-1e-12]
    omitted=[r for r in rows if r[3]<-1e-12]
    future_omit=min(future_omit,-omitted[0][3])

print()
print("min margins on 0<=t<=1e-3")
for name,val in zip(
    ["P-C->D","D-C->M root","M+D->H","H+M->R3"],mins
):
    print("%-16s %.16e" % (name,val))
print("future-action omitted gap %.16e" % future_omit)

print()
rows=reachable_at(0.0)
target=env(2,X-2*DELTA+TSTAR)
print("strong-H target action = %+.16e" % target)
print("entrance-generated classes above that target at t_*")
for r in rows:
    if r[3]>=-1e-12:
        print(r)
print("nearest omitted")
for r in rows:
    if r[3]<-1e-12:
        print(r)
        break
