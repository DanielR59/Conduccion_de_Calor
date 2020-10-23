import numpy as np

def generar_matriz(n):
    """
    Esta función genera y regresa la matriz de tamaño NxN a patir del tamaño n ingresado el cual debe ser la longitud del arreglo de temperaturas (T_n)
    """ 

    F=np.zeros((n,n)) #se genera una matriz cuadrada de ceros de tamaño n 

    #Se llenan la primer y ultima fila de la matríz
    F[0,0]=-2
    F[0,1]=1
    F[-1,-1]=-2
    F[-1,-2]=1

    v=[1,-2,1] #arreglo auxiliar

    #Se llena el resto de la matriz
    for i in range(1,n-1):
        F[i,(i-1):i+2]=v

    #print(F)

    #F_inv=np.linalg.inv(F)

    #print(F_inv)

    return F

def generar_matriz_derecha(N,h,Ta,Tb,kappa,Q):

    """
    docstring
    """
    k=np.ones(N)*kappa
    r=k/h

    Q2=np.ones(N)*Q

    T_aux=np.zeros(N)
    T_aux[0]=-Ta
    T_aux[-1]=-Tb

    b=(1/r)*Q2+T_aux

    return b


def solucion(A,b,Ta,Tb):

    """
    docstring
    """
    N=len(b)

    u=np.zeros(N+2)
    u[1:-1]=np.linalg.solve(A,b)
    u[0]=Ta
    u[-1]=Tb
    return u
