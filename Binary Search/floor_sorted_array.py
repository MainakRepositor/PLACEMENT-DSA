def floorSearch(arr, low, high, x):
 
    # If low and high cross each other
    if (low > high):
        return -1
 
    # If last element is smaller than x
    if (x >= arr[high]):
        return high
 
    # Find the middle point
    mid = int((low + high) / 2)
 
    # If middle point is floor.
    if (arr[mid] == x):
        return mid
 
    # If x lies between mid-1 and mid
    if (mid > 0 and arr[mid-1] <= x
                and x < arr[mid]):
        return mid - 1
 
    # If x is smaller than mid, 
    # floor must be in left half.
    if (x < arr[mid]):
        return floorSearch(arr, low, mid-1, x)
 
    # If mid-1 is not floor and x is greater than
    # arr[mid],
    return floorSearch(arr, mid + 1, high, x)
 
 
# Driver Code
arr = [1, 2, 4, 6, 10, 12, 14]
n = len(arr)
x = 7
index = floorSearch(arr, 0, n-1, x)
 
if (index == -1):
    print("Floor of", x, "doesn't exist\
                    in array ", end = "")
else:
    print("Floor of", x, "is", arr[index])