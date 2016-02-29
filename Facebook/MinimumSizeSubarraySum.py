class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if sum(nums) < s:
            return 0
        cur_sum = 0
        min_length = float('INF')
        i = 0
        j = 0
        while i < len(nums) and j < len(nums):
            if cur_sum < s:
                while cur_sum < s and j < len(nums):
                    cur_sum += nums[j]
                    j += 1
                if cur_sum >= s:
                    while cur_sum >= s:
                        cur_sum -= nums[i]
                        i += 1
                    print cur_sum, nums[i-1:j]
                    min_length = min(j - i + 1, min_length)
                    # cur_sum -= nums[i]
                    # i += 1
                else:
                    print min_length
                    return min_length
            else:
                cur_sum -= nums[i]
                i += 1
        print min_length
        return min_length


s = Solution()

s.minSubArrayLen(11, [1, 2, 3, 4 ,5])