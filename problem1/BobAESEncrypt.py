from cryptography.fernet import Fernet

print "Writing an encypted message to message.txt for alice using sharedKey.txt"

# Reading bob's key from sharedKey.txt
fileBobsKey = open("sharedKey.txt","rb")
bobskey = fileBobsKey.read()
fileBobsKey.close()

# Writing encrypted message to message.txt
message = """Dear Alice: 

Here is a secret message. You have successfully decrypted it!

Sincerely,
Bob"""

encryptedMessage = Fernet(bobskey).encrypt(message)
fileBobsMessage = open("message.txt", "w")
fileBobsMessage.write(encryptedMessage)
fileBobsMessage.close()

print "Done."