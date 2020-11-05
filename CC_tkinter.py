#import numpy as np
import tkinter
import os
#from tkinter import messagebox
# from graficas import *
# from matriz import solucion_sistema1D, solucion_sistema1D_Poisson, solucion_sistema1D_Neumann,solucion_sistema_conductividad_variable
#from Parametros import get_Parametros_basicos
# from PIL import Image,ImageTk
from funciones_tkinter import *

#Creamos carpetas auxiliares
try:
    os.mkdir('Imagenes')
    os.mkdir('Soluciones')
except FileExistsError:
    pass
#
ventana = tkinter.Tk()
ventana.geometry("400x400")
ventana.iconbitmap('fire.ico')
ventana.title('Conduccion de calor 1D')

my_menu = tkinter.Menu(ventana)
ventana.config(menu = my_menu)

contact_Menu= tkinter.Menu(my_menu)
my_menu.add_cascade(label = 'Ayuda', menu = contact_Menu)
contact_Menu.add_command(label = 'Contacto',command = Contacto )



etiqueta = tkinter.Label(ventana, text='Conduccion de calor', bg='red')
etiqueta.pack(fill = tkinter.X, expand = True)

boton1 = tkinter.Button(ventana, text = 'Conduccion de calor estacionaria, conductividad constante', padx=20,pady=20, command =lambda : opcion1(ventana))
boton1.pack(fill=tkinter.BOTH, expand = True)

boton2 = tkinter.Button(ventana, text = 'Conduccion de calor, ecuacion de Poisson condicion tipo Dirichlet', padx=20,pady=20, command=lambda : opcion2(ventana))
boton2.pack(fill=tkinter.BOTH, expand = True)

boton3 = tkinter.Button(ventana, text = 'Conduccion de calor, ecuacion de Poisson condicion tipo Neumman', padx=20,pady=20, command = lambda :opcion3(ventana))
boton3.pack(fill=tkinter.BOTH, expand = True)

boton4 = tkinter.Button(ventana, text = 'Conduccion de calor, ecuacion de Poisson conductividad no constante', padx=20,pady=20, command = lambda : opcion4(ventana))
boton4.pack(fill=tkinter.BOTH, expand = True)

boton5 = tkinter.Button(ventana, text = 'Solución analitica',padx=20,pady=20, command = lambda : opcion5(ventana,))
boton5.pack(fill=tkinter.BOTH, expand = True)

ventana.mainloop()




