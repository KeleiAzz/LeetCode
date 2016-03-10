from collections import Counter


class LogEntry(object):
    def __init__(self, c, t):
        self.candidate = c
        self.time = t


def findWinner(time, logs):
    candidates = []
    for log in logs:
        if log.time == time:
            candidates.append(log.candidate)
    winner = Counter(candidates).most_common(1)[0][0]
    return winner


logs = [LogEntry('c1', 2), LogEntry('c1', 2), LogEntry('c2', 2)]

print findWinner(2, logs)