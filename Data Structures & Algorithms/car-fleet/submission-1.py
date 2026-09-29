class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleets = 0
        stack = []

        cars = sorted(zip(position, speed), reverse = True)

        for pos, speed in cars:
            time = (target - pos) / speed

            if not stack or time > stack[-1]:
                stack.append(time)
            elif time <= stack[-1]:
                continue



        return len(stack)