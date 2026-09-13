class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        This problem forces us to be super careful about edge cases:
        1. empty []
        2. single value [0]
        3. duplicate [0, 0]
        4. duplicate interrupt [0, 1, 1, 2]
        """
        """
        # Hash map Solution
        intuition:
        1. create a hash set of k,v = {num, number_of_consecutive}
        2. as we insert new number, we check the neighbours: if both num-1 and num+1 exist, we join their consecutive number + 1 
        3. maintain only values for the keys at the boundaries:
            Left boundary: mp[num - mp[num - 1]] = length
            Right boundary: mp[num + mp[num + 1]] = length
        """
        num_map = defaultdict(int)
        max_consecutive = 0
        for num in nums:
            if num_map[num]: # duplicate
                continue
            
            num_map[num] = num_map[num - 1] + num_map[num + 1] + 1
            num_map[num - num_map[num - 1]] = num_map[num]
            num_map[num + num_map[num + 1]] = num_map[num]
            max_consecutive = max(max_consecutive, num_map[num])
        
        return max_consecutive



        """
        # Sorting Solution
        intuition:
        1. sort from smallest to largest, find max of each consecutive chain
        """
        # nums.sort()
        # print(nums)
      
        # max_consecutive = 0
        # num_consecutive = 1
        
        # for i, num in enumerate(nums):
        #     if i == 0:
        #         prev = num
        #         continue

        #     if num == prev:
        #         continue
        #     if num == prev + 1:
        #         num_consecutive += 1
        #         if i == len(nums) - 1: # end of loop
        #           return max(num_consecutive, max_consecutive)
        #         else:
        #           prev = num
        #     else:
        #         max_consecutive = max(num_consecutive, max_consecutive)
        #         num_consecutive = 1
        
        # return max_consecutive
            

            
            
            