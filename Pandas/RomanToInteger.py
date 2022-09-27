def romantointeger(str: str) -> int:

    roman_table = {"I": 1,
                   "V": 5,
                   "X": 10,
                   "L": 50,
                   "C": 100,
                   "D": 500,
                   "M": 1000}

    num = 0
    last = "I"

    for numeral in str[::-1]:
        if roman_table[numeral] < roman_table[last]:
            num -= roman_table[numeral]
        else:
            num += roman_table[numeral]
        last = numeral
    return num


if __name__ == "__main__":
    str="II"
    ans = romantointeger(str)
    print(ans)