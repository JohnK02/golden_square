from lib.gratitudes import *

def test_gratitudes_returns_correct_string():
    gratitudes = Gratitudes()
    gratitudes.add("dogs")
    result = gratitudes.format()
    assert result == "Be grateful for: dogs"