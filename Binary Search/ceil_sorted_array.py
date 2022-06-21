def ceilSearch(arr, low, high, x):
 
    # If x is smaller than or equal to the first element,
    # then return the first element */
    if x <= arr[low]:
        return low
 
    # If x is greater than the last element, then return -1 */
    if x > arr[high]:
        return -1 
  
    # get the index of middle element of arr[low..high]*/
    mid = (low + high)/2;  # low + (high - low)/2 */
  
    # If x is same as middle element, then return mid */
    if arr[mid] == x:
        return mid
 
    # If x is greater than arr[mid], then either arr[mid + 1]
    # is ceiling of x or ceiling lies in arr[mid+1...high] */
    elif arr[mid] < x:
        if mid + 1 <= high and x <= arr[mid+1]:
            return mid + 1
        else:
            return ceilSearch(arr, mid+1, high, x)
  
    # If x is smaller than arr[mid], then either arr[mid]
    # is ceiling of x or ceiling lies in arr[low...mid-1] */  
    else:
        if mid - 1 >= low and x > arr[mid-1]:
            return mid
        else:
            return ceilSearch(arr, low, mid - 1, x)
  
# Driver program to check above functions */
arr = [1, 2, 8, 10, 10, 12, 19]
n = len(arr)
x = 20
index = ceilSearch(arr, 0, n-1, x);
 
if index == -1:
    print ("Ceiling of %d doesn't exist in array "% x)
else:
    print ("ceiling of %d is %d"%(x, arr[index]))