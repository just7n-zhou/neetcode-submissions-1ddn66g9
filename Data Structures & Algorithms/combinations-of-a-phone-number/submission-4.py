class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitMap = ["", "", "abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

        def backtrack(digitIndex, comb):
            if digitIndex == len(digits):
                res.append("".join(comb))
                return 
            
            digit = int(digits[digitIndex])
            letters = digitMap[digit]

            for i in range(len(letters)):
                comb.append(letters[i])
                backtrack(digitIndex + 1, comb)
                comb.pop()
        
        if len(digits):
            backtrack(0, [])
        
        return res 