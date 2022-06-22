def printSubsequence(input, output):
    # Base Case
    if len(input) == 0:
        print(output, end=' ')
        return
    
    printSubsequence(input[1:], output+input[0])

    printSubsequence(input[1:], output)
 
output = ""
input = "abcd"
 
printSubsequence(input, output)