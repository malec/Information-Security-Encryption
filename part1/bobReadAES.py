from cryptography.fernet import Fernet
import sys

print "Printing an encrypted message from message.txt using key.txt"

try:
    fileName = sys.argv[1]
except IndexError:
    fileName = "key.txt"

# Read file
with open(fileName, "rb") as fileKey:
    key = fileKey.read()

# Reading message.txt
with open("message.txt", "rb") as fileMessage:
    message = fileMessage.read()

print ("The ciphertext is:\n" + message)

result = Fernet(key).decrypt(message)
print ("The plaintext is:\n" + result)