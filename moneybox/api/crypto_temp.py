import tink

from tink import cleartext_keyset_handle
from tink import daead

daead.register()


keyset = r"""{
        "key": [{
            "keyData": {
                "keyMaterialType":
                    "SYMMETRIC",
                "typeUrl":
                    "type.googleapis.com/google.crypto.tink.AesSivKey",
                "value":
                    "EkAl9HCMmKTN1p3V186uhZpJQ+tivyc4IKyE+opg6SsEbWQ/WesWHzwCRrlgRuxdaggvgMzwWhjPnkk9gptBnGLK"
            },
            "keyId": 1919301694,
            "outputPrefixType": "TINK",
            "status": "ENABLED"
        }],
        "primaryKeyId": 1919301694
    }"""
keyset_handle = cleartext_keyset_handle.read(tink.JsonKeysetReader(keyset))
primitive = keyset_handle.primitive(daead.DeterministicAead)


def encrypt_token(token):
    ciphertext = primitive.encrypt_deterministically(token, b"associated_data")
    return ciphertext  # <class 'bytes'>


def decrypt_ciphertext(ciphertext):
    # <class 'bytes'>
    decrypted_text = primitive.decrypt_deterministically(ciphertext, b"associated_data")
    return decrypted_text.decode()
