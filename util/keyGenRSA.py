from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import sys

private_key = rsa.generate_private_key(
    public_exponent=65537, key_size=2048, backend=default_backend()
)

def generatePrivateKey():
    return private_key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.TraditionalOpenSSL, serialization.NoEncryption())
def generatePublicKey():
    return private_key.public_key().public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)

try:
    pubFileName=sys.argv[2]
except IndexError:
    pubFileName = 'id_rsa.pub'

try:
    privateFileName=sys.argv[1]
except IndexError:
    privateFileName = 'id_rsa'

with open(pubFileName, 'wb') as file:
    file.write(generatePublicKey())
with open(privateFileName, 'wb') as file:
    file.write(generatePrivateKey())
