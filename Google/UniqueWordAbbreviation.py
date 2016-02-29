from collections import defaultdict
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.d = defaultdict(str)
        for word in dictionary:
            if len(word) < 3:
                # self.d[word] += 1
                pass
            else:
                s = word[0] + str(len(word) - 2) + word[-1]
                if s not in self.d:
                    self.d[s] = word
                else:
                    self.d[s] = ''


    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            s = word
        else:
            s = word[0] + str(len(word) - 2) + word[-1]
        if s in self.d and self.d[s] == '':
            return False
        elif s in self.d and self.d[s] != word:
            return False
        else:
            return True



# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")