class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        strings = list(s)
        stack = []

        for char in strings:
            if char in ["(","{","["]:
                stack.append(char)
            elif len(stack) > 0:
                if stack[-1] == "(" and char == ")":
                    stack.pop()
                elif stack[-1] == "[" and char == "]":
                    stack.pop()
                elif stack[-1] == "{" and char == "}":
                    stack.pop()
                else:
                    return False
            else:
                return False
                
        if len(stack) == 0:
            return True
        else: 
            return False