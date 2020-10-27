import matplotlib.pyplot as plt
import numpy as np
def plot_dominio(x_inicial,x_final,Nodos):
    """
    docstring
    """
    
    h=(x_final-x_inicial)/(Nodos+1)
    #x=[h*i for i in range(Nodos+2)]
    x=[i for i in np.arange(x_inicial,x_final+h,h)]
    plt.plot([x_inicial,x_final],[0,0], lw=10)
    plt.plot([x_inicial,x_inicial],[0,0], 'sr', )
    plt.plot([x_final,x_final],[0,0], 'sg', )
    plt.plot([x[1:-1],x[1:-1]],[0,0], 'ko')
    plt.legend(['','$T_a$','$T_b$','Nodos'])
    plt.show()

def plot_dominio2(x_inicial,x_final,N,u,Ta,Tb):
    """
    docstring
    """
    
    h=(x_final-x_inicial)/(N+1)
    x=[i for i in np.arange(x_inicial,x_final+h,h)]
    #x=[h*i for i in range(N+2)]
    
    
    plt.scatter(x,u,c=u,cmap='plasma')
    plt.colorbar()
    plt.xlabel('$x$')
    plt.ylabel('Temperatura')
    plt.title('Transferencia de calor')
    #plt.legend()
    plt.show()
    




