class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitMap = ["", "", "abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

        def backtrack(numIndex, comb): # numIndex track which digit currently at
            # when numIndex reach the pos after the last index, collect result
            if numIndex == len(digits):
                res.append("".join(comb))
                return 
            # get our current digit and its strs
            digit = int(digits[numIndex])
            strLetter = digitMap[digit]
            # every digit is constant 3 letters 
            # so backtrack for every letter 
            for i in range(len(strLetter)):
                comb.append(strLetter[i])
                backtrack(numIndex + 1, comb)
                comb.pop()
        
        if len(digits):
            backtrack(0, [])

        return res 


            