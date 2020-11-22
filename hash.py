from reader import getText
import hashlib

#-----------------------------------------
#         Obtener el hash del documento
#-----------------------------------------
def hash_documento(nombre_archivo):
    hash_md5 = hashlib.md5() 
    documento = getText(nombre_archivo)
    texto = documento[1]
    hash_md5.update(texto.encode())
    codigo_hash = hash_md5.hexdigest()
    return codigo_hash

print(hash_documento('documento-firmado'))