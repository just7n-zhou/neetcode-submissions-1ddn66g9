class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = [] # keep track of index of "(" and ")"
        res = list(s) # make string a list for easy modification

        for i, char in enumerate(s):
            # append index to stack if cur char is an opening
            if char == "(":
                stack.append(i)
            # elif encouter closing 
            elif char == ")":
                # if stack is not empty, pop from stack 
                # since we found closing matching an opening in stack
                if stack:
                    stack.pop()
                # if stack is empty, this closing is invalid, remove it 
                else:
                    res[i] = ""
        
        # In case stack if not empty, meaning there are extra opening 
        # that's not matched by an closing, also remove it in res 
        while stack:
            res[stack.pop()] = ""
        
        # return res in a string 
        return "".join(res)