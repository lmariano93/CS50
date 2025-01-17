from numb3rs import validate


def test_valid_addresses():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("192.168.0.1") == True


def test_invalid_addresses():
    assert validate("256.100.50.25") == False
    assert validate("-1.0.0.0") == False
    assert validate("192.168.1") == False
    assert validate("192.168.0.1.1") == False
    assert validate("192.275.5.1") == False
    assert validate("192.168.abc.1") == False



