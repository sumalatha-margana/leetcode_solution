class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod=10**9+7

        distinct_subsequence=1

        last = [0]*26

        for ch in s:

            i= ord(ch)-ord('a')
            new_ds = 2*distinct_subsequence-last[i]

            last[i]=distinct_subsequence

            distinct_subsequence=new_ds % mod

        return(distinct_subsequence - 1)%mod
            
        