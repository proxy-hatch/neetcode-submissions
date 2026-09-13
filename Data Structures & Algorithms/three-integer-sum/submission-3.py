class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        INTUITION: 2 pointers
        1. sort the list
        2. iterate thru the loop: select 1st number
        2. at each traversal: select leftmost and rightmost after this number, and search for sum = 0
        """
        nums.sort()
        result = []

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and nums[i-1] == num:
                continue

            l = i+1
            r = len(nums)-1
            while l < r:
                if l > i + 1 and nums[l] == nums[l-1]:
                    l += 1
                    continue
                
                sum = num + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
        
        return result


        """
        WRONG intuition:
        1. Build a collection of 2 sums - {k: sum, v: [[index1, index2], ...]}
        2. Check if the third number can contribute to 0 (the same 2 sums cannot be used twice)
        """
        
        # two_sums = defaultdict(list)
        # for i, num_1 in enumerate(nums):
        #     for offset_j, num_2 in enumerate(nums[i + 1 :]):
        #         two_sums[num_1 + num_2].append((i, i + 1 + offset_j))
        
        # removed_pair = None
        # result = []
        # for i, num in enumerate(nums):
        #     if -num in two_sums:
        #         for pair in two_sums[-num]:
        #             if i not in pair:
        #                 two_sums[-num].remove(pair)
        #                 result.append([nums[i], nums[pair[0]], nums[pair[1]]])
        #                 break
        
        # return result
                    
                    
