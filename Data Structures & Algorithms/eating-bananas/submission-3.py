class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1 and piles[0] < h:
            return 1
        lower = sum(piles)//h
        upper = max(piles)
        while lower != upper:
            i = 0
            time = h
            k = (lower + upper)//2
            while i < len(piles):
                exactNumberOfTimes = piles[i]/k if (piles[i]%k==0) else ((piles[i]//k)+1) 
                time -= exactNumberOfTimes
                i += 1
            if time < 0: 
                lower = k+1
            if time >= 0:
                upper = k
        return lower