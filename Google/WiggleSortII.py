class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # tmp = nums[:]
        # nums.sort()
        mid = self.r_select(nums, 0, len(nums)-1, len(nums)/2)
        ans = [mid] * len(nums)
        if len(nums) % 2 == 0:
            l = len(nums) - 2
            r = 1
            for i in range(len(nums)):
                if nums[i] < mid:
                    ans[l] = nums[i]
                    l -= 2
                elif nums[i] > mid:
                    ans[r] = nums[i]
                    r += 2
        else:
            l = 0
            r = len(nums) - 2
            for i in range(len(nums)):
                if nums[i] < mid:
                    ans[l] = nums[i]
                    l += 2
                elif nums[i] > mid:
                    ans[r] = nums[i]
                    r -= 2
        for i in range(len(nums)):
            nums[i] = ans[i]
    
    def r_select(self, nums, l, r, i):
        if l == r:
            return nums[i]
        else:
            q = self.r_partition(nums, l, r)
            k = q - l + 1
            if k == i:
                return nums[q]
            elif k > i:
                return self.r_select(nums, l, q - 1, i)
            else:
                return self.r_select(nums, q + 1, r, i - k)
                
    def r_partition(self, nums, l, r):
        x = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] < x:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[r] = nums[r], nums[i+1]
        return i + 1

nums = [1,2,3,5,3,2,6,1,2,3,7,8,4,2,3]
s = Solution()
print s.r_select(nums, 0, len(nums) - 1, len(nums)/2)
print sorted(nums)



    # def r_partition(self, nums, l, r, rank):
    #     left, right = l, r
    #     now = nums[left]
    #     while left < right:
    #         while left < right and nums[right] >= now:
    #             right -= 1
    #         nums[left] = nums[right]
    #         while left < right and nums[left] < now:
    #             left += 1
    #         nums[right] = nums[left]
    #     if left - l == rank:
    #         return now
    #     elif left - l > rank:
    #         return self.r_partition(nums, l, right - 1, rank)
    #     else:
    #         return self.r_partition(nums, left + 1, r, rank - (left - l + 1))