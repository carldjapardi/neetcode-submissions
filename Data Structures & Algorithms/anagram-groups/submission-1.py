class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # intuition: { [count_letters] : [word1, word2] ... }
        cl_map = {}
        for s in strs:
            # count letters
            arr = [0]*26
            for l in s:
                arr[ord(l)-97]+=1
            arr = tuple(arr)
            # append word as map value
            if arr not in cl_map:
                cl_map[arr] = []
            cl_map[arr].append(s)
        return list(cl_map.values())
            



    
