class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        maxLength = 0
        prefixSum = 0
        s = list(s)
        t = list(t)
        l=0
        for r in range(len(s)):
            prefixSum += abs(ord(s[r])-ord(t[r]))
            while prefixSum > maxCost:
                prefixSum -= abs(ord(s[l])-ord(t[l]))
                l+=1
            maxLength = max(maxLength, r-l+1)
        return maxLength