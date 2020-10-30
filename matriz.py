import numpy as np
from graficas import plot_dominio, plot_dominio2

#############DIRICHLET##########################################################################
def generar_matriz_izquierda(n):
    """
    Esta función genera y regresa la matriz de tamaño NxN a patir del tamaño n ingresado el cual debe ser la longitud del arreglo de temperaturas (T_n)
    
    Args:
        n (integer): Numero de nodos del sistema sin incluir las fronteras

    Returns:
        F: matriz de tamaño NxN 
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
    Función que genera la matriz del lado derecho a partir de los datos de entrada 
    
    Args:
        N (entero): Numero de nodos del sistema sin incluir las fronteras
        h ([type]): distancia entre nodos
        Ta ([type]): Condicion de frontera inicial
        Tb ([type]): Condicion de frontera final
        kappa ([type]): conductvidad del material, debe ser una constante >0 si no explota
        Q ([type]): [description]

    Returns:
        b[type]: matriz del lado derecho del sistema
    """


    k=np.ones(N)*kappa
    r=k/(h**2)

    Q2=np.ones(N)*Q

    T_aux=np.zeros(N)
    T_aux[0]=-Ta
    T_aux[-1]=-Tb

    b=(1/r)*Q2+T_aux

    return b


def solucion(A,b,Ta,Tb):

    """
    Funcion que genera el vector que contiene las soluciones a partir de la resolución del sistema Ax=b
    donde:
    A es la matriz generada por generar_matriz_izquierda
    
    b es la matriz generada por generar_matriz_derecha

    Ta,Tb son las condiciones de frontera
    
    """
    N=len(b)

    u=np.zeros(N+2)
    u[1:-1]=np.linalg.solve(A,b)
    u[0]=Ta
    u[-1]=Tb
    return u



def solucion_sistema1D(N,h,Ta,Tb,kappa,Q):
    """
    Funcion que utiliza las funciones:

    generar_matriz_izquierda
    generar_matriz_derecha
    solucion

    para regresar la solución del sistema apartir de los parámetros de entrada
    """
    A=generar_matriz_izquierda(N)
    b=generar_matriz_derecha(N,h,Ta,Tb,kappa,Q)

    u=solucion(A,b,Ta,Tb)
    return u


def solucion_sistema1D_Poisson(N,h,Ta,Tb,f):
    """
    Funcion que utiliza las funciones:

    generar_matriz_izquierda
    generar_matriz_derecha
    solucion

    para regresar la solución de la ecuacion de Poisson a partir de los parámetros de entrada


    Args:
        N (entero): Numero de nodos del sistema sin contar las fronteras 
        h ([type]): Espaciamiento entre los nodos
        Ta ([type]): Condicion de frontera inicial
        Tb ([type]): Condicion de frontera final
        f ([type]): coeficiente al cual está igualado en la ecuación de Poisson

    Returns:
        u[type]: Solucion del sistema
    """
        

    
    A=generar_matriz_izquierda(N)+np.eye(N)*(f*h)**2
    Q=0;kappa=1
    b=generar_matriz_derecha(N,h,Ta,Tb,kappa,Q)

    u=solucion(A,b,Ta,Tb)
    
    return u
#################intento interactivo##############
def solucion_sistema1D_interactive(N,Ta,Tb,kappa,Q,x_inicial,x_final):
    """
    Funcion que utiliza las funciones:

    generar_matriz_izquierda
    generar_matriz_derecha
    solucion

    para regresar la solución del sistema apartir de los parámetros de entrada
    """
    h=(x_final-x_inicial)/(N+1)
    plot_dominio(x_inicial,x_final,N)
    A=generar_matriz_izquierda(N)
    b=generar_matriz_derecha(N,h,Ta,Tb,kappa,Q)
    x=np.linspace(x_inicial,x_final,N+2)
    u=solucion(A,b,Ta,Tb)
    plot_dominio2(x,u)
    return u

###########################NEUMANN################################################################
#--------------------------NEUMANN------------------------------------------------------------##

def solucion_sistema1D_Neumann(N,h,kappa,Q,Ta,Tb,tipo):
    """
    Funcion que utiliza las funciones:

    generar_matriz_izquierda
    generar_matriz_derecha
    solucion

    para regresar la solución de la ecuacion de Poisson a partir de los parámetros de entrada


    Args:
        N (entero): Numero de nodos del sistema sin contar las fronteras 
        h ([type]): Espaciamiento entre los nodos
        Ta ([type]): Condicion de frontera inicial
        Tb ([type]): Condicion de frontera final
        f ([type]): coeficiente al cual está igualado en la ecuación de Poisson
        tipo([string]) "izquierda" o "derecha" frontera en la cual se tiene la condicion de Neumann

    Returns:
        u[type]: Solucion del sistema
    """
    A=generar_matriz_izquierda(N+1)

    if tipo=="izquierda":
        A[0,0]=-1
        b=generar_matriz_derecha_Neumann(N+1,h,Ta,Tb,kappa,Q[:-1],tipo)
    elif tipo=="derecha":
        A[-1,-1]=-1
        b=generar_matriz_derecha_Neumann(N+1,h,Ta,Tb,kappa,Q[1:],tipo)
    
    

    u=solucion_Neumman(A,b,Ta,Tb,tipo)
    
    return u

def generar_matriz_derecha_Neumann(N,h,Ta,Tb,kappa,Q,tipo):
    """
    Función que genera la matriz del lado derecho a partir de los datos de entrada 
    
    Args:
        N (entero): Numero de nodos del sistema sin incluir las fronteras
        h ([type]): distancia entre nodos
        Ta ([type]): Condicion de frontera inicial
        Tb ([type]): Condicion de frontera final
        kappa ([type]): conductvidad del material, debe ser una constante >0 si no explota
        Q ([type]): [description]

    Returns:
        b[type]: matriz del lado derecho del sistema
    """


    k=np.ones(N)*kappa
    r=k/(h**2)
    T_aux=np.zeros(N)
    
    if tipo=="izquierda":
        Q[0]=Q[0]/2
        T_aux[0]=-h*Ta
        T_aux[-1]=-Tb
    
    elif tipo=="derecha":
        Q[-1]=Q[-1]/2
        T_aux[0]=-Ta
        T_aux[-1]=-h*Tb
    
    Q2=np.ones(N)*Q

    

    b=(1/r)*Q2+T_aux

    return b


def solucion_Neumman(A,b,Ta,Tb,tipo):

    """
    Funcion que genera el vector que contiene las soluciones a partir de la resolución del sistema Ax=b
    donde:
    A es la matriz generada por generar_matriz_izquierda
    
    b es la matriz generada por generar_matriz_derecha

    Ta,Tb son las condiciones de frontera
    
    """
    N=len(b)

    u=np.zeros(N+1)
    
    
    
    if tipo=="izquierda":
        u[:-1]=np.linalg.solve(A,b)
        u[-1]=Tb
    
    elif tipo=="derecha":
        u[1:]=np.linalg.solve(A,b)
        u[0]=Ta
    return u

    




#####################################################################################################################################################################################################################################################################################################################################################################

def k_half(k):
    """Funcion que genera los valores auxiliares $k_{\frac{1}{2}}$ para la solución de la ecuación de conducción de calor de conductividad no constante.

    Args:
        k (array): vector de conductividad variable, debe ser de tamaño N+2, es decir, debe considerar el numero de nodos N+2 fronteras

    Returns:
        array: valores interpolados entre los valores de k, o sea k_medios 
    """

    n=len(k)
    k_medios=np.zeros(n-1)

    for i in range(n-1):
        k_medios[i]=(k[i+1]+k[i])/2

    return k_medios


def matriz_izquierda_conductividad_variable(k):

    """
    docstring
    """
    n=len(k)
    k_medios=k_half(k)
    MATRIZ=np.zeros((n-2,n-2))
    MATRIZ[0,0]=(k_medios[0]+k_medios[1])*-1
    MATRIZ[0,1]=k_medios[1]
    MATRIZ[-1,-1]=(k_medios[-2]+k_medios[-1])*-1
    MATRIZ[-1,-2]=k_medios[-2]
    for i in range(1,n-3):
        v_aux=[k_medios[i],(k_medios[i]+k_medios[i+1])*-1,k_medios[i+1]]
        MATRIZ[i,(i-1):i+2]=v_aux
    return MATRIZ


def matriz_derecha_conductividad_variable(f,k,h,Ta,Tb):
    """
    docstring
    """
    N=len(k)-2
    f=np.ones(N)*f*h**2
    k_medios=k_half(k)
    MD=np.zeros(N)
    u=np.zeros(N)
    u[0]=k_medios[0]*Ta*-1
    u[-1]=k_medios[-1]*Tb*-1
    MD=f+u

    return MD



def solucion_sistema_conductividad_variable(N,h,Ta,Tb,kappa,Q):
    
    """
    Funcion que utiliza las funciones:

    generar_matriz_izquierda
    generar_matriz_derecha
    solucion

    para regresar la solución del sistema apartir de los parámetros de entrada
    """
    A=matriz_izquierda_conductividad_variable(kappa)
    b=matriz_derecha_conductividad_variable(Q,kappa,h,Ta,Tb)

    u=solucion(A,b,Ta,Tb)
    return u