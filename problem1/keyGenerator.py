from cryptography.fernet import Fernet
import sys
outputFlie = sys.argv[1]
file = open(outputFlie, "wb")
file.write(Fernet.generate_key())
file.close()
print("Done.")