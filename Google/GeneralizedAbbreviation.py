class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        self.dfs('', word, res)
        return res

    
    
    def dfs(self, tmp, word, res):
        if not word:
            res.append(tmp)
        for i in range(1, len(word)+1):
            if not tmp or tmp[-1].isalpha():
                self.dfs(tmp+str(i), word[i:], res)
            if not tmp or tmp[-1].isdigit():
                self.dfs(tmp+word[:i], word[i:], res)