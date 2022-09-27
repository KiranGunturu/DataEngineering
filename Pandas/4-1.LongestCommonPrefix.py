def longestcommonprefix(str: list[str]) -> str:

    if len(str) == 0:
        return ("")
    if len(str) == 1:
        return str[0]

    pref = str[0]
    #print(pref)
    preflen = len(pref)
    #print(preflen)

    for s in str[1:]:
        while pref != s[0:preflen]:
            pref = pref[0:(preflen-1)]
            preflen -= 1

            if preflen == 0:
                return "No Prefix found"
    return(pref)


if __name__ == "__main__":
    str=["flower","flow","flight"]
    #str = ["fl", "llo", "hello"]
    ans=longestcommonprefix(str)
    print(ans)

#Best solution






