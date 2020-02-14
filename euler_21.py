#euler 21


limit = 10000

def amicable (x):
    x = int (x)
    sum = 0
    for i in range (1,x):
        if x %i == 0 :
            sum = sum + i
    return sum

a8r = 0
for i in range (1, limit + 1):
    temp = amicable (i)
    if amicable(temp) == i and i < temp:
        a8r = a8r + i + temp 

print (a8r)
        
    
