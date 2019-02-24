import sys
import time
import datetime
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend, interfaces
from cryptography.hazmat.primitives import serialization, asymmetric, hashes


File_Name_AES_Key = "key"
File_Name_RSA_Key = "id_rsa"
File_Name_RSA_Pub_Key = "id_rsa.pub"
count = 100

# Load Message
try:
    message = sys.argv[1]
    if(len(message) > 7):
        print("Length must be less than 7 bytes")
        exit()
except IndexError:
    print("You need to provide a message to encrypt")
    exit()

# Load AES Key
try:
    with open(File_Name_AES_Key, 'rb') as keyFile:
        AES_Key = keyFile.read()
except IOError:
    print "couldn't read the file"
    exit()

# Start stopwatch to measure AES performance
AES_start_time = time.time()

# AES Encrypt and Decrypt count times
for x in range(0, count):
    Fernet(AES_Key).decrypt(Fernet(AES_Key).encrypt(message))
    

AES_end_time = time.time()

# calculate average time
AES_uptime = AES_end_time - AES_start_time
AES_average_time = str(datetime.timedelta(seconds=(AES_uptime/count)))

# Load a public key
try:
    with open(File_Name_RSA_Pub_Key, 'rb') as keyFile:
        RSA_Pub_Key = keyFile.read()
except IOError:
    print "couldn't read the file"
    exit()

RSA_Pub_Key = serialization.load_pem_public_key(
    RSA_Pub_Key,
    backend=default_backend()
)

# Load a private key
try:
    with open(File_Name_RSA_Key, 'rb') as keyFile:
        RSA_Key = keyFile.read()
except IOError:
    print "couldn't read the file"
    exit()

RSA_Key = serialization.load_pem_private_key(
    RSA_Key,
    password=None,
    backend=default_backend()
)
# Start stopwatch to measure RSA performance
RSA_start_time = time.time()
# RSA Encrypt and Decrypt count times
for x in range(0, count):
    # do encryption and decryption
    RSA_Key.decrypt(
        RSA_Pub_Key.encrypt(
            message,
            asymmetric.padding.OAEP(
                mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA1()),
                algorithm=hashes.SHA1(),
                label=None
            )
        ),
        asymmetric.padding.OAEP(
            mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )

RSA_end_time = time.time()
RSA_uptime = RSA_end_time - RSA_start_time
RSA_average_time = str(datetime.timedelta(seconds=(RSA_uptime/count)))

# Print Averages
print("Average AES encryption and decryption time (H:MM:SS): " + AES_average_time)
print("Average RSA encryption and decryption time (H:MM:SS): " + RSA_average_time)
