"""n=15
no=0
x=0
import numpy as np

def m15(a):
    return 15*a
def m22(b):
    return 22*b

def m7(a):
    return 7*a
def m5(b):
    return 5*b

for i in range(10):
    for j in range(10):
        if(m15(i)+m22(j)==n):
            #print(i,j)
            n=n+1
        else:
            no=n
            n=n+1
            print(no)
            
            
print(no)
         
        
m=27
for i in range(100):
    for j in range(100):
        if((m7(i)+m5(j))==m):
            print(i,j,m)
            m=m+1
            
            
        else:
            x=m
print(x)   
"""
for j in range(14):
    print((293-22*j)/15,j)
import math
cumple=True
x=0
a=15
b=22
for m in range(5,330):
    i=0
    cumple=True
    while cumple:
        
        while i<=(m/a):
            j=(m-(a*i))/b 
            x=j-math.floor(j)
            #x=(m-(a*i))%b
            
            if(x==0):
                print(i,j,m)
                cumple=False
                i=m
            else:
                i=i+1
        if(i!=m):            
            print(m,"No sirve")
            cumple=False
            m=m+1         