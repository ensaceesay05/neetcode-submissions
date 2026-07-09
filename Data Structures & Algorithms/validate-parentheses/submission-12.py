class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {
        ')': '(',
        ']': '[',
        '}': '{'
        }
        
        stack = []

        for char in s:
            if char in ['{' , '(' , '[']:
                stack.append(char)
            elif char in ['}' , ')' , ']']:
                if not stack or stack.pop() != hashMap[char]:
                    return False
            else:
                return False
        return not stack
