from cryptography.fernet import Fernet
import sys
print("Writing an encypted message to message.txt for alice using sharedKey.txt")

# Reading bob's key from sharedKey.txt
fileBobsKey = open("sharedKey.txt","rb")
bobskey = fileBobsKey.read()
fileBobsKey.close()

# Writing encrypted message to message.txt
message = sys.argv[1]

encryptedMessage = Fernet(bobskey).encrypt(message)
fileBobsMessage = open("message.txt",   "wb")
fileBobsMessage.write(encryptedMessage)
fileBobsMessage.close()

print("Done.")