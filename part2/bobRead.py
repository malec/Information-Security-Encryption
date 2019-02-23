import base64
from cryptography.hazmat.primitives import serialization, asymmetric, hashes
from cryptography.hazmat.backends import default_backend
File_Name_Bob_Private_Key = "bobKeys/id_rsa"
File_Name_Decrypt = "ctext"


def deserializePrivateKey(data):
    return serialization.load_pem_private_key(
        data,
        password=None,
        backend=default_backend()
    )


# Read the private key file
try:
    with open(File_Name_Bob_Private_Key, 'rb') as keyFile:
        keyData = keyFile.read()
except IOError:
    print "couldn't read file " + File_Name_Bob_Private_Key
    exit()

private_key = deserializePrivateKey(keyData)

# Read the cipher text
try:
    with open(File_Name_Decrypt, 'r') as ctextFile:
        cipherText = base64.b64decode(ctextFile.read())
except IOError:
    print ("Couldn't read the file " + File_Name_Decrypt)
    exit()

plainText = private_key.decrypt(
    cipherText,
    asymmetric.padding.OAEP(
        mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA1()),
        algorithm=hashes.SHA1(),
        label=None
    )
)
print plainText