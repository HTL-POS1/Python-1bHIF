def reverseString(s: str) -> str:
    if s == "":
        return ""
    return reverseString(s[1:]) + s[0]

print(reverseString("Hallo lele"))