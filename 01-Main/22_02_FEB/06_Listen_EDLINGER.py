# Arbeiten mit listen
# Edlinger Marc | 1bHIF | 22.04.2022

def check_list_ascending(check_list: list) -> bool:
    for i in range(len(check_list) - 1):
        if (check_list[i] > check_list[i + 1]):
            return False
    return True

def check_list_descending(check_list: list) -> bool:
    for i in range(len(check_list) - 1):
        if (check_list[i] < check_list[i + 1]):
            return False
    return True

def check_list_equality(check_list: list, other_list: list) -> bool:
    for i in range(len(check_list)):
        if (check_list[i] != other_list[i]):
            return False
    return True

list1: list = [1, 3, 5, 7, 8, 22]
list2: list = [20, 5, 3, 2, 1, -1]
list3: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list4: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("*"*5 + " LIST 1 " + "*"*5)
print("Aufsteigend:", check_list_ascending(list1))
print("Absteigend:", check_list_descending(list1))

print("*"*5 + " LIST 2 " + "*"*5)
print("Aufsteigend:", check_list_ascending(list2))
print("Absteigend:", check_list_descending(list2))

print("*"*5 + " LIST 3/4 " + "*"*5)
print("Aufsteigend:", check_list_ascending(list3))
print("Absteigend:", check_list_descending(list3))
print("Gleich:", check_list_equality(list3, list4))