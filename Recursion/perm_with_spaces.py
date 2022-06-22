def toString(List):
    s = ""
    for x in List:
        if x == '&# 092;&# 048;':
            break
        s += x
    return s

def printPatternUtil(string, buff, i, j, n):
     
    if i == n:
        buff[j] = '&# 092;&# 048;'
        print (toString(buff))
        return
 
    # Either put the character
    buff[j] = string[i]
    printPatternUtil(string, buff, i + 1,
                                 j + 1, n)
 
    # Or put a space followed by next character
    buff[j] = ' '
    buff[j + 1] = string[i]
 
    printPatternUtil(string, buff, i + 1, j + 2, n)

def printPattern(string):
    n = len(string)
 
    buff = [0] * (2 * n)
 
    buff[0] = string[0]
 
    printPatternUtil(string, buff, 1, 1, n)
 
# Driver program
string = "ABCD"
printPattern(string)