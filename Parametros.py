import numpy as np
import sys
import csv

def Pedir_Parametros_basicos():
    
    x_inicial= float(input('| Punto inicial del dominio : x_inicial =  '))
    x_final=float(input('| Punto final del dominio      : x_final = '))
    N=int(input('| Número total de nodos (no contando fronteras)    : N = '))
    Ta=float(input('| Temperatura en la frontera A      : A = '))
    Tb=float(input('| Temperatura en la frontera B      : B ='))
    
    h=(x_final-x_inicial)/(N+1)

    x=np.linspace(x_inicial,x_final,N+2)

    return x_inicial,x_final,N,Ta,Tb,h,x


def menu():
    """
    docstring
    """
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
        sys.exit()
    return seleccion


def get_Parametros_basicos(diccionario):

    x_inicial=float(diccionario['x_inicial'].get())
    x_final=float(diccionario['x_final'].get())
    N=int(diccionario['Nodos'].get())
    Ta=float(diccionario['Ta'].get())
    Tb=float(diccionario['Tb'].get())
    
    
    h=(x_final-x_inicial)/(N+1)

    x=np.linspace(x_inicial,x_final,N+2)

    return x_inicial,x_final,N,Ta,Tb,h,x


    
    

def save_Parametros(diccionario,x,u,**kwars):
    """
    docstring
    """
    diccionario2={}
    for item,valor in diccionario.items():
        diccionario2[item]=valor.get()
    
    diccionario2['Dominio']=x
    diccionario2['Solucion']=u


    # f = open('./Soluciones/Solucion.txt', 'w')
    # f.write(str(diccionario))
    # f.close()

    f= csv.writer(open("./Soluciones/"+kwars['cadena']+"Parametros_con"+str(diccionario2['Nodos'])+"Nodos.csv",'w'))
    for item,valor in diccionario2.items():
        if type(valor)  != np.ndarray:

            f.writerow([item,valor])
        else:
            f.writerow([item])
            f.writerows([valor])
        
    
    