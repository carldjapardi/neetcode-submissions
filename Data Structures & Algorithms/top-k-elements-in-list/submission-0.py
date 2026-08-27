class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # { number : #OfOcc } ; track = [ top k occ ]
        num_occ = {}
        for i in nums:
            num_occ[i] = num_occ.get(i, 0) + 1
        top_k = []
        for i in num_occ:
            insert_idx = 0
            while ( insert_idx < len(top_k) 
                    and num_occ[top_k[insert_idx]] < num_occ[i] ):
                insert_idx += 1
            top_k.insert(insert_idx, i)
            if len(top_k) > k:
                top_k.pop(0)
        return top_k