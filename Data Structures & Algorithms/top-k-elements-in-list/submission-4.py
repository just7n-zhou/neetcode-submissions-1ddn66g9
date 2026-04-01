class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1
        
        for n, c in myDict.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
