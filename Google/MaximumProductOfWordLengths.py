class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) == 1:
            return 0
        words.sort(key = lambda s:len(s), reverse=True)
        words_set = [set(word)  for word in words]
        max_len = 0
        for i in xrange(len(words)-1):
            for j in xrange(i, len(words), 1):
                if len(words_set[i] & (words_set[j])) == 0:
                    max_len = max(max_len, len(words[i])*len(words[j]))
                    break
        return max_len


    def maxProduct2(self, words):
        """
        Another way, first know the "for else" syntax.
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0
        curr_max = 0
        while words:
            curr_word = set(words[0])
            curr_len = len(words[0])
            words = words[1:]
            for word in words:
                for char in curr_word:
                    if char in word:
                        break
                else:
                    curr_max = max(curr_max, curr_len*len(word))
        return curr_max