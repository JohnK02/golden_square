from lib.counter import *

def test_counter_to_count_to_seven():
    counter = Counter()
    counter.add(7)
    result = counter.report()
    assert result == "Counted to 7 so far."