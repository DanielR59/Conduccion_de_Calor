import sys
from PIL import Image
from graficas import *
from matriz import solucion_sistema1D,solucion_sistema1D_Poisson, solucion_sistema1D_Neumann,solucion_sistema_conductividad_variable
import numpy as np
from Parametros import Pedir_Parametros_basicos
#######33
Im2=Image.open('Poisson_Dirichlet.png')
######3
print('Selecciona el tipo de problema',end='\n')    
print('-----------------------------------------')
print('1) Conduccion de calor estacionaria, conductividad constante ',end='\n')
print('2) Conduccion de calor, ecuacion de Poisson condicion tipo Dirichlet ',end='\n')
print('3) Conduccion de calor, ecuacion de Poisson condicion tipo Neumman',end='\n')
print('4) Conduccion de calor, ecuacion de Poisson conductividad no constante',end='\n')
try:
    seleccion=int(input())
except:
    print("No seas ñero")
if 0<seleccion<5 :
    print("hola")
    pass
else:
    print("No estas dentro de las selecciones")
    sys.exit()

if seleccion ==1:
    
    x_inicial,x_final,N,Ta,Tb,h,x=Pedir_Parametros_basicos()
    kappa=float(input('| Valor de la conductividad  constante para todo el medio    : k ='))
    fuente=int(input('Existe alguna fuente, sumidero o ninguno \n 1)fuente \n 2)sumidero \n 3) ninguno \n'))
    if fuente ==1:
        print("Valor de la fuente sin signo \n")
        Q=float(input())*-1
        
    elif fuente==2:
        print("Valor de la fuente sin signo\n")
        Q=float(input())
                
    elif fuente == 3:
        Q=0    
    plot_dominio(x_inicial,x_final,N)
    u=solucion_sistema1D(N,h,Ta,Tb,kappa,Q)
    plot_dominio2(x,u)




if seleccion==2:
    Im2.show()
    x_inicial,x_final,N,Ta,Tb,h,x=Pedir_Parametros_basicos()
    f=float(input('| Valor de f      : f ='))
    plot_dominio(x_inicial,x_final,N)
    u=solucion_sistema1D_Poisson(N, h,Ta,Tb,f)
    plot_dominio2(x,u)

if seleccion==3:

    x_inicial,x_final,N,Ta,Tb,h,x=Pedir_Parametros_basicos()
    plot_dominio(x_inicial,x_final,N)
    kappa=1
    print('Condicion de Neummann \n 1)Izquierda\n 2) Derecha\n')
    tipo_cond=int(input())
    if tipo_cond==1:
        tipo="izquierda"
    elif tipo_cond==2:
        tipo="derecha"
    print("Tipo de funcion u(x)\n 1)cos(x)\n 2)sen(x) \n 3)e^x \n 4)Funcion de Python \n ")
    ux=int(input())

    if ux==1:
        Q=np.cos(x)
    elif ux==2:
        Q=np.sin(x)
    elif ux==3:
        Q=np.exp(x)
    elif ux==4:
        print("Escribe tu comando de python en funcion de x e.g np.exp(x*np.pi)\n")
        a=input()
        Q=eval(a)
        pass

    u = solucion_sistema1D_Neumann(N,h,kappa,Q,Ta,Tb,tipo)
    plot_dominio2(x,u)

if seleccion==4:
    x_inicial,x_final,N,Ta,Tb,h,x=Pedir_Parametros_basicos()
    plot_dominio(x_inicial,x_final,N)
    
    fuente=int(input('Existe alguna fuente, sumidero o ninguno \n 1)fuente \n 2)sumidero \n 3) ninguno \n'))
    if fuente ==1:
        print("Valor de la fuente sin signo \n")
        Q=float(input())*-1
        
    elif fuente==2:
        print("Valor de la fuente sin signo\n")
        Q=float(input())
                
    elif fuente == 3:
        Q=0    
    
    print("Tipo de funcion de conductividad k(x)\n 1)|cos(x)|\n 2)|sen(x)| \n 3)random \n 4)Funcion de Python \n ")
    ux=int(input())

    if ux==1:
        kappa=np.fabs(np.cos(x))
    elif ux==2:
        kappa=np.fabs(np.sin(x))
    elif ux==3:
        kappa=np.random.random(len(x))
    elif ux==4:
        print("Escribe tu comando de python en funcion de x e.g np.exp(x*np.pi)\n")
        a=input()
        kappa=eval(a)
        pass
    u=solucion_sistema_conductividad_variable(N,h,Ta,Tb,kappa,Q)
    plot_dominio2(x,u)





    
