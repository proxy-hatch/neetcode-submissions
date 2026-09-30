class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque() # list is possible too, but it is implemented as a dynamic array, while deque is implemented as a doubley LL
        def is_matching(opening:str, closing:str)->bool:
            match opening:
                    case '(':
                        return closing == ')'
                    case '{':
                        return closing == '}'
                    case '[':
                        return closing == ']'
                    case _:
                        return False

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not len(stack) or not is_matching(stack.pop(), char):
                    return False
        
        return len(stack) == 0

