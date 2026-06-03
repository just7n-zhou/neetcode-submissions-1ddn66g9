class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0 : 1}
        prefix = 0 

        res = 0
        for num in nums:
            prefix += num 
            if prefix - k in prefix_map:
                res += prefix_map[prefix - k]
            prefix_map[prefix] = prefix_map.get(prefix, 0) + 1
        
        return res 