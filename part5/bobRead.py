import base64, json
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

bobPubKeyFileName = "aliceKeys/id_rsa.pub"
def readFile():
    with open('sigtext', 'r') as sigFile:
        jsonText = sigFile.read()
        return json.loads(jsonText)
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
def verifySignature(pubKey, message, signature):
    try:
        verifier = pubKey.verifier(
            base64.b64decode(signature),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        verifier.update(bytes(message))
        verifier.verify()
        return True
    except InvalidSignature:
        return False

fileContentsAsObj = readFile()
if verifySignature(parsePubKey(loadKey(bobPubKeyFileName)), fileContentsAsObj['message'], fileContentsAsObj['signature']):
     print 'Success'
else:
    print "Invalid signature"
