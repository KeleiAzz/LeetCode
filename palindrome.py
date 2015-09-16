def answer(n):

    letter = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H'}
    for i in range(2, 10, 1):
        # print "-----", i, "-----"
        temp = n
        res = ''
        while temp >= i:
            reminder = temp % i
            # print reminder
            if reminder in letter.keys():
                reminder = letter[reminder]
            res = str(reminder) + res
            temp /= i
        res = str(temp) + res
        # print res
        token = True
        for j in range(len(res)/2):
            if res[j] != res[-1 - j]:
                token = False
                break
        if token:
            print i
            break
        # print "-----", i, "-----"


# answer(999)

def answer2(x):
    # your code here
    s = sum(x)

    for i in range(len(x), 1, -1):
        if s % i == 0:
            return i
    return 1

# print answer2([1, 2, 235, 1231, 54245, 1231, 123541])

def answer3(x):
    m = 0
    for i in range(20):
        if 3 ** i >= x:
            m = i
            break
    li = [3 ** i for i in range(m)]
    L = x
    if sum(li) < x:
        li.append(3 ** (m))
    elif sum(li) == x:
        return ['R'] * len(li)
    R = li[-1]
    # print li
    li1, li2 = check(L, li)
    res = []
    for i in li:
        if i not in li1 and i not in li2:
            res.append('-')
        elif i in li1:
            res.append('L')
        else:
            res.append('R')
    return res


def check(n, x):
    l = len(x)
    t = comb(x)
    tt = [ i + n for i in t.keys()]
    for key, value in t.items():
        eq = n + key

        if eq % 2 == 0 and eq/2 in tt and eq in tt and belong(t[eq/2-n], t[eq-n]):
            # print eq/2, t[eq/2-n], t[eq-n]
            return t[eq/2-n], t[eq-n]

def belong(li1, li2):
    for i in range(len(li1)):
        if li1[i] != 0 and li1[i] not in li2:
            return False
    return True

def comb(x):
    l = len(x)
    res = {}
    for i in range(2 ** l):
        li = tobinary(i, l)
        for j in range(l):
            li[j] = li[j] * x[j]
        res[sum(li)] = li
    return res

def tobinary(n, l):
    res = []
    while n >= 2:
        reminder = n % 2
        res = [reminder] + res
        n /= 2
    res = [n] + res
    while len(res) < l:
        res = [0] + res
    return res

# print answer3(19845021)

def answer4(x):
    m = 0
    for i in range(20):
        if 3 ** i >= x:
            m = i
            break
    li = [3 ** i for i in range(m)]
    L = x
    if sum(li) < x:
        li.append(3 ** (m))
    elif sum(li) == x:
        return ['R'] * len(li)
    R = li.pop()
    print li
    while(1):
        if L == R:
            return L
        if L < R:
            if L + li[-1] == R:
                return R
            tmp1 = L
            for i in li:
                if L + i == R:
                    return L, i, R
                elif L + i > R and L + li[-1] < R + sum(li[0:-1]):
                    print L, i, L+i, "L + i ="
                    L += i
                    li.remove(i)
                    break
            if L == tmp1:
                if L + li[-1] < R + sum(li[0:-1]):
                    print L, li[-1], L+li[-1], "L + li[-1]"
                    L += li.pop()
                elif L + li[-1] == R + sum(li[0:-1]):
                    return L, li[-1], R
                else:
                    print L, li[-2], L + li[-2], "L + li[-2]"
                    L += li[-2]
                    li.remove(li[-2])

        if L > R:
            if R + li[-1] == L:
                return R
            tmp2 = R
            for i in li:
                if R + i == L:
                    return L, i, R
                elif R + i > L and R + li[-1] < L + sum(li[0:-1]):
                    print R, i, R + i, "R + i="
                    R += i
                    li.remove(i)
                    break
            if R == tmp2:
                if R + li[-1] < L + sum(li[0:-1]):
                    print R, li[-1], R+li[-1], "R + li[-1"
                    R += li.pop()
                elif R + li[-1] == L +sum(li[0:-1]):
                    return L, li[-1], R
                else:
                    print R, li[-2], R + li[-2], "R + li[-2]"
                    R += li[-2]
                    li.remove(li[-2])

        if len(li) == 0:
            print L, R
            break

print answer4(1003)

