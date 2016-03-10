class Person(object):
    def __init__(self, name):
        self.name = name
        self.friends = set()

    def add_friends(self, friends):
        for friend in friends:
            self.friends.add(friend)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

a = Person('a')
b = Person('b')
c = Person('c')
d = Person('d')
e = Person('e')
f = Person('f')
g = Person('g')
h = Person('h')
i = Person('i')

a.add_friends([b, c, i])
b.add_friends([a, d, e, h])
c.add_friends([a, f, g, h])
i.add_friends([a, h, e])


from collections import defaultdict
def sortFriend(root):
    res = defaultdict(int)
    friends = root.friends
    for friend in friends:
        for ff in friend.friends:
            if ff not in friends and ff != root:
                res[ff] += 1
    print res


sortFriend(a)