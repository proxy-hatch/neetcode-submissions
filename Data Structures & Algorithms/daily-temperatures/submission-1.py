class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        
        stack = deque() # stack of indices

        for i, tmp in enumerate(temperatures):
            while len(stack) and temperatures[stack[-1]] < tmp:
                top = stack.pop()
                result[top] = i - top
            
            stack.append(i)
        
        return result
            
