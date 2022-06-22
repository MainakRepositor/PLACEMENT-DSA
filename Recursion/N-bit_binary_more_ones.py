def printRec(number, extraOnes, remainingPlaces):
 
    # if number generated
    if (0 == remainingPlaces):
        print(number, end=" ")
        return
 
    # Append 1 at the current number and
    # reduce the remaining places by one
    printRec(number + "1", extraOnes + 1,
             remainingPlaces - 1)
 
    # If more ones than zeros, append 0 to
    # the current number and reduce the
    # remaining places by one
    if (0 < extraOnes):
        printRec(number + "0", extraOnes - 1,
                 remainingPlaces - 1)
 
 
def printNums(n):
    str = ""
    printRec(str, 0, n)
 
 
# Driver Code
if __name__ == '__main__':
    n = 4
      
    # Function call
    printNums(n)