from plates import is_valid

def test_isvalid_valid_cases():
    assert is_valid("AB123") == True
    assert is_valid("XYZ789") == True
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True

def test_isvalid_numbers_in_middle():
    assert is_valid("AB12C3") == False
    assert is_valid("ABC123D") == False
    assert is_valid("A1B2C3") == False

def test_isvalid_starting_with_invalid_numbers():
    assert is_valid("A0123") == False
    assert is_valid("12345") == False
    assert is_valid("AB0123") == False

def test_isvalid_invalid_characters_or_length():
    assert is_valid("A!") == False
    assert is_valid("A") == False
    assert is_valid("TOOLONG") == False
    assert is_valid("AB12!C") == False
    assert is_valid("") == False
