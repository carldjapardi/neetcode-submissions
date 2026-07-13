class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_list = 0
        right_list = len(matrix) - 1
        while left_list <= right_list:
            middle_list = int((left_list + right_list)//2)
            if matrix[middle_list][0] <= target and matrix[middle_list][-1] >= target:
                return self.bin_search(matrix[middle_list], target)
            elif matrix[middle_list][0] < target:
                left_list = middle_list + 1
            elif matrix[middle_list][0] > target:
                right_list = middle_list - 1
        return False
    def bin_search(self, arr, targ):
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = int((l+r)//2)
            if arr[m] == targ:
                return True
            elif arr[m] > targ:
                r = m - 1
            else:
                l = m + 1
        return False

