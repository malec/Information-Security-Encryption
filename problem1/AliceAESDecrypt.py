from cryptography.fernet import Fernet

print "Reading an encrypted message from message.txt using sharedKey.txt"

# Reading sharedKey.txt
fileSharedKey = open("sharedKey.txt", "rb")
sharedKey = fileSharedKey.read()
fileSharedKey.close()

# Reading message.txt
fileMessage = open("message.txt", "rb")
message = fileMessage.read()
fileMessage.close()

# Writing result to result.txt
fileResult = open("result.txt", "w")
fileResult.write(Fernet(sharedKey).decrypt(message))
fileResult.close()

print "Done."