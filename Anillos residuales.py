"""
Tablas de suma y multiplicación (Anillos residuales-Z/nZ)
"""

def suma(n):
    matriz=[]
    for i in range (n): 
        fila=[]
        for j in range (n):            
            fila.append((i+j)%n) 
            if(j==n-1):
                matriz.append(fila)          
    return matriz

def multipl(n):
    matriz=[]    
    for i in range (n):  
        fila=[]
        for j in range (n):            
            fila.append((i*j)%n) 
            if(j==n-1):
                matriz.append(fila)           
    return matriz

