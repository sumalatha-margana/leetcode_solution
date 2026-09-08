class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {}

        for i in range(len(nums)):
            if nums[i] in hash:
                if i - hash[nums[i]] <= k:
                    return True

            hash[nums[i]] = i

        return False
        