from shutil import copyfile #Función para copiar archivos

#########################################
#         Lector de USB
#########################################

def usbReader():
    data = None
    try:
        with open('E:/token.txt', 'r') as file:
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
