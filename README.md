# Firmas-electronicas
Proyecto de Firmas Electrónicas en Python

- Para la ejecución del código, se necesita tener instalado Python-Docx, para esto se debe ejecutar 'pip install python-docx'
- Ejecutar el Archivo "intefaz.py"


Para firmar:

- Requisitos: Ingresar el nombre del documento, el documento, una clave publica y el Token. 
- El Token debe contener: Un archivo txt con su clave privada, y un estampado para el documento.
- Una vez ingresado todos los datos, y presionado el botón de firmar, el documento será estampado, y la información
será almacenada en la tabla hash de la siguiente forma:
    - El nombre del documento retornará un ID para indicar donde almacenar el arreglo.
    - Se obtendrá todo el texto del documento, y con esto se generará un algoritmo Hash.
    - Se encriptará la clave publica y privada, y se almacenará todo de la siguiente forma en un arreglo:

[Hash del documento, clave publica encriptada, clave privada encriptada]
Ejemplo: [d0c9eff4652915959b306d7e668baaa3, fffff, aaaaa]

----------------------------------------------------------------------------------------------------------------------

Para acceder al documento:

- Requisitos: Ingresar el nombre del documento, el documento, y la clave publica.
- El usuario debe ingresar todos los requisitos, una vez ingresados, se obtendrá el índice de la tabla hash con el nombre del documento
y se comprobará la información almacenada de la siguiente forma:
    - Se tomará el archivo ingresado por el usuario, y se obrendrá un hash de dicho documento:
        - Si el hash coincide con el hash almacenado, significa que el documento no ha sufrido cambios.
        - Si el hash no coincide, significa que el documento sufrió cambios, por lo tanto el documento es invalidado legalmente.
    - También se verificará la clave publica:
        - Si la clave publica coincide con la clave publica almacenada, significa que existe un acceso válido al documento.
        - Si no coincide, significa que no contamos con acceso comprobado al documento, invalidando legalmente el uso de este documento para el usuario.
- Si los datos coinciden, significa que poseemos acceso legal al documento.

----------------------------------------------------------------------------------------------------------------------

Para verificar una firma:

- Requisitos: Nombre del documento, documento y Token.
- El usuario ingresa el nombre del documento, y con esto se obtendrá el índice de la tabla hash.
- Una vez localizado el archivo, se continúa a verificar la integridad de la información:
    - Se tomará el archivo ingresado por el usuario, y se obrendrá un hash de dicho documento:
        - Si el hash coincide, significa que el documento no ha recibido ningún cambio no deseado.
        - Si el hash no coincide, significa que ha existido un cambio del archivo. El cliente puede elegir revisar el archivo para volver a firmarlo, o denegar el archivo, provocando que sea eliminado del sistema.
    - También se verificará la clave privada:
        - Si la clave privada es correcta, significa que el usuario, es la persona legal tras la firma de dicho documento.
        - Si la clave privada es incorrecta, significa que el usuario no es el dueño legal de la firma del documento.
- Si los datos coinciden, significa que el usuario verifica con éxito la firma de dicho documento.


