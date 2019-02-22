from cryptography.fernet import Fernet
import sys
outputFlie = sys.argv[1]
with open(outputFlie, "wb") as file:
    file.write(Fernet.generate_key())