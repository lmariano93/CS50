from twttr import shorten

def test_twttr():
    assert shorten("word") == "wrd"
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("1234") == "1234"
    assert shorten("TEST") == "TST"




