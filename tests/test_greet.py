from lib.greet import *

def test_greet_returns_correct_string():
    result = greet("John")
    assert result == 'Hello, John!'
