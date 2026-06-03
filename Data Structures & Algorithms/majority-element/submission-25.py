class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        maxFreq = res = 0
        for num in nums:
            freq[num] += 1
            if freq[num] > maxFreq:
                res = num 
                maxFreq = freq[num]
        
        return res


