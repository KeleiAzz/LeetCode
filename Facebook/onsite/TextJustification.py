class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not maxWidth:
            return [""]
        currLen, i = 0, 0
        currWords = []
        res = []
        while i < len(words):
            if currLen + len(words[i]) + 1 > maxWidth:
                spacesLen = maxWidth - currLen + len(currWords) - 1
                spacesCount = len(currWords) - 1
                spaces = [spacesLen / spacesCount for _ in xrange(spacesCount)]
                if spacesCount:
                    spacesLeft = spacesLen - (spacesLen / spacesCount * spacesCount)
                    if spacesLeft:
                        for j in range(spacesCount):
                            spaces[j] += 1
                            spacesLeft -= 1
                            if spacesLeft == 0:
                                break
                tmp = ''
                for j in range(spacesCount):
                    tmp += currWords[j]
                    tmp += ' '*spaces[j]
                if currWords:
                    tmp += currWords[-1]
                if spacesCount == 0:
                    tmp += ' ' * (maxWidth - len(tmp))
                if tmp != '':
                    res.append(tmp)
                currLen = len(words[i])
                currWords = [words[i]]
            else:
                currLen += len(words[i]) if len(currWords) == 0 else len(words[i]) + 1
                currWords.append(words[i])
            i += 1
        tmp = ' '.join(currWords)
        tmp += ' ' * (maxWidth - len(tmp))
        res.append(tmp)
        return res
words = ["Listen","to","many,","speak","to","a","few."]
width = 6
s = Solution()
print s.fullJustify(words, width)