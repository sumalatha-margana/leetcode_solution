class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        target = total-x
        if target<0:
            return -1
        if target==0:
            return len(nums)
        left = 0
        c_sum = 0
        max_leng = -1
        for right in range(len(nums)):
            c_sum += nums[right]
            while c_sum>target:
                c_sum -= nums[left]
                left += 1
            if c_sum == target:
                max_leng = max(max_leng, right - left+1)
        if max_leng == -1:
            return -1
        return len(nums) - max_leng                
        