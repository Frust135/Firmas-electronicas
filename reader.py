from shutil import copyfile #Función para copiar archivos
from docx import Document #Pip install python-docx
from docx.shared import Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import hashlib
import docx

#-----------------------------------------
#         Lector de USB
#-----------------------------------------

def usbReader():
    clave_privada = None
    try:
        with open('E:/token.txt', 'r') as file:
            clave_privada = file.read()
            return clave_privada
    except:
        print("Error al obtener el Token del USB, intente nuevamente.")
        return None
        
#-----------------------------------------
#         Firma el documento
#-----------------------------------------

def estamparDocumento(directorio_documento, nombre_archivo, estampado):
    try:
        path = r'./files/'+nombre_archivo+'.docx'
        documento = Document(directorio_documento)
        firma = documento.add_paragraph() #Crea un párrafo
        firma.alignment=  WD_PARAGRAPH_ALIGNMENT.RIGHT #Y lo alinea a la derecha
        ejecutar = firma.add_run("") 
        ejecutar.add_picture(estampado, width=Inches(1.75)) #Y se añade la imagen al párrafo
        documento.save(path)
    except:
        print("Error al firmar el documento.")

#-----------------------------------------
#         Obtener texto de todo el documento
#-----------------------------------------

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return fullText

#print(getText("documento-firmado.docx"))

#-----------------------------------------
#         Obtener el hash del documento
#-----------------------------------------

hash_md5 = hashlib.md5() 
documento = getText("documento-firmado.docx")
texto = documento[1]
hash_md5.update(texto.encode())
print (hash_md5.hexdigest())

