#4 May
import numpy as np
import matplotlib.pyplot as plt
a=9.5547 #UA
T=29.457#años
L=165#°
#Saturno helioc
t=38+ (124/365.25) #años
D_Lambda=360*((t/T)-1)#deg---mirar cómo hacer para tomar solo lo decimal
Lambda_S= D_Lambda+L #deg

#Tierra helioc
Lambda_T=180+(45*360/365.25) #deg

#Graficar
def xy(a,Lambda):
    return [a*np.cos(np.deg2rad(Lambda)),a*np.sin(np.deg2rad(Lambda))]

Saturno=(xy(a,Lambda_S))
Tierra=(xy(1,Lambda_T))

plt.figure(1)
plt.scatter(Saturno[0],Saturno[1],color='r')
plt.scatter(Tierra[0],Tierra[1],color='b')
plt.scatter(0,0,color='y')
plt.axis("equal")

#Posiciones relativas
x=Saturno[0]-Tierra[0]
y=Saturno[1]-Tierra[1]

plt.figure(2)
plt.scatter(0,0,color='b')
plt.scatter(x,y,color='r')
plt.axis("equal")
plt.axvline(0,0,1,linestyle='--',color='k')#eje y
plt.axhline(0,0,1,linestyle='--',color='k')#eje x
print(np.rad2deg(np.arctan(y/x)))
print(a*np.cos(np.deg2rad(2.5)))
print(a*np.sin(np.deg2rad(2.5)))
Longitud=np.rad2deg(np.arccos(x/a))#Revisar
L=np.rad2deg(np.arcsin(y/a))
print(180+Longitud,180-Longitud,180+L,Longitud,L)
