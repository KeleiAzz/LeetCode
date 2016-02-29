def regexMatch(s, p):
    pass



def fibonacci(n):
    p1, p2 = 0, 1
    for i in range(n):
        if i == 0:
            yield 0
        if i == 1:
            yield 1
        p1, p2 = p2, p1 + p2
        yield p2

f = fibonacci(100)
for i in range(100):
    print f.next()