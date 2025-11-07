from src.checksum import modulo11Checksum


def test_bad():
    assert not  modulo11Checksum("2-266-11156-8")
    assert not modulo11Checksum("1-563-9873X-X")

def test_good():
    assert  modulo11Checksum("2-266-11156-3")
    assert  modulo11Checksum("1-563-68745-X")
