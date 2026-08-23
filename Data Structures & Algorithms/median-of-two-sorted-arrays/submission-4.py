# parition from 0 to len(nums)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1)+len(nums2)
        half = (total_length+1)//2
        s_arr, l_arr = nums1, nums2
        if len(nums1) > len(nums2):
            l_arr, s_arr = nums1, nums2
        # bin search partition pos in shorter array
        l = 0
        r = len(s_arr)
        while l <= r:
            s_arr_partition = (l+r)//2 # middle of shorter array
            l_arr_partition = half - s_arr_partition

            l1 = float("-inf") if s_arr_partition == 0 else s_arr[s_arr_partition - 1]
            r1 = float("inf") if s_arr_partition == len(s_arr) else s_arr[s_arr_partition]

            l2 = float("-inf") if l_arr_partition == 0 else l_arr[l_arr_partition - 1]
            r2 = float("inf") if l_arr_partition == len(l_arr) else l_arr[l_arr_partition]

            if l1 > r2: # invalid
                r = s_arr_partition - 1
            elif l2 > r1: #  invalid
                l = s_arr_partition + 1
            else:
                if total_length%2==0:
                    return (max(l1, l2) + min(r1,r2))/2
                else:
                    return max(l1,l2)
            



