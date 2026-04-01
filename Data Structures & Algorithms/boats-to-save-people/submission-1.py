class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        m = max(people)
        count = [0] * (m + 1)
        for p in people:
            count[p] += 1
        
        index, i = 0, 1
        while index < len(people):
            while count[i] == 0:
                i += 1
            people[index] = i 
            count[i] -= 1
            index += 1
        
        res, l, r = 0, 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1 
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        
        return res 