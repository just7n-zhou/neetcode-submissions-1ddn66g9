class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitMap = ["", "", "abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

        def backtrack(numIndex, comb):
            if numIndex == len(digits):
                res.append("".join(comb))
                return 
            digit = int(digits[numIndex])
            strLetter = digitMap[digit]

            for i in range(len(strLetter)):
                comb.append(strLetter[i])
                backtrack(numIndex + 1, comb)
                comb.pop()
        
        if len(digits):
            backtrack(0, [])

        return res 


            