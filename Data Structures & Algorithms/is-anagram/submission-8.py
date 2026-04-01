class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False 
        mySet = set(s)
        for c in mySet:
            if s.count(c) != t.count(c):
                return False 
        return True 