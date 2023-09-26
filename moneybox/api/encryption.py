import json
import os
import tink

from tink import cleartext_keyset_handle
from tink import daead

daead.register()


pre_keyset = {
    "key": [
        {
            "keyData": {
                "keyMaterialType": os.getenv("KEY_MATERIAL_TYPE"),
                "typeUrl": os.getenv("TYPE_URL"),
                "value": os.getenv("VALUE"),
            },
            "keyId": os.getenv("KEY_ID"),
            "outputPrefixType": os.getenv("OUTPUT_PREFIX_TYPE"),
            "status": os.getenv("STATUS"),
        }
    ],
    "primaryKeyId": os.getenv("PRIMARY_KEY_ID"),
}
keyset = json.dumps(pre_keyset, indent=4)
keyset_handle = cleartext_keyset_handle.read(tink.JsonKeysetReader(keyset))
primitive = keyset_handle.primitive(daead.DeterministicAead)


def encrypt_token(token):
    ciphertext = primitive.encrypt_deterministically(token, b"associated_data")
    return ciphertext


def decrypt_ciphertext(ciphertext):
    decrypted_text = primitive.decrypt_deterministically(ciphertext, b"associated_data")
    return decrypted_text.decode()
