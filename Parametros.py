import numpy as np
def Pedir_Parametros_basicos():
    
    x_inicial= float(input('| Punto inicial del dominio : x_inicial =  '))
    x_final=float(input('| Punto final del dominio      : x_final = '))
    N=int(input('| Número total de nodos (no contando fronteras)    : N = '))
    Ta=float(input('| Temperatura en la frontera A      : A = '))
    Tb=float(input('| Temperatura en la frontera B      : B ='))
    
    h=(x_final-x_inicial)/(N+1)

    x=np.linspace(x_inicial,x_final,N+2)

    return x_inicial,x_final,N,Ta,Tb,h,x
