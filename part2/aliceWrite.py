import sys
import base64
from cryptography.hazmat.backends import default_backend, interfaces
from cryptography.hazmat.primitives import serialization, asymmetric, hashes


def loadKey(key):
    return serialization.load_pem_public_key(
        key,
        backend=default_backend()
    )


def encryptMessage(publicKey, message):
    return publicKey.encrypt(
        message,
        asymmetric.padding.OAEP(
            mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )

# Read message from the command line arg.
try:
    message = sys.argv[1]
    if(len(message)>18):
        print("message is too long")
        exit()
except IndexError:
    print "Give me a message to proceed"
    exit()

bobPubKeyFileName = "bobKeys/id_rsa.pub"
outputFileName = "ctext"

# Read bob's public key
try:
    with open(bobPubKeyFileName, 'r') as pubKeyFile:
        pubKey = pubKeyFile.read()
except IOError:
    print("Couldn't find " + "\"" + bobPubKeyFileName +
           "\"")
    exit()

# Encrypt the message
try:
    with open(outputFileName, 'w') as messageOut:
        encryptedMessage = encryptMessage(loadKey(pubKey), message)
        encryptedMessage = base64.b64encode(encryptedMessage)
        messageOut.write(encryptedMessage)
        print("The cipher text is: \n" + encryptedMessage)
except IOError:     
    print ("Couldn't write to the file " + outputFileName)
    exit()