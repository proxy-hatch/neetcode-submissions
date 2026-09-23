class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Intuition:
        First thought: we only need to keep track of the max at k, and keep removing and adding as we 
        slide.
        Second thought: we need to keep track of top len(k) max at all times with a min heap
        Third thought: we don't need to know the exact order. We just need O(1) return max, O(1) insert/remove. We can compromise with O(k) return max.

        Corner cases:
        - Input: nums = [1], k = 1 ; Output: [1]
        - Input: nums = [1], k = 1 ; Output: [1]
        - Input: nums = [1, 2], k = 2 ; Output: [2] (k == len(nums) => max of nums)
        """
    
        
        l = 0    
        window_nums = defaultdict(int) # k: element; val: number of element
    

        window_nums_set = set()            
        running_max = None
        result = []
        
        for r, num in enumerate(nums):
            window_nums[num] += 1
            window_nums_set.add(num)
            if running_max is None:
                # recalculate max - lazy
                running_max = max(window_nums_set)
            else:
                running_max = max(running_max, num)
            
            if r - l >= k - 1: # record result and shift window
                result.append(running_max)
                
                to_be_removed = nums[l]
                if window_nums[to_be_removed] == 1: # removed the last one
                    window_nums_set.remove(to_be_removed)
                    # adjust running max
                    if running_max == to_be_removed:
                        running_max = None
                
                window_nums[to_be_removed] -= 1
                l += 1
        
        return result
        
        

    
            

            
            



