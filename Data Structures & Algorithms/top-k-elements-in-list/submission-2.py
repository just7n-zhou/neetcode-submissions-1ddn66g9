class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            # # implement no.1
            # myDict[num] = 1 + myDict.get(num,0)
            # implement no.2
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1
        for n, f in myDict.items():
            freq[f].append(n)

        print(freq)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
