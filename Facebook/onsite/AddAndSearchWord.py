class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.childs = dict()
        self.isWord = False

class WordDictionary:
    '''
    Implement with Trie, insert word to a trie
    '''
    def __init__(self):
        self.root = TrieNode()
    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        node = self.root
        for c in word:
            if c in node.childs:
                node = node.childs[c]
            else:
                node.childs[c] = TrieNode()
                node = node.childs[c]
        node.isWord = True


    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.find(self.root, word)

    def find(self, node, word):
        if word == '':
            return node.isWord
        if word[0] == '.':
            for child in node.childs.values():
                if self.find(child, word[1:]):
                    return True
        else:
            if word[0] in node.childs:
                return self.find(node.childs[word[0]], word[1:])
        return False
