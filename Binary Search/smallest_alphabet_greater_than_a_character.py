def nextGreatestAlphabet(alphabets, K):
 
    n = len(alphabets)
    if(K >= alphabets[n-1]):
       return alphabets[0]
    l = 0
    r = len(alphabets) - 1
    ans = -1
    # Take the first element as l and
    # the rightmost element as r
    while (l <= r):
 
        # if this while condition does
        # not satisfy simply return the
        # first element.
        mid = int((l + r) / 2)
 
        if (alphabets[mid] > K):
            r = mid - 1
            ans = mid
        else:
            l = mid + 1
 
    # Return the smallest element
    if (alphabets[ans] < K):
        return alphabets[0]
    else:
        return alphabets[ans]
 
 
# Driver Code
letters = ['A', 'r', 'z']
K = 'z'
 
# Function call
result = nextGreatestAlphabet(letters, K)
print(result)