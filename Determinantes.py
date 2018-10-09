import numpy as np
import math

def det2x2(matriz):
    return((matriz[0][0]*matriz[1][1])-(matriz[0][1]*matriz[1][0]))
    
def part1(matriz):
    new=matriz
    n=np.shape(new)[0]
    for i in range(n-1):
        d=(-1*new[i][0]/new[n-1][0])
        for j in range(n):
            new[i][j]=(d*new[n-1][j])+new[i][j]
    temp=list(range(n-1))
    for i in range(n-1):
        row=[]    
        temp[i]=row
        for j in range(1,n):
            row.append(new[i][j])
    new=temp
    return(new)
y=[[1,-1,2,-2],[1,0,1,-1],[2,3,-1,1],[1,0,1,3]]
z=[[0,2,1],[-1,3,0],[1,-2,1]]    
x=[[3,2,3],[3,3,5],[2,4,3]]
def det(matriz):
    n=np.shape(matriz)[0]
    m=np.shape(matriz)[1]
    si=True
    deter=1    
    new=matriz
    if(n==m):
        while(si==True):            
            n=np.shape(new)[0]
            if(n==2):                
                deter=deter*det2x2(new)
                si=False             
            elif(n>2): 
                deter=((-1)**(n-1))*new[n-1][0]
                new=part1(new) 
                si=True
    return(round(deter))
 """   
(-1**n-1)*new[n-1][0]
        diagonal=[]
        var=1
        #if(invertible(matriz)==True):
        for i in range(len(matriz[0])):
            for j in range(len(matriz[1])):
                
                diagonal.append(matriz[i+1][j+1])
        for k in range(len(diagonal)):
            var=var*diagonal[k]
            
    return(var)    
if (matriz[i+1][j+1]==1):
 """ 
def invertible(matriz):
    v_f=True
    if(det(matriz)==0):
        v_f= False
    return v_f