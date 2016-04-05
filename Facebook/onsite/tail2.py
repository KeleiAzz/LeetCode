import sys
from collections import deque


def tail(path, n=10):
    try:
        with open(path, 'r') as f:
            queue = deque(maxlen=n)
            for line in f:
                queue.append(line)
        for line in queue:
            print line[:-1]  # do not print out the \n
    except IOError:
        print "Can not open", path
        exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        tail(sys.argv[-1])
    elif len(sys.argv) == 4 and sys.argv[1] == '-n' and sys.argv[2].isdigit():
        tail(sys.argv[-1], int(sys.argv[2]))
    else:
        print sys.argv
        print "command in this format: python tail.py -n 10 file"
