import sys
import base64
from cryptography.hazmat.primitives import serialization, asymmetric, padding, hashes
from cryptography.hazmat.backends import default_backend

alicePubKeyFileName = "aliceKeys/id_rsa.pub"
bobPubKeyFileName = "bobKeys/id_rsa.pub"
aliceKeyFileName = "aliceKeys/id_rsa"


def getMessage():
    try:
        if(len(sys.argv[1]) > 18):
            print "message must be less than 19 bytes"
            exit()
        return sys.argv[1]
    except IndexError:
        print "Provide a message"
        exit()
def loadKey(fileName):
    try:
        with open(fileName, 'r') as file:
            return file.read()
    except IOError:
        print("Couldn't find " + "\"" + fileName +
              "\"")
        exit()
def parsePubKey(text):
    return serialization.load_pem_public_key(
        text,
        backend=default_backend()
    )
def parseKey(text):
    return serialization.load_pem_private_key(
        text,
        password=None,
        backend=default_backend()
    )
def write(message, sig):
    try:
        result = "{\"message\": \"" + message + "\", \"signature\": \"" + sig + "\"}"
        with open("sigtext", 'w') as sigFile:
            sigFile.write(result)
    except IOError:
        print "couldn't write the file"
        exit()
# Load alice's public key
alicePubKey = parsePubKey(loadKey(alicePubKeyFileName))

# Read bob's public key
bobPubKey = parsePubKey(loadKey(bobPubKeyFileName))

# Load alice's private key
aliceKey = parseKey(loadKey(aliceKeyFileName))

# Get message
message = getMessage()

# RSA Sign message using private key to get sig
signer = aliceKey.signer(
    asymmetric.padding.PSS(
        mgf=asymmetric.padding.MGF1(hashes.SHA256()),
        salt_length=asymmetric.padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
signer.update(message)
sig = base64.b64encode(signer.finalize())

# print for grading
print("The RSA signature is:\n" + sig)

write(message, sig)
# Write message and sig to file sigtext