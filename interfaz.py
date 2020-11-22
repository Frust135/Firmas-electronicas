from tkinter import *

#-------------------------------------------------------------------
#      Creación ventana
#-------------------------------------------------------------------

myWindow = Tk()
myWindow.geometry("1270x450")
myWindow.title("Metodos de búsqueda")
myWindow['bg'] = '#060836'

Titulo=Label(text="Firma digital" ,font=("Cambria",15),fg="#060836" , bg="#703ABE", width="893", height="3")

Titulo.pack()

#-------------------------------------------------------------------
#      Box_1: Firmar documento
#-------------------------------------------------------------------
box1=Label(bg="#1E136E", width="40", height="21")
box1.place(x=25, y=100)

titulo_firmar_doc = Label(text = "Firmar documento", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
titulo_firmar_doc.place(x=25, y=100)

f=Frame(myWindow,height=1,width=260,bg="#1EEB74")
f.place(x=40, y=133)

nombre_archivo = Label(text = "Nombre del archivo", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
nombre_archivo.place(x=25, y=150)

#-------------------------------------------------------------------
#      Box_2: Obtener documento
#-------------------------------------------------------------------
box2=Label(bg="#1E136E", width="40", height="21")
box2.place(x=350, y=100)

#-------------------------------------------------------------------
#      Box_3: Revisar firma
#-------------------------------------------------------------------

box3=Label(bg="#1E136E", width="40", height="21")
box3.place(x=675, y=100)

myWindow.mainloop()