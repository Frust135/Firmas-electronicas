from tkinter import Label, Button, messagebox, Tk, Frame, Entry, END
from reader import *
from hash import *
#-------------------------------------------------------------------
#      Creación de funciones
#-------------------------------------------------------------------
def insertar_hash(nombre_documento, elementos, tabla_hash):
    #Elementos: [path del documento, clave publica, clave privada]
    if elementos[2] == None: return messagebox.showerror(title="Token faltante", message="Ingrese su Token con su clave privada.")
    if elementos[1] == '': return messagebox.showerror(title="Clave publica faltante", message="Ingrese una clave publica.")
    try:
        directorio = elementos[0]
        elementos[0]=hash_documento(elementos[0])
        arreglo_retorno = hashing(nombre_documento, elementos, tabla_hash)
        tabla_hash = arreglo_retorno
        print(tabla_hash)
        estamparDocumento(directorio,nombre_documento,'E:/estampado.png')
        return messagebox.showinfo(title="Éxito", message="Documento almacenado con éxito.")
    except:
        return messagebox.showerror(title="Documento faltante", message="Ingrese un documento para firmar.")

def abrir_archivo(entry):
    path = openFile(myWindow)
    entry.insert(END, path)
#-------------------------------------------------------------------
#      Creación ventana
#-------------------------------------------------------------------

myWindow = Tk()
myWindow.geometry("985x500")
myWindow.title("Metodos de búsqueda")
myWindow['bg'] = '#060836'

tabla_hash = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
hash_texto = ''

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

nombre_archivo = Label(text = "Nombre archivo", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
nombre_archivo.place(x=25, y=150)

ingreso_nombre_archivo = Entry(width = "41",bg="#B6ADE4")
ingreso_nombre_archivo.place(x=40, y=180)

seleccion_archivo = Label(text = "Seleccion",font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
seleccion_archivo.place(x=25, y= 220)

boton_seleccion_archivo =  Button(myWindow, text = "Seleccione archivo" ,width="34", bg="#B6ADE4", command=lambda:abrir_archivo(nombre_ruta))
boton_seleccion_archivo.place(x=42, y=250)

nombre_ruta = Entry (width = "41",bg="#B6ADE4")
nombre_ruta.place(x=40, y = 285)

clave_publica = Label(text = "Clave publica",font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
clave_publica.place(x=25, y=310)

ingreso_clave_publica = Entry(width = "41", bg="#B6ADE4")
ingreso_clave_publica.place(x=40, y=340)

insertar_token = Label(text = "Inserte token",font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
insertar_token.place(x=25, y=385)

boton_insercion_token = Button(myWindow, text = "Firmar", width="34", bg="#B6ADE4", command=lambda: insertar_hash(ingreso_nombre_archivo.get(),[nombre_ruta.get(), ingreso_clave_publica.get(),usbReader()], tabla_hash))
boton_insercion_token.place(x=42, y=415)


#-------------------------------------------------------------------
#      Box_2: Obtener documento
#-------------------------------------------------------------------
box2=Label(bg="#1E136E", width="40", height="25")
box2.place(x=350, y=100)

titulo_obtener_documento = Label(text = "Obtener documento",font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
titulo_obtener_documento.place(x=355, y=100)

f1=Frame(myWindow,height=1,width=260,bg="#1EEB74")
f1.place(x=360, y=133)

nombre_archivo_2 = Label(text = "Nombre archivo",font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1") 
nombre_archivo_2.place(x=355, y=150)

ingreso_nombre_archivo_2 = Entry(width = "41",bg="#B6ADE4")
ingreso_nombre_archivo_2.place(x=370, y=180)

clave_publica_2 = Label(text = "Clave publica",font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
clave_publica_2.place(x=355, y=220)

boton_seleccion_archivo_2 =  Button(myWindow, text = "Seleccione el archivo" ,width="34", bg="#B6ADE4", command=lambda: openFile(myWindow))
boton_seleccion_archivo_2.place(x=372, y=250)

boton_obtener_documento = Button(myWindow, text = "Obtener documento", width="34", bg="#B6ADE4")
boton_obtener_documento.place(x=372, y=400)
#-------------------------------------------------------------------
#      Box_3: Revisar firma
#-------------------------------------------------------------------
box3=Label(bg="#1E136E", width="40", height="25")
box3.place(x=675, y=100)

titulo_revisar_firma = Label(text = "Revisar firma",font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
titulo_revisar_firma.place(x=680, y=100)

f2=Frame(myWindow,height=1,width=260,bg="#1EEB74")
f2.place(x=685, y=133)

nombre_archivo_3 = Label(text = "Nombre archivo",font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
nombre_archivo_3.place(x=680, y=150)

ingreso_nombre_archivo_3 = Entry(width = "41",bg="#B6ADE4")
ingreso_nombre_archivo_3.place(x=695, y=180)

insertar_token_3 = Label(text = "Inserte token",font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
insertar_token_3.place(x=680, y=220)

boton_revisar = Button(myWindow, text = "Revisar", width="34", bg="#B6ADE4")
boton_revisar.place(x=697, y=400)

myWindow.mainloop()