from collections import Counter
class Solution(object):


    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        if len(s) == 1:
            return [s]
        c = Counter(s)
        odd_appear = [x[0] for x in c.items() if x[1] % 2 == 1]
        res = []
        if len(odd_appear) > 1:
            return []
        elif len(odd_appear) == 1:
            mid = odd_appear[0]
            c[mid] -= 1
            strs = []
            map(lambda x: strs.extend([x[0]] * (x[1]/2)), c.items())
            strs.sort()
            permutations = self.permute(strs)
            # print permutations
            for p in permutations:
                res.append(''.join(p + [mid] + p[::-1]))
        else:
            strs = []
            map(lambda x: strs.extend([x[0]] * (x[1]/2)), c.items())
            strs.sort()
            permutations = self.permute(strs)
            for p in permutations:
                res.append(''.join(p + p[::-1]))
        return res


    def permute(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        i = 0
        while i < len(nums):
            tmp = self.permute(nums[:i] + nums[i+1:])
            for t in tmp:
                # print [nums[i]] + t
                res.append([nums[i]] + t)
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res

s = Solution()

print s.generatePalindromes('aaadddd')