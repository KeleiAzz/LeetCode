__author__ = 'keleigong'
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        x = len(nums1) + len(nums2) - m - n
        nums1.insert(0, float('-inf'))
        # nums1.append(float('inf'))
        # nums1[m+1] = float('inf')
        if x != 0:
            nums1[m+1] = float('inf')
        if len(nums2) > 0:
            while i < m + n + 1 and j < n:
                # if nums1[i] <= nums2[j] <= nums1[i+1]:
                #     nums1.insert(i + 1, nums2[j])
                #     j += 1
                if nums1[i] >= nums2[j]:
                    nums1.insert(i, nums2[j])
                    j += 1
                else:
                    i += 1
        nums1.pop(0)
        for i in range(x):
            nums1.pop()


s = Solution()
nums1 = [1, 0]
m = 1
nums2 = [2]
n = 1
print s.merge(nums1, m, nums2, n)