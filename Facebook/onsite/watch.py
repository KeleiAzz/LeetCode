from collections import deque
import os

def tail(filename, n=10):
    return deque(open(filename), n)
print os.stat('questions.md')
print tail('questions.md')
