"""
Marc EDLINGER
1bHIF | 24/05/2022
"""


def encrypt(s: str, shift: int = 2, sign: str = "ASSE") -> (int, str):
    result: str = ""
    count: int = 0
    secret_number: int = 0
    for c in s:
        code = ord(c)
        mid: int = code + shift
        if mid % 2 == 0:
            right: int = mid - shift
            left: int = mid + shift
            secret_number += right + left
        elif mid % 3 == 0:
            right: int = 2 * shift
            left: int = (mid + shift) // 2
            secret_number -= right + left
        elif mid % 5 == 0:
            right: int = 2 * shift
            left: int = (mid + shift) // 2
            secret_number -= left**2
        elif mid % 7 == 0:
            right: int = 3 * shift - mid
            left: int = mid + shift**2
            secret_number += right**2
        else:
            right: int = mid + 2*shift
            left: int = mid + shift // 2
            secret_number += right ** 2

        result += chr(left % 126) + chr(mid % 126) + chr(right % 126)
        if count % ((len(s) // 10) + 1) == 0:
            result += result
        count += 1

    return (secret_number, sign + "==" + result)


print(encrypt("Auer stinkt"))
