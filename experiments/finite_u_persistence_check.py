#!/usr/bin/env python3
"""High-precision diagnostic for v0.4 finite-u persistence."""
import mpmath as mp
mp.mp.dps = 60
b1 = mp.mpf(25)/16
b2 = mp.mpf(9)/16
x1 = mp.mpf(29)/32

def xt(b,u):
    return mp.sqrt((1+u*u)*b**(-mp.mpf(4)/3)-1)/u

def E(b,x,u):
    t=xt(b,u)
    return mp.asinh(u*x)-mp.asinh(u*t)-b*b/(1+u*u)**(mp.mpf(3)/2)*(u*(x-t)+u**3*(x**3-t**3)/3)

def xc(y):
    return b1*x1-b2*y

def G(y,u):
    return E(b1,x1,u)+E(b2,y,u)-E(1,xc(y),u)

for u in [20,25,50,100,1000]:
    uu=mp.mpf(u)
    y=mp.findroot(lambda z:G(z,uu),(mp.mpf('1.2'),mp.mpf('1.25')))
    print(f"u={u:4d} y={mp.nstr(y,18)} xc={mp.nstr(xc(y),18)} residual={mp.nstr(G(y,uu),5)}")
