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


def test_list_function(function, given_list, expected_list, expected_return, *args):
    """
    Tests a function with a given expected value and arguments.
    """
    try:
        return_value = function(given_list, *args)
        successfully = False
        if given_list == expected_list:
            if expected_return is not None:
                if return_value == expected_return:
                    successfully = True
            else:
                successfully = True

        if not successfully:
            print("Test failed : expected", expected_list, "|", expected_return,  "got", given_list, "|", return_value)
        else:
            print("Test passed")
    except Exception as e:
        print("Test failed with exception:", e)
