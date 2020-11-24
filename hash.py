from reader import getText
import hashlib

#-----------------------------------------
#         Calcula el hash del documento
#-----------------------------------------
def hash_documento(nombre_archivo):
    hash_md5 = hashlib.md5() 
    documento = getText(nombre_archivo)
    texto = documento[1]
    hash_md5.update(texto.encode())
    codigo_hash = hash_md5.hexdigest()
    return codigo_hash

#-----------------------------------------
# Función que realiza el Doble Hash
#-----------------------------------------
def double_hash(h1 ,h2 ,arreglo):
    indice = h1
    aumentador = 1
    while arreglo[indice] != -1:
        indice = (h1 + aumentador* h2)%10     
        aumentador = aumentador+1       

    return indice
#-----------------------------------------
# Función que retorna el valor primo
#-----------------------------------------
def esPrimo(numero):
    contador = 0
    for iteracion_numero in range(1,numero+1,1):
        resto = numero % iteracion_numero
        if resto == 0:
            contador = contador+1

    if contador == 2:
        return 1
    else:
        return 0
#-----------------------------------------
# Función que retorna el número primo más cercano
#-----------------------------------------
def NumeroPrimoMasCercano(numero):
    ##recorrido menor a menor 
    for valor in range(numero,0,-1):
        primo = esPrimo(valor)
        if primo == 1:
            return valor
#-----------------------------------------
# Función Ascii (Retorna la suma del valor ascii de una palabra)
#-----------------------------------------
def get_ascii(palabra):
    arreglo_palabra=list(palabra)
    acumulador = 0
    for recorrido in range(0, len(arreglo_palabra)):
        acumulador+=ord(arreglo_palabra[recorrido])
    return acumulador

#-----------------------------------------
# Función que realiza el Hashing
#-----------------------------------------
def hashing(clave, valor, tabla_hash):
    nuevo_indice=''
    largo_hash = len(tabla_hash)
    indice_elemento=get_ascii(clave)%largo_hash
    indice = ("El indice de " +str(clave)+ " es: "+ str(indice_elemento))
    colision = ("No ha ocurrido ninguna colisión")
    while tabla_hash[indice_elemento]!=-1:
        colision = ("Ocurrió una colisión en el índice")
        numero_primo = NumeroPrimoMasCercano(largo_hash)
        calculo = int(get_ascii(clave)%numero_primo)
        ecuacion = numero_primo-calculo
        indice_elemento = double_hash(indice_elemento, ecuacion, tabla_hash)
        nuevo_indice=("El indice nuevo de "+str(clave)+ " es: "+str(indice_elemento))
    tabla_hash[indice_elemento] = valor
    return [tabla_hash,indice,colision, nuevo_indice]

#-----------------------------------------
# Función que realiza la busqueda
#-----------------------------------------
def busqueda(clave, valor, tabla_hash):
    largo_hash = len(tabla_hash)
    indice_elemento=get_ascii(clave)%largo_hash
    if tabla_hash[indice_elemento]!=valor:
        numero_primo = NumeroPrimoMasCercano(largo_hash)
        calculo = int(get_ascii(clave)%numero_primo)
        ecuacion = numero_primo-calculo
        for contador in range(1,20):
            indice_elemento = (indice_elemento + contador* ecuacion)%10 
            if tabla_hash[indice_elemento]==valor:
                return indice_elemento  
    return indice_elemento