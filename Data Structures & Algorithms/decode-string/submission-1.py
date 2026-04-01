class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0  # Our shared "bookmark" in the string
        
        def decode():
            res = ""
            k = 0
            
            while self.i < len(s):
                char = s[self.i]
                
                if char.isdigit():
                    # Update k and move to next char
                    k = k * 10 + int(char)
                    self.i += 1
                    
                elif char == '[':
                    # 1. Skip the '['
                    self.i += 1 
                    # 2. "Someone else solve the inside for me"
                    inner_result = decode()
                    # 3. Repeat that result k times
                    res += k * inner_result
                    k = 0 
                    # Note: self.i is now pointing past the ']' because of the recursive return
                    
                elif char == ']':
                    # 4. We found the end of our current bracket!
                    # Skip the ']' so the parent doesn't see it
                    self.i += 1
                    return res
                    
                else:
                    # 5. Just a regular letter
                    res += char
                    self.i += 1
            
            return res
            
        return decode()