# How it works?
# initialize parenthesis dictionary + stack
# add each opening parenthesis to stack
# if it's not a opening parenthesis and the stack is empty or 
# if the character is not equal to the matching parenthesis of 
# the top parenthesis on the stack
# return False

class Solution:
    def isValid(self, s: str) -> bool:
        parents = {"(": ")", "[": "]", "{": "}"}
        stack = []
        
        for char in s:
            if char in parents:
                stack.append(char)
            elif not stack or char != parents[stack.pop()]:
                return False
        
        if not stack:
            return True
        else:
            return False
