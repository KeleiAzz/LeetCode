def all_palindrome(s):
    res = []
    if len(s) < 2:
        return res
    if s[0] == s[1]:
        res.append(s[0:2])
    for i in range(2, len(s)):
        if s[i] == s[i-1]:

            res.append(get_palindrome(s, i - 1, i))
        if s[i] == s[i-2]:
            res.append(get_palindrome(s, i - 2, i))
    return res

def get_palindrome(s, left, right):
    while True:
        
        if s[left] == s[right]:
            left -= 1
            right += 1
        else:
            left += 1
            right -= 1
            break
        if left < 0 or right >= len(s):
            left += 1
            right -= 1
            break

    print left, right, s[left:right+1]
    return s[left:right+1]

s = "adabbbacca"
print all_palindrome(s)
