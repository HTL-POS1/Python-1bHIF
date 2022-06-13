"""
Marc EDLINGER
1bHIF | 13.06.2022
4. PLF
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


def insert_at(lst: list[int], at: int, val: int) -> int:
    """ set position at in lst to val
        if at is not a valid position, return -1, otherwise return at
    """
    result = -1
    if (at >= 0 and at < len(lst)):
        for i in range(len(lst) - 1, at, -1):
            lst[i] = lst[i - 1]

        lst[at] = val
        result = at

    return result


def expand_by(word: str, by: str) -> str:
    """ expand every character in word by the character by
        if by has more than one letter, an empty string is returned
    """
    result: str = ""
    if (len(by) == 1):
        last_word_index = len(word) - 1
        for i in range(last_word_index):
            result += word[i] + by
        result += word[last_word_index]
    return result


def first(word: str, sub: str) -> int:
    """ return the index where the string sub has its first occurrence in word
        if there is no occurrence, return -1
    """
    sub_word_length: int = len(sub)
    found_index = -1

    for i, c in enumerate(word):
        current_sequence: str = ""
        for j in range(sub_word_length):
            k: int = i + j
            if (k < len(word)):
                current_sequence += word[k]

        if current_sequence == sub:
            found_index = i

    return found_index


def count(word: list, c: int) -> int:
    """ liefert die Anzahl, wie oft c in word vorkommt"""
    count: int = 0
    for i in word:
        if (i == c):
            count += 1
    return count


def get_first_pos(lst: list, e: int):
    """ returns the first index, e value appears in lst """
    for i, n in enumerate(lst):             # i is the index, n is the current element at the index i
        if n == e:                          # if the current element equals the element, searching for
            return i                       # return the current index
    return -1


def build_string(i: int, s: str) -> str:
    tmp: str = ""
    for k in range(i):
        tmp += s
    return tmp


def analyse(word: str):
    used_chars: list[str] = [""] * len(word)
    for c in word:
        if get_first_pos(used_chars, c) == -1:
            occurrence: int = count(word, c)
            used_chars[get_first_pos(used_chars, "")] = c
            print(c, build_string(occurrence, "*") + build_string(10 - occurrence, " ") + str(occurrence) + "x", ord(c))


analyse("susanne")

list1: list[int] = [1, 3, 5, 7]
test_list_function(insert_at, list1, [1, 3, 4, 5], 2, 2, 4)
test_list_function(insert_at, list1, [1, 3, 4, 5], -1, -4, 0)

test_function(expand_by, "H-u-g-o", "Hugo", "-")
test_function(expand_by, "", "Hugo", "==")

test_function(first, 4, "Autobahn", "bahn")
test_function(first, -1, "Autobahn", "bahnsteig")
test_function(first, -1, "", "haus")

