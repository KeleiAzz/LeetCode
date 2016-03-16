# TODO think about how to do it in a 2D version
class Intervals(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

def getMostCovered(intervals):
    def compare(x, y):
        if x[0] != y[0]:
            return x[0] - y[0]
        else:
            return x[1] - y[1]

    times = []
    times.extend([(x.start, 1) for x in intervals])
    times.extend([(x.end, -1) for x in intervals])
    times.sort(cmp=compare)
    count = 0
    res = 0
    max_covered_points = -1
    for time in times:
        if time[1] == 1:
            count += 1
        else:
            count -= 1
        if count > res:
            res = count
            max_covered_points = time[0]
    return res, max_covered_points

a = Intervals(0, 3)
b = Intervals(1, 4)
c = Intervals(2, 5)
d = Intervals(3, 7)
e = Intervals(4, 6)
intervals = [a, b, c, d, e]
print getMostCovered(intervals)
