from cryptography.fernet import Fernet
import sys
print("Writing an encypted message using key.txt to message.txt")

# Reading bob's key from key.txt
with open("key.txt","rb") as fileBobsKey:
    bobskey = fileBobsKey.read()

# Encrypt message
encryptedMessage = Fernet(bobskey).encrypt(sys.argv[1])

# Write Result
with open("message.txt",   "wb") as fileBobsMessage:
    fileBobsMessage.write(encryptedMessage)