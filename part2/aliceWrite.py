import sys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
try:
    message=sys.argv[1]
except IndexError:
    print "Give me a message to proceed"
    exit()

## Encrypt a message for bob
aliceKeyFileName="aliceKeys/id_rsa"
bobPubKeyFileName="bobsKeys/id_rsa.pub"
with open(aliceKeyFileName) as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )
    