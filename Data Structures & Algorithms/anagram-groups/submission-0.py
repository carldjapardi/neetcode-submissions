class Solution:
    def make_count_let(self, word):
        arr = [0]*26
        for i in word:
            arr[ord(i)-97] += 1
        return tuple(arr)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # { [count_letters] : [word1, word2] ... }
        count_letters = {}
        for i in strs:
            arr = self.make_count_let(i)
            if arr not in count_letters:
                count_letters[arr] = []
            count_letters[arr].append(i)
        return list(count_letters.values())
            



    
