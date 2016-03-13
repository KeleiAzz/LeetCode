class TreeNode(object):
    def __init__(self, v):
        self.val = v
        self.end = False
        self.child = dict()


def generateTrie(words, reverse = False):
    root = TreeNode(".")
    # node = root
    for word in words:
        node = root
        if reverse:
            word = word[::-1]
        for letter in word:
            if letter in node.child:
                node = node.child[letter]
            else:
                node.child[letter] = TreeNode(letter)
                node = node.child[letter]
        node.end = True
    return root

def insertWord(word, root):
    node = root
    for letter in word:
        if letter in node.child:
            node = node.child[letter]
        else:
            node.child[letter]  = TreeNode(letter)
            node = node.child[letter]
    node.end = True

def searchWord(word, root):
    node = root
    for letter in word:
        if letter in node.child:
            node = node.child[letter]
        else:
            return False
    if node.end:
        return True
    return False


words = ['bana', 'nab', 'cooc', 'ooc', 'abedd', 'eba']

root = generateTrie(words)

def is_palindrome(a):
    return a == a[::-1]


def findAllPalindrome(words):
    root = generateTrie(words, True)
    res = []
    for word in words:
        node = root
        # word = word[::-1]
        cur_word = ''
        for i in range(len(word)):
            if word[i] in node.child:
                cur_word += word[i]
                node = node.child[word[i]]
                if node.end:
                    if is_palindrome(word[i+1:]):
                        res.append((word, cur_word))
            else:
                break
    print res


findAllPalindrome(words)