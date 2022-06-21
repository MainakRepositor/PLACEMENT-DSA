def findMinDiff(arr, n):
 
    # Sort array in non-decreasing order
    arr = sorted(arr)
 
    # Initialize difference as infinite
    diff = 10**20
 
    # Find the min diff by comparing adjacent
    # pairs in sorted array
    for i in range(n-1):
        if arr[i+1] - arr[i] < diff:
            diff = arr[i+1] - arr[i]
 
    # Return min diff
    return diff
 
# Driver code
arr = [1, 5, 3, 19, 18, 25]
n = len(arr)
print("Minimum difference is " + str(findMinDiff(arr, n)))