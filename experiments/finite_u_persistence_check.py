#!/usr/bin/env python3
"""High-precision diagnostic for the corrected v0.4 finite-u difference relay."""
import mpmath as mp
mp.mp.dps=60
beta1=mp.mpf(25)/16
beta2=mp.mpf(9)/16
x1=mp.mpf(29)/32


def xturn(beta,u):
    return mp.sqrt((1+u*u)*beta**(-mp.mpf(4)/3)-1)/u

def E(beta,u,x):
    xt=xturn(beta,u)
    return (mp.asinh(u*x)-mp.asinh(u*xt)
            - beta**2/(1+u*u)**(mp.mpf(3)/2)
            *(u*(x-xt)+u**3*(x**3-xt**3)/3))

def xc(y): return beta1*x1-beta2*y

def G(u,y): return E(beta1,u,x1)+E(beta2,u,y)-E(1,u,xc(y))

for u in [20,25,50,100,1000]:
    u=mp.mpf(u)
    y=mp.findroot(lambda yy:G(u,yy),(mp.mpf('1.1'),mp.mpf('1.3')))
    print('u=',u,'y=',mp.nstr(y,18),'xc=',mp.nstr(xc(y),18),'G=',mp.nstr(G(u,y),5))
