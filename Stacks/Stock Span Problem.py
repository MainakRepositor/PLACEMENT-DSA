# Stock Span Problem

def span(rates):
    stockspan = []
    stack = []

    stockspan.append(1)
    stack.append(0)

    for i in range(1,len(rates)):
        while rates[i] > rates[stack[-1]]:
            stack.pop()

            if len(stack) == 0:
                break

        if len(stack) > 0:
            stockspan.append(i - stack[-1])
        else:
            stockspan.append(i+1)
        
        stack.append(i)
    return stockspan

rates = [31,27,14,21,30,22]
stockspan = span(rates)
print(stockspan)


