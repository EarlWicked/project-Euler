# tringle divs

divisor = 0

i = 0
num = 0

#creating the triangle
while True:
    
    
    i= i + 1
    num =  num + i
    divisor = 0
   
   
    for j in range (1, num+1):
        if num % j == 0 :
            divisor = divisor +1
           
    

    
    if (divisor) >= 200:
        break

print (num)
