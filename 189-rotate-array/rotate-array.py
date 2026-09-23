class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        result = [0] * n
        for i in range(n):
            result[(i + k) % n] = nums[i]
        for i in range(n):
            nums[i] = result[i]