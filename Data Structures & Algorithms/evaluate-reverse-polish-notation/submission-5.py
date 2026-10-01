class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Intuition:
        1. single stack. 
            - should always begin with 2 operands
            - if we see a number, put it on the stack
            - if we see an operator, pop 2 numbers from the stack and compute. Put result back on stack
        """
        def compute(operand1: int, operand2: int, operator: str):
            match operator:
                case "+":
                    return  operand1 + operand2
                case "-":
                    return  operand1 - operand2
                case "*":
                    return  operand1 * operand2
                case "/":
                    return int(operand1 / operand2)
                case _:
                    raise ValueError(f"invalid {operator=}")

        def is_integer(string_to_check):
            try:
                int(string_to_check)
                return True
            except ValueError:
                return False

        if len(tokens) == 1 and is_integer(tokens[0]):
            return int(tokens[0])
        elif len(tokens) < 2:
            raise ValueError("Not enough operands.")

        stack = deque()
        for token in tokens:        
            if is_integer(token):
                stack.append(int(token))
                continue

            if len(stack) < 2:
                raise ValueError("Not enough operands.")
            operand2 = stack.pop()
            operand1 = stack.pop()

            stack.append(compute(operand1, operand2, token))
        
        return stack.pop()

