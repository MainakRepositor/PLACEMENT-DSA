def josephus(n, k):
 
    if (n == 1):
        return 1
    else:
 
        return (josephus(n - 1, k) + k-1) % n + 1

n = 14
k = 2
 
print("The chosen place is ", josephus(n, k))