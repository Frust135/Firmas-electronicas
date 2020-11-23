from tkinter import *
from reader import *
#-------------------------------------------------------------------
#      Creación ventana
#-------------------------------------------------------------------

myWindow = Tk()
myWindow.geometry("1000x500")
myWindow.title("Metodos de búsqueda")
myWindow['bg'] = '#060836'

Titulo=Label(text="Firma digital" ,font=("Cambria",15),fg="#060836" , bg="#703ABE", width="893", height="3")

Titulo.pack()

#-------------------------------------------------------------------
#      Box_1: Firmar documento
#-------------------------------------------------------------------
box1=Label(bg="#1E136E", width="40", height="25")
box1.place(x=25, y=100)

titulo_firmar_doc = Label(text = "Firmar documento", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
titulo_firmar_doc.place(x=25, y=100)

f=Frame(myWindow,height=1,width=260,bg="#1EEB74")
f.place(x=40, y=133)

nombre_archivo = Label(text = "Nombre del archivo", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
nombre_archivo.place(x=25, y=150)

ingreso_nombre_archivo = Entry(width = "42",bg="#B6ADE4")
ingreso_nombre_archivo.place(x=40, y=180)

seleccion_archivo = Label(text = "Seleccion",font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
seleccion_archivo.place(x=25, y= 220)

boton_seleccion_archivo =  Button(myWindow, text = "Seleccione el archivo" ,width="35", bg="#B6ADE4", command= lambda: openFile(myWindow))
boton_seleccion_archivo.place(x=40, y=250)

clave_publica = Label(text = "Ingrese clave publica",font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
clave_publica.place(x=25, y=295)

ingreso_clave_publica = Entry(width = "42", bg="#B6ADE4")
ingreso_clave_publica.place(x=40, y=325)

insertar_token = Label(text = "Inserte su token",font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
insertar_token.place(x=25, y=370)

boton_insercion_token = Button(myWindow, text = "Firmar", width="35", bg="#B6ADE4")
boton_insercion_token.place(x=40, y=400)
#-------------------------------------------------------------------
#      Box_2: Obtener documento
#-------------------------------------------------------------------
box2=Label(bg="#1E136E", width="40", height="25")
box2.place(x=350, y=100)

#-------------------------------------------------------------------
#      Box_3: Revisar firma
#-------------------------------------------------------------------

box3=Label(bg="#1E136E", width="40", height="25")
box3.place(x=675, y=100)

myWindow.mainloop()