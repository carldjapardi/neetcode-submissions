class Solution:
    def search(self, nums, target):
        def bin_search(l, r, targ):
            while l <= r:
                m = (l+r)//2
                if nums[m] == targ:
                    return m
                elif nums[m] > targ:
                    r = m - 1
                else:
                    l = m + 1
            return -1 
        def min_search(arr):
            left, right = 0, len(nums)-1
            while left < right:
                mid = (left+right)//2
                if nums[left] < nums[right]:
                    return left
                elif nums[right] > nums[mid]:
                    right = mid
                elif nums[right] < nums[mid]:
                    left = mid + 1
            return left
        min_idx = min_search(nums)
        if nums[min_idx] == target:
            return min_idx
        if min_idx == 0:
            return bin_search(0, len(nums)-1, target)
        min_left = nums[0]
        max_left = nums[min_idx-1]
        if (target >= min_left) and (target <= max_left):
            return bin_search(0, min_idx-1, target)
        else:
            return bin_search(min_idx+1, len(nums)-1, target) 

