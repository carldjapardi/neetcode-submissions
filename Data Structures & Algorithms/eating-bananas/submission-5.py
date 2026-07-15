class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # intuition: reducing search space of rate (mid)
        # Finding exact number of times is trivially arith
        lower = 1
        upper = max(piles)
        while lower < upper:
            time = h
            mid = (lower + upper)//2
            for p in piles:
                exactNumberOfTimes = math.ceil(p/mid)
                time -= exactNumberOfTimes
                if time < 0:
                    break
            if time < 0: 
                lower = mid+1
            else:
                upper = mid
        return lower