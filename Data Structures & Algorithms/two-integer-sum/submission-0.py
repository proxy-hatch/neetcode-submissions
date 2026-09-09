class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, value in enumerate(nums):
            if target - value in seen:
                return sorted([index, seen[target - value]])
            seen[value] = index
        
        # error handle. should not hit
        return False

