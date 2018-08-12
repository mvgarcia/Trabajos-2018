import numpy as np
import matplotlib.pyplot as plt

def squ(a):
    return (a**2)
Exct=0.016
R=1
#diferencia de longitudes
#1
psol= np.sin(np.deg2rad(291.98-191.43)) #s-m
pmarte=np.sin(np.deg2rad(191.43-155.68)) #m-mo
#2
ssol= np.sin(np.deg2rad(201.92-106.62)) #s-m
smarte=np.sin(np.deg2rad(106.62-65.21)) #m-mo
#3
tsol=np.sin(np.deg2rad(113.4-22.44))
tmarte=np.sin(np.deg2rad(22.44-335.03))
#4
csol=np.sin(np.deg2rad(19.77-282.83))
cmarte=np.sin(np.deg2rad(282.83-241.62))
def rTS (angulo):
    return(R*(1-squ(Exct))/1+(Exct*np.cos(angulo)))
def d(dia):
    return(365/360)*(28+ dia)
r1=(d(25)+d(-16))/2
r2=(d(28+31+30+31+30+31+31+30+31+27)+d(28+31+30+31+30+31+31+30+14+1))/2
r3=(d(28+31+30+31+30+31+28)+d(28+31+30+31+30+15))/2
r4=(d(28+31+30+22+1)+d(28+31+30+9))/2

#vector tierra-sol ('1UA')
r1=rTS(r1)
r2=rTS(r2)
r3=rTS(r3)
r4=rTS(r4)

#vector sol-marte
R1=(r1*psol)/pmarte
R2=(r2*ssol)/smarte
R3=(r3*tsol)/tmarte
R4=(r4*csol)/cmarte
#print(R1,R2,R3,R4)
#para graficar
def xy(R,ang):
    return [R*np.cos(np.deg2rad(ang)),R*np.sin(np.deg2rad(ang))]
R=[xy(R1,155),xy(R2,65),xy(R3,335),xy(R4,242)]
#print(R)
#Gráfica 1
plt.figure(1)
plt.scatter(R[0][0],R[0][1],color='g')
plt.scatter(R[1][0],R[1][1],color='b')
plt.scatter(R[2][0],R[2][1],color='r')
plt.scatter(R[3][0],R[3][1],color='y')
plt.axis("equal")#igualar ejes
plt.scatter(0,0)
#plt.axvline(0,0,1,linestyle='--',color='b')#eje y
plt.axhline(0,0,1,linestyle='-',color='k')#eje x
#plt.savefig('fig')

#Semieje mayor-menor
a=(R1+R3)/2
b=(R2+R4)/2
#print(a,b)
#Direccion del perihelio
w_=335
#Excentricidad
c=(a-R3)
e=c/a
#print(c,e)
#Inclinación
def i(r,ang):
    return(r*np.tan(np.deg2rad(ang)))
Z1=i(R1-1,4.36)
Z2=i(R2-1,1.47)
Z3=i(R3-1,-6.62)
Z4=i(R4-1,-1.19)
Zo=0.052
i=np.rad2deg(np.arctan(Zo/a))
print(Z1,Z2,Z3,Z4,i)
#Longitud del nodo ascendente
Omega=50
#Gráfica 2
plt.figure(2)
plt.scatter(155,Z1,color='g')
plt.scatter(65,Z2,color='b')
plt.scatter(335,Z3,color='r')
plt.scatter(242,Z4,color='y')
plt.axhline(0,0,1,linestyle='-',color='k')#eje x
plt.axis([0,360,-0.1,0.1])
plt.grid(True) #cuadricula
