class Solution(object):

    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        one = -1
        two = -1
        for i in range(1, len(nums)):
            if one == -1 and two == -1 and nums[i] > nums[i-1]:
                one = i - 1
                two = i
            elif nums[i] > nums[i-1]:
                if nums[i] > nums[two]:
                    return True
                if nums[i-1] > nums[one]:
                    return True
                if nums[i] < nums[one]:
                    one = i - 1
                    two = i
                else:
                    two = i
        return False
