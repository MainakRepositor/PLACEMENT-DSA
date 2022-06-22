def combinationUtil(arr, n, r, index, data, i):
    # Current combination is ready to be printed,print it
    if(index == r):
        for j in range(r):
            print(data[j], end = " ")
        print(" ")
        return
 
    # When no more elements are there to put in data[]
    if(i >= n):
        return

    # current is included, put next at next location
    data[index] = arr[i]
    combinationUtil(arr, n, r, index + 1, data, i + 1)
     
    # current is excluded,replace it with next 
    combinationUtil(arr, n, r, index, data, i + 1)
 
def printcombination(arr, n, r):
    data = list(range(r))
    combinationUtil(arr, n, r, 0, data, 0)
 
 
# Driver Code
arr = [10, 20, 30, 40, 50] 
r = 3
n = len(arr)
printcombination(arr, n, r)