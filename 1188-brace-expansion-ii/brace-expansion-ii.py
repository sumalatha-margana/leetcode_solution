class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(i):
            result = {""}
            total = set()
            while i < len(expression) and expression[i] != '}':
                if expression[i] == ',':
                    total |= result
                    result = {""}
                    i += 1
                    continue
                if expression[i] == '{':
                    part, i = parse(i + 1)
                else:
                    part = {expression[i]}
                    i += 1
                new_result = set()
                for a in result:
                    for b in part:
                        new_result.add(a + b)
                result = new_result
            total |= result
            return total, i + 1
        result, _ = parse(0)
        return sorted(result)