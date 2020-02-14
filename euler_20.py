#euler 20


def factorio(l):
    fa = 1
    l=int(l)
    if l!= 0:
        for i in range (l,1,-1):
            fa = fa* i

    return fa


def a8r(x):
    sum = 0
    while x!= 0:      
        sum = sum + int(x % 10) 
        x = int(x/10) 
      
    return sum


g = input("Enter your number : ")
temp = factorio(g)
temp = a8r(temp)

# 

print ("a8roisma einai ", temp)
