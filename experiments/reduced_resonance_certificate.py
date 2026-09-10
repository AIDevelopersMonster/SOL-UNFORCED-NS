#!/usr/bin/env python3
"""Exact-rational interval certificate for the corrected v0.4 reduced difference relay."""
from fractions import Fraction

beta1=Fraction(25,16)
beta2=Fraction(9,16)
x1=Fraction(29,32)
y_minus=Fraction(613,500)
y_plus=Fraction(1227,1000)


def ln_bounds(z: Fraction,n: int=40):
    if z<=0: raise ValueError('z must be positive')
    if z<1:
        lo,hi=ln_bounds(1/z,n)
        return -hi,-lo
    w=(z-1)/(z+1)
    s=Fraction(0)
    wp=w
    for j in range(n+1):
        s += wp/Fraction(2*j+1)
        wp *= w*w
    rem=wp/Fraction(2*n+3)/(1-w*w)
    return 2*s,2*(s+rem)


def G_bounds(y: Fraction,n: int=40):
    xc=beta1*x1-beta2*y
    z=(x1*y/xc)**3*(beta1*beta2)**2
    lo,hi=ln_bounds(z,n)
    poly=Fraction(1)-beta1*beta1*x1**3-beta2*beta2*y**3+xc**3
    return (lo+poly)/3,(hi+poly)/3,xc,z

for name,y in [('y_minus',y_minus),('y_plus',y_plus)]:
    lo,hi,xc,z=G_bounds(y)
    print(name,'y=',float(y),'xc=',float(xc),'G in',float(lo),float(hi))

assert G_bounds(y_minus)[1] < 0
assert G_bounds(y_plus)[0] > 0
print('CERTIFIED: G(613/500) < 0 < G(1227/1000)')
