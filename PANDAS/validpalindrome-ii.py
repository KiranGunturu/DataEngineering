#def validpalii(palstring: str):
    # pal = palstring[::-1]
    # if pal == palstring:
    #     print("valid palindrome")
    # else:
    #     size = len(palstring)
    #     print(size)
    #     pal = palstring[0:(size-1)]
    #     pal2 = pal[0:(size-2)] + palstring[:1]
    #     print(pal2)
    #     #print(pal)
    #     #pal = palstring.pop(size-1)
    #     if pal2 == pal2:
    #         print("palindrome")
    #     else:
    #         print("not a valid pal")

def validparlii(s: str) -> bool:
    l=0
    r=len(s)
    print(r)
    r=len(s)-1
    print(r)
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]
    return True


if __name__ == "__main__":
    palstring="madadm"
    ans=validparlii(palstring)
    print(ans)




