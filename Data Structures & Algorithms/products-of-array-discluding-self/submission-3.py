import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        # No division
        intuition:
        1. find the product of all the numbers
        2. divide by number @ index
        """
        zero_count = nums.count(0)
        if zero_count > 1: # always a 0 contributing each cell
            return [0] * len(nums)

        prod = math.prod(x for x in nums if x != 0)

        result = [1] * len(nums)
        for i, num in enumerate(nums):
            if zero_count:
                if num == 0: #  ==1
                    result[i] = prod
                else:
                    result[i] = 0
            else:
                result[i] = prod//num
        
        return result
            


        """
        # No division
        intuition:
        1. incrementally build before_index_product and after_index_product (2n)
        2. product @ i is before_index_product[i] * after_index_product[i]

        """
        # n = len(nums)
        # res = [1] * n
        
        # # 1. Build the prefix products directly into the result array
        # prefix = 1
        # for i in range(n):
        #     res[i] = prefix
        #     prefix *= nums[i]
            
        # # 2. Make a reverse pass, multiplying the suffix product on the fly
        # suffix = 1
        # for i in range(n - 1, -1, -1):
        #     res[i] *= suffix
        #     suffix *= nums[i]
            
        # return res

