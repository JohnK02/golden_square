import pytest
from lib.present import *

def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap("Pony")
    assert present.unwrap() == "Pony"

def test_unwrapping_before_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_wrapping_already_wrapped():
    present = Present()
    present.wrap("Pony")
    with pytest.raises(Exception) as e:
        present.wrap("Pony")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped." 

def test_wrapping_already_wrapped_preserves_value():
    present = Present()
    present.wrap("Pony")
    with pytest.raises(Exception) as e:
        present.wrap("Horse")
    assert present.unwrap() == "Pony"