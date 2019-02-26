import base64, sys, time, datetime
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac

count = 100

# Load key
keyFileName = "key"
try:
    with open(keyFileName, 'r') as keyFile:
        key = base64.b64decode(keyFile.read())
except IOError:
    print ("couldn't read the file named " + keyFileName)
    exit()

# Load Message
try:
    message = sys.argv[1]
    if(len(message) > 7):
        print("Length must be less than 7 bytes")
        exit()
except IndexError:
    print("You need to provide a message to encrypt")
    exit()

hmacStartTime = time.time()
for x in range(0, count):
    # Make signature
    instance = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
    instance.update(message)
    instance.finalize()
hmacStopTime = time.time()

hmacUptime = hmacStopTime - hmacStartTime
hmacAverageTime = str(datetime.timedelta(seconds=hmacUptime/count))
print("Average HMAC generation time (H:MM:SS): " + hmacAverageTime)
