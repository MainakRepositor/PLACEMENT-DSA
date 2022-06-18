from math import dist
from turtle import distance


def maxWater(height):
    stack = []
    n = len(height)
    ans = 0
    for i in range(n):
        while (len(stack)!=0 and (height[stack[-1]] < height[i])):
            pop_height = height[stack[-1]]
            stack.pop()
            if len(stack) == 0:
                break
            
            distance  = i - stack[-1] - 1
            min_height = min(height[stack[-1]],height[i]) - pop_height

            ans += distance * min_height
        stack.append(i)
    return ans 

arr = [0,1,0,2,1,0,1,3,2,1,2,1]
print(maxWater(arr))