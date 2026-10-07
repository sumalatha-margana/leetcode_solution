class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(x):
            balance = 0
            for ch in x:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0
        level = {s}
        while True:
            result = []
            for x in level:
                if isValid(x):
                    result.append(x)
            if result:
                return result
            next_level = set()
            for x in level:
                for i in range(len(x)):
                    if x[i] == '(' or x[i] == ')':
                        next_level.add(x[:i] + x[i + 1:])
            level = next_level
        