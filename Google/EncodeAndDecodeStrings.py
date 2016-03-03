class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        res = ''
        for s in strs:
            res += '%08d' % len(s)
            res += s
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        if s == '':
            return []
        res = []
        while s:
            length = int(s[:8])
            tmp = s[8:8+length]
            res.append(tmp)
            s = s[8+length:]
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))