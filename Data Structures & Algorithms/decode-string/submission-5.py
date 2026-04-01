class Solution:
    def decodeString(self, s: str) -> str:
        countStack = []
        stringStack = []
        cur = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                stringStack.append(cur)
                countStack.append(k)
                cur = ""
                k = 0 
            elif c == "]":
                temp = cur 
                cur = stringStack.pop()
                count = countStack.pop()
                cur += temp * count 
            else:
                cur += c 
        
        return cur