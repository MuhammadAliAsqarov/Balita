def isPalindrome(s: str) -> bool:
    k = ''
    for i in s:
        if i.isalpha and i.islower():
            k += i
        elif i.isalpha and i.isupper():
            t = i.lower()
            k += t
        elif i.isdigit():
            k += i
    if k[::-1] == k:
        return True
    else:
        return False
print(isPalindrome("A man, a plan, a canal: Panama"))