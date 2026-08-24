class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0

        for op in operations:
            if op == 'C':
                total -= stack.pop()
            elif op == 'D':
                v = stack[-1] * 2
                stack.append(v)
                total += v
            elif op == '+':
                v = stack[-1] + stack[-2]
                stack.append(v)
                total += v
            else:
                v = int(op)
                stack.append(v)
                total += v

        return total