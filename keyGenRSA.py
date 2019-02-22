from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import sys

private_key = rsa.generate_private_key(
    public_exponent=65537, key_size=2048, backend=default_backend()
)

with open(sys.argv[1], 'wb') as file:
    file.write(private_key.public_key().public_bytes('utf-8', serialization.PublicFormat.SubjectPublicKeyInfo))
