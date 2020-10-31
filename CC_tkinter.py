#import numpy as np
import tkinter
#from tkinter import messagebox
# from graficas import *
# from matriz import solucion_sistema1D, solucion_sistema1D_Poisson, solucion_sistema1D_Neumann,solucion_sistema_conductividad_variable
#from Parametros import get_Parametros_basicos
# from PIL import Image,ImageTk
from funciones_tkinter import *

ventana = tkinter.Tk()
ventana.geometry("400x300")
my_menu = tkinter.Menu(ventana)
ventana.config(menu = my_menu)

contact_Menu= tkinter.Menu(my_menu)
my_menu.add_cascade(label = 'Ayuda', menu = contact_Menu)
contact_Menu.add_command(label = 'Contacto',command = Contacto )



etiqueta = tkinter.Label(ventana, text='Conduccion de calor', bg='red')
etiqueta.pack(fill = tkinter.X)

boton1 = tkinter.Button(ventana, text = 'Conduccion de calor estacionaria, conductividad constante', padx=20,pady=20, command =lambda : opcion1(ventana))
boton1.pack(fill=tkinter.BOTH)

boton2 = tkinter.Button(ventana, text = 'Conduccion de calor, ecuacion de Poisson condicion tipo Dirichlet', padx=20,pady=20, command=lambda : opcion2(ventana))
boton2.pack(fill=tkinter.BOTH)

boton3 = tkinter.Button(ventana, text = 'Conduccion de calor, ecuacion de Poisson condicion tipo Neumman', padx=20,pady=20, command = lambda :opcion3(ventana))
boton3.pack(fill=tkinter.BOTH)

boton4 = tkinter.Button(ventana, text = 'Conduccion de calor, ecuacion de Poisson conductividad no constante', padx=20,pady=20, command = lambda : opcion4(ventana))
boton4.pack(fill=tkinter.BOTH)



ventana.mainloop()



