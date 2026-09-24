class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[0]*n
        l=0
        r=n-1
        position = n-1
        while l<=r:
            if abs(nums[l]) > abs(nums[r]):
                ans[position] = nums[l] * nums[l]
                l += 1
            else:
                ans[position] = nums[r] * nums[r]
                r -= 1
            position -= 1
        return ans            
