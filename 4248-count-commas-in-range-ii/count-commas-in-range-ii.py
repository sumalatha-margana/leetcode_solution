class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        start = 1000
        commas = 1

        while start <= n:
            end = start * 1000 - 1

            if n < end:
                count = n - start + 1
            else:
                count = end - start + 1

            ans += count * commas

            start = start * 1000
            commas += 1

        return ans
        
        