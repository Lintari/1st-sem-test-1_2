from src.bin_search import binSearch


def test_middle():
    assert binSearch([1, 2, 3, 4, 5], 4) == 3


def test_start():
    assert binSearch([1, 2, 3, 4], 2) == 1


def test_not_in_list():
    assert binSearch([1, 2, 3, 4], 5) == -1

def test_wrong_type():
    assert binSearch([1,2,3,4,5], 'a') == -1

def test_end():
    assert binSearch([1,2,3,4,5],5) == 4