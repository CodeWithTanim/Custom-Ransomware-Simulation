from src import utils

def test_key_generation_and_loading():
    key = utils.generate_key()
    loaded_key = utils.load_key()
    assert key == loaded_key
