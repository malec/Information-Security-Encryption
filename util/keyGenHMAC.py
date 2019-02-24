from cryptography.fernet import Fernet
import sys, os, base64
def generateKey(length):
    return os.urandom(length)

try:
    outputFlie = sys.argv[1]
except IndexError:
    print "Provide an output file as a command line argument."
    exit()
with open(outputFlie, "w") as file:
    file.write(base64.b64encode(generateKey(16)))