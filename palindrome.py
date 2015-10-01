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
    li1 = tobinary(li1, len(li))
    li2 = tobinary(li2, len(li))
    # print li1, li2
    for i in range(len(li)):
        if li1[i] == 0 and li2[i] == 0:
            res.append('-')
        elif li1[i] == 1 and li2[i] == 1:
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
        if eq % 2 == 0 and eq/2 in tt and eq in tt and belong(tobinary(t[eq/2-n], l), tobinary(t[eq-n], l)):
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
        res[sum(li)] = i
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

# print answer3(14)

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

# print answer4(1003)

def answer5(x):
    li = [ 3 ** i for i in range(20)]
    R = 0
    L = x
    res = []
    for i in range(20):
        if L/(3 ** i) % 3 == 1:
            R += 3 ** i
            res.append(["R"])
        elif L/(3 ** i) % 3 == 2:
            L += 3 ** i
            res.append(["L"])
        elif L/(3 ** i) % 3 == 0:
            res.append(["-"])
        if L == R:
            break
    print res

# answer5(28)

def answer6(n, x):
    l = len(x)

    m = []
    for i in range(l):
        m.append([0] * l)
    m[-1][-1] = n
    for i in range(l - 2, -1, -1):
        m[i][-1] = m[i + 1][-1] - x[i + 1][-1]
        m[-1][i] = m[-1][i + 1] - x[-1][i + 1]
    print m
    for i in range(l - 2, -1, -1):
        for j in range(l - 2, -1, -1):
            if m[i + 1][j] - x[i + 1][j] < 0 and m[i][j + 1] - x[i][j + 1] < 0:
                m[i][j] = -1
            elif m[i + 1][j] - x[i + 1][j] < 0:
                m[i][j] = m[i][j + 1] - x[i][j + 1]
            elif m[i][j + 1] - x[i][j + 1] < 0:
                m[i][j] = m[i + 1][j] - x[i + 1][j]
            else:
                m[i][j] = min(m[i + 1][j] - x[i + 1][j], m[i][j + 1] - x[i][j + 1])
    return m[0][0]




class cell():
    def __init__(self, value, origin, row, column, direction):
        self.value = value
        self.origin = origin
        self.row = row
        self.column = column
        self.direction = direction

    def __str__(self):
        return "%d %d %d %d %s " % (self.value, self.origin, self.row, self.column, self.direction)

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value
from operator import attrgetter
def answer7(n, x):
    l = len(x)
    m = []
    for i in range(l):
        m.append([0] * l)
    m[0][0] = cell(0, 0, 0, 0, 'None')
    for i in range(1, l, 1):
        m[0][i] = cell(m[0][i-1].value + x[0][i], x[0][i], 0, i, 'L' )
        m[i][0] = cell(m[i-1][0].value + x[i][0], x[i][0], i, 0, 'U')

    for i in range(1, l, 1):
        for j in range(1, l, 1):
            if m[i-1][j] > m[i][j-1]:
                m[i][j] = cell(m[i-1][j].value + x[i][j], x[i][j], i, j, 'U')
            else:
                m[i][j] = cell(m[i][j-1].value + x[i][j], x[i][j], i, j, 'L')
    if m[-1][-1].value <= n:
        return n - m[-1][-1].value
    # else:

    for i in range(l):
        print m[-1][i]



grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
grid2 = [[0, 2], [1, 3]]
n = 11

# print answer6(4, grid)
# print answer6(5, grid)

def smallest_remainder(total, grid):
    """Return the smallest remainder from total after subtracting the
    numbers on a path from top left to bottom right of grid, or -1 if
    there is no path whose sum is less than or equal to total.

    >>> smallest_remainder(7, [[0, 2, 5], [1, 1, 3], [2, 1, 1]])
    0
    >>> smallest_remainder(12, [[0, 2, 5], [1, 1, 3], [2, 1, 1]])
    1

    """
    # @memoized
    def r(t, i, j):
        # Smallest remainder from t after subtracting the numbers on a path
        # from top left to (i, j) in grid, or total + 1 if there is no
        # path whose sum is less than or equal to t.
        t -= grid[i][j]
        if i < 0 or j < 0 or t < 0:
            return total + 1
        elif i == j == 0:
            return t
        else:
            return min(r(t, i - 1, j), r(t, i, j - 1))

    remainder = r(total, len(grid) - 1, len(grid) - 1)
    return remainder if remainder <= total else -1

# print smallest_remainder(8, grid)

def answer8(food, grid):
    N = len(grid)
    ans_grid = [[set() for i in range(N)] for j in range(N)]
    ans_grid[0][0] |= {grid[0][0]}
    for (row, row_val) in enumerate(grid):
        for (col, val) in enumerate(row_val):
            if row != 0:
                ans_grid[row][col] |= {val + x for x in ans_grid[row-1][col]
                                       if (val + x) <= food}
            if col != 0:
                ans_grid[row][col] |= {val + x for x in ans_grid[row][col-1]
                                       if (val + x) <= food}
    all_ans = sorted(ans_grid[N-1][N-1], reverse=True)
    for el in all_ans:
        if el <= food:
            return food-el
    return -1

# when_it_rains_it_pours
def answer9(heights):  # time limit exceeded
    # your code here
    count = 0
    while(1):
        flag = 0
        end = 0
        start = 0
        for i in range(len(heights)):
            heights[i] = max(heights[i]-1, 0)
            if heights[i] > 0 and flag == 0:
                start = i
                flag = 1
        print heights
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > 0:
                end = i
                break
        print end
        if start == end:
            break
        count += heights[start:end].count(0)
    return count


def answer10(heights):
    if len(heights) <= 2:
        return 0
    highest = max(heights)
    h_index = heights.index(highest)
    left = heights[0:h_index]
    right = heights[h_index+1:]
    # right.reverse()
    return recurr(left, "L") + recurr(right, "R")

def recurr(l, side):
    if len(l) <= 1:
        return 0
    highest = max(l)
    h_index = l.index(highest)

    count = 0
    if side == "L":
        for i in range(h_index+1, len(l), 1):
            count += highest - l[i]
        count += recurr(l[0:h_index], "L")
    elif side == "R":
        for i in range(0, h_index, 1):
            count += highest - l[i]
        count += recurr(l[h_index+1:], "R")
    return count



print answer10( [9,4,5,4,99])