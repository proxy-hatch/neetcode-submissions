class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        
        stack = deque() # elements of (tmp: int, index: int)

        for i, tmp in enumerate(temperatures):
            while len(stack) and stack[-1][0] < tmp:
                top = stack.pop()
                result[top[1]] = i - top[1]
            
            stack.append((tmp, i))
        
        return result
        

            
