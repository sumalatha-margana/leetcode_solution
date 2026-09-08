class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash = {}
        for ch in s:
            if ch in hash:
                hash[ch]+=1
            else:
                hash[ch]=1
        for ch in t:
            if ch not in hash:
                return ch
            hash[ch]-=1
            if hash[ch]<0:
                return ch                

        