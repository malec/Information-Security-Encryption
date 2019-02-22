from cryptography.fernet import Fernet

print "Reading an encrypted message from message.txt using key.txt"

# Reading key.txt
with open("key.txt", "rb") as fileKey:
    key = fileKey.read()

# Reading message.txt
with open("message.txt", "rb") as fileMessage:
    message = fileMessage.read()

# Writing result to result.txt
with open("result.txt", "w") as fileResult:
    fileResult.write(Fernet(key).decrypt(message))

print "Done."