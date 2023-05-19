import base64
import os


def generate_encryption_key():
    """Generates a 256 bit (32 byte) AES encryption key and prints the
    base64 representation.

    """
    key = os.urandom(32)
    encoded_key = base64.b64encode(key).decode("utf-8")

    print(f"Base 64 encoded encryption key: {encoded_key}")