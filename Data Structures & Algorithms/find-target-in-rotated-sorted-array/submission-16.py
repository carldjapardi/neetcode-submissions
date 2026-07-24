class Solution:
    def search(self, nums, target):
        l = 0 
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] <= nums[r]: # m<->r sorted
                if nums[m] < target <= nums[r]: l = m+1
                else: r = m-1
            elif nums[m] > nums[r]: # l<->m sorted
                if nums[l] <= target < nums[m]: r = m-1
                else: l = m+1
        return -1 

