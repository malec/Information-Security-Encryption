import base64
import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.exceptions import InvalidSignature
keyFileName = "key"

# Load key file
try:
    with open(keyFileName, 'r') as keyFile:
        key = base64.b64decode(keyFile.read())
except IOError:
    print ("couldn't read the file named " + keyFileName)
    exit()

# Load message file
try:
    with open('mactext', 'r') as messageFile:
        messageJSON = messageFile.read()
        macText = json.loads(messageJSON)
        message = bytes(macText['message'])
        messageHMAC = base64.b64decode(macText['hmac'])
except IOError:
    print ("couldn't read mactext")
    exit()

# Verify message
try:
    h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
    h.update(message)
    h.verify(messageHMAC)
    print 'Success'
except InvalidSignature:
    print "Invalid signature"
