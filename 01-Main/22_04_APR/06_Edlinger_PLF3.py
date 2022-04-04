"""
Marc EDLINGER
1bHIF | 04/04/2022
3. PLF
"""


def quadrate(lst: list) -> int:
    """
    Fill the list lst ascending with the square of numbers and return the sum of the values
    """
    sum: int = 0
    for i in range(0, len(lst), 1):
        lst[i] = (i + 1) ** 2
        sum += lst[i]

    return sum


def count_descending(lst: list) -> int:
    """
    Check how many descending numbers are in the list lst and return the amount
    """
    count: int = 0
    for i in range(len(lst) - 1):
        count += 1
        if not lst[i] >= lst[i + 1]:
            break
    return count


def pretty_print(lst: list, should_print: bool) -> int:
    """
    print all negative numbers in lst with stars in front of it
    if should_print is False, it will only return the absolute value of the sum of the negative numbers
    """
    sum: int = 0
    for element in lst:
        if element < 0:
            if should_print:
                display: str = ""
                for i in range(abs(element)):
                    display += "*"
                print(display, element)
            sum += element
    return abs(sum)


def deltas_to_average(source: list, target: list) -> int:
    """
    Calculate and return the whole number average of the numbers in source
    Put the difference between the numbers in source and the average value in the target list
    """
    if (len(source) != len(target)):
        raise Exception("The lists must have the same length")

    average: int = 0
    if (len(source) != 0):
        for element in source:
            average += element
        average = round(average / len(source))

    for i in range(len(source)):
        target[i] = source[i] - average
    return average


def test_me(function, expected_result, *parameters):
    """
    Test the function with the parameters and the expected result
    """
    result = function(*parameters)
    if result == expected_result:
        print("Test passed")
    else:
        print("Test failed! Expected result:", expected_result, "but got:", result)


"""
TEST CASES
"""
if __name__ == "__main__":
    print("--- Tests for quadrate ---")
    test_me(quadrate, 55, [25, 7, 3, 232, 6])
    test_me(quadrate, 0, [])

    print("--- Tests for count_descending ---")
    test_me(count_descending, 7, [9, 8, 8, 2, 0, -3, -3, 2, -4, -11])
    test_me(count_descending, 0, [])

    print("--- Tests for pretty_print ---")
    test_me(pretty_print, 8, [-1, -2, 3, 4, -5], False)
    test_me(pretty_print, 0, [], False)
    test_me(pretty_print, 10, [-2, -5, 4, 0, -3], False)

    print("--- Tests for deltas_to_average ---")
    dummy: list = [0] * 6
    test_me(deltas_to_average, 2, [1, 5, 3, -2, 0, 3], dummy)
    assert dummy == [-1, 3, 1, -4, -2, 1]
    print("Test passed completely")

    dummy = [0] * 10
    test_me(deltas_to_average, 9, [6, 9, 2, 4, -3, 6, 2, 100, 2, -40], dummy)
    assert dummy == [-3, 0, -7, -5, -12, -3, -7, 91, -7, -49]
    print("Test passed completely")
