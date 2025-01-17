from um import count

def test_basic_case():
    assert count("hello, um, world") == 1

def test_no_um():
    assert count("hello, world") == 0

def test_multiple_occurrences():
    assert count("um hello um") == 2

def test_um_as_substring():
    assert count("yummy") == 0

def test_case_insensitivity():
    assert count("UM, um, Um") == 3

def test_um_with_punctuation():
    assert count("hello, um! how are you? um.") == 2
