from cryptography.fernet import Fernet
import sys

keyFileName = 'key.txt'
messageOutFileName = "message.txt"
try:
    message=sys.argv[1]
except IndexError:
    print "You need to provide a message."
    exit()

# Reading alice's key
with open(keyFileName, "rb") as filealiceKey:
    alicekey = filealiceKey.read()

# Encrypt message
encryptedMessage = Fernet(alicekey).encrypt(message)

# Write Result
with open(messageOutFileName, "wb") as filealiceMessage:
    filealiceMessage.write(encryptedMessage)