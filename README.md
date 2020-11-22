# Firmas-electronicas
Proyecto de Firmas Electrónicas en Python

Para firmar:

- El usuario ingresa el nombre del documento, y el documento.
- Debe ingresar el usb, el cual poseerá su firma (un logo de certificación) y su clave privada.
- Del nombre del documento: Se generará un ID de hash para saber donde almacenar el documento.
- De la clave privada: Se generará una clave pública que será mostrada al usuario a través de la interfaz, esta clave pública permite acceder
al documento.
- Al documento ingresado se le hará un append del logo de certificación al final del documento
- Del documento ingresado, se obtendrá todo el texto, y además se utilizará la clave pública con el fin de que con ambos datos se genere
una encriptación utilizando hash, este dato quedará almecenado en el índice que haya retornado el nombre del documento.
- Además aparte de almacenar todo la encriptación hash del documento, se realizará una encriptación de la clave privada del documento.

Ejemplo [Encriptación del documento + clave pública, clave privada] = [1x2r2f2w3ff, clave_privada]

Para acceder:

- El usuario debe ingresar el nombre del documento, y la clave pública.
- Si ambos elementos producen el mismo hash del documento, significa que tenemos acceso a dicho documento, y que dicho documento
no ha sido alterado.

Para confirmar la firma:

- En caso de confirmar la firma del sujeto en cuestión, debe ingresar el nombre del documento, junto a su token.
- Con el token, se comprobará si el documento posee la misma clave privada, de ser así, el usuario con el token
es el usuario que firmo dicho documento.
- Además, de la clave privada, se obtendrá la clave pública con la función de encriptación, y también se obtendrá la información
del documento, con el fin de generar un hash, y así comprobar si el documento que fue firmado, sigue siendo el mismo
documento, o si ha sufrido cambios, si el hash es el mismo, el documento sigue intacto, por el contrario, se supondrá
que el documento fue alterado.