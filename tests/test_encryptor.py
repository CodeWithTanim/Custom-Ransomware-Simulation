import os
from src import encryptor, utils

def test_encrypt_decrypt():
    key = utils.generate_key()
    sandbox_file = "sandbox/sample_text.txt"
    encryptor.encrypt_file(sandbox_file, key)
    from src import decryptor
    decryptor.decrypt_file(sandbox_file + ".aes", key)
    assert os.path.exists(sandbox_file)
