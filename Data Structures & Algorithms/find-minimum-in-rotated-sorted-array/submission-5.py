class Solution:
    # intuition: advance l when nums[m] > nums[r], 
    # nums[m] < nums[r] will stop at r = m until the point its sorted
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            m = (l+r)//2
            if nums[m] < nums[r]: r = m
            elif nums[m] > nums[r]: l = m+1
        return nums[r]
