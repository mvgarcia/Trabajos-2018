#4 May
"""
Revisar Longitud 
"""
import numpy as np
a=9.5547 #UA

#Saturno helioc
t=38+ 124/365.25 #años
D_Lambda=360*t/29.457#deg
Lambda_S= D_Lambda+165 #deg

#Tierra helioc
Lambda_T=180+(45*360/365.25) #deg

#Graficar
def xy(a,Lambda):
    return [a*np.cos(np.deg2rad(Lambda)),a*np.sin(np.deg2rad(Lambda))]

Saturno=xy(a,Lambda_S)
Tierra=xy(a,Lambda_T)

#Posiciones relativas
x=Saturno[0]-Tierra[0]
y=Saturno[1]-Tierra[1]

Longitud=180-np.rad2deg(np.arccos(x/9.44))#Revisar
L=np.rad2deg(np.arcsin(y/9.44)) ##creo que es este =200.0445
#Longitud=180+np.rad2deg(np.arccos(-2.546/4.235))
#L=180-np.rad2deg(np.arcsin(-3.384/4.235))
print(Longitud,L)
