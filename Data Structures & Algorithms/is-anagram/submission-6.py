class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        setS = set(s)
        for num in setS:
            if s.count(num) != t.count(num):
                return False 
        return True