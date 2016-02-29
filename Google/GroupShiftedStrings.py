from collections import defaultdict
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        for s in strings:
            d[self.hash(s)].append(s)
        for key in d.keys():
            d[key].sort()
        return d.values()



    def hash(self, string):
        atoi = 'abcdefghijklmnopqrstuvwxyz'
        nums = [atoi.index(c) for c in list(string)]
        nums = [x - nums[0] for x in nums]
        return ''.join([atoi[i] for i in nums])

        