class Solution:
    def isValid(self, s: str) -> bool:
        # Quick length check - odd length strings can't be valid
        if len(s) % 2:
            return False
            
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif not stack or stack.pop() != c:
                return False
        return not stack
