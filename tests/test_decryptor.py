import os
from src import decryptor, utils

def test_decrypt():
    key = utils.load_key()
    sandbox_file = "sandbox/sample_text.txt.aes"
    decryptor.decrypt_file(sandbox_file, key)
    assert os.path.exists(sandbox_file[:-4])
