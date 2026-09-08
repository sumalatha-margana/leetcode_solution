class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        if n>= 1000:
            count += n-999
        return count    
        