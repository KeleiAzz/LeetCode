import sys
from collections import deque


def tail(path, n=10):
    try:
        f = open(path, 'r')
        f.seek(0, 2)
        file_length = f.tell()
        if file_length < n * 100:
            f.seek(0, 0)
            text = f.read()
        else:
            offset = -n * 100
            while -offset <= file_length:
                f.seek(offset, 2)
                text = f.read()
                if text.count('\n') > n:
                    break
                else:
                    offset -= 100
        queue = deque(maxlen=n)
        lines = text.split('\n')
        for line in lines:
            queue.append(line)
        for line in queue:
            print line
    except IOError:
        print "Can not read", path
        exit(1)


if __name__ == '__main__':
    tail(sys.argv[2], int(sys.argv[1]))