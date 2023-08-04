from utils.app import sub_function, sum_function


def test_sum_function():
    """
    Test sum_function
    """
    assert sum_function(1, 2) == 3

def test_sub_function():
    """
    Test sum_function
    """
    assert sub_function(1, 2) == -1
