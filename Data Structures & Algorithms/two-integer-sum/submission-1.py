class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_sum = {} # value_needed : idx
        for i in range(len(nums)):
            if nums[i] not in check_sum:
                check_sum[target - nums[i]] = i
            else:
                return [check_sum[nums[i]], i]