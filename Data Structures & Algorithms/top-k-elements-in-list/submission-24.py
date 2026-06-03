class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store num at index that's equal to num's freq 
        freq_map = [[] for _ in range(len(nums) + 1)]
        # track freq of each num 
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        # populate freq_map
        for num, freq in count.items():
            freq_map[freq].append(num)
        
        res = []
        for i in range(len(freq_map) - 1, 0, -1):
            for num in freq_map[i]:
                res.append(num)
                if len(res) == k:
                    return res 
        