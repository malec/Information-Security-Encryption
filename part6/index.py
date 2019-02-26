import base64, sys, time, datetime
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac, asymmetric, serialization
from cryptography.hazmat.primitives.asymmetric import padding

count = 100
aliceKeyFileName = "id_rsa"
alicePubFileName = "id_rsa.pub"

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
hmacAverageTime = str(datetime.timedelta(seconds=hmacUptime / count))
print("Average HMAC generation time (H:MM:SS): " + hmacAverageTime)

rsaSigGenStartTime = time.time()
rsaSigGenEndTime = rsaSigGenStartTime

rsaSigVerStartTime = time.time()
rsaSigVerEndTime = rsaSigVerStartTime

def loadKey(fileName):
    try:
        with open(fileName, 'r') as file:
            return file.read()
    except IOError:
        print("Couldn't find " + "\"" + fileName +
              "\"")
        exit()
def parseKey(text):
    return serialization.load_pem_private_key(
        text,
        password=None,
        backend=default_backend()
    )
def parsePubKey(text):
    return serialization.load_pem_public_key(
        text,
        backend=default_backend()
    )
privateKey = parseKey(loadKey(aliceKeyFileName))
publicKey = parsePubKey(loadKey(alicePubFileName))

for x in range(0, count):
    tempGenStart = time.time()
    # Sign message
    signer = privateKey.signer(
        asymmetric.padding.PSS(
            mgf=asymmetric.padding.MGF1(hashes.SHA256()),
            salt_length=asymmetric.padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    signer.update(message)
    RSASignature = signer.finalize()
    # Done signing
    rsaSigGenEndTime += (time.time() - tempGenStart)

    tempVerStart = time.time()
    # Verify message
    verifier = publicKey.verifier(
            RSASignature,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
    verifier.update(bytes(message))
    verifier.verify()
    # Done verifying
    rsaSigVerEndTime += (time.time() - tempVerStart)

rsaSigGenUpTime = rsaSigGenEndTime - rsaSigGenStartTime
rsaSigGenAverageTime = str(datetime.timedelta(seconds=rsaSigGenUpTime / count))
print("Average RSA signature generation time (H:MM:SS): " + rsaSigGenAverageTime)

rsaSigVerUpTime = rsaSigVerEndTime - rsaSigVerStartTime
rsaSigVerAverageTime = str(datetime.timedelta(seconds = rsaSigVerUpTime / count))
print("Average RSA signature verification time (H:MM:SS): " + rsaSigVerAverageTime)