def reverse_string(s: str) -> str:
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]


print(reverse_string("Hallo lele"))
