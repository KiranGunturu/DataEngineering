def implementstr(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


if __name__ == "__main__":
    haystack="kuumar"
    needle="r"
    ans=implementstr(haystack, needle)
    print(ans)