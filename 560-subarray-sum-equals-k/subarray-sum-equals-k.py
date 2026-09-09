class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cs = 0
        ps = {0: 1}
        for num in nums:
            cs += num
            if (cs - k) in ps:
                count += ps[cs - k]
            ps[cs] = ps.get(cs, 0) + 1
        return count
        