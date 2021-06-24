def palindrome(str):
    for i in range(len(str)):
        if str[i] != str[len(str)-1-i]:
            return False
    return True

print(palindrome("abasba"))