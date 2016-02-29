from collections import defaultdict
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dictionary = defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.dictionary[len(word)].append(word)


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if '.' not in word:
            return word in self.dictionary[len(word)]
        def match(input, word):
            return all([x[0] == x[1] or x[0] == '.' for x in zip(input, word)])
        return any([match(word, w) for w in self.dictionary[len(word)]])


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")