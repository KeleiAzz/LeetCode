from collections import defaultdict
def minWindow( s, t):
    count = 0
    m = {}
    for c in t:
        if c not in m:
            count += 1
            m[c] = 0
        m[c] += 1

    start = 0
    size = len(s)
    ansLen = size + 1
    ans = ''
    for end in xrange(size):
        if s[end] not in m:
            continue
        m[s[end]] -= 1
        if m[s[end]] == 0:
            count -= 1

        while count == 0:
            if end - start + 1 < ansLen:
                ansLen = end-start+1
                ans = s[start:end+1]
            startC = s[start]
            start += 1
            if startC not in m:
                continue
            m[startC] += 1
            if m[startC] == 1:
                count += 1
                break

    if ansLen == size + 1:
        return ''
    return ans


def minWindow2(s, t):
    positions = defaultdict(int)
    for l in t:
        positions[l] += 1
    print positions
    counter = len(positions)
    i = 0
    j = 0
    l, r = 0, len(s)
    while j < len(s):
        if s[j] in positions:
            positions[s[j]] -= 1
            if positions[s[j]] == 0:
                counter -= 1
        # print counter
        while counter == 0:
            # print 'counter is 0'
            if j - i < r - l:
                l, r = i, j
            c = s[i]
            i += 1
            if c not in positions:
                continue
            positions[c] += 1
            if positions[c] == 1:
                counter += 1
                break
        j += 1
    if r - l == len(s):
        # print 'here'
        return ""
    return s[l:r+1]

print minWindow2('aa', 'aa')