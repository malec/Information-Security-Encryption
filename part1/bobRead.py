from cryptography.fernet import Fernet

print "Printing an encrypted message from message.txt using key.txt"

# Reading key.txt
with open("key.txt", "rb") as fileKey:
    key = fileKey.read()

# Reading message.txt
with open("message.txt", "rb") as fileMessage:
    message = fileMessage.read()

result = Fernet(key).decrypt(message)
print ("The message is: \n" + result)