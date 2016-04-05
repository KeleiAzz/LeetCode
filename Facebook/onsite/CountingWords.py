import heapq
import re


def countWords(input, n=10):
    words = re.findall('\w+', input)
    count = {}
    for word in words:
        word = word.lower()
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    countList = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(countList)
    res = []
    for i in range(n):
        _, word = heapq.heappop(countList)
        res.append(word)
    return res



