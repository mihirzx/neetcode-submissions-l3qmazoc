class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t in "+-*/":     # it's an operator
                a = stack.pop()
                b = stack.pop()
                if t == "+":
                    stack.append(b + a)
                elif t == "-":
                    stack.append(b - a)
                elif t == "*":
                    stack.append(b * a)
                elif t == "/":
                    stack.append(int(b / a))
            else:               # it's a number
                stack.append(int(t))
        
        return stack[-1]