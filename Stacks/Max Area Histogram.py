# Stack logic
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack Underflow')
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

# ------------------Stack Ends------------------#

# Nearest smaller to left
def nearest_smaller_to_left(arr):
    stack = Stack()
    result = []

    for i in range(0, len(arr)):
        if stack.is_empty():
            result.append(-1)
            stack.push(arr[i])
        elif not stack.is_empty():
            while(not stack.is_empty() and arr[i] < stack.peek()):
                stack.pop()
            if stack.is_empty():
                result.append(-1)
            else:
                result.append(stack.peek())
            stack.push(arr[i])

    return result

# Nearest Smaller to Right
def nearest_smaller_to_right(arr):
    stack = Stack()
    result = []

    for i in range(len(arr)-1,-1,-1):
        if stack.is_empty():
            result.append(-1)
            stack.push(arr[i])
        elif not stack.is_empty():
            while(not stack.is_empty() and arr[i] < stack.peek()):
                stack.pop()
            if stack.is_empty():
                result.append(-1)
            else:
                result.append(stack.peek())
            stack.push(arr[i])
    result.reverse()
    return result

#--------------------------#

# Area calculation Logic
def max_area_histogram(arr):
    NSL = nearest_smaller_to_left(arr)
    NSR = nearest_smaller_to_right(arr)

    width = []
    for i in range(0, len(arr)):
        width.append(NSR[i] - NSL[i] - 1)
    
    area = []
    for i in range(0, len(arr)):
        area.append(arr[i]*width[i])
    
    return max(area)


# Print statement
arr = [6,2,5,4,5,1,6]
print(max_area_histogram(arr))