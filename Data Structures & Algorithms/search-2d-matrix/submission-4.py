class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_list, r_list = 0, len(matrix)-1
        while l_list <= r_list:
            m_list = (l_list + r_list)//2
            first_e = matrix[m_list][0]
            last_e = matrix[m_list][-1]
            if last_e < target:
                l_list = m_list + 1
            elif first_e > target:
                r_list = m_list - 1
            else:
                return self.bin_search(matrix[m_list], target)
        return False
    def bin_search(self, arr, targ):
        l, r = 0, len(arr)-1
        while l <= r:
            m = (l+r)//2
            if arr[m] == targ:
                return True
            elif arr[m] > targ:
                r = m - 1
            else:
                l = m + 1
        return False

