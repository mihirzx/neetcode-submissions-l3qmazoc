class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        push = stack.append
        pop = stack.pop
        total = 0

        for op in operations:
            c = op[0]
            if c == '+':
                s = stack[-1] + stack[-2]
                push(s)
                total += s
            elif c == 'D':
                s = stack[-1] * 2
                push(s)
                total += s
            elif c == 'C':
                total -= pop()
            else:
                # handles digits and negative numbers ('-' prefix)
                v = int(op)
                push(v)
                total += v

        return total