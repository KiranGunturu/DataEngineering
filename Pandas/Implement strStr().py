def implementstr(haystack: str, needle: str) -> str:
    if not needle:
        return 0
    for i in range(len(haystack)):
        #print(i)
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


if __name__ == "__main__":
    haystack="hello"
    needle="ll"
    ans=implementstr(haystack, needle)
    print(ans)
