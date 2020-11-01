import numpy as np
import tkinter
from tkinter import messagebox
from graficas import *
from matriz import solucion_sistema1D, solucion_sistema1D_Poisson, solucion_sistema1D_Neumann,solucion_sistema_conductividad_variable
from Parametros import get_Parametros_basicos,save_Parametros
from PIL import Image,ImageTk

def Proceso1(diccionario):
    """
    docstring
    """
    # print(diccionario['x_inicial'].get())
    # print(diccionario['x_final'].get())
    x_inicial,x_final,N,Ta,Tb,h,x=get_Parametros_basicos(diccionario)
    kappa=float(diccionario['kappa'].get())
    Q=float(diccionario['Q'].get())
    plot_dominio(x_inicial,x_final,N,cadena='Conduccion de calor estacionaria, conductividad constante')
    u=solucion_sistema1D(N,h,Ta,Tb,kappa,Q)
    save_Parametros(diccionario,x,u,cadena='Conduccion de calor estacionaria, conductividad constante')
    
    plot_dominio2(x,u,cadena='Conduccion de calor estacionaria, conductividad constante')

def Proceso2(diccionario):
    """
    docstring
    """
    # print(diccionario['x_inicial'].get())
    # print(diccionario['x_final'].get())
    x_inicial,x_final,N,Ta,Tb,h,x=get_Parametros_basicos(diccionario)
    f=float(diccionario['f'].get())
    plot_dominio(x_inicial,x_final,N,cadena='Conduccion de calor, ecuacion de Poisson condicion tipo Dirichlet')
    u=solucion_sistema1D_Poisson(N, h,Ta,Tb,f)
    save_Parametros(diccionario,x,u,cadena='Conduccion de calor, ecuacion de Poisson condicion tipo Dirichlet')
    
    plot_dominio2(x,u,cadena='Conduccion de calor, ecuacion de Poisson condicion tipo Dirichlet')

def Proceso3(diccionario):
    """
    docstring
    """
    
    x_inicial,x_final,N,Ta,Tb,h,x=get_Parametros_basicos(diccionario)
    plot_dominio(x_inicial,x_final,N,cadena='Conduccion de calor, ecuacion de Poisson condicion tipo Neumman')
    
    kappa=float(diccionario['kappa'].get())
    Q=eval(diccionario['Q'].get())
    print(Q)
    Tipo=diccionario['Tipo'].get()
    u = solucion_sistema1D_Neumann(N,h,kappa,Q,Ta,Tb,Tipo)
    save_Parametros(diccionario,x,u,cadena='Conduccion de calor, ecuacion de Poisson condicion tipo Neumman')
    
    plot_dominio2(x,u,cadena='Conduccion de calor, ecuacion de Poisson condicion tipo Neumman')

def Proceso4(diccionario):
    """
    docstring
    """
    
    x_inicial,x_final,N,Ta,Tb,h,x=get_Parametros_basicos(diccionario)
    plot_dominio(x_inicial,x_final,N,cadena='Conduccion de calor, ecuacion de Poisson conductividad no constante')
    
    Q=float(diccionario['Q'].get())
    kappa=eval(diccionario['kappa'].get())
    
    u=solucion_sistema_conductividad_variable(N,h,Ta,Tb,kappa,Q)
    save_Parametros(diccionario,x,u,cadena='Conduccion de calor, ecuacion de Poisson conductividad no constante')
    
    plot_dominio2(x,u,cadena='Conduccion de calor, ecuacion de Poisson conductividad no constante')



def opcion1(ventana):
    """
    docstring
    """

    opciones = tkinter.Toplevel(ventana)
    opciones.title('Conduccion de calor estacionaria')
    for i in range(9):
        opciones.rowconfigure(i,weight=1)
    # for i in range(1):
    #     opciones.columnconfigure(i,weight=1)
    opciones.columnconfigure(0,weight=1)
    opciones.columnconfigure(1,weight=1)
    
    #opciones.geometry('400x300')

    myImg=Image.open('Estacionario.png')
    myImg= myImg.resize((300,150))
    myImg=ImageTk.PhotoImage(myImg)
    L0=tkinter.Label(opciones,image= myImg).grid(row=0,column=0,columnspan=2,)
    

    L1=tkinter.Label(opciones, text ='x inicial (m) :').grid(row=1,column=0)
    x_inicial = tkinter.Entry(opciones)
    x_inicial.grid(row =1,column=1)
    


    L2=tkinter.Label(opciones, text ='x final (m):').grid(row=2,column=0)
    x_final = tkinter.Entry(opciones)
    x_final.grid(row =2,column=1)

    L3=tkinter.Label(opciones, text ='Numero de nodos sin contar fronteras :').grid(row=3,column=0)
    Nodos = tkinter.Entry(opciones)
    Nodos.grid(row =3,column=1)

    L4=tkinter.Label(opciones, text ='Temperatura en la frontera A (K)     : A =  :').grid(row=4,column=0)
    Ta = tkinter.Entry(opciones)
    Ta.grid(row =4,column=1)

    L5=tkinter.Label(opciones, text ='Temperatura en la frontera B (K)     : B =  :').grid(row=5,column=0)
    Tb = tkinter.Entry(opciones)
    Tb.grid(row =5,column=1)

    L6=tkinter.Label(opciones, text ='Conductividad termica kappa (W/m) :').grid(row=6,column=0)
    kappa = tkinter.Entry(opciones)
    kappa.grid(row = 6,column=1)

    L7=tkinter.Label(opciones, text ='Fuente (-) o sumidero (+) Q(WK/m^3) :  ').grid(row=7,column=0)
    Q = tkinter.Entry(opciones)
    Q.grid(row = 7,column=1)

    diccionario={'x_inicial' : x_inicial, 'x_final' : x_final, 'Nodos' : Nodos, 'Ta' : Ta, 'Tb' :Tb, 'kappa' : kappa, 'Q' : Q}

    Calcular = tkinter.Button(opciones, text = 'Calcular', command=lambda: Proceso1(diccionario)).grid(row=8)
    

    opciones.mainloop()
    

def opcion2(ventana):
    """
    docstring
    """

    opciones = tkinter.Toplevel(ventana)
    opciones.title('Conduccion de calor eq Poisson')

    for i in range(8):
        opciones.rowconfigure(i,weight=1)
    # for i in range(1):
    #     opciones.columnconfigure(i,weight=1)
    opciones.columnconfigure(0,weight=1)
    opciones.columnconfigure(1,weight=1)
    


    myImg=Image.open('Poisson_Dirichlet.png')
    myImg= myImg.resize((300,150))
    myImg=ImageTk.PhotoImage(myImg)
    L0=tkinter.Label(opciones,image= myImg).grid(row=0,column=0,columnspan=2)
    #opciones.geometry('400x300')

    L1=tkinter.Label(opciones, text ='x inicial :').grid(row=1,column=0)
    x_inicial = tkinter.Entry(opciones)
    x_inicial.grid(row =1,column=1)

    L2=tkinter.Label(opciones, text ='x final :').grid(row=2,column=0)
    x_final = tkinter.Entry(opciones)
    x_final.grid(row =2,column=1)

    L3=tkinter.Label(opciones, text ='Numero de nodos sin contar fronteras :').grid(row=3,column=0)
    Nodos = tkinter.Entry(opciones)
    Nodos.grid(row =3,column=1)

    L4=tkinter.Label(opciones, text ='Temperatura en la frontera A      : A =  :').grid(row=4,column=0)
    Ta = tkinter.Entry(opciones)
    Ta.grid(row =4,column=1)

    L5=tkinter.Label(opciones, text ='Temperatura en la frontera B      : B =  :').grid(row=5,column=0)
    Tb = tkinter.Entry(opciones)
    Tb.grid(row =5,column=1)

    L6=tkinter.Label(opciones, text ='f  :').grid(row=6,column=0)
    f = tkinter.Entry(opciones)
    f.grid(row = 6,column=1)

    

    diccionario={'x_inicial' : x_inicial, 'x_final' : x_final, 'Nodos' : Nodos, 'Ta' : Ta, 'Tb' :Tb, 'f' : f}

    Calcular = tkinter.Button(opciones, text = 'Calcular', command=lambda: Proceso2(diccionario)).grid(row=7)
    

    opciones.mainloop()
    pass


    
def opcion3(ventana):
    """
    docstring
    """

    opciones = tkinter.Toplevel(ventana)
    opciones.title('Conduccion de calor condicion Neumman')

    for i in range(10):
        opciones.rowconfigure(i,weight=1)
    # for i in range(1):
    #     opciones.columnconfigure(i,weight=1)
    opciones.columnconfigure(0,weight=1)
    opciones.columnconfigure(1,weight=1)
    

    myImg=Image.open('Numman.png')
    myImg= myImg.resize((300,150))
    myImg=ImageTk.PhotoImage(myImg)
    
    L0=tkinter.Label(opciones,image= myImg).grid(row=0,column=0,columnspan=2)
    #opciones.geometry('400x300')

    L1=tkinter.Label(opciones, text ='x inicial :').grid(row=1,column=0)
    x_inicial = tkinter.Entry(opciones)
    x_inicial.grid(row =1,column=1)

    L2=tkinter.Label(opciones, text ='x final :').grid(row=2,column=0)
    x_final = tkinter.Entry(opciones)
    x_final.grid(row =2,column=1)

    L3=tkinter.Label(opciones, text ='Numero de nodos sin contar fronteras :').grid(row=3,column=0)
    Nodos = tkinter.Entry(opciones)
    Nodos.grid(row =3,column=1)

    L4=tkinter.Label(opciones, text ='Temperatura en la frontera A      : A =  :').grid(row=4,column=0)
    Ta = tkinter.Entry(opciones)
    Ta.grid(row =4,column=1)

    L5=tkinter.Label(opciones, text ='Temperatura en la frontera B      : B =  :').grid(row=5,column=0)
    Tb = tkinter.Entry(opciones)
    Tb.grid(row =5,column=1)

    L6=tkinter.Label(opciones, text ='Conductividad termica kappa  :').grid(row=6,column=0)
    kappa = tkinter.Entry(opciones)
    kappa.grid(row = 6,column=1)

    L7=tkinter.Label(opciones, text ='Fuente (-) o sumidero Q (+) \n Comando de Python en funcion del dominio x\n ejemplo: np.exp(x)').grid(row=7,column=0)
    Q = tkinter.Entry(opciones)
    Q.grid(row = 7,column=1)

    L8=tkinter.Label(opciones, text ='Tipo de condicion').grid(row=8,column=0)
    variable = tkinter.StringVar(opciones)
    Tipo = tkinter.OptionMenu(opciones, variable,'izquierda', 'derecha')
    Tipo.grid(row = 8,column=1)
    

    diccionario={'x_inicial' : x_inicial, 'x_final' : x_final, 'Nodos' : Nodos, 'Ta' : Ta, 'Tb' :Tb, 'kappa' : kappa, 'Q' : Q, 'Tipo' : variable}

    Calcular = tkinter.Button(opciones, text = 'Calcular', command=lambda: Proceso3(diccionario)).grid(row=9)
    

    opciones.mainloop()
    
def opcion4(ventana):
    """
    docstring
    """

    opciones = tkinter.Toplevel(ventana)
    opciones.title('Conduccion de calor conductividad variable')

    for i in range(9):
        opciones.rowconfigure(i,weight=1)
    # for i in range(1):
    #     opciones.columnconfigure(i,weight=1)
    opciones.columnconfigure(0,weight=1)
    opciones.columnconfigure(1,weight=1)
    

    myImg=Image.open('Conduc_variable.png')
    myImg= myImg.resize((300,150))
    myImg=ImageTk.PhotoImage(myImg)

    L0=tkinter.Label(opciones,image= myImg).grid(row=0,column=0,columnspan=2)
    #opciones.geometry('400x300')

    L1=tkinter.Label(opciones, text ='x inicial :').grid(row=1,column=0)
    x_inicial = tkinter.Entry(opciones)
    x_inicial.grid(row =1,column=1)

    L2=tkinter.Label(opciones, text ='x final :').grid(row=2,column=0)
    x_final = tkinter.Entry(opciones)
    x_final.grid(row =2,column=1)

    L3=tkinter.Label(opciones, text ='Numero de nodos sin contar fronteras :').grid(row=3,column=0)
    Nodos = tkinter.Entry(opciones)
    Nodos.grid(row =3,column=1)

    L4=tkinter.Label(opciones, text ='Temperatura en la frontera A      : A =  :').grid(row=4,column=0)
    Ta = tkinter.Entry(opciones)
    Ta.grid(row =4,column=1)

    L5=tkinter.Label(opciones, text ='Temperatura en la frontera B      : B =  :').grid(row=5,column=0)
    Tb = tkinter.Entry(opciones)
    Tb.grid(row =5,column=1)

    L6=tkinter.Label(opciones, text ='Conductividad termica kappa variable \nComando de python en funcion de x  :').grid(row=6,column=0)
    kappa = tkinter.Entry(opciones)
    kappa.grid(row = 6,column=1)

    L7=tkinter.Label(opciones, text ='Fuente (-) o sumidero Q (+)').grid(row=7,column=0)
    Q = tkinter.Entry(opciones)
    Q.grid(row = 7,column=1)

    
    

    diccionario={'x_inicial' : x_inicial, 'x_final' : x_final, 'Nodos' : Nodos, 'Ta' : Ta, 'Tb' :Tb, 'kappa' : kappa, 'Q' : Q, }

    Calcular = tkinter.Button(opciones, text = 'Calcular', command=lambda: Proceso4(diccionario)).grid(row=8)
    

    opciones.mainloop()

def Contacto():
    """
    docstring
    """
    messagebox.showinfo('Creadores', 'Creado por : \n Alan de la Fuente Bonfil \n Abraham Flores Miranda \n José Daniel Rosas Avila \n Github: https://github.com/DanielR59/Conduccion_de_Calor')
