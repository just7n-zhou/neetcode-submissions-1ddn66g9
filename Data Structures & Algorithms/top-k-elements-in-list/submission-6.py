class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # a dict to keep num n and their count c 
        myDict = {}
        # a list to store num at index of their count
        freq = [[] for i in range(len(nums) + 1)] 
        # loop through nums 
        for n in nums:
            # if n in myDict, increase count by 1
            if n in myDict:
                myDict[n] += 1
            # else keep it in dict 
            else:
                myDict[n] = 1
        # put n in freq at index equal to n's count c 
        for n, c in myDict.items():
            freq[c].append(n) 

        res = [] 
        # loop though freq backwards
        for i in range(len(freq) - 1, -1, -1):
            # # 
            for num in freq[i]:
                res.append(num)
            if len(res) == k:
                return res