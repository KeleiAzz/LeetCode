# coding=utf-8
class Person(object):
    def __init__(self, name):
        self.name = name
        self.knowing = []

def HaveAcquaintance(A, B):
    if B in A.knowing:
        return True
    return False

def findCelebrity(party):
    '''
    可以分析几种情况

    如果A认识B，那么A不可能是celebrity。去掉A，B则有可能是
    如果A不认识B，那么B不可能是celebrity。去掉B，A则有可能是
    重复以上两个步骤直到只剩下一个候选人
    再次确认是否这最后一个人是否为celebrity
    这里用stack来做。

    把所有的celebrity压栈
    弹出最上面的两个celebrity，根据HaveAcquaintance(A, B)的结果来去掉一个一定不是celebrity的人
    将2中剩下的那一位压栈
    重复以上两个步骤，直到stack中只剩一个人
    确认这个人不认识其他任何人
    :param party:
    :return:
    '''
    stack = []
    for person in party:
        stack.append(person)
    A = stack.pop()
    B = stack.pop()
    while len(stack) > 0:
        if HaveAcquaintance(A, B):
            A = stack.pop()
        else:
            B = stack.pop()
    # C = stack.pop()
    if HaveAcquaintance(A, B):
        C = B
    else:
        C = A
    # Now C is the potential celebrity, need to check weather it is truely the one.
    for person in party:
        if person != C:
            if HaveAcquaintance(C, person) or not HaveAcquaintance(person, C):
                return None
    return C