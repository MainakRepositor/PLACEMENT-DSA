def countRotations(arr):
    n = len(arr)
    start = 0
    end = n-1
 
    # Finding the index of minimum of the array
    # index of min would be equal to number to rotation
    while start<=end:
        mid = start+(end-start)//2
         
        # Calculating the previous(prev)
        # and next(nex) index of mid
        prev = (mid-1+n)%n
        nex = (mid+1)%n
 
        # Checking if mid is minimum
        if arr[mid]<arr[prev]\
           and arr[mid]<=arr[nex]:
          return mid
       
        # if not selecting the unsorted part of array
        elif arr[mid]<arr[start]: end = mid-1
        elif arr[mid]>arr[end]: start = mid+1
        else: return 0
 
# Driver code
arr = [15, 18, 2, 3, 6, 12]
n = len(arr)
print(countRotations(arr))