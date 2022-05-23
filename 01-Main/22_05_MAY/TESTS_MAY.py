"""
Marc EDLINGER
1bHIF | 23/05/2022
"""
from testing import test_function
from ASCII_Strings import get_character_position, print_ascii_table, to_lowe_case, show_statistics

"""
ASCII_STRINGS
"""

# get_character_position
test_function(get_character_position, 65, 'A')
test_function(get_character_position, -1, '2')
test_function(get_character_position, -1, '33ds')

# print_ascii_table
print_ascii_table(4)
print_ascii_table(10)
print_ascii_table(2)        # exception

# to_lower_case
binary_null: str = chr(7)
test_function(to_lowe_case, "a", "A")
test_function(to_lowe_case, binary_null, "AD")
test_function(to_lowe_case, binary_null, "2")
test_function(to_lowe_case, "e", "E")
test_function(to_lowe_case, "v", "v")

# statistics
get_character_position("A")
get_character_position("A")
get_character_position("A")
get_character_position("B")
get_character_position("D")
get_character_position("B")
get_character_position("B")
get_character_position("B")
get_character_position("Z")
get_character_position("Y")
get_character_position("Y")
get_character_position("Y")
show_statistics()

