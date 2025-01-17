import pytest
from seasons import calculate_minutes, format_minutes

def test_calculate_minutes():
    assert calculate_minutes("1990-01-01") == 18362880
    assert calculate_minutes("2020-12-31") == 2059200
    with pytest.raises(SystemExit):
        calculate_minutes("1990/01/01")
    with pytest.raises(SystemExit):
        calculate_minutes("2024-02-30")

def test_format_minutes():
    assert format_minutes(18361440) == "Eighteen million, three hundred sixty-one thousand, four hundred forty minutes"
    assert format_minutes(2057760) == "Two million, fifty-seven thousand, seven hundred sixty minutes"
    assert format_minutes(0) == "Zero minutes"

