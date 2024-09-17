def countConsistentStrings(allowed: str, words) -> int:
    s1 = set(allowed)
    c = 0
    for i in words:
        if set(i).issubset(s1):
            c += 1
    return c


print(countConsistentStrings("ab",
                             ["ad", "bd", "aaab", "baa", "badab"]))
