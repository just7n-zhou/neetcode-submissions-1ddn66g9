class Solution:
    def decodeString(self, s: str) -> str:
        # We use an iterator so all recursive calls 
        # share the same "progress" through the string
        it = iter(s)
        
        def decode():
            res = ""
            k = 0
            
            while True:
                try:
                    char = next(it)
                except StopIteration:
                    break
                
                if char.isdigit():
                    # Build the multiplier (e.g., '1' then '2' becomes 12)
                    k = k * 10 + int(char)
                
                elif char == '[':
                    # Dive! Solve the inner bracket
                    inner_str = decode()
                    res += k * inner_str
                    k = 0 # Reset multiplier for the next part
                
                elif char == ']':
                    # Return the solved inner part to the caller
                    return res
                
                else:
                    # Just a normal letter
                    res += char
            
            return res
            
        return decode()