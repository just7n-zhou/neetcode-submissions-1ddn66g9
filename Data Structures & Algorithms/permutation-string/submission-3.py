class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # populate count1 with s1 
        count1 = defaultdict(int)
        for c in s1:
            count1[c] += 1

        # need is num of unique char in s1 that must be matched in s2
        need = len(count1)
        for i in range(len(s2)):
            count2, cur = defaultdict(int), 0 
            # extend substring with starting i index
            for j in range(i, len(s2)):
                count2[s2[j]] += 1
                # if count2 has more char j than count1, it won't work
                if count1.get(s2[j],0) < count2[s2[j]]:
                    break 
                # if count for current char matches in both hashmap
                if count1.get(s2[j],0) == count2[s2[j]]:
                    # increase cur 
                    cur += 1
                # if cur is equal to the needed num of char, we found a valid permutation
                if cur == need:
                    return True 
        
        return False 