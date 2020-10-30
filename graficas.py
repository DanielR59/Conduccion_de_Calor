import matplotlib.pyplot as plt
import numpy as np
def plot_dominio(x_inicial,x_final,Nodos):
    """funcion que genera el plot del doominio de longitud L definido a partir de los valores de entrada, además de graficar el numero de nodos del sistema 

    Args:
        x_inicial ([type]): Punto inicial del sistema 1D
        x_final ([type]): Punto final del sistema 1D
        Nodos ([type]): Numero de nodos del sistema sin contar x_inicial y x_final
    """
    
    h=(x_final-x_inicial)/(Nodos+1)
    #x=[h*i for i in range(Nodos+2)]
    x=np.linspace(x_inicial,x_final,Nodos+2)
    plt.plot([x_inicial,x_final],[0,0], lw=10)
    plt.plot([x_inicial,x_inicial],[0,0], 'sr', )
    plt.plot([x_final,x_final],[0,0], 'sg', )
    plt.plot([x[1:-1],x[1:-1]],[0,0], 'ko')
    plt.legend(['','$T_a$','$T_b$','Nodos'])
    plt.show()

def plot_dominio2(x,u):
    """Funcion que genera la grafica del resultado final de la conducción de calor en 1D estacionaria, a partir de valores de entrada

    Args:
        x_inicial ([type]): Punto inicial del sistema 1D
        x_final ([type]): Punto final del sistema 1D
        N ([type]): Numero de nodos del sistema en los cuales se calcula la teperatura
        u ([type]): Solución del sistema
        Ta ([type]): Condicion de frontera izquierda
        Tb ([type]): Condicion de frontera derecha
    """
    
    
    
    plt.scatter(x,u,c=u,cmap='plasma')
    plt.colorbar()
    plt.xlabel('$x$')
    plt.ylabel('Temperatura')
    plt.title('Transferencia de calor')
    #plt.legend()
    plt.show()
    




