class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [] # store indices with monotomically increasing height
        max_area = 0
        for i in range(len(heights)+1):
            # >= is a space optimization. We are extra-considering scenarios with consecutive heights, but this way we don't grow the stack size, causing dynamic reallocation
            while stack and (i == len(heights) or heights[stack[-1]] >= heights[i]):
                popped = stack.pop()
                width = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, width*heights[popped])
            
            stack.append(i)
            
        return max_area
