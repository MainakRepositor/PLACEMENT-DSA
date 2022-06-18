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

# Problem solving logic
def nearest_greater_to_left(arr):
    stack = Stack()
    result = []

    for i in range(0, len(arr)):
        if stack.is_empty():
            result.append(-1)
            stack.push(arr[i])
        elif not stack.is_empty():
            while(not stack.is_empty() and arr[i] > stack.peek()):
                stack.pop()
            if stack.is_empty():
                result.append(-1)
            else:
                result.append(stack.peek())
            stack.push(arr[i])

    return result

#-----------Problem logic ends---------------#

#Output and function call
arr = [1, 6, 4, 10, 2, 5]
print(nearest_greater_to_left(arr))