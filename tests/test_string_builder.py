from lib.string_builder import *

def test_string_builder_returns_length_and_new_string():
    string = StringBuilder()
    string.add("John")
    size = string.size()
    assert size == 4
    result = string.output()
    assert result == "John"