from cryptography.fernet import Fernet
import sys
def generateKey():
    return Fernet.generate_key()

try:
    outputFlie = sys.argv[1]
except IndexError:
    print "Provide an output file as a command line argument."
    exit()
with open(outputFlie, "wb") as file:
    file.write(generateKey())