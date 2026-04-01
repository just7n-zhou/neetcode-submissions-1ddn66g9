class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Search every number from 1 to max num in piles 
        # Since with a rate of max num in pile, banana can be finished with 
        # at most len(piles) hours.  
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            # Get total time needed with current rate k 
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)

            # if rate is valid, keep searching for smaller rate, update r pointer 
            if totalTime <= h:
                res = k
                r = k - 1
            # other wise cur k is too small, update l pointer
            else:
                l = k + 1
        return res