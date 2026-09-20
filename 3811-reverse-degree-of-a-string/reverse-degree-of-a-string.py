class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            val = ord(s[i])-ord('a')+1
            reverse = 27-val
            ans+=reverse*(i+1)
        return ans    

        