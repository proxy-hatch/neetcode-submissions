class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Intuition (Optimized):
        One pass of sliding window, keep track of max.
        Problem: sometimes a max value fall out of the window and we need the 2nd max, or 3rd, and so on.
        Solution: Use Max heap

        Corner cases:
        - Input: nums = [1], k = 1 ; Output: [1]
        - Input: nums = [1], k = 1 ; Output: [1]
        - Input: nums = [1, 2], k = 2 ; Output: [2] (k == len(nums) => max of nums)
        """
        max_heap = []
        result = []

        for r, num in enumerate(nums):
            # Push (value, index) into the max heap
            heapq.heappush_max(max_heap, (num, r))

            # Once our window size is at least k
            if r >= k - 1:
                # If the max element's index is outside our current window,it's stale.
                # Keep popping until the top of the heap is inside the window.
                while max_heap[0][1] <= r - k:
                    heapq.heappop_max(max_heap)

                # The top element is now guaranteed to be valid and the maximum
                result.append(max_heap[0][0])

        return result

        """
        Intuition:
        One pass of sliding window, keep track of max.
        Problem: sometimes a max value fall out of the window and we need the 2nd max. To avoid keeping track of this, we simply recompute.

        Corner cases:
        - Input: nums = [1], k = 1 ; Output: [1]
        - Input: nums = [1], k = 1 ; Output: [1]
        - Input: nums = [1, 2], k = 2 ; Output: [2] (k == len(nums) => max of nums)
        """
        # l = 0
        # window_nums = defaultdict(int) # k: element; val: number of element

        # window_nums_set = set()
        # running_max = None
        # result = []

        # for r, num in enumerate(nums):
        #     window_nums[num] += 1
        #     window_nums_set.add(num)
        #     if running_max is None:
        #         # recalculate max - lazy
        #         running_max = max(window_nums_set)
        #     else:
        #         running_max = max(running_max, num)

        #     if r - l >= k - 1: # record result and shift window
        #         result.append(running_max)

        #         to_be_removed = nums[l]
        #         if window_nums[to_be_removed] == 1: # removed the last one
        #             window_nums_set.remove(to_be_removed)
        #             # adjust running max
        #             if running_max == to_be_removed:
        #                 running_max = None

        #         window_nums[to_be_removed] -= 1
        #         l += 1

        # return result
