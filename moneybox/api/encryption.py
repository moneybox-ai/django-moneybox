from moneybox.settings import PRIMITIVE


def encrypt_token(token):
    ciphertext = PRIMITIVE.encrypt_deterministically(token, b"associated_data")
    return ciphertext


def decrypt_ciphertext(ciphertext):
    decrypted_text = PRIMITIVE.decrypt_deterministically(ciphertext, b"associated_data")
    return decrypted_text.decode()
