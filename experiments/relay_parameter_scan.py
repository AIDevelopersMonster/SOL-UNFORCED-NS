#!/usr/bin/env python3
"""Reproduce the corrected v0.4 same-physical-scale beta difference relay witness."""
import math

beta1=25/16
beta2=9/16
beta_plus=beta1+beta2
x1=29/32
y2=1.2260460510205621
xc=beta1*x1-beta2*y2


def F(beta,x): return 1/x-beta*beta*x*x

def I(beta,x): return math.log(x)+(2/3)*math.log(beta)-beta*beta*x**3/3+1/3

xplus=(beta1*x1+beta2*y2)/beta_plus
G=I(beta1,x1)+I(beta2,y2)-I(1,xc)
Gp=F(beta2,y2)+beta2*F(1,xc)

print('SOL-UNFORCED-NS corrected v0.4 difference relay')
print('beta1-beta2 =',beta1-beta2)
print('beta_plus    =',beta_plus)
print('x1           =',x1)
print('y2           =',y2)
print('xc           =',xc)
print('envelope residual =',G)
print("G'(y2)      =",Gp)
print('F parent1    =',F(beta1,x1))
print('F catalyst   =',F(beta2,y2))
print('F child      =',F(1,xc))
print('sum xplus    =',xplus)
print('F sum branch =',F(beta_plus,xplus))
