import sys, base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac
keyFileName = "key"

# Read message from args
try:
    message = sys.argv[1]
    if(len(message) > 18):
        print("message is too long")
        exit()
except IndexError:
    print "Give me a message to proceed"
    exit()

# Load key file
try:
    with open(keyFileName, 'r') as keyFile:
        key = base64.b64decode(keyFile.read())
except IOError:
    print ("couldn't read the file named " + keyFileName)
    exit()

try:
    with open("mactext", 'w') as macFile:
        h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
        h.update(message)
        hmac = base64.b64encode(h.finalize())
        result = "{\"message\": \"" + message + "\", \"hmac\": \"" + hmac + "\"}"
        macFile.write(result)
except IOError:
    print "could not write the file"
    exit()