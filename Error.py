import numpy as np
import pandas as pd

def describe_error(sol_analitica,sol_numerica,h):
    """Funcion que presenta de manera decente el error entre dos vectores

    Args:
        sol_analitica (array): vector conteniendo la solucion analitica
        sol_numerica (array): vector que contiene la solucion numerica
    """
    E=sol_analitica-sol_numerica
    L_inf=np.linalg.norm(E,np.inf)
    L_1=np.linalg.norm(h*E,1)
    L_2=np.linalg.norm(h*E,2)

    Error=pd.DataFrame({'Solucion analitica' : sol_analitica,\
        'Solucion numerica' : sol_numerica, \
        'Vector Error' : E,\
        'Norma $L_\infty$' : L_inf,\
        'Norma $L_1$' : L_1,\
        'Norma $L_2$' : L_2})
    
    # print(Error)
    return Error

def csv_to_list(archivo):
    """
    docstring
    """
    print(archivo)
    Lista=pd.read_csv(archivo)
    Lista=pd.DataFrame(Lista)
    Dominio=Lista['Dominio'][1:]
    Solucion=Lista['Solucion'][1:]
    Dominio=Dominio.to_numpy().tolist()
    Solucion=Solucion.to_numpy().tolist()
    for i in range(len(Dominio)):
        Dominio[i]=float(Dominio[i])
        Solucion[i]=float(Solucion[i])
    return  Dominio,Solucion

if __name__ == "__main__":
    
    archivo1='./Soluciones/Conduccion de calor, ecuacion de Poisson condicion tipo NeummanParametros_con50Nodos.csv'
    archivo2='./Soluciones/Solucion AnaliticaParametros_con50Nodos.csv'
    D1,Sol1=csv_to_list(archivo1)
    D2,Sol2=csv_to_list(archivo2)
    describe_error(np.array(Sol1),np.array(Sol2),1)