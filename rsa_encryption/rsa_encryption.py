import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# generación de un par de llaves asimétricas
keyPair = RSA.generate(2048)

# escritura de llave privada a archivo 'rsa'
with open('rsa', 'wb') as f: # 'wb' abrir archivo para escritura en modo binario
    f.write(keyPair.export_key('PEM'))

# escritura de llave pública a archivo 'rsa.pub'
with open('rsa.pub', 'wb') as f:
    f.write(keyPair.publickey().export_key())

###########################################################################################

# se guarda la representación en bytes del texto
text = b'Este es el mensaje que se encriptara con la llave publica.'

# lectura de la llave pública con la que se encriptará el mensaje
publicKey = RSA.import_key(open('rsa.pub').read())

# encriptación del mensaje
cipherRSA = PKCS1_OAEP.new(publicKey)
encryptedText = cipherRSA.encrypt(text)

# escritura del texto encriptado a un archivo
with open('encrypted_text.txt', 'wb') as f:
    f.write(encryptedText)

###########################################################################################

# lectura de llave privada para desencriptar el mensaje
privateKey = RSA.import_key(open('rsa').read())

# lectura del texto encriptado del archivo
encryptedText = open('encrypted_text.txt', 'rb').read()

# se desencripta el mensaje y se muestra en pantalla
cipherRSA = PKCS1_OAEP.new(privateKey)
plainText = cipherRSA.decrypt(encryptedText)
print(plainText)