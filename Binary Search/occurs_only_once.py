def search(arr, n) :
 
    XOR = 0
    for i in range(n) :
        XOR = XOR ^ arr[i]
 
    print("The required element is", XOR)
 
# Driver code
arr = [ 1, 1, 2, 4, 4, 5, 5, 6, 6 ]
Len = len(arr)
 
search(arr, Len)