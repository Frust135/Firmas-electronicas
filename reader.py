from shutil import copyfile #Función para copiar archivos
import hashlib
import docx

#########################################
#         Lector de USB
#########################################

def usbReader():
    data = None
    try:
        with open('D:/token.txt', 'r') as file:
            data = file.read()
            return data
    except:
        print("Error al obtener el Token del USB, intente nuevamente.")
        return None
        
#########################################
#         Copia de Archivos
#########################################
def fileCopy(directory): #Recibe el directorio del archivo a copiar
    path = r'./files/test.txt'
    copyfile(directory, path)

#############################################
#         Obtener texto de todo el documento
#############################################

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return fullText

#print(getText("documento-firmado.docx"))

#############################################
#         Obtener el hash del documento
#############################################

hash_md5 = hashlib.md5() 
documento = getText("documento-firmado.docx")
texto = documento[1]
hash_md5.update(texto.encode())
print (hash_md5.hexdigest())

