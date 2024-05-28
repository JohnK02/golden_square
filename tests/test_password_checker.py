import pytest
from lib.password_checker import *

def test_check_password_is_valid():
    password = PasswordChecker()
    assert password.check("Password") == True

def test_check_password_not_valid():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("abc")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."