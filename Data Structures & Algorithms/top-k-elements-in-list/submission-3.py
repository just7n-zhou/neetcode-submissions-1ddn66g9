class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # a dict for storing count of each unique number
        myDict = {}

        # a list of list of len(nums), its index i represents frequency of freq[i]
        # higher the index, higher the freq
        freq = [[] for i in range(len(nums) + 1)]

        # store num in myDict, key is num and freq is the value
        for num in nums:
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1
        
        # for each num and count pair
        for n, c in myDict.items():
            # put the num in index of count c inside freq
            freq[c].append(n)
            
        res = [] 
        # starting backwards to check each list of num
        for i in range(len(freq) - 1, 0, -1):
            # if there is a num in list at index i
            for j in freq[i]:
                # append the num in res, otherwise nothing will add to res 
                res.append(j)
            # check len of res to equal target k 
            if len(res) == k:
                    return res
