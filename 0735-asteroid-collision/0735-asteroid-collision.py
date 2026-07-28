class Solution:
    def asteroidCollision(self, asteroids):
        stack = []  # here we make empty stack 

        for asteroid in asteroids: # yha hum pta krenge for loop ke through 
            survive = True

            while survive and asteroid < 0 and stack and stack[-1] > 0:
                # here we run while condition within survive and asteroid 

                if stack[-1] < -asteroid:
                    stack.pop()

                elif stack[-1] == -asteroid:
                    stack.pop()
                    survive = False

                else:
                    survive = False

            if survive:
                stack.append(asteroid)

        return stack