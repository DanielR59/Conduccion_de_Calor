import numpy as np
import pandas as pd

def describe_error(sol_analitica,sol_numerica):
    """Funcion que presenta de manera decente el error entre dos vectores

    Args:
        sol_analitica (array): vector conteniendo la solucion analitica
        sol_numerica (array): vector que contiene la solucion numerica
    """
    E=sol_analitica-sol_numerica
    L_inf=np.linalg.norm(E,np.inf)
    L_1=np.linalg.norm(E,1)
    L_2=np.linalg.norm(E,2)

    Error=pd.DataFrame({'Solucion analitica' : sol_analitica,\
        'Solucion numerica' : sol_numerica, \
        'Vector Error' : E,\
        'Norma $L_\infty$' : L_inf,\
        'Norma $L_1$' : L_1,\
        'Norma $L_2$' : L_2})
    print(Error)

    pass

