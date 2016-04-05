import os, sys, argparse


def tail(path, lines_to_print=5):
    if lines_to_print < 1:
        return
    with open(path, 'r') as file:
        file.seek(-1, os.SEEK_END)
        position = file.tell()
        lines_seen = 0
        if file.read(1) == '\n':
            position -= 1
            file.seek(position)
        while lines_seen < lines_to_print and file.tell() > 0:
            c = file.read(1)
            if c == '\n':
                lines_seen += 1
                if lines_seen == lines_to_print:
                    break
            position -= 2
            file.seek(position)
        sys.stdout.write(file.read())



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='The path to the file to tail')
    parser.add_argument('-n', help='Print the last n lines of the file', type=int, default=5)
    args = parser.parse_args()
    print args
    tail(args.path, args.n)
