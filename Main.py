import tkinter

from tkinter import ttk
from tkinter.messagebox import showinfo

def mostrarOpcion(event):
    selectedMessage='Usted ha seleccionado la opción {}'.format(seleccionado.get())
    showinfo(title='selección',message = selectedMessage)

def salida(event):
    showinfo(title='Salida',message="Adios")
    window.quit()

window = tkinter.Tk()

lblSaludo= tkinter.Label(window, text='Por favor selecciona una opción')

seleccionado= tkinter.StringVar()
opc1 = ttk.Radiobutton(window, text='Opcion 1', value='1', variable=seleccionado)
opc2 = ttk.Radiobutton(window, text='Opcion 2', value='2', variable=seleccionado)
opc3 = ttk.Radiobutton(window, text='Opcion 3', value='3', variable=seleccionado)
btnSeleccionar= ttk.Button(window,text='Seleccionar')
btnSalir=ttk.Button(window,text='Salir')

lblSaludo.place(x=10,y=5)
opc1.place(x=10, y=30)
opc2.place(x=10, y=50)
opc3.place(x=10, y=70)
btnSeleccionar.place(x=10,y=100)
btnSalir.place(x=100, y=100)

btnSeleccionar.bind('<Button-1>',mostrarOpcion)
btnSalir.bind('<Button-1>',salida)


window.mainloop()
