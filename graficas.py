import matplotlib.pyplot as plt

def plot_dominio(x_inicial,x_final,Nodos):
    """
    docstring
    """
    
    h=(x_final-x_inicial)/(Nodos+1)
    x=[h*i for i in range(Nodos+2)]
    plt.plot([x_inicial,x_final],[0,0], lw=10)
    plt.plot([x_inicial,x_inicial],[0,0], 'sr', )
    plt.plot([x_final,x_final],[0,0], 'sg', )
    plt.plot([x[1:-1],x[1:-1]],[0,0], 'ko')
    plt.legend(['','$T_a$','$T_b$','Nodos'])
    plt.show()