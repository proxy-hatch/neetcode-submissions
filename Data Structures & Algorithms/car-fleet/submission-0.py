class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Intuition:
        1. sort by position (i.e., distance to target) desc (closest to further to target)
        2. use a stack of fleets:
            - if next car is faster, it joins the previous fleet (dropped)
            - if next car is slower, it becomes its own fleet (pushed onto stack)
        3. count stack len
        """
        # sorted() auto-uses 1st key, skips 2nd arg "key=lambda x: x[0]"
        cars = tuple(sorted(zip(position, speed), reverse=True))

        fleet_stack = [] # list(time_to_target)

        for car in cars:
            time_to_target = (target - car[0]) / car[1]

            if not fleet_stack or time_to_target > fleet_stack[-1]:
                fleet_stack.append(time_to_target)
            
        return len(fleet_stack)
