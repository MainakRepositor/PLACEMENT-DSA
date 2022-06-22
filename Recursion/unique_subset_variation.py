from collections import deque
def printPowerSet(S, i, out=deque()):
 
    # if all elements are processed, print the current subset
    if i < 0:
        print(list(out))
        return
 
    # include the current element in the current subset and recur
    out.append(S[i])
    printPowerSet(S, i - 1, out)
 
    # backtrack: exclude the current element from the current subset
    out.pop()
 
    # remove adjacent duplicate elements
    while i > 0 and S[i] == S[i - 1]:
        i = i - 1
 
    # exclude the current element from the current subset and recur
    printPowerSet(S, i - 1, out)
 
 
# Wrapper over `printPowerSet()` function
def findPowerSet(S):
 
    # sort the set
    S.sort()
 
    # print the power set
    printPowerSet(S, len(S) - 1)
 
 
if __name__ == '__main__':
 
    S = [1, 3, 1]
 
    findPowerSet(S)