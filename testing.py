"""
Marc EDLINGER
1bHIF | 05/04/2022
"""


def test_function(function, expected_value, *args):
    """
    Tests a function with a given expected value and arguments.
    """
    try:
        result = function(*args)
        if result == expected_value:
            print("Test passed")
        else:
            print("Test failed : expected", expected_value, "got", result)
    except Exception as e:
        print("Test failed with exception:", e)


def test_list_function(function, given_list, expected_list, *args):
    """
    Tests a function with a given expected value and arguments.
    """
    try:
        function(given_list, *args)
        if given_list == expected_list:
            print("Test passed")
        else:
            print("Test failed : expected", expected_list, "got", given_list)
    except Exception as e:
        print("Test failed with exception:", e)