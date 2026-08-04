import math as m
import functools as f
a=int(input())
l=list(map(int,input().split()))
g=f.reduce(m.gcd,l)
p=m.prod(l)
m=(10**9)+7
print(p**g%m)
