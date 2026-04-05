class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0 

        l = maxFreq = 0 

        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            # get the most frequent char in current window
            maxFreq = max(maxFreq, count[s[r]])

            # window is valid as long as:
            # window size – count of the most frequent character ≤ k
            # if window invalid, thrink from left 
            while (r - l + 1) - maxFreq > k:
                # reduce left char freq in count by 1
                count[s[l]] -= 1
                l += 1
            
            # when window is valid, update res 
            res = max(res, r - l + 1)
        
        return res 