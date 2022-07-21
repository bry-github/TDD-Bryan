def increment_by_one(i):
    return i + 1

def test_increment():
    assert increment_by_one(1) == 2

def decrement_by_one(i):
    return i - 1

def test_decrement():
    assert decrement_by_one(1) == 0
