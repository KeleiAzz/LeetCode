
def isPowerOfThree(n):
    if n == 1:
        return True
    if n < 3:
        return False
    if n % 3 == 0 and isPowerOfThree(n // 3):
        return True
    return False