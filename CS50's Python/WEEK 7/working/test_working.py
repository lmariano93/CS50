import pytest
from working import convert

def test_valid_inputs():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 PM to 11:59 PM") == "12:00 to 23:59"
    assert convert("1 AM to 1 PM") == "01:00 to 13:00"

def test_invalid_inputs():

    with pytest.raises(ValueError): convert("8:60 AM to 4:60 PM")
    with pytest.raises(ValueError): convert("13:00 PM to 5:00 PM")
    with pytest.raises(ValueError): convert("9 AM - 5 PM")
    with pytest.raises(ValueError): convert("10AMto5PM")
    with pytest.raises(ValueError): convert("12:00 to 13:00 PM")


