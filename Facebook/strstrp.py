from collections import Counter
def strstrp(a, b):
    b_counter = Counter(b)
    m = len(b)
    for i in range(len(a) - m + 1):
        a_counter = Counter(a[i:i+m+1])
        if all([x == 0 for x in (a_counter-b_counter).values()]):
            return True
    return False


print strstrp('hello', 'loeal')