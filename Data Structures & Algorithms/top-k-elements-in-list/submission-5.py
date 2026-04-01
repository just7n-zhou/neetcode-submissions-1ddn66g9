class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            myDict[n] = 1 + myDict.get(n, 0)
        
        for n, c in myDict.items():
            freq[c].append(n) 
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res