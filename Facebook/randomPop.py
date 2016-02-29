import random



def randomPop(nums):
    for i in range(len(nums)):
        if random.random() < 0.5:
            yield nums.pop()
        else:
            yield nums.pop(0)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = randomPop(a)


def reconstruct(nums):
    s = []
    l = []
    a = nums.next()
    s.append(a)
    end = 0
    while not end:
        try:
            new = nums.next()
        except StopIteration:
            # new = None
            break
        if new > s[-1]:
            s.append(new)
        else:
            l.insert(0, s.pop())
            s.append(new)

    print s + l

reconstruct(n)