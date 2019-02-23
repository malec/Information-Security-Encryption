from cryptography.fernet import Fernet
import sys
def generateKey():
    return Fernet.generate_key()

outputFlie = sys.argv[1]
with open(outputFlie, "wb") as file:
    file.write(generateKey())