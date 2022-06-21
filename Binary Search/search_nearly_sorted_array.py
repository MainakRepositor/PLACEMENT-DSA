def binarySearch(arr, l, r, x):
 
    if (r >= l):
         
        mid = int(l + (r - l) / 2)
         
        # If the element is present at one
        # of the middle 3 positions
        if (arr[mid] == x): return mid
        if (mid > l and arr[mid - 1] == x):
            return (mid - 1)
        if (mid < r and arr[mid + 1] == x):
            return (mid + 1)
             
        # If element is smaller than mid, then
        # it can only be present in left subarray
        if (arr[mid] > x):
            return binarySearch(arr, l, mid - 2, x)
         
        # Else the element can only
        # be present in right subarray
        return binarySearch(arr, mid + 2, r, x)
 
    # We reach here when element
    # is not present in array
    return -1
 
# Driver Code
arr = [3, 2, 10, 4, 40]
n = len(arr)
x = 4
result = binarySearch(arr, 0, n - 1, x)
if (result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)