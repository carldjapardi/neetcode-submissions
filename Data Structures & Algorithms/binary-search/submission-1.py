class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = int((left + right)//2)
            mid_val = nums[middle]
            if mid_val == target:
                return middle
            elif mid_val > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1