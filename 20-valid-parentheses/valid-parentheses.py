class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        
        stack = []
        
        for char in s:
            if char == "[" or char == "(" or char == "{":
                stack.append(char)
            elif char == "]" or char == ")" or char == "}":
                if len(stack) <= 0: return False
                lastBracket = stack.pop()
                
                if   lastBracket == "[" and char != "]": return False
                elif lastBracket == "(" and char != ")": return False
                elif lastBracket == "{" and char != "}": return False
        
        return True if len(stack) == 0 else False