from lib.report_length import *

def test_report_length_is_correct():
    result = report_length("house")
    assert result == "This string was 5 characters long."