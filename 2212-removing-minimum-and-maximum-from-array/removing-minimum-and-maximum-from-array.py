class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return 1

        
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

       
        both_front = right + 1

        
        both_back = n - left

        
        front_and_back = (left + 1) + (n - right)

       
        return min(both_front, both_back, front_and_back)
        