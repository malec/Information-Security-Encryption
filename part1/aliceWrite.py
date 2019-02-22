from cryptography.fernet import Fernet
import sys
print("Writing an encypted message using key.txt to message.txt")

# Reading alice's key from key.txt
with open("key.txt","rb") as filealiceKey:
    alicekey = filealiceKey.read()

# Encrypt message
encryptedMessage = Fernet(alicekey).encrypt(sys.argv[1])

# Write Result
with open("message.txt",   "wb") as filealiceMessage:
    filealiceMessage.write(encryptedMessage)