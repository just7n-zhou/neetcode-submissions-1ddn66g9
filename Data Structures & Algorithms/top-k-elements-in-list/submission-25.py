class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = [[]for _ in range(len(nums) + 1)] # store frequency of num with index
        count = defaultdict(int) # count frequency of each num 

        # populate count 
        for num in nums:
            count[num] += 1
        # populate freq_map
        for num, freq in count.items():
            freq_map[freq].append(num)
        
        res = [] 
        # iterate through freq_map array backward, start with max freq
        for i in range(len(freq_map) - 1, -1, -1):
            # iterate through each subarray in freq_map
            for num in freq_map[i]:
                # add num in the subarray to res 
                res.append(num)
                # return res when its length reaches k 
                if len(res) == k:
                    return res 
                
