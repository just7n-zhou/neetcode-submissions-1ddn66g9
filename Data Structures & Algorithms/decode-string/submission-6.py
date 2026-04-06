class Solution:
    def decodeString(self, s: str) -> str:
        stringStack = []
        countStack = []
        cur = "" # substring before next []
        k = 0 # count before next []

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                stringStack.append(cur) # keep track of current substring 
                countStack.append(k) # keep track of current count 
                cur = "" # reset cur to track substring in current []
                k = 0 # reset k to track count in current []
            elif c == "]":
                temp = cur # keep track of finished substring in this []
                cur = stringStack.pop() # substring from before this [] begin
                count = countStack.pop() # count from before this [] begin
                cur += temp * count 
            else:
                cur += c # a normal string 
        
        return cur 