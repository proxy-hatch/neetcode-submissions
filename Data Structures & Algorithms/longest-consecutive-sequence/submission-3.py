class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        intuition:
        1. sort from smallest to largest, find max of each consecutive chain

        This problem forces us to be super careful about edge cases:
        1. empty []
        2. single value [0]
        3. duplicate [0, 0]
        4. duplicate interrupt [0, 1, 1, 2]
        """
        count = len(nums)
        if count < 2:
            return count
        
        nums.sort()
        print(f"{nums=}")
      
        max_consecutive = 0
        num_consecutive = 1
        for i in range(1, count):
            num = nums[i]
            if num == nums[i-1]:
                continue
            if num == nums[i-1] + 1:
                num_consecutive += 1
            else:
                max_consecutive = max(num_consecutive, max_consecutive)
                num_consecutive = 1
        return max(num_consecutive, max_consecutive)
            
            