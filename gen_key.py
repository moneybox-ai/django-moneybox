from io import StringIO

from tink import daead, new_keyset_handle, JsonKeysetWriter, cleartext_keyset_handle

daead.register()

key_template = daead.deterministic_aead_key_templates.AES256_SIV
keyset_handle = new_keyset_handle(key_template)
string_out = StringIO()
writer = JsonKeysetWriter(string_out)
cleartext_keyset_handle.write(writer, keyset_handle)
serialized_keyset = string_out.getvalue()
print(serialized_keyset)
