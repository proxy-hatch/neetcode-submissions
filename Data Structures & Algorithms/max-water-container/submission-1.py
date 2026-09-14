class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        intuition: traverse the search space to find
        max{(r - l) * max{h[r], h[l]}}
        increment l and decrement r at the same time, skip if h[l] < prev h[l] and  h[r] < prev h[r]
        2 pointers: go inward on the side that's shorter
        """
        i = max_area = 0
        j = len(heights) - 1
        while i < j:
            max_area = max(max_area, (j - i) * min(heights[i], heights[j]))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1 # move either side when i = j
        
        return max_area
