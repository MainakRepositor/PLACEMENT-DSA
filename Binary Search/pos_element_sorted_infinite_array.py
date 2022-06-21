def binary_search(arr,l,r,x):
 
    if r >= l:
        mid = l+(r-l)//2
 
        if arr[mid] == x:
            return mid
 
        if arr[mid] > x:
            return binary_search(arr,l,mid-1,x)
 
        return binary_search(arr,mid+1,r,x)
 
    return -1
 
# function takes an infinite size array and a key to be
# searched and returns its position if found else -1.
# We don't know size of a[] and we can assume size to be
# infinite in this function.
# NOTE THAT THIS FUNCTION ASSUMES a[] TO BE OF INFINITE SIZE
# THEREFORE, THERE IS NO INDEX OUT OF BOUND CHECKING
def findPos(a, key):
 
    l, h, val = 0, 1, arr[0]
 
    # Find h to do binary search
    while val < key:
        l = h            #store previous high
        h = 2*h          #double high index
        val = arr[h]       #update new val
 
    # at this point we have updated low and high indices,
    # thus use binary search between them
    return binary_search(a, l, h, key)
 
# Driver function
arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
ans = findPos(arr,10)
if ans == -1:
    print ("Element not found")
else:
    print("Element found at index",ans)