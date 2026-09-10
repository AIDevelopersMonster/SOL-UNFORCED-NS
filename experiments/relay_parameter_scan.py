#!/usr/bin/env python3
"""Reproduce the current v0.4 same-scale difference-relay witness."""
import math

beta1=25/16
beta2=9/16
beta_child=beta1-beta2
beta_sum=beta1+beta2
x1=29/32

def F(beta,x): return 1/x-beta*beta*x*x
def I(beta,x): return math.log(x)+(2/3)*math.log(beta)-beta*beta*x**3/3+1/3
def xc(y): return beta1*x1-beta2*y
def G(y): return I(beta1,x1)+I(beta2,y)-I(1,xc(y))

lo,hi=1.226,1.227
for _ in range(80):
    mid=(lo+hi)/2
    if G(mid)>0: hi=mid
    else: lo=mid
y=(lo+hi)/2
child=xc(y)
xsum=(beta1*x1+beta2*y)/beta_sum

print("SOL-UNFORCED-NS v0.4 difference relay")
print("beta1      =",beta1)
print("beta2      =",beta2)
print("difference =",beta_child)
print("sum beta   =",beta_sum)
print("x1         =",x1)
print("y          =",y)
print("xc         =",child)
print("G          =",G(y))
print("F1         =",F(beta1,x1))
print("F2         =",F(beta2,y))
print("Fc         =",F(1,child))
print("x_sum      =",xsum)
print("F_sum      =",F(beta_sum,xsum))
