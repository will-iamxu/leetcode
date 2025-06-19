class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                elif stack[-1] == "(" and ch != ")":
                    return False
                elif stack[-1] == "[" and ch != "]":
                    return False
                elif stack[-1] == "{" and ch != "}":
                    return False
                else:
                    stack.pop()
        if stack:
            return False 
        return True