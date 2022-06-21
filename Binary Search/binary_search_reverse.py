# Binary Search in the reversed array

def binarySearchRev(arr, n, x):
    l = 0
    r = n
    while (l <= r):
        mid = l + (r-l)//2
        if (x == arr[mid]):
            return mid

        elif (x < arr[mid]):  # Only this condition changes [x < arr[mid]]
            l = mid + 1

        else: r = mid - 1

    return -1

    
arr = [5,4,3,2,1]
n = len(arr)
x = 6
print(binarySearchRev(arr,n,x)) 
