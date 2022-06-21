def orderagnosticBS(arr, l, r, x):
 
    isAscending = arr[l] < arr[r]

    while l <= r:
        mid = l + (r - l)//2
        if (arr[mid] == x):
            return mid

        if (isAscending == True):
            if (arr[mid] < x):
                l = mid + 1
            else:r = mid - 1
        
        else:
            if (arr[mid] > x):
                l = mid+1
            else:  r = mid - 1

    return -1

arr = [50,40,5,3,2]
n = len(arr)
x = 1
print(orderagnosticBS(arr,0,n-1,x))
