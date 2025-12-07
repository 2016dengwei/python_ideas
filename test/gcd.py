# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 12:21:23 2025

@author: 2008d

edit test for git @20251207
"""
 
xi=[1,0]
yi=[0,1]     

def gcd(x,y) ->int:
    a=max(x,y)
    b=min(x,y)

    r=a-b*int(a/b)
    q=int(a/b)
    
    if r==0:
        
        d=b
    else:
        n=len(xi)
        i=xi[n-2]-q*xi[n-1]
        xi.append(i)
        i=yi[n-2]-q*yi[n-1]
        yi.append(i)

        d=gcd(b,r)
        
    return d

def test(m,n):

    
    d=gcd(m,n)
    print(xi,yi)
    print(d,'=',m,'*',xi[-1],'+',n,'*',yi[-1])